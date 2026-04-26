# Chat Assistant — Concept Notes

Product-specific concepts. Cross-product patterns (memory, tool calling, evals, etc.) live in [[../shared-knowledge/concept-notes]].

## Patterns to capture

Stub list. Each becomes its own section once applied and validated:

### Widget UX
- Collapsed → expanded states, position (bottom-right default), open-on-load triggers vs user-initiated
- Avatar / brand identity — does the widget show the client's brand or a generic "Assistant"?
- First-message defaults — proactive greeting vs wait-for-user
- Mobile UX — full-screen takeover vs floating bubble
- Reduced-motion compliance for the widget animations

### Streaming responses
- Token-by-token rendering vs sentence-buffered rendering — UX feel difference
- Cursor / typing indicator while streaming
- Cancel / interrupt mid-stream
- Error handling when the stream drops

### Conversation persistence across sessions
- localStorage default (per-device, per-domain)
- Optional server-side history keyed by visitor ID
- Privacy implications + how it's surfaced to the user
- TTL on stored conversations

### Escalation to human
- Detection: user explicitly asks ("can I talk to a person") vs assistant-initiated (low confidence, repeated misunderstanding)
- Handoff channel: email to client / SMS to client / in-widget callback request
- What context the human gets — full transcript? summary?

### Session handoff to booking calendar
- Intent scoring: when does the assistant decide the user is ready to book?
- Inline rendering of `<BookingCalendar />` inside the chat thread vs link-out
- Pre-fill: assistant pre-fills calendar form fields from conversation context (name, service, date preference)
- Confirmation: post-booking message in the chat thread closes the loop

### Per-client knowledge base
- Build-time generation from `/data/site.ts` vs runtime fetch
- RAG vs full-context inlining (see [[tech-stack-research]])
- Update mechanism when the client's site copy changes

---

#offering/ai-chat #status/draft
