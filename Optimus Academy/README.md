---
title: Optimus Academy
created: 2026-04-26
last-updated: 2026-04-26
tags: [#layer/optimus-os, #status/active]
---

# Optimus Academy

Personal daily learning hub. ~90 minutes a day across YouTube videos on Claude concepts and new releases (NemoClaw, OpenClaw, etc.), NVIDIA classes, Anthropic courses, agentic AI / autonomous agents / multi-agent systems, and whatever new tooling surfaces day-to-day. Separate from `[[../Offerings/README|Offerings]]` (what Optimus sells) and `[[../Optimus Inc/README|Optimus Inc]]` (the company itself). This folder is intentionally personal. It captures learning that may or may not yet apply to Optimus operations. The bridge from learning to business lives in `[[apply-to-optimus/README|apply-to-optimus/]]` — when a concept clearly improves an offering, a bridge note gets written that explicitly states "Concept X improves Offering Y by doing Z." That is the connective tissue that turns daily learning into compounding business value, and it is the engine that gets Optimus to a fully autonomous organization in the next 1-2 years.

## Folder model — daily IS the source capture (read this first)

The vault separates **comprehensive per-source captures** (which live as H2 sections inside daily files) from **synthesized atomic concept distillations** (which live as their own files in `concepts/`). There is NO separate `sources/` folder. The daily file IS where the full source extraction goes.

| Folder | What lives here | Mutation rule |
|---|---|---|
| `[[daily/]]` | One file per day. Multiple sources captured the same day → multiple H2 sections in one daily file, each with comprehensive detail extraction. Source attribution sits prominently at the top of each H2. | New H2 sections append throughout the day; existing H2 capture sections never modified after creation. |
| `[[concepts/]]` | One file per **topic** (not per source). Synthesized atomic distillations. The reusable layer above the raw daily captures. | Living. Original definition stays stable at top. New findings from later sources append as `## Update — date — from [[daily/...]]` sections. |
| `[[apply-to-optimus/README\|apply-to-optimus/]]` | One file per (concept × offering) operational insight. "Concept X improves Offering Y by doing Z." | Living. Same append behavior as concepts. |
| `[[courses/]]` | Structured course notes by source: `anthropic/`, `nvidia/`, `youtube/`, `books/`. Each course gets its own subfolder when started. Module-by-module notes live inside the course folder. | Manual organization. |
| `[[tools-tracking/]]` | New tool releases and ecosystem changes. NemoClaw, OpenClaw, Claude features, agent frameworks. One file per tool. Tracks what is real, what shipped, what to evaluate. | Manual updates. |

**The daily-vs-concept relationship.** Concrete example: watch a video today on "Obsidian + Claude combo" → the comprehensive notes go into today's daily file as one H2 section. Next month, watch "Supercharging Obsidian + Claude" → its comprehensive notes go into NEXT MONTH's daily file as one H2 section (each video captured immutably in its own day). The shared `obsidian-claude-integration` concept file consolidates what's actually known about the topic across both videos: the original definition stays stable at the top; the new findings from the second video append as a `## Update — YYYY-MM-DD HH:MM — from [[../daily/<later-date>#<anchor>]]` block. The concept file's visible blockquote at the top lists both daily-anchor sources.

**Cross-references are bidirectional and load-bearing.** Every daily H2 section's inline `concepts-touched::` field lists the concepts it touched (as wikilinks). Every concept file's `source-references:` frontmatter and visible blockquote list the daily-anchor sources that contributed to it (as wikilinks like `[[../daily/2026-04-26#11:36 — "Source Title" by Publisher]]`). You can answer "what concepts did this video teach?" from a daily H2 and "where did I learn this concept?" from a concept file with one click.

## The `/learn` workflow

Paste a transcript, YouTube URL, or course notes. Run `/learn`. Claude generates three traces:

1. **A daily file H2 capture section** in `daily/YYYY-MM-DD.md` — the comprehensive per-source extraction, with inline Dataview metadata fields and source-attribution blockquote at the top. New H2 section in today's file (or new file if today doesn't have one yet).
2. **One concept file per TOPIC** in `concepts/<concept-slug>.md` — created OR updated via scan-and-decide. The synthesized atomic distillation. Most sources touch one topic, so one concept file gets created or updated. A wide-ranging course module might touch 2-3 topics.
3. **Zero or more bridge notes** in `apply-to-optimus/<concept-slug>-applied-to-<offering-slug>.md` — operational insights, when the topic has clear application to one of the four Optimus offerings.

