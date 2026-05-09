# Pattern: Cream-on-cream ambient gradient hero backdrop with brass-tinted center

**Category:** Visual Design / Animation / Motion
**First used:** Ead Financial — 2026-05-08

## What

A single CSS-only radial-gradient layer behind the hero text, sized to fill most of the hero section, with a **brass-tinted cream** at the blob center (~7% accent mixed into base cream via `color-mix(in oklab, ...)`) falling off through 4% mix to base cream. Replaces both particle-system canvas heroes (rejected per design-system.md §10 anti-pattern #7 for editorial-register builds) and the failed naive cream-on-cream gradient using `--bg-elevated` as the blob center (which is perceptually invisible at viewport scale — see Error #56).

## When to Use

This recipe applies on hero sections of builds using [[patterns/light-mode-dominant-cream-theme]] (LIGHT-MODE-DOMINANT cream theme) where:
- The hero is single-column text-only (no photo, no canvas)
- The Energy axis is pinned ~20% from quiet pole (Section 8 axis 1) — too quiet for particles, too modern for static flat
- The marquee ribbon (or equivalent) sits below the hero as the cream→ink contrast beat
- The composition needs ambient depth without competing with the editorial italic-emphasis-in-brass H1 device

## How

```tsx
const HERO_BACKDROP_KEYFRAMES = `
@keyframes ead-hero-backdrop-drift {
  0%   { transform: translate3d(0, 0, 0) scale(1);    opacity: 0.85; }
  50%  { transform: translate3d(2.5%, -1.5%, 0) scale(1.04); opacity: 1; }
  100% { transform: translate3d(0, 0, 0) scale(1);    opacity: 0.85; }
}
.brand-hero-backdrop {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background:
    radial-gradient(
      ellipse 85% 70% at 50% 42%,
      color-mix(in oklab, var(--accent) 7%, var(--bg-base)) 0%,
      color-mix(in oklab, var(--accent) 4%, var(--bg-base)) 35%,
      var(--bg-base) 78%
    );
  will-change: transform, opacity;
  animation: brand-hero-backdrop-drift 20s ease-in-out infinite;
}
@media (prefers-reduced-motion: reduce) {
  .brand-hero-backdrop {
    animation: none !important;
    transform: none !important;
    opacity: 1 !important;
  }
}
`;

export function Hero() {
  return (
    <section className="relative flex items-start overflow-hidden pt-24 md:pt-40 pb-20 md:pb-28"
             style={{ backgroundColor: "var(--bg-base)", minHeight: "100svh" }}>
      <style dangerouslySetInnerHTML={{ __html: HERO_BACKDROP_KEYFRAMES }} />
      <div className="brand-hero-backdrop" aria-hidden="true" />
      <div className="relative z-10 mx-auto w-full max-w-[1200px] px-6 md:px-10 lg:px-16">
        {/* Centered single-column text composition with mx-auto on the inner column */}
        <div className="mx-auto max-w-[44rem]">
          {/* eyebrow + H1 (with .hero-shimmer + EmphasizedText) + subhead + 2 CTAs + trust strip */}
        </div>
      </div>
    </section>
  );
}
```

## Key Rules

- **`color-mix(in oklab, var(--accent) 7%, var(--bg-base))` at blob center.** 7% is the calibrated value. 6–8% is the editorial-register sweet spot. Below 5% is below perception (fails the "is this gradient actually visible?" test). Above 12% reads as "yellow stain" and kills the editorial register.
- **Use `oklab` color-mix, not `srgb` or default.** `oklab` mixes perceptually for warm-cream blends; `srgb` produces muddy mid-stops on cream/brass mixes.
- **Ellipse 85% 70% centered at 50% 42%** — sized to fill most of the hero composition, slightly above center to create visual gravity behind the H1 (which sits in upper-third due to `items-start` mobile-fix). Smaller ellipses (e.g., 70% 55%) feel like a localized blob; this size feels like ambient depth.
- **Single layer ONLY** per Section 12 cognitive resource preservation rule (Sweller Cognitive Load Theory 1988). Do not stack multiple radial gradients. Do not add a particle layer on top. The shimmer keyframe sweep on the H1 word is the second active motion layer in the hero — that's the budget ceiling.
- **GPU-cheap properties only** per CLAUDE.md Performance budget — `transform: translate3d()` + `opacity` on a 20s cycle. NEVER `filter`, `backdrop-filter`, `blur` on the animated layer.
- **`prefers-reduced-motion: reduce` → static gradient (NEVER flat).** The animation stops; the gradient stays. CLAUDE.md anti-pattern #14 prohibits flat solid section backgrounds even on text-heavy exception sections.
- **Inner column centering is required.** This recipe assumes `mx-auto` on the inner text column (centering it inside the outer `max-w-[1200px]`) — without that, the column hugs the left edge, the right side reads as empty rail, and the gradient halo (which is centered at 50%) sits behind empty whitespace instead of behind the text. This is what made the original v2 hero read sparse before calibration (Error #56).

## Reuse Condition

This recipe applies on every cream-dominant build using [[patterns/light-mode-dominant-cream-theme]]. The brass mix percentage and blob position may need tuning per project (depending on accent hue saturation and hero copy density), but the structure — single radial-gradient layer, `color-mix(in oklab, var(--accent) ~7%, var(--bg-base))` at center, slow `transform`+`opacity` drift, prefers-reduced-motion static fallback — is portable.

## Related

- [[patterns/light-mode-dominant-cream-theme]] — the broader theme this recipe supports
- [[patterns/luxury-gradient-backgrounds]] (Pattern #51) — the cross-build gradient-backgrounds rule
- [[errors/cream-on-cream-gradient-invisible-at-viewport-scale]] — the failed naive recipe (using `--bg-elevated` as blob center) that produced this pattern
- [[patterns/asymmetric-cost-pre-flight-calibration]] — the workflow rule that catches calibration errors before they ship
