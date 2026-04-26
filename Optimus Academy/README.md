---
title: Optimus Academy
created: 2026-04-26
last-updated: 2026-04-26
tags: [#layer/optimus-os, #status/active]
---

# Optimus Academy

Personal daily learning hub. ~90 minutes a day across YouTube videos on Claude concepts and new releases (NemoClaw, OpenClaw, etc.), NVIDIA classes, Anthropic courses, agentic AI / autonomous agents / multi-agent systems, and whatever new tooling surfaces day-to-day. Separate from `[[../Offerings/README|Offerings]]` (what Optimus sells) and `[[../Optimus Inc/README|Optimus Inc]]` (the company itself). This folder is intentionally personal. It captures learning that may or may not yet apply to Optimus operations. The bridge from learning to business lives in `[[apply-to-optimus/README|apply-to-optimus/]]` — when a concept clearly improves an offering, a bridge note gets written that explicitly states "Concept X improves Offering Y by doing Z." That is the connective tissue that turns daily learning into compounding business value, and it is the engine that gets Optimus to a fully autonomous organization in the next 1-2 years.

## Folder model — sources vs concepts (read this first)

The vault separates **immutable per-source captures** from **synthesized atomic concept distillations**. Both folders work together. Every learning session writes to both.

| Folder | What lives here | Mutation rule |
|---|---|---|
| `[[sources/]]` | One file per video / article / course module / book chapter / podcast / raw notes session. Comprehensive detail extraction. The source's title and publisher are the file's identity. | **Immutable.** Never appended after creation. If you re-watch the same video and learn something new, create a new dated source file (or update the relevant concept files instead). |
| `[[concepts/]]` | One file per reusable atomic idea. Synthesized from one or more source files. The reusable distillation. | **Living.** Original definition stays stable at top. New findings from later sources append as `## Update — YYYY-MM-DD HH:MM — from [[source]]` sections. |
| `[[apply-to-optimus/README\|apply-to-optimus/]]` | One file per (concept × offering) operational insight. "Concept X improves Offering Y by doing Z." | **Living.** Same append behavior as concepts. |
| `[[daily/]]` | One file per day. Chronological pointer with wikilinks to source + concepts + bridges captured that day. | Append-by-time within each day's file. |
| `[[courses/]]` | Structured course notes by source: `anthropic/`, `nvidia/`, `youtube/`, `books/`. Each course gets its own subfolder when started. Module-by-module notes live inside the course folder. | Manual organization. |
| `[[tools-tracking/]]` | New tool releases and ecosystem changes. NemoClaw, OpenClaw, Claude features, agent frameworks. One file per tool. Tracks what is real, what shipped, what to evaluate. | Manual updates. |

**The relationship between sources and concepts.** Concrete example: watch a video today on "Obsidian + Claude combo" → next month watch "Supercharging Obsidian + Claude" → in this hybrid model, BOTH videos get their own immutable source file (with full detail extraction preserved) AND there's one growing `obsidian-claude-integration` concept file that consolidates what's actually known about the topic across both videos. The concept file's visible blockquote at the top lists both source files. The newest video's findings appear as a `## Update — YYYY-MM-DD HH:MM — from [[source]]` block in the concept's `## Updates` section.

**Cross-references are bidirectional and load-bearing.** Every source file lists the concepts it taught (in `concepts-extracted:` frontmatter and the visible `## Key Concepts Extracted` section). Every concept file lists the source files it was distilled from (in `source-files:` frontmatter and the visible blockquote at top). You can answer "what did this video teach?" from a source file and "where did I learn this concept?" from a concept file with one click.

## The `/learn` workflow

Paste a transcript, YouTube URL, or course notes. Run `/learn`. Claude generates four traces:

1. **An immutable source file** in `sources/YYYY-MM-DD-<source-slug>.md` — comprehensive detail extraction, never appended after creation.
2. **One or more concept files** in `concepts/<concept-slug>.md` — created OR updated via scan-and-decide. The synthesized atomic distillations.
3. **A daily entry** in `daily/YYYY-MM-DD.md` — the chronological pointer linking to source + concepts + bridges.
4. **Zero or more bridge notes** in `apply-to-optimus/<concept-slug>-applied-to-<offering-slug>.md` — operational insights, when applicable.

Plus tags on every file. Plus a commit.

The full prompt that drives this lives at `[[../learn-prompt|learn-prompt]]` at vault root.

## The scan-and-decide rule

`/learn` always CREATES a new source file (no scan; sources are immutable). Then it scans `concepts/` and `apply-to-optimus/` for topic overlap before writing the synthesized concept and bridge files.

- **Strong match exists** → APPENDS a `## Update — YYYY-MM-DD HH:MM — from [[source]]` section to the existing concept or bridge file. The concept stays in one place and accretes detail over time.
- **Borderline match** → ASKS. Does not silently merge. Default suggestion: CREATE NEW.
- **No match** → CREATES a new file using the rigid concept/bridge structure.

Default-to-create when uncertain. A false-merge buries information inside the wrong file and is very expensive to undo. A false-create produces two files on similar topics, which is cheap to fix later by merging.

## Rigid identical structure — the contract

Every file produced by `/learn` follows a rigid section structure for its file type. **Section headers are always present, in the same order, even when the section has no content.** Empty sections show literally `(none)` as the body. This is non-negotiable.

The reason: predictability beats efficiency. A reader scrolling through any source file knows that code lives in `## Code & Examples`. They never have to scan to find it. They never wonder if a section was skipped because there was nothing to say or because the author got lazy. `(none)` means "I checked, and there genuinely was nothing for this section."

When NOT to use `(none)`: Don't use it to dodge work. If the source has 3 code examples, all 3 belong in `## Code & Examples`. If the source has zero code examples (a pure theory talk), then `(none)` is correct. The test: did you check, and was there genuinely nothing? Then `(none)`. Did you skip the section because it was a hassle? Then go back and fill it.

### Source file structure

Path: `sources/YYYY-MM-DD-<source-slug>.md`. Immutable after creation.

```
---
title: <Source Title>
source-type: <video|article|course|book|podcast|notes>
publisher: <publisher/author/channel>
url: <URL or "n/a">
source-date: <YYYY-MM-DD or "unknown">
captured: <YYYY-MM-DD HH:MM>
duration: <"32 min" or "n/a">
domain: <claude-api | agents | obsidian | etc.>
concepts-extracted: [<concept-slug-1>, <concept-slug-2>]
tags: [#learning/captured, #applies-to/<offering-or-all>]
---

# <Source Title>

> **Source title:** "<Source Title>"
> **By:** <publisher/author>
> **Type:** <video|article|course|book|podcast|notes>
> **URL:** <link or n/a>
> **Captured:** YYYY-MM-DD HH:MM
> **Duration:** <32 min or n/a>

## Summary
## Key Concepts Extracted
## Detailed Notes
## Code & Examples
## Notable Quotes
## Action Items
## Open Questions
## Related Sources
```

All 9 body sections always present. The visible blockquote with source attribution is non-negotiable — readers see attribution the moment they open the file, without peeking at YAML.

### Concept file structure

Path: `concepts/<concept-slug>.md`. Living distillation.

```
---
title: <Concept Name>
domain: <domain>
created: YYYY-MM-DD
last-updated: YYYY-MM-DD HH:MM
source-files: [<YYYY-MM-DD-source-slug-1>, <YYYY-MM-DD-source-slug-2>]
tags: [#learning/synthesized, #applies-to/<offering-or-all>]
---

# <Concept Name>

> **Concept distilled from:**
> - [[../sources/YYYY-MM-DD-<source-slug-1>]] — <publisher>
> - [[../sources/YYYY-MM-DD-<source-slug-2>]] — <publisher>
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

All 7 body sections always present. The `## Updates` section starts empty on creation but the header is still there — it's the contract that signals "this is where future findings will land." When a later source teaches more about this concept, `/learn` appends a `### YYYY-MM-DD HH:MM — <label> — from [[../sources/<source>]]` block under `## Updates` and bumps frontmatter `last-updated` + adds the new source to `source-files:`. The original `## What it is` / `## When to use` / `## Mechanics` / `## Examples` / `## Gotchas` content is byte-identical from one capture to the next.

## Tag schema

Full schema: `[[00 — Empire Index/tag-schema|the master tag schema]]`. Most-used tags in this hub:

- `#learning/captured` — raw capture, not yet processed
- `#learning/synthesized` — distilled into a concept note
- `#learning/applied` — wired into an Optimus offering
- `#applies-to/website-dev`
- `#applies-to/ai-agents`
- `#applies-to/ai-agents/chat`
- `#applies-to/ai-agents/voice`
- `#applies-to/ai-agents/marketing`

## Active study tracks

Edit this list as tracks start and complete.

- [ ] Anthropic Claude API course
- [ ] NVIDIA agentic AI track
- [ ] YouTube creators (TBD)
- [ ] OpenClaw / NemoClaw tracking
