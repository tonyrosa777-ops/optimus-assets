# Shared Concept Notes — AI Agents

Patterns that apply across all four agent products (Chat · Voice · Marketing · Tier-4 Autonomous Employee). To be filled as concepts from `Optimus Academy/concepts/` get applied across multiple products and prove out in production.

Cross-references:
- [`tech-stack.md`](tech-stack.md) — the canonical Python stack
- [`agent-infrastructure.md`](agent-infrastructure.md) — the four primitives (memory · tools · observability · approval) every agent uses
- [`../../../anthony-rosa/north-star.md`](../../../anthony-rosa/north-star.md) — founder layer rationale for the stack and the upsell-ladder progression

When a concept note in `Optimus Academy/concepts/` proves out across multiple agent products, summarize it here with a wikilink back to the source. The Academy is where I learn it; this file is where it becomes Optimus IP.

## Patterns to capture

Stub list. Each becomes its own H2 section with a wikilink to the Academy concept once it's been applied and validated:

- **Agentic loops** — the basic perceive → reason → act → observe cycle. Every agent product runs one of these.
- **Tool calling** — schema design, parameter validation, error handling, parallel vs sequential tool calls.
- **Conversational memory** — what to keep in the prompt, what to summarize, what to push to long-term store. Differs by product (chat: session-bound, voice: call-bound, marketing: 30-day rolling window).
- **Context window management** — when to compact, when to summarize, when to start fresh. Cost-per-turn implications.
- **Evals** — defining the rubric, building the dataset, regression-testing prompts.
- **Prompt caching** — what to cache, what not to, measuring cache hit rate. Mandatory on every Claude API call (see [[tech-stack]]).
- **Structured outputs** — JSON mode, tool use as output enforcement, validation layers.
- **Fallback handling** — what to do when the model returns garbage, when a tool fails, when the API is down.
- **Latency budgets** — voice tolerates ~300ms, chat tolerates ~2s, marketing tolerates 30s. Architectures differ accordingly.
- **Identity and tone** — keeping the agent on-brand across long conversations and across product lines.

## Python implementation patterns

Every Optimus agent is Python from day one. Implementation patterns shared across all four products:

- **Pydantic for tool schemas.** Every tool an agent can call has a Pydantic input model and a Pydantic output model. The Anthropic SDK consumes the JSON-schema export. Validation happens at the FastAPI orchestration tier before the LLM ever sees the tool result. Reference shapes in [`agent-infrastructure.md`](agent-infrastructure.md) § Tool registry.
- **FastAPI for backend services.** Every agent backend is a FastAPI service. SSE for streaming chat. WebSocket for Voice Receptionist Twilio Media Streams. Standard REST for everything else. Auto-generated `/docs` (Swagger UI) is the API documentation requirement from [`../../../anthony-rosa/portfolio-standards.md`](../../../anthony-rosa/portfolio-standards.md) § 4.
- **supabase-py for state.** Memory store, observability events, approval requests, tool registry — all in Supabase Postgres tables typed via Pydantic. pgvector for episodic + semantic memory embeddings.
- **anthropic SDK + prompt caching as default.** Every Claude API call uses the SDK directly with caching enabled. Cache hit rate is a first-class observability metric. No exceptions.
- **APScheduler for cron loops.** Marketing Team's Sunday 18:00 EST run, Tier-4's per-employee scheduled tasks, any periodic sweep — all APScheduler inside the FastAPI service. No external cron infrastructure.

## Promotion criteria

Before adding a pattern here, it must:

1. Be applied in at least 2 of the 4 agent products
2. Have a working implementation reference (not just a theory)
3. Solve a real problem we hit in production, not a hypothetical one

If a pattern only applies to one product, it lives in that product's own `concept-notes.md`.

---

#offering/all #status/active
