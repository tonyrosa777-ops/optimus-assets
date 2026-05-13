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

---

## Session 15 + 16 Addendum — 2026-05-13 Angela Revisions Pass

Third major round. Angela emailed a 6-page revision document covering homepage, About, Hot Tub Escapes, Stays, Proposals, Madison Guide, navigation, SEO, and analytics. 41 atomic commits shipped across Session 15 (planning + execution Phases A–K) and Session 16 (Playwright verification + 10 bugs caught + Pattern #51 systemic rollout). The full Angela revisions doc + verification report + changelog email are all logged in `progress.md` Sessions 15-16.

### What shipped
- **Phases A–L of a 12-phase execution plan** — every line item in Angela's revision doc shipped. Highlights: new SEO H1 + subheadline, sticky "Check Availability" CTA, Acuity gift certificate link in nav, double-pick friction removed on /date-night, About "What we believe" rewritten in Angela's voice, Cincinnati 75→60 min corrected sitewide, Google Analytics 4 installed, tent site SEO sweep, photographer FAQ rewrite, "Chandler Hotel" competitor mention removed.
- **The Starlit Buck shipped as a 5th property** with full fal.ai-generated photo set (warm-twilight Velvet Buck + deep-night Starlit Buck = distinct visual identities, ~$0.30 on flux/dev).
- **Per-property photo carousel** built on `/stays/[slug]` with `embla-carousel-react` + in-house Framer-Motion lightbox. Replaced the static hero image (redundancy with carousel below). Switched thumbnail to `object-contain` so portrait phone photos aren't cropped.
- **Pattern #51 luxury-gradient backgrounds applied site-wide** via one globals.css edit (Pattern #70). Site-wide audit found 11 pages with consecutive same-tone section runs (worst: /about with 6-cream-in-a-row). Single `::before` attribute-selector overlay with brass-tinted breathing orbs + 3 cream + 3 dark variants cycled through `:nth-of-type` modulo selectors — no per-section refactor.
- **VIP page luxury rebuild** — plain cream form replaced with dark hero + Fireflies/GodRays/Embers + glass-blur perk cards with brass-outlined ✦ medallions + glass-blur form with brass focus state + ShimmerText success state.
- **Orphan-cell grid bug class fixed** — /vip 3-perks-in-2-col (2+1 orphan) → vertical stack; /stays 5-stays-in-3-col (3+2 orphan) → featured (Cottage) + 2x2 grid of the rest. Codified as Pattern #71.
- **Photo source-filename remap** per Angela's stay-by-stay assignment rules (EC → Cottage, Glamping → Bell Tent + Campsite, Enhanced bedroom → Velvet Buck, Outdoor Movie → Cottage carousel). 26 source photos integrated; 2 previously orphaned files (Swing, Entrance, Outdoor Movie Bed) added to galleries. Photo source-filename rename pass deferred to a planned 15-min photo call with Angela.

### New errors logged (#59 – #63)
- **#59** Hero top padding insufficient for fixed header on `lg` — every page hero used static `pt-32` (128px) but SiteHeader is `h-28` (112px) on `lg` = 16px gap perceptually flush with the nav. Bulk fix: `pt-32 pb-` → `pt-32 sm:pt-36 lg:pt-40 pb-` across 15 hero sections. Class-of-bug pair with Error #49 (anchor behind fixed header) — both come from forgetting to budget for header height.
- **#60** H1 `clamp()` scale not retuned after headline content rewrite — Angela's 95-char SEO H1 rendered at 117px in the old `clamp(56, 140)` (sized for 28-char "Where Romance Meets the Wild"). CTAs pushed below the 900px fold. Retuned to `clamp(30, 60)`, then later `clamp(30, 100)` on wide desktops so the H1 fills the viewport meaningfully.
- **#61** Section alternation regression on revision-pass insertion — the new tagline section landed between cream trust strip and cream stays grid using default `bg-elevated`, creating 4 consecutive cream sections (violates Pattern #8 + Pattern #51). Fix: flip the inserted section to `bg-dark` + Fireflies. Class-of-bug: alternation rule existed but wasn't auto-checked when revisions insert into existing layouts.
- **#62** Sharp webp conversion silently drops EXIF Orientation tag — phone photos rendered sideways. Fix: add `.rotate()` to the sharp pipeline before resize/encode.
- **#63** Orphan-cell grid layouts — n items in `grid-cols-X` where `n % X !== 0` leaves the last row partially filled. User: *"we need to assume our viewer has OCD."*

### New patterns logged (#70 – #73)
- **#70** Auto-applied Pattern #51 gradients via CSS attribute selectors — `section[style*="var(--bg-*)"]::before` adds the gradient + breathing orb to every section that declares its bg via inline style. Zero per-section refactor. Saved an estimated 30+ commits.
- **#71** Never ship orphan-cell grids — decision matrix per item count (2 through 12+), featured-card recipe for odd counts ≥ 5, vertical stack alternative for 3-item sets, auto-fill minmax for dynamic counts. Pre-launch-auditor sweep: `grep -rnE "grid-cols-[2-5]"`.
- **#72** fal.ai parallel-property visual differentiation — when 2+ similar offerings exist, generate distinct fal.ai prompt aesthetics so they read as separate brand identities. Same scene types + identical style prefix + distinct style suffix per offering. Velvet Buck (warm twilight) vs Starlit Buck (deep-night Milky Way) shipped as the canonical example.
- **#73** Stay-prefix photo source-filename convention — every source photo named `[stay-slug]-[scene].ext` so integrate-photos.mjs mappings are unambiguous. Pre-launch 15-min rename pass with client; subfolder per category in `source-photos/`; ledger at project root tracking source → destination → photographer credit. Mandatory on every Optimus build with 2+ accommodations.

### Key lessons this session
1. **Live Playwright verification catches bugs typecheck doesn't.** All 10 bugs in Session 16's appendix were typecheck-clean and console-clean. The visual issues (orphan grids, oversized H1, section monotony, sideways photos, double-pick friction) only surface in a real browser at multiple viewports. Pattern #33 (multi-breakpoint browser audit) earned its place again.
2. **User reinforcement matters — codify the rule, don't just fix the instance.** Three times this session Angela / Anthony caught a class-of-bug, not a single instance: orphan grids, dark/cream alternation, sideways photos. Each became an Error + Pattern entry rather than a one-off fix. Pre-launch-auditor gets stronger every time.
3. **Photo source filenames are a workflow input, not a content output.** Angela's mixed-prefix filenames caused 3 mid-build re-mappings (Glamping → BT, Enhanced bedroom → VB, Outdoor Movie → Cottage). Documenting Pattern #73 + adding the question to `intake-prompt.md` Section 5 prevents this in every future build.
4. **Workflow rule reinforcement is content too.** User re-emphasized "always push and update progress.md" mid-session. Saved as durable feedback memory. Treat workflow rule reinforcement the same as a content rule reinforcement — it's a project decision that affects future agent behavior.

### Gaps flagged for toolkit (Phase 6)
- `website-build-template.md` — when adding a per-property photo carousel to an existing stay/listing template, the previous static hero image MUST be removed. Two large image surfaces back-to-back is redundancy (caught on Enchanted Madison cottage page).
- `project-prime.md` Phase 1 scaffold — `integrate-*-photos.mjs` template must include `.rotate()` before resize/encode (Error #62) and must read sources from `source-photos/<category>/` subfolders (Pattern #73).
- `pre-launch-auditor.md` — add 4 new checks:
  - Grep `grid-cols-[2-5]` and count items per match (Pattern #71)
  - Walk every page section flow for `>=3 same-tone in a row` (Error #61)
  - Hero header→eyebrow gap `>= 32px` at lg breakpoint via Playwright `getBoundingClientRect` (Error #59)
  - H1 height as % of viewport at 1440x900 + primary CTA above-fold check (Error #60)
- `intake-prompt.md` Section 5 — add: "Do your existing source photos use a stay-prefix convention (`cottage-bedroom.jpg`, `bell-tent-bathroom.png`)? If not, we'll do a 15-min rename pass before integration." (Pattern #73)
- `CLAUDE.md` — "Progress Tracking Rule" already covers per-subtask progress.md updates; user reinforcement this session confirms it's non-negotiable. No code change needed.

### Approximate cost + timing this round
- **fal.ai cost:** ~$0.30 for Velvet Buck + Starlit Buck galleries (12 images @ $0.025 on flux/dev)
- **Session 15 commits:** 26 atomic commits (revisions execution Phases A–K + Phase L deploy + changelog)
- **Session 16 commits:** 15 atomic commits (Playwright verification + 10 bug fixes + Pattern #51 systemic rollout + email refinement + photo placement)
- **Total session 15+16:** 41 commits, 5 new Errors, 4 new Patterns, 1 retrospective addendum (this section), zero TypeScript errors at every checkpoint.
