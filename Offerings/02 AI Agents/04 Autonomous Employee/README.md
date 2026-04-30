---
schema-version: 1
last-updated: 2026-04-29
review-by: 2026-10-29
tags: [offering/autonomous-employee, status/in-development]
---

# Autonomous AI Employee — Tier-4

The premium tier. Custom-trained autonomous AI employee for a client's business — purpose-built agent that runs continuously, takes actions, and operates like a member of staff. Privately deployed per client. Same custom-per-client model as Optimus's websites and workflows today.

This is **THE PRODUCT** the four-tier upsell ladder builds toward. See [`../../../anthony-rosa/north-star.md`](../../../anthony-rosa/north-star.md) § The End Goal for the strategic destination.

Cross-references:
- [`harness-research.md`](harness-research.md) — open-source harness comparison (OpenClaw / Hermes / Letta / Pydantic AI / LangGraph)
- [`python-architecture.md`](python-architecture.md) — complete build spec
- [`../shared-knowledge/agent-infrastructure.md`](../shared-knowledge/agent-infrastructure.md) — the four primitives Tier-4 inherits + extends
- [`../03 Marketing Team/python-architecture.md`](../03%20Marketing%20Team/python-architecture.md) — the prerequisite template every Tier-4 build inherits

---

## Positioning

> Custom-trained autonomous AI employee for your business. Per-client harness, per-client memory, per-client tool surface, per-client private GPU deployment (deployment options in [`python-architecture.md`](python-architecture.md)).

A Tier-4 employee runs continuously inside the client's stack:
- Observes events (CRM updates, calendar changes, inbox arrivals, schedule deadlines)
- Decides when action is warranted, against the four agent-infrastructure primitives
- Takes action (sends emails, books meetings, updates CRM, posts to social — all approval-gated initially, graduating to autonomy)
- Reports weekly on what it did, why, and what's next

Think OpenClaw or Hermes class — but Optimus builds and deploys them privately for each business that buys Tier-4.

---

## Pricing

| Component | Range | Drivers |
|---|---|---|
| **Setup** | $7,500–15,000 | Agent surface area: # of tools, # of integrations, training data prep, harness customization |
| **Monthly** | $2,500–5,000+ | Compute (private per-client GPU) + ongoing tuning + observability dashboard + monthly review session |

Custom-priced per client based on agent surface area. The price is the price — no haggling, no tier discounts. Same model as Optimus's $5,500 Premium website tier: anchor pricing that filters for the right buyer.

---

## What the customer gets

1. **A private GitHub repo** for their employee — the codebase lives in `optimus-employee-[client-slug]` (private, client has read access). The architecture, the prompts, the tool definitions, the memory schema, the eval suite — all in one place.
2. **An architecture diagram** of their stack at `/docs/architecture.png` — what the employee can see, what it can do, where its data lives, who it reports to.
3. **Weekly observability reports** — generated automatically from the Langfuse trace data (or Supabase fallback). What the agent did, every action, success/failure rates, approval-graduation status per tool.
4. **Approval-gated graduation** from human-in-the-loop to autonomy over 30/60/90 days, per the Approval primitive in [`../shared-knowledge/agent-infrastructure.md`](../shared-knowledge/agent-infrastructure.md) § 4.
5. **Quarterly tuning sessions** — review what's working, what's not, what new tools to add, what to retire.

---

## Prerequisite — Marketing Team (Tier-3) deployed first

Tier-4 is not a standalone product. It builds on Tier-3 — Marketing Team is the prerequisite template every Tier-4 employee inherits. Specifically:

- The **memory store** is the same Supabase + pgvector instance, with the Tier-4 employee adding new memory types alongside Marketing Team's pillar/saturation/identity facts.
- The **tool registry** extends — Marketing Team's existing tools (Supabase reads, anthropic calls, ElevenLabs, notification webhooks) are kept; Tier-4 adds a wider tool surface (CRM, calendar, inbox, social, payments — whatever the client authorizes).
- The **observability dashboard** the client already sees from their Marketing Team gets a new agent ID for the Tier-4 employee — same surface, expanded scope.
- The **approval workflow** extends to the new tools.

A client who has been running Marketing Team for 6 months can upgrade to Tier-4 without throwing away anything. The Marketing Team's content strategy module ships **preloaded** as the default tool/memory baseline of every Tier-4 employee.

---

## What it is NOT

- **Not a multi-tenant SaaS.** Each client gets their own deployment. Their data, their model, their compute.
- **Not a one-vertical product.** Optimus does not offer "AI Office Manager for Service Businesses" as a fixed-feature SKU. Every Tier-4 build is custom — same custom-per-client model as Optimus's websites and workflows today.
- **Not a fixed-feature offering.** The agent surface area expands per client. A trades client's employee handles dispatch, parts ordering, customer follow-up. A coach client's employee handles client check-ins, content scheduling, billing. Different clients, different employees, same core architecture.
- **Not built on any visual workflow orchestrator.** Tier-4 is Python-from-day-one — FastAPI control plane, Pydantic schemas, anthropic SDK, supabase-py, plus the open-source harness selected per `harness-research.md`.

---

## Optimus's own Tier-4 — the Drink-Own-Champagne instance

By **2027-Q3**, Optimus's own marketing pipeline + inbound qualification + scheduling runs autonomously on Optimus's own Tier-4 employee. The dogfood instance is tracked at [`../../../Optimus Inc/ai-agents/autonomous-employee/README.md`](../../../Optimus%20Inc/ai-agents/autonomous-employee/README.md).

This is not a marketing claim — it's the operational target. By the time the first paying Tier-4 client ships, Optimus has been running on its own employee for months. That dogfood data is one of the four moats per [`../../../anthony-rosa/north-star.md`](../../../anthony-rosa/north-star.md) § The Moat.

---

## Status

**Scoped. Implementation begins after the first paying Marketing Team (Tier-3) client is live AND the Optimus Tier-3 dogfood instance has hardened.** That sequence ensures the four agent-infrastructure primitives are battle-tested before Tier-4 extends them. Earliest first paying Tier-4 client target: **Year 3 (2028–2029)** per [`../../../anthony-rosa/ai-engineer-roadmap.md`](../../../anthony-rosa/ai-engineer-roadmap.md).

#offering/autonomous-employee #status/in-development
