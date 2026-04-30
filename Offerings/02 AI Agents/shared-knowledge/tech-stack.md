---
schema-version: 1
last-updated: 2026-04-29
review-by: 2026-10-29
tags: [offering/all, layer/optimus-os, status/active]
---

# Shared Tech Stack — AI Agents

The canonical Optimus stack. Source of truth for every agent product.

This file is governed by [`anthony-rosa/north-star.md`](../../../anthony-rosa/north-star.md) (founder layer). When proposing or making any architectural decision on the AI agent stack, read north-star first. Cross-reference: [`agent-infrastructure.md`](agent-infrastructure.md) defines the four primitives every agent uses.

---

## Runtime commitment — Python first

Every Optimus AI agent product (Tiers 1–4) is built once, correctly, in Python from day one. No phasing. No migration. No "current state vs target state."

| Layer | Stack |
|---|---|
| **Backend services** (chat API, voice agent, content engine, autonomous employee, all webhooks) | **FastAPI** · **anthropic SDK** (Claude API direct) · **Pydantic v2** · **supabase-py** |
| **Client-side widgets** (Chat Assistant only — embedded in Optimus sites) | TypeScript/React · Vercel AI SDK as a compatible client streaming library for the FastAPI backend |
| **Telephony** | **Twilio Programmable Voice** (PSTN ↔ Media Streams WebSocket) · **Twilio SMS** for confirmations across all four products |
| **Voice model** | **NVIDIA Personaplex 7B** (full-duplex speech-to-speech) — Twilio Media Streams bridge, FastAPI orchestration for tool calls (Personaplex native tool-calling not yet shipped — orchestration via the Inner Monologue text channel pattern) |
| **Calendar** | **Calendly API** (already standardized — same backend the website's BookingCalendar uses) |
| **Storage** | **Supabase Postgres** (sessions, transcripts, performance data, strategy outputs, agent memory · pgvector for embeddings) |
| **Scheduling** (Marketing Team weekly cron, autonomous-employee scheduled tasks) | **APScheduler** in the FastAPI service |
| **Agent infrastructure primitives** (used by Marketing Team, Voice Receptionist, Tier-4 Autonomous Employee) | Memory store · Tool registry · Observability layer · Approval/sandboxing — defined in [`agent-infrastructure.md`](agent-infrastructure.md) |
| **Tier-4 only — agent harness** | Open-source harness (OpenClaw / Hermes / Letta / Pydantic AI / LangGraph) — selection per [`../04 Autonomous Employee/harness-research.md`](../04%20Autonomous%20Employee/harness-research.md) |
| **Tier-4 only — deployment** | Private per-client GPU compute (see [`../04 Autonomous Employee/python-architecture.md`](../04%20Autonomous%20Employee/python-architecture.md)) |
| **Every shipped system** | Public GitHub repo · README · `/docs/architecture.png` · FastAPI auto-docs (or Postman collection) · `/docs/retro.md` · `/docs/agent-shape.md` (memory schema · tool surface · observability hooks — N/A on non-agent systems but the file is still required) |

**No visual workflow orchestrators in this stack — not as the engine, not as an optional dashboard, not shipped to clients in any form.** The orchestration runs in FastAPI; if a client wants visual workflow editing, that's a future client-facing dashboard built on top of the FastAPI control plane — never the engine.

---

## Model selection (Anthropic only)

Every Optimus agent uses Anthropic's Claude family. Pick the cheapest model that reliably hits the task's eval bar — do not default to Opus everywhere; cost compounds fast.

| Tier | When to use |
|---|---|
| **Claude Opus** | Complex reasoning, multi-step tool routing, ambiguous user intent. The decision-making turn, not the execution turn. Voice receptionist call-routing logic. Chat assistant intent disambiguation. Strategy generation in the Marketing Team's monthly deep-eval. Tier-4 high-stakes action approval. |
| **Claude Sonnet** | General agent loops, conversational turns, summarization, structured output generation. The default for the inner loop of an agent that's already had its routing decision made. Most chat assistant turns. Marketing Team weekly synthesis. Tier-4 routine tool calls. |
| **Claude Haiku** | Cheap classification, intent detection, extraction, guardrails. Use when latency and cost matter more than nuance. Pre-router for chat assistant. Real-time barge-in detection / intent extraction in voice. Content-pillar tagging in the Marketing Team. Approval-gate triage in Tier-4. |

---

## Prompt caching — mandatory, not optional

Every Anthropic API call at Optimus uses prompt caching by default. Cache the system prompt, the tool definitions, and the conversation history up to the last user turn. Measure cache hit rate per system — track it as a first-class observability metric (see the observability primitive in `agent-infrastructure.md`).

Cache hit rate is one of the strongest cost levers in the stack. Skipping prompt caching is the equivalent of skipping prepared statements in SQL — it works but it's professionally negligent.

---

## Backend hosting — FastAPI deploy targets

Each agent product chooses one. The choice is per-product, made at first deploy:

| Target | Best for | Notes |
|---|---|---|
| **Vercel Python Functions** | Chat Assistant backend (co-located with Optimus-built websites) | Same surface as the website builds; easy CI/CD via the existing Vercel projects |
| **Fly.io** | Marketing Team weekly cron, Voice Receptionist webhook tier | Persistent processes, low cold-start, machines-as-a-service |
| **Railway** | Quick-start dev/staging environments before production lock-in | Cheapest path to a deployed FastAPI |
| **Per-client private GPU compute** | Tier-4 Autonomous Employee runtime | See `04 Autonomous Employee/python-architecture.md` |

There is no shared "default" host. Each product picks at first deploy and documents the choice in its `/docs/architecture.png`.

---

## Eval framework

Every Optimus agent ships with an eval suite as a first-class deliverable. Per-product dimensions:

- **Chat Assistant** — helpfulness, escalation accuracy, booking conversion
- **Voice Receptionist** — intent recognition, latency P50/P95, transfer accuracy, booking conversion
- **Marketing Team** — pillar tagging accuracy, strategy quality scoring (rubric-graded), saturation detection precision/recall
- **Tier-4 Autonomous AI Employee** — per-tool action correctness, approval-graduation accuracy, end-to-end task completion against client-defined success criteria

Eval datasets live versioned in the relevant repo's `/evals/` directory (Pydantic-typed test cases). CI integration: block deploy on eval regression beyond a defined threshold.

Tooling decision: **TBD at first agent's first eval suite.** Candidates: Anthropic's evals tooling · Promptfoo · Inspect AI · custom Pydantic + pytest harness. Pydantic+pytest is the lightweight default unless a candidate proves clearly better for one of the four products — chosen at the first agent's eval-build moment, then propagated.

---

## Common dependencies

Things every agent product is likely to need. Pick the cross-product default once each:

- **Webhook receiver** — FastAPI endpoints (built-in, no separate dependency)
- **Vector DB** — Supabase pgvector (already in stack)
- **State store** — Supabase Postgres (already in stack); Upstash Redis if fast session state is needed and Postgres-only proves too slow
- **Observability** — see `agent-infrastructure.md` § Observability layer (Langfuse default · Supabase fallback)

---

## What this file is NOT

- Not the place to document a per-product implementation. That lives in each product's `tech-stack-research.md` and `python-architecture.md`.
- Not the place to make stack decisions on a one-off basis. The stack is the stack. If a build needs something off this list, propose it — and either the proposal becomes a new line on this table (cross-product), a new line in the relevant product's tech-stack-research (per-product), or it gets rejected.
- Not the place where deployment-thesis content lives. Stack tools live here; the long-term private per-client GPU compute thesis is documented in [`../../../anthony-rosa/north-star.md`](../../../anthony-rosa/north-star.md) and concrete deployment options live in `04 Autonomous Employee/python-architecture.md`.

---

#offering/all #layer/optimus-os #status/active
