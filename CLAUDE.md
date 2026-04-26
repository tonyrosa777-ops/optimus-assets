# CLAUDE.md — [BUSINESS_NAME] Project Rules
#
# VARIABLES TO FILL (Task 1 of /prime will complete these):
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

## Plan Mode Rule
Before writing ANY code — before touching a single file — enter Plan Mode.
Use EnterPlanMode and present a full build plan: what will be built, what files will
be created or modified, what design tokens will be used, what data will flow where.
Get alignment on the plan before the first keystroke. This is non-negotiable.

A wrong plan costs 5 minutes. A wrong build costs 5 hours.

## Vault Organization (Multi-Offering)
The Optimus Assets vault is organized into 4 top-level hubs plus the existing
website-development workflow files at root. Anyone (human or agent) entering the
vault should know where things live.

**For end-to-end vault operating procedures, read [`optimus-system-guide.md`](optimus-system-guide.md).** That file is the canonical operating manual — it covers all 4 hubs, the killer chain (source → daily capture → concept synthesis → apply-to-optimus bridge → offering improvement), the 5 main workflows, the autonomy roadmap, and the maintenance protocol. Update the system guide BEFORE making structural changes to the vault. This CLAUDE.md file documents rules; the system guide documents how-to.

**The 4 hubs:**
- **`00 — Empire Index/`** — vault navigation. Start here. Contains the master README,
  MOCs (Maps of Content), the canonical tag schema, and the glossary.
- **`Offerings/`** — what Optimus sells. Per-offering hubs.
  - `01 Website Development/` — productized core. Templates and lessons live at vault root + `knowledge/`; this hub is the index.
  - `02 AI Agents/` — umbrella for 3 in-development agent products: `01 Chat Assistant/`, `02 Voice Receptionist/`, `03 Marketing Team/`. Cross-product patterns live in `shared-knowledge/`.
- **`Optimus Inc/`** — the company itself (drinking own champagne). Optimus's own
  marketing site, deployed agent instances, market intelligence, social pipeline, brand.
  Distinct from Offerings: Offerings = template/IP, Optimus Inc = Optimus's own deployment.
- **`Optimus Academy/`** — daily personal learning hub. ~90 min/day capture across
  Anthropic courses, NVIDIA classes, YouTube on Claude/agentic concepts, tool tracking
  (NemoClaw, OpenClaw, etc.). The `apply-to-optimus/` subfolder is the bridge that
  connects learning to offering improvements.

**The workflow that fills Optimus Academy:** `/learn` (defined in `learn-prompt.md` at
vault root). Paste a transcript / YouTube URL / course notes → Claude generates three
traces (daily entry + atomic concept note(s) + optional apply-to-optimus bridge) with
scan-and-decide deduplication so `concepts/` doesn't fragment.

**Website-dev workflow is unchanged.** All existing root files (`CLAUDE.md`,
`project-prime.md`, `website-build-template.md`, `build-checklist.md`, `intake-prompt.md`,
`market-research-prompt.md`, `end-to-end-workflow.md`, `frontend-design.md`, `retro.md`,
`initial-business-data.md`, `market-intelligence.md`, `animation-inspiration.md`,
`animated-logo-inspiration.md`, `Revamp logo light.png`) and the entire `knowledge/`
folder (108 files of errors, patterns, retrospectives, sales, onboarding) stay where
they are. Every existing wikilink and every agent's Required Reading section keeps
working without edits. The reorg is additive, not migrational.

**Tag schema** lives at `00 — Empire Index/tag-schema.md` — every NEW note (after
2026-04-26) uses tags from that schema. Existing files stay untagged and findable
by their existing wikilinks. Tag families: `#offering/*`, `#layer/*`, `#learning/*`,
`#applies-to/*`, `#stage/*`, `#status/*`.

**Where to put new content (quick reference):**
- New website-dev lesson learned during a build → `knowledge/errors/` or `knowledge/patterns/` (unchanged from before)
- New website-dev client retrospective → `knowledge/retrospectives/` (unchanged)
- New AI agent pattern shared across chat+voice+marketing → `Offerings/02 AI Agents/shared-knowledge/lessons/`
- New AI agent pattern specific to one product → `Offerings/02 AI Agents/0X <product>/lessons/`
- Daily learning capture → `/learn` (writes to `Optimus Academy/`)
- Competitor or market signal about Optimus's own market → `Optimus Inc/market-intelligence/`
- Anything about a specific client project → that client's own repo (e.g. `c:\Projects\<client-slug>\`), NOT this vault — only the post-project retrospective lands here in `knowledge/retrospectives/`

## Subagent Delegation Rule
Any build phase with 3 or more discrete tasks MUST be broken into individual tasks
and delegated to subagents. One subagent per task. Run independent tasks in parallel.

Never execute a multi-task phase as a single monolithic session. This produces slower,
lower-quality output and exhausts context. The correct pattern:
1. Write a task list for the phase
2. Identify which tasks are independent (can run in parallel)
3. Spawn subagents for each task with complete context (file paths, design tokens, exact spec)
4. Collect outputs, verify, integrate

If a task is trivial (under 5 minutes, 1 file), do it inline. If it's substantive, delegate.

## Skill Creation Rule
When you solve a problem in a new way that works — a component pattern, an integration
flow, an animation approach, a build sequence — immediately:
1. Document the exact steps you took (not a summary — the actual implementation)
2. Create a skill file for it using /skill-creator
3. Reference the skill in future builds instead of reinventing

The goal: every non-trivial build decision becomes a reusable skill. Build once, reuse forever.
If a pattern is already in build-log.md, also create a skill so it can be invoked directly.

