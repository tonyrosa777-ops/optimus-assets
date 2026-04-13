# The Optimus System

c:\Projects\Optimus Assets is the entire operating system for every website build — open in Obsidian so you can browse and review it, and read directly by Claude Code on every project. It contains the rules Claude follows, the prompts that drive intake and research, the build template and design standards, a growing knowledge base that gets smarter with every build, and a team of specialized agents that each own one job. Every project starts from two manual steps — turning client discovery material into initial-business-data.md and running market research to produce market-intelligence.md, both done in Claude.ai Desktop. Once those two files exist, the agent system takes over: a design-synthesizer builds the brand constitution, a content-writer fills every copy field, an animation-specialist picks and implements the hero, and the orchestrator coordinates a full sweep that builds every page, the blog, and the shop in one pass. At project close, /retro scans the codebase, compares against the vault, and writes only new learnings back — so every build makes the next one faster.

---

## The Checklist

### PHASE 0 — Manual (you do this, no agents)

[ ] 1.  Raw discovery material + intake-prompt.md → initial-business-data.md
        (Claude.ai Desktop)

[ ] 2.  initial-business-data.md + market-research-prompt.md → market-intelligence.md
        (Claude.ai Desktop)
        [AGENT → market-researcher.md replaces this once VALIDATED]

[ ] 3.  Confirm both files have zero ⚠️ NOT FOUND flags. Resolve any before continuing.

[ ] 4.  Create new project folder. Copy these 6 files from Optimus Assets:
        CLAUDE.md / project-prime.md / frontend-design.md / website-build-template.md /
        initial-business-data.md ← filled / market-intelligence.md ← filled

[ ] 5.  Open project folder in VS Code. In the terminal, run: claude

[ ] 6.  Run: /new-client — do not skip. Extracts variables and creates the project-scoped
        .claude/commands/prime.md. Without it, /prime loads the wrong file.

[ ] 7.  Review the 10 variables. Type GO → scaffold runs.

[ ] 8.  Push to GitHub. Connect to Vercel → Framework: Next.js, Root Directory: set correctly.
        Confirm green build before continuing.

---

### PHASE 1 — Agent Sweep (orchestrator runs this, you review checkpoints)

[ ] 9.  Run: /prime → orchestrator starts. design-synthesizer agent produces design-system.md.

[ ] 10. Review design-system.md — approve the color palette (Section 2) and brand personality
        axes (Section 8). Every row in Section 11 (Sections Matrix) must have Yes or No.
        Type GO to continue. This is the brand constitution — get it right before the build starts.

