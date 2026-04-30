# MOC — Offerings

What Optimus sells. Status, pricing, and the entry point for each.

The Offerings hub is governed by [`../anthony-rosa/north-star.md`](../anthony-rosa/north-star.md) (founder layer). Read that first before any architectural decision on any offering.

## Offering Status Snapshot

### Website Development (productized)

| # | Offering | Status | Pricing | Hub |
|---|---|---|---|---|
| 01 | Website Development | Productized — actively shipping | Starter $1,500 / Pro $3,000 (Most Popular) / Premium $5,500 | [[Offerings/01 Website Development/README]] |

### AI Agents — the four-tier upsell ladder

| Tier | Product | Status | Pricing | Hub |
|---|---|---|---|---|
| 1 | AI Chat Assistant | In development | $1,500 setup / $597 MRR | [[Offerings/02 AI Agents/01 Chat Assistant/README]] |
| 2 | AI Voice Receptionist (Personaplex on Twilio) | In development | $2,500 setup / $797 MRR | [[Offerings/02 AI Agents/02 Voice Receptionist/README]] |
| 3 | AI Marketing Team / Content Engine | In development | $3,500 setup / $1,497 MRR | [[Offerings/02 AI Agents/03 Marketing Team/README]] |
| 4 | AI Autonomous Employee (custom-trained per client) | In development | $7,500–15,000 setup / $2,500–5,000+ MRR | [[Offerings/02 AI Agents/04 Autonomous Employee/README]] |

Total addressable MRR per fully-onboarded client: ~$5,400–7,900/mo.

## 01 — Website Development

The flagship. Fully productized at three tiers. Every site ships with the full Always-Built Features stack defined in [[CLAUDE]]: Pricing Page (sales tool, deleted before launch), Interactive Quiz, Inline Booking Calendar, Testimonials Page (36 testimonials, paginated 9 per page), Blog (9-10 articles minimum), Shop (always scaffolded). Hero is always the 3-layer stack — see [[glossary]].

Pro is the sell. Pro gets the Most Popular badge. Premium anchors so Pro reads as reasonable. Starter exists as a floor.

- Hub: [[Offerings/01 Website Development/README]]
- Build pipeline: [[CLAUDE]] + [[project-prime]] + [[build-checklist]] + [[website-build-template]]
- Memory: [[knowledge/build-log]]

## 02 — AI Agents (umbrella)

Four products under one umbrella sharing the **canonical Optimus Python stack** (FastAPI · anthropic SDK · Pydantic v2 · supabase-py · Twilio · Personaplex) and the **four agent infrastructure primitives** (memory · tools · observability · approval) — defined once in `shared-knowledge/`, used by every product. Cross-product patterns belong in `Offerings/02 AI Agents/shared-knowledge/`. Anything specific to a single product belongs in that product's subfolder.

- Umbrella hub: [[Offerings/02 AI Agents/README]]
- Canonical stack: [[Offerings/02 AI Agents/shared-knowledge/tech-stack]]
- Four primitives: [[Offerings/02 AI Agents/shared-knowledge/agent-infrastructure]]

### 01 — Chat Assistant — Tier 1

In development. Designed to embed directly into Optimus-built websites — the user-facing widget that answers questions, qualifies leads, and routes to the booking calendar. Brand-themed per client, just like the booking calendar component. **Backend:** Python · FastAPI · anthropic SDK + prompt caching · Pydantic. **Frontend:** TypeScript/React + Vercel AI SDK as the SSE client.

- Hub: [[Offerings/02 AI Agents/01 Chat Assistant/README]]

### 02 — Voice Receptionist — Tier 2

In development. Answers inbound calls, manages the client's CRM contacts, and books appointments directly into the client's calendar. **Stack:** Twilio Programmable Voice + Media Streams · NVIDIA Personaplex 7B (full-duplex S2S) · FastAPI WebSocket bridge · anthropic SDK (Sonnet) for reasoning fallback. Optimus's own deployed instance answers Optimus calls (drink-own-champagne — see [[glossary]]).

- Hub: [[Offerings/02 AI Agents/02 Voice Receptionist/README]]
- Build spec: [[Offerings/02 AI Agents/02 Voice Receptionist/personaplex-architecture]]

### 03 — Marketing Team / Content Engine — Tier 3

In development. **The first true scheduled-cron agent in the Optimus stack** and the prerequisite template every Tier-4 build inherits. Python service with APScheduler running Sundays 18:00 EST against Supabase + Claude (Sonnet weekly · Opus monthly deep-eval). Per-client configurable pillars. Build spec lives at `Offerings/02 AI Agents/03 Marketing Team/python-architecture.md`.

- Hub: [[Offerings/02 AI Agents/03 Marketing Team/README]]
- Build spec: [[Offerings/02 AI Agents/03 Marketing Team/python-architecture]]

### 04 — Autonomous AI Employee — Tier 4

In development. **THE PRODUCT** the four-tier upsell ladder builds toward. Custom-trained autonomous AI employee per client, running on an open-source agent harness (OpenClaw / Hermes / Letta / Pydantic AI / LangGraph — selection in `harness-research.md`). Per-client private GPU deployment. Marketing Team module pre-loaded as the default tool/memory baseline of every Tier-4 build.

- Hub: [[Offerings/02 AI Agents/04 Autonomous Employee/README]]
- Build spec: [[Offerings/02 AI Agents/04 Autonomous Employee/python-architecture]]
- Harness selection log: [[Offerings/02 AI Agents/04 Autonomous Employee/harness-research]]

## When to add a new offering

A new offering gets a hub here only when it is being actively built or sold. Backlog ideas live in `Optimus Academy/apply-to-optimus/` until they have a real product surface. Don't pre-allocate folders for things that don't exist yet — empty folders rot.