## Core Law: Research-Backed Decisions Only
Every design decision, copy choice, UX pattern, or technical recommendation
MUST be traceable to market-intelligence.md or initial-business-data.md.
If you cannot cite the research that backs a decision, do not make the
decision — surface it for review.

## Optimus Positioning Rule
Every Optimus site ships as a **premium, modern, 2026-era build with UI/UX engineered for conversion**. This positioning is non-negotiable regardless of client industry, tier, spend, or market segment. Trade businesses get the same luxury-grade foundation as luxury hospitality; $1,500 Starter tier gets the same visual floor as $5,500 Premium. We do not ship cheaper-looking sites — we ship fewer features.

**What this means in practice (UI/UX layer, set during design-synthesizer + scaffold):**
- Typography: modern variable fonts with serious type scale (clamp-based, declared in Phase 1 globals.css). No Arial, no Roboto, no default system stack.
- Animation: real motion — 3-layer hero stack (HeroParticles + BrandCanvas + stagger text), ambient effects on every interior page, Framer Motion scroll-triggered reveals. Never placeholder transitions.
- Visual density: generous whitespace, radial-gradient-overlayed dark sections (never flat), subtle-gradient-overlayed light sections.
- Interactions: micro-animation on hover, focus-visible states, skeleton loaders on async content.
- Color: brand-primary + brand-accent + restrained neutrals. No stock-corporate blue, no Bootstrap navy, no purple-gradient-on-white.
- Emoji: YES — as semantic UI icons on service cards, pain points, process steps, stats, quiz options. Modern premium brands (Linear, Stripe, Vercel, Raycast, Superhuman) use emoji freely. The tension is not "emoji vs luxury" — the tension is "emoji vs stock-corporate," and we are never stock-corporate.

**What varies by client (not scoped by this rule):**
- Copy voice and tone of voice (see content-writer.md Voice Anchor + design-system.md Section 7)
- Feature mix (see Always-Built Features Rule + design-system.md Section 11)
- Specific brand tokens — color values, fonts, personality axes (design-synthesizer output)
- Photography direction (design-system.md Section 6)

**frontend-design.md scope under this rule:** frontend-design.md offers a menu of aesthetic directions (brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art-deco/geometric, soft/pastel, industrial/utilitarian). For Optimus builds, the selection is constrained to the luxury-modern-2026-conversion family — typically "luxury/refined" or "editorial/magazine" or a hybrid. Never "brutalist/raw," "retro-futuristic," or "playful/toy-like" as a dominant direction, regardless of brand fit. The brand's voice can be casual; the visual presentation is always premium-modern.

See [knowledge/patterns/optimus-luxury-modern-positioning.md](knowledge/patterns/optimus-luxury-modern-positioning.md) for the rationale and the full pattern-doc version.

## Mandatory Pre-Read Protocol
At the start of EVERY session, read in order:
1. CLAUDE.md (this file)
2. progress.md
3. C:\Projects\Optimus Assets\knowledge\build-log.md  ← Cross-project errors + patterns. Check before starting any phase.
4. initial-business-data.md
5. market-intelligence.md
6. design-system.md
7. frontend-design.md
8. website-build-template.md

Never skip this sequence. Never rely on context from a previous session.
Treat each session as if it is your first.

EXCEPTION FOR SUBAGENTS: This protocol applies to the main orchestrator session only.
Subagents spawned via the Agent tool must NOT follow the full 8-file pre-read sequence —
they load only the files listed in their agent file's Required Reading section.
Loading all 8 files in every subagent wastes context before any work begins.

## Agent System Rules
These rules apply whenever the Subagent Delegation Rule triggers agent spawning.

**Agents never spawn agents.** Only orchestrators (workflow commands) spawn agents.
If a subagent needs help, it reports back to the orchestrator — it does not spawn
its own subagents. One level of hierarchy only. This is non-negotiable.

**Agents read files, not summaries.** Every agent gets context by reading known output
files directly (market-intelligence.md, design-system.md, /data/site.ts). The orchestrator
does NOT pass summaries or briefings — it passes file paths. The agent reads the file.

**Agents own their output files exclusively.** No two parallel agents may write to the
same file. Each agent owns exactly one output file or directory. If two tasks share an
output file, they run sequentially — not in parallel.

**Agents checkpoint progress.** After completing each discrete unit of work, the agent
writes a progress note to progress.md. If an agent fails mid-task, the orchestrator
can re-invoke it with "continue from [last checkpoint]" rather than starting over.

**Agent status lifecycle:** Every agent file has a status field: DRAFT → TESTED → VALIDATED.
Only VALIDATED agents run without human review of the output. DRAFT agents always get
output reviewed before proceeding.

**Orchestrators validate outputs.** Before unblocking the next task, the orchestrator
checks that the agent's output file exists, is non-empty, and passes the agent's
Validation criteria. Failing agents get re-run with a correction note — not silently passed.

**Variable injection via CLAUDE.md.** Agents read the project's CLAUDE.md directly to
get filled variables ([BUSINESS_NAME], [DOMAIN], etc. — already substituted by /prime).
Orchestrators do NOT perform string substitution on agent file contents.

## Skill File Name Aliases
Some design skills reference files by generic names that differ from this
project's actual filenames. Resolve them:

| Skill references this name | Read this project file instead          |
|----------------------------|-----------------------------------------|
| FRONTEND_GUIDELINES.md     | frontend-design.md                      |
| APP_FLOW.md                | progress.md (site architecture section) |
| PRD.md                     | progress.md (phase overview + task list) |
| LESSONS.md                 | C:\Projects\Optimus Assets\knowledge\build-log.md |
| TECH_STACK.md              | website-build-template.md (Stack section) |
| progress.txt               | progress.md                             |

