---
tags: [layer/optimus-os, status/active]
---

# Optimus AI Agent Deployments

Optimus's own running AI agent instances. The dogfood layer.

## What lives here

Three deployed instances, one per offering Optimus sells:

- [[chat-assistant/README]] — chat agent on Optimus's marketing site
- [[voice-receptionist/README]] — voice agent answering Optimus's inbound phone line
- [[marketing-team/README]] — n8n instance running Self Learning Content Engine on Optimus's pillars

## Instance vs product

Every folder here is an *instance* of an offering — Optimus's own running deployment. The *product spec* (the IP, the template that gets sold) lives under `[[../../Offerings/02 AI Agents/]]`. Every instance README cross-links back to its product spec.

This split keeps the product IP clean (one canonical spec, reusable across every client deployment) and the operational data clean (configuration, transcripts, tuning notes, performance — specific to Optimus's running deployment).

## Why dogfood

When a prospect interacts with Optimus, they interact with the offering they are evaluating:

- They land on the marketing site and the chat in the corner is the Chat Assistant offering
- They call the phone number and the voice that answers is the Voice Receptionist offering
- They see Optimus's content on social and the engine that produced it is the Marketing Team offering

The demo is the product. There is no separate sales rig. This is the strongest possible proof for any prospect evaluating any of these offerings.

## Cross-references

- Product specs (the IP): `[[../../Offerings/02 AI Agents/]]`
- Site these agents live on: `[[../website/README]]`
- Brand voice these agents speak in: `[[../brand/README]]`
