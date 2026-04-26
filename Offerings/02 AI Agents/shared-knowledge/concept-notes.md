# Shared Concept Notes — AI Agents

Patterns that apply to chat + voice + marketing alike. To be filled as concepts from `Optimus Academy/concepts/` get applied across all 3 agent products and prove out in production.

When a concept note in `Optimus Academy/concepts/` proves out across all 3 agent products, summarize it here with a wikilink back to the source. The Academy is where I learn it; this file is where it becomes Optimus IP.

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

## Promotion criteria

Before adding a pattern here, it must:

1. Be applied in at least 2 of the 3 agent products
2. Have a working implementation reference (not just a theory)
3. Solve a real problem we hit in production, not a hypothetical one

If a pattern only applies to one product, it lives in that product's own `concept-notes.md`.

---

#offering/all #status/draft
