---
tags: [offering/content-engine, status/in-development]
---

# Optimus Marketing Team — Live Instance

Optimus's own n8n instance running the Self Learning Content Engine for Optimus's own social channels. The instance, not the product spec or the workflow.

- Product spec: `[[../../../Offerings/02 AI Agents/03 Marketing Team/README|product spec]]`
- Workflow JSON (the actual product): `[[../../../Offerings/02 AI Agents/03 Marketing Team/workflows/self-learning-content-engine|workflow JSON]]`

This file tracks Optimus's running deployment of that workflow against Optimus's own pillars.

## Purpose

Generates the strategy that drives Optimus's own [[../../social-pipeline/README|social pipeline]]. The Marketing Team is the brain. The social pipeline is the output side — what actually gets published, when, where.

This is also the live demo of the offering. Prospects evaluating the Marketing Team see Optimus's own social presence as the proof.

## Configuration — pillars

The default workflow ships with Health / Wealth / Wisdom / Integration pillars (from the original Gray Method instance). Optimus's pillars are different. Working set, subject to revision once the engine has data:

1. **AI Empowerment** — what AI agents can actually do for a small business owner *today*, not the hypey 2027 narrative
2. **Business Automation** — concrete workflow examples, before/after, time saved, revenue unlocked
3. **Founder Story** — Anthony building Optimus in public, decisions made, mistakes corrected
4. **Client Wins** — outcomes from real Optimus deployments, sourced from `[[../../../knowledge/retrospectives/]]`

These pillars get tuned as the engine surfaces what actually performs. The whole point of the Self Learning Content Engine is that the pillars are not fixed — they evolve based on saturation logs and engagement signals.

## Tracking

| Field | Value |
|---|---|
| n8n instance URL | TBD |
| Workflow version deployed | TBD (track which commit of `self-learning-content-engine.json` is live) |
| Supabase project (strategy + saturation log storage) | TBD |
| Weekly strategy outputs | TBD — link to Supabase view or export folder once running |
| Saturation logs | TBD — same |
| Performance reads (what worked, what didn't) | TBD — weekly synthesis cadence |

## Status

Not yet deployed. Waiting on: n8n instance provisioning, Supabase setup, pillar finalization, social account credentials.

## Cross-references

- Product spec: `[[../../../Offerings/02 AI Agents/03 Marketing Team/README|product spec]]`
- Workflow JSON: `[[../../../Offerings/02 AI Agents/03 Marketing Team/workflows/self-learning-content-engine|workflow JSON]]`
- Output side (what gets published): `[[../../social-pipeline/README]]`
- Brand voice the content speaks in: `[[../../brand/README]]`
