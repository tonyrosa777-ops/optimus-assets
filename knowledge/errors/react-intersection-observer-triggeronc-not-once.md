# Error: react-intersection-observer Uses `triggerOnce` Not `once`

**Project:** Gray Method Training
**Date:** Mar 2026
**Phase:** Phase 2 — Animation Primitives

## Problem

All animation primitives were written using `useInView({ once: true })`. The `once` option does not exist in the `react-intersection-observer` library — it's silently ignored, meaning animations re-trigger every time the element scrolls in and out of view instead of firing once.

## Root Cause

The option name matches `IntersectionObserver` mental model and Framer Motion's own `once` prop, but `react-intersection-observer` uses a different prop name: `triggerOnce`. Easy to confuse across libraries.

## Solution

Replace every instance with `triggerOnce: true`:

```tsx
// Wrong
const { ref, inView } = useInView({ once: true, threshold: 0.2 });

// Correct
const { ref, inView } = useInView({ triggerOnce: true, threshold: 0.2 });
```

## Prevention

In the animation primitives template, always use `triggerOnce: true`. When writing a new animation component, confirm the prop name against the installed library version — don't assume it matches Framer Motion's API.

## Related

- [[patterns/responsive-canvas-animation-breakpoint-layout]] — animation library config
