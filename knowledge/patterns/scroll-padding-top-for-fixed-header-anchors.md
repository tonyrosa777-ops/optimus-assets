# Pattern: `scroll-padding-top` on `<html>` for fixed-header anchor safety
**Category:** Architecture / Navigation / CSS
**First used:** Enchanted Madison — 2026-04-15

## What
One global CSS declaration that guarantees every `#anchor` link on the site scrolls to its target with the target's heading fully visible below a fixed header — no per-section `scroll-margin-top` needed.

## When to Use
Every project that uses a `position: fixed` site header **and** any in-page anchor links. That's ~100% of Optimus builds (SiteHeader is fixed by convention, and almost every long page has at least one `#book`, `#pricing`, `#faq`, `#packages`, etc.).

## How
In `src/app/globals.css`:
```css
html {
  scroll-behavior: smooth;
  /* Reserve header-safe zone so #anchor links don't land behind the fixed nav.
     Values match SiteHeader h-20 / h-24 / h-28 + ~16px breathing room. */
  scroll-padding-top: 96px;
}
@media (min-width: 640px) { html { scroll-padding-top: 112px; } }
@media (min-width: 1024px) { html { scroll-padding-top: 128px; } }
```

Adjust the pixel values to match whatever header height the project actually uses. Rule of thumb: `header-height + 16px`.

## Key Rules
- Declared on `<html>`, not `<body>`. `<body>` only works in some browsers.
- Works for: `<Link href="#x">`, `<a href="#x">`, `location.hash = "#x"`, `element.scrollIntoView()`.
- Stacks with `scroll-behavior: smooth` for animated scroll.
- Per-section `scroll-margin-top` is a local override if one section needs a different offset (e.g., a banner above it).
- This is invisible in dev because devs manually scroll rather than clicking anchors. Catch it with the pre-launch anchor-click audit.

## Reuse Condition
Any site with a fixed-position header. Drop into `globals.css` during Phase 1 scaffold. Zero cost to add; expensive to retrofit after the client tries a CTA and calls it broken.

## Related
- [[errors/anchor-scroll-hidden-behind-fixed-header]]
- [[errors/hero-image-fill-intercepts-pointer-events]] (companion fix — both needed for a functioning hero-to-section CTA)
- Pattern #33: End-of-build multi-breakpoint browser audit (anchor click verification belongs in the checklist)
