---
schema-version: 1
last-updated: 2026-04-29
tags: [offering/ai-chat, status/active]
---

# Chat Assistant — Tech Stack

The Tier-1 product. Chat widget that embeds in Optimus-built websites; site-aware; routes to booking on high intent. Backend is Python (FastAPI · anthropic SDK · Pydantic) per the canonical Optimus stack. Frontend is the embeddable widget.

Cross-references:
- [`../shared-knowledge/tech-stack.md`](../shared-knowledge/tech-stack.md) — canonical Optimus stack
- [`../shared-knowledge/agent-infrastructure.md`](../shared-knowledge/agent-infrastructure.md) — the four primitives
- [`../../../anthony-rosa/north-star.md`](../../../anthony-rosa/north-star.md) — founder layer + four-tier ladder

---

## Frontend — the embeddable widget

| Layer | Choice | Why |
|---|---|---|
| **Widget framework** | Custom React widget (drop-in `<script>` tag) | Full control over UX, brand integration, streaming. No third-party lock-in. Co-located with Vercel-hosted Optimus sites. |
| **Streaming UX library** | **Vercel AI SDK** | Streaming primitives + tool-call rendering + UI hooks. First-party with Vercel. Consumes the FastAPI backend's SSE stream cleanly. |
| **Persistence** | localStorage default + optional server-side history | localStorage covers 95% of conversations. Server-side history opt-in for clients who want full transcript review. |

**Explicitly rejected:**
- **LangChain JS** — more machinery than needed for a single-agent chat widget. (We use Python LangChain on the backend selectively, not LangChain JS on the frontend.)
- **Intercom / Crisp / Tidio / similar SaaS** — off-domain redirect risk, generic UX, recurring per-client fee, breaks Optimus's "every site looks bespoke" positioning.

---

## Backend — FastAPI service

The Python backend is the core deliverable. The widget is a thin client of these endpoints.

### Endpoints

```
POST /api/chat            — SSE streaming chat completion
POST /api/intent-score    — single-turn intent scoring (Haiku, low-latency)
POST /api/escalate        — write an escalation event to Supabase + notify human
GET  /api/health          — readiness/liveness
```

### Pydantic schemas

```python
class Message(BaseModel):
    role: Literal["user", "assistant"]
    content: str
    timestamp: datetime

class ChatRequest(BaseModel):
    client_id: str
    session_id: str
    messages: list[Message]
    metadata: Optional[dict] = None  # page URL, referrer, user-agent

class IntentScore(BaseModel):
    session_id: str
    intent: Literal["browsing", "qualifying", "high_intent", "escalation"]
    confidence: float
    suggested_action: Literal["continue", "offer_booking", "escalate", "end_conversation"]

class EscalationPayload(BaseModel):
    client_id: str
    session_id: str
    transcript: list[Message]
    reason: str
    qualified_signals: list[str]
```

### Stack

- **FastAPI** for the HTTP service
- **anthropic SDK** for Claude calls (Sonnet for the conversation; Haiku for `/api/intent-score`)
- **Prompt caching** on the system prompt + the per-client knowledge base (the static portion injected from `/data/site.ts` at deploy time)
- **supabase-py** for session storage when server-side history is enabled
- **Pydantic v2** for every request/response model

### Knowledge base injection

The widget needs to answer questions grounded in the client's site (services, pricing, FAQ, hours, locations). Approach:

- **Default — full-context inlining** with prompt caching. At build time, `/data/site.ts` content gets dumped into the system prompt. Cache hits on every turn after the first; the LLM sees the entire site as context.
- **Escalation to RAG (Supabase pgvector)** only when full-context inlining causes cache misses or context overflow on a particular client (multi-page services × multi-locations × extensive FAQ).

Most Optimus client sites fit easily in a cached system prompt. Default position holds until a real client breaks it.

### Deployment

FastAPI service runs on **Vercel Python Functions** for production (co-located with the Optimus-built sites the widget embeds in). **Fly.io** as fallback for clients with high-volume sites where Vercel function limits bite. Decision per client at first deploy.

---

## What this product teaches toward Tier-4 Autonomous AI Employee

Each Tier-1 build deepens the Optimus capability stack toward Tier-4. Specifically, the Chat Assistant teaches:

- **System-prompt design.** Crafting a system prompt that gives the LLM stable identity, scoped knowledge, and clear decision criteria. Tier-4 employees inherit this design discipline scaled to multi-tool action surfaces.
- **Streaming.** SSE from FastAPI to the React widget. Tier-4 employees stream their reasoning traces to client-facing dashboards using the same pattern.
- **Prompt caching at scale.** Measuring cache hit rate, knowing what to cache and what not to. Tier-4's cost economics depend on this discipline.
- **Intent detection.** Separating "user is browsing" from "user is qualifying" from "user wants action." Tier-4 employees use richer versions of this same classification to decide when to invoke action-taking tools.
- **Escalation triggers.** When the agent should hand off to a human. The Approval primitive in `agent-infrastructure.md` § 4 is a generalization of this same idea — Chat Assistant's escalation logic is the simplest case of approval-gate routing.

These are the conversational surface every Tier-4 employee inherits when handling chat-channel interactions.

---

## Open questions

- Where does the client read their conversation analytics? (Optimus admin dashboard? Email digest? Embedded in client site?) — Decision at first paying client.
- How does the client edit the assistant's persona / disallow topics without a redeploy? — Likely a Sanity CMS entry per client; TBD at first build.
- Multi-language sites: one assistant per language vs one assistant that detects language — TBD at first multi-language client.

---

#offering/ai-chat #status/active
