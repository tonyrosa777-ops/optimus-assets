# Pattern: Dynamic import below-fold heavy components
**Category:** Performance / Bundle Size
**First used:** Goddu Imprint — 2026-05-17

## What
Components rendered in below-fold homepage sections that transitively import heavy deps (framer-motion, react-hook-form, zod, chart libraries, calendar libraries) must be `next/dynamic` imports with `ssr: false`, not static imports. Static imports add the full transitive bundle (~100KB+ gzipped) to the homepage's initial first-load chunk, threatening Lighthouse ≥ 90 budget for a section the user may never reach.

## When to Use
Any homepage section component where ALL three conditions hold:
1. The section renders **below the fold** (section 4+ on a typical homepage with 12 sections)
2. The component transitively imports a heavy dep — typical offenders: framer-motion (~60KB gz), react-hook-form (~20KB gz), zod (~12KB gz), chart libraries (~50KB+ gz), calendar libraries, 3D renderers, video players
3. The component is **interactive only when the user scrolls to it** — not visible above the fold, not required for first-paint SEO

Mandatory for the homepage's BookingPreview / BookingCalendar pattern (Stage 1J BUG-6 fix). Apply to any below-fold equivalent: shop teaser, quiz teaser, video embed, interactive chart, complex carousel.

## How

The bad pattern (static import):
```tsx
// src/components/sections/BookingPreview.tsx — Server Component
import BookingCalendar from "@/components/BookingCalendar";

export function BookingPreview() {
  return (
    <Section tone="base" id="booking-preview">
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-10 items-center">
        {/* Left: copy + CTAs */}
        <FadeUp>...</FadeUp>
        {/* Right: inline calendar */}
        <ScaleIn>
          <BookingCalendar />
        </ScaleIn>
      </div>
    </Section>
  );
}
```

`BookingCalendar.tsx` transitively imports framer-motion + react-hook-form + zod. The static import means all three land in the homepage's initial JS bundle even though the calendar renders in section 11 of 12.

The fix:

```tsx
// src/components/sections/BookingPreview.tsx
"use client";

import dynamic from "next/dynamic";
import { Container } from "@/components/ui/Container";
import { Eyebrow } from "@/components/ui/Card";
import { Section } from "@/components/ui/Section";
import { Button } from "@/components/ui/Button";
import { FadeUp } from "@/components/animations/FadeUp";
import { ScaleIn } from "@/components/animations/ScaleIn";

const BookingCalendar = dynamic(() => import("@/components/BookingCalendar"), {
  ssr: false,
  loading: () => (
    <div
      className="rounded-2xl border min-h-[420px] flex items-center justify-center"
      style={{
        background: "var(--bg-card)",
        borderColor: "var(--border-dark)",
        color: "var(--text-muted)",
      }}
      aria-label="Loading booking calendar"
    >
      <span className="font-mono text-xs uppercase tracking-widest">
        Loading availability...
      </span>
    </div>
  ),
});

export function BookingPreview() { /* unchanged JSX */ }
```

## Key Rules
- **`ssr: false` is mandatory for bundle savings.** `dynamic(...)` without `ssr: false` still server-renders the calendar AND ships its JS chunk in the initial manifest because hydration requires it — so the bundle stays the same. With `ssr: false`, the calendar JS only loads when the section enters the viewport (or hydration completes for client-side route changes).
- **`ssr: false` requires Client Component context.** App Router constraint: `dynamic({ ssr: false })` cannot be called from a Server Component. The parent section component must declare `"use client"` at the top. Acceptable trade-off for below-fold sections: SSR for SEO/initial-paint is not critical for a booking widget below the fold.
- **Loading skeleton uses design tokens.** Inline-style position/dimensions are layout-only; color/border/background MUST reference CSS custom properties (`var(--bg-card)`, `var(--border-dark)`, `var(--text-muted)`) so the skeleton stays on-brand. Do not hardcode hex.
- **Loading skeleton must reserve the height.** Use `min-h-[420px]` (or the calendar's actual rendered height) to prevent layout shift when the dynamic chunk loads. CLS impact on Lighthouse is real.
- **Don't dynamic-import above-fold components.** Hero, primary CTA, first-pain-points section — these need static imports for SSR + immediate hydration. Dynamic imports for above-fold = layout shift + slower LCP, the opposite of the optimization.

## Reuse Condition
Apply to every Optimus build's homepage where the homepage renders 6+ sections AND any below-fold section imports a 60KB+ gz transitive dep. Specifically:
- BookingPreview (every build with a custom BookingCalendar) — mandatory
- Shop teaser if it imports cart drawer + Stripe SDK
- Interactive blog preview if it imports a video player or carousel library
- Embedded calculator widgets

For each candidate component, check the transitive bundle weight:
```bash
cd web && npx next build && npx next-bundle-analyzer
```

If a below-fold component contributes >50KB gz to the homepage chunk, convert to dynamic import.

## Pre-launch-auditor SECTION 9 addition
Stage 1H pre-launch-auditor SECTION 9 (Performance) currently flags Lighthouse score as "manual check required." Add a file-level pre-check: grep `src/components/sections/*.tsx` for static imports of components in `src/components/` whose own imports include `framer-motion`, `react-hook-form`, `zod`, `recharts`, `react-player`, or similar heavy deps. WARN if any below-fold section static-imports such a component.

## Goddu Imprint trace
- BUG-6 from `/optimus-review` run-1: BookingPreview (section 11 of 12) static-imported BookingCalendar pulling ~100KB+ gz into homepage initial bundle.
- Fix (commit ef6ac5a): converted BookingPreview to Client Component + `dynamic({ ssr: false })` with branded loading skeleton.
- Run-3 verifier confirmed clean — no new performance findings.

## Related
- Pattern #34 (vault build-log) — clamp responsive type scale (same Phase 1 globals.css discipline)
- Pattern [[stage-1j-pre-launch-gate]] — the gate that catches misses of this pattern
- Pattern [[iterate-to-clean-n-run-review]] — the workflow that verifies the fix landed clean
