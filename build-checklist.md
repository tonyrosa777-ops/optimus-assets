# Optimus Build Checklist
# Follow every line. Do not skip. Check each box when done.
# Steps marked [AGENT →] will eventually be handled by a validated agent.
# Until the agent is built and VALIDATED, do the step manually.

---

## PHASE 0 — CLIENT ONBOARDING (before any code)

[ ] 1. Run discovery session with client. Capture raw notes or voice transcript.
[ ] 2. Open Claude.ai Desktop (Projects). Paste raw notes + intake-prompt.md contents.
        → Output: initial-business-data.md (all 8 sections filled, ⚠️ flags resolved)
[ ] 3. Open Claude.ai Desktop. Paste initial-business-data.md + market-research-prompt.md.
        → Output: market-intelligence.md (all 9 sections filled, competitors named, gaps identified)
        [AGENT → market-researcher.md will replace this step once VALIDATED]
[ ] 4. Confirm both files have no ⚠️ NOT FOUND flags before proceeding.
        If any remain: contact client, fill gaps, then continue.

---

## PHASE 1 — PROJECT SETUP

[ ] 5.  Create new project folder: C:\Projects\[ClientName]\
[ ] 6.  Copy these 6 files from C:\Projects\Optimus Assets\ into the new folder:
          - CLAUDE.md
          - project-prime.md
          - frontend-design.md
          - website-build-template.md
          - initial-business-data.md   ← the filled version from Phase 0
          - market-intelligence.md     ← the filled version from Phase 0
[ ] 7.  Open the project folder in VS Code.
[ ] 8.  In the VS Code terminal, run: claude
[ ] 9.  In the Claude Code terminal, run: /new-client
          NOTE: Do not skip even if files are pre-filled.
          This step extracts CLAUDE.md variables and creates .claude/commands/prime.md.
          Without it, /prime breaks.
[ ] 10. Review Phase 4 summary output. Verify all 10 variables are correct.
          Type GO to scaffold the project.
          Type STOP to review and correct a variable first.
[ ] 11. Wait for scaffold to complete. Verify these folders/files exist:
          - /src/app/page.tsx
          - /src/components/
          - /src/data/site.ts
          - /public/
          - package.json
          - tailwind.config.ts
          - globals.css (with design tokens)

---

## PHASE 2 — GITHUB + VERCEL

[ ] 12. Initialize git and push to GitHub:
          git init
          git add .
          git commit -m "feat(scaffold): initial project scaffold"
          gh repo create [client-name] --private --push --source=.
[ ] 13. Go to vercel.com → New Project → Import the repo
          Framework Preset: Next.js
          Root Directory: web  (or whatever subfolder Claude created)
          Environment Variables: skip for now, add in Phase 11
[ ] 14. Confirm Vercel build succeeds (green checkmark). Fix any build errors before continuing.

---

## PHASE 3 — DESIGN SYSTEM + HERO (Session 1)

[ ] 15. In Claude Code terminal, run: /prime
          This starts Phase 1. Run /prime at the start of EVERY session going forward.
[ ] 16. Confirm design-system.md exists and is filled (palette, typography, tone, brand personality).
          If missing: ask Claude to create it now from market-intelligence.md + initial-business-data.md.
[ ] 17. Build the hero section. Get approval on:
          - Animation type (Canvas / SVG / CSS — matched to brand personality in design-system.md)
          - Headline and tagline (pulled from /data/site.ts)
          - CTA pair (primary + secondary)
          - Color palette rendering correctly
          NOTE: Do not calibrate mobile hero until desktop is locked. This wastes commits.
[ ] 18. Build the navigation (desktop + mobile).
          Verify: all nav links point to existing routes. No broken links at this stage.
[ ] 19. Build the footer (links, social icons, legal copy, schema address).
[ ] 20. Commit: feat(layout): nav, hero, footer locked
[ ] 21. Run /prime to start Session 2.

---

## PHASE 4 — HOMEPAGE SECTIONS (Session 2)

Build all homepage teaser sections. Every section links to its full page.
[AGENT → frontend-developer.md and content-writer.md will run in parallel here once VALIDATED]

