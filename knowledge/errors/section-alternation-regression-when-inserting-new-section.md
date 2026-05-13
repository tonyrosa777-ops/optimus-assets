# Error: Section alternation regression — inserting a new section between two same-bg sections created 3 cream-in-a-row

**Project:** Enchanted Madison
**Date:** 2026-05-13
**Phase:** Client revisions pass (Stage 1I verification)

## Problem
Homepage section flow after a revision-pass addition:

  Hero (`bg-dark`) → Trust strip (`bg-elevated` cream) → **NEW tagline section** (`bg-elevated` cream) → Stays grid (`bg-base` cream) → Experiences (`bg-elevated` cream)

Four cream sections in a row. Page read as a flat cream wall after the hero, with no rhythm or breathing room. User flagged immediately during browser audit:

> *"we have an error with three cream sections in a row. That's not right."*

## Root Cause
When Angela's revisions doc called for a new "Tagline + Distance Info Box" section, the dev (me) inserted it between the existing Trust strip and the Stays grid using `var(--bg-elevated)` (cream) — matching the surrounding sections by default. Each individual decision was reasonable (a cream tagline section sandwiched between cream trust + cream stays *seemed* visually consistent), but the cumulative result broke the alternation rule.

This is **already a documented pattern**: Pattern #8 (Placed Right Fence, Apr 2026):
> *"Homepage dark/light section rhythm — plan alternation before building any section; 3 consecutive same-background sections always need a flip."*

And the May 2026 luxury-gradient workflow rule (2026-04-17):
> *"No flat solid backgrounds ever, on any page, any tone. Every section = gradient + subtle motion by default."*

The bug is not a *new* class — it's a regression case for an *existing* documented rule. The rule wasn't auto-checked when inserting a new section into an existing layout.

## Solution
Make the inserted section dark to break the chain. Use `var(--bg-dark)` + Fireflies + GodRays + WaveDivider down to the next cream section:

```tsx
<section
  className="relative py-14 lg:py-20 px-4 overflow-hidden"
  style={{ background: "var(--bg-dark)" }}
>
  <Fireflies count={14} />
  <GodRays opacity={0.35} />
  <div className="relative z-10">
    {/* tagline copy with rgba(254,252,250,0.78) text */}
    {/* distance pills with rgba(254,252,250,0.06) bg + backdrop-blur */}
  </div>
</section>
<WaveDivider fill="var(--bg-base)" background="var(--bg-dark)" />
```

Result flow: `dark / cream / DARK / cream / cream` — only 2-in-a-row before Experience Finder breaks it again. Rhythm restored.

## Prevention
Pattern #8 already exists. What was missing was the **auto-check** when a section is inserted. Three preventive measures:

1. **Pre-launch auditor check** (add to Stage 1I): walk the homepage section flow programmatically, classify each by background color family (`bg-dark`, `bg-base | bg-elevated | bg-card` = cream cluster). Any run of ≥3 same-family consecutive sections is a fail. Implementation:
   ```js
   const sections = Array.from(document.querySelectorAll('main > section, main > div'));
   const tones = sections.map(s => {
     const bg = window.getComputedStyle(s).backgroundColor;
     return /rgb\(2[0-9],/.test(bg) ? 'dark' : 'light'; // 1A2A1E → dark
   });
   // walk: any 'light,light,light' sequence?
   ```

2. **Revisions-pass checklist** (any time a new section is inserted into an existing layout): force the dev to log the new section's background tone AND the tone of its two neighbors. If all three match, escalate to alternation review.

3. **`siteData.homepageSections` manifest** (future enhancement): declare each section's `tone` in data, render the manifest, and let the type system check alternation. Too heavy for this size of project; mention as an option for future builds with > 8 sections.

4. **First-principles rule for revision passes**: when content-only revisions land, **also** audit visual rhythm. Don't treat copy edits as visual-neutral. Adding a paragraph block is visually equivalent to adding a section.

## Related
- Pattern #8 (Placed Right Fence, Apr 2026): Homepage dark/light section rhythm — alternation rule
- Pattern #51 (Optimus cross-project, 2026-04-17): Luxury gradient backgrounds — no flat solid backgrounds
- Pattern #67 (Ead Financial, May 2026): Dark-section ink-on-ink gradient recipe — the recipe used here for the new dark tagline section
- Workflow improvement (2026-04-17): Luxury gradient backgrounds rule codified — CLAUDE.md Visual QA Rule exit criteria