Never create duplicate files to satisfy a skill's expected filename.
Always resolve to the correct project file using this table.

## Reference File Hierarchy Rule
Three reference files define the build contract. Before any decision in their domain, re-read the relevant file:

- **design-system.md** — brand constitution (colors, typography, tone, personality axes). No deviation from its values without explicit written approval + a matching update to the file.
- **frontend-design.md** — UI/UX rules (layout, component architecture, visual decisions). Cite the section that authorizes your decision before implementing.
- **website-build-template.md** — the tech/build foundation (stack, directory structure, animation patterns, API routes). Scaffold from it first; then layer client-specific features on top, flagged in progress.md.

Precedence when they conflict: design-system.md > frontend-design.md > website-build-template.md. The brand constitution wins over UI rules; UI rules win over build-template defaults. If a component needs a value outside design-system.md, flag it — do not improvise.

## CSS Scaffold Completeness Rule
Phase 1 globals.css must be complete before any component is built. Required: full `--space-*` scale, all display-type sizes as clamp(), scroll-padding-top values — exact values in [website-build-template.md](website-build-template.md) §Design Tokens.

After scaffold, grep `src/` for any `var(--` reference and verify every referenced CSS variable is declared. An undefined custom property silently resolves to the empty string — layout collapses to 0px with zero build warnings and zero lint errors. This check is mandatory before Phase 1 proceeds.

## Market Intelligence Rule
market-intelligence.md contains competitive research, audience psychology,
pricing benchmarks, and feature gap analysis. Every new feature, page, or
content block must be cross-referenced against this report.
Ask: "Does this serve the target audience? Is this validated by research?
Does this close a gap competitors have left open?"

## Progress Tracking Rule
After completing ANY subtask — not at session end, AFTER EACH ONE — update progress.md with: what was completed, what was discovered/decided, what the next step is, any blockers. Do not batch updates. Context can exhaust mid-build; a deferred update means that work is undocumented.

## Knowledge Base Rule
Cross-project knowledge lives at `C:\Projects\Optimus Assets\knowledge\build-log.md` — every error solved and pattern discovered, indexed. Read it before starting any phase; if a similar problem was solved before, the solution is there.

**When to update:**
- Any error resolved → add a row to the Error Encyclopedia table in build-log.md immediately AND create a detailed entry in `knowledge/errors/`. Do not continue until the entry is written.
- Any phase completes with a non-obvious finding → add a row to the Build Patterns table.
- Project close → add a row to the Project Retrospectives table (see `/retro`).

**What belongs where:**
- CLAUDE.md + website-build-template.md = universal rules that apply to EVERY build. If a rule does not apply universally, it does not belong here.
- `knowledge/` = optional integrations (Sanity CMS, GHL, Instagram/Behold.so, bilingual support, credential-specific fields) and client-specific patterns. Agents consult knowledge/ only when initial-business-data.md indicates relevance.

Before adding any rule to CLAUDE.md or website-build-template.md, ask: "Does this apply to EVERY build regardless of client, industry, or tier?" If no → knowledge/ as a reference pattern. If yes → it is a workflow rule and belongs here.

## Image Generation Rule (fal.ai)
fal.ai image generation is NEVER optional and NEVER deferred. Every blog article ships
with both a card image and a header image. Every trade business ships with a gallery of
12-16 images. These are generated during the sweep, not "later."

**Prompt quality gate — non-negotiable:**
Before running ANY fal.ai generation batch, write ALL prompts first and review them as a set.
Every prompt must be:
- Truly distinct from every other prompt in the batch (no two prompts that would produce
  visually similar images)
- Specific to the article topic or gallery subject (not generic stock-photo descriptions)
- Grounded in design-system.md Section 6 (Photography & Media Direction)
- Creative and visually compelling — describe lighting, composition, mood, specific details

Wrong: "A person getting a haircut in a salon" × 10 with minor variations.
Right: Each prompt tells a different visual story — different angle, different moment,
different emotional beat, different subject within the business's domain.

If a prompt batch has two prompts that would produce near-identical results, rewrite
before generating. The cost of re-running fal.ai is higher than the cost of writing
better prompts. First-time quality is the goal.

**Never request readable text in image prompts.** AI image models cannot render legible
text — they produce garbled characters (e.g., "REJUPED" instead of "REJECTED"). Rewrite
any prompt that describes text on a sign, logo, label, or screen to describe the scene
visually without requiring readable text.

**Visual review before commit — non-negotiable.** After generating, visually inspect every
image before committing. Common artifacts that require regeneration with a revised prompt:
- Garbled or nonsense text baked into the image
- Deformed subjects (extra limbs, merged objects, distorted faces)
- Duplicate elements that shouldn't repeat
- Composition that doesn't match the prompt intent
If any image fails visual review, revise the prompt and regenerate. Do not commit artifacts.

**Enforcement:** If the sweep completes without blog card images + header images for
every article, that is a build failure. The pre-launch auditor checks for these files.

## Copy Writing Rule
**Voice: human phone review, not press quote.**
- Testimonials must read like a real human typed them on a phone. Never use the em dash (—). Humans use commas, periods, and ellipses. Em dashes are a copywriter/AI tell.
- Short sentences. Specific nouns. No corporate hedging.

**File discipline:**
- All copy lives in `/data/site.ts` — zero hard-coded strings in components.
- Blog article CTAs close with an action, never a soft suggestion.

