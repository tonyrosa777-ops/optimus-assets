# Plan — Capture 5h "Hermes + OpenClaw AI Agents Course" (Julian Goldie) via /learn

## Context

**Source.** A 5-hour YouTube course shared via X tweet:
- YouTube: <https://www.youtube.com/watch?v=MpItrr4OYf0>
- Tweet: <https://x.com/JulianGoldieSEO/status/2051918932970483944>
- Title: "FREE Hermes + OpenClaw AI Agents Course: Build & Automate ANYTHING"
- Publisher: Julian Goldie SEO · Duration: ~5h · Source-date: 2026-05-06 (per user)

**Why this is non-trivial.** /learn's standard short-form path runs Whisper locally on downloaded audio. For 5 hours of audio that's 4-8+ hours CPU time on this machine, no resumability, no chunking, no caching — confirmed by reading `Optimus Academy/tools/transcribe-url.py`. We must use a different transcript path AND parallelize the note extraction, otherwise this consumes a full day of one-session synchronous work.

**User intent.** Maximum-detail capture ("every minute of valuable information") organized as ONE Obsidian concept per the explicit instruction "make sure its all organized in one concept in obsidian." User authorized `/loop` if needed; we recommend single-session parallel agents instead.

**Outcome.** ONE comprehensive daily H2 capture (raw, ~15-30k words across 10 chapters) + ONE atomic concept file (~2-4k words, distilled) + 2 bridges (Hermes new, OpenClaw append) + optional Tier-3/Tier-4 lessons bridge surfaced from synthesis. Crash-safe via state file.

---

## Follow-ups (DEFERRED — for future sessions reading the archived plan)

**These are intentional deferrals, not omissions. A future session re-reading this plan must pick them up.**

1. **Update `/learn` command routing table at `C:\Users\Anthony\.claude\commands\learn.md`** to auto-route long-form YouTube (≥ 5 min) through `Optimus Academy/tools/fetch-youtube-captions.py` instead of WebFetch. Currently the routing table sends `youtube.com/watch?v=...` to WebFetch — which works for short videos but missed half the chapters on this 5h video and has no chunking story for transcripts > ~10k words. Defer until: (a) we've used the new helper on 1-2 more long-form videos and confirmed it's robust, (b) chunking strategy is proven beyond just chapter-pinned + 30-min fallback. Trigger: third successful long-form capture or first time WebFetch fails for a long-form video the user wanted captured.

2. **Update `/learn` command to encode the parallel-chunker fanout pattern** (Phase 3 of this plan) as a documented sub-flow for any source with transcript > ~10k words. Right now /learn assumes a single-pass capture — long-form needs the fanout pattern to stay tractable. Defer until: the pattern works cleanly here AND on at least one more 60+ min source.

3. **Graduate the manifest format** (`chunks-index.json`, `hermes-openclaw-status.md`) into a documented contract in `Optimus Academy/tools/README.md` if it survives 2-3 captures unchanged. If it mutates each run, it's still proto — don't lock it in.

These belong in this plan file (not in `Optimus Academy/tools/README.md` yet) precisely because they're conditional on this run going well. The archive copy of this plan at `Optimus Academy/tools/hermes-openclaw-5h-capture-plan.md` is the canonical record of the deferral — when re-reading it months later, treat the items above as live work.

---

## Strategy at a glance

```
Phase 0  Update .gitignore FIRST (before any working files exist) ── 1 commit
Phase 1a Build fetch-youtube-captions.py helper (permanent)    ── ~20 min
Phase 1b Run helper → fetch VTT + meta JSON                     ── seconds
Phase 2  Build split-vtt-into-chunks.py + run → 10 chunks      ── ~15 min build, seconds run
Phase 3  Fanout: 10 parallel chunker agents (1 chunk each)     ── ~10 min wall, parallel
Phase 4  Synthesize 10 notes → 1 daily H2 + 1 concept file     ── orchestrator, ~10 min
Phase 5  Bridges (hermes CREATE, openclaw APPEND, conditional) ── orchestrator
Phase 6  Commit + push                                          ── git
Phase 7  Archive working files                                  ── move, not delete
```

Total wall time: ~60 min. The +35 min for permanent helpers (vs inline one-off) pays back on the first re-use.

---

