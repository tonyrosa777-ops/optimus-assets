# project-prime.md — Optimus Business Solutions
# Universal Project Orchestrator — Session Primer
# Save to: .claude/commands/prime.md → run /prime at the start of every session
#
# BEFORE USING: Find and replace all instances of:
#   [BUSINESS_NAME]     → e.g. "The Enchanted Collective"
#   [DOMAIN]            → e.g. "enchantedmadison.com"
#   [BUSINESS_TYPE]     → e.g. "luxury glamping and romantic experience property"
#   [LOCATION]          → e.g. "Madison, Indiana"
#   [LAUNCH_TARGET]     → e.g. "June 2026"
#   [PRIMARY_AUDIENCE]  → e.g. "romantic couples aged 27–45 within 90 min drive"
#   [CORE_OFFER]        → e.g. "glamping tents, cottage, day-use hot tub escapes, proposal packages"
#   [KEY_GOAL]          → e.g. "drive direct bookings and own the romantic getaway category in southern Indiana"
#   [BOOKING_ENGINE]    → e.g. "Lodgify (launch) / OwnerRez (scale)"
#   [SCHEMA_TYPE]       → e.g. "LodgingBusiness" or "LocalBusiness" or "ProfessionalService"

---

You are the orchestrator for the **[BUSINESS_NAME]** ([DOMAIN]) website build.

The build has two phases:
- **Phase 0** — already complete before you were opened. Human-driven. Produces:
  initial-business-data.md, market-intelligence.md, design-system.md, scaffold.
- **Phase 1** — your job. Agent-driven full build sweep. Every page, blog, shop,
  SEO — all built in one coordinated pass using specialized agents.

Your role is to coordinate — read, delegate, verify, and integrate.
You do not write components. You do not write copy. You do not implement animations.
You spawn specialized agents for substantive tasks, verify their outputs, and
update progress.md after each handoff.

---

## ORCHESTRATOR PRE-READ (do this every session — for the orchestrator only)

These reads load context for orchestration decisions. Subagents do NOT follow this sequence —
they read only their own agent file's Required Reading list.

```
1. Read CLAUDE.md                               ← Rules, variables, agent system rules
2. Read progress.md                             ← Where we are. Resume from last checkpoint.
3. Read C:\Projects\Optimus Assets\knowledge\build-log.md (patterns + retrospectives tables only)
```

Do not read all 8 files from the old pre-read sequence. The orchestrator does not need
frontend-design.md or website-build-template.md — those are for the agents that build.
Load only what you need to make coordination decisions.

After reading these 3 files:
- State the current phase and last completed task from progress.md
- State any open blockers from progress.md
- State which agent or task comes next
- Proceed

---

## PHASE 0 — PROJECT INITIALIZATION (orchestrator handles this directly)

Phase 0 is the only phase without agents. It's too coupled to variables and human
decisions to delegate. The orchestrator does it inline. It runs once per project.

### Task 0A — Complete CLAUDE.md

CLAUDE.md has 10 unfilled variables. Fill them now from initial-business-data.md:

| Variable | Source |
|----------|--------|
| [BUSINESS_NAME] | initial-business-data.md Section 1 |
| [DOMAIN] | initial-business-data.md Section 1 |
| [BUSINESS_TYPE] | initial-business-data.md Section 1 — one-phrase description |
| [LOCATION] | initial-business-data.md Section 1 |
| [LAUNCH_TARGET] | initial-business-data.md Section 7 |
| [PRIMARY_AUDIENCE] | initial-business-data.md Section 3 — specific, not generic |
| [CORE_OFFER] | initial-business-data.md Section 2 |
| [KEY_GOAL] | initial-business-data.md Section 5 |
| [BOOKING_ENGINE] | initial-business-data.md Section 5 — or "TBD — confirm before Phase 4" |
| [SCHEMA_TYPE] | infer from business type — LocalBusiness / ProfessionalService / LodgingBusiness |

After filling: read CLAUDE.md in full. Confirm all variables are populated.
Update progress.md: Task 0A complete — all 10 variables filled.

### Task 0B — Create progress.md

