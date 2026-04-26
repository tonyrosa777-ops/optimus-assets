# Voice Receptionist — Tech Stack Research

Options to investigate. Voice has a much larger build-vs-buy spectrum than chat — the platforms have done real work on the hardest pieces (latency, interrupts, telephony glue). The default position is to lean on a platform for v1 and revisit custom orchestration once we know what we're missing.

## Telephony + orchestration

| Option | Pros | Cons |
|---|---|---|
| **Twilio + custom orchestration** | Maximum control. Telephony is well-understood. Can use any LLM. | Have to build interrupt handling, latency tuning, ASR/TTS plumbing, state management. Months of work before parity with platforms. |
| **Vapi** | Voice-agent platform. Sub-500ms latency claims. Tool calling. Multiple model providers. | Platform fees on top of usage. Vendor risk. Custom UI for client dashboards is on us. |
| **Bland AI** | Similar voice-agent platform. Pitched at outbound + inbound. Strong telephony reliability claims. | Same vendor risk class as Vapi. Comparison vs Vapi is on a feature-by-feature basis — both worth a shootout. |
| **Retell** | Newer platform. Strong WebSocket / low-latency story. Good developer experience reports. | Less mature than Vapi/Bland. Smaller ecosystem. |
| **LiveKit Agents** | Open-source orchestration on top of LiveKit's WebRTC. Self-host or LiveKit Cloud. | More setup. Self-host means we own the ops. |

**Lean: shootout between Vapi, Bland, Retell on the dogfood instance.** Pick one based on real latency numbers + tool-calling reliability + per-minute cost. Revisit Twilio + custom only if all three platforms hit a blocker.

## CRM integration

Whichever CRM the client already uses. Optimus does not pick the CRM for the client. Common targets to support out of the gate:

| CRM | Notes |
|---|---|
| **GoHighLevel (GHL)** | Common in trades / service business space. API supports contact + opportunity creation. Already referenced in `knowledge/`. |
| **HubSpot** | Common in professional services. Robust API. Free tier covers most Optimus clients. |
| **Pipedrive** | Lighter weight. Common in small B2B. |
| **Airtable / Google Sheets fallback** | For clients with no real CRM. Not great long-term, fine as v1. |
| **Custom Supabase table** | If the client wants Optimus to host the lead store. Reasonable default for clients without an existing CRM. |

Build the integration layer once with a clean interface, then swap providers per client.

## Calendar API

Already standardized: **Calendly.** Same backend as the website's `<BookingCalendar />` (per [[CLAUDE]] Always-Built Features Rule). The voice agent uses the same `CALENDLY_API_KEY` and the same event type URI. No new calendar provider until there's a real reason.

## Open questions

- Inbound number provisioning: client's existing number forwarded to the agent vs new number provisioned by Optimus?
- Who owns the recording? Compliance varies by state — two-party consent states require disclosure on call connect.
- How does the client review/override agent decisions? (Daily digest? Real-time monitoring? Live takeover?)
- Pricing model: flat monthly + per-minute usage vs all-inclusive vs revenue-share on bookings?

---

#offering/ai-voice #status/draft