**Act as business owner when data is thin.**
If initial-business-data.md lacks information needed for any section (about story, founder background, service detail, company history), YOU MUST write it yourself in the voice of the business owner: compelling, specific, plausible, grounded in what you do know about their industry and market. Mark every invented section with `// [DEMO COPY — pending client review]`.

Do NOT leave sections blank. Do NOT write `[MISSING:]`. Do NOT ask the business owner. The demo must look complete and impressive — a half-empty site loses the sale. Corrections and personalizations happen after payment, not before the pitch.

This is cardinal: we never hassle the business owner for details we can reasonably write ourselves.

## Code Standards
- Next.js (App Router) + Tailwind CSS 4 + PostCSS — see website-build-template.md Stack section
- Animations: Framer Motion + react-intersection-observer — all scroll-triggered
- Design tokens defined as CSS custom properties in globals.css — not in tailwind.config
- TypeScript — strict mode on
- Mobile-first breakpoints: always design for 390px width before desktop
- Atomic git commits after every subtask — format: type(scope): description
- All copy lives in /data/site.ts — zero hard-coded strings in components
- Performance budget: Lighthouse score ≥ 90 on all pages
- Icons: use high-quality emoji, not SVG icon libraries. No Lucide, no Heroicons, no react-icons.
  Emoji renders natively, loads at zero cost, and looks clean at display size.
  Reference style: tonyrosa777-ops/placed-right-fence service page.

  Emoji is required in every one of these locations — never a plain text label alone:
  - Quiz answer options: every option has a leading emoji before the label text
  - Service cards: each service has an emoji (sourced from site.ts services[].emoji)
  - Pain point cards: each pain point has an emoji (site.ts painPoints[].emoji)
  - How It Works / Process steps: each step has an emoji (site.ts processSteps[].emoji)
  - Stats bar: each stat has a leading emoji (site.ts stats[].emoji)
  - About section belief/value bullets: each belief has an emoji
  - Pricing page feature lists: ✅ for included, ✗ for not included (never plain text)
  - Trust checklist bullets on service area pages: ✅ or context-specific emoji per bullet
  - FAQ: optional — emoji per question category group, not per question

  Choosing the right emoji: match the semantic meaning, not decoration.
  A plumbing service gets 🔧. A lawn care service gets 🌿. Speed stat gets ⚡.
  Wrong: generic ✨ on everything. Right: specific, meaningful, instantly readable.

## Git Identity Rule
Before the first commit on any new project, verify git identity is set:
  git config user.name
  git config user.email
If either is empty or wrong, set per-repo identity:
  git config user.name "Anthony Rosa"
  git config user.email "anthonyrosa14@icloud.com"
