# Error: Hero `<Image fill>` background intercepts pointer events, silently killing CTA clicks
**Project:** Enchanted Madison
**Date:** 2026-04-15
**Phase:** Post-launch polish / client feedback

## Problem
Client (Angela) reported "See Packages" and "Book Now" CTAs in the hero of `/date-night` and `/proposals` "don't work" — clicks appeared to do nothing. No console errors, no network activity, no route change. Buttons rendered correctly, hover styles worked.

Playwright reproduced the bug cleanly and gave the exact diagnosis:
```
<img sizes="100vw" ... alt="Private date night escape..."> intercepts pointer events
```

## Root Cause
The hero pattern used was:
```tsx
<section className="relative ...">
  <Image src="..." fill className="object-cover" />   {/* absolute, later-paint */}
  <Fireflies /> <GodRays />
  <FadeUp>                                             {/* static flow, no z-index */}
    <h1>...</h1>
    <Button href="#packages">See Packages</Button>
  </FadeUp>
</section>
```

Two compounding problems:
1. `<Image fill>` renders as `position: absolute; inset: 0`. Because it appears earlier in the DOM but has `position: absolute`, it paints **above** later static-flow siblings that have no explicit `z-index`.
2. The `<FadeUp>` content wrapper was static flow with no `relative z-10`, so the image stacking context won.

Result: the hero image layer sat on top of the CTAs and captured every click. Visually everything looked fine because the image was at 0.28 opacity. Functionally the buttons were dead.

## Solution
Two-line fix per hero:
```tsx
<Image ... className="object-cover pointer-events-none" />
...
<FadeUp className="relative z-10">
```

- `pointer-events-none` on the decorative background image so clicks pass through it.
- `relative z-10` on the content wrapper so it owns the top of the stacking context regardless of DOM order.

Applied to [src/app/date-night/page.tsx](enchanted-madison/src/app/date-night/page.tsx) and [src/app/proposals/page.tsx](enchanted-madison/src/app/proposals/page.tsx).

## Prevention
Any hero that uses `<Image fill>` (or any full-bleed absolutely-positioned decorative layer) **must**:
- Add `pointer-events-none` to the decorative layer
- Give the content wrapper `relative z-10`

Add to the hero scaffold in `website-build-template.md` so every future build ships with this baked in. Otherwise the bug is invisible during dev — you only catch it when a user actually tries to click a CTA and nothing happens. Console shows nothing. Lighthouse shows nothing. Only Playwright's pointer-events trace exposes it.

Also: **manually click every hero CTA in Playwright** during the end-of-build multi-breakpoint audit (Pattern #33). Hover states alone aren't proof of function.

## Related
- Pattern: [[patterns/scroll-padding-top-for-fixed-header-anchors]] (same commit — companion fix for anchor destinations)
- Extends Pattern #33: End-of-build multi-breakpoint browser audit must include CTA click verification, not just render verification.
