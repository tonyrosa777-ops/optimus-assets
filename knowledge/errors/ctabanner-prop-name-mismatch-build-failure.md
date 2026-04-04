# Error: CTABanner Prop Name Mismatch Causes Vercel Build Failure
**Project:** Danielle Thompson
**Date:** Apr 2026
**Phase:** Post-build page additions

## Problem
A new `/testimonials` page was added using `ctaLabel` and `ctaHref` props on `<CTABanner />`. The build passed locally (no type errors surfaced during dev) but failed on Vercel with a TypeScript error pointing to unrecognized props.

## Root Cause
The `CTABanner` component interface defines `buttonText` and `buttonHref` — not `ctaLabel`/`ctaHref`. The local dev server was lenient; Vercel runs `tsc --noEmit` at build time and catches the mismatch.

## Solution
Updated the testimonials page to use the correct prop names:
```tsx
// Wrong
<CTABanner ctaLabel="Book Now" ctaHref="/book" />

// Correct
<CTABanner buttonText="Book Now" buttonHref="/book" />
```

## Prevention
- Before adding any new page that uses shared components, read the component's TypeScript interface to get exact prop names
- Run `npx tsc --noEmit` locally before pushing if adding new component usages
- When a component wraps common UI elements, name props semantically (`buttonText`, not `label`, `cta`, or `ctaLabel`) and document in the component file

## Related
- [[patterns/constants-ts-single-source-of-truth]] — centralizing data reduces prop-passing errors
