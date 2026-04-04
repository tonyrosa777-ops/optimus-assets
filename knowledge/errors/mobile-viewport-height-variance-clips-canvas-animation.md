# Error: Mobile Viewport Height Variance Clips Canvas Animation Behind CTA

**Project:** Placed Right Fence
**Date:** Apr 2026
**Phase:** Hero animation polish (mobile)

## Problem
Canvas animation picket tip was landing in the correct position on one test device (iPhone SE, ~667px), but on taller phones (iPhone Pro Max, 932px) the tip disappeared completely behind the CTA button block. The exact same code produced visually different results on different physical devices.

## Root Cause
The picket tip position is `groundY - fullH`. When `groundY = H * 0.88` and fullH is fixed:
- On H=667: tip = 587 - 200 = 387px (above CTAs ✓)
- On H=932: tip = 820 - 200 = 620px (behind CTA buttons at 539px ✗)

The CTA row position is determined by content layout (fixed offset from top), not by H. But groundY scales with H. As phone height grows, the gap between tip and CTAs closes, then inverts.

## Solution
Make `fullH` viewport-height-aware:
```js
const fullH = H > 750 ? 240 : 200;
```
And cap groundY so it never pushes below a safe threshold:
```js
groundY: Math.min(H * 0.78, 700)
```
This ensures: on a 932px phone, groundY=700 (not 820), tip=700-240=460 — well above CTAs.

## Prevention
On mobile canvas animations where tip/element position must stay above content CTAs:
1. Never use fixed fullH — make it viewport-height-aware
2. Always cap groundY with Math.min() — never let it scale unbounded
3. Test on both short (667px) and tall (932px) viewports before signing off

## Related
- [[errors/canvas-animation-breaks-after-hero-flex-change]]
- [[patterns/responsive-canvas-animation-breakpoint-layout]]
