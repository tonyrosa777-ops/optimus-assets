---
tags: [offering/ai-voice, status/in-development]
---

# Optimus Voice Receptionist — Live Instance

The voice agent answering Optimus's inbound phone line. The instance, not the product spec.

Product spec lives at: `[[../../../Offerings/02 AI Agents/02 Voice Receptionist/README|product spec]]`

This file tracks the running deployment.

## Purpose

When a prospect dials Optimus, this agent answers. It is also the live demo of the Voice Receptionist offering. The prospect evaluating the offering is talking to the offering.

This is the most powerful demo Optimus has. A prospect who hears the voice agent qualify them, book them, and route the right context to Anthony has *experienced* the product. No deck slide can match that.

## Configuration

Intake flow:
1. Greeting in Optimus brand voice (warm, direct, no IVR maze)
2. Ask what they are calling about
3. Qualify: industry, current digital presence, what they need built, budget signal, timeline
4. Offer to book a discovery call directly into Anthony's calendar (same Calendly backend as the site)
5. Escalate to Anthony in real time on hot inbound (existing client, urgent issue, high-intent qualified prospect)
6. Voicemail with structured transcript + qualified-or-not tag delivered to Anthony for everyone else

Escalation triggers:
- Existing client phrase match → page Anthony immediately
- Qualified + timeline within 30 days → offer immediate hand-off if Anthony's status is available
- Tech support or post-sale issue → page Anthony, do not let it sit in voicemail

## Tracking

| Field | Value |
|---|---|
| Phone number | TBD |
| System prompt version | TBD — versioned in this folder once built |
| Voice model + voice selection | TBD |
| Call recordings (good) | TBD — collect once live, with consent |
| Call recordings (bad) | TBD — drives tuning |
| Tuning notes log | TBD |

## Status

Not yet deployed. Waiting on: phone number provisioning, voice/model selection, system prompt finalization, Calendly integration validation.

## Cross-references

- Product spec: `[[../../../Offerings/02 AI Agents/02 Voice Receptionist/README|product spec]]`
- Calendar backend (same as site): `[[../../website/README]]`
- Brand voice this speaks in: `[[../../brand/README]]`
