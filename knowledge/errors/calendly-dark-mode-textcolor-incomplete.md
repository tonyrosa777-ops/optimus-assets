# Error: Calendly dark-mode `pageSettings.textColor` incomplete

**Project:** Collaborative Insights
**Date:** 2026-04-20
**Phase:** Phase 9 — Booking (polish pass)

## Problem
Calendly `InlineWidget` configured for dark theme via `pageSettings`:

```ts
pageSettings={{
  backgroundColor: "1A1A1A",
  primaryColor: "C5A55A",
  textColor: "FFFFFF",   // tried F5F0EB, FFFFFF, C5A55A — all same visual result
  hideGdprBanner: true,
}}
```

produced a calendar that was **near-unreadable on the live site**: the "Select a Date & Time" heading, the month label ("April 2026"), day-of-week headers (SUN/MON/TUE/…), past/disabled date numbers, the "Time zone" label, and the footer links (Privacy Policy, Cookie settings) all rendered in Calendly's internal low-contrast blue-gray, ignoring the `textColor` value we passed.

`primaryColor` (gold on available dates + arrows) *was* honored. `backgroundColor` was honored. Only `textColor` failed to propagate to secondary elements.

## Root Cause
Calendly's embed HTML/CSS applies `pageSettings.textColor` selectively — mostly to the primary event-title block on the left pane. Secondary elements (date headers, weekday labels, time-zone select, footer links) are styled by Calendly's internal CSS with fixed color values that assume a light background. Those colors are not exposed as a pageSettings override. The iframe is cross-origin, so we cannot patch it from outside with CSS.

No combination of `textColor` hex values we tried (pure white `FFFFFF`, brand ivory `F5F0EB`, brand gold `C5A55A`) visibly changed those elements.

## Solution
Stop forcing dark mode. Switch the widget to Calendly's native **light theme** and give it a dedicated light "stage" section in the page layout:

```ts
// BookingClient.tsx
<section style={{ background: "#F5F0EB" }}>    {/* brand ivory stage */}
  …
  <div style={{ backgroundColor: "#FFFFFF", boxShadow: "0 12px 40px rgba(26,26,26,0.08)" }}>
    <InlineWidget
      url={session.url}
      pageSettings={{
        primaryColor: "C5A55A",      // brand gold still applied to selections
        hideGdprBanner: true,
        // NO backgroundColor, NO textColor — Calendly's light-mode defaults handle contrast
      }}
    />
  </div>
</section>
```

The hero section above stays dark; the booking section becomes an intentional tonal break. Session selector cards also switch to light styling (white bg, dark text, gold accent border on active).

## Prevention
**Default Calendly embeds to light theme from the start of a build.** Dark theme is a custom request that the embed API can't fully deliver — building on top of it will require a retheme pass later when the client sees the live page. If the site is dark-brand, pair the light Calendly widget with a dedicated light-stage section behind it (frame it as "the moment we step into the light") rather than fighting the iframe CSS.

Flag for pre-launch auditor: if `pageSettings.backgroundColor` is set to a dark hex and `textColor` is also set, call it out. Screenshot the page header and the month label — if they read dim/blue, the config is broken.

## Related
- [[patterns/calendly-light-stage-section]]
- [[patterns/calendly-inline-embed-brand-colors]] (Pattern #13 — needs an "only for light theme" caveat)
