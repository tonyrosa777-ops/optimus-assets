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
          → business-specific pages from Sections Matrix (service areas)
          → QUIZ (always — non-negotiable):
               Multi-step component on homepage + standalone /quiz page.
               Flow: hook CTA → problem selection → qualifying questions → lead capture
               → result screen with recommended service → opens booking calendar.
               Quiz answers sent to client via Resend on submit. Never ends at a dead end.
          → BOOKING CALENDAR (always — non-negotiable):
               Calendly InlineWidget on /booking page + homepage teaser section.
               Brand colors injected via URL params. Visually native to the site.
               Never an href link or redirect. Configured via NEXT_PUBLIC_CALENDLY_URL.
          → PRICING PAGE (always — sales tool, deleted before launch):
               Fixed Optimus tiers: Starter $1,500 / Pro $3,000 / Premium $5,500
               Pro gets "Most Popular" badge. Starter + Premium anchor it psychologically.
               Includes: tier cards with 50% deposit breakdown + ROI calculator (sliders:
               avg job value + clients/month → break-even + 12-month ROI per tier) +
               full comparison chart (Foundation / Conversion / Content & SEO / Commerce / Support).
               In the nav bar throughout the build and demo. Tier CTAs open booking calendar.
               Deleted in pre-launch audit — pre-launch-auditor flags it as hard FAIL if still present.
          → blog: Sanity schema + 9-10 articles + index + post template (always)
          → shop: scaffold → decision gate → wire APIs if premium / delete if not
          → SEO/AEO: schema, meta, OG images, sitemap, robots, AEO article validation
          → pre-launch audit: PASS/FAIL/WARN report — fix every FAIL before proceeding
        Run /prime at the start of each session. The orchestrator picks up from the last
        checkpoint in progress.md automatically.

[ ] 12. Human review checkpoints during the sweep:
          → Hero copy (H1, tagline, CTA pair) — approve or request correction
          → Hero animation — approve or request correction
          → Any [MISSING:] flags in site.ts — fill the gap, then continue

[ ] 13. Assets (generate when pages need them, not all at the end):
          Hero sections → animated SVG only. Never a photo, never fal.ai.
          Hero video (cinematic brands only) → Kling AI (prompt from design-system.md Section 6)
          Blog post card images → fal.ai fal-ai/flux-pro/v1.1 (one per article, prompts from Section 6)
          Service cards / about page / OG image → real client photos when provided; build without if absent.
          Replace fal.ai blog card images with real photos if client provides them.
          Each asset committed with the page that uses it.

---

### PHASE 2 — Launch (you do this, requires credentials)

[ ] 14. Resend: create client account → add domain → auto-configure DNS → create API key.
        Add RESEND_API_KEY to Vercel. Test contact form → confirm email arrives within 30 seconds.

[ ] 15. Connect domain to Vercel:
        GoDaddy DNS → delete parking A record → add A record 76.76.21.21 → add CNAME cname.vercel-dns.com
        Wait 5-30 minutes → verify green checkmarks in Vercel.

[ ] 16. Add all Vercel env vars:
        Always: NEXT_PUBLIC_SITE_URL, NEXT_PUBLIC_SHOW_PRICING_TOOLS=false,
                NEXT_PUBLIC_CALENDLY_URL, SANITY_PROJECT_ID, SANITY_DATASET
        Shop only: STRIPE_SECRET_KEY (live), STRIPE_WEBHOOK_SECRET, PRINTFUL_API_KEY

[ ] 17. Register Stripe webhook if shop is live:
        Stripe → Developers → Webhooks → https://www.[domain]/api/stripe/webhook
        Event: checkout.session.completed. Copy secret → add as STRIPE_WEBHOOK_SECRET.

[ ] 18. Send client the live URL. Collect revision requests. Make all revisions in one session.

[ ] 19. Run /retro → vault updates automatically. Hand off credentials (GoDaddy, Resend,
        Vercel viewer, Sanity editor). Send final invoice.
