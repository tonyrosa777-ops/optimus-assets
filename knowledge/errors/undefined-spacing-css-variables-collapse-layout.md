# Error: Undefined Spacing CSS Variables Collapse All Layout Gaps to 0
**Project:** JCM Graphics
**Date:** 2026-04-12
**Phase:** Post-build QA (discovered during client review)

## Problem
Every page on the site had compressed/missing spacing between cards, grid items, form sections, and pagination. Contact page form and info section had zero gap. Service cards were jammed together. Testimonial grid had no padding. About page belief cards stacked with no space.

## Root Cause
The component-level spacing scale (`--space-xs`, `--space-sm`, `--space-md`, `--space-lg`, `--space-xl`, `--space-2xl`) was referenced in 6+ files across the site (contact, services, services/[slug], testimonials, about, ContactForm) but never declared in `globals.css` `:root`. CSS custom properties without a declaration resolve to their initial value (nothing), which for gap/padding/margin means 0px.

The section-level variables (`--section-padding-y`, `--section-padding-x`) WERE defined, so section-to-section spacing looked fine — only internal component spacing collapsed.

## Solution
Add the complete spacing scale to `:root` in `globals.css`:
```css
--space-xs: 0.5rem;
--space-sm: 0.75rem;
--space-md: 1rem;
--space-lg: 1.5rem;
--space-xl: 2rem;
--space-2xl: 3rem;
--space-3xl: 4rem;
```

One 7-line addition fixed spacing across every page simultaneously.

## Prevention
- **Phase 1 scaffold checklist:** after creating globals.css, grep the entire `src/` directory for `var(--space-` references and verify every referenced variable has a declaration
- **Build-time check:** CSS variables used but never declared produce no error in any tool (not TypeScript, not PostCSS, not Tailwind, not the browser console) — the only way to catch this is visual inspection or a custom lint rule
- **Template update:** add the spacing scale to `website-build-template.md` as a required globals.css section alongside the type scale

## Related
- Pattern #34: Clamp-based responsive type scale — same category of "design token declared once, used everywhere"
- The section-level spacing (`--section-padding-y`) was correctly defined, which masked the problem — page-level padding looked fine while component-level spacing was broken
