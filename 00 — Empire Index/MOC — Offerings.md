# MOC — Offerings

The 4 things Optimus sells. Status, pricing position, and the entry point for each.

## Offering Status Snapshot

| # | Offering | Status | Pricing | Hub |
|---|---|---|---|---|
| 01 | Website Development | Productized — actively shipping | Starter $1,500 / Pro $3,000 (Most Popular) / Premium $5,500 | [[Offerings/01 Website Development/README]] |
| 02 | AI Chat Assistant | In development — embeds in Optimus websites | TBD (likely add-on to Pro/Premium) | [[Offerings/02 AI Agents/01 Chat Assistant/README]] |
| 03 | AI Voice Receptionist | In development — answers calls, syncs CRM + calendar | TBD (standalone subscription) | [[Offerings/02 AI Agents/02 Voice Receptionist/README]] |
| 04 | AI Marketing Team / Content Engine | In development — n8n-driven autonomous marketing | TBD (subscription, tier-based output) | [[Offerings/02 AI Agents/03 Marketing Team/README]] |

## 01 — Website Development

The flagship. Fully productized at three tiers. Every site ships with the full Always-Built Features stack defined in [[CLAUDE]]: Pricing Page (sales tool, deleted before launch), Interactive Quiz, Inline Booking Calendar, Testimonials Page (36 testimonials, paginated 9 per page), Blog (9-10 articles minimum), Shop (always scaffolded). Hero is always the 3-layer stack — see [[glossary]].

Pro is the sell. Pro gets the Most Popular badge. Premium anchors so Pro reads as reasonable. Starter exists as a floor.

- Hub: [[Offerings/01 Website Development/README]]
- Build pipeline: [[CLAUDE]] + [[project-prime]] + [[build-checklist]] + [[website-build-template]]
- Memory: [[knowledge/build-log]]

## 02 — AI Agents (umbrella)

Three distinct AI products live under one umbrella because they share infrastructure (LLM routing, CRM handoff patterns, voice/chat unification, deployment templates). Cross-product patterns belong in `Offerings/02 AI Agents/shared-knowledge/`. Anything specific to a single product belongs in that product's subfolder.

- Umbrella hub: [[Offerings/02 AI Agents/README]]
- Shared patterns: `Offerings/02 AI Agents/shared-knowledge/`

### 01 — Chat Assistant

In development. Designed to embed directly into Optimus-built websites — the user-facing widget that answers questions, qualifies leads, and routes to the booking calendar. Brand-themed per client, just like the booking calendar component. Backend: Claude API with prompt caching.

- Hub: [[Offerings/02 AI Agents/01 Chat Assistant/README]]

### 02 — Voice Receptionist

In development. Answers inbound calls, manages the client's CRM contacts, and books appointments directly into the client's calendar. Optimus's own deployed instance answers Optimus calls (drink your own champagne — see [[glossary]]).

- Hub: [[Offerings/02 AI Agents/02 Voice Receptionist/README]]

### 03 — Marketing Team / Content Engine

In development. n8n workflow runs Sundays 6pm EST against Supabase + GPT-4o, scoring content by 4 pillars (Health / Wealth / Wisdom / Integration) and pushing into the social pipeline. The flagship workflow (`self-learning-content-engine.json`) lives at `Offerings/02 AI Agents/03 Marketing Team/workflows/`.

- Hub: [[Offerings/02 AI Agents/03 Marketing Team/README]]

## When to add a new offering

A new offering gets a hub here only when it is being actively built or sold. Backlog ideas live in `Optimus Academy/apply-to-optimus/` until they have a real product surface. Don't pre-allocate folders for things that don't exist yet — empty folders rot.
