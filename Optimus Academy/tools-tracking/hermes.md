---
title: Hermes
schema-version: 1
tool-name: Hermes
maintainer: Noose Research (open-source community)
repo: https://github.com/Noose-Research/Hermes
domain: agents
created: 2026-05-06
last-updated: 2026-05-06 21:18
status: evaluating
review-by: 2026-08-06
tags: [#learning/captured, #status/draft]
---

# Hermes

> **Status:** `evaluating` — surfaced via Julian Goldie's 5-hour course, late April 2026 hands-on review. Not adopted. Not rejected.
> **Concept:** [[../concepts/hermes-openclaw-agents-course]]
> **First surfaced:** [[../daily/2026-05-06#21:18 — "FREE Hermes + OpenClaw AI Agents Course: Build & Automate ANYTHING" by Julian Goldie SEO]] — Julian Goldie SEO
> **Last updated:** 2026-05-06 21:18

## What it is
Open-source, MIT-licensed self-improving AI agent runtime built by Noose Research. Launched February 2026. Single-curl install across Linux, macOS, WSL2; runs on a $5 VPS, Docker, SSH, Singularity, Modal, or Daytona (six terminal backends total). Native messaging-channel surface in v0.9 covers 16 platforms (Telegram, Discord, Slack, WhatsApp, Signal, email, iMessage via BlueBubbles, WeChat, Matrix, Mattermost, plus Termux mobile and the local web dashboard). Connects to 200+ models through OpenRouter / Noose Portal / OpenAI-compatible endpoints.

The key differentiator: Hermes writes its own skills as it works. After completing any task with five or more tool calls, it generates a `skill.md` describing how it solved the problem. Skills self-improve during use (the agent edits its own `skill.md` when later runs reveal a refinement) and are portable across runtimes via the agentskills.io open standard. Skill installs are surfaced through Claw Hub, Wonderlay, and Awesome-Hermes-Agent. A built-in security scanner runs on any skill before install. Maintains a `memory.md` for project context plus a `user.md` modeling the operator. Repo: `https://github.com/Noose-Research/Hermes` (the GitHub org slug is unverified in the source course audio — flag for confirmation before external citation). Cross-link to concept: [[../concepts/hermes-openclaw-agents-course]].

## Why it's on the radar for Optimus
1. **Self-improving skill model could shave Tier-3 / Tier-4 build time.** The agent generates its own reusable skills as it works rather than Optimus engineering each skill manually. If the skill quality is real (not just demo-grade), this compounds engineering leverage on every Marketing Team and Autonomous AI Employee build.
2. **Memory architecture is the deepest of any open-source agent currently surveyed.** Pluggable engine (v0.7 release), Obsidian as primary backend, OMI for auto-capture, the Karpathy LLM-wiki pattern shipped as a built-in skill, plus Honcho and Mem-Zero as backend options. Directly relevant to the canonical agent-infrastructure memory primitive in [`Offerings/02 AI Agents/shared-knowledge/agent-infrastructure.md`](../../Offerings/02%20AI%20Agents/shared-knowledge/agent-infrastructure.md).
3. **Free-forever cost path matches "SMB-affordable" positioning.** Olama (Ollama) running local models on the brain-plus-local-sub-agent pattern keeps marginal cost at $0 for steady-state operation, which is the exact economic shape Optimus needs to defend Tier-3 margin.
4. **Equal evaluation track time vs OpenClaw.** Julian's "I'm over OpenClaw" sentiment (April 2026) does NOT mean OpenClaw is dead — Nate B. Jones's production-grade architectural claim still stands at the topology level. But Hermes deserves equal evaluation track time alongside [[../tools-tracking/openclaw]] before any adoption decision.

## Adoption decision criteria
The tool gets promoted from `evaluating` to `adopted` only if a spike-test confirms ALL of:
- [ ] Per-client deploy footprint fits inside Tier-3 ($1,497/mo) and Tier-4 ($2,500-5,000/mo) margin targets without margin compression.
- [ ] Skill model security and sandboxing is reviewable, not just trust-the-model. The auto-skill-generation surface is the obvious risk: an agent that writes its own executable skills can also write its own backdoor. The built-in security scanner is a starting point, not a sufficient control.
- [ ] Memory layer composability with Optimus's canonical Pydantic v2 + Supabase + pgvector primitives. Hermes's pluggable memory engine is the question; if the plug surface accepts a Supabase backend cleanly, this is a green light.
- [ ] License (MIT) compatible with Optimus client deployments. Verified per Julian, but confirm against the actual repo LICENSE file before any client ship.
- [ ] Spike-test confirms skill quality on a representative Optimus workflow (not just demo cases). Run a Tier-3 Marketing Team task and verify the auto-generated skill is actually reusable, not slop.
- [ ] Star-count and community-velocity claims verifiable against live GitHub. Julian cited Hermes star counts ranging from 8.1k to 106k inconsistently across the course — the course is stitched from segments at different dates, so any single number is point-in-time at best. Verify before citing externally.
- [ ] Compatibility with Hermes-OpenClaw migration tool (`hermes claw migrate`) for clients on existing OpenClaw deployments. Matters if Optimus ever inherits an OpenClaw client install during a Tier-3 upsell.

## Decision log
- **2026-05-06** — Surfaced via [[../daily/2026-05-06#21:18 — "FREE Hermes + OpenClaw AI Agents Course: Build & Automate ANYTHING" by Julian Goldie SEO]]. Status set to `evaluating`. Driver: Julian's empirical 5-hour hands-on review crowns Hermes over OpenClaw on reliability, ease-of-setup, and improvement-rate as of late April 2026. Not blocking any current build, but Hermes' self-improving skill model is novel enough to warrant a deliberate spike-test before Tier-3 build.

## Related
- **OpenClaw** — peer / competitor framework. See tool entry [[../tools-tracking/openclaw]] and concept [[../concepts/openclaw-multi-agent-orchestration]]. The two tools are evaluated in parallel; adoption of one does not preclude the other (Julian explicitly recommends serious operators run both).
- **Paperclip** — orchestration shell that runs Hermes (or OpenClaw) as agent runtime. Wraps agents into a "company structure" with C-suite role hierarchy, per-agent budgets, scheduled heartbeats, ticketing audit log. Mentioned course-wide; not yet a tools-tracking entry.
- **Multica** — alternative orchestration shell to Paperclip. Wraps agents into a "team workspace" with first-class human collaborators, Linear-style Kanban board, multi-tenant workspace support. Not yet a tools-tracking entry.
- **agentskills.io** — Hermes' skill marketplace and the open standard that makes skills portable across Hermes, Claude Code, and Cursor. Tracked separately if it surfaces in its own capture.
- **Olama** (likely Ollama) — local-LLM runtime that powers the free-forever Hermes setup path via the `Olama launch Hermes` bridge command. Vault canonical spelling stays "Ollama"; Julian's "Olama" is preserved here per the source.