[ ] 11. Orchestrator runs the full build sweep in order:
          → content-writer + animation-specialist (run in parallel)
          → nav, footer, all homepage sections
          → core pages: /about, /services, /services/[slug], /contact, /faq, /testimonials
               (homepage testimonials section has "See All Testimonials" → /testimonials)
          → service area pages (local service businesses — most builds need these):
               Route: /service-areas/[city] — NOT /areas/[slug] or any other path.
               Index page at /service-areas. Data in src/data/serviceAreas.ts.
               Each city page: 4 sections — hero, 2-col info (LEFT: text + checklist /
               RIGHT: Google Maps iframe + distance card), services grid, city FAQ.
               Google Maps: <iframe src="maps.google.com/maps?q=[City, State]&output=embed">
               Nav: "Service Areas" = DROPDOWN listing each city → /service-areas/[slug].
               Plain nav link causes 404. Dropdown with direct city links prevents it.
               Reference: tonyrosa777-ops/codys-complete-junk-removal Header.tsx + CityPageClient.tsx
          → QUIZ (always — non-negotiable):
               Multi-step component on homepage + standalone /quiz page.
               Flow: hook CTA → problem selection → qualifying questions → lead capture
               → result screen with recommended service → opens booking calendar.
               Quiz answers sent to client via Resend on submit. Never ends at a dead end.
          → BOOKING CALENDAR (always — non-negotiable):
               Custom BookingCalendar component (NOT Calendly iframe). Looks 100% native.
               Under the hood: /api/calendly/slots + /api/calendly/book API routes.
               Demo mode with seeded fake availability when CALENDLY_API_KEY is not set.
               Lives on /booking page + homepage teaser section. Never an href or redirect.
          → PRICING PAGE (always — sales tool, deleted before launch):
               Fixed Optimus tiers: Starter $1,500 / Pro $3,000 / Premium $5,500
               Starter includes: core pages + animated hero + FAQ page.
               Pro includes: Starter + blog + quiz + booking + gallery + testimonials.
               Premium includes: Pro + shop. No badge — anchors Pro as reasonable.
               Pro gets "Most Popular" badge.
               NEVER include: "deposit," "upfront," payment-split language, or
               any Google service on any tier (not Google Business Profile, not Google
               Ads, not Google Analytics — no Google anything. Build failure if present).
               Includes: tier cards (price only) + ROI calculator (sliders:
               avg job value + clients/month → break-even + 12-month ROI per tier) +
               full comparison chart (Foundation / Conversion / Content & SEO / Commerce / Support).
               In the nav bar throughout the build and demo. Tier CTAs open BookingCalendar.
               Deleted in pre-launch audit — pre-launch-auditor flags it as hard FAIL if still present.
          → blog: Sanity schema + 9-10 articles + index + post template (always)
          → shop: always scaffold (cart.tsx, CartDrawer, ShopContent, API routes, seeded fallback JSON)
               Seeded fallback is the key: shop renders a full product grid during demo with zero
               Printful/Stripe credentials. Reference: tonyrosa777-ops/andrea-abella-marie.
               Decision gate after scaffold: wire Printful + Stripe if premium / delete all if not.
          → SEO/AEO: schema, meta, OG images, sitemap, robots, AEO article validation
          → pre-launch audit (file-level): pre-launch-auditor agent produces PASS/FAIL/WARN report
               from reading files — fix every FAIL before proceeding. This audit catches
               configuration, wiring, and copy bugs but CANNOT catch visible-state bugs.
          → end-of-build multi-breakpoint browser audit (visible-state gate): see step 14 below.
               This step is MANDATORY and is the true final gate — no project ships without it.
        Run /prime at the start of each session. The orchestrator picks up from the last
        checkpoint in progress.md automatically.

[ ] 12. Human review checkpoints during the sweep:
          → Hero copy (H1, tagline, CTA pair) — approve or request correction
          → Hero animation — approve or request correction
          → Any [MISSING:] flags in site.ts — fill the gap, then continue

[ ] 13. Assets (generate when pages need them — NEVER skip fal.ai step):
          ⛔ HUMAN PAUSE before generating: Orchestrator checks .env.local for FAL_KEY.
          If blank → STOP, display message asking user to add fal.ai key, WAIT for GO.
          Do NOT auto-continue. Do NOT skip. Missing images = build failure.
          Hero: animated canvas/JS (logo-based default) — never a photo, never fal.ai.
          Blog post card images + article header images → fal.ai (one card + one header per article)
            ⚠️ PROMPT QUALITY GATE: Write ALL prompts first, review as a set.
            Every prompt must be truly distinct and creative — no two should produce
            visually similar images. Describe lighting, composition, mood, specific details.
            If any two prompts overlap, rewrite before generating. First-time quality is the goal.
          Gallery (trade businesses only — contractors, painters, fencers, electricians, landscapers,
          cleaners, builders, and any hands-on service business):
            → Build /gallery page. Generate 12-16 job site images via fal.ai.
            → Same prompt quality gate applies — each image a distinct visual story.
            → Wire to nav + sitemap.ts in same commit.
          Replace any fal.ai image with real client photo when provided.
          Each asset committed with the page that uses it.
          **If sweep completes without blog card + header images, it is a build failure.**