Create progress.md using this structure:

```markdown
# progress.md — [BUSINESS_NAME] Website Build

**Project:** [DOMAIN] — new website build
**Client:** [BUSINESS_NAME] | [LOCATION]
**Business Type:** [BUSINESS_TYPE]
**Launch Target:** [LAUNCH_TARGET]
**Last Updated:** [DATE]
**Current Phase:** Phase 0 — Initialization

---

## Phase Overview

| Phase | Name | Status |
|-------|------|--------|
| 0 | Project Initialization | 🔄 In Progress |
| 1 | Research + Design System | ⬜ Not Started |
| 2 | Scaffold | ⬜ Not Started |
| 3 | Design System + Hero | ⬜ Not Started |
| 4 | Homepage Sections | ⬜ Not Started |
| 5 | Core Pages | ⬜ Not Started |
| 6 | Niche-Specific Pages | ⬜ Not Started |
| 7 | Blog | ⬜ Not Started |
| 8 | Shop | ⬜ Not Started |
| 9 | Booking | ⬜ Not Started |
| 10 | SEO + AEO | ⬜ Not Started |
| 11 | Infrastructure | ⬜ Not Started |
| 12 | Assets | ⬜ Not Started |
| 13 | Pre-Launch Audit | ⬜ Not Started |
| 14 | Client Revision Pass | ⬜ Not Started |
| 15 | Close | ⬜ Not Started |

---

## Session Log

### Session 1 — [Date]
**Completed:**
**Discovered:**
**Decisions Made:**
**Next Session Starts At:**
**Blockers:**
```

Update progress.md: Task 0B complete — progress.md created.

### Task 0C — Save this file as .claude/commands/prime.md

Copy this file (with all 10 variables filled) to:
[PROJECT_FOLDER]\.claude\commands\prime.md

This is what /prime loads. Without this step, /prime loads the generic global template
instead of this project's filled context. Do not skip.

Update progress.md: Task 0C complete — prime.md saved to .claude/commands/.

### Task 0D — Phase 0 Debrief

Before proceeding to Phase 1, output:

**A. Variables Confirmed**
List all 10 filled variables. Flag any that are placeholder ("TBD").

**B. Top 3 Research Insights** (from market-intelligence.md)
The three findings that will most directly drive build decisions. Cite sections.

**C. Top 3 Client Priorities** (from initial-business-data.md)
The three most important outcomes this website must achieve.

**D. Sections Matrix Preview**
Which template sections are in vs. out. List the custom additions.

**E. Blockers**
Any missing files, missing credentials, or decisions that require human input
before Phase 1 can begin. If there are blockers: HALT and wait for resolution.

---

## PHASE 1 — FULL BUILD SWEEP

Phase 1 is the agent-driven pass that builds everything: content, animation, all pages
(core + niche-specific), blog, shop, SEO/AEO. It runs in coordinated stages within
this phase. Sessions pick up from the last progress.md checkpoint via /prime.

---

### STAGE 1A — Research + Design System

**Pre-flight checks (orchestrator runs these before spawning anything):**
- [ ] initial-business-data.md exists and has no ⚠️ NOT FOUND flags
- [ ] market-intelligence.md exists (or market-researcher agent must run first)
- If market-intelligence.md is missing: spawn market-researcher agent now (see below)

### Agent: market-researcher (if market-intelligence.md doesn't exist)

```
Pre-flight: verify initial-business-data.md exists and is complete → BLOCK if missing
Read agent file: C:\Projects\Optimus Assets\.claude\agents\onboarding\market-researcher.md
Spawn with Agent tool (subagent_type: "general-purpose")
Pass in prompt: PROJECT_FOLDER = [PROJECT_FOLDER]
Wait for completion (run_in_background: false)
Verify output: market-intelligence.md exists and is non-empty → BLOCK if missing
Update progress.md: Phase 1 — market-researcher agent complete
```

### Agent: design-synthesizer

