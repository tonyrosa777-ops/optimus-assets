---
schema-version: 1
last-updated: 2026-04-29
tags: [offering/autonomous-employee, status/in-development]
---

# Optimus Autonomous AI Employee — Live Instance (Drink-Own-Champagne)

Optimus's own custom-trained Tier-4 Autonomous AI Employee. The instance that runs Optimus's marketing pipeline + inbound qualification + scheduling autonomously by **2027-Q3** — proving the product on Optimus before selling it to Tier-4 clients.

Cross-references:
- Product spec: [[../../../Offerings/02 AI Agents/04 Autonomous Employee/README|product spec]]
- Build spec: [[../../../Offerings/02 AI Agents/04 Autonomous Employee/python-architecture|python-architecture.md]]
- Harness selection: [[../../../Offerings/02 AI Agents/04 Autonomous Employee/harness-research|harness-research.md]]
- Founder layer governing this instance: [[../../../anthony-rosa/north-star]] § The Drink-Own-Champagne Milestone

---

## Stack

Per the canonical Optimus stack + Tier-4 additions:

- **Backend:** Python · FastAPI control plane · anthropic SDK (Sonnet routine, Opus high-stakes reasoning) · Pydantic v2 · supabase-py
- **Schedule:** APScheduler for periodic cycles (Marketing Team module pre-loaded with Sunday 18:00 EST cron)
- **Voice channel** (when wired): Twilio Programmable Voice + Media Streams + NVIDIA Personaplex 7B
- **Agent harness:** TBD per `harness-research.md` — selected at this dogfood build kickoff (planned 2027-H1)
- **Deployment:** Self-hosted on owned GPU initially; migration target is private per-client GPU compute per `python-architecture.md` § Deployment options

**Per-client (or per-deployment) build only — no multi-tenant SaaS architecture.** Every Tier-4 employee — including Optimus's own — is its own deployment on the canonical Optimus Python stack.

---

## Purpose — The Drink-Own-Champagne 2027-Q3 milestone

By **end of 2027-Q3**, Optimus's own operations run on this instance:
- **Marketing pipeline running autonomously** — coordinating with Marketing Team's strategy outputs, expanding to direct-posting (with approval gates), monitoring engagement, surfacing saturation/identity signals to Anthony in weekly reports.
- **Inbound qualification running autonomously** — coordinating with the Chat Assistant + Voice Receptionist instances, applying scoring rubrics, escalating only what genuinely needs human attention.
- **Scheduling running autonomously** — owning the Calendly integration, prioritizing slots, handling reschedules, sending confirmations, blocking time for deep work.
- **Anthony's daily attention to operational marketing/inbound/scheduling tasks: near zero.**

This is not a marketing claim. It is the operational target. Slips get explicit attention in [[../../../anthony-rosa/wins.md]] — not silent rolling.

---

## Why this instance matters strategically

Three reasons it is the highest-priority deployment in the entire Optimus AI agent layer:

1. **The strongest sales asset.** "We run our own company on this" beats every case study, every slide, every demo. Every Tier-4 prospect can see Optimus's own employee on Optimus's own marketing site, working in public, in real time.
2. **The first true exercise of Tier-4 architecture.** The four primitives ([[../../../Offerings/02 AI Agents/shared-knowledge/agent-infrastructure]]) get extended with the harness on top here first — every paying Tier-4 client benefits from the operational learning Optimus eats first.
3. **One of the four moats** per [[../../../anthony-rosa/north-star]] § The Moat point 3 — by 2029 this is 24+ months of dogfood data nobody else has. It compounds.

---

## Tracking

| Field | Value |
|---|---|
| Repo | `optimus-employee-self` (TBD on GitHub creation, likely private) |
| Harness | TBD per `harness-research.md` — selected at build kickoff |
| Deployment | TBD — initial owned-GPU; evaluate private GPU compute deployment as Year-2 unfolds |
| Tools graduated to autonomous | TBD — tracked weekly via the WeeklyReport schema in `python-architecture.md` |
| Tools still approval-gated | TBD — high-stakes actions (external email, public posts, payments) stay approval-gated indefinitely |
| Anthony attention budget per week (target) | <2 hours by end of 2027-Q3 |

---

## Status

**Scoped, build target Q3 2027 for the Drink-Own-Champagne milestone.**

Build sequence:
1. **2026** — Marketing Team Tier-3 dogfood instance hardens. Voice Receptionist Tier-2 dogfood instance hardens. The four agent-infrastructure primitives prove out.
2. **2027-H1** — Harness selection finalized in `harness-research.md`. Tier-4 reference architecture (this instance) build begins. First custom-trained Optimus persona deployed.
3. **2027-Q3** — Drink-Own-Champagne milestone. Operational marketing/inbound/scheduling running autonomously.
4. **2027-Q4 → 2028** — Tier-4 reference architecture battle-tested on Optimus's own ops; first paying Tier-4 client onboarded.

Waiting on: Marketing Team Tier-3 production-hardening (prerequisite), Voice Receptionist Tier-2 dogfood call quality validated, harness research completed.

---

## Cross-references

- Product spec: [[../../../Offerings/02 AI Agents/04 Autonomous Employee/README|product spec]]
- Build spec: [[../../../Offerings/02 AI Agents/04 Autonomous Employee/python-architecture|python-architecture.md]]
- Harness selection log: [[../../../Offerings/02 AI Agents/04 Autonomous Employee/harness-research|harness-research.md]]
- The four primitives: [[../../../Offerings/02 AI Agents/shared-knowledge/agent-infrastructure]]
- Marketing Team Tier-3 dogfood instance (prerequisite): [[../marketing-team/README]]
- Voice Receptionist Tier-2 dogfood instance: [[../voice-receptionist/README]]
- Site this lives on: [[../../website/README]]
- Brand voice this speaks in: [[../../brand/README]]
