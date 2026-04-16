# Pattern: Consistent page header structure across all interior pages
**Category:** Architecture / Visual Design
**First used:** Witt's Restoration LLC — 2026-04-12

## What
Every interior page must use the same header structure: fragment root (no `<main>` wrapper), radial gradient header section with `relative overflow-hidden`, big shimmer heading + optional subtitle, ambient canvas animation (RisingAsh), then content sections below with alternating backgrounds.

## When to Use
Every Optimus build — enforce during scaffold and verify during pre-launch audit.

## How
Standard header pattern:
```tsx
<>
  {/* Page Header */}
  <section
    className="relative overflow-hidden py-16 md:py-24"
    style={{
      background: "radial-gradient(ellipse at 50% 0%, rgba(brand,0.08), transparent 70%)",
    }}
  >
    <RisingAsh />
    <div className="relative z-10 mx-auto max-w-4xl px-6 text-center">
      <FadeUp>
        <h1 className="hero-shimmer font-display text-display mb-6">
          Page Title
        </h1>
      </FadeUp>
      <FadeUp delay={0.15}>
        <p style={{ color: "var(--text-secondary)" }}>Subtitle here</p>
      </FadeUp>
    </div>
  </section>

  {/* Content sections follow */}
</>
```

## Key Rules
- Fragment `<>` root — NOT `<main>` with inline background (causes color scheme mismatch)
- H1 always uses `hero-shimmer font-display text-display` — no `text-h1`, no `text-h2`, no inline fontSize
- Heading and subtitle belong in the SAME section — don't split into separate sections
- Canvas animation component sizes from parent via `parentElement.getBoundingClientRect()`
- Content div gets `relative z-10` so text renders above canvas

## Reuse Condition
Every Optimus build with interior pages (all of them)

## Related
- Pattern #37: page-header ambient radial gradient
- Error #42: missing text-h1 CSS utility
- Error #44: canvas offsetWidth inside fixed container
