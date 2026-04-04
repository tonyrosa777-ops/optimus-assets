# Danielle Thompson — Project Retrospective
**Type:** Notary Public + Justice of the Peace — dual-credential service business
**Location:** Gardner, MA (statewide Massachusetts service)
**Completed:** Apr 2026
**Build sessions:** ~4 sessions (estimated from git log boundary commits)

---

## What Went Well

- **Dual-brand positioning** landed cleanly — notary and JP sections visually distinct (navy vs. gold tone) while cohesive under one brand
- **Calendly integration** worked first try — inline embed with brand color params, env var-driven, graceful null fallback
- **OG image** generated natively with `opengraph-image.tsx` + `readFileSync` + `ImageResponse` — no external service, looks great in iMessage/Slack
- **21 testimonials + /testimonials page** added in one session with proper split (notary vs. wedding) and navbar integration
- **Google Maps iframe** (no API key) dropped in cleanly after SVG map was rejected — 60-second fix
- **Resend architecture** (CLIENT_EMAIL env var, per-client account model) set up correctly — will scale
- **constants.ts single source of truth** pattern paid off immediately when client sent corrections — updated in one file, propagated everywhere
- **Domain → Vercel DNS** (GoDaddy A record) set up and resolving within minutes
- Auto-deploy pipeline (GitHub → Vercel) established and stable after git identity fix

---

## What Didn't

| # | Gap | Fix Applied |
|---|-----|-------------|
| 1 | Invented paralegal backstory for bio — client immediately corrected it | Rewrote bio with real background (medical + law enforcement fields) |
| 2 | Base city set to Worcester (wrong) — real base is Gardner | Updated `constants.ts` + all hardcoded instances site-wide |
| 3 | Commission dates, bilingual claim, and expiry year were placeholders never verified | Corrected across 7 files after client review |
| 4 | Custom SVG map built and rejected immediately — client wanted real Google Maps | Replaced with iframe in one edit |
| 5 | Git email mismatch caused Vercel deploy block after pipeline connected | Fixed git config, empty commit to re-trigger |
| 6 | CTABanner props named wrong on /testimonials page — Vercel build failed | Corrected prop names to match component interface |
| 7 | Rate badge overflow — long travel policy text in whitespace-nowrap pill | Shortened to "See travel policy" pointer |
| 8 | Resend free plan 1-domain limit hit — needed separate client account | Each client gets own Resend account |
| 9 | next.config.ts scaffolded instead of next.config.mjs | Renamed — Next.js 14 doesn't support .ts config |

---

## Tools Introduced This Build

| Tool | Use | Notes |
|------|-----|-------|
| Resend | Transactional email for contact form | Per-client account model established |
| Calendly | Inline scheduling embed | Brand color params via URL query string |
| Next.js `ImageResponse` | OG image generation | readFileSync + base64 pattern for local assets |
| Google Maps `output=embed` | Service area map | Legacy format, no API key |
| `next-sitemap` | Sitemap + robots.txt generation | Config at project root |

---

## Changes Made to Toolkit

- Added intake question: base city vs. service area (they differ)
- Added intake question: travel radius + travel pay policy
- Added intake question: commission dates (both notary + JP)
- Added intake question: bilingual Y/N
- Added pre-proposal checklist item: audit all placeholder facts before showing client
- Added rule: client bio must be labeled UNVERIFIED PLACEHOLDER until client confirms
- One Resend account per client — documented in patterns
- constants.ts single source of truth — documented in patterns
