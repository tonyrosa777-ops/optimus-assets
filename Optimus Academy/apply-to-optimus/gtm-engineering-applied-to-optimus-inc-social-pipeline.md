---
title: GTM Engineering applied to Optimus Inc's own outbound pipeline
schema-version: 1
concept: [[../concepts/gtm-engineering]]
source-references: ["[[../daily/2026-05-02#23:34 — \"If you're a SWE or Marketer looking for a change, look into GTM Engineering\" by @maven_hq]]"]
applies-to: [[../../Optimus Inc/social-pipeline/README]]
created: 2026-05-02
last-updated: 2026-05-02 23:34
status: not-started
value-vector: [revenue, productivity]
expected-impact: medium
tags: [#learning/applied, #applies-to/optimus-inc/marketing, #value-vector/revenue, #value-vector/productivity, #status/active]
---

# GTM Engineering applied to Optimus Inc's own outbound pipeline

> **Concept:** [[../concepts/gtm-engineering]]
> **Source(s):**
> - [[../daily/2026-05-02#23:34 — "If you're a SWE or Marketer looking for a change, look into GTM Engineering" by @maven_hq]] — @maven_hq
> **Applies to:** [[../../Optimus Inc/social-pipeline/README]]
> **Status:** `not-started`
> **Value vector(s):** revenue, productivity
> **Expected impact:** medium
> **Last updated:** 2026-05-02 23:34

## What I learned

GTM engineering — see [[../concepts/gtm-engineering]] — is a discipline where one technical operator produces SDR-team-equivalent outbound output by wiring together Clay (enrichment + AI personalization) + cold-email infrastructure (Smartlead/Instantly) + LinkedIn automation (HeyReach) + CRM (HubSpot/Salesforce) + automation glue (n8n/Make/Zapier) + an AI layer. Total stack cost for a solo operator runs $700–$1,500/month. The 2026 shift is toward AI GTM engineering and "revenue data engineering" — clean data pipelines over which AI agents act.

## Why it applies to Optimus Inc's own outbound pipeline

The 2027-Q3 drink-own-champagne milestone (per `anthony-rosa/north-star.md`) requires Optimus's own marketing and inbound qualification to run autonomously. Today, `Optimus Inc/social-pipeline/` is a placeholder — there is no operating outbound system. GTM engineering is the canonical reference shape for what that system needs to do:

- **Ideal-client targeting** — local SMBs in defined niches who would buy website-dev + AI-agent tiers.
- **Multi-source enrichment** — LinkedIn for decision-maker, public web for fit signals, intent data for buying-readiness (recent website launch, recent hiring posts for marketing roles).
- **Personalized multi-channel outbound** — cold email + LinkedIn DM, Optimus voice + offer, AI-generated per-prospect opening line.
- **CRM logging** — Supabase as system of record (already aligned to Optimus's Python stack).
- **Notification + follow-up automation** — Anthony as the human-in-the-loop reviewer for high-value leads via SMS / Slack.

Building this is also the most direct way to validate the Tier-3 offering — Optimus runs the offering on itself before selling it. (See companion bridge `[[gtm-engineering-applied-to-marketing-team]]`.)

## How to apply it

This is a build plan, not a code change. The bridge captures the WHAT; sequencing and timing depend on Optimus's runway and current focus.

1. **Decide the stack substitution.** The canonical GTM-eng stack uses Clay + Smartlead + HeyReach + n8n. Optimus's canonical Python stack (per `feedback_optimus-canonical-stack.md`) is FastAPI + anthropic SDK + Pydantic + Supabase + Twilio. The drink-own-champagne version of Optimus's outbound should be Python-native, NOT bolted onto Clay+n8n. Document the per-substep mapping (e.g., Clay enrichment → custom Python enrichment service hitting Apollo's API + LinkedIn scrape).
2. **Define ICP scoring rules in code.** The ICP today is implicit. Make it explicit: industry, company size band, geography, signals (recently launched a website, recently posted hiring for a marketing role). Code these as Pydantic models persisted in a Supabase table that the outbound agent reads.
3. **Build the cold-email infrastructure first.** Domain warmup, secondary-inbox rotation, deliverability monitoring. This is the longest-lead-time part of any GTM-eng setup; if it's not started, nothing downstream is unblockable.
4. **Layer the LinkedIn automation in second.** Connection requests + follow-up DMs targeting the same ICP. Capture each prospect's response in Supabase.
5. **Wire the AI personalization layer.** Anthropic SDK calls that take an enriched prospect record and generate a per-contact opening line / value-prop framing. Cache aggressively (per `claude-api` skill guidance) since most prospect records don't change between sequence runs.
6. **Anthony reviews high-value leads via SMS / Slack.** Twilio sends a notification when a prospect responds positively; Anthony qualifies and books from the phone.

## Value vector reasoning

- **revenue** — every additional booked discovery call from systematic outbound is a chance to close a $1,500+ Starter or $3,000+ Pro website build, plus follow-on AI-agent tiers. Currently lead-gen is opportunistic (network, referrals); switching to a systematic GTM-engineering stack changes the slope of the pipeline.
- **productivity** — Anthony's own time today is split between client builds and sales motion. A GTM-engineering pipeline removes the manual "find the company → find the contact → write the email → send → follow up" loop from his day; he reviews and qualifies, not prospects.

## Status

`not-started`

## Updates

(none)
