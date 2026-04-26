# Pricing — Website Development

Three tiers. Same on every build. Never customized per client. The Pro tier carries the "Most Popular" badge; Starter and Premium are anchors that exist to make Pro feel like the obvious choice.

## Tiers

### Starter — $1,500

Core pages. Canvas + SVG animated hero. FAQ page.

- Homepage with the full 3-layer hero (HeroParticles + brand canvas + Framer Motion stagger)
- Services overview + individual service pages
- About page
- Contact page
- FAQ page
- All built on the same Next.js + Tailwind 4 + Framer Motion foundation as the higher tiers

### Pro — $3,000 (MOST POPULAR)

Starter, plus the conversion engine. This is the sell.

- Professional Blog (9-10 articles minimum, full SEO/AEO foundation)
- Lead-Capture Quiz (8-question max, 4 archetypes, scored result, inline booking on result screen)
- Automated Booking Calendar (custom-branded UI, Calendly API backend, demo-mode fallback)
- Photo Gallery
- Testimonials Showcase (36 testimonials, paginated 9 per page across 4 pages)

### Premium — $5,500

Pro, plus commerce. Premium never gets a badge. Its job is to make $3,000 feel reasonable.

- Branded Merch Shop (Printful + Stripe + cart drawer, fully scaffolded with seeded fallback)

## Client-facing feature names

Use these labels exactly. They describe what the client gets, not how it's built.

| Use this label | Never use this |
|---|---|
| Automated Booking Calendar | inline booking calendar / custom calendar |
| Lead-Capture Quiz | interactive quiz / quiz funnel |
| Professional Blog | blog architecture / Sanity blog |
| Branded Merch Shop | shop scaffold / Printful integration |
| Testimonials Showcase | testimonials page |
| Photo Gallery | gallery page |

## The pricing page is a sales tool

The `/pricing` page is built into every demo. It is in the nav bar throughout the entire build. It is deleted before launch by the pre-launch-auditor agent — the live client site never has a `/pricing` route. The nav link displays in amber with a `⬥ Pricing` marker so anyone viewing the demo can see it is an internal Optimus tool, not a client-owned page.

Required components on the page:
1. Three tier cards with feature lists. Price only. No deposit math.
2. ROI Calculator: two sliders (avg job/project value + clients per month) + package selector → outputs monthly revenue, break-even timeline, 12-month ROI per tier.
3. Full comparison chart: feature rows grouped by category (Foundation / Conversion / Content & SEO / Commerce / Support), checkmarks per tier.
4. CTA on each tier opens the booking calendar inline. Never links away.

## Never on the page

> **Hard rules. Build failure if violated.**
>
> - **No "deposit," "upfront," or any payment-split language.** The price on the page is the price. Anthony offers deposit splits verbally as a backup close. It is never on the page.
> - **No Google services on any tier.** Not "Google Business Profile optimization," not "Google Ads setup," not "Google Analytics," not any Google product. Optimus does not offer Google services. If the word "Google" appears on the pricing page, it is a build failure.

---

#offering/website-dev #status/active