Plus tags on every file. Plus a commit.

The full prompt that drives this lives at `[[../learn-prompt|learn-prompt]]` at vault root.

## Input pathways — what `/learn` accepts

`/learn` is the single capture skill. The input layer routes by URL pattern:

| Input | Pathway | Notes |
|---|---|---|
| `youtube.com/watch?v=...` (long-form) | `WebFetch` for transcript | Existing path, unchanged. |
| `tiktok.com`, `vm.tiktok.com`, `instagram.com/reel`, `instagram.com/p`, `youtube.com/shorts`, `x.com/.../status/.../video` | `[[tools/transcribe-url.py]]` — yt-dlp downloads audio + LOCAL openai-whisper transcribes | No API key. No external request to OpenAI. Privacy-preserving. |
| Plain article URL | `WebFetch` for body + meta tags | Existing path, unchanged. |
| Pasted text / raw notes | Direct processing | Existing path. User provides source attribution in the same message. |
| X (Twitter) single posts | **Skip** — too short to earn a concept note | Capture the *thought* via paste-text if a tweet sparks one, but don't capture the tweet itself. |
| X threads | Paste-text fallback | Copy full thread top-to-bottom, paste into `/learn` with `publisher = @handle`, `url = first-tweet-link`, `source-type = thread`. |

**Critical invocation rule:** `transcribe-url.py` must be invoked via `py -3.11` exactly — never bare `python` or `python3`. Python 3.14 is broken on this machine and shadows 3.11 on PATH. The `/learn` skill spec spells this out so a future Claude run doesn't fall back to `python` and crash.

**No second API key required.** Local Whisper means transcription is offline, free, and private. The Anthropic SDK key already in the env is the only key in the loop.

**Enrichment when sources are shallow** (added during execution): a 15-second TikTok mentioning a tool is real signal but the source itself can't fill out Mechanics/Examples/Gotchas. `/learn` Step 1.5 auto-fires WebSearch + WebFetch when the source is short (<60s or <200 words), mentions a new tool/framework, or hits a borderline scan-and-decide case. The enriched info populates the concept's body; the original source still owns the daily file's H2 attribution; the enrichment URLs land in a new `enriched-from:` field on the concept's frontmatter. Opt out per call with `/learn --no-enrich <URL>`.

**Within-concept dedup at append time** (added during execution): when `/learn` appends to an existing concept, it ONLY blocks identical/near-verbatim repetition. Variations always pass — a new angle on a known principle, a new example, a new gotcha, a new mechanism are NEW information and earn an `## Updates` block. The `source-references:` list always grows with the new daily-anchor regardless of whether the body changes.

**Folder creation policy.** Bridges may need to write into folders that don't exist yet (`knowledge/craft/<area>/`, `Optimus Inc/finance/`, `Optimus Inc/operations/`). Before any bridge write, `/learn` runs `Test-Path` on the parent folder; if missing, `New-Item -ItemType Directory -Force` creates it. Never preemptively scaffold empty folders. Folders materialize only when a real bridge file lands.

**Weekly review surface:** see `[[weekly-review]]` — Dataview-powered file that lists active bridges grouped by value vector (revenue → productivity → overhead), plus applied-awaiting-promotion and 30+-day abandonment candidates. Dataview re-runs on file open; no script.

## The scan-and-decide rule

Daily file H2 captures are always CREATED (immutable per source). The scan-and-decide logic applies only to `concepts/` and `apply-to-optimus/` — those are the living layers where dedup matters.

For each topic the source touches, /learn:
- **Strong match exists** in `concepts/` → APPENDS a `## Update — YYYY-MM-DD HH:MM — from [[daily-anchor]]` section to the existing concept file. The concept stays in one place and accretes detail over time.
- **Borderline match** → ASKS. Default suggestion: APPEND to existing.
- **No match** → CREATES a new concept file using the rigid concept structure.

