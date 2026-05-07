"""
fetch-youtube-captions.py — Long-form YouTube auto-caption helper for /learn skill.

Takes a YouTube URL (typically watch?v=... long-form, > 5 min) and returns
JSON {transcript, transcript_timestamped, publisher, title, url, source_date,
duration, chapters, vtt_path, meta_path} on stdout.

Sibling to transcribe-url.py. Same invocation contract (py -3.11), same exit
codes for shared failures, same JSON-on-stdout idiom. Difference: this helper
uses YouTube auto-captions via yt-dlp, NOT Whisper. For 5h of audio Whisper
takes 4-8h CPU; auto-captions take seconds.

INVOCATION (from /learn or manual testing):
    py -3.11 "Optimus Academy/tools/fetch-youtube-captions.py" <URL> [--out-dir <dir>]

Default --out-dir: "Optimus Academy/tools/working/<video-id>/"

Idempotent: if both <video-id>.en.vtt and <video-id>.meta.json already exist
in --out-dir, the script skips fetching and re-emits JSON from disk. Enables
resumability after a crash or interrupt.

DEPENDENCIES (verified installed at build time):
    - Python 3.11 via py -3.11 launcher
    - yt-dlp Python module (used directly, not the .exe shim)

NO API key, no Whisper, no ffmpeg dependency. yt-dlp's auto-caption mode pulls
the YouTube-served VTT directly — no audio download, no transcoding.

EXIT CODES:
    0 — success; stdout has valid JSON
    1 — runtime error during fetch; stderr has details
    3 — yt-dlp Python module missing for active interpreter
    6 — wrong Python version (must be 3.11)
    7 — no English auto-captions available for this video

OUT-OF-SCOPE failure modes — handled by caller, not this helper:
    - No captions in any language → exit 7. Caller decides whether to fall back
      to Whisper (slow, separate helper), request transcript from creator, or
      capture from chapter notes only.
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

# Preflight 1: Python version
if sys.version_info[:2] != (3, 11):
    print(
        f"ERROR: this script requires Python 3.11. Active interpreter is "
        f"{sys.version_info.major}.{sys.version_info.minor}. "
        f"Invoke via: py -3.11 \"Optimus Academy/tools/fetch-youtube-captions.py\" <URL>",
        file=sys.stderr,
    )
    sys.exit(6)

# Preflight 2: yt-dlp Python module
try:
    import yt_dlp
except ImportError:
    print(
        "ERROR: yt-dlp Python module not installed for the active Python. "
        "Run: py -3.11 -m pip install yt-dlp",
        file=sys.stderr,
    )
    sys.exit(3)


VTT_TIMING_RE = re.compile(
    r"(\d{2}:\d{2}:\d{2}\.\d{3})\s+-->\s+(\d{2}:\d{2}:\d{2}\.\d{3})"
)
VTT_TAG_RE = re.compile(r"<[^>]+>")
VTT_BRACKET_TIME_RE = re.compile(r"<\d{2}:\d{2}:\d{2}\.\d{3}>")


def timestamp_to_seconds(ts: str) -> float:
    """'00:01:23.456' → 83.456"""
    h, m, s = ts.split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


def parse_vtt(vtt_text: str) -> tuple[str, list[dict]]:
    """Parse a VTT file body into (clean_transcript, timestamped_segments).

    Returns:
        clean_transcript: deduplicated plain text of all caption text
        timestamped_segments: list of {"start": float, "end": float, "text": str}

    YouTube auto-captions emit rolling captions where each cue contains the
    previous cue's text plus a new word at the end. We dedupe by collapsing
    consecutive identical or near-identical cue text into the longest version.
    """
    segments: list[dict] = []
    blocks = re.split(r"\n\n+", vtt_text.strip())

    for block in blocks:
        lines = block.strip().split("\n")
        if not lines:
            continue

        timing_line_idx = None
        for i, line in enumerate(lines):
            if VTT_TIMING_RE.search(line):
                timing_line_idx = i
                break

        if timing_line_idx is None:
            continue

        timing_match = VTT_TIMING_RE.search(lines[timing_line_idx])
        if not timing_match:
            continue
        start = timestamp_to_seconds(timing_match.group(1))
        end = timestamp_to_seconds(timing_match.group(2))

        text_lines = lines[timing_line_idx + 1:]
        text = "\n".join(text_lines).strip()
        text = VTT_BRACKET_TIME_RE.sub("", text)
        text = VTT_TAG_RE.sub("", text)
        text = re.sub(r"\s+", " ", text).strip()

        if not text:
            continue

        segments.append({"start": start, "end": end, "text": text})

    deduped = _dedupe_rolling_captions(segments)
    transcript = " ".join(seg["text"] for seg in deduped)
    transcript = re.sub(r"\s+", " ", transcript).strip()
    return transcript, deduped


def _dedupe_rolling_captions(segments: list[dict]) -> list[dict]:
    """Collapse rolling-caption duplicates.

    YouTube auto-cap emits a new cue every ~1-2 seconds where each cue contains
    the previous cue's tail + a new word or two. The naive concatenation
    duplicates 90%+ of the text. Strategy: when cue N+1's text starts with
    cue N's text (prefix match), keep cue N+1 and drop cue N. When they
    diverge, keep both.
    """
    if not segments:
        return []

    out: list[dict] = []
    for seg in segments:
        if out and seg["text"].startswith(out[-1]["text"]):
            out[-1] = {
                "start": out[-1]["start"],
                "end": seg["end"],
                "text": seg["text"],
            }
        elif out and out[-1]["text"].startswith(seg["text"]):
            continue
        else:
            out.append(dict(seg))
    return out


def fetch_metadata(url: str) -> dict:
    """yt-dlp --print-json equivalent: extract info without downloading anything."""
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "noprogress": True,
        "skip_download": True,
        "writesubtitles": False,
        "writeautomaticsub": False,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    return info


def fetch_captions(url: str, out_dir: Path, video_id: str) -> Path:
    """Fetch English auto-captions and write VTT to disk. Returns the VTT path.

    Raises FileNotFoundError if no English auto-captions are available — caller
    should map to exit code 7.
    """
    out_template = str(out_dir / f"{video_id}.%(ext)s")
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "noprogress": True,
        "skip_download": True,
        "writesubtitles": False,
        "writeautomaticsub": True,
        "subtitleslangs": ["en", "en-US", "en-GB", "en-orig"],
        "subtitlesformat": "vtt",
        "outtmpl": out_template,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(url, download=True)

    for candidate in (
        out_dir / f"{video_id}.en.vtt",
        out_dir / f"{video_id}.en-US.vtt",
        out_dir / f"{video_id}.en-GB.vtt",
        out_dir / f"{video_id}.en-orig.vtt",
    ):
        if candidate.exists():
            return candidate
    raise FileNotFoundError(
        f"No English auto-caption VTT was written for video {video_id}. "
        "yt-dlp returned without error but no .en[.*].vtt file landed in "
        f"{out_dir}. Captions may be disabled by the creator."
    )


def format_duration(seconds: int | float | None) -> str:
    if seconds is None:
        return "unknown"
    seconds = int(seconds)
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    if h > 0:
        return f"{h}h {m:02d}min"
    return f"{m}min {s:02d}s"


def normalize_youtube_url(info: dict, fallback_url: str) -> str:
    """Return canonical youtube.com/watch?v=ID form."""
    video_id = info.get("id")
    if video_id:
        return f"https://www.youtube.com/watch?v={video_id}"
    return fallback_url


def normalize_chapters(chapters: list[dict] | None) -> list[dict]:
    if not chapters:
        return []
    out = []
    for ch in chapters:
        out.append({
            "start": float(ch.get("start_time", 0)),
            "end": float(ch.get("end_time", 0)) if ch.get("end_time") is not None else None,
            "title": ch.get("title", "").strip(),
        })
    return out


def fetch(url: str, out_dir: Path) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)

    info = fetch_metadata(url)
    video_id = info.get("id") or "unknown"
    canonical_url = normalize_youtube_url(info, url)

    meta_path = out_dir / f"{video_id}.meta.json"
    vtt_path = out_dir / f"{video_id}.en.vtt"

    if vtt_path.exists() and meta_path.exists():
        with meta_path.open("r", encoding="utf-8") as fp:
            info = json.load(fp)
    else:
        with meta_path.open("w", encoding="utf-8") as fp:
            json.dump(info, fp, ensure_ascii=False, indent=2, default=str)
        try:
            actual_vtt = fetch_captions(url, out_dir, video_id)
            if actual_vtt != vtt_path:
                actual_vtt.replace(vtt_path)
        except FileNotFoundError as exc:
            raise CaptionsUnavailable(str(exc)) from exc

    with vtt_path.open("r", encoding="utf-8") as fp:
        vtt_text = fp.read()

    transcript, timestamped = parse_vtt(vtt_text)

    upload_date_raw = info.get("upload_date")
    if upload_date_raw and isinstance(upload_date_raw, str) and len(upload_date_raw) == 8:
        source_date = f"{upload_date_raw[:4]}-{upload_date_raw[4:6]}-{upload_date_raw[6:8]}"
    else:
        source_date = "unknown"

    return {
        "transcript": transcript,
        "transcript_timestamped": timestamped,
        "publisher": (
            info.get("uploader")
            or info.get("channel")
            or info.get("uploader_id")
            or "unknown"
        ),
        "title": info.get("title") or "untitled",
        "url": canonical_url,
        "source_date": source_date,
        "duration": format_duration(info.get("duration")),
        "duration_seconds": int(info.get("duration") or 0),
        "chapters": normalize_chapters(info.get("chapters")),
        "vtt_path": str(vtt_path.resolve()),
        "meta_path": str(meta_path.resolve()),
        "video_id": video_id,
        "transcript_word_count": len(transcript.split()),
    }


class CaptionsUnavailable(Exception):
    """Raised when no English auto-captions exist for the video."""


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fetch YouTube auto-captions for long-form video.",
    )
    parser.add_argument("url", help="YouTube video URL (watch?v=... form preferred)")
    parser.add_argument(
        "--out-dir",
        default=None,
        help=(
            "Output directory for VTT + meta.json. Default: "
            "Optimus Academy/tools/working/<video-id>/"
        ),
    )
    args = parser.parse_args()

    url = args.url.strip()
    if not url:
        print("ERROR: empty URL.", file=sys.stderr)
        return 1

    if args.out_dir:
        out_dir = Path(args.out_dir)
    else:
        try:
            info = fetch_metadata(url)
            video_id = info.get("id") or "unknown"
        except Exception as exc:
            print(f"ERROR: metadata fetch failed: {exc}", file=sys.stderr)
            return 1
        out_dir = Path("Optimus Academy") / "tools" / "working" / video_id

    try:
        result = fetch(url, out_dir)
    except CaptionsUnavailable as exc:
        print(
            f"ERROR: {exc} "
            "Manual subs may exist on the creator's channel — pass a different "
            "--sub-lang to yt-dlp manually if you know the language code. "
            "Whisper fallback is out of scope for this helper.",
            file=sys.stderr,
        )
        return 7
    except yt_dlp.utils.DownloadError as exc:
        print(f"ERROR: yt-dlp download failed: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"ERROR: caption fetch failed: {exc.__class__.__name__}: {exc}", file=sys.stderr)
        return 1

    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
