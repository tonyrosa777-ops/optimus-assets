# Error: `backdrop-filter` traps `position: fixed` descendants

**Project:** Goddu Imprint
**Date:** 2026-05-17
**Phase:** Stage 1J post-revision audit (post-v3 hero ship)
**Severity:** P0 conversion-killer on mobile (visual layout failure)

## Problem

Goddu's mobile nav drawer rendered with the dialog wrapper height stuck at 80px instead of full viewport. The drawer's nav links extended OUTSIDE the dialog's bounding box with NO backdrop behind them, so the hero video + headline + CTAs were fully visible THROUGH the drawer. Nav items overlapped with hero text and became unreadable.

Markup at fault (Nav.tsx):

```tsx
<header className="fixed top-0 inset-x-0 ... backdrop-blur-md">
  {/* nav controls ... */}

  <AnimatePresence>
    {open && (
      <motion.div
        className="fixed inset-0 z-50 lg:hidden"
        style={{ background: "var(--bg-base)" }}
        role="dialog"
        aria-modal="true"
      >
        {/* drawer contents — header strip + nav list */}
      </motion.div>
    )}
  </AnimatePresence>
</header>
```

The `<motion.div>` has `position: fixed` + `inset-0`, which SHOULD expand to fill the viewport. Instead it rendered at 80px tall. Hero text below the header showed through the drawer.

## Root Cause

**The `<header>` parent has `backdrop-blur-md` → `backdrop-filter: blur(12px)`. This property creates a new containing block.** Per CSS spec, the following properties (when applied with a non-default value) make their element a containing block for `position: fixed` descendants:

- `transform` (anything non-`none`)
- `filter` (anything non-`none`)
- `backdrop-filter` (anything non-`none`)
- `perspective` (anything other than `none`)
- `contain` (with `paint`, `layout`, `strict`, or `content`)
- `will-change` (with `transform`, `filter`, `backdrop-filter`, `perspective`)
- Modern: `container-type: size`

When ANY of these is on a parent, `position: fixed` descendants inside that element bind to the PARENT'S box, not the viewport. The "fixed" keyword behaves like "absolute" relative to that parent.

In Goddu's case, the header was sized to its child flex container's `h-20` (80px). The drawer's `position: fixed inset-0` therefore expanded to fill 80px instead of the 844px viewport. Its background-color painted only the top 80px. The drawer's nav-list child div, being `position: static`, overflowed the drawer's box and rendered on top of the hero with no backdrop between them.

## Symptoms

- `getComputedStyle(drawer).position === 'fixed'` ✓ (correct)
- `drawer.getBoundingClientRect().height === 80` ❌ (should be viewport height)
- Visually: nav links sit on top of hero content with no opaque backdrop
- Mobile drawer-open screenshot shows BOTH the nav items AND the hero copy simultaneously

## Solution

**Move the `position: fixed` descendant OUT of the element with `backdrop-filter`.** Three viable patterns:

### Pattern A — Sibling wrap (chosen for Goddu)

Wrap the header and the drawer in a fragment so they're siblings. The drawer is no longer a descendant of the backdrop-blurred header.

```tsx
return (
  <>
    <header className="... backdrop-blur-md">{/* ... */}</header>
    <AnimatePresence>
      {open && (
        <motion.div
          className="fixed inset-0 z-[60] lg:hidden overflow-y-auto"
          style={{ background: "var(--bg-base)" }}
          role="dialog"
          aria-modal="true"
        >
          {/* drawer contents */}
        </motion.div>
      )}
    </AnimatePresence>
  </>
);
```

Bump `z-index` so the drawer (now sibling) stays above the header. Add `overflow-y-auto` for tall nav lists.

### Pattern B — React Portal

`createPortal(drawer, document.body)` renders the drawer at the document root, bypassing the header entirely. Stronger isolation but adds SSR considerations and requires `useEffect` to mount the portal target.

### Pattern C — Drop the `backdrop-filter`

Replace `backdrop-blur-md` with a fully-opaque background. Loses the visual treatment but eliminates the containing-block issue. Wrong tradeoff for premium-positioning Optimus builds where the blurred-glass nav IS the luxury cue.

## Prevention

**Add to design-synthesizer + animation-specialist agents:** before placing ANY `position: fixed` descendant inside a `backdrop-filter`, `filter`, `transform`, `perspective`, or `contain`-bearing element, render it as a sibling or via portal.

**Add to pre-launch-auditor checklist:** at mobile widths (390/375/428), open the mobile nav drawer and verify the drawer's `getBoundingClientRect()` height equals the viewport height. If less, the containing-block trap has fired.

**Add to multi-breakpoint audit (Pattern: end-of-build-multi-breakpoint-browser-audit.md):** mobile drawer-open MUST be tested at every mobile viewport. Screenshot + verify hero content is NOT visible through the drawer.

## Affected Patterns

This same trap fires for ANY of these compositions:

- Floating CTA / scroll-to-top button inside a header with `backdrop-filter`
- Tooltip/popover positioned via `position: fixed` inside a card with `filter: drop-shadow`
- Modal dialog inside an element with `will-change: transform`
- Toast notifications inside a layout wrapper with `transform: translateZ(0)` (a common hack for hardware acceleration that ALSO traps fixed descendants)
- Sticky header inside a parent with `contain: paint` (sticky becomes absolute)

If a layout component visually behaves like an absolutely-positioned element when you wanted viewport-bound positioning, walk up the DOM tree and check for these properties on every ancestor.

## How to detect during audit

```js
// Run in console — finds ancestors that would trap position:fixed
function findContainingBlockAncestor(el) {
  let cur = el.parentElement;
  const trapProps = ['transform', 'filter', 'backdrop-filter', 'perspective'];
  while (cur && cur !== document.documentElement) {
    const cs = getComputedStyle(cur);
    for (const prop of trapProps) {
      if (cs[prop] && cs[prop] !== 'none') {
        return { ancestor: cur, property: prop, value: cs[prop] };
      }
    }
    if (cs.contain && /paint|layout|strict|content/.test(cs.contain)) {
      return { ancestor: cur, property: 'contain', value: cs.contain };
    }
    cur = cur.parentElement;
  }
  return null;
}
// Usage:
findContainingBlockAncestor(document.querySelector('[role="dialog"]'));
```

## Related

- Pattern [[../patterns/end-of-build-multi-breakpoint-browser-audit]] — add mobile drawer-open verification step
- Project Goddu Imprint commit `047bce3` — the fix
- CSS spec: [Containing block — MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Containing_block#identifying_the_containing_block)
- The Stage 1I audit at commit `16e6a85` opened the drawer but did not stress-test with hero content visible — checklist gap that allowed this to ship initially.

## Why this took two Stage 1I audits to catch

The prior Stage 1I audit at `16e6a85` opened the drawer + verified the close button worked. It did NOT verify that hero content was NOT visible through the drawer. With a properly-opaque drawer of viewport size, you don't notice the trap because nothing bleeds through. The bug becomes visible only when the drawer is collapsed to a smaller-than-viewport box AND the content behind it has high visual weight. In Goddu's case, the v3 hero video added that visual weight — every frame now actively competes with foreground content, so the bleed-through became immediately obvious during the post-v3 audit even though the underlying DOM structure was unchanged.

**Lesson for future audits:** mobile drawer test = open + screenshot AT a viewport with rich hero content behind it + verify hero text is NOT readable through the drawer. Not just "drawer opens, X closes it."
