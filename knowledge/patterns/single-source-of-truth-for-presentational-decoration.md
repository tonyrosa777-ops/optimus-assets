# Pattern: Single source of truth for presentational decoration — data layer OR component layer, never both

**Category:** Architecture / Component-Data Contract / Quality Gate
**First used:** Ead Financial — 2026-05-08

## What

A binding rule for every component that wraps data-layer strings with presentational marks: **either the data string contains the decoration and the component does not, or the component renders the decoration and the data string does not.** Never both. Applies to every form of presentational decoration: stars (`★★★★★`), dollar prefixes (`$`), percent suffixes (`%`), em-dash attributions (`— Sarah`), bullet markers (`•`, `·`), chevron eyebrows (`»`, `›`), brass dot dividers, parentheses around credentials, etc.

The contract is documented inline as a comment next to the data field, citing the component that owns the decoration:

```ts
// Hero.tsx renders the ★★★★★ prefix and the credentials suffix from siteConfig.credentials.
// This string holds the middle content only — no stars, no credentials, no leading/trailing dots.
trustMicrocopy: "Trusted by New England business owners · 30+ years of practice"
```

## When to Use

Mandatory for every component-data pair where the component wraps a string from `/data/site.ts` with any presentational decoration. The pattern triggers whenever ANY of these are true:
- Component prepends a fixed character/string to the data (`★`, `$`, `»`, `—`)
- Component appends a fixed character/string to the data (`%`, ` →`, ` ·`)
- Component interpolates other config alongside the data (`{value} · {credentials.join(" · ")}`)
- Component renders the data inside a wrapping element with semantic decoration (`<sup>$</sup>`, `<em>—</em>`)

Most-common applicable surfaces in an Optimus build:
- **Hero trust microcopy** — stars + credentials decoration (this pattern's first instance)
- **Pricing tier card** — `$` prefix on `setupPrice` / `monthlyPrice`, `/mo` suffix on monthly retainers, `+` infix on hybrid prices ("$1,250/return + $1,000/mo")
- **Stats bar** — `+` suffix on year counts ("30+"), `%` suffix on percentages, `$` prefix on revenue savings, `,` thousands-separator on counts
- **Testimonial attribution** — em-dash separator (`— Sarah, Treatment Center Operator`), dot dividers between role and location
- **Eyebrow labels** — chevron prefix (`» CHAPTER 02`), uppercase + tracking-wide via CSS
- **CTA button labels** — arrow suffix (`Book Now →`), call-to-action verb prefix
- **FAQ category labels** — emoji prefix per CLAUDE.md emoji rule, parentheses around count
- **Breadcrumb separators** — `›` or `/` between segments
- **Disclosure caption** — italic asterisk prefix on testimonial provenance

## How

The decision procedure when designing a component-data contract:

1. **Identify every presentational mark the component will display.** Stars, currency, separators, suffixes, prefixes, decoration.
2. **For each mark, decide which layer owns it:**
   - **Data layer (string contains it):** if content-writer needs to vary the mark per entry (some testimonials get a fancy quote treatment, some don't), or if the mark is part of voice ("$1,250" is different content from "$1,500" — the dollar amount is data, but the `$` itself is structural).
   - **Component layer (JSX renders it):** if the mark is a fixed structural decoration that NEVER varies between entries (every star gets brass color via CSS; every pricing tier gets `$` prefix; every testimonial attribution gets em-dash), if the mark needs CSS styling that's awkward in a string (color, hover state), if the mark depends on other config (`credentials.join()` interpolation, locale-specific formatting).
3. **Default rule when in doubt: COMPONENT layer.** Components have the rendering tools (CSS, conditional logic, locale formatting). Data layer should be content-only.
4. **Document the contract inline next to the data field.** A two-line comment citing the component that owns the decoration prevents the next agent (or the next session of the same agent) from re-adding the mark to the string.
5. **Run the audit grep at Stage 1H pre-launch-auditor:** see Anti-Pattern Greps below.

## Key Rules

- **One mark, one source.** If the component renders `★★★★★`, the data string does NOT contain `★`. If the data string contains `$1,250`, the component does NOT prepend another `$`.
- **Inline comment citing the contract is required.** Two lines next to the data field:
  ```ts
  // <Component>.tsx renders the <decoration> from <source>.
  // This string holds <what content stays in the data layer>.
  ```
- **CSS-renderable marks belong in the component.** Stars colored with `var(--accent)` brass are easier to maintain in JSX than UTF-8 chars styled via embedded `<span>` tags inside a string.
- **Configurable marks belong in the component.** Credentials interpolated from `siteConfig.credentials: string[]` cannot live in a string literal — they must be JSX-rendered. By extension: any mark that depends on other config (`credentials.join("•")`, locale-specific currency formatting, conditional `(Most Popular)` tag) belongs in the component.
- **Voice-as-content marks belong in the data.** Em-dashes embedded inside a sentence (`"…all of these without professional guidance — an attorney, an accountant, and ideally a consultant…"`) are content, not decoration. They stay in the data. Em-dashes used as attribution separators (`— Sarah`) ARE decoration. They go in the component.

## Anti-Pattern Greps (Stage 1H pre-launch-auditor checklist)

Add to the pre-launch-auditor's source scan:

```bash
# Star prefix duplicated in data layer
grep -nE '"\\s*★' web/src/data/site.ts

# Dollar prefix duplicated in data layer (any tier/stat/pricing string)
grep -nE '"\\s*\\$\\s*[0-9]' web/src/data/site.ts

# Em-dash attribution duplicated (testimonial source + Testimonial component both prepending)
grep -nE '"\\s*—\\s+[A-Z]' web/src/data/site.ts

# Chevron eyebrow duplicated
grep -nE '"\\s*[›»]\\s' web/src/data/site.ts

# Leading/trailing dot separator (typically a sign the component will add another)
grep -nE '"\\s*·' web/src/data/site.ts
grep -nE '·\\s*"' web/src/data/site.ts
```

If any of these match, manually verify the corresponding component to confirm whether it ALSO renders the same mark. If yes, BLOCK launch until the duplicate is reconciled.

## Reuse Condition

Every Optimus build, every component-data pair where the component wraps strings with presentational decoration. The pattern is a CLAUDE.md-class workflow rule that should be added to design-synthesizer.md briefs and content-writer.md briefs as the binding contract: "Decide which layer owns each presentational mark before populating /data/site.ts. Document the contract inline. Pre-launch-auditor verifies via grep."

The most-likely future hits (in approximate frequency order):
1. Pricing tier card `$` prefix on prices when content-writer puts `"$1,250"` in the data + PricingCard prepends another `$`
2. Stats bar `+` suffix on year counts when site.ts has `"30+ years"` + Stat component appends `+`
3. Testimonial attribution em-dash when site.ts has `"— Sarah"` + Testimonial prepends `—`
4. Eyebrow chevron when site.ts has `"» CHAPTER 02"` + Eyebrow prepends `»`
5. Breadcrumb separator when site.ts has `"Service Areas › Methuen"` + Breadcrumb component re-renders the `›`

## Related

- [[errors/hero-trust-microcopy-double-rendered-decoration]] (Error #57) — the Ead Financial instance that produced this pattern
- [[patterns/section-12-psychological-foundations-design-system]] (Pattern #61) — Subsection 7 (pre-launch-auditor checklist) should include the anti-pattern greps from this pattern
- CLAUDE.md Copy Writing Rule — voiced-copy em dash ban is a related but distinct rule (em dashes in CONTENT vs em dashes as decoration)
