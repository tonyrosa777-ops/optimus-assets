# Pattern: `clamp()`-Based Responsive Type Scale
**Category:** Typography / Architecture
**First used:** Gray Method Training — 2026-04-10

## What

Declare every display-tier font size (anything above ~2rem / 32px) as a `clamp(min, vw-based preferred, max)` expression in the CSS custom property AND the matching `@utility` class. One change in `globals.css` makes every heading in the project scale responsively from mobile to desktop without touching any component files.

## When to Use

- On every new build: do this at Phase 1 (globals.css setup), not as a retrofit
- On any project where the display type scale is declared once and reused across many pages
- When `text-display`, `text-title-xl`, or similar utilities exist and are used in more than ~3 places
- Any time a designer specifies a single pixel value for a hero heading (translate it to a clamp)

## How

### Tailwind v4 / CSS-first approach (Gray Method Training)

```css
@theme {
  /* Fixed value — wrong */
  --text-display: 4.5rem;

  /* Clamp — correct */
  --text-display: clamp(2.5rem, 8vw, 4.5rem);
  --text-title-xl: clamp(2rem, 5.5vw, 3rem);
  --text-title-lg: clamp(1.75rem, 4vw, 2.25rem);
}

@utility text-display {
  font-size: clamp(2.5rem, 8vw, 4.5rem);
  line-height: 1.05;
  letter-spacing: -0.02em;
}
```

Both the `--text-*` variable AND the `@utility` must be updated — the utility's `font-size` is what Tailwind actually emits for `className="text-display"`, and other files may reference `var(--text-display)` directly in styles.

### Tailwind v3 / config approach (older projects)

```ts
// tailwind.config.ts
export default {
  theme: {
    extend: {
      fontSize: {
        'display': ['clamp(2.5rem, 8vw, 4.5rem)', { lineHeight: '1.05', letterSpacing: '-0.02em' }],
      }
    }
  }
}
```

### Picking the three values

For an 8-character to 30-character display heading:

| Role | Size | Reasoning |
|------|------|-----------|
| **Min** | 40–44px (2.5–2.75rem) | Smallest phone (iPhone SE 375px) minus 48px padding = 327px. A 15-char phrase at ~20px avg char width needs ~300px — fits with breathing room. |
| **Preferred** | 7–8vw | At 1440px viewport, 8vw = 115px → clamped to max. At 600px viewport, 8vw = 48px → above min. Smooth scaling in between. |
| **Max** | 64–72px (4–4.5rem) | Desktop hero ceiling. Any larger and the column overflow risk at 1024 grows. |

Rule of thumb: **min is ~55% of max, preferred is 7–8vw.**

## Key Rules

- **Never use a fixed rem value for display-tier type.** If a designer hands you "72px hero", translate it to `clamp(2.5rem, 8vw, 4.5rem)` before writing CSS.
- **Update both the variable AND the `@utility`** in Tailwind v4. If you only update the variable, `className="text-display"` still uses the hardcoded value in the utility.
- **Verify the min at 375px.** The widest word-pair in any H1 on the site must fit on one line at the min size. Check with the multi-breakpoint browser audit.
- **Don't clamp body text sizes.** 1rem (16px) is a standard; users expect it. Clamp only applies to display-tier sizes that would otherwise be disproportionate on mobile.
- **Letter-spacing stays fixed**, not clamped. Tracking of `-0.02em` scales naturally with font-size since `em` is relative.

## Reuse Condition

Every build with a custom type scale in `globals.css`. This should be baked into the project-setup phase so it's never a retrofit.

For typography-forward brands (luxury, editorial, fashion) consider going further and clamping `--text-lead` and `--text-body-large` as well.

## Related

- [[errors/fixed-rem-display-font-size-breaks-mobile]] — the bug this pattern prevents
- [[patterns/end-of-build-multi-breakpoint-browser-audit]] — the audit that catches fixed-size regressions
- Workflow gap: add to `website-build-template.md` Phase 1 (globals.css setup) as mandatory
