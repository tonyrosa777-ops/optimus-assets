# JCM Graphics — Project Retrospective
**Type:** Local large-format printing, vinyl graphics, and signage company
**Location:** Salem, NH
**Completed:** 2026-04-12 (demo build — Phases 0-9 complete, 10-16 remaining)
**Build sessions:** 6+ (4 initial build + hero animation iteration + polish pass)

---

## What Went Well
- Full site scaffold (60 TypeScript files) built in a single session with 5 parallel agents — zero compile errors
- Gallery organized cleanly from 36 portfolio images across 7 categories before any code was written
- Design system synthesized correctly first try (electric steel blue + warm cream + jet black)
- Blog (10 articles), shop (13 seeded products), quiz (scored lead funnel), booking calendar all shipped in the initial sweep
- SEO/AEO (JSON-LD LocalBusiness schema, robots.ts, sitemap with blog slugs) completed efficiently
- New logo with transparent background integrated seamlessly — JCMCanvas `src` prop just points to the image file
- Chaos→convergence→explosion animation approach discovered through iterative design: tried per-letter reveals, identified the problem (unrecognizable mid-state), pivoted to single convergence — better result through honest assessment
- Spacing fix was a single 7-line CSS addition that repaired every page simultaneously
- Page-header ambient radial gradient replaced per-page custom effects — one CSS class, all interior pages look polished
- About-teaser section iterated through 4 layout attempts and landed on a clean 3-belief + photo balance
- CTA routing audit caught and fixed every inconsistent button href in two focused commits

---

## What Didn't
| # | Gap | Fix Applied |
|---|-----|-------------|
| 1 | Hero animation went through 9+ iterations (truck → roller → LogoParticles → per-letter → convergence) before landing on the right approach | Should have started with the proven LogoParticles pattern from Gray Method immediately, not attempted novel approaches first |
| 2 | Per-letter region reveal looked broken mid-animation — rectangular cuts through script font letters created unidentifiable fragments | Pivoted to single chaos→convergence→explosion approach; documented as Pattern #36 |
| 3 | Bolt outline trace (pentagon shape) was distracting and didn't match the actual logo geometry | Removed entirely; replaced with shockwave flash |
| 4 | Spacing CSS variables (`--space-*`) used across 6+ files but never declared — all component-level gaps collapsed to 0 | Added complete spacing scale to globals.css `:root`; logged as Error #39 |
| 5 | Spacing issue was only caught by human visual review, not by any automated tool | CSS custom properties with no declaration produce zero warnings in TypeScript, PostCSS, Tailwind, or browser console |
| 6 | Fixed navbar covered interior page content — no global offset applied to `<main>` | Added nav-height padding-top to layout; should be in scaffold template |
| 7 | CTA buttons inconsistently routed to /contact vs /booking across pages | Site-wide audit + hierarchy enforcement: primary → /booking, secondary → /quiz; add CTA href constants to site.ts and agent briefings |
| 8 | About-teaser required 4 commits to balance layout (beliefs → photo → paragraph → trim) | Design iteration is expected for above-the-fold sections; budget for it, don't treat first pass as final |
| 9 | Vehicle wrap references in content — JCM does lettering, not wraps | Content agents need explicit service boundary constraints in their briefings, not just service names |

---

## Tools Introduced This Build
- None new (fal.ai, Playwright, Framer Motion, canvas 2D API all previously established)

---

## Changes Made to Toolkit
- Error #38 added: More dropdown items missing from mobile nav drawer
- Error #39 added: undefined spacing CSS variables
- Error #40 added: fixed navbar covers interior page content
- Error #41 added: CTA routing inconsistency (/contact vs /booking)
- Pattern #36 added: chaos→convergence→explosion logo reveal
- Pattern #37 added: page-header ambient radial gradient
- **Recommended but not yet applied:**
  - Add `--space-*` scale to `website-build-template.md` as mandatory globals.css section
  - Add `pt-[var(--nav-height)]` to `<main>` in template layout.tsx scaffold
  - Add CTA routing constants (`PRIMARY_CTA_HREF`, `SECONDARY_CTA_HREF`) to site.ts template
  - Add CTA destination enforcement to agent briefings and pre-launch auditor checks
