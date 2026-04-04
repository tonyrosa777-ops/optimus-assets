# Pattern: Responsive Canvas Animation with Breakpoint Layout Function

**Category:** Animation / Architecture
**First used:** Placed Right Fence — Apr 2026

## What
A single `getLayout(W, H)` function returns all canvas animation parameters per breakpoint, keeping responsive logic centralized and preventing scattered magic numbers across the animation loop.

## When to Use
Any time a canvas 2D (or WebGL) animation must behave differently across mobile / tablet / desktop — different element counts, positions, sizes, or physics. Especially useful when the animation must stay visually aligned with surrounding page content (hero CTAs, headlines).

## How
```ts
interface Layout {
  n: number;        // element count
  spacing: number;  // gap between elements
  w: number;        // element width
  fullH: number;    // element height
  startX: number;   // horizontal origin
  groundY: number;  // vertical anchor (floor)
  isMobile: boolean;
}

function getLayout(W: number, H: number): Layout {
  if (W < 640) {
    // Mobile — viewport-height-aware sizing
    const fullH = H > 750 ? 240 : 200;
    return {
      n: 1, spacing: 0, w: 18, fullH,
      startX: W * 0.5,
      groundY: Math.min(H * 0.78, 700),  // ALWAYS cap on mobile
      isMobile: true,
    };
  }
  if (W < 1024) {
    // Tablet
    return { n: 8, spacing: 36, w: 12, fullH: 100,
      startX: W * 0.5 - (7 * 36) / 2,
      groundY: H * 0.80, isMobile: false };
  }
  // Desktop
  return { n: 10, spacing: 46, w: 15, fullH: 240,
    startX: W * 0.72 - (9 * 46) / 2,
    groundY: H * 0.73, isMobile: false };
}
```

Call `getLayout` inside a `useEffect` resize listener and re-initialize canvas state when layout changes.

## Key Rules
1. **Always cap mobile groundY with Math.min()** — phone heights vary 667–932px. A raw percentage will misplace elements on tall devices.
2. **Make fullH viewport-height-aware on mobile** — `H > 750 ? tallValue : shortValue`. Fixed fullH clips behind CTAs on Pro Max-class phones.
3. **groundY and hero flex alignment are coupled** — if you change `items-center` ↔ `items-start` on the hero section, recalibrate groundY immediately. See [[errors/canvas-animation-breaks-after-hero-flex-change]].
4. **Lock the values once approved** — canvas animation calibration takes many iterations. Once the user signs off, save exact values to project memory and never touch them without explicit instruction.

## Reuse Condition
Any project with a canvas hero animation that needs to remain visually aligned with page content across breakpoints and device heights.

## Related
- [[errors/canvas-animation-breaks-after-hero-flex-change]]
- [[errors/mobile-viewport-height-variance-clips-canvas-animation]]
