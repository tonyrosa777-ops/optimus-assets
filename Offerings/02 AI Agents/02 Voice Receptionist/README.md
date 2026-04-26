# Voice Receptionist

Phone agent that answers inbound calls, has tools for CRM lookup/update and calendar booking, and hands off to humans on escalation. Replaces the missed-call problem for service businesses that lose leads after hours.

Status: in development as of 2026-04-26. Pricing TBD — likely a recurring monthly fee plus per-minute usage.

## Why it exists

Service businesses miss calls. Trades miss calls during jobs. Hospitality misses calls during turnovers. Professional services miss calls during sessions. Every missed call is a lost lead, and the lead almost always calls a competitor next.

The voice receptionist solves that with three guarantees:

1. **24/7 coverage.** No call goes to voicemail unless the caller chooses voicemail.
2. **Instant booking.** The agent has the calendar in its toolset — it books while the caller is on the phone, not "we'll call you back."
3. **Structured CRM capture.** Every call ends with a clean CRM record: name, contact info, intent, outcome. No "I'll write that down" drift.

## Product spec (v1)

- Inbound number provisioned per client (Twilio or platform-managed)
- Agent reads the client's services, pricing tiers, hours, service area from a per-client knowledge base
- Tools available to the agent:
  - `lookup_customer(phone)` — CRM lookup by caller ID
  - `create_or_update_customer(...)` — write back to CRM
  - `check_calendar(date, service_type)` — Calendly API availability
  - `book_appointment(...)` — Calendly API booking
  - `transfer_to_human(reason)` — warm transfer with context summary
  - `send_followup_sms(message)` — Twilio SMS for confirmations and recap
- Post-call: structured summary written to CRM + SMS confirmation to caller
- Escalation triggers: explicit request, low confidence, complaint detection, billing/legal topics
- Latency budget: <500ms perceived response time (see [[concept-notes]])

## Linked notes

- [[concept-notes]] — voice-specific patterns (latency, interrupts, ambient sound, accents, transfers, post-call summaries)
- [[tech-stack-research]] — telephony platform options (Twilio + custom vs Vapi vs Bland vs Retell), CRM integrations, calendar API choices

## Optimus's own deployed instance

The dogfood instance — Optimus's own number, our own services, our own bookings:

- [[../../../Optimus Inc/ai-agents/voice-receptionist/README|Optimus's own deployed voice receptionist]]

The dogfood instance answers Anthony's sales line. If it can't qualify a prospect for a $1,500-$5,500 website build over the phone, we can't ship it to clients.

---

#offering/ai-voice #status/in-development
