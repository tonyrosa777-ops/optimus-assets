# Shared Tech Stack — AI Agents

Cross-product tech notes. Anything that applies to chat AND voice AND the marketing team belongs here. Product-specific decisions live in each product's own `tech-stack-research.md`.

## Model selection

Default to Anthropic models. Where an existing implementation already runs on GPT-4o (Marketing Team today), document the migration path but don't break what works.

| Tier | When to use |
|---|---|
| **Claude Opus** | Complex reasoning, multi-step tool routing, ambiguous user intent. Use when the agent needs to make a real decision, not just classify or extract. Voice receptionist call-routing logic. Chat assistant intent disambiguation. Strategy generation in the Marketing Team. |
| **Claude Sonnet** | General agent loops, conversational turns, summarization, structured output generation. The default for the inner loop of an agent that's already had its routing decision made. Most chat assistant turns. |
| **Claude Haiku** | Cheap classification, intent detection, extraction, guardrails. Use when latency and cost matter more than nuance. Pre-router for chat assistant. Real-time barge-in detection for voice. Content-pillar tagging in the Marketing Team. |

Pick the cheapest model that reliably hits the eval bar for the task. Do not default to Opus everywhere — the cost compounds fast and most agent turns don't need it.

## Provider stack

- **Anthropic API** — primary. Every Anthropic-API project at Optimus uses prompt caching by default (per the existing `claude-api` skill convention). Cache the system prompt, the tool definitions, and the conversation history up to the last user turn. Do not skip this — cache hit rate directly drives cost and latency.
- **OpenAI** — only where an existing implementation already runs on it (Marketing Team's GPT-4o strategy generation). Migration to Claude is on the roadmap but is not blocking.
- **Vercel AI Gateway** — TBD. Investigate for unified API + provider failover + cost tracking once we have 2+ models in production.

## Hosting options

No single answer across all 3 products. TBD per product, but the candidates are:

| Option | Best for | Notes |
|---|---|---|
| **n8n** | Scheduled workflows, multi-step orchestration with HTTP nodes | Proven for Marketing Team — workflow already in production. Less suited for low-latency request/response. |
| **Vercel Functions** | Chat assistant request/response, webhook receivers | Co-located with the Optimus-built websites the chat widget embeds in. Streaming via Vercel AI SDK is well-supported. |
| **AWS Lambda** | Long-running async jobs, voice telephony glue | More setup overhead than Vercel. Reserve for cases where Vercel limits bite. |
| **Dedicated server (Railway, Fly, Render)** | Voice agents that need persistent WebSocket connections, anything with strict latency SLAs | Voice receptionist is the likely candidate. TBD. |

## Eval framework

**TBD: define eval harness shared across all 3 products.** Open questions:

- Anthropic's evals tooling vs Promptfoo vs Inspect AI vs custom
- Where to store eval datasets (versioned in repo? Supabase?)
- CI integration — block deploy on eval regression?
- Per-product eval dimensions: chat (helpfulness, escalation accuracy, booking conversion), voice (intent recognition, latency, transfer accuracy), marketing (pillar tagging accuracy, strategy quality scoring)

This is a cross-product concern. Solving it once for chat first, then extending to voice and marketing.

## Common dependencies (stub)

Things every agent product is likely to need. Pick the cross-product default once each, then reuse.

- **Webhook receiver** — for inbound events (Calendly bookings, Twilio call events, social platform callbacks)
- **Vector DB** — only if RAG is in scope. Candidates: Supabase pgvector (already in stack), Pinecone, Turbopuffer
- **State store** — Supabase (already in stack for Marketing Team) or Redis (Upstash via Vercel) for fast session state
- **Observability** — TBD. Langfuse, Helicone, or roll-your-own via Supabase logging

---

#offering/all #status/draft
