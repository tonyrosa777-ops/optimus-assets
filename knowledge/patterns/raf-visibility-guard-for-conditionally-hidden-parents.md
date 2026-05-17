# Pattern: rAF visibility guard for canvas animations in conditionally-hidden parents
**Category:** Animation / Performance
**First used:** Goddu Imprint — 2026-05-17

## What
Canvas animations whose parent element is conditionally hidden via CSS (`hidden lg:block`, `display: none`, `prefers-reduced-motion` toggles, conditional render branches) need a visibility guard in the rAF loop. The guard pauses the loop entirely when the canvas has zero dimensions and resumes from the resize handler when dimensions return positive. Naive guards that reschedule rAF while dimensions are 0 burn the main thread at 60Hz forever on mobile.

## When to Use
Every canvas component imported by a section that uses responsive visibility classes (`hidden`, `lg:block`, breakpoint-conditional render). Especially:
- Hero canvas animations in `hidden lg:block` wrappers (the GodduCanvas case)
- Decorative canvas effects in sections that hide on mobile
- Any `<canvas>` rendered inside a parent with conditional `display: none` toggling

Skip the pattern only when the canvas's parent is always visible across all breakpoints AND can never transition to `display: none`.

## How

Track a `loopActive` flag near the `rafId` declaration:

```ts
let rafId = 0;
let loopActive = false;
```

Inside the `draw` loop, the 0×0 guard pauses without rescheduling:

```ts
const draw = (t: number) => {
  // Pause the loop entirely when parent is hidden (e.g. mobile `hidden lg:block`).
  // Previously rescheduled rAF at ~60Hz forever, wasting main-thread time
  // and battery on every mobile pageview.
  // Resumed by onResize when dimensions transition back to positive.
  if (W <= 0 || H <= 0) {
    loopActive = false;
    return;
  }
  // ... draw logic
  rafId = requestAnimationFrame(draw);
};
```

Each rAF ignition site sets `loopActive = true` before scheduling:

```ts
// PNG-onload success branch (must match other branches — see Error #65)
logoImg.onload = () => {
  if (octx) {
    octx.drawImage(logoImg, 0, 0, SAMPLE_SIZE, SAMPLE_SIZE);
    sourceCanvas = off;
    sourceReady = true;
    buildParticles();
    loopActive = true;
    rafId = requestAnimationFrame(draw);
  }
};

// PNG-onerror fallback branch
logoImg.onerror = () => {
  sourceCanvas = renderWordmarkToCanvas();
  sourceReady = true;
  buildParticles();
  loopActive = true;
  rafId = requestAnimationFrame(draw);
};

// Text-only readyHandler branch (no src= prop)
const readyHandler = () => {
  sourceCanvas = renderWordmarkToCanvas();
  sourceReady = true;
  buildParticles();
  loopActive = true;
  rafId = requestAnimationFrame(draw);
};
```

Resize handler restarts the loop when dimensions become positive:

```ts
let resizeFrame = 0;
const onResize = () => {
  cancelAnimationFrame(resizeFrame);
  resizeFrame = requestAnimationFrame(() => {
    buildParticles();  // Calls sizeCanvas() internally, updates W and H
    // Restart loop if it paused while hidden
    if (!loopActive && W > 0 && H > 0) {
      loopActive = true;
      rafId = requestAnimationFrame(draw);
    }
  });
};
window.addEventListener("resize", onResize);

return () => {
  cancelAnimationFrame(rafId);
  cancelAnimationFrame(resizeFrame);
  window.removeEventListener("resize", onResize);
};
```

## Key Rules
- **Pause, don't reschedule.** The old anti-pattern was `if (W <= 0) { rafId = requestAnimationFrame(draw); return; }`. That rescheduled at ~60Hz forever on every mobile pageview, wasting main thread + battery, threatening Lighthouse ≥ 90 budget per CLAUDE.md Performance Standards.
- **All ignition sites set `loopActive = true`.** The PNG-onload branch and the text-only branch and the onerror branch all schedule rAF — every site must update the invariant. Missing one site = latent regression that activates when that branch executes (e.g., when a client adds a logo PNG asset).
- **Resize handler is the resume mechanism.** Window resize crossing the `lg` breakpoint (1024px) is what transitions the parent from `display: none` to `display: block`. The handler's job: rebuild particles for new dimensions AND restart the loop if it paused.
- **Pairs with Pattern #44 (Error #44).** Canvas `offsetWidth`/`offsetHeight` inside fixed/absolute container returns 0 — the same root cause. Pattern #44 fixes by using `parentElement.getBoundingClientRect()` and observing the parent with ResizeObserver; this pattern fixes by guarding the rAF loop against zero dimensions. Both apply to canvas in mobile-hidden parents.

## Reuse Condition
Apply to every canvas-based hero animation on every future Optimus build where:
- The canvas wrapper uses `hidden lg:block` (or any breakpoint-conditional visibility)
- The canvas component's `useEffect` starts an rAF loop that calls `sizeCanvas()` on first frame
- The build is positioned as luxury/premium where Lighthouse ≥ 90 budget matters

Add to animation-specialist.md template as part of the canvas-component scaffold.

## Goddu Imprint trace
- BUG-5 from `/optimus-review` run-1: rAF rescheduled at 60Hz forever when GodduCanvas parent was `hidden lg:block`. Caught at Stage 1J.
- First fix (commit ef6ac5a) used `replace_all=true` and silently missed the PNG-onload branch's deeper indentation.
- Run-2 verifier caught the missed branch as a state-invariant violation (latent since no `src=` prop in production, but real for any future logo PNG).
- Second fix (commit 467ef0b) added `loopActive = true;` to the PNG-onload branch.

## Related
- Pattern #44 / Error #44 (vault build-log) — canvas offsetWidth inside fixed/absolute container = 0
- Pattern [[iterate-to-clean-n-run-review]] — caught the half-shipped fix
- Error [[../errors/edit-replace-all-silently-misses-indentation-variants]] — class-of-bug from the half-shipped fix
- Pattern [[api-public-form-defense-in-depth]] — companion BUG fix from the same Stage 1J session
