# Error: Reusable widget invisible on light section — Card variant="dark" + cream tokens

**Project:** LMP Financial
**Date:** 2026-05-02
**Phase:** Phase 1K — i18n + nav cleanup polish

## Problem

`BookingCalendar` rendered as **completely invisible** on the quiz results page (light gradient section): cream "Pick a day" headline, cream date numbers, cream "DEMO MODE" badge — all sitting on a near-identical cream background. Same bug affected the `/booking` page, where the calendar was deliberately placed on a light section per the page's dark→light→dark rhythm.

User reported: *"The calendar is practically invisible. White on white, we need to fix this everywhere it applies."*

The widget worked correctly on dark sections (LO landing pages at `/team/[lo-slug]`), so the bug only manifested when the same component was reused in a different section context.

## Root Cause

Two design-system tokens collided:

1. **`Card variant="dark"`** in `src/components/ui/Card.tsx` applies `bg-[var(--bg-card-dark)]` = `rgba(255, 255, 255, 0.04)`. That 4% white overlay is *intentionally* translucent — designed to read as a subtle elevation when the parent section is also dark navy. On a cream parent, the overlay is functionally invisible: 4% white over cream produces another shade of cream.

2. **Internal text** uses `--text-primary` = `#F5EFE2` (cream) and the cream `--text-secondary` / `--text-muted` family — all designed for dark backgrounds.

Result: cream text rendered on the underlying section's cream gradient. Zero contrast.

The Card variant system silently assumes `variant="dark"` cards always sit on dark sections. Static page Cards get hand-paired with their adjacent section at write time (eyeball check), so the assumption holds. But `BookingCalendar` is a *reusable widget* dropped into multiple section contexts (LO page = dark, /quiz results = light, /booking = light, /pricing modal = overlay). Its parent context varies, the variant doesn't.

## Solution

Stop using the translucent Card variant for context-portable widgets. `BookingCalendar` now renders a **self-sufficient solid dark surface**:

```tsx
// src/components/BookingCalendar.tsx
return (
  <div
    className={cn(
      'rounded-[var(--radius-xl)] p-6 border backdrop-blur-sm shadow-[var(--shadow-lg)]',
      className,
    )}
    style={{
      background: 'var(--primary)',          // SOLID navy — works on any parent
      borderColor: 'var(--border-dark)',
    }}
  >
    {/* …all internal text keeps its cream tokens, now on real navy */}
  </div>
);
```

Replaced `<Card variant="dark" hover={false}>` with a hand-rolled container using `var(--primary)` (#0E1B33). The cream text tokens inside the calendar now sit on real navy regardless of what section the calendar lands in.

Visually: on dark sections the calendar reads as a subtly elevated surface (border + shadow against the section gradient). On light sections it reads as a focused dark widget — Stripe-style inline embed pattern, premium and intentional.

## Verification

Browser-tested at 1440px:

- **`/booking`** (light gradient parent, was broken): calendar reads cleanly as a navy widget on cream, dates crisp, weekend-disabled state visible, DEMO MODE badge readable.
- **`/team/mike-comerford`** (dark gradient parent, was working): no regression — calendar still renders as a slightly elevated surface via border + shadow.
- **`/quiz` results** (light gradient parent, was broken): inherits the fix.
- **`/pricing` modal** (modal overlay, was working): inherits the fix.

Site-wide sweep agent mapped every `<section className="...section-(dark|light)-gradient...">` against every `<Card variant="...">` it contains across all 39 candidate files. **Zero other instances of this bug class** — every Card variant matches its parent section's tone correctly. The BookingCalendar was uniquely affected because it's the only widget where parent context varies.

## Prevention

**Universal rule for any reusable widget that ships into multiple section contexts:** use a self-sufficient solid surface, never the translucent `Card variant="dark"`. The translucent variant is only safe when the widget's parent is *always* a dark gradient.

Decision tree:
- Static page Card placed adjacent to one specific section → use `Card variant="dark"` or `variant="light"` matching the section. Eyeball-check at write time.
- Reusable widget rendered by multiple consumers across mixed dark/light contexts → use solid `var(--primary)` for dark-themed widgets or solid `var(--bg-card)` for light-themed widgets. Both work on any parent.

Pre-launch auditor addition: before sign-off, identify every component imported into 2+ files. For each, list the parent sections of every consumer. If any consumer puts the widget in an opposite-tone section to the others, the widget MUST use a solid surface, not a translucent variant.

See [[patterns/reusable-widget-self-sufficient-surface]] for the codified pattern + decision tree.

## Related

- [[patterns/reusable-widget-self-sufficient-surface]]
- [[errors/calendly-dark-mode-textcolor-incomplete]] (different mechanism — third-party iframe — but same symptom: low-contrast text on calendar surfaces)
- LMP Financial commit `db06ed5`
