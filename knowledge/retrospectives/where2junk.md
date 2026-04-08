# Where2 Junk Removal Services LLC — Project Retrospective
**Type:** Local residential & commercial junk removal service
**Location:** Manchester, NH
**Completed:** 2026-04-05 (active build — demo-ready, pre-launch)
**Build sessions:** ~6 sessions estimated from git log (75+ commits)

---

## What Went Well

- **Hero truck animation landed on first approved concept** — custom JS canvas dump truck with CSS speed lines + radial glow, completed in ~8 iteration commits before approval. Faster than Placed Right Fence (9+ iteration commits).
- **Full Pro package build** — blog (10 articles), interactive quiz with lead capture, automated booking calendar, service area pages (8 NH cities), pricing page, gallery, shop, Resend email wiring, SEO/JSON-LD — all completed without a structural rework.
- **Printful+Stripe shop ported directly from andrea-abella-marie** — cart context, CartDrawer, ShopClient, API routes all transferred and adapted in one session. Seeded fallback JSON handled the no-Printful-account state cleanly.
- **Demo booking calendar** — hash-based seeded availability replaced the static "Calendly not configured" placeholder. Fully interactive without backend. Calendly silently integrates when URL is set. New pattern documented.
- **fal.ai images on-demand** — generated 2 missing blog card images mid-session using `scripts/generate-blog-images.ts` without leaving context. Pattern established for all future blog image gaps.
- **Nav evolution handled gracefully** — 3 nav iterations (click-dropdown → hover/click hybrid → More overflow) without breaking changes. Final state: hover-open for Services/Service Areas, click-navigate to parent pages, More dropdown for secondary links.

---

## What Didn't

| # | Gap | Fix Applied |
|---|-----|-------------|
| 1 | `preview_image_url: null` in seeded JSON caused TS build error — `null` ≠ `undefined` | Omitted field from all seeded entries; absent key = `undefined` in TS |
| 2 | `/areas/page.tsx` prerender crash — Server Component had `onMouseEnter`/`onMouseLeave`; standard fix (`'use client'`) blocked by `metadata` export | Used CSS `:hover` rules in `<style>` block instead of JS event handlers |
| 3 | Nav "Services" button opened dropdown but never navigated to `/services` — user had to find "View All Services" in dropdown | Replaced click-toggle `<button>` with hover-open container + `<Link href="/services">` |
| 4 | `/areas` route didn't exist when Service Areas became a clickable nav link | Created `/areas/page.tsx` index with city card grid + booking CTA |
| 5 | Mobile hero text sat mid-screen — `min-h-screen + flex items-center` centers content vertically | Changed to `items-start lg:items-center` + tightened mobile top padding clamp |
| 6 | Quiz email field was optional — user removed the "(optional)" label requirement | Added `required` attribute + email format validation in `handleSubmit` |
| 7 | Booking page showed "Calendly URL not configured" static fallback — unusable for demo | Built full 4-step interactive demo calendar with seeded availability |
| 8 | progress.md never updated after Session 5 — all subsequent build phases undocumented | Retrospective reconstructed from git log and session summary |

---

## Tools Introduced This Build

| Tool | First Used For |
|------|---------------|
| `@fal-ai/client` (not `@fal-ai/serverless-client`) | Blog card image generation — newer SDK, same pattern |
| `@fal-ai/client` + `scripts/generate-blog-images.ts` | On-demand mid-session image generation without leaving context |
| Hash-based seeded availability | Demo booking calendar without scheduling backend |
| CSS `:hover` in `<style>` block | Server Component hover effects when `'use client'` is blocked by metadata export |

---

## Changes Made to Toolkit

| File | Change |
|------|--------|
| `knowledge/errors/json-null-vs-typescript-undefined-seeded-data.md` | New — null vs undefined in seeded JSON |
| `knowledge/errors/server-component-hover-metadata-constraint.md` | New — CSS hover variant when metadata blocks 'use client' |
| `knowledge/patterns/demo-booking-calendar-seeded-availability.md` | New — hash-based demo calendar pattern |
| `knowledge/patterns/hover-open-click-navigate-nav-dropdown.md` | New — hover to open, click to navigate, for category nav items |
| `knowledge/patterns/more-overflow-dropdown-desktop-nav.md` | New — ≡ More button for crowded 8+ link nav |
| `build-log.md` | 2 errors + 3 patterns + 1 retrospective row added |

---

## Open Items at Retro Time

These are NOT build failures — they are pending client actions before launch:

- `NEXT_PUBLIC_CALENDLY_URL` — Joshua needs to create Calendly account
- `RESEND_API_KEY` — Joshua needs to verify where2junk.com in Resend
- `STRIPE_SECRET_KEY` + `NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY` — needed for live shop checkout
- Real photography — fal.ai placeholders throughout until Joshua provides job photos + headshot
- Instagram handle — unknown; social link conditional on this
- Email confirmation: `hello@where2junk.com` assumed, needs client confirmation
