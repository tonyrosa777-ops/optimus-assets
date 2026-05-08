---
title: Skills — Anthony Rosa Career Progression
schema-version: 1
created: 2026-05-08
last-updated: 2026-05-08
tags: [#owner/anthony-rosa, #layer/optimus-os, #status/active]
---

# Skills — Anthony Rosa Career Progression

> **Scope of this folder.** `anthony-rosa/skills/` holds Anthony Rosa's personal career skill development as an AI engineer — Python production-grade practice, LangChain, FastAPI, Pydantic, Anthropic SDK fluency, Personaplex audio, and similar progression goals and roadmaps. These are career intent and learning targets, not knowledge content.
>
> **What this folder is NOT.** This folder is distinct from:
> - **Claude Code skills** at `.claude/skills/` — those are tool/instruction files Claude Code loads when invoking `/<skill-name>`. Different system, different purpose.
> - **Optimus build skill instructions** referenced by Claude tools during builds (the skill-creator system, frontend-design, etc.) — those are Claude-executable instructions, not human career-progression notes.
> - **Optimus Academy concepts** — those are the actual knowledge content (the "what" of a skill: how Pydantic v2 works, what FastAPI dependency injection does). Concepts are ingested via `/learn` and live in `Optimus Academy/concepts/`. This folder holds the "why I'm learning this and where I am on the path"; concepts hold the substance.
>
> **Naming pattern for files in this folder:** `<skill-area>-progression.md` (e.g., `ai-engineer-progression.md`, `python-progression.md`). Each file: goals → gates / milestones → current status → why this matters for career.

## How this folder relates to the rest of the vault

- **`anthony-rosa/ai-engineer-roadmap.md`** is the year-by-year technical progression at the founder-vision level. The files in THIS folder are the per-skill drill-downs — each progression file is the concrete "where am I, what's next" tracker for a specific skill area.
- **Optimus Academy `/learn` captures** that teach a skill (e.g., a course on FastAPI dependency injection) land as concepts in `Optimus Academy/concepts/<concept-slug>.md`. When that concept advances Anthony's career-skill progression, a bridge file lands in `Optimus Academy/apply-to-anthony-rosa/<concept-slug>.md` with `applies-to:: [[../../anthony-rosa/skills/<progression-file>]]` — the bridge connects the knowledge to the career progression.

## Files

| File | What |
|---|---|
| `ai-engineer-progression.md` | Career skill goals + gates + why for the AI engineer track. The skill umbrella corresponding to the [[../ai-engineer-roadmap]] year-over-year plan. |

> Add new progression files as new skill areas come into focus. Don't preemptively create files for skills not actively in scope — empty progression files become noise.

## Bridge zone

`/learn` captures that bridge to a skill progression land at `Optimus Academy/apply-to-anthony-rosa/<concept-slug>.md` with `#applies-to/anthony-rosa/skills` and `applies-to:: [[../../anthony-rosa/skills/<progression-file>]]`. See `Optimus Academy/apply-to-anthony-rosa/README.md` for the bridge contract.
