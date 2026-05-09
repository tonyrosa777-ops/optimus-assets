# Error: Hero trust microcopy double-rendered stars + credentials

**Project:** Ead Financial
**Date:** 2026-05-08
**Phase:** Stage 1E pre-flight Playwright calibration

## Problem

Hero.tsx trust strip rendered `★★★★★ ★★★★★ Trusted by New England business owners · 30+ years of practice · CPA · CPA` — duplicate star prefix AND duplicate credentials suffix. Visible at both 1440x900 desktop and 390x844 mobile screenshots. Caught only by the Playwright pre-flight pass; would have shipped to Stage 1I (and possibly past Stage 1I if the auditor wasn't looking specifically at the trust strip).

## Root Cause

**Data layer AND component layer both renderered the same presentational decoration.** Two specific overlaps:

```ts
// site.ts (content-writer agent's output, Stage 1D)
trustMicrocopy: "★★★★★ Trusted by New England business owners · 30+ years of practice · CPA"
//               ^^^^^                                                                    ^^^
//               star prefix in DATA                                              credential suffix in DATA
```

```tsx
// Hero.tsx (animation-specialist's output, Stage 1D)
<span style={{ color: "var(--accent)" }}>{"★★★★★"}</span>{" "}
<span>{trustText}</span>
{siteConfig.credentials.length > 0 && (
  <>{" · "}<span>{siteConfig.credentials.join(" + ")}</span></>
)}
//   ^^^                                                ^^^^^^^^^^^^^^^^^^^^^^^^
//   star prefix in COMPONENT                           credential suffix in COMPONENT
```

Both layers had reasonable-looking implementations in isolation:
- The data is a string → makes sense to have the visual marks in the string for content-writer to control voice
- The component renders semantic elements → makes sense to have stars colored brass via CSS and credentials interpolated from `siteConfig.credentials` for OVERRIDE 6 configurability

The bug emerges only when both are seen side-by-side. Each agent's output passed its own validation. Each agent ran in parallel without cross-visibility. The contract gap between data and component was invisible until rendering.

## Solution

**Pick a single source of truth for each presentational mark, document the contract inline.** For Ead's hero trust strip, the component layer wins because:
- Stars use CSS color (`var(--accent)` brass), which JSX controls more cleanly than embedding decorative chars in strings
- Credentials are configurable per OVERRIDE 6 (`siteConfig.credentials: string[]` array, no hardcoded "CPA"/"EA" strings) — must be interpolated, can't live in a string

Fix:

```ts
// site.ts — strip the leading "★★★★★ " and trailing " · CPA"
// Hero.tsx renders the ★★★★★ prefix and the credentials suffix from siteConfig.credentials.
// This string holds the middle content only — no stars, no credentials, no leading/trailing dots.
trustMicrocopy: "Trusted by New England business owners · 30+ years of practice"
```

Hero.tsx unchanged (it remains the single source of truth for both the star prefix and the credentials suffix).

## Prevention

This is the canonical instance of a class that recurs whenever a component wraps a data string with presentational decoration. **Will absolutely hit the next build's pricing card (`$` prefix), testimonial attribution (em-dash separator), eyebrow label (`»` chevron), or any other component wrapping data.** See [[patterns/single-source-of-truth-for-presentational-decoration]] (Pattern #64) for the cross-build prevention rule and the audit grep that catches it.

Specific anti-patterns to grep for at Stage 1H pre-launch-auditor:
- `"★` in any string literal in `site.ts` — stars belong in the component
- `"$` followed by a number in any tier or stat string — dollar prefix belongs in the component
- `"— ` at the start of any testimonial attribution — em-dash separator belongs in the component
- `"· ` at the start of any string that gets interpolated into a list — dot separator belongs in the join

## Related

- [[patterns/single-source-of-truth-for-presentational-decoration]] (Pattern #64) — the cross-build prevention rule
- design-system.md §11 OVERRIDE 6 — credentials configurability driver
- Pattern #61 §12 Subsection 7 — pre-launch-auditor checklist this error class should join
