# Chat Assistant

Chat widget that embeds in Optimus-built websites. Site-aware: knows the client's services, pricing, FAQ, and brand voice. Routes to the booking calendar when intent is high. Continues the conversion funnel from "visitor lands on the homepage" to "visitor is on the calendar."

Status: in development as of 2026-04-26. Pricing TBD — likely an upsell on top of Pro/Premium tiers, monthly subscription with usage cap.

## Why it exists

The website does conversion through static copy + the quiz + the booking calendar. The chat assistant adds three things the static site can't:

1. **Off-hours lead capture.** A visitor at 11pm with a question doesn't bounce — they get an answer and move toward booking.
2. **Pre-booking qualification.** The calendar gets a higher-quality booking because the assistant has already disambiguated intent.
3. **Site-specific Q&A.** Pricing questions, service-fit questions, FAQ-shaped questions get answered in-context instead of "go read the FAQ page."

The widget is not a generic Intercom-style chat — it is a conversion tool that happens to look like chat.

## Product spec (v1)

- Embeddable React widget — single `<script>` tag drop-in for Optimus-built sites
- Site-aware via per-client knowledge base built at deploy time from `/data/site.ts` (services, pricing, FAQ, brand voice)
- Streaming responses via Vercel AI SDK (TBD — see [[tech-stack-research]])
- Routes to `<BookingCalendar />` inline when intent score crosses threshold
- Conversation persistence across page reloads (localStorage + optional server-side history)
- Escalation handoff to email/SMS when the user explicitly asks for a human
- Per-client analytics: conversation count, qualification rate, booking conversion, top intents

## Linked notes

- [[concept-notes]] — chat-specific patterns (widget UX, streaming, persistence, escalation, session handoff to booking)
- [[tech-stack-research]] — chat-specific tech investigation (widget framework, streaming library, RAG approach for the per-site knowledge base)

## Optimus's own deployed instance

Once the Optimus marketing site has the widget live, it lives here:

- [[../../../Optimus Inc/ai-agents/chat-assistant/README|Optimus's own deployed chat assistant]] (the dogfood instance)

The dogfood instance is the reference implementation and the first eval target. If the widget can't sell Optimus, it can't sell our clients.

---

#offering/ai-chat #status/in-development
