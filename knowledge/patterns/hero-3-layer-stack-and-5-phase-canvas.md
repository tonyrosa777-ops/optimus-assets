# Hero 3-Layer Stack and 5-Phase Canvas Lifecycle

**Referenced from:** CLAUDE.md Hero Architecture Rule
**Applied by:** animation-specialist agent
**Established:** 2026-04-17 (extracted from CLAUDE.md during Opus 4.7 retune)

## The 3-layer stack — always exactly 3 layers

**Layer 1 — HeroParticles.tsx (canvas particle system).**
Selected by animation-specialist from design-system.md Section 8 (Brand Personality Axes). Renders at z-0 (behind all content). Always present.

**Layer 2 — [BrandName]Canvas.tsx (brand canvas — custom `<canvas>`).**
Creative niche-specific canvas animation. NOT an SVG. NOT a generic shape. Named after the brand (e.g. `HealthShieldCanvas.tsx`, `ForgeCanvas.tsx`). Lives in the right panel of the two-column hero split. Follows the 5-phase lifecycle below.

**Layer 3 — Framer Motion stagger text.**
H1 first (tagline, with shimmer class), subheadline at 0.15s delay, CTAs at 0.3s delay. Renders at z-10. Always present.

## The 5-phase lifecycle (Layer 2 brand canvas)

Every brand canvas follows this sequence. The implementation is nearly identical across brands — what changes per build is the shape drawn in RISE, the heat palette endpoint, and the secondary element in ARC.

### Phase 1 — STREAM
N particles spawn at canvas edges and flow along quadratic bezier curves toward a center target. Each frame: `t += speed`. When all particles reach `t >= 0.94`, fire phase 2.

```
for each particle p:
  p.t += p.speed
  draw p at bezier(p.start, p.control, p.target, p.t)
if allAtOrPast(particles, 0.94): startPhase(RISE)
```

### Phase 2 — RISE
Particles cleared. Brand shape extrudes using `springOut(t)` for physical spring overshoot. Duration: ~500ms.

```
springOut(t) = 1 - 2^(-9t) * cos(t * 10π * 0.68)
```

### Phase 3 — COOL
Shape color animates through a heat palette: white-hot → brand accent → brand primary. The shape literally "becomes" the brand as it cools.

```
heatRGB(t) interpolates between:
  t=0.0 → white (#ffffff)
  t=0.5 → brand accent
  t=1.0 → brand primary
```

### Phase 4 — ARC
Secondary element draws progressively — examples: rail across fence pickets (Placed-Right-Fence), arc around shield (HealthShield). Drawn via `ctx.arc(x, y, r, start, end * progress)`.

### Phase 5 — IDLE
Ambient pulse. `breathe = sin(elapsed * 0.00088)` oscillates cooling-T and arc alpha — ~12-second breath cycle.

## What changes per brand

- **Shape drawn in RISE.** `drawPicket`, `drawCross`, `drawFlame`, `drawShield`, `drawCoatOfArms` — one function per brand that stamps the brand's visual identity.
- **Heat palette endpoint in COOL.** Always cools to the brand's primary color — that's the "this is our brand" reveal moment.
- **Secondary element in ARC.** Brand-specific (rail, arc, orbit, crest assembly).

What does NOT change: the 5-phase sequence, `springOut` function, `heatRGB` interpolation, requestAnimationFrame structure.

## Container + canvas setup

```tsx
<div style={{ position: "relative", height: "clamp(340px, 50vw, 540px)" }}>
  <canvas
    ref={canvasRef}
    style={{ position: "absolute", inset: 0, width: "100%", height: "100%" }}
  />
</div>
```

Always cast the 2D context:
```ts
const ctx = canvas.getContext("2d") as CanvasRenderingContext2D
```
Never leave it nullable — nested draw functions will fail TypeScript strict mode.

## requestAnimationFrame cleanup (non-negotiable)

Missing rAF cleanup = memory leak on page navigation. Always:

```tsx
useEffect(() => {
  let rafId: number
  const loop = () => {
    draw()
    rafId = requestAnimationFrame(loop)
  }
  loop()
  return () => cancelAnimationFrame(rafId)
}, [])
```

## Reference implementations (real repos)

- `tonyrosa777-ops/Sylvia-Rich-Hungary-Consul-NE` — gold dust particles, coat of arms
- `tonyrosa777-ops/where-2-junk` — junk/debris particle system
- `tonyrosa777-ops/Placed-Right-Fence` — forge ember extrusion

File paths cited here are real. If reading one of these repos and the path does not exist, report it — do not invent file contents.

## Selection process (from CLAUDE.md — repeated here for canvas-specific context)

1. Read design-system.md Section 8 (Brand Personality Axes) + business type.
2. Brainstorm 10 conceptually distinct visual metaphors tied to the niche. (10 particle-color variations is ONE concept, not 10 — see animation-specialist.md for the distinctness test.)
3. Spawn a critic agent, score on niche relevance / visual impact / technical feasibility / uniqueness.
4. Build ONLY the winner. If it produces blocking errors within 2 fix commits, HALT with `[FALLBACK-REQUIRED: <reason>]`. Do not autonomously switch to LogoParticles.
5. Fallback: Pattern #36 LogoParticles chaos→convergence→explosion from JCM Graphics. Requires client logo PNG with transparent background.

## Related patterns
- `knowledge/patterns/logo-particles-phased-reveal.md` — the LogoParticles fallback (Pattern #36)
- `knowledge/patterns/responsive-canvas-animation-breakpoint-layout.md` — mobile handling
- `knowledge/patterns/hero-server-client-animation-split.md` — server/client component split

## Status
ACTIVE. Extracted from CLAUDE.md on 2026-04-17 during Opus 4.7 retune to reduce session-prefix size.