**Default-to-APPEND on borderline.** False-merge (folding new info into an adjacent concept) is recoverable later by splitting. False-fragmentation (creating a new concept file when an existing one would have absorbed the topic) accumulates and degrades the synthesis layer faster. Sub-patterns of an existing topic stay as `### sub-headings` inside that concept's `## Mechanics`, NOT as separate concept files.

## Rigid identical structure — the contract

Every file produced by `/learn` follows a rigid section structure for its file type. **Section headers are always present, in the same order, even when the section has no content.** Empty sections show literally `(none)` as the body.

The reason: predictability beats efficiency. A reader scrolling through any daily H2 section knows that code lives in `### Code & Examples`. They never have to scan to find it. They never wonder if a section was skipped because there was nothing to say or because the author got lazy. `(none)` means "I checked, and there genuinely was nothing for this section."

When NOT to use `(none)`: don't use it to dodge work. The test: did you check, and was there genuinely nothing? Then `(none)`. Did you skip the section because it was a hassle? Then go back and fill it.

## Autonomy bake-ins — non-negotiable from day 1

Every /learn-produced file carries autonomy hooks so that future autonomous agents can operate over the vault without reading every file individually:

- **`schema-version: 1`** in YAML frontmatter on every file (enables safe future migrations)
- **Inline Dataview `key:: value` fields** under every H2 source section in daily files (queryable per-source metadata)
- **Deterministic slug rule** — same input always produces same slug (defined in `[[../00 — Empire Index/tag-schema|tag-schema.md]]`)
- **Controlled `domain:` vocabulary** — pick from the 11-entry list in tag-schema.md, don't invent
- **`captured-by: human | agent:<name>`** field — future-proofs autonomous-vs-manual capture audits
- **`review-by: <YYYY-MM-DD>`** on concept files (default created+6mo) — enables nightly autonomous stale-knowledge surface
- **Source URL canonical form** — normalized at capture time per the rule in tag-schema.md so dedup-by-URL works

These hooks cost almost nothing per file. Retrofitting them across hundreds of historical files later is painful and prone to drift. They're baked in from day 1.

## Daily file structure

Path: `daily/YYYY-MM-DD.md`. Multiple H2 capture sections per day (one per source). Each H2 capture section is immutable after creation.

```
---
date: YYYY-MM-DD
schema-version: 1
tags: [#learning/captured]
---

# YYYY-MM-DD — Daily Learning

## HH:MM — "Source Title" by Publisher

publisher:: Publisher Name
source-type:: video
url:: <canonical-url-or-n/a>
source-date:: <YYYY-MM-DD or unknown>
captured:: YYYY-MM-DD HH:MM
captured-by:: human
duration:: <duration or n/a>
domain:: <controlled-vocab>
concepts-touched:: [[../concepts/concept-slug]]
bridges-created:: [[../apply-to-optimus/bridge-slug]] | (none)

> **Source title:** "Source Title"
> **By:** Publisher Name
> **Type:** video
> **URL:** <canonical-url>
> **Captured:** YYYY-MM-DD HH:MM
> **Duration:** <duration>

### Summary
### Key Concepts Extracted
### Detailed Notes
### Code & Examples
### Notable Quotes
### Action Items
### Open Questions
```

All 7 H3 sections always present. Inline Dataview fields are mandatory under each H2. Visible blockquote with source attribution is mandatory.

## Concept file structure

Path: `concepts/<concept-slug>.md`. Living distillation. ONE file per topic.

```
---
title: <Concept Name>
schema-version: 1
domain: <controlled-vocab>
created: YYYY-MM-DD
last-updated: YYYY-MM-DD HH:MM
review-by: <YYYY-MM-DD ~6 months ahead>
source-references: ["[[../daily/YYYY-MM-DD#HH:MM — \"Source Title\" by Publisher]]"]
tags: [#learning/synthesized, #applies-to/<offering-or-all>]
---

# <Concept Name>

> **Concept distilled from:**
> - [[../daily/YYYY-MM-DD#HH:MM — "Source Title" by Publisher]] — Publisher
>
> **Last updated:** YYYY-MM-DD HH:MM

## What it is
## When to use
## Mechanics
## Examples
## Gotchas
## Related Concepts
## Updates
```