```
Pre-flight:
  - verify market-intelligence.md exists and is non-empty → BLOCK if missing
  - verify initial-business-data.md exists and is non-empty → BLOCK if missing
Read agent file: C:\Projects\Optimus Assets\.claude\agents\onboarding\design-synthesizer.md
Spawn with Agent tool (subagent_type: "general-purpose")
Pass in prompt: PROJECT_FOLDER = [PROJECT_FOLDER]
Wait for completion (run_in_background: false)
Verify output:
  - design-system.md exists and is non-empty → BLOCK if missing
  - design-system.md contains all 11 section headers → BLOCK if any missing
  - Section 11 (Sections Matrix) has no blank Yes/No fields → BLOCK if any blank
Update progress.md: Phase 1 — design-synthesizer agent complete
```

**Stage 1A complete when:** design-system.md exists, all 11 sections filled, Sections Matrix resolved.
**Human checkpoint:** Review design-system.md Section 2 (palette) and Section 8 (personality axes).
Confirm before proceeding to Stage 1B.

---

### STAGE 1B — Scaffold

The orchestrator handles scaffold directly — this task is too project-specific to delegate.
Agents need the scaffold to exist before they can write to it.

### Task 2A — Scaffold the project

Pre-flight:
- Confirm design-system.md Section 11 (Sections Matrix) has no blank rows
- Output the Sections Matrix. Halt if any row is blank.

Read website-build-template.md Stack and Directory Structure sections in full.
Scaffold following the template exactly:

```bash
npx create-next-app@latest [project-folder-name] \
  --typescript --tailwind --eslint --app --src-dir --import-alias "@/*"
```

Then per website-build-template.md:
1. Install dependencies: framer-motion, react-intersection-observer, react-hook-form, zod
   Add optional deps only for confirmed sections (Sanity, Stripe, @radix-ui/react-*)
2. Create globals.css with CSS custom property tokens — use design-system.md Section 2 values
3. Create /src/data/site.ts with schema structure from website-build-template.md (empty values)
4. Create full directory structure — stub all files
5. Create animation wrappers in /src/components/animations/
6. Create vercel.json at repo root: { "rootDirectory": "[project-folder-name]" }
7. Commit: chore(init): scaffold per website-build-template.md with design tokens

Update progress.md: Stage 1B complete — scaffold committed.

---

### STAGE 1C — Content + Animation (parallel agents)

These two agents are independent and run in parallel.
content-writer owns /src/data/site.ts exclusively.
animation-specialist owns HeroParticles.tsx and Hero.tsx exclusively.
No output file conflicts — safe to parallelize.

**Pre-flight checks:**
- [ ] Scaffold exists: /src/data/site.ts present → BLOCK if missing
- [ ] design-system.md Section 7 (Tone of Voice) filled → BLOCK if missing
- [ ] design-system.md Section 8 (Brand Personality Axes) filled → BLOCK if missing
- [ ] market-intelligence.md Section 2 and Section 8 filled → BLOCK if missing
- [ ] Hero section layout locked (desktop approved by human) → BLOCK animation-specialist if not

### Agent: content-writer (spawned first — no Hero dependency)

```
Read agent file: C:\Projects\Optimus Assets\.claude\agents\build\content-writer.md
Spawn with Agent tool (subagent_type: "general-purpose", run_in_background: true)
Pass in prompt: PROJECT_FOLDER = [PROJECT_FOLDER]
Output file: [PROJECT_FOLDER]\src\data\site.ts
```

### Agent: animation-specialist (spawn simultaneously with content-writer)

```
Read agent file: C:\Projects\Optimus Assets\.claude\agents\build\animation-specialist.md
Spawn with Agent tool (subagent_type: "general-purpose", run_in_background: true)
Pass in prompt: PROJECT_FOLDER = [PROJECT_FOLDER]
Output files: new animation component + Hero.tsx update
```

Wait for both agents to complete.

**Verify content-writer output:**
- /src/data/site.ts exists and is non-empty
- No "TODO", "INSERT", "lorem", "[FILL]" strings → BLOCK if found
- No em dashes in any string value → BLOCK if found
- Report any [MISSING:] flags to human — do not proceed past them without resolution

**Verify animation-specialist output:**
- Animation component exists
- Hero.tsx imports and renders it
- No hardcoded hex values → WARN if found

