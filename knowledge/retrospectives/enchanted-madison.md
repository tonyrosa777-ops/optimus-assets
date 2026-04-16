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

---

## Session 14 Addendum — 2026-04-15 Responsive + CTA Polish Pass

Second round of client feedback from Angela (post-launch). Five fixes shipped this session; two revealed genuinely new bugs worth documenting in the cross-project vault.

### What shipped
- **Responsive header scaling** (commit `86559d1`) — initial type scale pass had hardcoded `h-28 / logo h-20 / 19px nav` with no breakpoints. Added `h-20 sm:h-24 lg:h-28`, `h-14 sm:h-16 lg:h-20`, `clamp(15px, 1.15vw, 19px)` for nav font, `gap-5 xl:gap-8`. Desktop ≥1280px preserved at Angela's approved scale; mobile/tablet/laptop degrade gracefully.
- **Velvet Buck + both campsites badged "Opens This June"** (commit `a556915`) — copy fix; Angela clarified timing.
- **Hero H1 no longer renders behind the fixed header on short laptops** (commit `7debbcb`) — `items-center` + 100vh + large H1 was overflowing upward into the nav zone on 1366×768 / 1440×800. Fixed with `items-start` + `pt-32 sm:pt-36 lg:pt-40`, vh-capped H1 `clamp(56px, min(8.5vw, 13vh), 140px)`, widened content column `min(1080px, 94vw)` so desktop H1 stays 2 lines.
- **Hero "See Packages" / "Book Now" CTAs functional** (commit `a421b7c`) — two compounding bugs: hero `<Image fill>` was intercepting pointer events, and anchor destinations landed behind the fixed header. Fixed with `pointer-events-none` + `relative z-10` on hero content, and global `scroll-padding-top` on `<html>`.

### New errors logged (#48, #49)
- **#48** Hero `<Image fill>` background intercepts pointer events → [[errors/hero-image-fill-intercepts-pointer-events]]
- **#49** `#anchor` links scroll target hidden behind fixed header → [[errors/anchor-scroll-hidden-behind-fixed-header]]

### New pattern logged (#43)
- **#43** `scroll-padding-top` on `<html>` with breakpoint-matched values → [[patterns/scroll-padding-top-for-fixed-header-anchors]]

### Extensions to existing entries (not new)
- Error #25 (mobile hero `items-center` centers text mid-screen) — today's finding extends the same root cause to short laptop viewports, where the symptom is worse: H1 overflows **up into the fixed header**. Same fix family: `items-start` with explicit `pt-*`. The hero pattern in `website-build-template.md` should default to `items-start` + header-safe pt, not `items-center`.

### Key lessons this session
1. **Pointer-events bugs are invisible in dev.** Hover works, render looks right, console is clean. Only a click test catches it. The multi-breakpoint audit (Pattern #33) must include "click every hero CTA", not just "render every hero CTA".
2. **Type scale passes without responsive breakpoints break laptops.** The initial "scale up" commit used global values. Every type/size scale pass must ship with breakpoint awareness in the same commit, not as a follow-up.
3. **Angela's screenshots outranked my in-browser verification.** Took three passes on the hero before I stopped trusting `items-center` and switched to `items-start`. Root-cause first, don't patch symptoms with bigger `pt`.

### Gaps flagged for toolkit (Phase 6)
- `website-build-template.md` hero scaffold should default to `pointer-events-none` on decorative bg image + `relative z-10` on content wrapper.
- `globals.css` scaffold should include `scroll-padding-top` breakpoints for the project's actual header height.
- Pre-launch auditor checklist should include: "Click every in-page CTA (hash anchors and route links). Verify destination heading is fully visible."
