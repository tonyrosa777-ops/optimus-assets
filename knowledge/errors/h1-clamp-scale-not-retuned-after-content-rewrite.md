# Error: H1 `clamp()` scale not retuned after headline content length doubled

**Project:** Enchanted Madison
**Date:** 2026-05-13
**Phase:** Client revisions pass (Stage 1I verification)

## Problem
Homepage H1 was rendering at `117 px` on 1440×900 viewport, wrapping to 6+ lines, pushing both hero CTAs (`Make It Unforgettable`, `Find My Escape →`) completely **off-screen below the fold**. The hero looked like a wall of typography with no call-to-action.

Caught by user during Playwright pass:
> *"the h one text is so big that there's no CTAs. The two CTA buttons are just nonexistent."*

## Root Cause
The H1 font-size clamp was tuned for a **short** original headline:

```tsx
// Hero in HeroSection.tsx
fontSize: "clamp(56px, min(8.5vw, 13vh), 140px)"
```

Original H1: `"Where Romance Meets the Wild"` — 28 characters, fit on 1 line at any size in this clamp.

New H1 (Angela's revision, SEO-optimized long-tail): `"Private Hot Tub Escapes, Luxury Glamping and Bell Tent sites in Madison, Indiana"` — **95 characters, 3.4x longer**.

At 1440px wide with `paddingLeft: clamp(24px, 7vw, 96px)` and `maxWidth: min(1080px, 94vw)`, the clamp resolved to `min(8.5vw, 13vh) = min(122px, 117px) = 117px`. 95 chars at 117px font-size in a ~975px text column = ~8 chars per line = **12 lines** of headline. CTAs lived at y ≈ 1400px on a viewport of 900px height. Invisible.

The content layer (data) and the presentational layer (CSS clamp) were independently maintained. When the data changed, the CSS didn't get retuned.

## Solution
Tighten the clamp scale to match the new headline length:

```tsx
// Before — sized for 28 chars
fontSize: "clamp(56px, min(8.5vw, 13vh), 140px)"

// After — sized for 95+ chars
fontSize: "clamp(30px, min(4.2vw, 6.5vh), 60px)"
```

Also tightened `leading-[1.02]` → `leading-[1.08]` to give long wrapped lines more breathing room.

Verified:
- 1440×900: font-size = `58.5 px` (was `117 px`)
- Primary CTA `y = 753 px` → comfortably above the 900px fold
- H1 wraps to ~3 lines instead of ~12

## Prevention
This is a **class-of-bug** that recurs whenever a client revision swaps a short brand-voice H1 for a long SEO H1, or vice versa. Three preventive measures:

1. **Content-length budget annotation in `site.ts`**: when defining a clamp-tuned headline, document the design budget inline:
   ```ts
   hero: {
     // Headline budget: ≤ 35 chars (tuned in HeroSection.tsx clamp).
     // Longer headlines require retuning fontSize clamp.
     headline: "Where Romance Meets the Wild",
   }
   ```
   If a future edit exceeds the budget, the comment forces the dev to acknowledge the clamp retune.

2. **Pre-launch auditor check** (Stage 1I): for every page H1, measure `getBoundingClientRect()`'s height vs viewport height at 1440×900 and 390×844. H1 occupying > 35% of viewport height is a fail — CTAs are likely below the fold. Auto-fail rule:
   ```js
   const h1 = document.querySelector('h1');
   const h1H = h1.getBoundingClientRect().height;
   const ratio = h1H / window.innerHeight;
   if (ratio > 0.35) fail(`H1 occupies ${(ratio*100).toFixed(0)}% of viewport`);
   ```

3. **CTAs-above-fold gate**: at 1440×900, primary CTA's `getBoundingClientRect().top` MUST be < 900px (i.e. visible without scrolling). Should be part of the Stage 1I checklist alongside hero-padding check.

4. **Cross-reference to existing patterns**:
   - Pattern #34 (Gray Method Training): clamp-based responsive type scale — declare clamp at Phase 1, retune is then a one-file edit
   - Pattern #35 (Gray Method Training): conversion-first hero headline — H1 is one of the most-contested copy fields; expect 3-5 revisions per build; bake retune workflow in
   - Error #37 (Gray Method Training): `--text-display: 4.5rem` H1 breaks at mobile width — closely related; same root cause (static font-size + variable content length)

## Related
- Error: [[errors/fixed-rem-display-font-size-breaks-mobile]] — closely related; same fix family (clamp instead of fixed-rem)
- Pattern: clamp-based responsive type scale (build-log Pattern #34)
- Pattern: conversion-first hero headline (build-log Pattern #35)
