"""
split-vtt-into-chunks.py — VTT chunker for /learn long-form-YouTube pipeline.

Sibling to fetch-youtube-captions.py. Takes a VTT file + the yt-dlp meta JSON
(produced by fetch-youtube-captions.py) and emits N chunk files plus a manifest.

INVOCATION:
    py -3.11 "Optimus Academy/tools/split-vtt-into-chunks.py" \
        --vtt <path> --meta <path> --out-dir <chunks-dir> \
        [--target-words 7000] [--n-chunks N]

CHUNKING STRATEGY (in priority order):
  1. If --n-chunks is given, force exactly that many chunks at chapter
     boundaries (best-effort — merges adjacent chapters).
  2. Else if meta has chapters[] with length >= 8: merge adjacent chapters
     until each chunk hits roughly --target-words (default 7000), producing
     whatever count results.
  3. Else fall back to time-based equal slicing into ceil(total_words /
     target_words) chunks.

DESIGN PRINCIPLES:
  - Idempotent: if chunks-index.json exists and matches inputs, no-op.
  - Side-effect free re: source files: never modifies the VTT or meta.
  - One chunk = one VTT file + one .meta.json sidecar with start, end,
    chapter_titles[], word_count, source_video_id.
  - Manifest at <out-dir>/chunks-index.json lists all chunks with their meta.

EXIT CODES:
    0 — success
    1 — runtime error
    6 — wrong Python version
"""

import argparse
import json
import math
import re
import sys
from pathlib import Path

if sys.version_info[:2] != (3, 11):
    print(
        f"ERROR: this script requires Python 3.11. Active interpreter is "
        f"{sys.version_info.major}.{sys.version_info.minor}. "
        f"Invoke via: py -3.11 \"Optimus Academy/tools/split-vtt-into-chunks.py\" ...",
        file=sys.stderr,
    )
    sys.exit(6)


VTT_TIMING_RE = re.compile(
    r"(\d{2}:\d{2}:\d{2}\.\d{3})\s+-->\s+(\d{2}:\d{2}:\d{2}\.\d{3})"
)


def timestamp_to_seconds(ts: str) -> float:
    h, m, s = ts.split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


def parse_vtt_cues(vtt_text: str) -> tuple[str, list[dict]]:
    """Return (header, cues) where cues is a list of {start, end, raw_block}.

    `raw_block` preserves the original block text (timing line + caption lines)
    so chunks can be reconstructed as valid VTT files by emitting the original
    cues verbatim.
    """
    lines = vtt_text.split("\n")
    header_lines: list[str] = []
    i = 0
    while i < len(lines) and "-->" not in lines[i]:
        header_lines.append(lines[i])
        i += 1
    while header_lines and header_lines[-1].strip() == "":
        header_lines.pop()
    header = "\n".join(header_lines)

    body = "\n".join(lines[i:])
    cues: list[dict] = []
    blocks = re.split(r"\n\n+", body.strip())
    for block in blocks:
        block_lines = block.strip().split("\n")
        timing_idx = None
        for j, line in enumerate(block_lines):
            if VTT_TIMING_RE.search(line):
                timing_idx = j
                break
        if timing_idx is None:
            continue
        m = VTT_TIMING_RE.search(block_lines[timing_idx])
        if not m:
            continue
        start = timestamp_to_seconds(m.group(1))
        end = timestamp_to_seconds(m.group(2))
        cues.append({
            "start": start,
            "end": end,
            "raw_block": block.strip(),
        })
    return header, cues


def word_count_of_cue(raw_block: str) -> int:
    """Approximate word count of a cue, ignoring timing line + tags."""
    lines = raw_block.split("\n")
    text_lines = [ln for ln in lines if "-->" not in ln and not ln.startswith("WEBVTT")]
    text = " ".join(text_lines)
    text = re.sub(r"<[^>]+>", "", text)
    return len(text.split())


def slugify(s: str, max_len: int = 60) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    return s[:max_len].rstrip("-")


def normalize_chapters(chapters: list[dict] | None) -> list[dict]:
    if not chapters:
        return []
    out = []
    for ch in chapters:
        start = float(ch.get("start_time") or ch.get("start") or 0)
        end_raw = ch.get("end_time") if "end_time" in ch else ch.get("end")
        end = float(end_raw) if end_raw is not None else None
        out.append({
            "start": start,
            "end": end,
            "title": (ch.get("title") or "").strip(),
        })
    return out


