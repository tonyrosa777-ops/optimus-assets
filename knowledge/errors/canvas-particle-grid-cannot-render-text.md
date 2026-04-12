# Error: Canvas Particle Grid Cannot Render Antialiased Text
**Project:** Gray Method Training
**Date:** Apr 2026
**Phase:** Hero LogoParticles component build

## Problem
Built a canvas-based hero animation that samples a logo image pixel-by-pixel and renders each bright pixel as a colored particle. The overall circular badge and "GRAY METHOD" main banner were somewhat recognizable, but the subtitle text "ONLINE HEALTH & FITNESS" was unreadable — blurry, smudged, indistinct. Increasing the sample density from 200px to 260px and then trying even denser sampling with tighter particle spacing did not fix it. The user's response: "its still really fuzzy?"

## Root Cause
Square pixels at any grid density cannot render antialiased text. The subtitle text in a typical circular badge logo is only ~8–12 px tall at source resolution. When particles represent this text as a grid of square rects:
- Letter curves become stair-stepped
- Thin strokes alias against the particle grid
- Sub-pixel antialiasing (which real text rendering uses) is impossible
- The eye perceives the result as blurry even when the particles are perfectly placed

Higher particle density doesn't help — each letter still only has the same number of sampled pixels, and doubling the particles just creates overlapping squares.

## Solution
Hybrid rendering: use particles for animation drama, use `drawImage()` for the final crisp state.

```typescript
// During assembly phases (converge → hold → explode): draw particles
if (phase !== "idle") {
  drawParticles(...);
}

// Crossfade: particles fade out as image fades in during explode phase
if (phase === "explode") {
  drawLogoImage(phaseT); // alpha = 0..1 over explode duration
} else if (phase === "idle") {
  drawLogoImage(1); // full opacity, crisp forever
}
```

`drawImage()` with `imageSmoothingQuality: "high"` renders the logo pixel-perfect because the browser uses real image scaling, not a grid of squares.

## Prevention
- **Rule:** particle grids are for decoration and assembly animation only. If the final rendered output needs to be legible (text, fine detail, thin strokes), the idle state must use `drawImage()` or inline SVG — not particles.
- If a client logo contains text, plan for the hybrid approach from the start — don't try to solve it with denser sampling.
- The assembly animation can still use particles sampled from the logo image (for colors) — they just need to hand off to the real image before the user is expected to read anything.

## Related
- [[patterns/logo-particles-phased-reveal]] — the reusable pattern that emerged from this fix
- [[errors/canvas-effect-overlay-washes-out-text]] — sibling bug discovered in the same build
