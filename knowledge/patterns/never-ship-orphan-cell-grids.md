# Pattern #71 — Never ship orphan-cell grids

**Status:** ACTIVE. Binding on every Optimus build from 2026-05-13 onward.
**Source incident:** Enchanted Madison `/vip` 3-perks-in-2-col + `/stays` 5-stays-in-3-col bugs.
**User framing:** *"assume our viewer has OCD and make sure things look right."*

## The rule in one sentence
For every CSS grid in a rendered layout, the visible item count `n` MUST equal `cols × rows` so every row is fully filled — never ship a grid where the last row has empty cells.

## Why this matters

Luxury-modern positioning (Pattern #49) commits every Optimus site to feel as polished as Stripe / Vercel / Linear. None of those brands ship a section with 3 cards in a 2-col grid where the third sits alone next to an empty cell. The asymmetry reads as "missing content" or "page is broken" — even when the visitor can't articulate why. That perception kills trust at the conversion layer.

Visual completeness is a precondition of luxury, not a polish item.

## Decision matrix by item count

Pick a layout where `n % cols === 0` for the cols value used at every breakpoint:

| Items | Recommended layout | Tailwind class | Notes |
|---|---|---|---|
| 2 | 2-col OR stack | `grid-cols-1 sm:grid-cols-2` | Both clean |
| 3 | 3-col OR stack | `grid-cols-1 lg:grid-cols-3` OR `flex flex-col` | **NEVER `2-col`** — orphans on the 2nd row |
| 4 | 2x2 OR 4-col OR stack | `grid-cols-1 sm:grid-cols-2` OR `grid-cols-1 lg:grid-cols-4` | 2x2 is the safest default |
| 5 | **featured + 2x2** OR stack | See "Featured + grid" pattern below | Stand-alone 5-col on lg makes cards too narrow |
| 6 | 2-col (3x2) OR 3-col (2x3) | `grid-cols-1 sm:grid-cols-2` OR `lg:grid-cols-3` | Both clean |
| 7 | **featured + 3x2** OR stack | featured-1 + `grid-cols-1 sm:grid-cols-2 lg:grid-cols-3` (6 below) | 7 alone never grids cleanly |
| 8 | 2-col (4x2) OR 4-col (2x4) | `grid-cols-1 sm:grid-cols-2 lg:grid-cols-4` | Both clean |
| 9 | 3x3 | `grid-cols-1 sm:grid-cols-2 lg:grid-cols-3` | Clean |
| 10 | 2-col (5x2) OR featured + 3x3 | `grid-cols-1 sm:grid-cols-2` OR featured + `lg:grid-cols-3` | Featured + 3x3 for hero-page lists |
| 11 | **featured + 3x3 with 2 stacked below** OR stack | Custom — most fragile count | Consider growing to 12 or shrinking to 10 |
| 12 | 2-col (6x2), 3-col (4x3), 4-col (3x4) | `grid-cols-1 sm:grid-cols-2 lg:grid-cols-3` | Very flexible |

**Above 12:** likely pagination or scroll-based virtual list. Apply the same per-page rule.

## The "Featured + grid" canonical pattern

For odd counts ≥ 5 where no clean grid exists, lift one item out as a "featured" card above a clean grid of the rest:

```tsx
{/* Featured — width-constrained so it reads "highlighted" not "viewport-dominating" */}
<div className="max-w-3xl mx-auto">
  <ScaleIn>
    <Card {...items[0]} variant="featured" />
  </ScaleIn>
</div>

{/* Clean grid of the rest */}
<div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
  {items.slice(1).map((item, i) => (
    <ScaleIn key={item.id} delay={(i + 1) * 0.08}>
      <Card {...item} />
    </ScaleIn>
  ))}
</div>
```

**Featured-card sizing rules:**
- `max-w-3xl mx-auto` keeps the featured card centered + width-constrained. Image at 16:10 inside this comes out around 768×480 — large, but not viewport-dominating.
- For genuinely hero-style featured: use `max-w-5xl mx-auto` with a custom horizontal-split card variant (image on one side, content on the other). See blog `PostCard featured` for the reference implementation.
- The featured card should be the LEGITIMATELY most-prominent item (flagship product, top-ranked story, most-popular tier). Don't pluck items arbitrarily — viewers smell it.

## Vertical stack alternative

For 3 items specifically (and any count where the available width per card in a horizontal grid would be cramped), vertical stack is the cleanest fallback:

```tsx
<ul className="flex flex-col gap-3">
  {items.map((item) => (
    <li key={item.id} className="rounded-xl p-4 flex gap-3 items-start" style={{ background: "var(--bg-card)" }}>
      <span className="text-xl flex-shrink-0">{item.icon}</span>
      <p className="text-sm font-medium leading-relaxed">{item.label}</p>
    </li>
  ))}
</ul>
```

Each item gets the full container width with horizontal layout inside the card (icon + text side by side). Reads more deliberate than a narrow 3-col row of cards. Works for any item count.

## Dynamic / filtered counts (blog categories, faceted browsing)

When the item count varies based on user filter, three options:

1. **Featured + remaining**: always feature the top item, render `slice(1)` in a grid. Pick a `cols` value where common remaining counts grid cleanly. If filter narrows to 1, featured carries the page alone.

2. **CSS auto-fill minmax**: `grid-template-columns: repeat(auto-fill, minmax(280px, 1fr))`. Browser computes how many cards fit per row at the current viewport and fills accordingly. Last row may have orphan cells visually, but `justify-content: start` aligned to a known card-width feels more grid-like than column-mismatched.

3. **Enforce minimum item count**: if a category has < 4 items, hide the category filter OR show a different layout for that category. Don't ship a grid that breaks at specific filter values.

The featured + remaining pattern is the most luxury-aligned and is the default for Optimus blog / shop / browse pages.

## Pre-launch-auditor sweep

```bash
# Find every grid-cols-N use in the codebase
grep -rnE "grid-cols-[2-5]" src/
```

For each match: count the items being mapped into the grid. Fail if `items.length % cols !== 0` at any breakpoint.

For dynamic counts (filtered lists): identify every filter value the user can toggle, compute the resulting item count for each, fail if any filter produces an orphan grid.

Add this check to the Stage 1I Visual QA checklist alongside Error #59 hero-padding measure and Error #61 dark/light alternation walk.

## Common mistakes to avoid

1. **Defaulting to `sm:grid-cols-2` because "pairs read well"** — only true for even item counts. 3 in a 2-col grid is the most common orphan-grid bug in Optimus history.

2. **Forgetting that grids inherit from data** — if `siteData.stays` was 4 items when you wrote the page and is 5 now, the layout breaks. Anchor the layout decision to the data length, not the original design.

3. **Mismatched breakpoints** — `sm:grid-cols-2 lg:grid-cols-3` with 6 items is clean at `lg` (2x3) AND at `sm` (3x2). With 4 items it's clean at `lg` (1x3 + orphan) — WAIT, that's NOT clean at lg. Always check every breakpoint.

4. **Hiding the orphan with `place-items-center`** — centering an orphan card in its half-empty row makes it look more orphaned, not less. The empty space on either side announces the missing content. Restructure the layout.

5. **Adding placeholder cards to fill the grid** — ships fake content. Never do this. Restructure.

## Related
- Pattern #49 — Optimus luxury-modern positioning (the "why" this rule exists)
- Pattern #8 — Homepage dark/light section rhythm (related visual-contract rule)
- Pattern #51 — Luxury gradient backgrounds (no flat solids = no incomplete grids; both are visual-contract rules)
- Error #61 — Section alternation regression (same class-of-bug family: visual contract broken by structural mismatch)
- Error #63 — Orphan-cell grid layouts (the discovery incident for this pattern)