[ ] 22. Pain Points section (4 cards, 2x2 grid, empathy — no CTA)
[ ] 23. Founder / About teaser (2-3 paragraphs + photo placeholder + link to /about)
[ ] 24. Services preview (3 cards → link to /services)
[ ] 25. Stats row (CountUp animations — 3 key numbers from market-intelligence.md)
[ ] 26. Testimonials section (3-4 featured quotes — NO em dashes in quote text)
[ ] 27. Quiz CTA section ("Not sure where to start?" → /quiz)
[ ] 28. Blog preview (3 latest posts — placeholder cards until blog is built in Phase 7)
[ ] 29. Booking preview (Calendly widget inline OR placeholder until Phase 9)
[ ] 30. Final CTA (last chance conversion block — headline + primary CTA button)
[ ] 31. Verify homepage dark/light section rhythm: no 3 consecutive same-background sections.
[ ] 32. Test on mobile (390px). Fix any overflow or alignment issues.
[ ] 33. Commit: feat(homepage): all sections complete

---

## PHASE 5 — CORE PAGES (Session 3)

[ ] 34. /about page — Full founder story, credentials list, photo, stats row, CTA
[ ] 35. /services page — Service cards with 1-line tagline each → link to individual pages
[ ] 36. /services/[slug] pages — One page per service:
          Hero (service name, who it's for, CTA)
          What you get (bullet list with icons)
          Who it's for (3 persona cards)
          How it works (numbered steps)
          Service-specific testimonials
          FAQ (Radix accordion, 5-7 questions)
          Final CTA
[ ] 37. /contact page — Form (React Hook Form + Zod), Google Maps iframe centered on service area,
          contact info (phone, email, address/region), business hours if applicable
[ ] 38. /faq page — Full FAQ with Radix accordion, all top objections from market-intelligence.md
[ ] 39. Add all new routes to navigation and sitemap.ts in the SAME commit. (Page Wiring Rule)
[ ] 40. Commit: feat(pages): about, services, contact, faq complete

---

## PHASE 6 — NICHE-SPECIFIC PAGES (Session 3 continued)

Build all that apply to this business type. Leave none out that fit.

[ ] 41. SERVICE AREA PAGES (local businesses — contractors, consultants, regional service providers)
          One page per city/region served. Minimum 3, up to 10.
          Each page: local H1, local testimonials if available, Google Maps iframe for that city,
          schema LocalBusiness with that city's address, unique meta description.
          Add all to navigation dropdown and sitemap.ts.

[ ] 42. PRICING PAGE (service businesses — coaches, consultants, professionals)
          3-tier anchoring (Starter / Growth / Complete or equivalent).
          Growth tier gets "Most Popular" badge. Premium tier gets NO badge — it anchors.
          ROI calculator component (dev-only — gated by NEXT_PUBLIC_SHOW_PRICING_TOOLS=true).
          Remove ROI calculator before launch.

[ ] 43. REVIEWS / TESTIMONIALS PAGE (any business with 10+ testimonials)
          Featured quote full-width at top.
          Full grid below — all testimonials from site.ts.
          Filter by program/service type (URL params).

[ ] 44. QUIZ PAGE (/quiz)
          Multi-step: problem selection → goal → state/location → lead capture form → result.
          Result shows the recommended service + booking CTA.
          Quiz answers appended to contact form submission (sent to Resend).

[ ] 45. Commit: feat(niche-pages): [list which pages were built]

---

## PHASE 7 — BLOG / KNOWLEDGE BASE (Session 4)

SEO and AEO live here. This phase is non-negotiable — always built on every project.
[AGENT → blog-architect.md will handle Sanity schema + article generation once VALIDATED]

[ ] 46. Deploy Sanity schema: npx sanity deploy
          Schema fields: title, slug, publishedAt, mainImage, excerpt, categories, body, seo
[ ] 47. Write 9-10 blog articles targeting the gap topics from market-intelligence.md Section 5.
          Article requirements:
          - Each article answers ONE specific question a buyer has (not a general topic)
          - H1 is the exact question (e.g., "What Does an Honorary Consul Actually Do?")
          - First paragraph: direct 2-sentence answer (AEO: AI systems quote the first clear answer)
          - Body: detailed explanation with subheadings
          - Every article closes with a CTA to book/contact
          - No em dashes in article text
          AEO schema on every article: Article schema + FAQ schema (if article contains Q&A)
[ ] 48. Categories to cover (customize per niche — these are the standard Optimus set):
          - "[Business type] explained" (what do they do, who needs them)
          - "Process / how it works" (step by step)
          - "[Service A] vs. [Service B]" (decision guide for confused buyers)
          - "Who qualifies / who is this for"
          - "Pricing / what does it cost"
          - "Common mistakes / what to avoid"
          - "Local guide" (niche + location — highest local SEO value)
          - "FAQ mega-post" (top 20 questions compiled)
          - "[Niche] checklist" (what to bring, what to prepare)
[ ] 49. Build blog index page:
          Featured post (full-width card, first/pinned post)
          Post grid (3-col desktop, 1-col mobile)
          Category filter tabs
          Newsletter signup CTA at bottom
[ ] 50. Build blog post template (/blog/[slug]):
          Hero image, title, date, category badge, reading time
          PostBody (Portable Text → semantic HTML)
          Sidebar: TableOfContents (sticky), Author card, Related posts
          Newsletter signup at end of post
[ ] 51. Verify: each article has unique meta title, meta description, and OG image.
[ ] 52. Commit: feat(blog): Sanity schema, [N] articles, index + post template

---

## PHASE 8 — SHOP (Session 4-5)

The shop is ALWAYS scaffolded on every project. The decision is whether to wire APIs.
That decision happens IMMEDIATELY after scaffold — before any API key is touched.
[AGENT → shop-builder.md will handle this phase once VALIDATED]

### 8A — Scaffold (always, every project)

[ ] 53. Populate /src/data/shop.ts with placeholder product data:
          - Product names, base cost, retail markup (real numbers if known, placeholders if not)
          - Unsplash placeholder images
          - Printful sync IDs left blank until decision gate below
[ ] 54. Build cart context (/src/lib/cart.tsx) — custom React Context, NOT Snipcart.
          Cart persists to localStorage. CartDrawer in SiteHeader (not layout).
[ ] 55. Build shop page (UI only — no live API calls yet):
          Page hero, category filter tabs, product grid (3-col / 2-col / 1-col)
          ProductCard: image, badge, name, price, description, variant picker, Add to Cart
          Skeleton loaders while variants fetch
          ?success=true query param → success toast after Stripe return
[ ] 56. Build /api/stripe/checkout, /api/stripe/webhook, /api/printful/* route files.
          Scaffold the routes fully. Do NOT add any API keys or real credentials yet.
[ ] 57. Commit: feat(shop): shop scaffold complete — UI, cart, route stubs

### 8B — DECISION GATE: Did the client purchase the premium tier (shop included)?

          [ ] YES → proceed to Step 58 (wire APIs)
          [ ] NO  → proceed to Step 58-DELETE (delete shop entirely, then skip to Phase 9)

          ⚠️ DELETE PATH (client did not purchase premium):
          [ ] 58-DELETE. Delete all shop files:
                - /src/app/shop/ (entire directory)
                - /src/app/api/stripe/ (entire directory)
                - /src/app/api/printful/ (entire directory)
                - /src/lib/cart.tsx
                - /src/data/shop.ts
                - CartDrawer from SiteHeader
                - Shop link from navigation
                - Shop teaser from homepage (if added)
          [ ] 59-DELETE. Commit: chore(shop): removed shop — not in client scope
          [ ] 60-DELETE. Skip to Phase 9. Do NOT add any Stripe, Printful, or Resend shop env vars.

### 8C — API Integration (only if client purchased premium)

[ ] 58. Configure Printful account: create products, set retail prices, generate mockups.
[ ] 59. Fill /src/data/shop.ts with real product data:
          - Correct Printful sync product IDs
          - Real product names, base cost, retail markup, actual mockup images
[ ] 60. Wire /api/stripe/checkout route (POST):
          Always include: customer_creation: "always", absolute HTTPS image URLs,
          cart in metadata.cart as JSON
[ ] 61. Wire /api/stripe/webhook route (POST):
          Verify Stripe signature. Split cart by POD vs manual fulfillment.
          POD items → Printful API. Manual items → Resend owner alert.
[ ] 62. Wire /api/printful/products and /api/printful/variants/[id] routes.
          Use KNOWN_COLORS lookup for variant parsing (not position-based).
[ ] 63. Commit: feat(shop): Stripe + Printful + Resend APIs wired

---

## PHASE 9 — BOOKING / SCHEDULING

[ ] 64. Client sets up Calendly account with their availability and event types.
[ ] 65. Copy the Calendly event URL.
[ ] 66. Add to Vercel env vars: NEXT_PUBLIC_CALENDLY_URL=https://calendly.com/[client]/[event]
[ ] 67. Build BookingWidget component (Calendly inline embed with brand color URL params).
[ ] 68. Embed on /booking page AND as homepage teaser section.
          Confirm no redirect — widget stays on the site domain (traffic retention rule).
[ ] 69. Test: submit a booking. Confirm confirmation email arrives to client.
[ ] 70. Commit: feat(booking): Calendly inline widget wired

---

## PHASE 10 — SEO + AEO LAYER (Session 5)

Run this phase after all pages and blog articles are built. Always run — never skip.
[AGENT → seo-aeo-specialist.md will run this phase as a dedicated pass once VALIDATED]

[ ] 71. Schema markup on every page (add to page.tsx metadata or JSON-LD component):
          Homepage: LocalBusiness / ProfessionalService / LodgingBusiness (match SCHEMA_TYPE in CLAUDE.md)
          Blog posts: Article schema + FAQ schema (if applicable)
          Service pages: Service schema
          Contact page: LocalBusiness with address, phone, hours
[ ] 72. Meta tags: every page has unique title tag (under 60 chars) + meta description (under 160 chars).
[ ] 73. OG images: generate for homepage + all major pages using Next.js native opengraph-image.tsx.
          Use readFileSync for local logo asset as base64 (see pattern #12 in build-log.md).
[ ] 74. Sitemap: run next-sitemap or generate sitemap.ts with all routes.
[ ] 75. robots.txt: allow all crawlers, disallow /studio (Sanity CMS).
[ ] 76. AEO checks:
          [ ] Every blog article H1 is a specific question (not a vague topic)
          [ ] Every article has a direct 2-sentence answer in the first paragraph
          [ ] FAQ schema on all FAQ-format pages and applicable blog posts
          [ ] Business entity clearly defined: name, owner name, location, phone, email, schema
          [ ] Google Business Profile created or updated (client handles this separately)
[ ] 77. Heading hierarchy check: every page has exactly ONE H1. Subheadings use H2/H3 correctly.
[ ] 78. Commit: feat(seo-aeo): schema, meta, OG images, sitemap, robots

---

## PHASE 11 — CLIENT ONBOARDING INFRASTRUCTURE

[ ] 79. Create client's Resend account (resend.com, free tier):
          Use client's business email. Note credentials for handoff.
[ ] 80. In Resend: add the client's domain → Auto-configure DNS (signs into GoDaddy, sets DKIM + SPF).
[ ] 81. In Resend: API Keys → Create API Key → copy immediately (only shown once).
[ ] 82. Add to Vercel: RESEND_API_KEY=[key]
[ ] 83. Test contact form: submit → verify email arrives in client's inbox within 30 seconds.
          If not: check Resend → Emails tab for error.
[ ] 84. Connect domain to Vercel:
          Vercel → Project → Settings → Domains → Add [clientdomain.com] and www.[clientdomain.com]
          Click Learn More → get A record (76.76.21.21) and CNAME (cname.vercel-dns.com)
          In GoDaddy DNS: delete parking A record, add Vercel A record, add CNAME for www.
          Wait 5-30 minutes → verify green checkmarks in Vercel.
[ ] 85. Add all remaining Vercel env vars:
          Always:
            NEXT_PUBLIC_SITE_URL=https://www.[clientdomain.com] (with www if canonical)
            NEXT_PUBLIC_SHOW_PRICING_TOOLS=false
            NEXT_PUBLIC_CALENDLY_URL=https://calendly.com/[client]/[event]
            SANITY_PROJECT_ID, SANITY_DATASET (blog is always built)
          Only if client purchased premium (shop was NOT deleted in Phase 8B):
            STRIPE_SECRET_KEY (live key, not test)
            STRIPE_WEBHOOK_SECRET
            PRINTFUL_API_KEY
[ ] 86. Register Stripe webhook (only if client purchased premium — shop was not deleted):
          Stripe Dashboard → Developers → Webhooks → Add endpoint
          URL: https://www.[clientdomain.com]/api/stripe/webhook
          CRITICAL: must be canonical URL — Stripe does NOT follow 301/307 redirects
          Event: checkout.session.completed only
          Copy signing secret → add to Vercel as STRIPE_WEBHOOK_SECRET

---

## PHASE 12 — ASSETS (generate when needed, before image-dependent pages go live)

[ ] 87. Hero video (cinematic/premium brands): generate via Kling AI.
          Prompt from design-system.md: photo style description + brand mood.
          Place in /public/ and commit with the page that uses it (Generated Assets Rule).
[ ] 88. Gallery images / blog images / hero photos: generate via fal.ai (fal-ai/flux-pro/v1.1).
          Use prompts derived from design-system.md photography style section.
          Generate: hero photos (3-5), gallery images (8-12), blog post images (1 per article).
          All generated assets committed in the same task commit that uses them.
[ ] 89. Client photography: if client sends real photos, use them. Replace fal.ai placeholders.
          Ask client to take photos at job sites, events, or in their space — the more the better.

---

## PHASE 13 — PRE-LAUNCH AUDIT

[AGENT → pre-launch-auditor.md will run this phase once VALIDATED]

[ ] 90. Remove dev-only components:
          [ ] ROI Calculator (or confirm NEXT_PUBLIC_SHOW_PRICING_TOOLS=false in Vercel)
          [ ] Tier Comparison Chart
          [ ] Any console.log statements
          [ ] Hardcoded test emails in API routes
[ ] 91. All copy reviewed by client. No placeholder text anywhere.
[ ] 92. All photos: real or fal.ai — no broken image URLs, no missing alt text.
[ ] 93. All forms tested end-to-end:
          [ ] Contact form → Resend email delivered to client inbox
          [ ] Quiz form → Resend email delivered with quiz answers appended
          [ ] Shop checkout → Stripe session created, Printful order triggered, owner alert sent
                (skip if shop was deleted in Phase 8B)
[ ] 94. Booking flow tested: Calendly widget loads inline, booking submitted, confirmation received.
[ ] 95. All navigation links functional — no 404s.
[ ] 96. Mobile tested on real phone (390px). Not just browser resize.
[ ] 97. Run Lighthouse on homepage: target ≥ 90 on Performance, Accessibility, SEO.
          Fix any score below 90 before launch.
[ ] 98. OG image verified: paste URL into Twitter Card Validator or LinkedIn Post Inspector.
[ ] 99. Sitemap accessible at: https://www.[clientdomain.com]/sitemap.xml
[ ] 100. robots.txt accessible at: https://www.[clientdomain.com]/robots.txt
[ ] 101. Final commit: chore(launch): pre-launch audit complete, dev tools removed

---

## PHASE 14 — CLIENT REVISION PASS

[ ] 102. Send client the live URL and a revision request:
           "Please read every page. For each edit: which page + what to change + what it should say."
[ ] 103. Make all revisions in one session.
[ ] 104. Commit: fix(copy): client revision pass [date]

---

## PHASE 15 — CLOSE

[ ] 105. Run /retro in Claude Code terminal → vault updates automatically.
           build-log.md gets new errors, patterns, and retrospective entry.
[ ] 106. Hand off credentials to client:
           GoDaddy: their account (they paid for it)
           Resend: email + password from Phase 11
           Vercel: invite client as Viewer (Settings → Members)
           Sanity: invite client as Editor (blog is always active)
[ ] 107. Send invoice for any remaining balance.
[ ] 108. Archive raw notes, transcripts, and discovery material in project folder.

---

## Notes

- Sessions 1-5 map to Phases 3-10. Each session = run /prime at the start.
- [AGENT →] markers show where agents will plug in once VALIDATED. Do manually until then.
- Phase 7 (Blog) and Phase 8 (Shop): always built. Shop scaffold always happens. API wiring depends on tier purchased.
- Phase 10 (SEO/AEO): always run — never skipped. This is what makes the site findable.
- Phase 11 (infrastructure): can happen anytime after Phase 1, but must be complete before launch.
- Phase 12 (assets): generate assets as pages need them, not all at the end.
