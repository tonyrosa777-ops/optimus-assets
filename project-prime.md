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

### STAGE 1A — Repo Scan (always — before any build work begins)

Before writing a single line of code, scan the finished Optimus projects in C:\Projects\
for animation patterns, component structure, and implementation approaches relevant
to this client's niche and brand personality.

Repos to scan (read their /src/components/ and key page files):
- C:\Projects\Placed-Right-Fence\ — canvas forge animation, trade/contractor structure
- C:\Projects\Gray-Method-Training\ — canvas particle system, coaching/fitness structure
- C:\Projects\andrea-abella-marie\ — cosmic SVG animations, luxury/personal brand structure
- C:\Projects\Xpertise-Painting\ — trade business, pricing page reference, gallery
- C:\Projects\Cody's Complete Junk Removal\ — SVG effects, local service structure
- C:\Projects\Enchanted Madison\ — hospitality/experience brand structure
- C:\Projects\Sylvia Rich\ — bilingual, formal/professional brand structure

What to look for:
- Hero animation that matches this client's brand personality axes (design-system.md Section 8)
- Component patterns for pages this client needs (gallery, quiz, booking, etc.)
- Any niche-specific structural decisions relevant to this business type

Note findings in progress.md: which repo has the closest match, what to reuse vs. adapt.
This scan informs the animation-specialist agent and frontend build — do not skip.

Commit: nothing — this is research only.
Update progress.md: Stage 1A complete — repo scan done, findings noted.

---

### STAGE 1B — Research + Design System

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

### STAGE 1C — Scaffold

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
1. Install dependencies: framer-motion, react-intersection-observer, react-hook-form, zod,
   @fal-ai/client (always — used in Stage 1G for blog card + article header images)
   Add optional deps only for confirmed sections (Sanity, Stripe, @radix-ui/react-*)
2. Create globals.css with CSS custom property tokens — use design-system.md Section 2 values
3. Create /src/data/site.ts with schema structure from website-build-template.md (empty values)
4. Create full directory structure — stub all files
5. Create animation wrappers in /src/components/animations/
6. Create vercel.json at repo root: { "rootDirectory": "[project-folder-name]" }
7. Create .env.local at project root with ALL placeholder keys:

```bash
# Site
NEXT_PUBLIC_SITE_URL=https://[DOMAIN]
NEXT_PUBLIC_SHOW_PRICING_TOOLS=true

# Calendly — replace with client URL before demo
NEXT_PUBLIC_CALENDLY_URL=https://calendly.com/demo/30min

# fal.ai — image generation for blog cards, article headers, gallery
# Get key at: fal.ai/dashboard → API Keys
FAL_KEY=

# Resend — transactional email (contact forms, quiz submissions)
RESEND_API_KEY=

# Sanity CMS — blog
SANITY_PROJECT_ID=
SANITY_DATASET=production
NEXT_PUBLIC_SANITY_PROJECT_ID=
NEXT_PUBLIC_SANITY_DATASET=production

# Shop (Premium tier only — leave blank if client didn't purchase Premium)
PRINTFUL_API_KEY=
STRIPE_SECRET_KEY=
STRIPE_WEBHOOK_SECRET=
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=
```

   ⚠️ FAL_KEY is blank at scaffold. Add the key before Stage 1G runs.
   Without FAL_KEY set, fal.ai calls will fail and blog images won't generate.
   NEXT_PUBLIC_CALENDLY_URL defaults to the Calendly demo URL so the booking
   widget renders during the build without waiting for the client's real URL.

8. Commit: chore(init): scaffold per website-build-template.md with design tokens

Update progress.md: Stage 1C complete — scaffold committed.

---

### STAGE 1D — Content + Animation (parallel agents)

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

Update progress.md: Stage 1D complete — content-writer and animation-specialist done.

**Human checkpoint:** Review hero animation and site.ts hero copy. Approve before Stage 1E.

---

### STAGE 1E — All Pages (core + niche-specific + blog + shop + booking)

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
12. Mobile QA pass — test at 390px viewport width before committing:
    ✓ Hero text starts within ~32px of the navigation bar bottom — NOT mid-screen
      If text is mid-screen: hero section is using `items-center`. Change to `items-start`
      and ensure content div has `pt-24 md:pt-40`. Do not commit until this passes.
    ✓ Dark/light section rhythm — ZERO adjacent sections share the same background (strict alternation, not just "no 3 in a row")
    ✓ No horizontal overflow at 390px (check every section)
    ✓ Quiz options render as emoji + label cards, not plain text list
    ✓ Booking calendar InlineWidget renders (not an empty box)
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

