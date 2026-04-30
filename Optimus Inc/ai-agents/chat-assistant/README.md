---
schema-version: 1
last-updated: 2026-04-29
tags: [offering/ai-chat, status/in-development]
---

# Optimus Chat Assistant — Live Instance

The chat agent deployed on Optimus's own marketing site. The instance, not the product spec.

Cross-references:
- Product spec: [[../../../Offerings/02 AI Agents/01 Chat Assistant/README|product spec]]
- Tech-stack: [[../../../Offerings/02 AI Agents/01 Chat Assistant/tech-stack-research]]
- Founder layer governing this instance: [[../../../anthony-rosa/north-star]]

---

## Stack

Per the canonical Optimus stack:

- **Backend:** Python · FastAPI · anthropic SDK (Claude Sonnet for conversation; Haiku for `/api/intent-score`) · Pydantic v2 · supabase-py
- **Frontend:** TypeScript/React custom widget · Vercel AI SDK (consumes the FastAPI SSE stream)
- **Knowledge base:** full-context inlining of the Optimus marketing site `/data/site.ts` content into the system prompt with prompt caching

---

## Purpose

The chat assistant in the corner of the Optimus marketing site. It is also the live demo of the Tier-1 Chat Assistant offering. Prospects evaluating the offering interact with the offering itself.

---

## Configuration

Knows:
- The full Optimus services catalog (Website Dev + the four-tier upsell ladder: Chat Assistant · Voice Receptionist · Marketing Team · Autonomous AI Employee)
- Optimus's actual pricing (not the client-build Starter/Pro/Premium sales structure)
- Booking calendar availability (calls the same Calendly API as the site's `BookingCalendar` component)
- Common qualifying questions (industry, current site status, budget signal, timeline)
- When to stay in-conversation vs hand off to Anthony

Escalation rules:
- Hot inbound (qualified, budget-signaled, timeline within 60 days) → notify Anthony immediately + offer booking
- Cold curiosity → answer + offer the lead-capture quiz
- Pricing pushback → defer to a discovery call rather than negotiate in chat

---

## Tracking

| Field | Value |
|---|---|
| Deployment URL | TBD (lives on Optimus marketing site once shipped) |
| Repo | `optimus-chat-assistant` (TBD on GitHub creation) |
| FastAPI backend host | TBD (Vercel Python Functions vs Fly.io vs Railway — decision per `tech-stack.md` § Backend hosting) |
| System prompt version | TBD — versioned in this folder once built |
| Knowledge base contents | TBD — services, pricing, FAQ, common objections (auto-inlined from `/data/site.ts`) |
| Cache hit rate target | ≥90% (system prompt + KB cached) |
| Transcript samples (good) | TBD — collect once live |
| Transcript samples (bad) | TBD — collect once live, drives tuning |

---

## Status

**Scoped, build in progress.** Waiting on: Optimus marketing site build, FastAPI backend deploy target chosen, system prompt finalization, knowledge base assembly from `/data/site.ts`.

---

## Cross-references

- Product spec: [[../../../Offerings/02 AI Agents/01 Chat Assistant/README|product spec]]
- Site this lives on: [[../../website/README]]
- Brand voice this speaks in: [[../../brand/README]]
