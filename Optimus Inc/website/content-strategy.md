---
tags: [offering/website-dev, status/draft]
---

# Optimus Site — Content Strategy

Direction for the copy and page architecture of Optimus's own marketing site. Aligned with the Optimus Positioning Rule in `[[../../CLAUDE]]`: premium, modern, 2026-era, UI/UX engineered for conversion.

## Voice

Direct. Opinionated. Specific. No corporate hedging. No "transform your business" platitudes. No agency-speak.

Anthony's voice carries the brand. Short sentences. Real numbers where they exist. Real client wins where they exist (cited from `[[../../knowledge/retrospectives/]]`). When data is thin, write the section in the voice of the founder per the Copy Writing Rule and flag with `// [DEMO COPY — pending real data]`.

Zero em dashes in any quoted material (testimonials, case study pull-quotes). Em dashes elsewhere only when grammatically necessary.

## Required pages

| Page | Purpose | Notes |
|---|---|---|
| Home | Position Optimus, route to Services or Booking | Hero, services overview, 3 case study tiles, social proof, booking CTA |
| Services | One page per offering | Website Dev, Chat Assistant, Voice Receptionist, Marketing Team — each gets its own page with detail, demo, and pricing |
| Pricing | Real pricing | Optimus's actual pricing, not the sales-tool `/pricing` page that gets deleted from client builds. Stays live in production. |
| About | Founder story, philosophy, why Optimus exists | Anthony front and center. The "drink your own champagne" framing belongs here. |
| Case Studies | Client work + outcomes | Index page + individual case study pages. Source material lives in `[[../../knowledge/retrospectives/]]`. |
| Booking | Custom `BookingCalendar` component | Per Always-Built Features Rule — never an iframe |

## Differentiator messaging

Lead with this on Home and Services:

Optimus is the only agency that ships the AI agents *with* the website, on the same conversion-first foundation. Most agencies ship a website. A different vendor sells you a chatbot. A third bolts on a voice agent. None of them talk to each other, none of them share a brand voice, and none of them are designed around the same conversion architecture.

Optimus ships all four as one stack: site, chat, voice, marketing-team. Every agent knows the offering catalog. Every agent routes to the same booking calendar. Every agent speaks in the same voice that the site speaks in.

That is not "an agency that also does AI." That is the product.

## Content sourcing

- Client wins → `[[../../knowledge/retrospectives/]]`
- Pricing → real Optimus pricing (not the Starter/Pro/Premium sales structure used in client builds)
- Process → derive from `[[../../website-build-template]]` Phase 1-9 sweep
- AI agent capabilities → cite the live deployments at `[[../ai-agents/chat-assistant/README]]`, `[[../ai-agents/voice-receptionist/README]]`, `[[../ai-agents/marketing-team/README]]`

## Open questions

- Pricing page format: tier cards (familiar to prospects) vs custom-quote-only (more accurate to actual deal flow)
- Whether to publish a blog from Optimus directly or let the Marketing Team agent run that surface
- How heavily to lean on the founder narrative vs the product narrative on the Home page
