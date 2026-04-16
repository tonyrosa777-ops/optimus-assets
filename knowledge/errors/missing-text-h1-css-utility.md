# Error: Missing text-h1 CSS utility causes tiny page headings
**Project:** Witt's Restoration LLC
**Date:** 2026-04-12
**Phase:** Post-sweep retro fixes

## Problem
All interior page headings rendered at default browser text size instead of the large display size. The `text-h1` Tailwind utility class was used across 8+ page components but was never defined in globals.css. Only `text-display`, `text-h2`, `text-h3`, and `text-h4` existed in the clamp-based type scale.

## Root Cause
The scaffold created the type scale utilities but skipped `text-h1`, jumping from `text-display` (for hero) directly to `text-h2`. Page components were written referencing `text-h1` which didn't exist — Tailwind silently ignores unknown utility classes with zero build warnings.

## Solution
Added `text-h1` utility to globals.css with the same values as `text-display`:
```css
@utility text-h1 {
  font-size: clamp(2.5rem, 8vw, 4.5rem);
  line-height: 1.05;
  font-weight: 800;
}
```
Then standardized all page headers to use `hero-shimmer font-display text-display` (the proven pattern from Testimonials page) instead of `text-h1`.

## Prevention
- Scaffold phase must define ALL utility tiers referenced in the design system (text-display through text-h4)
- Pre-launch auditor should grep for CSS utility classes used in components and verify each has a definition
- Standardize on one class combo for all page H1s: `hero-shimmer font-display text-display`

## Related
- Error #37: fixed-rem display font size breaks mobile (same category — type scale issues)
- Pattern #34: clamp-based responsive type scale
