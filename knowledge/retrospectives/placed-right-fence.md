# Placed Right Fence Co. LLC — Project Retrospective

**Type:** Family-run residential fence installation and repair contractor
**Location:** Nashua, NH (Southern NH and Seacoast)
**Completed:** Apr 2026 (in progress — hero + homepage locked, secondary pages pending)
**Build sessions:** ~7 sessions (Apr 2026)

---

## What Went Well

- **Black + gold rebrand landed immediately** — the initial light/cream design system was discarded early once it became clear that the business card was black and gold. The rebrand commit (`901cf74`) was clean and decisive. No half-measures.
- **fal.ai image generation extended Pattern #4** — gallery hero photos (wood/vinyl/aluminum), blog post images (10 articles), and gallery page grid all generated with no client photography. Saved multiple sessions.
- **ForgeCanvas animation is genuinely distinctive** — a custom canvas 2D fence-forging animation (particles → forge flash → picket extrusion → rail draw) is the kind of hero that gets shown to other business owners. No Three.js, no GSAP, pure rAF + Canvas API.
- **Blog shipped static without Sanity** — 10 SEO articles shipped as static Next.js pages with `STATIC_AS_POSTS` mapper. Sanity was wired in parallel but not required. Build never blocked.
- **30 testimonials with pagination** — not 6. Competitive differentiation starts with depth. Marquee + paginated dedicated page.
- **Shop (Stripe + Printful + Resend) fully scaffolded** — plug 3 keys to go live. Rare to have a functional merch store on a fence contractor site.
- **Service areas page redesign** — dark hero, stats row, region cards with city counts, dark "Why Local" section with CountUp. One of the stronger secondary pages built to date.
- **Pricing psychology applied correctly** — 3-tier with Growth as unambiguous hero, premium badge removed after user caught it.

---

## What Didn't

| # | Gap | Fix Applied |
|---|-----|-------------|
| 1 | Hero went through 4 full concepts before final (AI images → video → text particle → canvas forge) | Canvas ForgeCanvas kept; prior concepts committed and left as reference |
| 2 | Mobile canvas animation took 9+ commits to calibrate (fullH, groundY, items-center vs items-start) | Math.min(H*0.78, 700) cap + viewport-height-aware fullH locked the values |
| 3 | groundY broke silently after hero flex alignment changed from items-center to items-start | items-start + recalibrated groundY; values saved to persistent memory as LOCKED |
| 4 | Desktop fullH started at 148, should have been ~240 — took a separate session to identify | fullH: 240 set and locked at user approval |
| 5 | Sanity Studio SSR crash with Turbopack — createContext boundary | Two-file pattern: StudioClient extracted as `use client` + dynamic(ssr:false) |
| 6 | Gallery page blank on client navigation | Specific fix in commit c831812 — likely a missing client directive on filter component |
| 7 | Dark/light section rhythm not planned upfront — 3 sections had to be flipped mid-build (Blog, Trust, FAQ) | Now documented as a pattern: plan rhythm before building any section |
| 8 | Nav had wrong PRIMARY_HREFS set initially (services/gallery/about instead of services/gallery/blog/shop) | Corrected in Session 6; nav planning should happen in intake |
| 9 | "Full Service" badge on premium tier not caught until user flagged it | Removed; 3-tier anchoring psychology now documented as a pattern |

---

## Tools Introduced This Build

| Tool | Use | Notes |
|------|-----|-------|
| Canvas 2D rAF animation | Custom forge hero animation | No Three.js required for 2D particle + extrusion work |
| fal-ai/flux-pro/v1.1 | Gallery + blog image generation | Extended from Enchanted Madison Pattern #4 |
| Web3Forms | Contact form delivery | Free tier, no backend, leads to email/phone |
| Sanity (embedded Studio) | Blog CMS | Wired but not activated — awaiting client env vars |
| Stripe + Printful + Resend | Shop POD fulfillment | First fence contractor merch implementation |

---

## Sales Notes (from closing meeting with Jen, Apr 2026)

**Package sold:** Complete build (premium tier) — client anticipated ~$4k, closed at/above that.

**What closed the deal:**
- ForgeCanvas animation was the "wow" moment — shown to the business partner Roger before even seeing full demo
- ROI calculator presented immediately before pricing: 8 leads/month × 50% conversion × $5,200 avg = $130k/year = 2,623% ROI
- No monthly fees positioning: "A lot of agencies charge 15k then 500/month — you can never leave. You own this from day one."
- Tax write-off close: credit card → business expense → reduces tax bill by package price

**Pain points surfaced that helped close:**
- Their existing site's contact form wasn't sending email notifications — they nearly missed a real lead (found it by accident checking Yelp stats)
- Jen said "I am not a coder" — sold the support/handholding component hard

**Invoice sent during the meeting.** Client committed to paying Friday when credit card cleared.

**Upsell pipeline planted:**
- Phase 2 (marketing/ads) mentioned briefly: "Once we're launched, we'll start talking"
- Phase 3 (automation) introduced when Jen asked about "additional fees" — separate packages, details to follow post-launch

**Key quote to remember:**
> "This is our foundation. There's still so much we can build."

---

## Changes Made to Toolkit

- Added [[errors/canvas-animation-breaks-after-hero-flex-change]]
- Added [[errors/mobile-viewport-height-variance-clips-canvas-animation]]
- Added [[errors/sanity-studio-ssr-crash-createcontext-turbopack]]
- Added [[patterns/responsive-canvas-animation-breakpoint-layout]]
- Added [[patterns/hero-concept-iteration-budget]]
- Added [[patterns/homepage-dark-light-section-rhythm]]
- Added [[patterns/pricing-three-tier-anchoring]]
- Created `knowledge/patterns/` directory (first patterns in vault)