**Service Area Pages (conditional — most local service businesses need these):**
Build if the business serves customers across multiple cities/towns (trade businesses,
home services, delivery, cleaning, junk removal, landscaping, etc.).
Skip if the business is location-fixed (retail, restaurant, single-location studio).

Reference implementation: C:\Projects\Cody's Complete Junk Removal\src\
Read these files before building:
  - src/data/serviceAreas.ts (data shape + example entries)
  - src/app/service-areas/[city]/CityPageClient.tsx (4-section page structure)
  - src/app/service-areas/[city]/page.tsx (generateStaticParams, generateMetadata, notFound)
  - src/app/service-areas/ServiceAreasClient.tsx (index page grid)
  - src/components/layout/Header.tsx (dropdown nav pattern)

18. Data file first — src/data/serviceAreas.ts:
    Export a `serviceAreas` array. Each entry shape (mirror Cody's):
    {
      city: string       // "Springfield"
      state: string      // "IL"
      slug: string       // "springfield" (lowercase, hyphenated)
      population: number // approximate city population
      distance: string   // "12 miles" from the business base location
      description: string // 2-3 sentences — what's notable about this city + why this
                         //  business serves it well. Written by content-writer from
                         //  market-intelligence.md. If data is missing, write it in
                         //  the business owner's voice. [DEMO COPY — pending client review]
    }
    Minimum 3 cities. Maximum 10. Pull city list from initial-business-data.md Section 1.
    If client didn't specify cities, use the 5-6 most populous cities within 20 miles
    of the business address. Write the descriptions yourself.

19. Route structure — /service-areas/[city]:
    CRITICAL: The route MUST be /service-areas/[city] — not /areas/[slug] or any other path.
    Getting this wrong causes 404s from every nav link.

    Files to build:
    A. src/app/service-areas/page.tsx — index page
       - Server component. Imports ServiceAreasClient.
       - generateMetadata: title "Service Areas | [BUSINESS_NAME]"

    B. src/app/service-areas/ServiceAreasClient.tsx — index page UI ('use client')
       - Hero: H1 "[Service Type] Serving [Region]" + subheading about coverage area
       - Grid: all cities from serviceAreas array, each card links to /service-areas/[slug]
         City cards show: city name, state, population, distance from base, description preview
       - "Not in our area?" CTA section at bottom → phone or /contact

    C. src/app/service-areas/[city]/page.tsx — individual city page (SERVER component)
       - generateStaticParams(): return serviceAreas.map(a => ({ city: a.slug }))
       - generateMetadata({ params }): unique title + description per city
         title: "[Service] in [City], [State] | [BUSINESS_NAME]"
         description: "Fast, [service] in [City], [State]. [differentiator]. [CTA]."
       - Find area: const area = serviceAreas.find(a => a.slug === params.city)
       - if (!area) notFound() ← always include this or invalid slugs throw errors
       - Render: <CityPageClient area={area} /> + <FinalCTABanner>

    D. src/app/service-areas/[city]/CityPageClient.tsx — city page UI ('use client')
       Build exactly these 4 sections in order:

       SECTION 1 — Hero:
         - Breadcrumb: Service Areas › [City], [State]
         - H1: "[Service Type] in [City], [State]" (AEO: this IS a search query)
         - area.description as the subheading
         - Primary CTA: "Get a Free [Quote/Estimate] in [City]" → /contact
         - Secondary CTA: phone number (tel: link)

       SECTION 2 — City Info (2-column grid):
         LEFT COLUMN:
         - H2: "Your Local [Service] Experts in [City]"
         - 2 paragraphs about serving this city (pull from area.description + expand)
         - Trust checklist (3-5 bullets — same for every city, from site.ts)
           Examples: "Licensed & insured", "Upfront pricing", "Same-day availability"

         RIGHT COLUMN (⚠️ REQUIRED — this was missing in sweep test 1):
         - Google Maps iframe:
           <div className="rounded-2xl overflow-hidden shadow-md h-64">
             <iframe
               src={`https://maps.google.com/maps?q=${encodeURIComponent(area.city + ', ' + area.state)}&output=embed&hl=en`}
               width="100%"
               height="100%"
               style={{ border: 0 }}
               allowFullScreen
               loading="lazy"
               referrerPolicy="no-referrer-when-downgrade"
               title={`${area.city}, ${area.state} map`}
             />
           </div>
         - Info card below map: "Serving [City], [State]" + distance from base + population

       SECTION 3 — Services Available in [City]:
         - H2: "Services Available in [City]"
         - Grid of all services (from src/data/services.ts or site.ts services array)
         - Each service links to /services/[slug]

       SECTION 4 — City FAQ (auto-generated, no manual content needed):
         const cityFaqs = (city: string, service: string) => [
           {
             q: `Do you offer same-day ${service} in ${city}?`,
             a: `Yes! We offer same-day service in ${city} whenever our schedule allows...`
           },
           {
             q: `How much does ${service} cost in ${city}?`,
             a: `Our pricing is based on [pricing model]. We give you an upfront price before...`
           },
           {
             q: `What areas of ${city} do you serve?`,
             a: `We serve all neighborhoods throughout ${city}...`
           },
         ]
         Accordion expand/collapse on click. No library needed — simple useState toggle.

20. Nav dropdown for Service Areas (⚠️ REQUIRED — plain nav link causes 404 in some builds):
    The "Service Areas" nav item MUST be a dropdown, not a plain link.
    Pattern (adapt from Header.tsx in Cody's):
    - Button: "Service Areas ▾" with ChevronDown icon (use ▾ emoji or CSS, not Lucide)
    - Dropdown panel: lists all cities as links → /service-areas/[slug]
    - Footer of dropdown: "View All Service Areas →" → /service-areas (index page)
    - Click-outside closes: useRef + mousedown event listener
    - AnimatePresence fade + slide: same pattern as services dropdown

    Mobile: all cities listed inline in the mobile nav drawer.

21. Wire /service-areas to sitemap.ts:
    - /service-areas (index) — priority 0.8
    - /service-areas/[city] for each city — priority 0.7 each
    All wired in the same commit as the pages.
Commit: feat(service-areas): /service-areas index + /service-areas/[city] pages + nav dropdown

**Interactive Quiz (always — non-negotiable, every project):**
Reference: tonyrosa777-ops/enchanted-madison quiz for component structure.
Quiz data lives in site.ts quiz object (written by content-writer — see Quiz Data Spec).

20. Homepage quiz CTA component — inline multi-step, launches without leaving the page
    Flow: hook headline + start CTA → step-by-step questions → lead capture → result screen.

    ⚠️ EMOJI ON EVERY ANSWER OPTION — non-negotiable:
    Each answer option renders as a card or button with:
      [emoji] [label text]
    The emoji is the first thing the eye lands on. It makes the quiz feel visual and
    human instead of a plain form. Read quiz.steps[].options[].emoji from site.ts.
    Never render an option as plain text only.

    Step rendering pattern:
    - Each step: full-width question text + grid of option cards (2-col on mobile, 2-4 col desktop)
    - Each option card: emoji large (text-2xl or text-3xl) + label text below or beside
    - Selected state: brand --accent border + subtle background tint
    - Progress indicator: step dots or "Step 1 of 3" text at top
    - "Back" link on steps 2+ — never trap the user

    Lead capture step: name + email + phone fields (React Hook Form + Zod)
    Result screen: recommended service card + primary CTA opens /booking calendar

    Quiz answers + lead info → Resend contact API on form submit.
    Reference implementation: C:\Projects\Enchanted Madison\ (if accessible)

21. /quiz standalone page — same Quiz component, full-page layout, /quiz route
22. "Take the Quiz" in site header — always visible, routes to /quiz
23. Wire /quiz to nav + sitemap.ts in same commit.
Commit: feat(quiz): multi-step quiz with emoji options — homepage CTA + /quiz page, Resend wired

**Inline Booking Calendar (always — non-negotiable, every project):**
23. /booking page — Calendly InlineWidget filling the page. Brand colors via URL params.
    Uses process.env.NEXT_PUBLIC_CALENDLY_URL. Never an href link. Never a redirect.
    The calendar renders inside the site. Visitor never leaves the domain.
24. Homepage booking teaser section — same InlineWidget, constrained height with scroll.
    This is distinct from the quiz CTA — it's the direct "ready to book" section.
25. Wire /booking to nav + sitemap.ts in same commit.
Commit: feat(booking): Calendly inline calendar — /booking page + homepage section

**Pricing Page (always — Optimus sales tool, deleted before launch):**
Reference implementation: C:\Projects\Xpertise-Painting\website\app\pricing\page.tsx
Read that file before building. Adapt the structure — NOT the Xpertise-specific copy.

26. Build src/app/pricing/page.tsx as a "use client" self-contained file.
    Fixed Optimus tier structure — identical on every project:
    - Starter: $1,500 — core pages + animated hero ($750 deposit)
    - Pro: $3,000 — everything in Starter + blog + quiz + booking calendar ($1,500 deposit)
      "Most Popular" badge. This is the sell.
    - Premium: $5,500 — everything in Pro + shop ($2,750 deposit)
      No badge — anchors Pro as the reasonable middle.

    Section A — Tier cards:
    - tiers[] array: id, label, name, price, deposit, recommended, features[], cta
    - Features are CUSTOMIZED to this client's business type — not the painting-specific list
      from the reference. Pull from site.ts services and market-intelligence.md.
    - "Most Popular" badge on Pro. Deposit shown as "(${deposit} deposit today)".
    - Each tier CTA opens the Calendly InlineWidget inline — same widget as /booking page.
      Import InlineWidget from react-calendly. Inject brand colors via URL params.

    Section B — ROI Calculator (ROICalculator component in same file):
    - Slider 1: Average job/project value — min $500, max $20,000, step $100
      Default value: pull from market-intelligence.md avg job value for this business type
    - Slider 2: New clients per month from website — min 1, max 20, step 1. Default: 3
    - Package selector: buttons toggle between Starter / Pro / Premium
    - Outputs (live, calculated on slider change):
        Monthly Revenue = jobValue × clientsPerMonth
        Annual Revenue = Monthly × 12
        Break-even = Math.ceil((packagePrice / monthlyRevenue) × 10) / 10 months
        12-month ROI = ((annualRevenue - packagePrice) / packagePrice × 100)%
    - Animate result cards: opacity + translateY transition on value change

    Section C — Comparison chart (comparisonGroups array in same file):
    - Categories: Foundation / Conversion / Content & SEO / Commerce / Support
    - Each row: feature name + 3 checkmarks (true/false/string per tier)
    - Use ✓ / — style (SVG or text, never Lucide/Heroicons)

27. Wire /pricing to nav bar — visible throughout the entire build and demo.
    Add to sitemap.ts with <priority>0.1</priority> and noindex in page metadata.
    This page must appear in the nav. It is part of the sales presentation.
Commit: feat(pricing): Optimus pricing page — tiers, ROI calc, comparison chart

NOTE: This page is deleted before launch. The pre-launch-auditor flags /pricing
still existing as a hard FAIL.
Delete: src/app/pricing/ + remove from nav + remove from sitemap.ts
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
Reference implementation: C:\Projects\andrea-abella-marie\src\ — read these files before building:
  - src/components/ShopContent.tsx (product grid, category filter, variant picker, cart flow)
  - src/lib/cart.tsx (CartProvider + useCart — localStorage-persisted cart state)
  - src/components/CartDrawer.tsx (slide-in cart drawer, quantity controls, checkout trigger)
  - src/lib/printful.ts (Printful API client)
  - src/app/api/printful/products/route.ts
  - src/app/api/printful/variants/[id]/route.ts
  - src/app/api/stripe/checkout/route.ts
  - src/app/api/stripe/webhook/route.ts
  - src/lib/printful-seeded-products.json (the seeded fallback — critical, see below)

25. Build these files in this order:
    A. src/lib/cart.tsx — CartProvider context + useCart hook (localStorage persistence)
    B. src/components/CartDrawer.tsx — slide-in drawer, quantity +/-, subtotal, checkout CTA
    C. src/lib/printful-seeded-products.json — seed 10-15 generic products with name, price,
       category (Apparel / Drinkware / Bags / Accessories), and a placeholder preview_image_url
       These are the products that show during demo when no Printful API key exists.
    D. src/lib/printful.ts — Printful API client (reads PRINTFUL_API_KEY from env)
    E. src/app/api/printful/products/route.ts — returns Printful sync products or throws
    F. src/app/api/printful/variants/[id]/route.ts — returns variant options or throws
    G. src/app/api/stripe/checkout/route.ts — creates Stripe checkout session
    H. src/app/api/stripe/webhook/route.ts — handles checkout.session.completed
    I. src/components/ShopContent.tsx — product grid, category filter tabs, inline variant picker
       (color swatches + size chips), add-to-cart button, seeded fallback on fetch error
    J. src/app/shop/page.tsx — page wrapper (Navigation + ShopContent + Footer)
    K. Wire CartProvider to src/app/layout.tsx
    L. Wire CartDrawer to src/app/layout.tsx (renders on all pages)
    M. Wire /shop to nav + sitemap.ts in same commit

    ⚠️ CRITICAL — SEEDED FALLBACK PATTERN (non-negotiable):
    ShopContent must fetch /api/printful/products and .catch(() => fallback to seeded JSON).
    The seeded JSON is imported statically: import seededProducts from "@/lib/printful-seeded-products.json"
    This means the shop renders a full, real-looking product grid during the demo
    with zero Printful or Stripe credentials. The demo must show a working shop.
    An empty product grid kills the demo. The seeded fallback is the demo.

    ⚠️ CART MUST FUNCTION WITHOUT API KEYS:
    CartProvider, CartDrawer, and add-to-cart flow are all client-side.
    They work without any env var. This is visually complete for demo day.
    The Stripe checkout route stub can return a demo success response when no
    STRIPE_SECRET_KEY is present — never show a raw error to the demo visitor.

Commit: feat(shop): shop scaffold — cart, drawer, seeded grid, route stubs

⚠️ DECISION GATE: Did client purchase premium tier?
    YES → wire APIs:
          1. Get Printful API key from client → add PRINTFUL_API_KEY to .env.local
          2. Get Stripe secret key + webhook secret → add to .env.local
          3. Remove demo fallback from checkout route — replace stub with real Stripe session
          4. Test: add item → checkout → confirm Stripe session created → confirm webhook fires
          Commit: feat(shop): Stripe + Printful APIs wired
    NO  → delete all shop files + remove nav link + remove sitemap entry
          Files to delete: src/app/shop/, src/app/api/printful/, src/app/api/stripe/,
                           src/components/ShopContent.tsx, src/components/CartDrawer.tsx,
                           src/lib/cart.tsx, src/lib/printful.ts, src/lib/printful-seeded-products.json
          Also: remove CartProvider and CartDrawer from layout.tsx
          Commit: chore(shop): removed shop — not in client scope
          Do NOT add STRIPE_SECRET_KEY, STRIPE_WEBHOOK_SECRET, or PRINTFUL_API_KEY to Vercel.

**Booking:**
26. Client sets up Calendly (wait if pending)
27. Add NEXT_PUBLIC_CALENDLY_URL to .env.local
28. Build BookingWidget (inline embed, not redirect, brand color URL params)
29. Embed on /booking page AND homepage teaser. Test: submit booking, confirm email received.
Commit: feat(booking): Calendly inline widget wired

Update progress.md: Stage 1E complete — all pages, blog, shop, booking built.

---

### STAGE 1F — SEO + AEO

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
Update progress.md: Stage 1F complete.

---

### STAGE 1G — Assets

⚠️ PRE-FLIGHT — check .env.local before generating a single image:
  - FAL_KEY is set and non-empty → BLOCK if blank. Add key now, then continue.
    Get key at: fal.ai/dashboard → API Keys → Create Key
    Without FAL_KEY, every fal.ai call fails silently and blog images won't exist.
  - NEXT_PUBLIC_CALENDLY_URL is set → WARN if still the demo default; note for client

Generate as needed. Each asset commits with the page that uses it.

1. Hero video (cinematic brands): Kling AI — prompt from design-system.md Section 6
   Hero sections use animated SVG or custom canvas/JS — never a photo, never fal.ai.
   Animation selection is handled in Stage 1C by the animation-specialist agent.
2. Blog post card images + article header images: fal.ai (@fal-ai/client, model: fal-ai/flux-pro/v1.1)
   One card image + one header image per article. 9-10 articles = 18-20 images total.
   Prompt = article topic + design-system.md Section 6 (photography style + mood).
   Save to /public/images/blog/[article-slug]-card.jpg and [article-slug]-header.jpg
   Commit each batch of images with the article that uses them.
4. Gallery (trade businesses — always include):
   Check BUSINESS_TYPE in CLAUDE.md. If the business is a trade (contractor, painter,
   fencer, electrician, landscaper, cleaner, builder, or any hands-on service):
   - Build a /gallery page
   - Generate 12-16 job site images via fal.ai — finished work, in-progress shots,
     before/after style. Prompts show the actual trade work, not generic stock.
   - Wire /gallery to nav + sitemap.ts in the same commit
   If not a trade business: skip gallery entirely.
5. Replace any fal.ai image with a real client photo when the client provides one.

Update progress.md: Stage 1G complete — [N] assets generated.

---

### STAGE 1H — Pre-Launch Audit

All Stage 1A-1G work must be complete and committed before this runs.

### Agent: pre-launch-auditor

```
Pre-flight: verify all Stage 1A-1G tasks are marked complete in progress.md → BLOCK if any incomplete
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
Update progress.md: Stage 1H complete. Phase 1 complete.

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
