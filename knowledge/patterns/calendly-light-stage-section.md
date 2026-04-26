# Pattern: Calendly light-stage section (dark-brand sites)

**Category:** Scheduling / Visual Design / Conversion
**First used:** Collaborative Insights — 2026-04-20

## What
When embedding Calendly on a dark-brand Optimus site, give the widget its own **light-themed section** (ivory/cream background) instead of fighting Calendly's dark-mode embed. Use Calendly's native light theme (where contrast is built-in), keep only `primaryColor` + `hideGdprBanner` in `pageSettings`, and frame the booking section as a deliberate visual break — "the moment we step into the light."

## When to Use
- Any Optimus build with a dark-brand site + Calendly inline embed
- Default choice, not exception — dark-mode Calendly embeds have un-overridable secondary-text contrast issues (see [[errors/calendly-dark-mode-textcolor-incomplete]])
- Works for any scheduler iframe with similar customization limits (Cal.com, SavvyCal if we add them later)

## How

```tsx
// BookingClient.tsx — light stage section
<section style={{ padding: "3rem 0 var(--section-padding-mobile)", background: "#F5F0EB" }}>
  <div className="container-page max-w-5xl mx-auto">

    {/* Session selector cards — light variant */}
    <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-10">
      {sessions.map((s, active) => (
        <button style={{
          backgroundColor: active ? "#FFFFFF" : "rgba(255,255,255,0.6)",
          border: active ? "2px solid var(--accent)" : "1px solid rgba(26,26,26,0.08)",
          boxShadow: active
            ? "0 8px 24px rgba(197,165,90,0.15)"
            : "0 2px 8px rgba(26,26,26,0.04)",
        }}>
          {/* Title: color "#1A1A1A"       (dark on light) */}
          {/* Duration: color "#7A7470"    (warm muted)   */}
          {/* Description: color "#4A4A4A" (dark secondary) */}
          {/* Price: color "var(--accent)" (brand gold)   */}
        </button>
      ))}
    </div>

    {/* Widget wrapper — clean white card with soft elevation */}
    <div style={{
      backgroundColor: "#FFFFFF",
      boxShadow: "0 12px 40px rgba(26,26,26,0.08)",
      border: "1px solid rgba(26,26,26,0.06)",
      borderRadius: "1rem",
      overflow: "hidden",
    }}>
      <InlineWidget
        url={session.url}
        styles={{ height: "720px", width: "100%" }}
        pageSettings={{
          primaryColor: "C5A55A",   // brand gold — selections, arrows, available dates
          hideGdprBanner: true,
          // NO backgroundColor, NO textColor — let Calendly's light defaults handle contrast
        }}
      />
    </div>

  </div>
</section>
```

Hero section above this stays dark with the gold shimmer H1. The tonal transition hero→stage is intentional and satisfies the dark/light section alternation rule (Pattern #8 + CLAUDE.md Section Alternation Rule).

## Key Rules
- **Never set `backgroundColor` or `textColor` in `pageSettings`** when using this pattern. Those params force Calendly into a custom-theme mode that has the contrast bugs. Omit them; Calendly's light-mode defaults are better.
- **Section background** must be a warm light tone (`#F5F0EB` brand ivory works for most palettes; cream/off-white also fine) — NOT pure white. Pure white makes the white widget card disappear into the bg and kills the "card" feel.
- **Widget wrapper** is pure white with subtle shadow so the card reads as elevated above the section.
- **Session selector** also needs the light variant — don't leave it on dark-surface styling, it'll feel pasted-in.
- **Text colors on light surface:** titles `#1A1A1A`, descriptions `#4A4A4A`, muted `#7A7470`. Brand accent stays `var(--accent)` (gold works fine on light).

## Reuse Condition
Any future Optimus build where:
- The site is dark-brand AND
- Calendly (or any scheduler iframe with similar theming limits) is embedded inline on a dedicated booking page

If the client explicitly requests an all-dark booking page with Calendly: push back. The dark-mode embed cannot deliver readable secondary text, and users will abandon before reaching the booking form.

## Related
- [[errors/calendly-dark-mode-textcolor-incomplete]] — the problem this pattern solves
- [[errors/native-picker-plus-calendly-double-entry]] — the wrong fix that prompted this pattern
- [[patterns/calendly-inline-embed-brand-colors]] (Pattern #13) — brand-color URL params; amend with "only for light theme" caveat
- Pattern #8 homepage-dark-light-section-rhythm — this is the same alternation principle applied to the booking page's internal structure
