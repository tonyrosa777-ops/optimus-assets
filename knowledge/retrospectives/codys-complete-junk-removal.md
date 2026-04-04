# Cody's Complete Junk Removal — Project Retrospective
**Type:** Junk removal contractor (local service business)
**Location:** Dracut, MA / Greater Lowell / Middlesex County
**Completed:** Apr 2026
**Stack:** Next.js 14 (App Router) + Tailwind CSS + TypeScript + Vercel
**Build sessions:** ~2 sessions (estimated from git log density)

---

## What Went Well

- **Firecrawl site capture** replaced the content questionnaire entirely — all copy, pricing, FAQs, testimonials, and contact info lifted from the existing WordPress site in 2 scrape calls. Zero back-and-forth with client.
- **Market research document** (`Intelligence-Market-Research.md`) was dense and directly actionable — competitive weaknesses in the local market were translated directly into site decisions (omnipresent phone number, transparent pricing, review-first positioning).
- **Hero animation split** (server content + client `HeroEffects`) kept the `"use client"` boundary tight while delivering electric bolt / particle effects without Framer Motion overhead.
- **Calendly widget** built and wired on first attempt using the established `calendly-inline-embed-brand-colors` pattern.
- **30 real Google reviews** sourced and structured into the testimonials array — the reviews section launched with real social proof.
- **Blog architecture** shipped with 10 launch posts, all SEO-optimized for local junk removal keywords.
- **12 service pages + 6 service area pages** built with schema markup — local SEO foundation stronger than any competitor in the market.
- **Static Printful merch shop** populated with real catalog data (correct product names, base costs, retail markup) in advance of client setting up their Printful account.

---

## What Didn't

| # | Gap | Fix Applied |
|---|-----|-------------|
| 1 | Printful CDN image URLs fabricated for products without confirmed scrape URLs → would 404 in prod | Replaced with Unsplash placeholders; kept only 3 confirmed CDN URLs |
| 2 | No global `.gitconfig` on Windows — git identity missing, commit would fail | Set per-repo `git config user.name/email` before first commit |
| 3 | No `CLAUDE.md` or `progress.md` created — retro had no project variables file to read | Reconstructed from git log + TODO.md; gap flagged for next project |
| 4 | Shop scope changed mid-session (Growth package removed shop, then Printful shop added back) — created unnecessary churn | Scope decision should be locked at intake before any code is written |

---

## Tools Introduced This Build

- **Firecrawl (`firecrawl_scrape`)** — first time used as a content capture / project brief tool (previously used for competitive research only)
- **CSS keyframe SVG lightning bolts** — pure CSS animated SVG paths with `drop-shadow` glow; no canvas, no GSAP

---

## Changes Made to Toolkit

- Added error: `printful-cdn-image-url-fabricated.md`
- Added error: `no-global-gitconfig-windows.md`
- Added pattern: `firecrawl-existing-site-capture.md`
- Added pattern: `hero-server-client-animation-split.md`
- Added pattern: `static-printful-merch-data-file.md`
- Workflow gaps flagged: CLAUDE.md creation not enforced at project start; shop scope lock missing from intake
