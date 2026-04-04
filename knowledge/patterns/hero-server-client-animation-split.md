# Pattern: Hero Server/Client Animation Split
**Category:** Architecture / Animation / Performance
**First used:** Cody's Complete Junk Removal — Apr 2026

## What
Split the hero section into two components: a server-rendered main component (text, CTAs, layout) and a client-only `HeroEffects` component (all decorative animations). This keeps `"use client"` scope tight while keeping the primary content SSR'd.

## When to Use
- Hero section has heavy decorative animations (particles, lightning bolts, pulse rings, scan lines)
- You want hero content to be SSR'd for performance and SEO (H1, CTAs, phone number)
- Animations are purely decorative and don't depend on props or state from the parent

## How

**HeroSection.tsx** (server component — no `"use client"`):
```tsx
import HeroEffects from './HeroEffects';

export default function HeroSection() {
  return (
    <section className="relative min-h-screen ...">
      <HeroEffects />  {/* client boundary here */}
      <div className="relative z-10 ...">
        {/* All real content — SSR'd */}
        <h1>...</h1>
        <a href="/contact">Get Free Quote</a>
      </div>
    </section>
  );
}
```

**HeroEffects.tsx** (client component — all animation):
```tsx
'use client';
// SVG lightning bolts, CSS-animated particles, pulse rings
// All positioned absolute, pointer-events-none, aria-hidden
export default function HeroEffects() {
  return (
    <div className="absolute inset-0 overflow-hidden pointer-events-none" aria-hidden="true">
      {/* decorative elements only */}
    </div>
  );
}
```

## Key Rules
- `HeroEffects` must be `pointer-events-none` so it never blocks clicks on CTAs
- Always `aria-hidden="true"` on the effects wrapper — decorative elements shouldn't be read by screen readers
- Keep `z-index` hierarchy explicit: effects layer behind content (`z-0`), content above (`z-10`)
- CSS keyframe animations (not Framer Motion) for the decorative layer — no JS overhead for visual-only effects
- Use `filter: drop-shadow()` for SVG bolt glow — cheaper than box-shadow on SVG

## Reuse Condition
Any hero section with animated background effects. Standard pattern for premium/luxury local service sites.

## Related
- [[errors/turbopack-use-client-not-first-token]]
- [[errors/framer-motion-v12-ease-type]]
