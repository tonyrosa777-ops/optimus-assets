# Enchanted Madison — Project Retrospective
**Type:** Luxury glamping / romantic experience property
**Location:** Madison, Indiana
**Completed:** March 2026
**Build sessions:** ~7

---

## What Went Well

- **fal.ai image generation** — Generated custom brand-matched imagery via terminal API. Eliminated the need for a full professional photoshoot before launch. Script pulled prompts directly from design-system.md photography direction.
- **Kling video hero** — AI-generated hero background video gave the site a premium feel without stock footage. Took <30 min to generate and deploy.
- **ROI Calculator** — Built as a sales tool on /optimus-pricing. CountUp animations + exaggerated motion made it emotionally compelling.
- **VIP Lead Capture** — react-hook-form + zod form with success state worked cleanly as a conversion mechanism.
- **Lodgify booking integration** — Embedded seamlessly without domain redirect.
- **Vercel MCP redeploy** — Triggered redeploys via MCP tool without leaving Claude Code.
- **build-log.md integration** — First build to reference cross-project error knowledge. Caught the Vercel subdirectory 404 issue before it happened.

---

## What Didn't (10 Gaps — All Closed)

| # | Gap | Fix Applied |
|---|-----|-------------|
| 1 | Blog/shop not decided before Phase 1 scaffolding | Phase 0 BLOCKER added to project-prime.md — sections matrix required before scaffold |
| 2 | progress.md updates batched to session end | Rule changed to per-subtask in CLAUDE.md + Standing Order #7 |
| 3 | Forms/lead capture not audited in discovery | New field added to intake-prompt.md Section 5 |
| 4 | Nav broke with >4 links | Nav split rule added to website-build-template.md |
| 5 | /optimus-pricing rebuilt from scratch | Pattern documented; template logic added to website-build-template.md |
| 6 | New page not wired into nav in same commit | Standing Order #12 added to CLAUDE.md |
| 7 | Booking placeholder accepted as phase-complete | Standing Order #13 added to CLAUDE.md |
| 8 | Sales tool animations underbuilt | fal.ai + Kling patterns + animation requirements documented |
| 9 | Generated assets not committed with task | Standing Order #14 added to CLAUDE.md |
| 10 | hero-forest.mp4 placed in repo root | Asset placement rules added to website-build-template.md |

---

## Tools Introduced This Build

- **fal.ai** — AI image generation via Node.js terminal API → see [[patterns/fal-ai-image-generation]]
- **Kling** — AI video generation web app for hero loops → see [[patterns/kling-video-hero]]

---

## Changes Made to Toolkit

All 10 gaps closed. See build-log.md Workflow Improvements table for full list.
`website-build-template.md` — nav rule, asset placement, AI asset generation section
`CLAUDE.md` — Standing Orders #12, #13, #14
`project-prime.md` — Phase 0 sections matrix BLOCKER
`intake-prompt.md` — forms/lead capture audit field
`knowledge/` — 4 error entries, 2 pattern entries added
