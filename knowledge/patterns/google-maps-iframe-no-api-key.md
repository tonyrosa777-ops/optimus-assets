# Pattern: Google Maps Iframe Embed Without API Key
**Category:** Maps / Third-party Integration
**First used:** Danielle Thompson — Apr 2026

## What
Embed a live, interactive Google Maps iframe on any page using the legacy `output=embed` URL format — no API key, no billing account, no setup required.

## When to Use
- Any site needing a service area or location map
- Client doesn't have a Google Cloud account or Maps API key
- Quick deployment needed (no DNS records, no API setup)

## How
```tsx
<iframe
  src="https://maps.google.com/maps?q=Gardner,MA&t=m&z=8&output=embed"
  width="100%"
  height="100%"
  style={{ border: 0 }}
  loading="lazy"
  allowFullScreen
  title="Service area map"
/>
```

Parameters:
- `q=` — search query (city, address, business name)
- `t=m` — map type (m=roadmap, k=satellite, h=hybrid)
- `z=` — zoom level (7=state, 8=regional, 10=city, 13=neighborhood)
- `output=embed` — removes Google Maps UI chrome

## Key Rules
- This is a legacy format Google hasn't officially deprecated but doesn't actively support — it works as of Apr 2026
- For custom styling, polygon overlays, or markers, the Maps JavaScript API (requires key) is needed
- Wrap in a container with explicit height — the iframe needs a fixed height to render
- Add `loading="lazy"` to avoid blocking page load

## Reuse Condition
Any service-area business needing a map. Works until Google deprecates this format.

## Related
None
