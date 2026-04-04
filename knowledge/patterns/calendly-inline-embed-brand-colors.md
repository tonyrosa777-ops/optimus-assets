# Pattern: Calendly Inline Embed with Brand Color Matching
**Category:** Scheduling / Third-party Integration
**First used:** Danielle Thompson — Apr 2026

## What
Embed Calendly's scheduling widget inline on a page with colors matched to the site's brand palette — no default Calendly purple, seamless visual integration.

## When to Use
- Service business needing online booking (notary, coaching, consulting, etc.)
- Client already has a Calendly account
- Want the embed to feel like part of the site, not a bolted-on widget

## How
```tsx
// src/app/components/sections/CalendlyEmbed.tsx
'use client'
import { useEffect } from 'react'

export default function CalendlyEmbed() {
  const calendlyUrl = process.env.NEXT_PUBLIC_CALENDLY_URL

  useEffect(() => {
    const script = document.createElement('script')
    script.src = 'https://assets.calendly.com/assets/external/widget.js'
    script.async = true
    document.head.appendChild(script)
    return () => { document.head.removeChild(script) }
  }, [])

  if (!calendlyUrl) return null

  const embedUrl = `${calendlyUrl}?hide_gdpr_banner=1&background_color=FAF9F6&text_color=1A1A1A&primary_color=D4870A`

  return (
    <div
      className="calendly-inline-widget"
      data-url={embedUrl}
      style={{ minWidth: '320px', height: '700px' }}
    />
  )
}
```

Store the URL in Vercel env:
```
NEXT_PUBLIC_CALENDLY_URL=https://calendly.com/client-handle
```

Color params (all hex, no `#`):
- `background_color` — widget background
- `text_color` — all text
- `primary_color` — buttons and accents

## Key Rules
- Must be a `'use client'` component — script injection via `useEffect` requires browser
- `NEXT_PUBLIC_` prefix required — this env var is read client-side
- Calendly free tier: 1 event type. $10/mo unlocks separate event types (e.g. Notary vs. Officiant)
- Host gets email notification on every booking automatically — no additional setup needed
- Return `null` if env var not set — graceful degradation during dev

## Reuse Condition
Any service business using Calendly for scheduling.

## Related
None
