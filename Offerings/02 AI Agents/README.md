# AI Agents

Three products grouped under one umbrella. Each is a Claude/LLM-powered agent with tools, memory, and structured outputs. Each ships as a productized SKU on top of the website-development core. All three are in development as of 2026-04-26.

## What "AI Agent" means at Optimus

Not a chatbot wrapper. Not a single LLM call. An agent has:

- A model (Claude Opus / Sonnet / Haiku, or GPT-4o where the existing implementation is already there)
- A defined set of tools it can call (CRM lookup, calendar booking, knowledge base retrieval, webhook fires)
- Conversational or stateful memory between turns
- Structured outputs the rest of the system can act on
- Evals that catch regressions before clients see them

Every Optimus agent is built to this spec, regardless of which product line it lives under.

## The three products

- [[01 Chat Assistant/README|Chat Assistant]] — chat widget that embeds in Optimus-built websites. Site-aware, routes to booking on high intent.
- [[02 Voice Receptionist/README|Voice Receptionist]] — phone agent that answers calls, manages CRM, books the calendar.
- [[03 Marketing Team/README|Marketing Team]] — the Self Learning Content Engine. Weekly n8n workflow, Supabase + GPT-4o, 4-pillar content strategy.

## Why grouped

Three reasons these live under one umbrella instead of three siblings of Website Development:

1. **Shared tech stack.** All three use Anthropic API (or where they don't yet, they will). All three need prompt caching, tool calling, model selection, eval harnesses, and a hosting decision (n8n vs Vercel Functions vs Lambda vs dedicated).
2. **Shared patterns.** Memory management, tool routing, fallback handling, structured output validation, latency budgets — these problems show up in chat, voice, and the content engine in different shapes. Solving them once and writing it down once is the leverage.
3. **Shared learning input.** The daily learning pipeline (Anthropic courses, agentic-AI YouTube, applied-AI write-ups) feeds all three products. A concept proven out in `Optimus Academy/` gets promoted to the shared layer below as soon as it applies.

## The leverage layer

When a pattern, tech choice, or concept applies to all three products, it lives in `shared-knowledge/` — never duplicated into each product folder.

- [[shared-knowledge/concept-notes]] — agentic patterns that apply across all 3 products (memory, tool calling, evals, prompt caching, etc.)
- [[shared-knowledge/tech-stack]] — model selection, providers, hosting, eval framework, common dependencies

When a pattern is product-specific (voice latency budgets, chat streaming UX, marketing pillar frameworks), it lives in that product's own `concept-notes.md` or `tech-stack-research.md`.

---

#offering/all #status/in-development
