# Error: Hero top padding insufficient for fixed header on `lg`

**Project:** Enchanted Madison
**Date:** 2026-05-13
**Phase:** Stage 1I multi-breakpoint browser audit (post-revision verification pass)

## Problem
On `/stays/[slug]` pages (and 14 other inner pages), the hero `eyebrow` label and `<h1>` were rendered **flush against the bottom of the fixed `SiteHeader`** at the `lg` breakpoint. At 1440×900 the eyebrow text was literally touching the nav — no breathing room. Most obvious on light-background hero pages where there's no atmospheric mask. Dark heroes with Fireflies / GodRays particles visually hid the bug at first glance but the underlying spacing was the same.

Caught by user during Playwright pass:
> *"way to close to the nav bar? the text is literally touching it"*

## Root Cause
The SiteHeader is `h-20 sm:h-24 lg:h-28` (80 / 96 / 112 px tall). Almost every page hero section used static `pt-32` (128 px). On `lg`:

  128 px (pt-32) − 112 px (h-28) = **16 px of breathing room**

16 px is below the perception threshold for "this section is below the nav" — eye reads the eyebrow as glued to the navbar.

Compounded by:
1. `pt-28` (112 px) on `/stays/[slug]` — gave **0 px** of breathing room on `lg`
2. Static padding (no responsive variants) — pattern was set in stone for whichever breakpoint the dev tested

## Solution
Use a responsive padding scale that always provides `~48px` breathing room above the eyebrow at every breakpoint:

```tsx
// Before — touches nav on lg
<section className="pt-32 pb-16 px-4">

// After — clean 48px gap at every breakpoint
<section className="pt-32 sm:pt-36 lg:pt-40 pb-16 px-4">
```

Math:
| Breakpoint | Header | Padding-top | Gap |
|---|---|---|---|
| mobile | h-20 (80px) | pt-32 (128px) | 48px ✓ |
| sm     | h-24 (96px) | pt-36 (144px) | 48px ✓ |
| lg     | h-28 (112px) | pt-40 (160px) | 48px ✓ |

Bulk-fix one-liner used (Enchanted Madison, May 2026):
```bash
grep -rl "pt-32 pb-" --include="*.tsx" src/app \
  | xargs sed -i 's/pt-32 pb-/pt-32 sm:pt-36 lg:pt-40 pb-/g'
```

15 files updated in a single commit; verified with Playwright that header-bottom → eyebrow-top gap went from `15px` → `47px` on `/about`.

## Prevention
1. **Project scaffold rule** (add to `website-build-template.md` Phase 1): every page hero section MUST use `pt-32 sm:pt-36 lg:pt-40` if the header is `h-20 sm:h-24 lg:h-28`. If the project uses different header heights, derive the padding scale: `pt-X` where `X * 4px >= headerHeight + 48px`.
2. **Pre-launch auditor check** (add to Stage 1I): for every page, measure `getBoundingClientRect()` of the first eyebrow/h1 element vs the header's bottom edge at `lg`. Anything < 32px is a fail.
3. **Class-of-bug pairing**: this is the static-counterpart of [[errors/anchor-scroll-hidden-behind-fixed-header]] — both bugs come from forgetting to budget for header height. Anchor links use `scroll-padding-top` on `<html>`; hero section uses responsive `pt-*` classes. Same prevention principle, different mechanic.
4. **Dark heroes mask the bug visually**. Particle systems / atmospheric gradients camouflage 16px under-spacing. Devs who test only on `/about` or `/proposals` won't see it; devs who test on light-background interior pages catch it immediately. Always test a light-bg interior page (typical surfaces: `/contact`, `/stays/[slug]`, `/privacy`).

## Related
- Error: [[errors/anchor-scroll-hidden-behind-fixed-header]] (same root cause family — fixed header height budgeting)
- Error: [[errors/fixed-navbar-covers-interior-page-content]] (JCM Graphics) — even more severe variant where `<main>` had no offset at all
- Pattern: [[patterns/scroll-padding-top-for-fixed-header-anchors]] (companion fix for anchor links)
- Pattern #34 build-log: clamp-based responsive type scale (same architectural principle: scale with breakpoint, not static)
