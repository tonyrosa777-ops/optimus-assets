# Witt's Restoration LLC — Project Retrospective
**Type:** 24/7 towing, auto body, restoration, and mobile mechanic shop
**Location:** Groveton, NH
**Completed:** 2026-04-12 (demo-ready, pre-launch)
**Build sessions:** 3 sessions (init + sweep + retro fixes + UI polish)

---

## What Went Well
- Zero online competition — dark cinematic theme is a genuine category disruptor in northern NH/VT
- Design system synthesized cleanly from market research; black+gold palette needed zero revision
- Scaffold to demo-ready in a single continuous session (Phases 0–10)
- fal.ai blog images generated successfully on first attempt (10/10, FLUX Schnell)
- Gallery page created quickly with 16 seeded project entries covering all service categories
- ShopTeaser homepage section integrated cleanly with existing seeded Printful product data
- Rising ash canvas animation added consistent ambient motion across all page headers
- Category filters on blog and gallery followed identical pattern — reusable component opportunity

---

## What Didn't
| # | Gap | Fix Applied |
|---|-----|-------------|
| 1 | `text-h1` CSS utility never defined — all page headings rendered tiny | Added utility, then standardized all H1s to `hero-shimmer font-display text-display` |
| 2 | Pricing page included "Google" services Optimus doesn't offer + technical feature names | Removed Google refs, renamed to client-facing names |
| 3 | Duplicate CTA sections (BookingPreview + FinalCTA) back-to-back on homepage | Removed BookingPreview, kept single FinalCTA |
| 4 | Hero primary CTA was "Call Now" (tel: link) — phone belongs in nav, not hero | Changed to "Book Your Free Estimate" → /booking |
| 5 | Shop scaffolded but invisible — not in nav, no homepage presence | Added to nav + ShopTeaser homepage section |
| 6 | fal.ai generated garbled text ("REJUPED") and deformed vehicle in 2 of 10 images | Regenerated with text-free prompts using FLUX Pro v1.1 |
| 7 | Blog and Gallery pages had different bg color than other pages — `<main>` wrapper with inline bg vs fragment root | Switched to fragment roots matching Services/About pattern |
| 8 | Page header structure inconsistent — some had eyebrow+title+subtitle crammed together, others split | Standardized all to Testimonials pattern (heading + subtitle in gradient section) |
| 9 | Blog featured post too large — article grid pushed below fold | Tightened spacing, switched to horizontal 50/50 layout, 3-col grid |
| 10 | RisingAsh canvas only rendered in tiny corner — `offsetWidth` returns 0 on absolute canvas | Fixed to use `parentElement.getBoundingClientRect()` |
| 11 | Build failure: missing closing `}}` in service-area styles after bulk edit | Fixed syntax error in 2 files |

---

## Tools Introduced This Build
- **FLUX Pro v1.1** (`fal-ai/flux-pro/v1.1`) for higher-quality image regeneration (used when Schnell produced artifacts)
- **RisingAsh.tsx** — reusable ambient canvas particle component for page headers (gold particles, ~40 desktop / ~18 mobile, sizes from parent container)

---

## Changes Made to Toolkit
- New Error #42: missing text-h1 CSS utility
- New Error #43: duplicate CTA sections on homepage
- New Error #44: canvas offsetWidth inside fixed container
- New Error #45: pricing page includes non-offered services
- New Pattern #38: fal.ai avoid text in prompts
- New Pattern #39: consistent page header structure
- New Pattern #40: blog index above-fold content
