---
title: Personal Automated Revenue Projects — Anthony Rosa
schema-version: 1
created: 2026-05-08
last-updated: 2026-05-08
tags: [#owner/anthony-rosa, #layer/optimus-os, #status/active]
---

# Personal Automated Revenue Projects

Anthony Rosa's personal projects that are intended to become **fully automated revenue streams**. These are NOT Optimus offerings — they're personal projects, on Anthony's time, under Anthony's name. Some may eventually graduate to Optimus offerings via the validation gates pattern below.

## Scope

This folder holds:
- **Personal automated revenue projects.** Trading bot, AI influencer (Anthony's TikTok Shop revenue stream), Akash Network deployment research with personal-revenue or personal-investment angle.
- **Status, stack, validation gates** for each project — what needs to be true before the project graduates from "side project" to "validated revenue stream," and from there potentially to "Optimus offering."

This folder does NOT hold:
- Optimus offerings (lives in `Offerings/`).
- Optimus's own internal operations (lives in `Optimus Inc/`).
- Investment positions (lives in `anthony-rosa/investments/`).
- Career skill goals separate from a revenue project (lives in `anthony-rosa/skills/`).

## Files

| File | What |
|---|---|
| `akash-network.md` | Technical research on Akash Network deployments + cross-link to the personal AKT investment thesis. Personal R&D, distinct from Optimus's product use of "private per-client GPU compute." |
| `ai-influencer.md` | Personal AI influencer pipeline — avatar AI + voice + Claude orchestration → TikTok Shop affiliate revenue. Cross-link to the Optimus client offering version (split bridge). |
| `trading-bot.md` | Personal automated trading bot. Status, stack thesis, validation gates. Mission-orthogonal to Optimus (different audience, different regulatory surface) — stays personal until validation gates clear. |

## Graduation gates pattern (side project → revenue stream → Optimus offering)

Every project in this folder declares three gates explicitly. A project doesn't graduate to the next stage until its gate clears. This is the same drink-own-champagne discipline as the rest of the vault.

### Gate 1 — "Side project → Revenue stream"
The project must produce REAL revenue (not paper, not theoretical) on Anthony's own deployment for a meaningful duration. Suggested floor: **$X profit/month for 3 consecutive months** (X is per-project; trading bot's gate also requires surviving a drawdown). Until gate 1 clears, the project is a side project — no productization, no client-facing version.

### Gate 2 — "Revenue stream → Productizable"
The validated revenue stream must be re-deployable for a third party without rebuilding from scratch. The stack must be repeatable, the methodology must be teachable, and at least one validation case beyond Anthony's own deployment must exist.

### Gate 3 — "Productizable → Optimus offering"
The productizable system fits Optimus's mission (newest tech for SMBs at affordable prices), the unit economics work at SMB price points, and the operational load doesn't break Optimus's ability to deliver other offerings. Only after gate 3 does the project move from `anthony-rosa/projects/` to `Offerings/`.

## Bridge zone

Learning from `/learn` that applies to a personal project lands in `Optimus Academy/apply-to-anthony-rosa/<concept-slug>.md` with `applies-to:: [[../../anthony-rosa/projects/<file>]]` and `#applies-to/anthony-rosa/projects` tag.

When a single concept applies to **both** an Optimus offering AND a personal project (canonical example: AI influencer is both an Optimus client content offering AND Anthony's personal TikTok Shop pipeline), follow the **cross-zone split rule** — TWO single-zone bridge files (one in each apply-to-X folder), both linking to the same shared concept. See `Optimus Academy/apply-to-anthony-rosa/README.md` for the split rule details.

## Naming pattern for files in this folder

`<project-slug>.md` — slug from project name. Examples:
- `akash-network.md` (not `akash.md`, not `decentralized-compute.md`)
- `ai-influencer.md` (not `tiktok-shop.md` — TikTok Shop is the revenue surface; AI influencer is the project)
- `trading-bot.md`
