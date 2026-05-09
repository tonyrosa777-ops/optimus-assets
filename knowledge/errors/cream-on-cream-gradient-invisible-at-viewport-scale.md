# Error: Cream-on-cream ambient gradient perceptually invisible at 1440 viewport scale

**Project:** Ead Financial
**Date:** 2026-05-08
**Phase:** Stage 1D + Stage 1E pre-flight Playwright calibration

## Problem

Hero.tsx v2 (single-column text-only composition, post-photo-removal correction) shipped with an ambient cream-on-cream radial gradient as the only non-text visual interest above the fold. The intent: subtle warm halo behind the text that registers as "considered editorial composition" rather than "flat empty page."

Initial implementation:
```css
background: radial-gradient(
  ellipse 70% 55% at 32% 38%,
  var(--bg-elevated) 0%,
  color-mix(in oklab, var(--bg-elevated) 65%, var(--bg-base)) 35%,
  var(--bg-base) 70%
);
```

Where `--bg-elevated` = `#EEE6DA` and `--bg-base` = `#F5EFE6`. **The two values differ by ~7–9 RGB points.** At 1440×900 viewport scale, the perceptual contrast between blob center and the surrounding cream was effectively zero — the gradient was invisible.

Hero read as "left-aligned text on flat empty page" when verified at Playwright 1440×900. Failed the user's stated test: *"If your eye scans, the gradient isn't carrying enough weight."*

## Root Cause

Two compounding factors:

1. **`--bg-elevated` was specced for "alternating section background" use** (per design-system.md §2: *"Use when two consecutive sections both need to be 'light' but visually distinct"*). At that use case, `--bg-elevated` sits adjacent to `--bg-base` on a section boundary — the eye sees both side-by-side and the 7-RGB-point delta registers. As a **gradient blob** centered inside a single section, the same delta has no edge contrast — the eye reads "uniform cream."

2. **The cream-tinted color stops did not include the brand accent.** The blob center (`--bg-elevated`) and falloff (color-mix of two creams) all sat in the cream region of color space. Without any accent injection, there was no warmth, no character, no "intentional design decision" reading.

Sub-cause: the assumption that "cream-on-cream is editorial" is true at section boundaries (where the eye anchors to the boundary line) but FALSE inside a single section (where there's no boundary to anchor on).

## Solution

Replace the cream-on-cream gradient with a **brass-tinted cream** at the blob center. Specifically, mix ~7% of `--accent` (`#B07D2A` muted brass) into `--bg-base` for the blob center, falling off through a 4% mix to base cream:

```css
background: radial-gradient(
  ellipse 85% 70% at 50% 42%,
  color-mix(in oklab, var(--accent) 7%, var(--bg-base)) 0%,
  color-mix(in oklab, var(--accent) 4%, var(--bg-base)) 35%,
  var(--bg-base) 78%
);
```

Plus three secondary calibrations:
- **Blob size 70% 55% → 85% 70%** — bigger blob fills more of the centered hero composition
- **Position 32% 38% → 50% 42%** — center the blob behind the (now centered via `mx-auto`) text column
- **Falloff stop 70% → 78%** — softer edge transition to base cream

7% accent mix is calibrated: subtle enough to read as "warm cream" not "yellow stain," visible enough to register as intentional. 12%+ starts reading as a peach blob; 4% is below perception. 6–8% is the editorial-register sweet spot.

## Prevention

Two rules:

1. **Cream-on-cream gradients require accent injection at the blob center.** If the design system has cream-dominant tokens (`--bg-base` + `--bg-elevated` + `--bg-card`), do NOT use them as gradient blob centers — they're specced for section-boundary alternation, not in-section ambient depth. Inject ~6–8% of the brand accent via `color-mix(in oklab, var(--accent) 7%, var(--bg-base))` for the warm-halo blob center.

2. **Verify ambient gradients at Playwright before content lands on top.** Cream-on-cream invisibility is a class of bug that doesn't show up in dev (designer's monitor calibration may exaggerate the contrast) and won't be caught by typecheck or build. Run a 1440×900 screenshot of the hero alone before any other content hides the failure mode. The user's [[patterns/asymmetric-cost-pre-flight-calibration]] argument applies: 15 min now vs. 3 hours of rework once Stage 1E adds surrounding sections that mask the regression.

See also [[patterns/cream-on-cream-ambient-gradient-with-brass-mix]] for the calibrated recipe.

## Related

- [[patterns/cream-on-cream-ambient-gradient-with-brass-mix]] — the corrected recipe pattern
- [[patterns/light-mode-dominant-cream-theme]] — when this whole class of gradient applies
- [[patterns/luxury-gradient-backgrounds]] (Pattern #51) — the broader gradient-backgrounds rule