Vercel deploy will fail if the committer email does not match the GitHub account.
This has caused blocked deploys on two prior builds (Errors #13, #23).

## Hero Architecture Rule
Every hero ships with exactly 3 layers. No exceptions. **No photos in the hero, ever** — a photo placeholder in the hero is a build failure. The client photo belongs in the About section.

**Layer 1 — HeroParticles.tsx (canvas particle system).** Selected by the animation-specialist from design-system.md Section 8 (Brand Personality Axes). Renders at z-0.

**Layer 2 — [BrandName]Canvas.tsx (brand canvas — custom `<canvas>`).** A creative niche-specific canvas animation. NOT an SVG. NOT a generic shape. Named after the brand (e.g. `HealthShieldCanvas.tsx`, `ForgeCanvas.tsx`). Lives in the right panel of the two-column hero split. Follows the 5-phase lifecycle (STREAM → RISE → COOL → ARC → IDLE) documented in [knowledge/patterns/hero-3-layer-stack-and-5-phase-canvas.md](knowledge/patterns/hero-3-layer-stack-and-5-phase-canvas.md). Container: `position: relative`, explicit height `clamp(340px, 50vw, 540px)`. Canvas fills container with `position: absolute; inset: 0`.

**Selection process (non-negotiable — prevents iteration waste):**
1. Read design-system.md Section 8 + the business type.
2. Brainstorm 10 conceptually distinct visual metaphors tied to this specific business niche. (10 particle-system color variations is ONE concept, not 10. Different metaphors only.)
3. Spawn a harsh critic agent to score all 10 on: niche relevance, visual impact, technical feasibility, uniqueness. Critic picks ONE winner with written rationale.
4. Build ONLY the winner. No pivots mid-implementation. If the winner produces TypeScript errors, runtime errors, or mobile-overflow issues requiring >2 fix commits, HALT and report `[FALLBACK-REQUIRED: <reason>]` — do not autonomously switch.
5. Fallback: the proven LogoParticles chaos→convergence→explosion pattern (Pattern #36 from JCM Graphics). Requires a client logo PNG with transparent background. Safe option, not the default.

Reference implementations for structure (real repos — do not invent file contents):
- tonyrosa777-ops/Sylvia-Rich-Hungary-Consul-NE (gold dust + coat of arms)
- tonyrosa777-ops/where-2-junk (junk/debris particles)
- tonyrosa777-ops/Placed-Right-Fence (forge ember extrusion)

**Layer 3 — Framer Motion stagger text.** H1 first, subheadline at 0.15s, CTAs at 0.3s. z-10.

**H1 = siteConfig.tagline always, with shimmer.** The tagline IS the H1 — emotional hook copy goes in the subheadline, never the H1. The H1 always receives `.hero-shimmer` (amber/gold for warm brands) or `.hero-shimmer-sage` (sage/white for cool/green/neutral brands). "Where healthcare finally makes sense." is the H1 with shimmer — verify it renders before phase sign-off.

**Hero text must always be readable.** Hero headings + body always use `color: var(--text-primary)` (#f5f5f5 on dark builds). If background is dark and text is dark, it's a build failure — can you read every word without highlighting?

**Primary CTA is always booking.** Drives directly to the booking calendar ("Book Your Free Estimate," "Schedule Service," "Book Now"). NEVER "Call Now" — phone CTA belongs in the nav bar, not the hero. Never "Learn More" or "See Our Work."

**Secondary CTA is always the quiz.** Links to `/quiz` with label from `hero.ctaSecondary`. Never a webinar, info session, events page, or external link.

Both CTAs funnel to booking. Primary → calendar directly. Quiz → qualifies → surfaces calendar on result screen. Two paths, same destination.

## Always-Built Features Rule
Every project ships with ALL of the following, no exceptions, no client-by-client decisions:

**Pricing Page (sales tool — deleted before launch)**
Built in Phase 1. If the sweep completes without a /pricing page, that is a build failure.
In the nav bar throughout the entire build and demo process.
Deleted as part of the pre-launch audit — it is an Optimus sales tool, not a client deliverable.
The pre-launch-auditor agent flags /pricing still existing as a hard FAIL.

Nav display: the "Pricing" link renders in amber with a ⬥ marker (e.g. `⬥ Pricing`) so it is
instantly visually distinct from client-facing nav items. This signals to anyone viewing the demo
that it is an internal tool, not a page the client owns.

Fixed Optimus pricing structure — same on every build, never customized per client:
- Starter: $1,500 — core pages + canvas+SVG animated hero + FAQ page
- Pro: $3,000 — Starter + blog architecture, quiz lead capture, booking calendar,
  gallery page, testimonials page (MOST POPULAR — this is the sell)
- Premium: $5,500 — Pro + shop (anchors Pro as reasonable, never gets a badge)

Pro gets the "Most Popular" badge. Starter and Premium are anchors.
Premium never gets a badge — its job is to make $3,000 feel reasonable.

**Client-facing feature names (use these exact labels — this is a sales page):**
- "Automated Booking Calendar" — NOT "inline booking calendar" or "custom calendar"
- "Lead-Capture Quiz" — NOT "interactive quiz" or "quiz funnel"
- "Professional Blog" — NOT "blog architecture" or "Sanity blog"
- "Branded Merch Shop" — NOT "shop scaffold" or "Printful integration"
- "Testimonials Showcase" — NOT "testimonials page"
- "Photo Gallery" — NOT "gallery page"
Technical names describe what we build. Client-facing names describe what they get.

**Never include on pricing page:**
- "Deposit," "upfront," or any payment-split language. The price is the price.
  Anthony offers deposit splits verbally as a backup close — it is never on the page.
- Any Google service on any tier — not "Google Business Profile optimization," not
  "Google Ads setup," not "Google Analytics," not any Google product. Optimus does
  not offer Google services. If the word "Google" appears on the pricing page, it is
  a build failure.

The pricing page always contains:
1. Three tier cards (Starter / Pro / Premium) with feature lists — price only, no deposit math
2. ROI Calculator — two sliders (average job/project value + clients per month) + package selector
   → outputs: monthly revenue, break-even timeline, 12-month ROI per tier
3. Full comparison chart — feature rows grouped by category, checkmarks per tier
   Categories: Foundation / Conversion / Content & SEO / Commerce / Support
4. CTA on each tier that opens the booking calendar inline (never a link away)

**Interactive Quiz**
A scored lead funnel with typed output — not a contact form with extra steps. The quiz
computes a result archetype and delivers personalized results to the user via email. The client
gets a qualified lead notification. Both emails are sent via Resend in parallel.

**Architecture — two layers, fully decoupled:**

Data layer (`src/data/quiz.ts` — all quiz logic, zero UI dependency):
- `QuizType` — 4 result archetypes named for THIS brand's actual audience segments. Read `initial-business-data.md` and `market-intelligence.md` before writing these. Never copy archetypes from a prior build.
- `QUIZ_QUESTIONS` — 8 questions, each with exactly 4 answers, every answer tagged with a `QuizType`
- `QUIZ_RESULTS` — keyed by `QuizType`: name, tagline, body[] paragraphs, recommendedProgram { name, href, reason }
- `scoreQuiz(answers: QuizType[]): QuizType` — counts type occurrences, returns the highest; deterministic, pure, testable

UI layer (`src/app/quiz/QuizClient.tsx` — 3 phases via single `phase` state):
1. **intro** — hook headline + "Start the quiz" CTA
2. **question** — 8 questions rendered one at a time via `questionIndex` (0–7)
   - Each answer click → sets `pendingAnswer` for 400ms: selected answer glows brand primary, others dim to 30% opacity → auto-advances
   - On Q8 (last question): same 400ms timeout → `scoreQuiz(newAnswers)` → sets `resultType` → advances directly to results. No interstitial.
   - Back navigation → slices `answers` array to discard future answers, re-highlights the saved answer for that question
   - `direction` (1 or -1) → AnimatePresence x-offset: forward slides right-to-left, back slides left-to-right
3. **results** — renders `QUIZ_RESULTS[resultType]`: name, tagline, body paragraphs, recommended program card with link, then `<BookingCalendar />` inline directly below — never a link to /booking. The user typed themselves, saw their result, and the calendar is right there. One decision, one click.

There is no email gate phase. No name/email is collected by the quiz. Calendly's booking
form collects name and email as part of its own flow — nothing is lost. The friction wall
of an email gate at peak motivation is the worst possible place to ask for anything.

No `/api/quiz` email route. The client is notified of bookings through Calendly's own
booking confirmation notifications — not through a separate quiz API call.

Quiz CTA placement — two mandatory locations:
1. Site header: "Take the Quiz" button always visible in nav, always routes to /quiz
2. Homepage CTA block: full section that launches the quiz (links to /quiz page — not inline)
Never omit the header CTA. It is the highest-visibility quiz entry point.

Question count: 8 is the ceiling, not the floor. Use the minimum number of questions needed
to reliably assign an archetype. If 5 questions type the user cleanly, use 5. Do not pad
to 8 because Gray Method used 8. The auto-advance glow buys back some engagement time,
but drop-off still compounds with every extra question.

Reference implementation: tonyrosa777-ops/gray-method-training quiz.

**Inline Booking Calendar**
Custom-built calendar UI — a date picker that looks completely native to the site.
Uses the site's brand colors, typography, and design tokens. Not a Calendly iframe.
Under the hood, it calls the Calendly API to fetch available slots and submit bookings.

Architecture:
- `/api/calendly/slots` — GET, calls Calendly API for available times on a given date
- `/api/calendly/book` — POST, submits a booking via Calendly API
- `CALENDLY_API_KEY` — server-side env var (never NEXT_PUBLIC — key must stay server-only)
- `NEXT_PUBLIC_CALENDLY_EVENT_TYPE_URI` — the Calendly event type URI (public, safe to expose)
- Custom `<BookingCalendar />` component: month grid → date selection → time slot picker → confirm form

The component is 100% branded: brand-color selected states, brand font, brand button style.
A user looking at it should not be able to tell it uses Calendly under the hood.

Lives on a dedicated /booking page AND as a homepage teaser section.
NEVER implemented as an href link or Calendly iframe redirect.

Demo mode: if `CALENDLY_API_KEY` is not set, render seeded fake availability (deterministic
hash of date → available times) so the calendar is fully interactive during demo.
A blank or broken calendar kills the demo. A working calendar closes the sale.

**Testimonials Page**
Always built as a core page at /testimonials. Always ships with 36 testimonials.
Never conditional. Never "use what the client has." Write all 36.

Testimonial writing rules (non-negotiable):
- Written in the voice of the target audience from initial-business-data.md/design-system.md
- 36 total. Written by the content-writer agent from scratch, grounded in audience psychology.
- Any real testimonials the client provides are included and count toward the 36.
  Remaining slots are written to match the same voice and specificity.
- Paginated 9 per page on the /testimonials page (4 pages total = 4 × 9 = 36)
- Grid is always 3 columns × 3 rows — this makes every page a complete, consistent square.
  NEVER use 8 per page: 8 in a 3-col grid = 2 full rows + 2 orphans = broken layout on all 4 pages.
  9 per page is the only number that fills 3 columns perfectly. This is non-negotiable.
- ZERO em dashes (—) in any testimonial. Use commas, periods, ellipses only.
- Human tone: short sentences, specific details, sounds like a phone review, not a press quote.
- Vary by: service type, outcome, persona, and length (2 sentences to 4 sentences)

Homepage testimonials section: shows 3-4 featured quotes + "See All Testimonials" → /testimonials.
Page layout: featured quote full-width → paginated grid (9 per page, 3-col × 3-row) → filter by service → booking CTA.

**Blog**
9-10 articles minimum. SEO and AEO foundation. Always built. See Phase 7 in build-checklist.md.

**Shop**
Always scaffolded on every project. The scaffold is built whether or not the client bought Premium.
The decision gate runs AFTER scaffold — not before.

Reference implementation: C:\Projects\andrea-abella-marie\src\

Required files (scaffold on every build):
- src/lib/cart.tsx — CartProvider + useCart (localStorage-persisted cart state)
- src/components/CartDrawer.tsx — slide-in drawer, quantity controls, subtotal, checkout CTA
- src/lib/printful-seeded-products.json — 10-15 seeded products (name, price, category, preview image)
- src/lib/printful.ts — Printful API client (reads PRINTFUL_API_KEY from env)
- src/app/api/printful/products/route.ts
- src/app/api/printful/variants/[id]/route.ts
- src/app/api/stripe/checkout/route.ts
- src/app/api/stripe/webhook/route.ts
- src/components/ShopContent.tsx — product grid, category filter, variant picker, seeded fallback
- src/app/shop/page.tsx
CartProvider and CartDrawer wired in layout.tsx.

Seeded fallback rule (non-negotiable): ShopContent fetches /api/printful/products and falls back
to printful-seeded-products.json on any error. The shop must render a real-looking product grid
during demo with zero Printful credentials. An empty grid kills the demo.

Decision gate (after scaffold):
- Client bought Premium → wire PRINTFUL_API_KEY + STRIPE_SECRET_KEY + STRIPE_WEBHOOK_SECRET
- Client did not buy Premium → delete all shop files from the list above, remove from nav + sitemap

These are built in every Phase 1 agent sweep. They are never optional, never deferred,
never listed as "if applicable." If a phase sign-off doesn't include all of them: it is not done.

## Homepage Section Architecture Rule
Three requirements govern homepage section architecture: animation depth by page type, purpose-level deduplication, and dark/light alternation.

### Animation depth
The full 3-layer stack (HeroParticles + BrandCanvas + stagger text) is **homepage hero only**. Every other page gets ambient effects only — never the full canvas+SVG assembly.

Per-page minimums (never static flat):
- `/services` + individual service pages: rising ash particles or subtle twinkle canvas behind the page header.
- `/testimonials`: shimmer text on featured quote header + subtle twinkle/ash particles. Booking CTA teaser = breathing orb or gradient animation.
- `/blog` index: shimmer overlay or animated gradient on featured post hero header.
- `/about`: SlideIn on stats + photo. FadeUp on section headers.
- `/contact` and `/booking`: breathing orb behind CTA header.
- `/quiz`: slide left/right transition between each step.

Ambient effects defined:
- Rising ash: ~20-30 particles drifting up and fading (not the 145-particle hero system).
- Subtle twinkles: occasional 4-point glimmer flashes, low density.
- Shimmer text: `.hero-shimmer` or `.hero-shimmer-sage` on the page H1 — always.
- Breathing orb: 1-2 radial gradient blobs, CSS-only, 12s cycle.

Before marking any page complete: scroll through at full speed. If it feels flat compared to the homepage, add ambient effects. A site with one animated page and seven static pages is not a luxury product — it loses the sale the moment the client clicks past the hero.

### Purpose-level deduplication
Adjacent sections must each serve a distinct PURPOSE and deliver a distinct MESSAGE. Two sections that both say "ready to [action]?" or both push the same CTA or both frame the same emotional beat are duplicates — even with different background colors. This is a content architecture failure, not a styling issue.

Before building: for each pair of adjacent sections ask "If a visitor scrolled past these back-to-back, would they feel they just read the same thing twice?" If yes → merge one into the other, replace with a different section type (social proof, stats, process steps, FAQ preview), or reposition with 2+ unrelated sections between.

Always-duplicate patterns that must never be adjacent:
- Two CTA sections ("Ready to X?" / "Ready to Y?" / "Let's get started" / "Book now").
- Two testimonial-style sections.
- Two sections both leading with a question headline and ending with the same button.
- A "contact us" section directly above or below a "book now" section.

One CTA block at the bottom of the homepage is sufficient. Mid-page conversion nudge → use the quiz CTA (different format, different intent), not another "Ready to...?" block.

### Dark/light alternation
Homepage alternates background tones. Zero adjacent sections may share the same background tone — every transition shifts tone.

Before building: write the full section order as a comment block at the top of `app/page.tsx` with THREE columns — section name, dark/light, purpose (empathy, social proof, education, conversion, commerce, content preview, etc.). No two adjacent sections may share the same purpose — this catches duplicate CTA sections that color alternation misses.

Example rhythm map:
```
// Hero           — dark  — conversion (primary CTA + quiz CTA)
// Pain Points    — light — empathy
// Services       — dark  — education
// Stats          — light — social proof
// Testimonials   — dark  — social proof (OK — not adjacent to Stats after reorder)
// Quiz CTA       — light — conversion (mid-page nudge, different format than hero)
// Blog Preview   — dark  — content preview
// Shop Teaser    — light — commerce
// Booking        — dark  — conversion (final CTA — only ONE at bottom)
```

**No flat solid backgrounds. Ever.** Every section background is a gradient with subtle motion by default — this applies to BOTH dark and light sections, across ALL pages, not just the homepage hero. Stillness is the exception (see below), never flat solid is the default. A flat section on a luxury-positioned site reads as unfinished.

Two background tones (both gradient + motion, never flat):

- **Dark:** `background: var(--primary)` as the base. Overlay a multi-stop radial or conic gradient (brand accent or warm neutral, 0.05-0.12 alpha) with subtle drift via CSS `@keyframes` on `background-position` or a transformed gradient layer. Cards: `rgba(255,255,255,0.04)` bg, `rgba(255,255,255,0.08)` border. Text: `var(--text-primary)`.

- **Light:** `background: var(--bg-base)` or `var(--bg-elevated)` as the base. Overlay a multi-stop radial gradient (brand accent or muted neutral, 0.04-0.08 alpha) with the same motion treatment. Same motion budget as dark.

**Motion vocabulary — pick ONE per section, do not stack:**
- **Breathing orb** — 1-2 radial blobs, CSS-only, 12s cycle (scale + opacity).
- **Mesh drift** — mesh gradient with animated `background-position`, 20-30s cycle.
- **Aurora sweep** — diagonal conic gradient sweeping across, 15-25s cycle.
- **Grain shimmer** — static gradient + animated fine-grain noise overlay, 8s loop.

**Static-gradient exceptions (still a gradient, no motion):**
- Long-form text sections: blog article bodies, legal/privacy/terms, FAQ answer blocks.
- Pricing comparison tables — focus belongs on the rows, not the background.
- Form-dense sections: signup, contact, booking details.
Never flat even here. Only motion turns off, not the gradient.

**Performance budget — non-negotiable:**
- Maximum 3 active motion layers visible in any viewport simultaneously. The hero counts as 1 (its particle canvas + ambient orb). Count every `@keyframes` background layer toward the limit.
- CSS-only implementation for section backgrounds. Never JavaScript-driven. Canvas is reserved for hero + intentional interior-page ambient effects per the Animation depth subsection above.
- GPU-cheap properties only: `transform`, `opacity`, `background-position`. Avoid `filter`, `backdrop-filter`, `blur` on animated layers.
- Test at 390px mobile — if FPS drops below 50 on a mid-range device, reduce motion layer count before shipping.

**Accessibility — non-negotiable:**
- All motion MUST respect `@media (prefers-reduced-motion: reduce)` by degrading to the STATIC form of the same gradient. Never degrade to a flat color.
- Motion must not exceed 0.3Hz at peak (one visible cycle per 3+ seconds minimum). Faster reads as "loading spinner," not "ambient luxury."

**Dark/light alternation still applies.** Gradient + motion does not replace the purpose-level dedup and dark/light tone alternation rules — both still enforced. No two adjacent sections share the same tone; no two adjacent sections share the same purpose.

See [knowledge/patterns/luxury-gradient-backgrounds.md](knowledge/patterns/luxury-gradient-backgrounds.md) for the full implementation recipes (breathing orb / mesh drift / aurora sweep / grain shimmer), CSS snippets, and common mistakes to avoid.

Plan the rhythm first. Fixing alternation after the fact costs 3-5 refactor commits. If a section is added or reordered later, update the rhythm map and verify no adjacency clash.

Reference pattern: `knowledge/patterns/homepage-dark-light-section-rhythm.md`. Gallery/photo sections should almost always be light — dark backgrounds compete with images.

## Conversion Flow Rule
Never embed third-party redirects that take users off the [DOMAIN] domain.
All conversion flows (booking, scheduling, purchase, inquiry) must be embedded
inline or iframed with seamless visual integration. Approved conversion tool:
[BOOKING_ENGINE]. Every extra click costs conversions. Every domain redirect
costs trust.

## SEO Rule
Every page must include: semantic HTML5 structure, unique title tag, meta
description, Open Graph tags, [SCHEMA_TYPE] schema markup, crawlable text
(zero content locked in images or iframes), and proper heading hierarchy
(one H1 per page).

## Page Wiring Rule
Any new route or page must be added to navigation and sitemap.ts in the same commit. Never create a page without connecting it.

## Placeholder CTA Rule
"Coming soon" or static CTA boxes are not acceptable phase sign-offs. Every primary
conversion flow must have a demo-mode interactive component before the phase is marked
complete — embedded calendar, mock booking widget, or form with success state.
Flag any static placeholder as a blocker and propose the interactive component before closing.

## Generated Assets Rule
Any script that outputs files into /public must commit those files as part of the
same task commit. Generated images, videos, and data files are never a separate
follow-up step. Generated assets are part of the task that created them.

## Visual QA Rule (Pre-Ship Browser Audit — Mandatory)
No Optimus build ships — no project is marked complete, no PR is merged to
production, no demo URL is sent to the client — until a live multi-breakpoint
browser audit has been run with Playwright against the dev server. This is the
final gate. It is not optional and it is not delegable.

The audit drives Playwright through four viewports and captures screenshots at
each, reads the console at each, and opens/closes the mobile nav drawer:
  1. Desktop 1440×900 — static + scrolled (navbar state change)
  2. Mobile 390×844 — iPhone 14/15, most common real-user viewport (first)
  3. Mobile 375×812 — iPhone SE, narrowest — catches wraps first
  4. Mobile 428×926 — iPhone Pro Max, widest single-column
  5. Mobile 390 with nav drawer open — verifies overlay, branding, CTA

Full workflow, gotchas, and exit criteria live in:
  C:\Projects\Optimus Assets\knowledge\patterns\end-of-build-multi-breakpoint-browser-audit.md

Workflow integration (all five enforcement points):
  - build-checklist.md Phase 1 step 14 — human-facing schedule, before Phase 2 Launch
  - project-prime.md Stage 1I — orchestrator execution layer, runs after Stage 1H
    (pre-launch-auditor file-level audit)
  - website-build-template.md Checklist: Before Launch → Visual QA — template reference
  - .claude/agents/launch/pre-launch-auditor.md — file-level agent emits a
    [BLOCKED-ON: Section 11 Multi-Breakpoint Browser Audit] handoff template in its
    output report, instructing the orchestrator to run the Playwright audit before
    advancing to Stage 1J /ultrareview

The pre-launch-auditor agent defers ALL visible-state checks to this audit —
file-reading agents cannot verify layout, overflow, hydration, or console noise.

The audit is ALSO re-run after every client revision batch in Phase 2 (Task 2B
in project-prime.md, step 19 in build-checklist.md) — no revision ships back to
the client without re-passing the audit.

Mandatory exit criteria before marking the audit complete:
  - 0 console errors and 0 console warnings at every viewport
  - No H1 orphan lines at any mobile width
  - No horizontal scroll at 375
  - Hero fits above the fold (eyebrow + H1 + tagline + primary CTA) at every mobile width
  - Mobile nav drawer opens, overlay is dark and opaque, closes cleanly via its inner X
  - **No flat solid-color section backgrounds at any viewport.** Scroll the full page at 1440 and 390. Every section must show a gradient (multi-stop radial, conic, or mesh). If a section reads as a solid fill at any breakpoint, it's a FAIL per the Homepage Section Architecture Rule → Background depth & motion subsection — regardless of whether it's a "text-heavy exception" section (those still require a gradient, only motion is waived).
  - **Motion layer count within budget.** In any single viewport, count the active `@keyframes` background layers visible at once. Maximum 3 simultaneously. Hero counts as 1. Over-budget sections produce visible GPU thrash on mobile; reduce before shipping.
  - **`prefers-reduced-motion` graceful degradation check.** Toggle the OS-level reduce-motion setting (macOS: System Settings → Accessibility → Display → Reduce motion; iOS: Settings → Accessibility → Motion). Reload. Every section must still render as a GRADIENT (not flat) with motion stopped. If any section collapses to flat color under reduce-motion, that's a FAIL.
  - Any fix applied mid-audit triggers a full re-verify of all four viewports
  - Dev server explicitly stopped with TaskStop — `browser_close` does NOT stop it

Skipping any of these = audit incomplete = build not ready to ship. No exceptions.
TypeScript says the code compiles. Tests say the logic works. Only a browser at
the right viewport width tells you the product looks right.

## Communication Rule
Be opinionated. Flag tradeoffs. Cite research. When there is a clearly better
architectural choice, recommend it with justification. When something will break
at scale, say so. Do not pad responses. Do not assume obvious tasks are complete
without verifying.
