# Pattern: Blog index must show article grid above the fold
**Category:** UX / Content
**First used:** Witt's Restoration LLC — 2026-04-12

## What
Blog index page spacing must be tight enough that the article grid cards are partially visible on initial page load without scrolling. Users need to see there's more content below the featured post.

## When to Use
Every blog index page on every Optimus build.

## How
- Header section: `py-12 md:py-16` (not py-16 md:py-24)
- Featured post section: `py-6 md:py-8` (not py-8 md:py-12)
- Featured post inner padding: `p-6 md:p-8` (not p-8 md:p-10)
- Article grid section: `py-6` (not py-8 md:py-12)
- Use horizontal side-by-side layout for featured post (image left, text right via `md:grid md:grid-cols-2`) — more compact than full-width hero image
- Use 3-column grid for articles (`lg:grid-cols-3`) not 2-column

## Key Rules
- If the featured post image takes up the entire viewport, nobody scrolls
- Category filter bar goes between header and content (same bg-elevated pattern as gallery)
- Color rhythm: header (dark/gradient) → filters (bg-elevated) → content (bg-base)

## Reuse Condition
Every Optimus build with a blog (all Pro+ builds)

## Related
- Pattern #8: homepage dark/light section rhythm