## Phase 0 — Update .gitignore (BEFORE any working files exist)

**This phase is non-negotiable and runs first.** If working files are created before `.gitignore` is updated, a stray `git add -A` (or a future agent's commit-everything reflex) could stage 500KB+ of VTT files and pollute repo history. Doing this first makes the repo safe-by-default before Phase 1 generates any output.

```powershell
# Step 1: Read .gitignore
# Step 2: Confirm these two lines are present (add if missing):
#   Optimus Academy/tools/working/
#   Optimus Academy/tools/archive/
# Step 3: Stage + commit + push immediately, BEFORE any working file is created
```

Commit message:
```
chore(gitignore): ignore Optimus Academy tools/working and tools/archive

Pre-commit guard for the /learn long-form-YouTube capture pipeline.
Working scratch files (VTTs, chunk slices, agent notes) and post-run
archives must never enter repo history.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
```

**Verification before proceeding to Phase 1:**
- `git check-ignore "Optimus Academy/tools/working/foo.vtt"` returns the path (proves ignore is active)
- `git check-ignore "Optimus Academy/tools/archive/2026-05-06-test/foo.vtt"` returns the path

If either check fails, fix the .gitignore pattern before any Phase 1 work.

**Single-session parallel fanout. NOT /loop.** /loop is for recurring tasks; this is parallel work. Reserved as fallback only if context exhausts mid-synthesis.

**Subagent Delegation Rule applies** — Phase 3 is 10 independent tasks → 10 parallel agents in ONE batch (single message, multiple Agent tool calls). Spawning one-per-message is a process failure per CLAUDE.md.

---

## Phase 1 — Transcript fetch (auto-captions, NOT Whisper) — via NEW permanent helper

**Build the helper FIRST, then use it.** The user opted to graduate the auto-caption fetch into a reusable tool — long-form YouTube captures will recur, and the helper pays back on first reuse.

### 1a. Build `Optimus Academy/tools/fetch-youtube-captions.py`

A new Python helper that wraps yt-dlp for fast caption extraction. Sibling to `transcribe-url.py`. Sole responsibility: long-form YouTube. (No video routing inside the helper — the caller picks which helper to use; same convention as transcribe-url.py.)

**CLI contract:**
```
py -3.11 "Optimus Academy/tools/fetch-youtube-captions.py" <youtube-url> [--out-dir <dir>]
```

**Behavior:**
1. Verify Python is 3.11 (exit 6 otherwise — same convention as `transcribe-url.py`).
2. Verify `yt_dlp` importable (exit 3).
3. Fetch `--print-json --skip-download` first → metadata (title, uploader, upload_date, duration, chapters[]).
4. Fetch auto-captions: `--write-auto-sub --skip-download --sub-lang en --convert-subs vtt`. If en auto-sub unavailable, try `--sub-lang en-US,en-GB`. If still none, exit 7 with message: "No English auto-captions available for <video-id>. Manual subs may exist on creator's channel — use --langs <code> if you know the language code."
5. Strip VTT timing into clean text + per-line timestamp index. Output JSON on stdout:
   ```json
   {
     "transcript": "<full plain text>",
     "transcript_timestamped": [{"start": 12.34, "end": 18.21, "text": "..."}, ...],
     "publisher": "<channel>",
     "title": "<title>",
     "url": "<canonical youtube.com/watch?v=ID>",
     "source_date": "YYYY-MM-DD",
     "duration": "Xh Ymin",
     "chapters": [{"start": 0, "end": 43, "title": "Intro"}, ...],
     "vtt_path": "<absolute path to saved VTT>",
     "meta_path": "<absolute path to saved meta json>"
   }
   ```
6. Files written to `--out-dir` (default: `Optimus Academy/tools/working/<video-id>/`):
   - `<video-id>.en.vtt` (raw VTT — preserved for audit)
   - `<video-id>.meta.json` (raw yt-dlp `--print-json` output)
7. Idempotent: if both files already exist for this video-id, skip fetch and re-emit JSON from disk. Enables resumability.
8. Exit codes mirror `transcribe-url.py` conventions (0 success / 1 runtime / 3 yt-dlp missing / 6 wrong Python / 7 no captions available).

**Documentation:** add a section to `Optimus Academy/README.md` describing the helper and when to use it (long-form YouTube > 5 min where Whisper would be slow).

**Out of scope for this run:** updating the /learn command routing table at `C:\Users\Anthony\.claude\commands\learn.md` to auto-route long-form YouTube through the new helper. That's a follow-up decision after we've used the helper 1-2 times and confirmed it's robust. Note the deferred update in `Optimus Academy/tools/hermes-openclaw-5h-capture-plan.md` (the preserved plan copy).

### 1b. Use the helper for THIS capture

```powershell
New-Item -ItemType Directory -Force -Path "Optimus Academy/tools/working/MpItrr4OYf0"
New-Item -ItemType Directory -Force -Path "Optimus Academy/tools/working/MpItrr4OYf0/chunks"
New-Item -ItemType Directory -Force -Path "Optimus Academy/tools/working/MpItrr4OYf0/notes"

py -3.11 "Optimus Academy/tools/fetch-youtube-captions.py" `
  "https://www.youtube.com/watch?v=MpItrr4OYf0" `
  --out-dir "Optimus Academy/tools/working/MpItrr4OYf0" `
  > "Optimus Academy/tools/working/MpItrr4OYf0/fetch-output.json"
```

**Output:** `tools/working/MpItrr4OYf0/MpItrr4OYf0.en.vtt`, `MpItrr4OYf0.meta.json`, plus stdout-captured `fetch-output.json` for downstream consumption.

**Failure modes:**
- Exit 7 (no captions) → abort. Do NOT fall back to Whisper. Surface the failure to user with options: request transcript from creator, capture from chapter notes only, or defer until manual subs land. **Whisper is explicitly out-of-scope** for this run.
- Exit 3/6 → install missing deps as the helper's stderr instructs, retry.

---

## Phase 2 — Chunk by chapter (with 30-min time fallback) — also a permanent helper

Build `Optimus Academy/tools/split-vtt-into-chunks.py` (sibling to fetch-youtube-captions.py — same long-form YouTube workflow).

**CLI:**
```
py -3.11 "Optimus Academy/tools/split-vtt-into-chunks.py" `
  --vtt <path> --meta <path> --out-dir <chunks-dir> [--target-words 5000] [--n-chunks 10]
```

**Behavior:**
1. Parse `meta.json.chapters[]`. If length ≥ 8: chunk by chapter, merging short adjacent chapters until each chunk's word-count is within ±30% of `--target-words`.
2. If chapters missing/sparse OR `--n-chunks` overrides: time-based slicing into N equal chunks.
3. Output to `<out-dir>/`:
   - `chunk-{01..NN}-<chapter-or-time-slug>.vtt`
   - `chunk-{01..NN}.meta.json` (`{start, end, chapter_title, word_count, source_video_id}`)
   - `chunks-index.json` (manifest: list of all chunks with their meta)
4. Idempotent: if all chunk files already exist matching the manifest, no-op (resumability).

**Pinned chapters surfaced from WebFetch (incomplete — yt-dlp meta.json is authoritative):**
Intro · What Is Hermes · How Hermes Learns · Hermes vs Traditional Agents · Hermes vs OpenClaw · Real Use Cases · Honest Limitations.

**Invocation for this capture:**
```powershell
py -3.11 "Optimus Academy/tools/split-vtt-into-chunks.py" `
  --vtt "Optimus Academy/tools/working/MpItrr4OYf0/MpItrr4OYf0.en.vtt" `
  --meta "Optimus Academy/tools/working/MpItrr4OYf0/MpItrr4OYf0.meta.json" `
  --out-dir "Optimus Academy/tools/working/MpItrr4OYf0/chunks" `
  --target-words 5000 --n-chunks 10
```

---

## Phase 3 — Parallel chunker fanout (10 agents, single batch)

**Dispatch all 10 in ONE message** (multiple Agent tool calls in one block). Spawning sequentially violates the Subagent Delegation Rule's concurrency checkpoint.

Each agent:
- **Subagent type:** `general-purpose`
- **Required reading:**
  - `00 — Empire Index/tag-schema.md`
  - `Optimus Academy/concepts/openclaw-multi-agent-orchestration.md` (cross-ref, do not duplicate)
  - `Optimus Academy/tools-tracking/openclaw.md`
  - Its own chunk file: `tools/working/chunks/chunk-NN-*.vtt` + meta sidecar
- **Output file (sole owner):** `tools/working/notes/chunk-NN-notes.md`
- **Word floor:** ≥ 800 words. Aggregate target ≥ 15k words across 10 chunks.
- **Structure (rigid):** Summary / Mechanics (sub-headed) / Examples / Quotes (with timestamps) / Action Items / Open Questions / Cross-refs.

**Hard prompt rule given to each chunker:** "You are processing a 30-min slice of a 5h course. The user wants every framework, every example, every number captured — they will re-read your notes instead of re-watching. If you write < 800 words, you are aggressively summarizing — go back."

**Status checkpoint:** each agent appends one line to `tools/working/hermes-openclaw-status.md` on completion.

---

## Phase 4 — Synthesis (orchestrator, single session)

Orchestrator reads all 10 `chunk-NN-notes.md`, then writes:

### 4a. Daily file — CREATE `Optimus Academy/daily/2026-05-06.md`

File-level YAML:
```yaml
---
date: 2026-05-06
schema-version: 1
tags: [#learning/captured]
---
```

Single H2 section per /learn rigid contract. Inline Dataview fields (`publisher::`, `source-type:: course`, `url:: https://www.youtube.com/watch?v=MpItrr4OYf0`, `source-date::`, `captured::`, `captured-by:: agent:learn-orchestrator`, `duration:: 5h`, `domain:: agents`, `concepts-touched::`, `bridges-created::`).

`### Detailed Notes` is the **comprehensive aggregation** — one `####` per course chapter, holding each chunker's Mechanics + Examples + Quotes content concatenated and lightly de-duplicated. Target 15-30k words. This is the "future-Anthony re-reads instead of re-watching" artifact.

All 7 H3 sections present (Summary / Key Concepts / Detailed Notes / Code & Examples / Notable Quotes / Action Items / Open Questions) — empty ones show `(none)`.

### 4b. Concept file — CREATE `Optimus Academy/concepts/hermes-openclaw-agents-course.md`

```yaml
---
title: Hermes + OpenClaw Agents Course (Julian Goldie)
schema-version: 1
domain: agents
created: 2026-05-06
last-updated: 2026-05-06 HH:MM
review-by: 2026-11-06
source-references: ["[[../daily/2026-05-06#HH:MM — \"FREE Hermes + OpenClaw AI Agents Course: Build & Automate ANYTHING\" by Julian Goldie SEO]]"]
enriched-from: []
level: intermediate
prerequisites: ["[[openclaw-multi-agent-orchestration]]"]
audience: [developer, founder]
tags: [#learning/synthesized, #applies-to/ai-agents]
---
```

All 7 sections (What it is / When to use / Mechanics / Examples / Gotchas / Related Concepts / Updates). **Mechanics** sub-headed by chapter (one `###` per major topic — Hermes definition, learning model, Hermes vs OpenClaw, use cases, limitations, plus any chapters surfaced from yt-dlp meta). **Related Concepts** MUST link `[[openclaw-multi-agent-orchestration]]`. Target 2-4k words — distilled, atomic, NOT a transcript dump (the daily file holds that).

---

## Phase 5 — Bridges

**Mandatory (write at synthesis time):**

| File | Action | Value-vector | Reason |
|---|---|---|---|
| `tools-tracking/hermes.md` | CREATE | (n/a — tool entry, not a bridge) | New tool, not yet tracked. Mirror the `openclaw.md` shape. Status: `evaluating`. |
| `apply-to-optimus/hermes-openclaw-agents-course-applied-to-tools-tracking-hermes.md` | CREATE | `[productivity]` | Hermes self-improving skill model could shave agent build time on Tier-3/Tier-4. |
| `tools-tracking/openclaw.md` | APPEND `## Decision log` entry | (n/a — tool entry update) | Course teaches new use patterns of an already-tracked tool. |
| `apply-to-optimus/hermes-openclaw-agents-course-applied-to-tools-tracking-openclaw.md` | CREATE | `[productivity]` | Specific application of new course-taught patterns to OpenClaw evaluation. |

**Conditional (defer until synthesis output reveals them — DO NOT pre-commit):**
- `Offerings/02 AI Agents/shared-knowledge/lessons/<slug>.md` — if course teaches a Tier-3/Tier-4 architecture pattern Optimus would adopt. Likely yes given "Real Use Cases" chapter. `value-vector: [productivity, revenue]`.
- `Optimus Inc/ai-agents/<tier>/<slug>.md` — if Optimus's drink-own-champagne deployment would absorb a specific pattern. Defer.
- `.claude/agents/build/<canonical>.md` — if course teaches a content/build pattern mapping to a canonical agent. Defer.

---

## Phase 6 — Commit + push

```bash
git add "Optimus Academy/daily/2026-05-06.md" \
        "Optimus Academy/concepts/hermes-openclaw-agents-course.md" \
        "Optimus Academy/tools-tracking/hermes.md" \
        "Optimus Academy/tools-tracking/openclaw.md" \
        "Optimus Academy/apply-to-optimus/hermes-openclaw-agents-course-applied-to-*.md"

git commit -m "$(cat <<'EOF'
learn(agents): Hermes + OpenClaw 5h course capture (Julian Goldie)

- Source: [[2026-05-06#HH:MM — "FREE Hermes + OpenClaw AI Agents Course"]]
- Concepts: hermes-openclaw-agents-course (created)
- Tools: hermes (created), openclaw (appended)
- Bridges: tools-tracking-hermes, tools-tracking-openclaw[, ai-agents-lessons-...]

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"

git push
```

Working/scratch files NOT staged. Plan-Preservation: copy this plan file to `Optimus Academy/tools/hermes-openclaw-5h-capture-plan.md` in the same commit (per the global rule that plan + implementation share a commit).

---

## Phase 7 — Archive (NOT delete)

```powershell
Move-Item "Optimus Academy/tools/working/" `
  "Optimus Academy/tools/archive/2026-05-06-hermes-openclaw-course/" -Force
```

If `.gitignore` doesn't already cover `Optimus Academy/tools/working/` and `Optimus Academy/tools/archive/`, add both lines and stage `.gitignore` in the same commit. **Audit-trail rationale:** raw VTT + chunk notes are ~500KB and let us re-derive the synthesis if we find it wrong months later — recovery from delete is impossible.

---

## Resumability

State file: `tools/working/hermes-openclaw-status.md`. Orchestrator checks at startup:

- `hermes-openclaw-course.en.vtt` exists → skip Phase 1
- All 10 `chunks/chunk-NN-*.vtt` exist → skip Phase 2
- For each chunk: if `notes/chunk-NN-notes.md` exists AND status says `complete` → skip in fanout
- All 10 notes files complete → jump to Phase 4

A single chunker crash loses ~5 min, not the whole run.

---

## Files created / modified (explicit)

**Created (NOT committed — gitignored):**
- `Optimus Academy/tools/working/MpItrr4OYf0/MpItrr4OYf0.en.vtt`
- `Optimus Academy/tools/working/MpItrr4OYf0/MpItrr4OYf0.meta.json`
- `Optimus Academy/tools/working/MpItrr4OYf0/fetch-output.json`
- `Optimus Academy/tools/working/MpItrr4OYf0/chunks/chunk-{01..10}-*.vtt` (+ `.meta.json` + `chunks-index.json`)
- `Optimus Academy/tools/working/MpItrr4OYf0/notes/chunk-{01..10}-notes.md`
- `Optimus Academy/tools/working/MpItrr4OYf0/hermes-openclaw-status.md`

**Created (committed):**
- `Optimus Academy/tools/fetch-youtube-captions.py` — NEW permanent helper
- `Optimus Academy/tools/split-vtt-into-chunks.py` — NEW permanent helper
- `Optimus Academy/daily/2026-05-06.md`
- `Optimus Academy/concepts/hermes-openclaw-agents-course.md`
- `Optimus Academy/tools-tracking/hermes.md`
- `Optimus Academy/apply-to-optimus/hermes-openclaw-agents-course-applied-to-tools-tracking-hermes.md`
- `Optimus Academy/apply-to-optimus/hermes-openclaw-agents-course-applied-to-tools-tracking-openclaw.md`
- `Optimus Academy/tools/hermes-openclaw-5h-capture-plan.md` (plan-preservation copy of THIS plan)
- (conditional) `Offerings/02 AI Agents/shared-knowledge/lessons/<slug>.md` + matching bridge

**Modified (committed):**
- `Optimus Academy/tools-tracking/openclaw.md` — APPEND `## Decision log` entry (in Phase 6 commit)
- `Optimus Academy/README.md` — document the two new helpers + when to use each (in Phase 6 commit)
- `.gitignore` — add `Optimus Academy/tools/working/` and `Optimus Academy/tools/archive/` (**Phase 0 commit, BEFORE Phase 1 — separate commit, not part of Phase 6**)

**Archived (post-commit, not committed):**
- `Optimus Academy/tools/working/` → `Optimus Academy/tools/archive/2026-05-06-hermes-openclaw-course/`

---

## Critical files (read before implementing)

- `c:\Projects\Optimus Assets\Optimus Academy\concepts\openclaw-multi-agent-orchestration.md` — peer concept; cross-link, don't duplicate
- `c:\Projects\Optimus Assets\Optimus Academy\tools-tracking\openclaw.md` — APPEND target + structural template for new `hermes.md`
- `c:\Projects\Optimus Assets\Optimus Academy\daily\2026-05-03.md` — most-recent daily exemplar
- `C:\Users\Anthony\.claude\commands\learn.md` — the rigid contract
- `c:\Projects\Optimus Assets\00 — Empire Index\tag-schema.md` — controlled vocab + slug rule
- `c:\Projects\Optimus Assets\Optimus Academy\tools\transcribe-url.py` — reference pattern for tool helpers (do NOT extend; yt-dlp invoked directly inline)

---

## Verification (run before reporting done)

1. **Transcript completeness** — `(Get-Content hermes-openclaw-course.en.vtt | Measure-Object -Line).Lines` ≥ 5000.
2. **Chunk completeness** — 10 chunks, no zero-byte files, sum of word counts ≈ VTT word count ±2%.
3. **Notes completeness** — 10 notes files, each ≥ 800 words, aggregate ≥ 15k.
4. **Daily structure** — all 7 H3 sections; one `####` per chapter under Detailed Notes.
5. **Concept structure** — all 7 sections; `Related Concepts` contains `[[openclaw-multi-agent-orchestration]]`.
6. **Cross-reference bidirectionality** — concept's `source-references:` includes daily anchor; daily's `concepts-touched::` includes concept wikilink; bridge `concept:` fields point to concept; bridge `source-references:` include daily anchor.
7. **Frontmatter validity** — `domain: agents`; `review-by: 2026-11-06`; `schema-version: 1` everywhere.
8. **Tag audit** — daily `#learning/captured`; concept `#learning/synthesized` + `#applies-to/ai-agents`; bridges `#learning/applied` + `#applies-to/tools/{hermes,openclaw}`.
9. **Git history** — `git log -1 --stat` shows expected files; commit message matches /learn contract; `git push` exit 0; remote tracking up-to-date.
10. **Cleanup** — `Test-Path "Optimus Academy/tools/working/"` returns `False`; archive folder exists.

---

## Decision summary

| Decision | Choice | Why |
|---|---|---|
| Transcript path | yt-dlp auto-captions via NEW permanent helper | Whisper takes 4-8h on 5h audio; auto-captions take seconds. User opted to graduate to permanent helper. |
| Helper scope | TWO permanent tools (fetch-youtube-captions + split-vtt-into-chunks) | Long-form YouTube will recur; helpers pay back on first reuse |
| /learn routing update | DEFERRED (separate decision) | Use helpers manually for this run; update /learn.md routing table after 1-2 successful re-uses |
| Concept slug | `hermes-openclaw-agents-course` | User-confirmed |
| Concept count | ONE | User explicit ask; sub-topics live as Mechanics sub-headings |
| Chunk count | 10 (~30 min / ~5k words each) | Parallel agent context budget sweet spot |
| Concurrency | Single batch, 10 parallel agents | Subagent Delegation Rule + concurrency checkpoint |
| `/loop` usage | None (fallback only) | Work is parallel, not recurring |
| Cleanup | Archive, not delete | Audit trail; storage cost trivial |
| Bridge to OpenClaw concept | Cross-link in Related Concepts, NOT merge | Different center-of-mass; merge would dilute the OpenClaw concept |