[ ] 14. **End-of-build multi-breakpoint browser audit — MANDATORY visible-state gate.**
        This is the final gate before Phase 2. No project ships without it. No exceptions.
        Full playbook: knowledge/patterns/end-of-build-multi-breakpoint-browser-audit.md

        Execution outline (orchestrator drives this — NOT delegated to a file-reading agent):
          a. Start dev server in background, wait for ✓ Ready, save the task ID.
          b. Desktop 1440×900 → navigate → browser_wait_for post-hydration text → screenshot
             top of page → screenshot scrolled (window.scrollTo(0, 400) via browser_evaluate).
             Read console at level "error" AND "warning" → expect 0 / 0.
          c. Mobile 390×844 (iPhone 14/15 — most common real viewport, screenshot first).
          d. Mobile 375×812 (iPhone SE — narrowest, catches wraps).
          e. Mobile 428×926 (iPhone Pro Max — widest single column).
          f. Re-check console at every viewport — some warnings only fire on responsive
             class changes.
          g. Resize to 390 → open mobile nav drawer → screenshot → verify dark overlay.
          h. Re-snapshot dialog → click the INNER "Close navigation menu" X (NOT the
             hamburger — it is behind the overlay and will 5-second-timeout).
          i. If any fix is applied mid-audit: re-verify all four viewports, not just the
             one where you caught it. A CSS variable change affects every viewport.
          j. Commit fixes one-per-distinct-issue with the breakpoint referenced in the
             commit body. Push after every commit (standing rule).
          k. TaskStop(task_id) — mcp__playwright__browser_close does NOT stop the dev
             server; it only closes the tab. Explicit TaskStop required.

        Exit criteria (all must be true):
          [ ] 0 console errors / 0 console warnings at all four viewports
          [ ] Hero fits above the fold at every mobile width (eyebrow + H1 + tagline + primary CTA)
          [ ] No H1 orphan lines at any mobile width
          [ ] No horizontal scroll at 375
          [ ] Mobile nav drawer overlay is dark and opaque, not transparent
          [ ] Every interior page has a brand-appropriate animation (Page Animation Rule)
          [ ] Homepage passes the Section Alternation Rule scroll-check (background tones)
          [ ] Homepage passes the Section Content Deduplication Rule (no adjacent sections
              with similar messaging, purpose, or CTA — e.g. two "Ready to X?" blocks)
          [ ] Dev server explicitly stopped via TaskStop

        If any exit criterion fails: fix, re-verify all affected breakpoints, re-check console.
        Only after all criteria pass does the orchestrator proceed to Phase 2.

---

### PHASE 2 — Launch (you do this, requires credentials)

[ ] 15. Resend: create client account → add domain → auto-configure DNS → create API key.
        Add RESEND_API_KEY to Vercel. Test contact form → confirm email arrives within 30 seconds.

[ ] 16. Connect domain to Vercel:
        GoDaddy DNS → delete parking A record → add A record 76.76.21.21 → add CNAME cname.vercel-dns.com
        Wait 5-30 minutes → verify green checkmarks in Vercel.

[ ] 17. Add all Vercel env vars:
        Always: NEXT_PUBLIC_SITE_URL, NEXT_PUBLIC_SHOW_PRICING_TOOLS=false,
                NEXT_PUBLIC_CALENDLY_URL, SANITY_PROJECT_ID, SANITY_DATASET,
                FAL_KEY (same key used during build — images already generated, key kept for future updates)
        Shop only: STRIPE_SECRET_KEY (live), STRIPE_WEBHOOK_SECRET, PRINTFUL_API_KEY,
                   NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY

[ ] 18. Register Stripe webhook if shop is live:
        Stripe → Developers → Webhooks → https://www.[domain]/api/stripe/webhook
        Event: checkout.session.completed. Copy secret → add as STRIPE_WEBHOOK_SECRET.

[ ] 19. Send client the live URL. Collect revision requests. Make all revisions in one session.
        After every revision batch, re-run the Phase 1 step 14 browser audit before re-sending.

[ ] 20. Run /retro → vault updates automatically. Hand off credentials (GoDaddy, Resend,
        Vercel viewer, Sanity editor). Send final invoice.
