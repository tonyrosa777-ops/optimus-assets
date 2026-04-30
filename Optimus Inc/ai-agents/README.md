---
schema-version: 1
last-updated: 2026-04-29
tags: [layer/optimus-os, status/active]
---

# Optimus AI Agent Deployments

Optimus's own running AI agent instances. The dogfood layer.

This hub is governed by [`../../anthony-rosa/north-star.md`](../../anthony-rosa/north-star.md) — the **Drink-Own-Champagne 2027-Q3 milestone** runs through the dogfood instances tracked here.

---

## What lives here

Four deployed instances, one per offering Optimus sells:

- [[chat-assistant/README]] — chat agent on Optimus's marketing site (Tier 1)
- [[voice-receptionist/README]] — voice agent answering Optimus's inbound phone line (Tier 2 · Personaplex on Twilio Media Streams)
- [[marketing-team/README]] — Self Learning Content Engine running Optimus's own content strategy (Tier 3 · the first true scheduled-cron agent)
- [[autonomous-employee/README]] — Optimus's own custom-trained Tier-4 Autonomous AI Employee. The Drink-Own-Champagne instance — Optimus's marketing pipeline + inbound qualification + scheduling running autonomously by **2027-Q3**.

---

## Instance vs product

Every folder here is an *instance* of an offering — Optimus's own running deployment. The *product spec* (the IP, the template that gets sold) lives under [[../../Offerings/02 AI Agents/]]. Every instance README cross-links back to its product spec.

This split keeps the product IP clean (one canonical spec, reusable across every client deployment) and the operational data clean (configuration, transcripts, tuning notes, performance — specific to Optimus's running deployment).

---

## Why dogfood

When a prospect interacts with Optimus, they interact with the offering they are evaluating:

- They land on the marketing site and the chat in the corner is the **Tier-1 Chat Assistant** offering
- They call the phone number and the voice that answers is the **Tier-2 Voice Receptionist** offering
- They see Optimus's content on social and the engine that produced it is the **Tier-3 Marketing Team** offering
- And by 2027-Q3, the system running Optimus's marketing pipeline + inbound qualification + scheduling autonomously is the **Tier-4 Autonomous AI Employee** offering — proving the product on Optimus before selling it to Tier-4 clients.

The demo is the product. There is no separate sales rig. This is the strongest possible proof for any prospect evaluating any of these offerings, and it is the foundation of the Optimus moat — see [`../../anthony-rosa/north-star.md`](../../anthony-rosa/north-star.md) § The Moat point 3 (two-plus years of dogfood data nobody else has).

---

## The Drink-Own-Champagne 2027-Q3 milestone

The operational target for this hub. By **end of 2027-Q3:**

- Marketing pipeline running autonomously through the Tier-4 employee (delegating from / extending Marketing Team's strategy outputs)
- Inbound qualification running autonomously (Chat Assistant + Voice Receptionist + Tier-4 employee coordinating)
- Scheduling running autonomously (Calendly integration owned by the Tier-4 employee)
- Anthony's daily attention to operational marketing/inbound/scheduling tasks: **near zero**

This is not a marketing claim. It is the operational target. Slips get explicit attention in [`../../anthony-rosa/wins.md`](../../anthony-rosa/wins.md) — not silent rolling.

---

## Cross-references

- Product specs (the IP): [[../../Offerings/02 AI Agents/]]
- Site these agents live on: [[../website/README]]
- Brand voice these agents speak in: [[../brand/README]]
- Founder vision governing these instances: [[../../anthony-rosa/north-star]]
