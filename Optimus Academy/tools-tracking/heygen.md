---
title: HeyGen
schema-version: 1
tool-name: HeyGen
maintainer: HeyGen Inc. (commercial)
website: https://www.heygen.com
domain: tooling
created: 2026-05-03
last-updated: 2026-05-03 17:49
status: evaluating
review-by: 2026-08-03
tags: [#learning/captured, #status/draft]
---

# HeyGen

> **Status:** `evaluating` — surfaced via the AI Influencer Revenue Pipeline capture (2026-05-03). Specific evaluation tied to the AI-influencer pattern; HeyGen is the dominant talking-head avatar tool for that use case.
> **Concept:** [[../concepts/ai-influencer-revenue-pipeline]]
> **First surfaced:** [[../daily/2026-05-03#17:49 — "OnlyFans + Claude Code" (X Article) by @Raytargt]] — @Raytargt (concept), enriched from heygen.com pricing pages and trade-press 2026 reviews
> **Last updated:** 2026-05-03 17:49

## What it is

Commercial AI avatar video generation platform. Specializes in **talking-head AI avatars** — realistic clones of real people (Avatar IV) or selection from 700+ pre-built avatars. Pairs with voice cloning (built-in or ElevenLabs) and a Claude MCP integration ("HeyGen Skills") that lets Claude Code or Claude Desktop drive end-to-end render workflows. See concept note for the broader AI-influencer pattern HeyGen fits into: [[../concepts/ai-influencer-revenue-pipeline]].

## Why it's on the radar for Optimus

1. **Anchor tool in the AI-influencer revenue pipeline pattern** captured 2026-05-03. If Optimus pursues AI-influencer as a revenue stream (personal side venture or productized client offering), HeyGen is the most-likely talking-head layer in the stack.

2. **Claude MCP integration** (parallel to Higgsfield's MCP). Means HeyGen plugs into Optimus's existing Claude-orchestrated workflow with minimal added complexity. Claude writes the script, HeyGen renders the avatar, all in one conversation.

3. **Talking-head specialization** complements Higgsfield's cinematic/scene focus. The two compose for production-grade AI-influencer pipelines: HeyGen for the avatar's on-camera moments, Higgsfield for B-roll / lifestyle / product shots. Different layers, not competing.

4. **Mature pricing + API tiers** (Free → $29 Creator → $99 Pro → $149 Business → API at $5+). Predictable cost modeling for client engagements. Compares favorably to hiring a human creator for daily-cadence content.

## Pricing structure (mid-2026)

| Tier | Cost | Key features |
|---|---|---|
| **Free** | $0 | 3 videos / month, 720p, watermarked, 3-min max — testing only |
| **Creator** | $29 / month | Unlimited 1080p, 700+ avatars, voice cloning, 175+ languages, 200 monthly credits |
| **Pro** | $99 / month | Same as Creator + 4K export, 10× Premium Credit usage, faster processing, translation script editing |
| **Business** | $149 / month + $20/seat | Team collab, longer videos (up to 60 min), SSO, integrations (Zapier, HubSpot) |
| **Enterprise** | Custom | Negotiated |
| **API** | $5+ start | ~$1 per minute of generated video at 720p / 1080p (standard generation) |

**Premium credit math (the gotcha):** Avatar IV (the realistic-clone tier — what production AI-influencer work actually uses) costs **20 credits per minute** of video. Creator's 200 monthly credits = **10 minutes of premium avatar video** per month. Daily-post cadence at 30-60 seconds per post requires Pro ($99/mo) or credit-pack add-ons. Model per-video cost AND monthly volume before subscribing.

## Adoption decision criteria

The tool gets promoted from `evaluating` to `adopted` only if a spike-test confirms ALL of:

- [ ] **Output quality on representative beauty / fashion / fitness / lifestyle prompt** matches what a brand-acceptable AI-influencer post requires. Avatar IV realism vs. uncanny-valley assessment. Test on Free tier before paying.
- [ ] **Per-client or per-vertical cost economics** fit Optimus's offering price points. Avatar IV at 20 credits/min × $1/16 credits = $1.25/min of premium video. Compare against the price the client pays for a Marketing Team (Tier-3) tier or whatever scoped engagement.
- [ ] **Claude MCP integration** is stable and battle-tested via direct spike-test. Run end-to-end Claude → script → HeyGen render → shareable link, measure failure rate, latency, edge cases.
- [ ] **ElevenLabs voice-clone integration path** is verified. Production AI-influencer work pairs HeyGen avatar with ElevenLabs voice; confirm the integration is clean (HeyGen's built-in voices may be sufficient for some verticals; for trust-driven verticals like education / B2B the founder-voice clone is needed).
- [ ] **Disclosure compliance** is achievable without tanking conversion. TikTok / Meta / YouTube AI-content rules require disclosure; the production-grade balance (visible badge vs. caption tag vs. platform-native AI flag) is something the spike-test must validate per platform.
- [ ] **Content fatigue / refresh cadence** is manageable. Test how long a single Avatar IV character can run before audience perceives staleness. Higgsfield Soul training is the comparison benchmark.
- [ ] **Voice-clone security** practices are operationalizable. ElevenLabs founder-voice clones are deepfake-class capabilities; the team needs key-rotation, access-restriction, and audit-trail discipline.

## Decision log

- **2026-05-03** — Surfaced via [[../daily/2026-05-03#17:49 — "OnlyFans + Claude Code" (X Article) by @Raytargt]] alongside the AI-influencer revenue pipeline concept. Status set to `evaluating`. No spike-test yet. Anchor tool for the AI-influencer evaluation track but not blocking any current Optimus offering.

## Related

- **Higgsfield AI** — sibling tool tracked at [[openclaw]] *(no — Higgsfield)* — see [[../concepts/higgsfield-ai-video-claude-integration]]. Composes with HeyGen for production AI-influencer pipelines (HeyGen for talking-head, Higgsfield for cinematic / B-roll / scene generation). Both have Claude MCP integrations.
- **ElevenLabs** — voice cloning layer in the AI-influencer stack. Not yet a tools-tracking entry. Surface to its own entry if a future capture goes deep on it.
- **Synthesia** — closest commercial competitor to HeyGen. Mentioned in trade-press enrichment but not deeply evaluated. Comparison capture pending.
- **Claude Code Playbook for Scaling Influencer Marketing (Stormy AI Blog)** — flagged in enrichment as the deepest published reference on Claude Code as the orchestrator for influencer pipelines. Worth a dedicated `/learn` capture as a follow-up.
