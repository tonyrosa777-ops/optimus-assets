# project-prime.md — Optimus Business Solutions
# Universal Project Environment Setup & Session Primer
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

You are the lead architect on a high-stakes website build for **[BUSINESS_NAME]** ([DOMAIN]) — a [BUSINESS_TYPE] based in [LOCATION]. This is a full ground-up build: new brand identity, conversion-optimized architecture, built on the Optimus standard stack.

Before you write a single line of code or make any design decision, you must read and internalize every file in this project. Here is the complete file manifest and reading protocol.

---

## MANDATORY PRE-READ SEQUENCE

Execute these reads in this exact order before doing anything else:

```
Step 1: read CLAUDE.md                                              ← Your rules. Non-negotiable.
Step 2: read progress.md                                            ← Where we are. Resume from here.
Step 3: read C:\Projects\Optimus Assets\knowledge\build-log.md     ← Known errors + patterns from all prior builds.
Step 4: read initial-business-data.md                               ← Business data: offers, pricing, audience, brand, goals.
Step 5: read market-intelligence.md                                 ← Competitive research, market gaps, strategic recommendations.
Step 6: read design-system.md                                       ← Brand identity, palette, typography, tone. The law.
Step 7: read frontend-design.md                                     ← UI/UX principles and implementation rules.
Step 8: read website-build-template.md                              ← Stack, directory structure, components, architecture. The build bible.
```

Do not skip steps. Do not proceed to any task until all eight files are loaded and acknowledged.
If a file does not yet exist, flag it immediately and halt until it is created.

---

## FIRST SESSION OBJECTIVE: ENVIRONMENT SETUP + PLANNING

This first session has one goal: build the project foundation. No website code gets written yet. We are in **Phase 0 — Environment & Strategy**. Execute the following tasks in order.

---

### Task 1 — Complete CLAUDE.md

CLAUDE.md is already in this project copied from the Optimus toolkit. It contains
10 unfilled variables at the top. Fill them now using the project context above
and the data in `initial-business-data.md`:

| Variable | Fill with |
|----------|-----------|
| `[BUSINESS_NAME]` | The client's business name |
| `[DOMAIN]` | The client's domain |
| `[BUSINESS_TYPE]` | One-phrase description of the business category |
| `[LOCATION]` | City, state/country — or "remote/online" |
| `[LAUNCH_TARGET]` | Target launch month/year |
| `[PRIMARY_AUDIENCE]` | Who the website is built for — specific, not generic |
| `[CORE_OFFER]` | The primary product or service being sold |
| `[KEY_GOAL]` | The single most important outcome this website must achieve |
| `[BOOKING_ENGINE]` | The approved conversion tool — infer from initial-business-data.md. Use "TBD — confirm before Phase 4" if unclear. |
| `[SCHEMA_TYPE]` | The correct schema.org type — e.g. `LodgingBusiness`, `LocalBusiness`, `ProfessionalService`, `Restaurant`, `MedicalBusiness` |

After filling the variables, read CLAUDE.md in full and confirm all rules are loaded.
Do not proceed until CLAUDE.md is complete and confirmed.

---

### Task 2 — Create progress.md

Create `progress.md` in the project root using this exact structure:

```markdown
# progress.md — [BUSINESS_NAME] Website Build

**Project:** [DOMAIN] — new website build
**Client:** [BUSINESS_NAME] | [LOCATION]
**Business Type:** [BUSINESS_TYPE]
**Launch Target:** [LAUNCH_TARGET]
**Last Updated:** [DATE — update every session]
**Current Phase:** Phase 0 — Environment Setup

---

## Phase Overview

| Phase | Name | Status |
|-------|------|--------|
| 0 | Environment Setup & Strategy | 🔄 In Progress |
| 1 | Design System & Brand Identity | ⬜ Not Started |
| 2 | Site Architecture & Content Planning | ⬜ Not Started |
| 3 | Core Pages Build | ⬜ Not Started |
| 4 | Conversion Flow Integration | ⬜ Not Started |
| 5 | Secondary Pages & Content | ⬜ Not Started |
| 6 | SEO, Schema & Analytics | ⬜ Not Started |
| 7 | Performance, QA & Launch Prep | ⬜ Not Started |

---

## Phase 0 — Environment Setup & Strategy

### Checklist
- [ ] CLAUDE.md confirmed — 10 variables filled
- [ ] progress.md created (this file)
- [ ] design-system.md created
- [ ] Tech stack scaffolded per website-build-template.md
- [ ] `.claude/commands/prime.md` created inside this project folder with all 10 variables filled — without this, /prime loads the generic global template instead of project context
- [ ] Vercel project connected — Framework Preset and Root Directory set before first deploy
- [ ] Primary conversion tool selected and confirmed
- [ ] Domain DNS confirmed ([DOMAIN])
- [ ] All source files confirmed readable
- [ ] **BLOCKER — do not proceed to Phase 1:** Open design-system.md Section 11. Output the complete sections matrix (every row filled Yes/No with notes). Wait for confirmation before scaffolding anything.
- [ ] Phase 1 task list written and approved

### Decisions Log
_Add key decisions here as they are made. Format: [Date] — Decision — Rationale_

### Open Questions
_Add blockers and unresolved questions here. Format: [Date] — Question — Owner_

### Discovered Insights
_Add anything learned from the pre-read sequence that changes the plan_

---

## Session Log

### Session 1 — [Date]
**Completed:**
**Discovered:**
**Decisions Made:**
**Next Session Starts At:**
**Blockers:**
```

