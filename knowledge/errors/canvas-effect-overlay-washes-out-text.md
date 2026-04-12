# Error: Canvas Effect Overlays Wash Out Text
**Project:** Gray Method Training
**Date:** Apr 2026
**Phase:** Hero LogoParticles component — energy effects

## Problem
After fixing the fuzziness by switching to hybrid `drawImage()` rendering, the idle state drew continuous energy effects on top of the crisp logo: a rotating gold arc on the ring, a horizontal shimmer sweep, and additive sparkle bursts. All three were drawn with `globalCompositeOperation = "lighter"` for a glowing additive feel.

Problem: the ring pulse and shimmer sweep both passed through the "GRAY METHOD" banner and "ONLINE HEALTH & FITNESS" subtitle at various points in their animation cycles, washing out the dark text on the gold banner and making it hard to read. Additive blending over already-bright pixels pushed them toward white, reducing contrast.

The user's response: "if you can make the flowing energy part go behind the text so it never interferes with the readability that would be ideal".

## Root Cause
Additive overlay effects (rotating arcs, shimmer sweeps) that traverse the entire canvas will eventually pass over any text area. Even with `lighter` blend mode (which only adds brightness), the result on already-bright text banners is to push them toward pure white, destroying the contrast with the dark text characters.

Drawing the effects BEHIND the image doesn't work either:
- If the logo PNG has a solid dark background, effects behind it are invisible
- If the logo PNG is transparent, the ring pulse gets hidden wherever the ring itself is opaque — which is exactly where you wanted it visible

## Solution
Use `ctx.clip("evenodd")` with two subpaths to carve a hole in the drawable area for all energy effects:

```typescript
// Inside the idle phase, before drawing ring pulse and shimmer:
const bannerY0 = canvas.height * 0.34;
const bannerY1 = canvas.height * 0.80;

ctx.save();
ctx.beginPath();
ctx.rect(0, 0, canvas.width, canvas.height);      // full canvas
ctx.rect(0, bannerY0, canvas.width, bannerY1 - bannerY0); // banner hole
ctx.clip("evenodd"); // evenodd: points in both rects are EXCLUDED

drawRingPulse(elapsed);
drawShimmerSweep(elapsed);

ctx.restore();
```

The `evenodd` fill rule means "a point is inside if contained in an odd number of subpaths". Points inside the banner hole are contained in both rects (count = 2 = even = excluded). Points outside the banner but inside the canvas are contained in 1 rect (odd = included). The effect: nothing draws in the banner strip.

Separately, sparkle spawn candidates are filtered to the same exclusion at sample time, so sparkles physically cannot land on text:

```typescript
if (brightness > 200) {
  const yFrac = hy / canvasSize;
  if (yFrac < 0.34 || yFrac > 0.80) {
    spawnableSpots.push({ x: hx, y: hy });
  }
}
```

## Prevention
- **Rule:** any canvas overlay effect drawn over a logo with text must be clipped to exclude the text area, OR drawn before the image with the image rendered opaque on top.
- **Tuning rule for circular badge logos:** the banner text region typically extends from y ≈ 0.34 × H to y ≈ 0.80 × H. Start with that range and tune inward if the logo is unusual. The subtitle extends LOWER than most people estimate — initial guess of 0.68 was too shallow; the actual bottom was closer to 0.78.
- **Visual bonus:** when the exclusion is working correctly, rotating effects appear to "dive behind" the banner as they pass through, reading as intentional depth layering rather than a bug.
- For sparkles and discrete effects, filter spawn positions at sample time. Don't rely on clipping alone — it's cheaper to not spawn than to clip every frame.

## Related
- [[patterns/logo-particles-phased-reveal]]
- [[errors/canvas-particle-grid-cannot-render-text]]
