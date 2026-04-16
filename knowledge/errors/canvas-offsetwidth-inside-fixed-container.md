# Error: Canvas uses offsetWidth/Height inside fixed/absolute container — renders in tiny corner
**Project:** Witt's Restoration LLC
**Date:** 2026-04-12
**Phase:** Post-sweep animation fixes

## Problem
RisingAsh canvas particle animation only rendered in a small corner of the page header instead of spanning the full width. The canvas appeared as a tiny cluster of particles in the top-left.

## Root Cause
The canvas element used `canvas.offsetWidth` and `canvas.offsetHeight` for its pixel dimensions, but these properties return 0 or very small values when the canvas has `position: absolute; inset: 0` inside a container — because the canvas itself has no intrinsic dimensions. The ResizeObserver was observing the canvas element, not its parent container.

## Solution
Changed to observe the **parent element** via ResizeObserver and use `parent.getBoundingClientRect()` for canvas pixel dimensions:
```typescript
const parent = canvas.parentElement;
const ro = new ResizeObserver(() => {
  const rect = parent.getBoundingClientRect();
  canvas.width = rect.width;
  canvas.height = rect.height;
});
ro.observe(parent);
```
Parent section must have `position: relative; overflow: hidden`.

## Prevention
- Canvas animation components should ALWAYS size from parent container, not from self
- Use `parentElement.getBoundingClientRect()` not `canvas.offsetWidth`
- Parent must be `relative overflow-hidden` for absolute canvas to fill correctly
- Test canvas animations visually in browser before marking complete — pixel dimensions of 0 produce no build errors

## Related
- Error #10: canvas groundY breaks after hero flex change (same category — canvas sizing)
- Error #11: mobile viewport height variance clips canvas animation
