# Pattern: Chaos → Convergence → Explosion Logo Reveal
**Category:** Animation / Architecture
**First used:** JCM Graphics — 2026-04-12

## What
A canvas logo animation where all particles start scattered, slam to a center energy ball, hold compressed with white-hot glow, then explode outward to their final logo pixel positions with spring overshoot and a shockwave flash.

## When to Use
When the brand canvas needs a dramatic reveal animation that looks intentional at every frame. Replaces the per-region/per-letter approach (which looks broken mid-assembly for script fonts) and the direct-convergence approach (which has less visual drama).

## How
1. **Sample logo** — offscreen canvas, 280px at step=2, extract RGB for every opaque pixel above brightness threshold
2. **Scatter positions** — random angle + random distance (0.3–1.0× canvas width) from center
3. **Drift velocities** — small random vx/vy for the scatter phase (visual chaos)
4. **Phase machine** — single elapsed timer drives 7 phases:
   - SCATTER (0–0.5s): particles visible at scatter positions, drifting
   - CONVERGE (0.5–1.3s): `easeInCubic(t)` interpolation from drift-end → center; brightness increases with compression; center glow intensifies; impact sparks at 85%
   - HOLD (1.3–1.9s): all particles at center with diminishing jitter; white-hot pulse via `sin(t * 3π)`; intense radial glow
   - EXPLODE (1.9–2.7s): `springOut(t)` from center → home positions; brightness flash on overshoot; full-screen white flash at start
   - SHOCKWAVE (2.5–3.2s): 160 sparks (80 white-hot + 50 brand blue + 30 cream accent); double expanding rings; full-screen flash at 55% opacity
   - CROSSFADE (2.6–3.2s): `drawImage()` with increasing alpha
   - IDLE (3.2s+): ring pulse + shimmer sweep + sparkles (same as Pattern #31)

## Key Rules
- **springOut** function: `1 - 2^(-9t) * cos(t * 10π * 0.68)` — gives physical spring overshoot
- **easeInCubic** for convergence: slow start → violent slam at end (NOT easeOut, which would decelerate)
- **Hold phase jitter** must DECREASE over time (particles settling) — `(1 - t * 0.3) * 4 * dpr`
- **Center point** at (0.5, 0.45) not dead center — logo visual weight is usually upper-half
- **Shockwave spawns 3 spark layers** with different speeds and lifetimes for depth
- **Crossfade overlaps shockwave** — logo image fades in while rings are still expanding
- Per-letter/per-region reveals do NOT work for script/overlapping fonts — the mid-state is unrecognizable partial letterforms. Single convergence always looks intentional.

## Reuse Condition
Any project with a raster logo that needs a canvas-based reveal animation. Especially effective for logos with script/cursive fonts where individual letter isolation is impractical. Works for any brand color palette — just change the glow/spark colors.

## Related
- Pattern #31 (LogoParticles phased reveal) — predecessor pattern; this replaces the assembly phase approach with chaos→convergence→explosion
- Pattern #28 (Brand Canvas 5-phase) — the geometric shape approach; this pattern is for raster logo images, not drawn shapes
- Error #35 (canvas particle grid cannot render text) — why crossfade to `drawImage()` is required for idle state
