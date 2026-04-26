---
title: Optimus Academy
created: 2026-04-26
last-updated: 2026-04-26
tags: [#layer/optimus-os, #status/active]
---

# Optimus Academy

Personal daily learning hub. ~90 minutes a day across YouTube videos on Claude concepts and new releases (NemoClaw, OpenClaw, etc.), NVIDIA classes, Anthropic courses, agentic AI / autonomous agents / multi-agent systems, and whatever new tooling surfaces day-to-day. Separate from `[[../Offerings/README|Offerings]]` (what Optimus sells) and `[[../Optimus Inc/README|Optimus Inc]]` (the company itself). This folder is intentionally personal. It captures learning that may or may not yet apply to Optimus operations. The bridge from learning to business lives in `[[apply-to-optimus/README|apply-to-optimus/]]` — when a concept clearly improves an offering, a bridge note gets written that explicitly states "Concept X improves Offering Y by doing Z." That is the connective tissue that turns daily learning into compounding business value, and it is the engine that gets Optimus to a fully autonomous organization in the next 1-2 years.

## What goes here

| Subfolder | Purpose |
|---|---|
| `[[daily/]]` | Date-keyed daily notes (`YYYY-MM-DD.md`). Each day's learning gets summarized here with wikilinks down to the deeper concept notes captured. The chronological log. |
| `[[courses/]]` | Structured course notes by source: `anthropic/`, `nvidia/`, `youtube/`, `books/`. Each course gets its own subfolder when started. Module-by-module notes live inside the course folder. |
| `[[concepts/]]` | Atomic Zettelkasten-style notes. ONE concept per file. Wikilinked to related concepts. Updated over time (with `## Update — YYYY-MM-DD HH:MM` sections appended) when new info on the same topic arrives. The permanent knowledge base. |
| `[[tools-tracking/]]` | New tool releases and ecosystem changes. NemoClaw, OpenClaw, Claude features, agent frameworks. One file per tool. Tracks what is real, what shipped, what to evaluate. |
| `[[apply-to-optimus/README\|apply-to-optimus/]]` | Bridge notes. "Concept X improves Offering Y by doing Z." Where learning becomes business value. |

## The `/learn` workflow

Paste a transcript, YouTube URL, or course notes. Run `/learn`. Claude generates:

1. A daily entry under `daily/YYYY-MM-DD.md` (or appends to today's existing entry)
2. One or more atomic concept notes under `concepts/`
3. When applicable, an `apply-to-optimus/` bridge note linking the concept to the offering it improves
4. Tags on every file
5. A commit

The full prompt that drives this lives at `[[../learn-prompt|learn-prompt]]` at vault root.

## The scan-and-decide rule

`/learn` first scans `concepts/` and `apply-to-optimus/` for topic overlap before writing anything new.

- **Strong match exists** → APPENDS a dated `## Update — YYYY-MM-DD HH:MM` section to the existing file. The concept stays in one place and accretes detail over time.
- **Borderline match** → ASKS. Does not silently merge.
- **No match** → CREATES a new file.

Default-to-create when uncertain. A false-merge buries information inside the wrong file and is very expensive to undo. A false-create produces two files on similar topics, which is cheap to fix later by merging. The full reasoning lives in the plan file `[[i-had-a-big-buzzing-blanket]]` (in `C:\Users\Anthony\.claude\plans\`).

## Concept note structure

Every concept note follows this shape. Top stays stable. Updates stack chronologically below.

```
---
title: <Concept Name>
created: YYYY-MM-DD
last-updated: YYYY-MM-DD HH:MM
sources:
  - <URL or course reference>
tags: [#learning/synthesized, #applies-to/...]
---

# <Concept Name>

<Core definition / when to use / mechanics — stays stable at top>

## Updates

### YYYY-MM-DD HH:MM — <short label>
<Later additions stack here chronologically>
```

The top section is the durable definition. The `## Updates` log is where new sources, refinements, counter-examples, and links to related concepts get appended over time. Never rewrite the top — append below.

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