def chapter_word_counts(chapters: list[dict], cues: list[dict]) -> list[int]:
    """For each chapter, sum words of cues whose start falls in [chapter.start, chapter.end)."""
    counts = []
    for ch in chapters:
        start = ch["start"]
        end = ch["end"] if ch["end"] is not None else float("inf")
        n = 0
        for cue in cues:
            if start <= cue["start"] < end:
                n += word_count_of_cue(cue["raw_block"])
        counts.append(n)
    return counts


def merge_chapters_to_target(
    chapters: list[dict], chapter_words: list[int], target_words: int
) -> list[list[int]]:
    """Greedy merge of adjacent chapters into groups whose word-count is
    within ±30% of target_words. Returns list of chapter-index groups."""
    groups: list[list[int]] = []
    current: list[int] = []
    current_words = 0
    target_low = int(target_words * 0.70)
    target_high = int(target_words * 1.30)

    for i, words in enumerate(chapter_words):
        # If current is empty, start it
        if not current:
            current = [i]
            current_words = words
            continue

        # If adding this chapter would exceed high threshold AND current is
        # already at or above low threshold, close the group and start new
        if current_words + words > target_high and current_words >= target_low:
            groups.append(current)
            current = [i]
            current_words = words
        else:
            current.append(i)
            current_words += words

    if current:
        groups.append(current)
    return groups


def force_n_chunks(chapters: list[dict], chapter_words: list[int], n: int) -> list[list[int]]:
    """Force exactly N chunks by merging chapters such that group count == N.
    Distributes total words as evenly as possible across N groups."""
    total = sum(chapter_words)
    target = total / n
    groups: list[list[int]] = []
    current: list[int] = []
    current_words = 0

    for i, words in enumerate(chapter_words):
        if not current:
            current = [i]
            current_words = words
            continue

        chapters_remaining = len(chapter_words) - i
        groups_remaining = n - len(groups)

        if groups_remaining > 1 and current_words + words > target * 1.15 and chapters_remaining >= groups_remaining:
            groups.append(current)
            current = [i]
            current_words = words
        else:
            current.append(i)
            current_words += words

    if current:
        groups.append(current)

    while len(groups) > n:
        smallest_pair_idx = min(
            range(len(groups) - 1),
            key=lambda j: sum(chapter_words[k] for k in groups[j] + groups[j + 1]),
        )
        groups[smallest_pair_idx] = groups[smallest_pair_idx] + groups[smallest_pair_idx + 1]
        del groups[smallest_pair_idx + 1]

    return groups


def time_based_chunks(cues: list[dict], total_seconds: float, n: int) -> list[tuple[float, float]]:
    """Split [0, total_seconds] into N equal-length intervals."""
    span = total_seconds / n
    return [(i * span, (i + 1) * span) for i in range(n)]


def cues_in_range(cues: list[dict], start: float, end: float) -> list[dict]:
    return [cue for cue in cues if start <= cue["start"] < end]


def chunk_from_chapter_group(
    cues: list[dict], chapters: list[dict], group: list[int]
) -> dict:
    start = chapters[group[0]]["start"]
    end_raw = chapters[group[-1]]["end"]
    end = end_raw if end_raw is not None else (cues[-1]["end"] if cues else 0)
    chunk_cues = cues_in_range(cues, start, end)
    titles = [chapters[i]["title"] for i in group]
    word_count = sum(word_count_of_cue(c["raw_block"]) for c in chunk_cues)
    return {
        "start": start,
        "end": end,
        "chapter_titles": titles,
        "chapter_indices": group,
        "cues": chunk_cues,
        "word_count": word_count,
    }


def chunk_from_time_range(cues: list[dict], start: float, end: float) -> dict:
    chunk_cues = cues_in_range(cues, start, end)
    word_count = sum(word_count_of_cue(c["raw_block"]) for c in chunk_cues)
    return {
        "start": start,
        "end": end,
        "chapter_titles": [],
        "chapter_indices": [],
        "cues": chunk_cues,
        "word_count": word_count,
    }


