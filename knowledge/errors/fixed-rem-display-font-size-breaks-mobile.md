# Error: Fixed-rem display font size breaks mobile wrapping
**Project:** Gray Method Training
**Date:** 2026-04-10
**Phase:** Post-launch conversion rework (Session 4)

## Problem

New hero H1 "Stronger. / More energized. / Finally free from the diet cycle." rendered perfectly on desktop but split awkwardly on mobile at 390px:

```
Stronger.
More
energized.          ← "More" alone on its own line
Finally free
from the
diet cycle.
```

`More` orphaned on its own line broke the rhythm of the three-phrase mission statement and reduced the emotional punch of the climax line. Same class of bug previously hit Gray Method in commit `3bc3fe7 Fix word-break on mobile in RevealText headline` — so this was the **second time** the same category of issue hit this project.

## Root Cause

`--text-display` was declared as a fixed value in `globals.css`:

```css
--text-display: 4.5rem;   /* 72px everywhere, no scaling */

@utility text-display {
  font-size: 4.5rem;
  line-height: 1.05;
  letter-spacing: -0.02em;
}
```

72px Cormorant Display at 390px viewport width (342px available after `px-6` padding) cannot fit "More energized." — approximately 15 chars × ~22px average char width = ~330px, right at the edge of the available space. The browser wraps at the first space it can find. TypeScript compiled cleanly, desktop looked fine, no one noticed until the multi-breakpoint visual audit caught it.

## Solution

Swap the fixed value for a `clamp()` expression in both the custom property and the matching `@utility`:

```css
--text-display: clamp(2.5rem, 8vw, 4.5rem);

@utility text-display {
  font-size: clamp(2.5rem, 8vw, 4.5rem);
  line-height: 1.05;
  letter-spacing: -0.02em;
}
```

- **Min 2.5rem (40px):** "More energized." is ~15 chars × ~20px = ~300px, comfortable fit in 342px
- **Preferred 8vw:** scales smoothly with viewport width
- **Max 4.5rem (72px):** hits the ceiling around ~900px viewport, so desktop rendering is identical to before

One change in `globals.css` fixed the H1 and also improved type scale for 11 other components (`about`, `contact`, `quiz`, `reviews`, `programs/*`, `FinalCTA`, `GrayMethodPhilosophy`) that use the same utility — all of them were technically oversized on mobile, nobody had noticed yet.

## Prevention

**Rule added to toolkit:** Display font sizes (anything > 2rem / 32px) must use `clamp(min, vw-based preferred, max)` in the CSS variable definition AND the matching `@utility` class. Fixed-rem display sizes are a mobile bug waiting to happen.

**Audit trigger:** The end-of-build multi-breakpoint live-browser audit ([[patterns/end-of-build-multi-breakpoint-browser-audit]]) is what caught this. Without that step, it would have shipped to production.

## Related

- [[patterns/clamp-responsive-type-scale]] — the pattern this error produced
- [[patterns/end-of-build-multi-breakpoint-browser-audit]] — the workflow that caught the bug
- Error #25 (Mobile hero text starts mid-screen) — same project class but different root cause (layout vs type scale)
- Previous Gray Method precedent: commit `3bc3fe7 Fix word-break on mobile in RevealText headline`
