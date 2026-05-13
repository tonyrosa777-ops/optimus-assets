# Error: Orphan-cell grid layouts — incomplete final row breaks luxury-modern positioning

**Project:** Enchanted Madison
**Date:** 2026-05-13
**Phase:** Client revisions verification pass (Stage 1I)

## Problem
On the `/vip` page, the perks section rendered as 2 cards in a row followed by 1 card alone in a half-empty second row (`sm:grid-cols-2` × 3 items = 2+1 orphan). Anthony caught it immediately and named the class-of-bug:

> *"a grid must have 4. we cant have incomplete griids. we need to find a more aesthetic approach for 3 items. We need to assume our viewer has OCD and make sure things look right."*

Same root cause surfaced on `/stays` (5 stays in `lg:grid-cols-3` = 3+2 orphan in the second row). Both were rendering with one or two cards floating alone next to empty grid cells — visually identical to a section that's missing content.

## Root Cause
A CSS grid with a fixed column count fills row-major. When the item count is not an exact multiple of the column count, the last row only fills the first few cells. The remaining cells stay empty, leaving the rendered section asymmetric and "incomplete" by perception.

For luxury-modern brand positioning (Optimus Pattern #49), this asymmetry is unacceptable. The visitor doesn't articulate why the page feels off — they just feel that something is missing. That feeling kills conversion at the trust layer.

Common offenders:
- **Static value lists** with 3 items (perks, "what's included," differentiators) placed in `sm:grid-cols-2` because the dev assumed pairs read well — but 3 ÷ 2 always orphans
- **Stay / product / blog card lists** with 5 items in `lg:grid-cols-3` (3+2 orphan) or 7 items in `lg:grid-cols-3` (3+3+1 orphan)
- **Dynamic filtered lists** (blog categories, faceted product browsing) where item count varies per filter, so some filters produce orphans even though the all-items view is clean

## Solution
Pattern #71 is the binding rule going forward — every grid's `n` must equal `cols × rows` (every row full), OR a non-grid layout must be used.

For Enchanted Madison specifically:

**`/vip` perks (3 items) — fix: vertical stack** (was `sm:grid-cols-2`):
```tsx
// Was: orphan after 2nd card
<div className="grid grid-cols-1 sm:grid-cols-2 gap-3">{benefits.map(...)}

// Now: clean stack, every row complete (1 card per row)
<ul className="flex flex-col gap-3">{benefits.map(...)}
```

**`/stays` 5-stay grid — fix: featured + 2×2 grid** (was `lg:grid-cols-3`):
```tsx
// Was: 3+2 orphan in second row
<div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
  {siteData.stays.map(stay => <StayCard ... />)}
</div>

// Now: featured + 2x2, every row complete
<div className="flex flex-col gap-6">
  <div className="max-w-3xl mx-auto">
    <ScaleIn><StayCard {...siteData.stays[0]} /></ScaleIn>
  </div>
  <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
    {siteData.stays.slice(1).map(stay => <StayCard ... />)}
  </div>
</div>
```

The featured wrapper's `max-w-3xl mx-auto` constrains the highlighted card so it reads as "featured" without a 1152px-wide image dominating the viewport.

## Prevention

1. **Pattern #71 (this build-log)** documents the canonical decision matrix per item count. Reference it before choosing any `grid-cols-X`. Stack-or-grid is a deliberate design choice, not a default.

2. **Pre-launch-auditor sweep**:
   ```bash
   grep -rnE "grid-cols-[2-5]" src/
   ```
   For every match: count items mapped into the grid; fail if `n % cols !== 0`. Add to Stage 1I checklist alongside Error #59 hero-padding check and Error #61 alternation walk.

3. **Component-data contract for variable lists**: if a `<Grid>` component takes a variable item count via props, it MUST internally compute `cols` from `n` (auto-fill minmax) OR enforce a `featured + grid` pattern OR require a known-good `n` matching the declared `cols`. Don't ship a fixed-`cols` grid that accepts any `items` array without orphan handling.

4. **Mental model**: every visible row of a grid is a contract — "look how complete this set is." A partial row breaks the contract. If you can't fill the row, change the layout, don't ship the orphan.

## Related
- Pattern #71 (build-log Pattern table): canonical decision matrix per item count + featured-card recipe + auto-fill alternative
- Pattern #49: Optimus luxury-modern positioning rule — the "why" this matters
- Error #61: Section alternation regression — same class-of-bug family (visual contract broken by structural mismatch)
