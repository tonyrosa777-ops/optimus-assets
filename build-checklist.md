# Optimus Build Checklist
# Two phases. Follow every line. Do not skip. Check each box when done.
#
# PHASE 0 — Human-driven. Same as baseline. No agents.
# PHASE 1 — Agent-driven. One coordinated sweep builds everything.
# PHASE 2 — Launch. Manual infrastructure + client handoff.

---

## PHASE 0 — CLIENT ONBOARDING
Everything here is done manually before touching Claude Code.
This phase is unchanged from the baseline workflow.

### 0A — Discovery

[ ] 1. Run discovery session with client. Capture raw notes or voice transcript.

### 0B — Intake + Research (Claude.ai Desktop)

[ ] 2. Open Claude.ai Desktop (Projects). Paste raw notes + intake-prompt.md.
        → Output: initial-business-data.md (all 8 sections filled, no ⚠️ flags)
[ ] 3. Paste initial-business-data.md + market-research-prompt.md.
        → Output: market-intelligence.md (all 9 sections filled, competitors named, gaps identified)
        [AGENT → market-researcher.md replaces this step once VALIDATED]
[ ] 4. Confirm both files have zero ⚠️ NOT FOUND flags.
        If any remain: contact client, fill the gap, then continue.

### 0C — Project Setup

[ ] 5.  Create new project folder: C:\Projects\[ClientName]\
[ ] 6.  Copy these 6 files from C:\Projects\Optimus Assets\ into the new folder:
          - CLAUDE.md
          - project-prime.md
          - frontend-design.md
          - website-build-template.md
          - initial-business-data.md   ← filled version from 0B
          - market-intelligence.md     ← filled version from 0B
[ ] 7.  Open the project folder in VS Code.
[ ] 8.  Run: claude
[ ] 9.  Run: /new-client
          Extracts CLAUDE.md variables and creates .claude/commands/prime.md.
          Without this step /prime loads the wrong file.
[ ] 10. Review output. Verify all 10 variables are correct.
          Type GO to continue. Type STOP to fix a variable first.

### 0D — Design System

[ ] 11. Run: /prime
          This starts the orchestrator. It will run the design-synthesizer agent.
          Wait for design-system.md to be produced.
          [AGENT → design-synthesizer.md handles this automatically]
[ ] 12. Review design-system.md:
          [ ] Section 2 (Color Palette) — all 9 CSS tokens have values
          [ ] Section 8 (Brand Personality Axes) — 3 axes defined
          [ ] Section 11 (Sections Matrix) — every row has Yes/No (no blanks)
          Approve before continuing. This is the brand constitution — get it right.

### 0E — Scaffold + GitHub + Vercel

[ ] 13. Orchestrator scaffolds the project per website-build-template.md.
          Verify these exist after scaffold:
          - /src/app/page.tsx
          - /src/components/
          - /src/data/site.ts (empty schema, not populated yet)
          - globals.css (with design tokens from design-system.md Section 2)
[ ] 14. Push to GitHub:
          git init && git add . && git commit -m "feat(scaffold): initial project scaffold"
          gh repo create [client-name] --private --push --source=.
[ ] 15. Connect to Vercel:
          New Project → Import repo → Framework: Next.js → Root Directory: set correctly
          Skip env vars for now. Add in Phase 2.
[ ] 16. Confirm Vercel build succeeds (green). Fix any build errors before continuing.

---

## PHASE 1 — FULL BUILD SWEEP
This entire phase is agent-driven. The orchestrator coordinates everything.
Run /prime to start each session. The orchestrator picks up from the last checkpoint.
All pages, blog, shop, and SEO are built in this phase — in one coordinated sweep.

### 1A — Content + Hero Animation (parallel — run simultaneously)

The content-writer and animation-specialist are independent.
They run at the same time. Content-writer owns site.ts. Animation-specialist owns Hero.tsx.