---

### Task 3 — Create design-system.md

This is the brand constitution. Synthesize it entirely from `market-intelligence.md`
and `initial-business-data.md`. Do not invent anything not grounded in the research.
Every section must cite its source document.

Cross-reference the design token structure in `website-build-template.md` (Design Tokens section)
— the contract must produce values compatible with the CSS custom property system defined there.

**Required sections — do not omit any:**

**1. Brand Identity Statement**
One paragraph. Who this business is, who it is not, what feeling the brand should produce
in a visitor within 5 seconds. Derived from: market-intelligence.md audience profile +
competitor differentiation analysis.

**2. Color Palette**
Map to the CSS custom property system from website-build-template.md:
`--primary`, `--primary-muted`, `--accent`, `--bg-base`, `--bg-elevated`, `--bg-card`,
`--text-primary`, `--text-secondary`, `--text-muted`. Include hex/rgb values and usage rules.
Note whether this is a light or dark theme build.

**3. Typography System**
Three font roles matching website-build-template.md: `font-display` (headlines),
`font-body` (paragraphs), `font-mono` (labels, eyebrows, UI micro-copy).
For each: font name, source, weights, sizes per heading level (H1–H4), body, caption.
Include the Google Fonts or CDN import string.

**4. Spacing & Layout System**
Max-width containers (full, content, narrow), section vertical padding (desktop + mobile),
card padding, grid column system, gutter widths. All values as Tailwind classes.

**5. Component Style Rules**
Buttons (primary, secondary, ghost), cards, form inputs, navigation.
For each: shape, size, color states (default, hover, active, disabled).

**6. Photography & Media Direction**
Required shot types, mood, processing style, prohibited content.
Aspect ratios for hero, cards, gallery. Video: autoplay rules, mute, fallback.

**7. Tone of Voice**
3–5 writing principles. For each: principle name, one-sentence rule,
BEFORE (wrong) example from competitors, AFTER (correct) example.

**8. Brand Personality Axes**
3 axes as spectrums with position marker. Example:
`Intimate ◄━━━●━━━━━━━━━━━━► Grand`

**9. Competitor Differentiation Statement**
How this brand's visual and verbal language differs from the top 3 competitors
in market-intelligence.md. One paragraph per competitor.

**10. Design Anti-Patterns (The Prohibited List)**
Explicit numbered list of what is banned. Derived from market-intelligence.md
"What to Avoid" section and competitor weaknesses.

**11. Sections to Include / Remove / Add**
The template is the foundation — not the ceiling. First decide what to keep or cut,
then identify what needs to be built on top for this specific client.

Use the removal guide at the bottom of website-build-template.md for the base sections.

**Base template sections:**

| Section | Include? | Notes |
|---------|----------|-------|
| Shop (Stripe + Printful) | Yes / No | |
| Blog (Sanity CMS) | Yes / No | |
| Quiz / Lead capture | Yes / No | |
| Instagram feed | Yes / No | |
| ROI Calculator | Yes / No | Dev/sales tool — remove before launch |

**Custom additions (features required by this client, not in the template):**
Derived from initial-business-data.md Sections 2 and 5, and market-intelligence.md
Section 5 (Feature Gap Analysis). List every feature that needs to be built on top
of the foundation.

| Custom Feature | Source (file + section) | Complexity |
|----------------|-------------------------|------------|
| | | |

---

### Task 4 — Scaffold the Project

Before running any commands, confirm:
- `initial-business-data.md` — all 8 sections filled (not just headers present)
- `market-intelligence.md` — all 9 sections filled (not just headers present)
- `design-system.md` Section 11 (Sections Matrix) — every row has a Yes/No decision. Output the matrix. Halt if any row is blank.

If any file is incomplete or the sections matrix has blank rows, halt and resolve before proceeding.

Read `website-build-template.md` Stack section and Directory Structure section in full
before running any commands. Scaffold the foundation exactly as specified there.

Then review `initial-business-data.md` Sections 2 (Core Offering) and 5 (Conversion & Tech)
for any client-specific features that fall outside the template's base sections. Stub
those directories and files now — do not leave custom additions for later discovery.

```bash
npx create-next-app@latest [project-folder-name] \
  --typescript \
  --tailwind \
  --eslint \
  --app \
  --src-dir \
  --import-alias "@/*"
```

Immediately after scaffolding, following website-build-template.md exactly:

1. Install dependencies from the Stack table:
   `npm install framer-motion react-intersection-observer react-hook-form zod`
   Add optional deps only if sections are included (Sanity, Stripe, etc.)
2. Create `globals.css` with the CSS custom property design token structure from
   website-build-template.md — swap values for this client's design-system.md palette