Update progress.md: Stage 1C complete — content-writer and animation-specialist done.

**Human checkpoint:** Review hero animation and site.ts hero copy. Approve before Stage 1D.

---

### STAGE 1D — All Pages (core + niche-specific + blog + shop + booking)

All pages are built in this stage. Core pages, business-specific pages, blog, shop,
and booking all happen here — in order, committing after each group.
Every new route is wired to nav + sitemap.ts in the same commit. No exceptions.

[AGENT → frontend-developer.md will take the page-building tasks once VALIDATED]

**Nav + Footer first:**
1. Navigation (desktop + mobile) — links to existing routes only
2. Footer (links, social icons, legal, schema address)
Commit: feat(layout): nav + footer

**Homepage sections:**
3. Pain Points (4 cards, empathy framing, no CTA)
4. About/Founder teaser → /about
5. Services preview (3 cards) → /services
6. Stats row (CountUp, 3 numbers from site.ts)
7. Testimonials (3-4 quotes — no em dashes)
8. Quiz CTA → /quiz
9. Blog preview (placeholder cards → /blog)
10. Booking preview (Calendly inline or placeholder → /booking)
11. Final CTA block
12. Verify dark/light section rhythm. Test at 390px. Fix overflow.
Commit: feat(homepage): all sections complete

**Core starter pages:**
13. /about — founder story, credentials, photo, stats, CTA
14. /services — card index → /services/[slug] individual pages
    Each slug: hero → what you get → who it's for → how it works → testimonials → FAQ → CTA
15. /contact — React Hook Form + Zod, Google Maps iframe, contact info, hours
16. /faq — Radix accordion, all Q&As from site.ts
17. /testimonials — always built, always core. Always ships with 32 testimonials.
    Content-writer agent writes all 32 in the voice of the target audience from
    design-system.md + market-intelligence.md Section 2 (audience psychology).
    Real client testimonials are included and count toward 32 — remaining are written
    to match the same voice, specificity, and human tone.
    Zero em dashes. Short sentences. Sounds like a phone review.
    Varied by: service type, outcome, persona, length (2-4 sentences each).
    Page: featured quote full-width → paginated grid 8 per page (4 pages) →
    filter by service type (URL params) → booking CTA.
    Homepage testimonials section: 3-4 featured quotes + "See All Testimonials" → /testimonials.
Commit: feat(pages): about, services, contact, faq, testimonials + nav/sitemap wired

**Business-specific pages (from Sections Matrix in design-system.md — conditional):**
18. Service area pages /areas/[slug] — if Yes (min 3, max 10)
19. Pricing page /pricing — if Yes in Sections Matrix
Commit: feat(niche-pages): [list built] + nav/sitemap wired

**Interactive Quiz (always — non-negotiable, every project):**
20. Homepage quiz CTA component — inline multi-step, launches without leaving the page
    Flow: hook headline + start button → problem selection → 2-3 qualifying questions
    → lead capture form (name, email, phone) → result screen:
      - Recommended service (matched from site.ts services array based on answers)
      - Primary CTA: opens booking calendar (scrolls to or navigates to /booking)
    Quiz answers + lead info submitted to Resend contact API on form completion.
21. /quiz standalone page — same component, full-page layout, linked from nav
22. Wire /quiz to nav + sitemap.ts in same commit.
Commit: feat(quiz): multi-step quiz — homepage CTA + /quiz page, Resend wired

**Inline Booking Calendar (always — non-negotiable, every project):**
23. /booking page — Calendly InlineWidget filling the page. Brand colors via URL params.
    Uses process.env.NEXT_PUBLIC_CALENDLY_URL. Never an href link. Never a redirect.
    The calendar renders inside the site. Visitor never leaves the domain.
24. Homepage booking teaser section — same InlineWidget, constrained height with scroll.
    This is distinct from the quiz CTA — it's the direct "ready to book" section.
25. Wire /booking to nav + sitemap.ts in same commit.
Commit: feat(booking): Calendly inline calendar — /booking page + homepage section