[ ] 17. content-writer agent → populates /src/data/site.ts completely
          All fields filled. No placeholders. No em dashes. No invented facts.
          Any [MISSING:] flags get escalated to human before proceeding.
[ ] 18. animation-specialist agent → selects and builds hero animation
          Selection based on design-system.md Section 8 (Brand Personality Axes).
          Implements from the 13-pattern inventory. Mobile handling included.

[ ] 19. Human review checkpoint:
          [ ] Hero copy (H1, tagline, CTA pair) approved
          [ ] Hero animation approved
          Not approved → agent re-runs with correction note.

### 1B — Navigation, Footer, Homepage Sections

[ ] 20. Build navigation (desktop + mobile). All links point to existing routes only.
[ ] 21. Build footer (links, social icons, legal copy, schema address).
[ ] 22. Build all homepage teaser sections:
          [ ] Pain Points (4 cards, empathy framing, no CTA)
          [ ] About/Founder teaser → /about
          [ ] Services preview (3 cards) → /services
          [ ] Stats row (CountUp, 3 numbers from site.ts)
          [ ] Testimonials (3-4 quotes, no em dashes)
          [ ] Quiz CTA → /quiz
          [ ] Blog preview (placeholder cards → /blog)
          [ ] Booking preview (Calendly inline or placeholder → /booking)
          [ ] Final CTA block
[ ] 23. Verify dark/light section rhythm (no 3 consecutive same-background sections).
[ ] 24. Test at 390px. Fix any overflow or clip.
[ ] 25. Commit: feat(layout+homepage): nav, hero, footer, all sections

### 1C — Core Starter Pages

Every new route wired to nav + sitemap.ts in the SAME commit. No exceptions.