3. Create `/src/data/site.ts` using the siteData structure from website-build-template.md —
   populate with client copy from initial-business-data.md
4. Create the full directory structure from website-build-template.md — stub out all files
5. Create the 8 animation wrappers in `/src/components/animations/` per website-build-template.md
6. Create `vercel.json` at the **repo root**:
   ```json
   { "rootDirectory": "[project-folder-name]" }
   ```
   Also set Framework Preset → Next.js in Vercel Dashboard before first deploy.
7. Commit: `chore(init): scaffold per website-build-template.md with design tokens`

---

### Task 5 — Debrief & Phase 1 Planning

Once Tasks 1–4 are complete, provide a structured debrief containing exactly:

**A. Pre-Read Confirmation**
List all 7 files read. For any file that did not exist, flag it.

**B. Top 3 Strategic Insights from market-intelligence.md**
The three research findings that will most directly drive design and conversion
decisions on this project. Cite the specific section.

**C. Top 3 Critical Problems from initial-business-data.md**
The three most important gaps or weaknesses in the current business presence
that the website must solve. Cite the source directly.

**D. Design System Summary**
3–5 sentences summarizing the brand direction from design-system.md.
Confirm the CSS custom property values and font pairing.

**E. Sections In / Out / Add**
Confirm which template sections are included and which are removed, with rationale.
Then confirm every custom feature to be built on top of the template foundation —
anything required by this client that isn't in the template's base sections.
Source each custom addition to initial-business-data.md or market-intelligence.md.

**F. Phase 1 Task List (proposed)**
A numbered checklist of every task in Phase 1 — Design System Implementation —
broken down small enough that each task takes 30–60 minutes max.

**G. Blockers**
Any questions, missing files, missing credentials, or decisions that require
human input before Phase 1 can begin.

---

## PROJECT CONTEXT

**Primary objective:**
[KEY_GOAL]

**Target audience:**
[PRIMARY_AUDIENCE]

**Core offerings:**
[CORE_OFFER]

**Tech stack:**
See website-build-template.md — Stack section. All architectural decisions
derive from that document, not from this file.

**Competitive advantages to own:**
_(To be populated from market-intelligence.md after pre-read.)_

---

## STANDING ORDERS

These apply to every session, every task, every line of code, forever:

1. **Read before you build.** The eight files in the pre-read sequence contain everything needed to avoid bad decisions. Use them every session.
2. **website-build-template.md is the build foundation.** Stack, directory structure, animation patterns, and base components are defined there. Scaffold from it first — then layer client-specific features on top based on initial-business-data.md and market-intelligence.md. Build custom additions using the same conventions the template establishes.
3. **design-system.md is the brand law.** Every color, font, and component rule comes from there. Do not improvise values not in the system.
4. **Mobile first, always.** Design at 390px. Then scale up. Never the reverse.
5. **Research backs every choice.** If you cannot point to market-intelligence.md or design-system.md to justify a decision, flag it before implementing.
6. **Commit atomically.** Every subtask = one commit. Never batch unrelated changes.
7. **Update progress.md after every subtask — not at session end.** Context can exhaust mid-build. If you defer, it's lost. Commit the progress.md update as part of each subtask commit. No exceptions.
8. **The conversion flow is sacred.** Every extra click costs conversions. Every domain redirect costs trust.
9. **All copy lives in /data/site.ts.** Zero hard-coded strings in components. Client handoff and future edits must be trivial.
10. **If it isn't in progress.md, it didn't happen.** Document everything.
11. **Log it or lose it.** Every resolved error → entry in `build-log.md` before continuing. Every completed project → retrospective entry. The knowledge base only works if it grows.
12. **Every new page gets wired immediately.** Any new route created must be added to navigation and sitemap.ts in the same commit. Never create a page without connecting it.
13. **Placeholder CTAs are blockers, not completions.** "Coming soon" or static CTA boxes are not acceptable phase sign-offs. Every primary conversion flow must have a demo-mode interactive component before the phase is marked complete. Flag it and propose the component before closing.
14. **Generated assets are part of the task.** Any script that outputs files into /public must commit those files as part of the same task commit. Generated images, videos, and data files are never a separate follow-up step.

---

## HOW TO USE THIS FILE FOR A NEW PROJECT

1. Copy this file into the new project root as `project-prime.md`
2. Find and replace all 10 bracketed variables at the top of this file
3. Copy `CLAUDE.md`, `frontend-design.md`, and `website-build-template.md` from the Optimus toolkit
4. Copy `initial-business-data.md` and `market-intelligence.md` templates from the Optimus toolkit — fill both completely before proceeding
5. Save a copy to `.claude/commands/prime.md` so `/prime` loads it automatically in Claude Code
6. Open Claude Code, run `/prime`, let Task 1 complete CLAUDE.md, then execute Tasks 2–5
7. Do not proceed past the debrief in Task 5 until all blockers are resolved

---

Begin by executing the Mandatory Pre-Read Sequence.
Confirm each file was read.
Then execute Tasks 1 through 5 in order.
Go.
