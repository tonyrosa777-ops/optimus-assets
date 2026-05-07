---
title: OpenClaw
schema-version: 1
tool-name: OpenClaw
maintainer: Peter Steinberger (open-source community)
repo: https://github.com/openclaw/openclaw
domain: agents
created: 2026-05-03
last-updated: 2026-05-06 21:18
status: evaluating
review-by: 2026-08-03
tags: [#learning/captured, #status/draft]
---

# OpenClaw

> **Status:** `evaluating` — on the radar after the April 2026 maturity step. Not adopted. Not rejected.
> **Concept:** [[../concepts/openclaw-multi-agent-orchestration]]
> **First surfaced:** [[../daily/2026-05-03#09:36 — "Your Claw can orchestrate multiple agents, handle Slack threads, and ..." by nate.b.jones]] — nate.b.jones
> **Last updated:** 2026-05-03 09:36

## What it is
Open-source, self-hosted multi-agent orchestrator with first-class messaging-channel integration (Slack, Telegram, WhatsApp, Discord, Signal, iMessage, Teams) and multi-model abstraction (Claude, GPT-4o, Gemini, DeepSeek, local via Ollama). Hierarchical agents run in isolated Docker containers, communicate via RPC. Created by Peter Steinberger; ~310k GitHub stars, 1,200+ contributors as of April 2026. See concept note for mechanics: [[../concepts/openclaw-multi-agent-orchestration]].

## Why it's on the radar for Optimus
1. **Potential service-business surface.** "Managed OpenClaw deployment" is a coherent product idea — install, configure, maintain OpenClaw on client infrastructure, sell the management layer. Could complement (not replace) the four-tier ladder. The strategic case for/against this lives in [[../apply-to-optimus/openclaw-multi-agent-orchestration#Applied to AI Agents — Marketing Team (Tier-3)]].
2. **Multi-channel native behavior.** Tier-3 Marketing Team and Tier-4 Autonomous Employee both eventually need to live inside client messaging surfaces (Slack for ops teams, Teams for enterprise, etc.). Building channel adapters from scratch in canonical Python vs. inheriting them from OpenClaw is a real build-vs-buy question.
3. **Multi-model abstraction.** Aligns with Nate B. Jones's thesis that the orchestration layer is the moat, not the model. Optimus's canonical stack is anthropic-SDK direct — a deliberate single-vendor choice today. OpenClaw represents a different bet (orchestrator-mediated, vendor-agnostic).

## Adoption decision criteria
The tool gets promoted from `evaluating` to `adopted` only if a spike-test confirms ALL of:
- [ ] Per-client deploy overhead (Docker daemon, container management, log aggregation) fits inside Tier-3 ($1,497/mo) and Tier-4 ($2,500-5,000/mo) margin targets without margin compression.
- [ ] Tool registry / approval / observability surface is composable with the four canonical Optimus agent-infrastructure primitives, not a competing opinionated shape.
- [ ] Channel-native behavior (Slack thread reply, Teams thread reply) actually works as advertised on a representative client workflow, not just demo cases.
- [ ] Upgrade cadence is manageable — version-pinning + deliberate quarterly upgrade beats the breaking-change blast radius of a 310k-star repo in active development.
- [ ] Voice channel: confirms Personaplex / Twilio Media Streams pattern is integrable, OR explicitly accept that OpenClaw is text-channels-only (which means Tier-2 Voice Receptionist stays canonical Python regardless).

## Decision log
- **2026-05-03** — Surfaced via [[../daily/2026-05-03#09:36 — "Your Claw can orchestrate multiple agents, handle Slack threads, and ..." by nate.b.jones]]. Status set to `evaluating`. No spike-test yet. Not blocking any current build.
- **2026-05-06** — Empirical data update via [[../daily/2026-05-06#21:18 — "FREE Hermes + OpenClaw AI Agents Course: Build & Automate ANYTHING" by Julian Goldie SEO]] (Julian Goldie SEO 5h course). Course's empirical hands-on take from late April 2026 frames OpenClaw as DEGRADED relative to peers: Julian reports config-invalidation breakage requiring workarounds, declining day-to-day reliability vs Hermes Agent (Noose Research), and explicitly states "I'm over OpenClaw" by chapter 29. This does NOT contradict the May 3 framing of OpenClaw as "production-grade" per nate.b.jones — both can be true at different abstraction layers (the architecture remains production-grade; the operator experience has degraded relative to a faster-moving competitor). Net effect on Optimus evaluation: status STAYS `evaluating` but with reduced urgency to spike-test for Tier-3 adoption, because the comparable Hermes runtime is now equally-or-more credible AND has a built-in `hermes claw migrate` cross-tool migration path. Star count claims also shifted: Julian cites 340-345k stars (April 2026) vs the May 3 figure of 310k — flagged as inconsistency to reconcile. Companion entry: see new tools-tracking file [[../tools-tracking/hermes]].

## Related
- **OB1 (Open Brain)** — companion memory-layer project by Nate B. Jones (https://github.com/NateBJones-Projects/OB1). Self-hosted persistent memory database for AI agents. Tracked separately when it surfaces in its own capture.
- **Adjacent orchestrators:** Ruflo (Claude swarm orchestration), OpenWork (Claude Cowork alternative), Paperclip (orchestrates OpenClaw + Claude Code into "company structure"). Not yet evaluated; only logged here for situational awareness.
