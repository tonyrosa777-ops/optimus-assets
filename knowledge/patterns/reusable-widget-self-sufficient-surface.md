# Pattern: Self-sufficient solid surface for reusable widgets

**Category:** Visual Design / Component Architecture
**First used:** LMP Financial — 2026-05-02
**Status:** VALIDATED — 2026-05-02

## What

When a component ships into **multiple section contexts** (some dark, some light, sometimes a modal overlay), it must render a **solid background of its own** rather than relying on a translucent Card variant that assumes a particular parent.

Rule of thumb:
- **Translucent variants** (`Card variant="dark"` = `rgba(255,255,255,0.04)`, `Card variant="light"` with shadow) are *safe* when the parent section's tone is fixed at write time.
- **Self-sufficient solid surfaces** are *required* when the parent's tone varies across consumers.

## When to use this pattern

Apply it to any component that meets either condition:

1. The component is imported by 2+ files AND those files put it inside section-tone-mismatched parents (e.g. one consumer wraps it in `section-dark-gradient`, another in `section-light-gradient`).
2. The component is sometimes rendered inside a modal/dialog/portal where the surrounding tone is unknown.

If both consumers are always inside the same tone, you don't need this pattern — the standard `Card variant` is fine.

## When NOT to use this pattern

- Static page sections written next to their parent in the same file (e.g. a `LoanProgramCard` rendered inside `ServicesSection.tsx` only). The variant is eyeball-paired at write time.
- A widget that's *intentionally* tone-portable but uses pure white surfaces (e.g. a price-comparison card) — the white Card variant is already self-sufficient.

## Pattern

For dark-themed widgets (calendar, video player, audio player, code block, dark-mode chart):

```tsx
// component.tsx
import { cn } from '@/lib/utils';

export default function MyWidget({ className }: { className?: string }) {
  return (
    <div
      className={cn(
        'rounded-[var(--radius-xl)] p-6 border backdrop-blur-sm shadow-[var(--shadow-lg)]',
        className,
      )}
      style={{
        background: 'var(--primary)',          // SOLID navy — independent of parent
        borderColor: 'var(--border-dark)',
      }}
    >
      {/* internal text uses cream tokens —
          --text-primary, --text-secondary, --text-muted */}
    </div>
  );
}
```

For light-themed widgets (form panel, info card meant to read as "stepping into the light" on a dark page):

```tsx
<div
  className="rounded-[var(--radius-xl)] p-6 border shadow-[var(--shadow-lg)]"
  style={{
    background: 'var(--bg-card)',              // solid white
    borderColor: 'var(--border-light)',
  }}
>
  {/* internal text uses --text-on-light family */}
</div>
```

The shadow gives the widget elevation against any parent. The border is the safety net — even if the parent is the same tone as the widget, the border defines the edge.

## Why this beats `Card variant="dark"`

| Scenario | Card variant="dark" | Self-sufficient solid |
|---|---|---|
| Dark section parent | Translucent overlay reads as elevation ✓ | Solid bg + border + shadow ✓ |
| Light section parent | 4% white-on-cream = invisible ✗ | Solid navy on cream = focused widget ✓ |
| Modal overlay (`bg-black/70` backdrop) | Translucent overlay disappears into backdrop ✗ | Solid surface stands out ✓ |
| Future tone change of parent | Silent regression ✗ | No change needed ✓ |

## Reference implementations

- **LMP Financial** `src/components/BookingCalendar.tsx` (commit `db06ed5`) — solid `var(--primary)` widget rendered in 4 contexts: LO landing page (dark), `/booking` (light), `/quiz` results (light), `/pricing` modal (overlay).

## Pitfalls

- **Don't drop the border.** On a dark-section parent, the widget's solid navy and the section's navy gradient blend without one — the widget loses its edge. `var(--border-dark)` (~10% cream alpha) provides a hairline that reads on both tones.
- **Don't drop the shadow.** Shadow is what sells the elevation on light sections. `var(--shadow-lg)` is the right default.
- **Don't use `var(--primary-deep)` instead of `var(--primary)`** unless the widget needs to read as "deeper" than the surrounding dark sections. `--primary-deep` is reserved for footers and the dropdown menu panels — using it for inline widgets makes them read as recessed instead of elevated.
- **Don't mix tones.** Dark widget = cream text family throughout. Light widget = navy text family throughout. Don't put `--text-on-light` text inside a `var(--primary)` background or vice versa — that's the same bug class on the inside of the widget.

## Pre-launch auditor addition

Before sign-off:
1. List every component imported by 2+ consumer files.
2. For each, identify the parent section type at every consumer site (`section-dark-gradient`, `section-light-gradient`, modal, other).
3. If the parent tone varies across consumers, the component must render a self-sufficient solid surface — not `Card variant="dark"` or `variant="light"`.
4. If any consumer puts the widget in a tone that mismatches the variant, that's a BLOCK-class contrast bug.

## Related

- [[errors/reusable-widget-card-variant-mismatch]] — the bug that prompted this pattern
- [[errors/calendly-dark-mode-textcolor-incomplete]] — a different surface-contrast bug (third-party iframe) with a related "give it its own light stage" solution
- [[patterns/calendly-light-stage-section]] — companion pattern for third-party scheduler embeds