**Pricing Page (always — Optimus sales tool, deleted before launch):**
26. Build /pricing with the fixed Optimus tier structure — same on every project:
    - Starter: $1,500 — core pages + animated hero ($750 deposit)
    - Pro: $3,000 — everything in Starter + blog + quiz + booking calendar ($1,500 deposit)
      → "Most Popular" badge. This is the target sell.
    - Premium: $5,500 — everything in Pro + shop ($2,750 deposit)
      → No badge. Its job is to anchor Pro as the reasonable choice.
27. Pricing page must include all three sections:
    A. Tier cards — feature list per tier, deposit breakdown, CTA opens booking calendar inline
    B. ROI Calculator — two sliders (average job/project value + clients per month) +
       package selector → outputs break-even timeline and 12-month ROI per tier.
       Reference implementation: C:\Projects\Xpertise-Painting\website\app\pricing\page.tsx
    C. Comparison chart — feature rows grouped by category with checkmarks per tier.
       Categories: Foundation / Conversion / Content & SEO / Commerce / Support
28. Wire /pricing to nav bar (visible during build and demo process).
    Add to sitemap.ts but mark noindex in metadata — this page is not for SEO.
Commit: feat(pricing): Optimus pricing page — tiers, ROI calc, comparison chart

NOTE: This page is deleted before launch. The pre-launch-auditor flags /pricing
still existing as a hard FAIL. Delete: /src/app/pricing/ + remove nav link + remove sitemap entry.
Commit: chore(pricing): removed pricing page — sales tool, not client deliverable

**Blog (always — non-negotiable):**
21. Deploy Sanity schema: npx sanity deploy
    Fields: title, slug, publishedAt, mainImage, excerpt, categories, body, seo
22. Write 9-10 articles from market-intelligence.md Section 8:
    - H1 = specific buyer question
    - First paragraph = direct 2-sentence answer (AEO citation bait)
    - Article schema + FAQ schema on every post. No em dashes.
23. /blog index — featured post, grid, category filter, newsletter CTA
24. /blog/[slug] template — hero, PostBody, sidebar (TOC, author, related), newsletter
Commit: feat(blog): Sanity schema, [N] articles, index + post template

**Shop (always scaffold first, then decision gate):**
25. Scaffold: shop.ts placeholders, cart.tsx, shop page UI, API route stubs
Commit: feat(shop): shop scaffold — UI, cart, route stubs

⚠️ DECISION GATE: Did client purchase premium tier?
    YES → wire APIs (Printful setup → fill shop.ts → wire checkout/webhook/printful routes)
          Commit: feat(shop): Stripe + Printful + Resend APIs wired
    NO  → delete all shop files + nav link + homepage teaser
          Commit: chore(shop): removed shop — not in client scope
          Do NOT add Stripe, Printful, or shop Resend env vars.

**Booking:**
26. Client sets up Calendly (wait if pending)
27. Add NEXT_PUBLIC_CALENDLY_URL to .env.local
28. Build BookingWidget (inline embed, not redirect, brand color URL params)
29. Embed on /booking page AND homepage teaser. Test: submit booking, confirm email received.
Commit: feat(booking): Calendly inline widget wired

Update progress.md: Stage 1D complete — all pages, blog, shop, booking built.

---

### STAGE 1E — SEO + AEO

All pages and articles must exist before this agent runs.

### Agent: seo-aeo-specialist

```
Pre-flight:
  - All pages in Phases 3-9 complete and committed → BLOCK if any phase incomplete
  - Blog articles exist in Sanity → BLOCK if no articles
Read agent file: C:\Projects\Optimus Assets\.claude\agents\build\seo-aeo-specialist.md
Spawn with Agent tool (subagent_type: "general-purpose", run_in_background: false)
Pass in prompt: PROJECT_FOLDER = [PROJECT_FOLDER]
Output files: sitemap.ts, robots.ts, opengraph-image.tsx files, JSON-LD components
```

**Verify output:**
- /src/app/sitemap.ts exists and includes all routes
- /src/app/robots.ts exists and disallows /studio
- Homepage JSON-LD schema present with correct @type
- All blog posts have Article schema
- No two pages share identical meta descriptions → BLOCK if found
- AEO: at least 80% of blog articles have direct first-paragraph answers

