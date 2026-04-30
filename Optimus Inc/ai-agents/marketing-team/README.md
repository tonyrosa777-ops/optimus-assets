---
schema-version: 1
last-updated: 2026-04-29
tags: [offering/content-engine, status/in-development]
---

# Optimus Marketing Team — Live Instance

Optimus's own deployment of the Self Learning Content Engine, running against Optimus's own content pillars. The instance, not the product spec or the build.

Cross-references:
- Product spec: [[../../../Offerings/02 AI Agents/03 Marketing Team/README|product spec]]
- Build spec: [[../../../Offerings/02 AI Agents/03 Marketing Team/python-architecture|python-architecture.md]]
- Tech-stack rationale: [[../../../Offerings/02 AI Agents/03 Marketing Team/tech-stack-research]]
- Founder layer governing this instance: [[../../../anthony-rosa/north-star]]

This file tracks Optimus's running deployment of the engine.

---

## Stack

Per the canonical Optimus stack ([`../../../Offerings/02 AI Agents/shared-knowledge/tech-stack.md`](../../../Offerings/02%20AI%20Agents/shared-knowledge/tech-stack.md)):

- Python · FastAPI · anthropic SDK (Claude Sonnet weekly · Claude Opus monthly deep-eval)
- Pydantic v2 for all schemas
- supabase-py for the 30-day rolling performance table + strategy outputs + the four agent-infrastructure primitives
- APScheduler for the Sunday 18:00 EST cron
- Optional ElevenLabs HTTP for audio strategy briefings

This is a Python service from day one — no visual workflow orchestrators in the runtime.

---

## Purpose

Generates the strategy that drives Optimus's own [[../../social-pipeline/README|social pipeline]]. The Marketing Team is the brain. The social pipeline is the output side — what actually gets published, when, where.

This is also the live demo of the Tier-3 Marketing Team offering. Prospects evaluating the Marketing Team see Optimus's own social presence as the proof.

---

## Configuration — pillars

Optimus's own pillars. Working set, subject to revision once the engine has data:

1. **AI Empowerment** — what AI agents can actually do for a small business owner *today*, not the hypey 2027 narrative
2. **Business Automation** — concrete workflow examples, before/after, time saved, revenue unlocked
3. **Founder Story** — Anthony building Optimus in public, decisions made, mistakes corrected
4. **Client Wins** — outcomes from real Optimus deployments, sourced from [[../../../knowledge/retrospectives/]]

These pillars get tuned as the engine surfaces what actually performs. The whole point of the Self Learning Content Engine is that the pillars are not fixed — they evolve based on saturation logs and engagement signals. Per-client pillar configuration is documented in the product build spec.

---

## Tracking

| Field | Value |
|---|---|
| FastAPI service URL | TBD (deployment target per `tech-stack.md` § Backend hosting) |
| Repo | `optimus-marketing-team` (TBD on GitHub creation) |
| Supabase project | TBD |
| Weekly strategy outputs | TBD — Supabase view URL once running |
| Saturation/identity signal logs | TBD — same |
| Performance reads | TBD — weekly synthesis cadence |
| Cache hit rate target | ≥85% on weekly Sonnet calls (cached: pillar definitions + scoring rubric + system prompt) |

---

## Status

**Scoped, build in progress.** This is the **first true scheduled-cron agent** Optimus ships — it sets the agent-architecture pattern every subsequent Optimus agent (including the Tier-4 dogfood employee) inherits. The Drink-Own-Champagne 2027-Q3 milestone runs through this instance: by end of 2027-Q3 Optimus's content strategy is fully autonomous via this running deployment, ahead of the Tier-4 employee taking over coordination.

Waiting on: pillar finalization, Supabase setup, FastAPI deploy target chosen, social-account performance ingestion path wired (Phyllo or per-platform native APIs).

---

## Cross-references

- Product spec: [[../../../Offerings/02 AI Agents/03 Marketing Team/README|product spec]]
- Build spec: [[../../../Offerings/02 AI Agents/03 Marketing Team/python-architecture|python-architecture.md]]
- Output side (what gets published): [[../../social-pipeline/README]]
- Brand voice the content speaks in: [[../../brand/README]]
- Tier-4 dogfood instance (the next step up): [[../autonomous-employee/README]]
