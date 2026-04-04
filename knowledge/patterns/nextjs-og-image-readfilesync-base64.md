# Pattern: Next.js OG Image with Local Asset via readFileSync + base64
**Category:** SEO / Social Sharing
**First used:** Danielle Thompson — Apr 2026

## What
Generate a branded Open Graph image at build time using Next.js's native `ImageResponse` API, embedding a local image file (headshot, logo, etc.) by reading it as base64 — no external image hosting or third-party OG image service needed.

## When to Use
- Site has a professional headshot or hero image to feature in link previews
- Want a branded OG card (name, tagline, CTA) for iMessage/Slack/social previews
- No external image CDN or OG generation service available

## How
```tsx
// src/app/opengraph-image.tsx
import { ImageResponse } from 'next/og'
import { readFileSync } from 'fs'
import { join } from 'path'

export const size = { width: 1200, height: 630 }
export const contentType = 'image/png'

export default async function Image() {
  const imageBuffer = readFileSync(join(process.cwd(), 'public/professional-headshot.png'))
  const imageBase64 = `data:image/png;base64,${imageBuffer.toString('base64')}`

  return new ImageResponse(
    (
      <div style={{ display: 'flex', width: '100%', height: '100%' }}>
        {/* Left: brand card */}
        <div style={{ background: '#1B2A4A', flex: 1, display: 'flex', flexDirection: 'column', padding: 60 }}>
          <span style={{ color: '#C9A84C', fontSize: 18 }}>Massachusetts</span>
          <h1 style={{ color: 'white', fontSize: 58 }}>Danielle Thompson</h1>
          {/* CTA button, subtitle, domain */}
        </div>
        {/* Right: headshot */}
        <img src={imageBase64} style={{ width: 480, objectFit: 'cover' }} />
      </div>
    ),
    { width: 1200, height: 630 }
  )
}
```

Wire up in `layout.tsx`:
```ts
openGraph: {
  images: [{ url: '/opengraph-image.png', width: 1200, height: 630 }],
},
twitter: { card: 'summary_large_image', images: ['/opengraph-image.png'] }
```

## Key Rules
- The image must be in `public/` — `readFileSync` uses `process.cwd()` which resolves to the project root
- `ImageResponse` only supports inline styles — no Tailwind, no className
- Keep the base64 image under ~1MB or the `ImageResponse` payload bloats
- The route file must be named exactly `opengraph-image.tsx` (or `.jsx`) to be auto-detected by Next.js App Router

## Reuse Condition
Any site with a client headshot or logo that needs a branded link preview card.

## Related
None
