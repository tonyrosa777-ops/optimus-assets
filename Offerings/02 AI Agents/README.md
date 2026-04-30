---
schema-version: 1
last-updated: 2026-04-29
tags: [offering/all, status/active]
---

# AI Agents

Four products grouped under one umbrella. Each is a Claude/Personaplex-powered agent built on the canonical Optimus Python stack — FastAPI · anthropic SDK · Pydantic v2 · supabase-py · Twilio · Personaplex. Each ships as a productized SKU on top of the website-development core.

This umbrella is governed by [`../../anthony-rosa/north-star.md`](../../anthony-rosa/north-star.md) (founder layer). Read that first before any architectural decision on any of the four products.

---

## What "AI Agent" means at Optimus

Not a chatbot wrapper. Not a single LLM call. An agent has:

- A model (Claude Opus / Sonnet / Haiku via the anthropic SDK; Personaplex 7B for voice)
- A defined set of tools it can call (CRM lookup, calendar booking, knowledge base retrieval, action-taking webhooks) — typed, permissioned, rate-limited
- Conversational or stateful memory between turns
- Structured outputs the rest of the system can act on (Pydantic-validated)
- Evals that catch regressions before clients see them

Every Optimus agent is built on the **four shared infrastructure primitives** in [`shared-knowledge/agent-infrastructure.md`](shared-knowledge/agent-infrastructure.md): memory store · tool registry · observability layer · approval/sandboxing. These primitives are the compounding artifact — they turn what would otherwise be three discrete codebases into a composable agent stack that Tier-4 inherits wholesale.

---

## The four-tier upsell ladder

| Tier | Product | Setup | MRR | Folder |
|---|---|---|---|---|
| **1** | Chat Assistant | $1,500 | $597 | [[01 Chat Assistant/README]] |
| **2** | Voice Receptionist | $2,500 | $797 | [[02 Voice Receptionist/README]] |
| **3** | Marketing Team — Self Learning Content Engine | $3,500 | $1,497 | [[03 Marketing Team/README]] |
| **4** | Autonomous AI Employee — custom-trained per client | $7,500–15,000 | $2,500–5,000+ | [[04 Autonomous Employee/README]] |

**Tier 3 (Marketing Team) is the prerequisite template every Tier-4 build inherits.** The marketing module ships preloaded into every Autonomous Employee. Marketing Team is also a standalone product — clients who don't need full autonomy can stay at Tier 3 indefinitely.

---

## Why grouped

Three reasons these live under one umbrella instead of four siblings of Website Development:

1. **One canonical Python stack across all four.** FastAPI + anthropic SDK + Pydantic + supabase-py + Twilio + Personaplex. The stack is documented once at [`shared-knowledge/tech-stack.md`](shared-knowledge/tech-stack.md). No per-product hosting sprawl.
2. **Four shared agent-infrastructure primitives** — memory store · tool registry · observability layer · approval/sandboxing — used by Marketing Team, Voice Receptionist, and Tier-4 Autonomous Employee. Defined once at [`shared-knowledge/agent-infrastructure.md`](shared-knowledge/agent-infrastructure.md). Tier-4 IS these primitives with an open-source harness on top.
3. **Shared learning input.** The daily learning pipeline (Anthropic courses, agentic-AI YouTube, applied-AI write-ups) feeds all four products. A concept proven out in `Optimus Academy/` gets promoted to the shared layer below as soon as it applies.

---

## The leverage layer

When a pattern, tech choice, or concept applies across multiple products, it lives in `shared-knowledge/` — never duplicated into each product folder.

- [[shared-knowledge/tech-stack]] — the canonical Optimus Python stack (FastAPI · anthropic SDK · Pydantic · supabase-py · Twilio · Personaplex). Source of truth referenced by every product spec.
- [[shared-knowledge/agent-infrastructure]] — the four primitives every agent uses (memory · tools · observability · approval). The compounding artifact across tiers.
- [[shared-knowledge/concept-notes]] — agentic patterns proven across multiple products (memory management, tool calling, evals, prompt caching, etc.)

When a pattern is product-specific (voice latency budgets, chat streaming UX, marketing pillar frameworks, Tier-4 harness selection), it lives in that product's own `tech-stack-research.md` or `python-architecture.md`.

---

## What this umbrella is NOT for

- **Not a place to introduce non-Python tooling for the agent stack.** The stack is Python-first, day one, no exceptions. No visual workflow orchestrators or third-party voice platforms.
- **Not a place to compromise the four primitives.** Every agent uses all four (or marks specific primitives N/A in `/docs/agent-shape.md` with a one-line reason). Inventing a parallel memory store or parallel tool registry per product is the exact failure mode the primitives prevent.

---

#offering/all #status/active