[ ] 26. /about — founder story, credentials, photo placeholder, stats, CTA
[ ] 27. /services — service card index → links to /services/[slug]
[ ] 28. /services/[slug] — one page per service:
          Hero (who it's for, CTA) → What you get → Who it's for (3 personas) →
          How it works (numbered steps) → Testimonials → FAQ accordion → Final CTA
[ ] 29. /contact — React Hook Form + Zod, Google Maps iframe, contact info, hours
[ ] 30. /faq — Radix accordion, all Q&As from site.ts
[ ] 31. Commit: feat(pages): about, services, contact, faq + nav/sitemap wired

### 1D — Business-Specific Pages

Read design-system.md Section 11 (Sections Matrix). Build everything marked Yes.

[ ] 32. SERVICE AREA PAGES — if Yes:
          /areas/[slug] — one per city/region served (minimum 3, up to 10)
          Local H1, local testimonials, Google Maps iframe for that city,
          LocalBusiness schema with that city's address.
          All wired to nav dropdown + sitemap.ts.

[ ] 33. PRICING PAGE — if Yes:
          3-tier anchoring. Growth = "Most Popular." Premium = no badge (it anchors).
          ROI calculator gated by NEXT_PUBLIC_SHOW_PRICING_TOOLS=true (dev only).

[ ] 34. REVIEWS PAGE — if Yes (10+ testimonials):
          Featured quote full-width → full grid → filter by service type (URL params).

[ ] 35. QUIZ PAGE — always build:
          Multi-step: problem → goal → location → lead capture → result + booking CTA.
          Quiz answers appended to Resend email on submit.

[ ] 36. Commit: feat(niche-pages): [list which pages built] + nav/sitemap wired

### 1E — Blog

Blog is always built. Non-negotiable.

[ ] 37. Deploy Sanity schema: npx sanity deploy
          Fields: title, slug, publishedAt, mainImage, excerpt, categories, body, seo
[ ] 38. Write 9-10 blog articles from market-intelligence.md Section 8 (content gaps):
          - H1 = a specific buyer question (not a topic)
          - First paragraph = direct 2-sentence answer (this is what AI systems quote)
          - Body = detailed explanation with H2/H3 subheadings
          - Closes with CTA (action, not suggestion)
          - No em dashes
          - Article schema + FAQ schema on every post
[ ] 39. Build /blog index:
          Featured post (full-width) → post grid (3-col) → category filter → newsletter CTA
[ ] 40. Build /blog/[slug] post template:
          Hero image, title, date, category, reading time → PostBody → sidebar (TOC, author,
          related posts) → newsletter signup
[ ] 41. Wire /blog to nav + sitemap.ts.
[ ] 42. Commit: feat(blog): Sanity schema, [N] articles, index + post template

### 1F — Shop

Shop is always scaffolded first. Decision gate determines whether APIs get wired.

[ ] 43. Scaffold shop UI (no live API calls yet):
          /src/data/shop.ts with placeholder products
          /src/lib/cart.tsx — custom React Context, persists to localStorage
          Shop page UI — hero, filter tabs, product grid, ProductCard, skeleton loaders
          /api/stripe/checkout, /api/stripe/webhook, /api/printful/* — route stubs only
[ ] 44. Commit: feat(shop): shop scaffold — UI, cart, route stubs

          ⚠️ DECISION GATE: Did client purchase premium tier (shop included)?

          [ ] YES → proceed to Step 45 (wire APIs)
          [ ] NO  → DELETE all shop files:
                    /src/app/shop/, /src/app/api/stripe/, /src/app/api/printful/,
                    /src/lib/cart.tsx, /src/data/shop.ts,
                    CartDrawer from SiteHeader, shop link from nav, shop teaser from homepage
                    Commit: chore(shop): removed shop — not in client scope
                    Skip to Step 49. Do NOT add Stripe/Printful env vars.

[ ] 45. Configure Printful: create products, set prices, generate mockups.
[ ] 46. Fill shop.ts with real Printful sync IDs, product names, prices, mockup images.
[ ] 47. Wire /api/stripe/checkout — customer_creation: "always", HTTPS image URLs, cart in metadata
[ ] 48. Wire /api/stripe/webhook — verify signature, split POD vs. manual, Printful API call
        Wire /api/printful/products and /api/printful/variants/[id] — KNOWN_COLORS lookup
[ ] 49. Commit: feat(shop): Stripe + Printful + Resend APIs wired
          (or: chore(shop): removed shop — not in scope)

### 1G — Booking

[ ] 50. Client sets up Calendly with event types and availability.
[ ] 51. Add NEXT_PUBLIC_CALENDLY_URL to .env.local.
[ ] 52. Build BookingWidget component — Calendly inline embed with brand color URL params.
          Not a redirect link. Widget stays on the client's domain. (Traffic Retention Rule)
[ ] 53. Embed on /booking page AND as homepage teaser section.
[ ] 54. Test: submit a booking. Confirm confirmation email arrives to client.
[ ] 55. Commit: feat(booking): Calendly inline widget wired

### 1H — SEO + AEO Pass

seo-aeo-specialist agent runs after all pages and articles exist.

[ ] 56. seo-aeo-specialist agent:
          [ ] JSON-LD schema on every page (type matches SCHEMA_TYPE in CLAUDE.md)
          [ ] Unique meta title + description on every page (under character limits)
          [ ] OG images for homepage + major pages (readFileSync pattern — not URL fetch)
          [ ] sitemap.ts — all routes included
          [ ] robots.ts — /studio disallowed
          [ ] AEO: every blog article H1 is a question, first paragraph is direct answer
          [ ] Heading hierarchy: exactly one H1 per page
[ ] 57. Commit: feat(seo-aeo): schema, meta, OG images, sitemap, robots

### 1I — Assets

Generate as needed. Each asset commits with the page that uses it. (Generated Assets Rule)

[ ] 58. Hero video (cinematic brands): Kling AI — prompt from design-system.md Section 6
[ ] 59. Gallery/blog/hero images: fal.ai (fal-ai/flux-pro/v1.1) — prompts from Section 6
          Hero photos (3-5), gallery (8-12), blog post images (1 per article)
[ ] 60. Replace fal.ai placeholders with real client photos when received.

### 1J — Pre-Launch Audit

pre-launch-auditor agent runs before anything goes live.

[ ] 61. pre-launch-auditor agent → writes pre-launch-audit.md
          Review the FAIL list. Fix every FAIL before proceeding.
          Review the WARN list. Escalate each to human.
[ ] 62. Manual checks the agent can't do:
          [ ] Mobile tested on real phone (390px) — not just browser resize
          [ ] Lighthouse ≥ 90 on Performance, Accessibility, SEO — fix anything under 90
          [ ] OG image verified — paste URL into Twitter Card Validator
[ ] 63. Commit: chore(audit): pre-launch audit complete, all FAIL items resolved

---

## PHASE 2 — LAUNCH + CLOSE
Manual infrastructure, client handoff, close.

### 2A — Infrastructure

[ ] 64. Create client Resend account (resend.com, free tier, client's business email).
[ ] 65. Resend: add domain → Auto-configure DNS (sets DKIM + SPF in GoDaddy).
[ ] 66. Resend: create API key → copy immediately (only shown once).
[ ] 67. Add to Vercel: RESEND_API_KEY=[key]
[ ] 68. Test contact form → verify email arrives in client inbox within 30 seconds.
          If not: Resend → Emails tab → find error.
[ ] 69. Connect domain to Vercel:
          Vercel → Project → Settings → Domains → add [domain.com] and www.[domain.com]
          Get: A record (76.76.21.21) and CNAME (cname.vercel-dns.com)
          GoDaddy DNS: delete parking A record → add Vercel A record → add CNAME for www
          Wait 5-30 minutes → verify green checkmarks in Vercel.
[ ] 70. Add all Vercel env vars:
          Always:
            NEXT_PUBLIC_SITE_URL=https://www.[domain.com]
            NEXT_PUBLIC_SHOW_PRICING_TOOLS=false
            NEXT_PUBLIC_CALENDLY_URL=https://calendly.com/[client]/[event]
            SANITY_PROJECT_ID, SANITY_DATASET
          Only if shop is live (not deleted):
            STRIPE_SECRET_KEY (live, not test)
            STRIPE_WEBHOOK_SECRET
            PRINTFUL_API_KEY
[ ] 71. Register Stripe webhook (only if shop is live):
          Stripe → Developers → Webhooks → Add endpoint
          URL: https://www.[domain.com]/api/stripe/webhook (canonical — no redirects)
          Event: checkout.session.completed only
          Copy signing secret → add as STRIPE_WEBHOOK_SECRET in Vercel

### 2B — Client Revision Pass

[ ] 72. Send client the live URL:
          "Please read every page. For each edit: which page + what to change + what it should say."
[ ] 73. Make all revisions in one session. Keep edits in site.ts wherever possible.
[ ] 74. Commit: fix(copy): client revision pass [date]

### 2C — Close

[ ] 75. Run /retro → build-log.md updated automatically (errors, patterns, retrospective entry).
[ ] 76. Hand off credentials:
          GoDaddy: their account (they paid for it)
          Resend: email + password
          Vercel: invite client as Viewer (Settings → Members)
          Sanity: invite client as Editor
[ ] 77. Send final invoice for any remaining balance.
[ ] 78. Archive discovery notes, transcripts, and raw materials in project folder.

---

## Notes

- Phase 0 is baseline — same as it always was. Human-driven. No agents.
- Phase 1 is the agent sweep — everything built in one coordinated pass.
  Sessions in Phase 1: run /prime at the start of each. The orchestrator picks up from
  the last progress.md checkpoint automatically.
- [AGENT →] markers = step is handled by a validated agent.
  Steps without that marker = orchestrator or human handles it directly.
- Shop: always scaffolded. Decision gate at Step 44 determines whether APIs get wired.
- Blog: always built. Non-negotiable.
- Phase 2 always requires human presence — credentials, DNS, client communication.