All 7 body sections always present. The `## Updates` section starts empty on creation but the header is still there — it's the contract that signals "this is where future findings will land." When a later source teaches more about this concept, `/learn` appends a `### YYYY-MM-DD HH:MM — <label> — from [[../daily/<date>#<anchor>]]` block under `## Updates` and bumps frontmatter `last-updated` + adds the new daily-anchor to `source-references:`. The original `## What it is` / `## When to use` / `## Mechanics` / `## Examples` / `## Gotchas` content is byte-identical from one capture to the next.

**Concept body discipline:** concept body is **subject-pure** (teaches the topic itself for awareness) and **enrichment-substance-dense** (every `enriched-from:` URL contributes at least one body fact). Optimus-relationship framing belongs ONLY in `apply-to-optimus/` bridges, never in the concept body. See `learn-prompt.md` → CREATE path for the full Concept body discipline rules.

## Useful Dataview queries

The inline Dataview metadata baked into every daily H2 section makes the vault queryable from day 1. Drop these into any note inside the vault to see live results.

**1. All sources by publisher (sorted by date)**
```dataview
TABLE publisher, source-type, captured, domain, concepts-touched
FROM "Optimus Academy/daily"
WHERE publisher
SORT captured DESC
```

**2. All concepts in a given domain** (replace `obsidian` with the domain you care about)
```dataview
LIST
FROM "Optimus Academy/concepts"
WHERE domain = "obsidian"
SORT last-updated DESC
```

**3. Bridges by status** — kanban-style summary
```dataview
TABLE WITHOUT ID file.link AS Bridge, status, offering, last-updated
FROM "Optimus Academy/apply-to-optimus"
WHERE status
SORT status ASC, last-updated DESC
```

**4. Sources captured in last 7 days**
```dataview
TABLE publisher, source-type, captured, domain
FROM "Optimus Academy/daily"
WHERE captured >= date(today) - dur(7 days)
SORT captured DESC
```

**5. Concepts with 2+ source references** (cross-validated topics)
```dataview
TABLE length(source-references) AS sources, domain, last-updated
FROM "Optimus Academy/concepts"
WHERE length(source-references) >= 2
SORT length(source-references) DESC
```

**6. Concepts not yet bridged to any offering** (the "interesting but not actionable" backlog)
```dataview
LIST
FROM "Optimus Academy/concepts"
WHERE !contains(file.outlinks, "apply-to-optimus")
```

**7. Concepts past their `review-by` date** (stale-knowledge surface)
```dataview
TABLE review-by, last-updated, domain
FROM "Optimus Academy/concepts"
WHERE review-by AND review-by < date(today)
SORT review-by ASC
```

The same query set lives in `[[../optimus-system-guide]]` (the canonical operating manual) — they're duplicated here for convenience at the point of use.

## Tag schema

Full schema: `[[00 — Empire Index/tag-schema|the master tag schema]]`. Most-used tags in this hub:

- `#learning/captured` — raw capture (used on daily file YAML)
- `#learning/synthesized` — distilled into a concept note
- `#learning/enriched` — concept augmented via Step 1.5 web enrichment
- `#learning/applied` — wired into an Optimus offering or other bridge target (used on bridges)
- `#applies-to/website-dev`
- `#applies-to/ai-agents`, `#applies-to/ai-agents/{chat,voice,marketing}`
- `#applies-to/craft/{copywriting,psychology,sales,design}` — cross-cutting craft
- `#applies-to/optimus-inc/{finance,marketing,operations,brand}` — Optimus the company itself
- `#applies-to/tools/<tool-slug>` — tool-evaluation captures

## Active study tracks

Edit this list as tracks start and complete.

- [ ] Anthropic Claude API course
- [ ] NVIDIA agentic AI track
- [ ] YouTube creators (TBD)
- [ ] OpenClaw / NemoClaw tracking