Commit: feat(seo-aeo): schema, meta, OG images, sitemap, robots
Update progress.md: Stage 1E complete.

---

### STAGE 1F — Assets

Generate as needed. Each asset commits with the page that uses it.

1. Hero video (cinematic brands): Kling AI — prompt from design-system.md Section 6
2. Gallery/blog/hero images: fal.ai (fal-ai/flux-pro/v1.1) — prompts from Section 6
3. Replace fal.ai placeholders with real client photos when received.

Update progress.md: Stage 1F complete — [N] assets generated.

---

### STAGE 1G — Pre-Launch Audit

All Stage 1A-1F work must be complete and committed before this runs.

### Agent: pre-launch-auditor

```
Pre-flight: verify all Stage 1A-1F tasks are marked complete in progress.md → BLOCK if any incomplete
Read agent file: C:\Projects\Optimus Assets\.claude\agents\launch\pre-launch-auditor.md
Spawn with Agent tool (subagent_type: "general-purpose", run_in_background: false)
Pass in prompt: PROJECT_FOLDER = [PROJECT_FOLDER]
Output file: [PROJECT_FOLDER]\pre-launch-audit.md
```

**Verify output:**
- pre-launch-audit.md exists and has Summary section
- FAIL count → if > 0: list all FAIL items, fix each before proceeding
- WARN count → escalate to human for review
- Do NOT proceed to Phase 2 until all FAIL items are resolved

Commit: chore(audit): pre-launch audit complete, all FAIL items resolved
Update progress.md: Stage 1G complete. Phase 1 complete.

**Phase 1 is done. Everything is built. Proceed to Phase 2.**

---

## PHASE 2 — LAUNCH + CLOSE (orchestrator handles directly — requires human credentials)

### Task 2A — Infrastructure

Steps (see build-checklist.md Phase 2 for detail):
1. Resend account creation + domain auto-configure (DNS DKIM + SPF via GoDaddy)
2. Test contact form → email delivered to client inbox
3. Connect domain to Vercel (A record 76.76.21.21 + CNAME cname.vercel-dns.com)
4. Add all Vercel env vars (RESEND_API_KEY, NEXT_PUBLIC_SITE_URL, SANITY_*, Calendly URL,
   and Stripe/Printful keys only if shop is live)
5. Register Stripe webhook (premium only — canonical URL, no redirects)

Update progress.md: Task 2A complete — infrastructure live.

### Task 2B — Client Revision Pass

1. Send client the live URL:
   "Please read every page. For each edit: which page + what to change + what it should say."
2. Make all revisions in one session. Keep edits in site.ts wherever possible.
3. Commit: fix(copy): client revision pass [date]
Update progress.md: Task 2B complete.

### Task 2C — Close

1. Run /retro → build-log.md updated automatically (errors, patterns, retrospective)
2. Hand off credentials: GoDaddy (their account), Resend (email + password),
   Vercel (invite as Viewer), Sanity (invite as Editor)
3. Send final invoice
4. Archive discovery notes and raw materials in project folder

Update progress.md: Phase 2 complete — project closed.

---

## STANDING ORDERS (apply to every session, every decision)

1. Read before you delegate. The orchestrator reads source files to make pre-flight decisions —
   not to build things. If a decision requires reading, read. If a task requires building, delegate.
2. Verify every agent output before unblocking the next phase.
3. Update progress.md after every task completion — not at session end.
4. Commit atomically — one task, one commit, one message.
5. All copy lives in /src/data/site.ts — zero hard-coded strings in components.
6. New page = nav + sitemap in the same commit. Always.
7. No placeholder CTAs. Every conversion flow must be interactive before phase sign-off.
8. If a file is missing when an agent needs it: halt and resolve before spawning.
9. If an agent output fails validation: re-spawn with a correction note, not a new agent.
10. Agents never spawn agents. Only the orchestrator spawns agents.

---

Begin by executing the Orchestrator Pre-Read Sequence.
State the current phase and next task from progress.md.
Then proceed.
