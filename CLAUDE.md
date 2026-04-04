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

## Frontend Design Rule
Before making ANY UI/UX decision, visual design change, component creation,
color selection, typography choice, layout decision, or CSS modification,
you MUST re-read frontend-design.md in full. No exceptions.
Reference the specific section of frontend-design.md that authorizes the
decision before implementing it.

## Build Template Rule
website-build-template.md is the build foundation — not the ceiling.
It defines the tech stack, directory structure, animation patterns, base
component architecture, and API route patterns that every Optimus project
starts from. Scaffold from the template first.

Then layer client-specific features on top, informed by initial-business-data.md
and market-intelligence.md. If a client need requires a component or pattern
not in the template, build it using the same stack, conventions, and patterns
the template establishes. Flag every custom addition in progress.md.

Do not ignore the template's patterns. Do not be constrained by its scope.

## Design System Rule
design-system.md is the brand constitution. It was synthesized directly
from market-intelligence.md and initial-business-data.md. You may not deviate
from the approved color palette, typography system, tone of voice, or brand
personality without explicit written approval and an update to design-system.md.
If a component requires a value not in the contract, flag it — do not improvise.

## Market Intelligence Rule
market-intelligence.md contains competitive research, audience psychology,
pricing benchmarks, and feature gap analysis. Every new feature, page, or
content block must be cross-referenced against this report.
Ask: "Does this serve the target audience? Is this validated by research?
Does this close a gap competitors have left open?"

## Progress Tracking Rule
After completing ANY subtask — not at the end of the session, AFTER EACH ONE —
immediately update progress.md with:
- What was completed
- What was discovered or decided
- What the next step is
- Any blockers or open questions

Do not batch updates. Do not defer to end of session. Context can exhaust mid-build
and a deferred update means that work is undocumented. Update after every subtask,
every time, without exception.

## Build Knowledge Rule
Before starting any phase, read the cross-project knowledge base:
`C:\Projects\Optimus Assets\knowledge\build-log.md`

This file contains every error solved and pattern discovered across all builds.
If a similar problem has been solved before, the solution is there.

When any error is resolved:
1. Add a row to the Error Encyclopedia table in `build-log.md` immediately
2. Create a detailed entry file in `C:\Projects\Optimus Assets\knowledge\errors\`
3. Do not continue work until the entry is written

When any phase completes with a non-obvious finding or pattern:
1. Add a row to the Build Patterns table in `build-log.md`

At project close:
1. Add a row to the Project Retrospectives table in `build-log.md`

## Content Standards
- Testimonials must read like a real human typed them on a phone. Never use the em dash (—).
  Humans use commas, periods, and ellipses. Em dashes are a copywriter/AI tell.
- All copy in `/data/site.ts` — zero hard-coded strings in components.
- Blog article CTAs close with an action, never a soft suggestion.
- Hungarian translations must be in third-person formal register — this is culturally
  mandatory for any client in a formal/governmental role (see Sylvia Rich retrospective).

## Code Standards
- Next.js (App Router) + Tailwind CSS 4 + PostCSS — see website-build-template.md Stack section
- Animations: Framer Motion + react-intersection-observer — all scroll-triggered
- Design tokens defined as CSS custom properties in globals.css — not in tailwind.config
- TypeScript — strict mode on
- Mobile-first breakpoints: always design for 390px width before desktop
- Atomic git commits after every subtask — format: type(scope): description
- All copy lives in /data/site.ts — zero hard-coded strings in components
- Performance budget: Lighthouse score ≥ 90 on all pages

## Always-Built Features Rule
Every project ships with ALL of the following, no exceptions, no client-by-client decisions:

**Pricing Page (sales tool — deleted before launch)**
Built in Phase 1. In the nav bar throughout the entire build and demo process.
Deleted as part of the pre-launch audit — it is an Optimus sales tool, not a client deliverable.
The pre-launch-auditor agent flags /pricing still existing as a hard FAIL.

Fixed Optimus pricing structure — same on every build, never customized per client:
- Starter: $1,500 — core pages + animated hero
- Pro: $3,000 — everything in Starter + blog + quiz + booking calendar (MOST POPULAR — this is the sell)
- Premium: $5,500 — everything in Pro + shop

Pro gets the "Most Popular" badge. Starter and Premium are anchors.
Premium never gets a badge — its job is to make $3,000 feel reasonable.

The pricing page always contains:
1. Three tier cards (Starter / Pro / Premium) with feature lists and deposit breakdown (50% upfront)
2. ROI Calculator — two sliders (average job/project value + clients per month) + package selector
   → outputs: monthly revenue, break-even timeline, 12-month ROI per tier
3. Full comparison chart — feature rows grouped by category, checkmarks per tier
   Categories: Foundation / Conversion / Content & SEO / Commerce / Support
4. CTA on each tier that opens the booking calendar inline (never a link away)

**Interactive Quiz**
Built as a multi-step component on the homepage AND as a standalone /quiz page.
Structure: opening hook CTA → problem selection → qualifying questions → lead capture form
→ result screen with recommended service + booking CTA.
The quiz ends at the booking calendar — never at a dead end.
Quiz answers are emailed to the client via Resend on submission.
The homepage version is a CTA block that launches the quiz inline (not a page link).

**Inline Booking Calendar**
Uses Calendly under the hood via react-calendly InlineWidget.
Visually native to the site — brand colors injected via Calendly URL params.
Lives on a dedicated /booking page AND as a homepage teaser section.
NEVER implemented as an href link or redirect. The calendar renders inside the page.
Configured via NEXT_PUBLIC_CALENDLY_URL env var — never hardcoded.

**Testimonials Page**
Always built as a core page at /testimonials. Never conditional on testimonial count.
Homepage hero or testimonials section includes a "See All Testimonials" CTA linking to /testimonials.
Page layout: featured quote full-width at top → full grid of all testimonials from site.ts
→ filter by service type (URL params) → final CTA to book.
If the client has fewer than 4 testimonials at build time: use what exists, flag [MISSING: more testimonials]
in site.ts and note it in progress.md. The page still ships.

**Blog**
9-10 articles minimum. SEO and AEO foundation. Always built. See Phase 7 in build-checklist.md.

These three are built in every Phase 1 agent sweep. They are never optional, never deferred,
never listed as "if applicable." If a phase sign-off doesn't include all three: it is not done.

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
Any new route or page created must be added to navigation and sitemap.ts in the
same commit. Never create a page without connecting it. New page = nav + sitemap
in the same commit, no exceptions.

## Placeholder CTA Rule
"Coming soon" or static CTA boxes are not acceptable phase sign-offs. Every primary
conversion flow must have a demo-mode interactive component before the phase is marked
complete — embedded calendar, mock booking widget, or form with success state.
Flag any static placeholder as a blocker and propose the interactive component before closing.

## Generated Assets Rule
Any script that outputs files into /public must commit those files as part of the
same task commit. Generated images, videos, and data files are never a separate
follow-up step. Generated assets are part of the task that created them.

## Communication Rule
Be opinionated. Flag tradeoffs. Cite research. When there is a clearly better
architectural choice, recommend it with justification. When something will break
at scale, say so. Do not pad responses. Do not assume obvious tasks are complete
without verifying.
