---
tags: [offering/ai-chat, status/in-development]
---

# Optimus Chat Assistant — Live Instance

The chat agent deployed on Optimus's own marketing site. The instance, not the product spec.

Product spec lives at: `[[../../../Offerings/02 AI Agents/01 Chat Assistant/README|product spec]]`

This file tracks the running deployment.

## Purpose

The chat assistant in the corner of the Optimus marketing site. It is also the live demo of the Chat Assistant offering. Prospects evaluating the offering interact with the offering itself.

## Configuration

Knows:
- The full Optimus services catalog (Website Dev, Chat Assistant, Voice Receptionist, Marketing Team)
- Optimus's actual pricing (not the client-build Starter/Pro/Premium sales structure)
- Booking calendar availability (calls the same Calendly API as the site's `BookingCalendar` component)
- Common qualifying questions (industry, current site status, budget signal, timeline)
- When to stay in-conversation vs hand off to Anthony

Escalation rules:
- Hot inbound (qualified, budget-signaled, timeline within 60 days) → notify Anthony immediately + offer booking
- Cold curiosity → answer + offer the lead-capture quiz
- Pricing pushback → defer to a discovery call rather than negotiate in chat

## Tracking

| Field | Value |
|---|---|
| Deployment URL | TBD (lives on Optimus marketing site once shipped) |
| System prompt version | TBD — versioned in this folder once built |
| Knowledge base contents | TBD — services, pricing, FAQ, common objections |
| Transcript samples (good) | TBD — collect once live |
| Transcript samples (bad) | TBD — collect once live, drives tuning |
| Tuning notes log | TBD |

## Status

Not yet deployed. Waiting on: Optimus marketing site build, system prompt finalization, knowledge base assembly.

## Cross-references

- Product spec: `[[../../../Offerings/02 AI Agents/01 Chat Assistant/README|product spec]]`
- Site this lives on: `[[../../website/README]]`
- Brand voice this speaks in: `[[../../brand/README]]`
