---
name: Journal — Anthony Rosa (private)
description: Daily journal entries. Personal, never auto-fed to Claude context. Weekly review extracts learnings into north-star/roadmap/wins.
type: founder-vision
schema-version: 1
last-updated: 2026-04-29
tags: [layer/optimus-os, status/active]
---

# Journal

> The thinking happens here. The decisions land in the static layer (`north-star.md`, `ai-engineer-roadmap.md`, `portfolio-standards.md`, `wins.md`).

## How this works

The `journal/` folder contains daily markdown entries named `YYYY-MM-DD.md`. Format is loose — whatever you actually want to write. No template, no enforced sections, no `(none)` placeholders. This is the only file in the founder layer that escapes the rigid-structure contract.

**These entries are never automatically fed into Claude Code context.** The founder layer's static docs (`north-star`, `roadmap`, `portfolio-standards`, `wins`) get pulled into Claude prime context via the `## Founder Vision` section in `CLAUDE.md`. The journal does NOT. It stays personal.

## Why personal

Not every thought belongs in production context. Frustration with a client, doubts about a decision, half-formed ideas, weekly regrets, working through a hard architectural choice in plain prose — these belong somewhere private where they can be raw without leaking into Claude's reasoning about a build. The journal is that place.

## Weekly review

Once a week (Sunday afternoon works), read through the week's journal entries and extract anything worth promoting:

- A pattern you noticed about how Optimus builds → maybe it belongs in `portfolio-standards.md` as a new rule, or in `Offerings/02 AI Agents/shared-knowledge/concept-notes.md` as a new pattern.
- A capability gap that surfaced → maybe `ai-engineer-roadmap.md` Year 1 needs a skill added.
- A milestone that quietly happened → goes into `wins.md`.
- A strategic shift you noticed yourself making → maybe `north-star.md` needs an update, or its `review-by` date is overdue.

The journal is the input. The static docs are the output. Without the weekly review, the journal becomes a graveyard of insights that never compound.

## What NOT to put here

- Project task lists (use `progress.md` in the relevant client repo)
- Build-time decisions on a specific system (those go in the system's `/docs/retro.md`)
- Anything that would change a vault structural rule without going through `optimus-system-guide.md` first (per the maintenance protocol — structural drift without a guide update is a failure mode)

## Format

```markdown
# YYYY-MM-DD

## What happened
- Bullet points. Whatever felt notable.

## What I'm working on / stuck on
- The tactical state.

## What I'm thinking about
- Strategic / introspective.
```

But again — loose. If you write three sentences, that's fine. If you write three pages, that's also fine. Showing up daily matters more than the structure.

## First entry

Not pre-seeded. The first entry is yours to write — when you write it, the runway starts measuring itself.
