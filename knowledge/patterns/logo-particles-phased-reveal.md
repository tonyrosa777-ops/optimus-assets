# Pattern: LogoParticles Phased Reveal
**Category:** Animation / Architecture
**First used:** Gray Method Training — Apr 2026

## What
Hybrid canvas animation that samples a logo image into particles, runs a four-phase reveal (converge → hold → explode → idle), crossfades to the real image at the end, then overlays continuous energy effects (rotating ring pulse, shimmer sweep, sparkle bursts) clipped to avoid text regions.

## When to Use
- Hero sections where the client has a distinctive logo (circular badge, shield, seal, monogram) and the brand is premium / editorial / luxury.
- When the brand wants "flowing energy" or living feel without a video background.
- Works for any logo — the same component reads the source image and builds particles automatically. No per-logo code changes needed aside from tuning the ring radius and text exclusion bounds.

## How

**Component location:** `src/components/sections/LogoParticles.tsx`

**Props:**
```typescript
interface LogoParticlesProps {
  src?: string;           // logo image path, default /images/gray-method-logo.png
  className?: string;
}
```

**Phase timeline (total 1.95s assembly, then infinite idle):**
```
CONVERGE (0.70s) — particles rush from outside canvas → center, easeInCubic
HOLD     (0.25s) — dense bright cluster at center, sine-pulse radial bloom
EXPLODE  (1.00s) — burst outward to home positions, easeOutExpo
                 — particles fade out as real image fades in (crossfade)
IDLE     (∞)     — real image via drawImage + energy overlays
```

**Sampling the logo:**
```typescript
const sampleSize = 240;
const step = 3;
const off = document.createElement("canvas");
off.width = off.height = sampleSize;
const octx = off.getContext("2d", { willReadFrequently: true });
octx.drawImage(logoImg, 0, 0, sampleSize, sampleSize);
const data = octx.getImageData(0, 0, sampleSize, sampleSize).data;
// Iterate, filter a < 120 and brightness < 55, collect particles with r,g,b colors
```

**Idle state — draw the real image (not particles):**
```typescript
ctx.save();
ctx.globalAlpha = 1;
ctx.imageSmoothingEnabled = true;
ctx.imageSmoothingQuality = "high";
ctx.drawImage(logoImg, 0, 0, canvas.width, canvas.height);
ctx.restore();
```

**Energy overlays (idle only, clipped to exclude text band):**
```typescript
const bannerY0 = canvas.height * 0.34;
const bannerY1 = canvas.height * 0.80;
ctx.save();
ctx.beginPath();
ctx.rect(0, 0, canvas.width, canvas.height);
ctx.rect(0, bannerY0, canvas.width, bannerY1 - bannerY0);
ctx.clip("evenodd");

drawRingPulse(elapsed);    // rotating gold arc at radius 0.375 * W, shadowBlur glow
drawShimmerSweep(elapsed); // horizontal gradient band, ~6.5s cycle, lighter blend
ctx.restore();

drawSparkles(dt); // additive cross-shaped bursts at filtered bright pixels
```

## Key Rules
- **Never render idle state with particles if the logo has text.** Square particle grids cannot antialias text. Always crossfade to `drawImage()` before the user is expected to read anything. See [[errors/canvas-particle-grid-cannot-render-text]].
- **Clip all overlay effects to exclude the text band** — `evenodd` clip is the cleanest approach. Default exclusion for a circular badge logo: `y ∈ [0.34, 0.80]`. Tune per logo. See [[errors/canvas-effect-overlay-washes-out-text]].
- **Sparkle spawn positions must also be filtered** — don't rely on clipping alone. Check `yFrac` at build time and only push candidates outside the text band.
- **Ring pulse radius** is a tunable constant (default `0.375 * canvas.width`). Adjust to match where the gold ring sits in the source logo.
- **DPR cap at 2** — `Math.min(devicePixelRatio, 2)` prevents particle count from exploding on 3x retina displays without visible quality loss.
- **Honors `prefers-reduced-motion`** — skips the assembly phases, goes straight to idle with crisp logo + reduced/no effects.
- **Resize handling** — rebuild particles on window resize. `requestAnimationFrame`-wrapped debounce prevents build thrash.
- **Cleanup** — cancel `rafId` and remove listeners on unmount.

## Reuse Condition
Any hero for a client with a logo that has:
- A distinctive shape (circle, shield, seal — something with a recognizable silhouette)
- Contains text that needs to be readable in the final state
- Brand tone is premium / luxury / editorial (this pattern is too dramatic for casual brands)

The Gray Method implementation lives at `src/components/sections/LogoParticles.tsx`. Copy it verbatim, then tune:
1. Logo path (`src` prop default)
2. Ring radius (`drawRingPulse` — `canvas.width * 0.375`)
3. Text exclusion bounds (`bannerY0`, `bannerY1`)
4. Shimmer sweep speed (`elapsed % 6.5 / 6.5`)
5. Sparkle spawn interval (`0.14 + Math.random() * 0.24`)

## Related
- [[errors/canvas-particle-grid-cannot-render-text]]
- [[errors/canvas-effect-overlay-washes-out-text]]
- [[patterns/dual-hero-animation-canvas-orbs]] — the simpler canvas hero from the original Gray Method build (no logo sampling)
