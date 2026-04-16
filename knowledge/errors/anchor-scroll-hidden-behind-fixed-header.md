# Error: `#anchor` links scroll destination hidden behind fixed header
**Project:** Enchanted Madison
**Date:** 2026-04-15
**Phase:** Post-launch polish / client feedback

## Problem
Every `<Link href="#packages">` / `<a href="#section">` on the site would scroll correctly but the destination section's heading was rendered **behind the fixed site header**, so clicking "See Packages" looked like it had jumped into the middle of the next section. Visually indistinguishable from a broken anchor link.

## Root Cause
The site uses a fixed-position `SiteHeader` component (`h-20` mobile → `h-24` sm → `h-28` lg, so 80–112px tall). Native browser anchor scrolling places the target element at `y = 0` of the viewport — directly under the fixed header. No amount of `scroll-margin-top` on individual sections would fix this at scale (every section would need the rule).

## Solution
One global rule in `globals.css` fixes every `#anchor` link on the site:
```css
html {
  scroll-behavior: smooth;
  scroll-padding-top: 96px;                       /* mobile header 80 + 16 buffer */
}
@media (min-width: 640px) { html { scroll-padding-top: 112px; } }
@media (min-width: 1024px) { html { scroll-padding-top: 128px; } }
```

`scroll-padding-top` on `<html>` tells the browser to reserve that space at the top of the viewport whenever it scrolls to any `#id` target. Works for hash navigation via `<Link>`, native `<a href="#...">`, `window.location.hash = ...`, and `element.scrollIntoView()`.

## Prevention
Any project with a fixed header **must** declare `scroll-padding-top` on `<html>` during Phase 1 scaffold, with breakpoint values matching the header's height plus ~16px breathing room. This is invisible during dev because devs typically test by scrolling manually, not by clicking in-page anchor links.

Add to `website-build-template.md` globals.css scaffold. Add to pre-launch auditor checklist: "Click every in-page anchor CTA; verify target section heading is fully visible, not tucked under nav."

## Related
- Error: [[errors/hero-image-fill-intercepts-pointer-events]] (discovered in same commit — both bugs were blocking the same CTA user journey)
- Pattern: [[patterns/scroll-padding-top-for-fixed-header-anchors]]
