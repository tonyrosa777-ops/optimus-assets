# Error: Canvas Animation groundY Breaks After Hero Flex Alignment Change

**Project:** Placed Right Fence
**Date:** Apr 2026
**Phase:** Hero animation polish (multiple sessions)

## Problem
Canvas animation tip position was perfectly calibrated, then broke after changing the hero section's flex alignment from `items-center` to `items-start`. The picket tip visually shifted far down the screen and landed behind the CTA buttons.

## Root Cause
`groundY` was set as a percentage of `H` (e.g. `H * 0.88`). With `flex items-center`, hero content position scales proportionally with viewport height — so on a taller device, content and groundY both move proportionally and stay aligned. When hero was changed to `flex items-start`, content pinned to the top, but `groundY` still scaled with H. On a 932pt iPhone the groundY was 820px while content CTAs were at ~539px — tip landed completely behind the buttons.

## Solution
1. Switch hero to `items-start lg:items-center` (mobile top-aligned, desktop centered)
2. Apply a cap to mobile groundY: `Math.min(H * 0.78, 700)` — prevents groundY from pushing past 700px on any device, keeping the tip in the subheadline zone regardless of phone height
3. Recalibrate `fullH` independently of groundY: `H > 750 ? 240 : 200`

## Prevention
Any time you change the hero section's vertical alignment (`items-center` ↔ `items-start`), immediately recalibrate `groundY` in the canvas animation. They are coupled. Never change one without checking the other.

Also: never use a raw `H * N` percentage for `groundY` on mobile without a `Math.min()` cap. Phones vary from 667px (SE) to 932px (Pro Max) — a 40% height range. A percentage that looks right on one device will be 100+px off on another.

## Related
- [[errors/mobile-viewport-height-variance-clips-canvas-animation]]
- [[patterns/responsive-canvas-animation-breakpoint-layout]]
