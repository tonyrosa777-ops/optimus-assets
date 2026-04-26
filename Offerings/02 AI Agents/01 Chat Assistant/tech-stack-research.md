# Chat Assistant — Tech Stack Research

Options to investigate, not decisions. Decisions get promoted into the README's "Product spec" section once chosen and proven out.

## Widget framework

| Option | Pros | Cons |
|---|---|---|
| **Custom React widget + drop-in script** | Full control over UX, brand integration, streaming. No third-party lock-in. Co-located with Vercel-hosted Optimus sites. | Build everything from scratch. More maintenance surface. |
| **Vercel AI SDK `useChat` + custom UI** | Streaming + tool calling primitives ready to go. Still our UX. | Still custom UI work, but shorter path. |
| **Intercom-style hosted chat** | Zero build cost. | Off-domain redirect risk, generic UX, recurring fee per client, breaks the conversion-first positioning. |
| **Crisp / Tidio / similar SaaS** | Cheap. | Same problems as Intercom — off-brand, generic, conflicts with Optimus's "every site looks bespoke" positioning. |

**Lean: custom React widget with Vercel AI SDK under the hood.** Verify against the dogfood instance before committing.

## Streaming UX library

| Option | Notes |
|---|---|
| **Vercel AI SDK** | Streaming + tool calling + UI hooks. First-party with Vercel. Strong default. |
| **LangChain JS streaming** | More machinery than we need for a single-agent chat widget. |
| **Hand-rolled SSE** | Total control. More code we have to maintain. |

**Lean: Vercel AI SDK.** Already in the wider stack.

## Per-client knowledge base — RAG approach

The widget needs to answer questions grounded in the client's site (services, pricing, FAQ, hours, locations, policies). Options:

| Approach | Pros | Cons |
|---|---|---|
| **Full-context inlining** — at build time, dump `/data/site.ts` content into the system prompt with prompt caching | Zero infra. Cache hit on every turn after the first. Simple. | Breaks if the site copy is huge (multi-page services × multi-locations × FAQ). Latency on first turn. |
| **Embedded RAG with Supabase pgvector** | Scales to large sites. Already have Supabase in the stack. | Build + maintenance overhead per client. Embeddings need refresh on copy changes. |
| **Hybrid: inline core copy + retrieve long-tail (blog, location pages)** | Best of both. | More moving parts. |

**Default position: start with full-context inlining.** Most Optimus client sites fit easily in a cached system prompt. Only move to RAG when the cache miss / context-overflow problem actually appears in production.

## Open questions

- Where does the client read their conversation analytics? (Optimus admin dashboard? Email digest? Embedded in client site?)
- How does the client edit the assistant's persona / disallow topics without redeploying? (Sanity entry? `/data/site.ts` field? Admin UI?)
- Multi-language sites: do we ship one assistant per language or one assistant that detects language?

---

#offering/ai-chat #status/draft
