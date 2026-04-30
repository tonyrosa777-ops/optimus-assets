# Voice Receptionist — Tier 2

Phone agent that answers inbound calls, qualifies callers, books on the calendar, sends SMS confirmations, and escalates hot leads to the human owner. Built on **NVIDIA Personaplex 7B** (full-duplex speech-to-speech) with Twilio Programmable Voice + Media Streams as the telephony bridge and FastAPI orchestration for tool calls. Replaces the missed-call problem for service businesses that lose leads after hours.

Tier-2 in the four-tier upsell ladder: **$2,500 setup + $797/mo**.

Cross-references:
- Build spec: [[personaplex-architecture|personaplex-architecture.md]] — complete Pydantic schemas, FastAPI endpoint signatures, audio pipeline, deployment options
- Tech-stack rationale: [[tech-stack-research]]
- Voice-specific concept patterns: [[concept-notes]]
- Optimus's own dogfood instance: [[../../../Optimus Inc/ai-agents/voice-receptionist/README|Optimus's own deployed voice receptionist]]
- Founder layer: [[../../../anthony-rosa/north-star]]

---

## Why it exists

Service businesses miss calls. Trades miss calls during jobs. Hospitality misses calls during turnovers. Professional services miss calls during sessions. Every missed call is a lost lead, and the lead almost always calls a competitor next.

The voice receptionist solves that with three guarantees:

1. **24/7 coverage.** No call goes to voicemail unless the caller chooses voicemail.
2. **Instant booking.** The agent has the calendar in its toolset — it books while the caller is on the phone, not "we'll call you back."
3. **Structured CRM capture.** Every call ends with a clean CRM record: name, contact info, intent, outcome. No "I'll write that down" drift.

---

## Product spec

Per the canonical Optimus stack — Python from day one, Personaplex as the voice model:

| Component | Choice |
|---|---|
| **Telephony** | Twilio Programmable Voice + Media Streams (binary audio, mulaw 8 kHz) + Twilio SMS API |
| **Voice model** | NVIDIA Personaplex 7B (full-duplex S2S, MIT + NVIDIA Open Model License, Docker self-hostable) |
| **Bridge** | FastAPI WebSocket service handling Twilio Media Streams ↔ Personaplex audio pipeline (mulaw ↔ PCM, 8 kHz ↔ 24 kHz, Opus codec, barge-in handling) |
| **Per-client persona** | Personaplex zero-shot voice cloning from a short audio sample |
| **Reasoning fallback** | anthropic SDK (Claude Sonnet) for any reasoning Personaplex can't handle natively |
| **Tool orchestration** | FastAPI handlers (Personaplex native tool-calling not yet shipped — pattern uses Inner Monologue text channel for tool-result drip-feed) |
| **State** | Supabase Postgres (sessions, transcripts, caller history per the agent-infrastructure memory primitive) |
| **Schemas** | Pydantic v2 — see [[personaplex-architecture]] |

Inbound number provisioned per client (Twilio). Agent reads the client's services, pricing tiers, hours, service area from a per-client knowledge base injected into the Personaplex system prompt with prompt caching.

Tools available to the agent:
- `lookup_customer(phone)` — CRM lookup by caller ID
- `create_or_update_customer(...)` — write back to CRM
- `check_calendar(date, service_type)` — Calendly API availability
- `book_appointment(...)` — Calendly API booking
- `transfer_to_human(reason)` — warm transfer with context summary
- `send_followup_sms(message)` — Twilio SMS for confirmations and recap

Post-call: structured `CallSummary` (Pydantic-validated, see [[personaplex-architecture]]) written to CRM + SMS confirmation to caller.

Escalation triggers: explicit request, low confidence, complaint detection, billing/legal topics.

Latency budget: <500ms perceived response time on conversational turns. Personaplex 170–240ms turn-taking + Twilio Media Streams ~75ms + FastAPI tool round-trip 100–300ms.

---

## Linked notes

- [[personaplex-architecture]] — complete build spec (Pydantic schemas, FastAPI endpoint signatures, Mermaid diagram, audio pipeline, deployment options)
- [[tech-stack-research]] — stack rationale, latency budget, why Personaplex from day one
- [[concept-notes]] — voice-specific patterns (latency, interrupts, ambient sound, accents, transfers, post-call summaries)
- [[../shared-knowledge/agent-infrastructure]] — the four primitives this product inherits

---

## Optimus's own deployed instance

The dogfood instance — Optimus's own number, our own services, our own bookings:

- [[../../../Optimus Inc/ai-agents/voice-receptionist/README|Optimus's own deployed voice receptionist]]

The dogfood instance answers Anthony's sales line. If it can't qualify a prospect for an Optimus website build over the phone, we can't ship it to clients. The Personaplex audio pipeline gets shaken out on this instance before any paying Tier-2 client touches the system.

---

#offering/ai-voice #status/active
