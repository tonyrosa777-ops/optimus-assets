---
schema-version: 1
last-updated: 2026-04-29
tags: [offering/ai-voice, status/in-development]
---

# Optimus Voice Receptionist — Live Instance

The voice agent answering Optimus's inbound phone line. The instance, not the product spec.

Cross-references:
- Product spec: [[../../../Offerings/02 AI Agents/02 Voice Receptionist/README|product spec]]
- Build spec: [[../../../Offerings/02 AI Agents/02 Voice Receptionist/personaplex-architecture|personaplex-architecture.md]]
- Tech-stack rationale: [[../../../Offerings/02 AI Agents/02 Voice Receptionist/tech-stack-research]]
- Founder layer governing this instance: [[../../../anthony-rosa/north-star]]

---

## Stack

Per the canonical Optimus stack:

- Python · FastAPI WebSocket bridge
- anthropic SDK (Claude Sonnet) for the reasoning fallback
- Pydantic v2 for all schemas
- supabase-py for sessions, transcripts, caller history
- **Twilio** Programmable Voice + Media Streams + SMS
- **NVIDIA Personaplex 7B** as the voice model — full-duplex speech-to-speech (Twilio Media Streams bridge → FastAPI WebSocket → Personaplex)

Personaplex is the voice model from day one. Tool-call orchestration via FastAPI's Inner Monologue pattern (Personaplex native tool-calling not yet shipped).

---

## Purpose

When a prospect dials Optimus, this agent answers. It is also the live demo of the Tier-2 Voice Receptionist offering — the prospect evaluating the offering is talking to the offering.

This is the most powerful demo Optimus has. A prospect who hears the voice agent qualify them, book them, and route the right context to Anthony has *experienced* the product. No deck slide can match that.

---

## Configuration

Intake flow:
1. Greeting in Optimus brand voice — Personaplex per-client cloned voice, warm/direct/no IVR maze
2. Ask what they are calling about
3. Qualify: industry, current digital presence, what they need built, budget signal, timeline
4. Offer to book a discovery call directly into Anthony's calendar (same Calendly backend as the website)
5. Escalate to Anthony in real time on hot inbound (existing client, urgent issue, high-intent qualified prospect)
6. Voicemail with structured `CallSummary` (Pydantic-validated, per `personaplex-architecture.md`) delivered to Anthony for everyone else

Escalation triggers:
- Existing client phrase match → page Anthony immediately
- Qualified + timeline within 30 days → offer immediate hand-off if Anthony's status is available
- Tech support or post-sale issue → page Anthony, do not let it sit in voicemail

---

## Tracking

| Field | Value |
|---|---|
| Phone number (Twilio) | TBD |
| FastAPI WebSocket bridge URL | TBD (deployment target per `tech-stack.md`) |
| Repo | `optimus-voice-receptionist` (TBD on GitHub creation) |
| Personaplex deployment | TBD — first build evaluates self-host on owned GPU vs. `personaplex.io` hosted API for the dogfood instance |
| Voice persona ID (per-client cloned voice) | TBD — record source audio for the Optimus persona at first deployment |
| Latency target (P50 conversational turn) | <300ms |
| Latency target (P95 tool-call turn) | <600ms |
| Call transcripts (good) | TBD — collect once live, with consent |
| Call transcripts (bad) | TBD — drives tuning |

---

## Status

**Scoped, build in progress.** Build begins after the Marketing Team Tier-3 dogfood instance is live and the four agent-infrastructure primitives are battle-tested in production. Personaplex deployment for this dogfood instance is where the audio pipeline (mulaw ↔ PCM, 8 kHz ↔ 24 kHz resampling, Opus codec) gets shaken out before any paying client touches the system.

Waiting on: Marketing Team Tier-3 production-hardening, phone number provisioning, Personaplex deployment target chosen for the dogfood instance, voice persona audio recorded, system prompt finalization.

---

## Cross-references

- Product spec: [[../../../Offerings/02 AI Agents/02 Voice Receptionist/README|product spec]]
- Build spec: [[../../../Offerings/02 AI Agents/02 Voice Receptionist/personaplex-architecture|personaplex-architecture.md]]
- Calendar backend (same as site): [[../../website/README]]
- Brand voice this speaks in: [[../../brand/README]]
- Tier-4 dogfood instance (the next step up): [[../autonomous-employee/README]]
