---
schema-version: 1
last-updated: 2026-04-29
tags: [offering/ai-voice, status/active]
---

# Voice Receptionist — Tech Stack

The Tier-2 product. Phone agent that answers calls, qualifies callers, books on the calendar, sends SMS confirmations, and escalates hot leads to the human owner. Greenfield Python build from day one. NVIDIA Personaplex is the voice model.

Cross-references:
- [`personaplex-architecture.md`](personaplex-architecture.md) — the complete build spec (Pydantic schemas · FastAPI signatures · Mermaid diagram · audio pipeline)
- [`../shared-knowledge/tech-stack.md`](../shared-knowledge/tech-stack.md) — canonical Optimus stack
- [`../shared-knowledge/agent-infrastructure.md`](../shared-knowledge/agent-infrastructure.md) — the four primitives
- [`../../../anthony-rosa/north-star.md`](../../../anthony-rosa/north-star.md) — founder layer

---

## Telephony

| Layer | Choice |
|---|---|
| **Carrier / phone numbers** | **Twilio Programmable Voice** |
| **Audio bridge** | **Twilio Media Streams WebSocket** (binary audio, mulaw at 8 kHz) |
| **SMS confirmations** | **Twilio SMS API** (same Twilio account) |

Twilio handles the PSTN side. The Media Streams WebSocket sends binary audio frames to and from a FastAPI WebSocket endpoint, which bridges to Personaplex. Full audio pipeline (mulaw ↔ PCM, 8 kHz ↔ 24 kHz resampling, Opus encoding/decoding, barge-in handling) detailed in [`personaplex-architecture.md`](personaplex-architecture.md).

---

## Voice model — NVIDIA Personaplex 7B

Released January 15, 2026 by NVIDIA Research. Full-duplex speech-to-speech model — listens and speaks simultaneously. End-to-end (not ASR + LLM + TTS chained), which collapses the cascading latency of the traditional pipeline.

| Property | Value |
|---|---|
| **Architecture** | 7B parameter end-to-end S2S, built on the Moshi architecture |
| **License** | MIT (code) + NVIDIA Open Model License (weights) — fully open and commercially permissible |
| **Turn-taking latency** | ~170 ms |
| **Interruption response** | ~240 ms (≥95% success on barge-in) |
| **Languages** | English (Spanish on roadmap) |
| **Voice cloning** | Zero-shot from a short audio sample → per-client persona |
| **Tool calling** | Not yet shipped natively. External orchestration via FastAPI (see § Orchestration tier below). |
| **Self-host minimum** | 24 GB VRAM (RTX 4090 / A10 / A100 / H100) |

**Deployment options** (all three supported in spec; chosen per client at first build):
1. Self-hosted Docker on owned GPU
2. Hosted API (`personaplex.io` at $0.08/min)
3. Private per-client GPU compute — see [`personaplex-architecture.md`](personaplex-architecture.md) § Deployment

---

## Orchestration tier — FastAPI

Personaplex handles audio. FastAPI handles every business action:
- CRM lookup (per-client CRM — GoHighLevel, HubSpot, Pipedrive, Airtable fallback, or a Supabase-hosted contact table)
- Calendar booking via the Calendly API (the same `CALENDLY_API_KEY` the website uses)
- SMS confirmations via Twilio SMS
- Escalation triggers (page Anthony / page the client owner)
- Post-call structured summary

**Tool-calling pattern** (because Personaplex native tool-calling is not shipped):
1. Personaplex emits an intent signal in its text channel — e.g. `[BOOK calendar 2026-05-12 14:00]` or `[LOOKUP crm contact "John Smith"]`.
2. The FastAPI WebSocket bridge detects the intent token, suspends Personaplex audio output briefly, and dispatches the corresponding tool handler.
3. Tool result is fed back into Personaplex via its **Inner Monologue** text input — the next thing it "thinks" is the structured tool result, which it then narrates conversationally to the caller.
4. Audio resumes.

This pattern lets Personaplex feel like it's calling tools natively from the caller's perspective, even though the orchestration is happening in a separate FastAPI process.

**Reasoning fallback — Claude Sonnet via FastAPI.** For any reasoning Personaplex can't handle natively (multi-turn pricing math, conditional eligibility logic, complex routing), the FastAPI orchestrator calls anthropic SDK with prompt caching, gets a structured response (Pydantic-validated tool-use output), and feeds that back via the Inner Monologue.

---

## Stack summary

| Layer | Tool |
|---|---|
| Telephony | Twilio Programmable Voice + Media Streams + SMS |
| Voice model | Personaplex 7B (Docker / hosted API / private GPU) |
| Orchestration | FastAPI (WebSocket bridge + tool handlers) |
| Reasoning fallback | anthropic SDK (Claude Sonnet) — prompt caching default |
| State | Supabase Postgres (sessions, transcripts, caller history per memory primitive) |
| Calendar | Calendly API |
| Schemas | Pydantic v2 — see `personaplex-architecture.md` |

---

## Latency budget

Target: sub-500 ms perceived response time on conversational turns. Tool-call turns may run higher and that's acceptable when the agent verbally signals the wait ("Let me check the calendar...").

| Component | Latency |
|---|---|
| Personaplex turn-taking | ~170 ms |
| Twilio Media Streams WebSocket overhead | ~75 ms |
| FastAPI tool round-trip | 100–300 ms (Calendly · CRM · SMS) |
| **Total (conversational turn)** | ~245 ms — well under budget |
| **Total (tool-call turn)** | ~345–545 ms — at or just over budget; acceptable with verbal signal |

---

## What this product teaches toward Tier-4 Autonomous AI Employee

The Voice Receptionist deepens the capability stack toward Tier-4 by teaching:

- **Real-time orchestration under latency budget.** Tier-4 employees handling phone-channel tasks inherit this exact FastAPI + Media Streams + Personaplex shape.
- **Tool calls with state across turns.** A caller mentions their name on turn 1, asks for an appointment on turn 5, and the agent has to remember the name. Memory primitive (`agent-infrastructure.md` § 1) gets exercised across long voice sessions — a richer test than the chat product.
- **Audio I/O — the synchronous-action surface.** Tier-4 employees that handle voice channels (which is most of them, eventually) inherit the audio pipeline from this product wholesale.
- **Per-client voice cloning.** Personaplex's zero-shot voice cloning from a short audio sample becomes the per-client persona pattern Tier-4 uses for "the Sarah employee at this client's business."

The Voice Receptionist is also the first product where the reasoning fallback (Claude Sonnet via FastAPI) gets wired in. That fallback pattern reappears in Tier-4 wherever the harness's local reasoning is insufficient for a particular client task.

---

## Open questions

- Inbound number provisioning: client's existing number forwarded to the agent vs. new number provisioned by Optimus — TBD at first paying client.
- Recording ownership and consent — varies by state. Two-party-consent states require disclosure on call connect; this disclosure becomes part of Personaplex's opening greeting per state.
- Client review/override flow — daily digest? Real-time monitoring? Live takeover? — TBD at first paying client.
- Pricing model: flat monthly + per-minute usage vs. all-inclusive vs. revenue-share on bookings — TBD; per `north-star.md` four-tier ladder, current target is $2,500 setup + $797/mo all-inclusive.
- **Personaplex tool-calling roadmap** — recheck monthly. When NVIDIA ships native tool-calling, the FastAPI Inner-Monologue pattern simplifies. Open question logged in `personaplex-architecture.md`.

---

#offering/ai-voice #status/active
