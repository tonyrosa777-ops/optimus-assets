---
title: AI Engineer Progression
schema-version: 1
domain: agents
created: 2026-05-08
last-updated: 2026-05-08
tags: [#owner/anthony-rosa, #layer/optimus-os, #status/active]
---

# AI Engineer Progression

The concrete "where am I, what's next" tracker for Anthony's AI engineer career skill development. The umbrella roadmap (year-over-year vision) lives at [[../ai-engineer-roadmap]]; this file is the active tracker that gets updated as skills firm up.

## Why this matters

Optimus's long-term destination is Tier-4 Autonomous AI Employees as the flagship product — custom-trained per client on an open-source harness, deployed on private per-client GPU compute. That's the most technically ambitious tier of the upsell ladder. Anthony's personal skill progression on the AI engineering side is what makes Tier-4 deliverable in-house at SMB pricing. Skill development is mission-critical infrastructure, not optional career hygiene.

Cross-reference: [[../north-star]] § The End Goal (2027-Q3 Drink-Own-Champagne milestone, 4-point moat).

## Skill domains in scope

> *Stub. Each domain gets its own status block as work progresses.*

Suggested domains, mapped to the year-over-year roadmap in [[../ai-engineer-roadmap]]:

- **Python production-grade** — beyond scripting. Type hints (mypy strict), packaging, testing (pytest), async patterns, structured logging, error boundaries, dependency injection.
- **Pydantic v2** — schema design, validators, model factories, serialization control, the migration patterns that broke Pydantic v1 codebases.
- **FastAPI** — DI patterns, lifespan events, dependency-injected services, OpenAPI auto-doc discipline, auth/middleware patterns, background tasks.
- **Anthropic SDK fluency** — prompt caching breakpoints, tool use, computer use, structured outputs, batch API, files API, citations, agent loops with critic patterns.
- **Personaplex audio** — full-duplex speech-to-speech architecture, Twilio Media Streams bridge, voice agent state management, escalation patterns.
- **Agent infrastructure** — the four primitives (memory, tool registry, observability, approval) at the production grade required for Tier-4.
- **Container orchestration / deployment** — what's required to ship per-client GPU deployments. Docker, the orchestration layer, secrets management, observability for distributed agent systems.

## Gates

Goals don't track without gates. Each domain in scope needs a gate that confirms the skill is at the level required for the next ladder rung.

### Suggested gate framework

- **Beginner gate:** can read code in this domain confidently and can write basic patterns from scratch.
- **Working gate:** can ship a production-grade module in this domain that gets used by Optimus offerings without needing rework. Code passes review by an external standard (e.g., Greg-Osuri test per [[../portfolio-standards]]).
- **Teaching gate:** can teach this skill in Optimus University (2027-2028 horizon, gated on $100k+ revenue from the methods being taught — see `memory/project_optimus-university.md`).

Per-domain gate-current-state assessment lives in the Updates section as it gets evaluated.

## Updates

> Append-only. Each entry: `### YYYY-MM-DD — <domain> — <gate-state-or-decision>`.
