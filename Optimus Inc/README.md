---
tags: [layer/optimus-os, status/active]
---

# Optimus Inc

The company itself. Distinct from the product offerings it sells, and distinct from the client projects it delivers.

## What this hub is

Optimus Business Solutions has two different things that live in this vault. `Offerings/` is what Optimus *sells* — productized templates, agent specs, workflows, pricing structures. Reusable across every client.

`Optimus Inc/` (this hub) is how Optimus *operates as a business itself* — its own marketing site, its own deployed AI agents, its own competitive intelligence, its own marketing pipeline, its own brand identity.

The relationship is template to instance. The Voice Receptionist product spec lives at `Offerings/02 AI Agents/02 Voice Receptionist/`. The Voice Receptionist that picks up when a prospect dials Optimus's actual phone number lives at `Optimus Inc/ai-agents/voice-receptionist/`. Same offering, different role: one is the IP, one is the running deployment.

## Drink your own champagne

Every Optimus deployment in this hub is a live demo. When a prospect calls Optimus, the Voice Receptionist that answers them *is* the Voice Receptionist offering they are evaluating. When they hit the Optimus marketing site, the chat assistant in the corner *is* the Chat Assistant offering. When they see Optimus's content on social, the engine producing it *is* the Marketing Team offering.

Sales motion: the demo is the product, the product is the demo. There is no separate sales rig.

## Sub-areas

- [[website/README|Optimus's own marketing site]] — built on the same `[[website-build-template]]` as every client site
- [[ai-agents/chat-assistant/README]] — Optimus's deployed chat assistant instance
- [[ai-agents/voice-receptionist/README]] — Optimus's deployed voice receptionist instance
- [[ai-agents/marketing-team/README]] — Optimus's deployed marketing-team instance
- [[market-intelligence/README]] — daily competitive intel on Optimus's own market
- [[social-pipeline/README]] — Optimus's own content calendar and active campaigns
- [[brand/README]] — Optimus's brand identity (logo, voice, palette, typography)

## What this hub is *not*

- Not the product IP. That lives in `Offerings/`.
- Not client work. Each client project lives in its own repo at `c:\Projects\<client-slug>\` with its own `CLAUDE.md`, `initial-business-data.md`, and `market-intelligence.md`. Those files describe the *client's* business and market, not Optimus's.
- Not a knowledge base. Cross-project patterns and errors live at `[[../knowledge/build-log|knowledge/build-log.md]]`.
