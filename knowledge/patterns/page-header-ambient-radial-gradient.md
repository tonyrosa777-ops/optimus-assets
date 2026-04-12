# Pattern: Page-Header Ambient Radial Gradient
**Category:** Visual Design / Animation
**First used:** JCM Graphics — 2026-04-12

## What
A subtle brand-colored radial gradient behind all interior page headers, replacing per-page custom effects (breathing orbs, particle canvases) with a single consistent CSS-only approach.

## When to Use
- Dark-brand builds where interior pages need ambient visual energy without the weight of canvas animations
- When the Page Animation Rule requires every page header to feel non-static
- As the default interior page effect — upgrade to canvas particles only if the page warrants it

## How
Add a `::before` pseudo-element or background layer to the page header section:
```css
.page-header {
  position: relative;
  overflow: hidden;
}
.page-header::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 50% 0%, rgba(brand-primary, 0.15) 0%, transparent 70%);
  pointer-events: none;
}
```
- Use the brand primary color at 10-20% opacity
- Center the gradient at top-center (ellipse at 50% 0%)
- Fade to transparent at ~70% radius
- Apply to ALL interior page headers via a shared component or utility class

## Key Rules
- CSS-only — no JavaScript, no canvas, no runtime cost
- Never compete with the homepage hero's full 3-layer stack — this is deliberately subtle
- Opacity stays under 20% — it's ambient atmosphere, not a spotlight
- Works on dark backgrounds only — on light pages, use a darker shade or skip

## Reuse Condition
Any dark-brand build. Replaces the need to build custom breathing orbs or particle canvases for every interior page header. One shared class, applied everywhere.

## Related
- CLAUDE.md Page Animation Rule (requires non-static headers on every page)
- Replaced breathing orbs on JCM gallery page — simpler, more consistent
