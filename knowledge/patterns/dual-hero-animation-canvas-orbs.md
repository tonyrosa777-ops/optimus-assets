# Pattern: Dual Hero Animation System — Canvas Particles + CSS Breathing Orbs

**Category:** Animation / Visual Design
**First used:** Gray Method Training — Mar 2026

## What

Two independent animation layers stack in the hero to create a luxury, high-motion opening without video. Layer 1 is a canvas-based particle system (stars, embers, glimmers). Layer 2 is CSS `@keyframes` breathing orbs (radial gradient blobs). Together they produce depth, motion, and warmth using only brand colors.

## When to Use

Any premium dark-background brand where:
- No hero video is available or desired
- The brand color palette includes warm tones (gold, amber, orange)
- The hero needs to feel alive at page load with zero user interaction

## How

**Layer 1 — Canvas Particles (`HeroParticles.tsx`)**

Separate client component, mounted as a sibling behind the hero copy. Uses `requestAnimationFrame` loop:

```tsx
// Three particle types
type Star = { x, y, vx, vy, opacity, targetOpacity, size, color }
type Ember = { x, y, vy, opacity, size, color }  // rises upward, fades out
type Glimmer = { x, y, life, maxLife, size }      // 4-point burst, brief

// Counts (tune to taste)
const STAR_COUNT = 85;
const EMBER_COUNT = 32;

// Each frame: update position, twinkle opacity, draw
// Canvas fills hero container, ResizeObserver keeps it matched
// Guard: if (prefersReducedMotion) return null
```

**Layer 2 — CSS Breathing Orbs (globals.css)**

Three absolutely-positioned divs with radial gradients + `@keyframes`:

```css
@keyframes orb-breathe {
  0%, 100% { transform: scale(1); opacity: 0.15; }
  50% { transform: scale(1.2); opacity: 0.28; }
}
@keyframes orb-breathe-slow {
  0%, 100% { transform: scale(1); opacity: 0.1; }
  50% { transform: scale(1.3); opacity: 0.2; }
}
```

```tsx
// In Hero.tsx — three orbs, different positions, sizes, phases
<div className="orb-1" />  {/* Bottom-left, primary, 6s */}
<div className="orb-2" />  {/* Top-right, muted, 9s, -3s delay */}
<div className="orb-3" />  {/* Center-top, accent, 8s, -5s delay */}
```

**Text shimmer on headline (CSS utility)**

```css
@keyframes shimmer-sweep {
  0% { background-position: -200% center; }
  100% { background-position: 200% center; }
}
@utility text-shimmer {
  background: linear-gradient(90deg, var(--primary) 20%, white 50%, var(--primary) 80%);
  background-size: 200%;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: shimmer-sweep 5s linear infinite;
}
```

## Key Rules

- Canvas z-index must be below the hero copy container (`z-0` canvas, `z-10` copy)
- Canvas uses `mix-blend-mode: screen` for the stars to glow through the dark bg correctly
- Both layers must respect `prefers-reduced-motion` — if true, skip canvas entirely and use static orbs with no animation
- Orb divs get `pointer-events: none` — they must not block clicks on CTAs

## Reuse Condition

Any dark-theme hero for a premium personal brand. Swap colors to brand palette — the architecture stays the same. The particle count and speed can be tuned to feel lighter (lifestyle, wellness) or heavier (energy, performance).

## Related

- [[patterns/hero-concept-iteration-budget]]
- [[patterns/hero-server-client-animation-split]] — alternative approach for sites where SSR matters more than animation richness