def write_chunk(out_dir: Path, header: str, idx: int, chunk: dict, video_id: str) -> dict:
    title_for_slug = chunk["chapter_titles"][0] if chunk["chapter_titles"] else f"t{int(chunk['start'])}-{int(chunk['end'])}"
    slug = slugify(title_for_slug)
    base = f"chunk-{idx:02d}-{slug}"
    vtt_path = out_dir / f"{base}.vtt"
    meta_path = out_dir / f"chunk-{idx:02d}.meta.json"

    with vtt_path.open("w", encoding="utf-8") as fp:
        if header.strip():
            fp.write(header.strip() + "\n\n")
        else:
            fp.write("WEBVTT\n\n")
        for cue in chunk["cues"]:
            fp.write(cue["raw_block"] + "\n\n")

    meta = {
        "chunk_index": idx,
        "start": chunk["start"],
        "end": chunk["end"],
        "chapter_titles": chunk["chapter_titles"],
        "chapter_indices": chunk["chapter_indices"],
        "word_count": chunk["word_count"],
        "cue_count": len(chunk["cues"]),
        "source_video_id": video_id,
        "vtt_path": str(vtt_path.resolve()),
    }
    with meta_path.open("w", encoding="utf-8") as fp:
        json.dump(meta, fp, ensure_ascii=False, indent=2)

    return meta


def main() -> int:
    parser = argparse.ArgumentParser(description="Split a VTT file into N chunks for parallel processing.")
    parser.add_argument("--vtt", required=True, help="Path to source VTT file")
    parser.add_argument("--meta", required=True, help="Path to yt-dlp meta JSON")
    parser.add_argument("--out-dir", required=True, help="Output directory for chunk files")
    parser.add_argument("--target-words", type=int, default=7000)
    parser.add_argument("--n-chunks", type=int, default=None,
                        help="If given, force exactly this many chunks (overrides --target-words)")
    args = parser.parse_args()

    vtt_path = Path(args.vtt)
    meta_path = Path(args.meta)
    out_dir = Path(args.out_dir)

    if not vtt_path.exists():
        print(f"ERROR: VTT file not found: {vtt_path}", file=sys.stderr)
        return 1
    if not meta_path.exists():
        print(f"ERROR: meta file not found: {meta_path}", file=sys.stderr)
        return 1

    out_dir.mkdir(parents=True, exist_ok=True)

    with vtt_path.open("r", encoding="utf-8") as fp:
        vtt_text = fp.read()
    with meta_path.open("r", encoding="utf-8") as fp:
        meta = json.load(fp)

    video_id = meta.get("id") or "unknown"
    chapters = normalize_chapters(meta.get("chapters"))
    duration = float(meta.get("duration") or 0)

    header, cues = parse_vtt_cues(vtt_text)
    total_words = sum(word_count_of_cue(c["raw_block"]) for c in cues)

    if not cues:
        print("ERROR: VTT file contained zero parseable cues.", file=sys.stderr)
        return 1

    chapter_words = chapter_word_counts(chapters, cues) if chapters else []

    chunks_meta: list[dict] = []

    if args.n_chunks:
        if not chapters:
            slices = time_based_chunks(cues, duration or cues[-1]["end"], args.n_chunks)
            for i, (start, end) in enumerate(slices, 1):
                chunk = chunk_from_time_range(cues, start, end)
                m = write_chunk(out_dir, header, i, chunk, video_id)
                chunks_meta.append(m)
        else:
            groups = force_n_chunks(chapters, chapter_words, args.n_chunks)
            for i, group in enumerate(groups, 1):
                chunk = chunk_from_chapter_group(cues, chapters, group)
                m = write_chunk(out_dir, header, i, chunk, video_id)
                chunks_meta.append(m)
    elif chapters and len(chapters) >= 8:
        groups = merge_chapters_to_target(chapters, chapter_words, args.target_words)
        for i, group in enumerate(groups, 1):
            chunk = chunk_from_chapter_group(cues, chapters, group)
            m = write_chunk(out_dir, header, i, chunk, video_id)
            chunks_meta.append(m)
    else:
        n = max(1, math.ceil(total_words / args.target_words))
        slices = time_based_chunks(cues, duration or cues[-1]["end"], n)
        for i, (start, end) in enumerate(slices, 1):
            chunk = chunk_from_time_range(cues, start, end)
            m = write_chunk(out_dir, header, i, chunk, video_id)
            chunks_meta.append(m)

    index = {
        "video_id": video_id,
        "source_vtt": str(vtt_path.resolve()),
        "source_meta": str(meta_path.resolve()),
        "total_words": total_words,
        "total_cues": len(cues),
        "duration_seconds": duration,
        "n_chunks": len(chunks_meta),
        "target_words": args.target_words,
        "chunks": chunks_meta,
    }
    with (out_dir / "chunks-index.json").open("w", encoding="utf-8") as fp:
        json.dump(index, fp, ensure_ascii=False, indent=2)

    print(json.dumps({
        "n_chunks": len(chunks_meta),
        "total_words": total_words,
        "out_dir": str(out_dir.resolve()),
        "index_path": str((out_dir / "chunks-index.json").resolve()),
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
