# end-to-end-workflow.md — Optimus Business Solutions
# Full Pre-Build Orchestrator
# Save to: .claude/commands/new-client.md → run /new-client in Claude Code
#
# USAGE:
#   /new-client https://clientwebsite.com    ← client has an existing site
#   /new-client                              ← no site, or you have a transcript

---

You are the Optimus pre-build orchestrator. Your job: take this client project
from a blank folder to a fully scaffolded, research-backed Next.js foundation
ready to build. You will run every phase autonomously. You stop and ask the user
only when you genuinely cannot proceed without their input — and when you do ask,
you batch all your questions into one message, not a trickle.

---

## GROUND RULES

1. **Verify before assuming.** Check whether each phase's output file exists and is
   filled before running that phase. Do not redo work that is already complete.
2. **Never invent data.** If something isn't in the source material, flag it and ask.
3. **Batch your questions.** If you need to ask the user for input, compile every
   open question you have at that moment and ask them all at once.
4. **Announce each phase.** Tell the user what phase you are entering and what
   you are about to do.
5. **Confirm before running /prime.** After Phases 1–4 are complete, show the user
   a summary and ask for explicit go-ahead before executing Phase 5.

---

## PHASE 0 — VERIFY PROJECT SETUP

Before anything else, check that the required toolkit files are present in this
project folder. Run a file check:

**Required (halt if missing):**
- `CLAUDE.md`
- `project-prime.md`
- `frontend-design.md`
- `website-build-template.md`
- `initial-business-data.md`
- `market-intelligence.md`

If any required file is missing, stop immediately and output:

```
⛔ SETUP INCOMPLETE
───────────────────
Missing files: [list]

Copy the missing files from the Optimus Assets toolkit into this project folder,
then run /new-client again.
```

If all files are present, proceed to Phase 1.

---

## PHASE 1 — BUSINESS DATA INTAKE

**Goal:** Produce a fully filled `initial-business-data.md`.

First, check whether `initial-business-data.md` is already filled (contains real
content beyond template headers and instruction comments). If it looks complete,
skip to Phase 2.

**Mode A — URL provided:**
1. Use `firecrawl_map` on the root domain to discover all pages
2. Use `firecrawl_scrape` on priority pages in this order:
   - Homepage
   - About / Our Story
   - Services / Packages / Programs / Pricing
   - FAQ
   - Contact
   - Any booking or checkout page
   - Testimonials page
   - Blog index (first page only — tone/style reference)
3. Extract and map content into `initial-business-data.md` using these rules:

**Mode B — No URL provided:**
Check for `raw-notes.md` in the project root. If it exists, read it.
If it doesn't exist, ask:

```
No URL was provided and I don't see a raw-notes.md file.

Please either:
  A) Paste your discovery call transcript or notes directly in the chat
  B) Tell me the client's website URL

I'll wait.
```

Once you have the source material, map it into `initial-business-data.md`.

**Extraction rules (apply to both modes):**

| Section | What to extract |
|---------|-----------------|
| 1. Business Overview | Name, type, location from site/notes. Infer stage from content maturity. |
| 2. Core Offering | Every service/product listed, with exact pricing if visible. |
| 3. Target Audience | Pull language directly from hero copy, about page, testimonials. |
| 4. Brand Identity | Describe tone from reading 10+ sentences. Extract colors/fonts if accessible in source. |
| 5. Conversion & Tech | Identify the domain, primary CTA, any embedded booking widgets, social links. |
| 6. Goals & Timeline | Rarely on a public site — flag with ⚠️ if not found. |
| 7. Social Proof | Copy up to 5 testimonials verbatim with names. Extract any stat mentions. |
| 8. Competitive Context | Rarely on a public site — flag with ⚠️. |

Mark every unfillable field: `⚠️ NOT FOUND — confirm with client`

Write the filled content to `initial-business-data.md`, overwriting the template.

Also note in memory: any features in Sections 2 or 5 that fall outside the Optimus
base template (shop, blog, quiz, Instagram, hero, services, testimonials, pricing).
Flag these as `🔧 CUSTOM BUILD REQUIRED — [feature name]`.

---

## PHASE 2 — RESOLVE INTAKE GAPS

**Phase 2 trigger (deterministic):**
Phase 2 runs IF AND ONLY IF initial-business-data.md contains at least one `⚠️ NOT FOUND` marker after Phase 1 completes. If Phase 1 completes with zero `⚠️ NOT FOUND` markers, skip directly to Phase 3. Do not run Phase 2 "just to double-check" — the gap resolution interaction is batched; skipping it when unnecessary saves a round-trip with Anthony.

Review the filled `initial-business-data.md`. Collect every `⚠️ NOT FOUND` flag
in Sections 1–6 (these are the sections `/prime` relies on most).

If there are any flags, compose a single message with all of them:

```
I've completed the intake for [BUSINESS_NAME]. Before I can run market research,
I need a few things I couldn't find from the [source]:

1. [Field name]: [why it matters]
2. [Field name]: [why it matters]
...

Please answer each one — I'll update the file and continue.
```

Wait for the user's response. Update `initial-business-data.md` with their answers.
Then proceed.

If Section 6 (Goals & Timeline) is entirely empty, always ask — `/prime` needs
`[LAUNCH_TARGET]` and `[KEY_GOAL]` to be real, not placeholder values.

---

## PHASE 3 — MARKET RESEARCH

**Goal:** Produce a fully filled `market-intelligence.md`.

First, check whether `market-intelligence.md` is already filled (contains real
competitor names, pricing data, and strategic content). If it looks complete,
skip to Phase 4.

Read `initial-business-data.md` in full. Extract:
- Business type, location, core offer, target audience
- Competitors named in Section 8
- Conversion goal from Section 5
- Pricing from Section 2

These are your research seeds.

**Execute the following research — in order, using web search:**

### 3A — Competitor Research
Start with any competitors named in `initial-business-data.md` Section 8.
Search for 2–3 additional competitors in the same category (same geography or
national competitors in the same niche) that the client may not know about.

For each competitor (3–6 total), visit their site and record:
- Positioning (how they describe themselves)
- Strengths and weaknesses (be specific — not "good design" but "full-screen hero
  with immediate booking widget, no pricing visible")
- Price point (exact if public, estimated range if not)
- Primary conversion mechanism (what does clicking the main CTA do?)
- Design quality score 1–10 with brief justification

### 3B — Pricing Intelligence
Search for: "[service type] pricing", "how much does [service] cost", Reddit or
forum discussions about this category's pricing. Identify the market price floor,
mid-market, and premium tier. Note how competitors anchor price.

### 3C — Audience Research
Read Google, Yelp, or relevant platform reviews for 2–3 competitors.
Extract verbatim phrases people use when describing their problem and their
desired outcome. These are headline candidates.

Search Reddit and forums for questions buyers ask in this category.
Note buying triggers (what made them decide) and blockers (what made them hesitate).

### 3D — SEO Research
Search for the core service + location combination to see who ranks and why.
Identify 5 primary keywords with intent (transactional / informational / local).
Find 3 long-tail queries that competitors aren't answering well.

### 3E — Design & Conversion Landscape
Open the top 3–5 competitor sites and note:
- Dominant visual style in the category (color palette patterns, typography, photography)
- What every site does (table stakes)
- What no site does (gap = opportunity)
- What trust signals are expected in this market

### 3F — Feature Gap Analysis
**Target 4-6 real gaps.** If fewer than 4 real gaps surface after auditing at least 3 competitor sites, output WHAT YOU FOUND plus a short note explaining why the competitive field has no larger gap. Never fabricate gaps to reach 4.

For each gap:
- What competitors are missing
- Why it matters to the target buyer
- Whether closing it requires a `🔧 CUSTOM BUILD REQUIRED` beyond the Optimus base template

### Synthesize
Write all 9 sections of `market-intelligence.md`:
1. Executive Summary (write this last)
2. Target Audience Deep Dive
3. Competitor Analysis (one block per competitor)
4. Pricing Intelligence
5. Feature & Content Gap Analysis
6. SEO & Content Opportunities
7. Conversion Patterns
8. Design & Aesthetic Landscape
9. Strategic Recommendations

Write the filled content to `market-intelligence.md`, overwriting the template.

If any section cannot be completed due to limited search results, note it explicitly
in the file and flag it in the Phase 4 summary.

---

## PHASE 4 — PREPARE /PRIME

**Goal:** Fill all 10 variables in `project-prime.md` and save it as
`.claude/commands/prime.md`, ready to execute.

Extract each variable from `initial-business-data.md`:

| Variable | Source |
|----------|--------|
| `[BUSINESS_NAME]` | Section 1 — Business Name |
| `[DOMAIN]` | Section 5 — Domain |
| `[BUSINESS_TYPE]` | Section 1 — Business Type |
| `[LOCATION]` | Section 1 — Location |
| `[LAUNCH_TARGET]` | Section 6 — Launch target |
| `[PRIMARY_AUDIENCE]` | Section 3 — Ideal client description (compress to one phrase) |
| `[CORE_OFFER]` | Section 2 — Primary service or product |
| `[KEY_GOAL]` | Section 6 — Primary goal for the website |
| `[BOOKING_ENGINE]` | Section 5 — Booking or conversion tool |
| `[SCHEMA_TYPE]` | Section 5 — Schema.org type |

For any variable still marked `⚠️ NOT FOUND` or genuinely ambiguous, add it to
a question batch. Compose a single message:

```
Almost ready to run /prime. I need to confirm a few values I couldn't confidently
infer from the research:

1. [Variable]: [options or context]
2. [Variable]: [options or context]
...
```

Wait for answers. Then:
1. Find-and-replace all 10 variables in `project-prime.md`
2. Create the `.claude/commands/` directory if it doesn't exist
3. Save the filled file as `.claude/commands/prime.md`

---

## PHASE 4 SUMMARY — CONFIRM BEFORE /PRIME

Before executing Phase 5, output a full summary for user approval:

```
PRE-BUILD COMPLETE — READY TO RUN /PRIME
──────────────────────────────────────────
Client:           [BUSINESS_NAME] ([DOMAIN])
Business type:    [BUSINESS_TYPE]
Location:         [LOCATION]
Launch target:    [LAUNCH_TARGET]
Primary audience: [PRIMARY_AUDIENCE]
Core offer:       [CORE_OFFER]
Key goal:         [KEY_GOAL]
Booking engine:   [BOOKING_ENGINE]
Schema type:      [SCHEMA_TYPE]

Research complete:
  ✓ initial-business-data.md — [count] / 8 sections filled
  ✓ market-intelligence.md — 9 / 9 sections filled
  ✓ Competitors analyzed: [names]
  ✓ Key strategic insight: [one sentence]

Custom builds flagged (beyond base template):
  [list, or "None — base template sufficient"]

Open questions carried into /prime:
  [list any unresolved flags, or "None"]

──────────────────────────────────────────
Type GO to execute /prime and build the project foundation.
Type STOP to review the research files before proceeding.
```

Wait for the user's response.

---

## PHASE 5 — EXECUTE /PRIME

Read `project-prime.md` (the filled version now at `.claude/commands/prime.md`)
in full. Execute Tasks 1 through 5 exactly as specified in that file:

- **Task 1:** Complete CLAUDE.md — fill all 10 variables
- **Task 2:** Create `progress.md`
- **Task 3:** Create `design-system.md` — synthesize from `market-intelligence.md`
  and `initial-business-data.md`
- **Task 4:** Scaffold the Next.js project per `website-build-template.md`
- **Task 5:** Deliver the full debrief (pre-read confirmation, strategic insights,
  critical problems, design system summary, sections in/out/add, Phase 1 task list,
  blockers)

Do not skip tasks. Do not proceed to Task 4 until Task 3 is complete.
Update `progress.md` as each task completes.

---

## PHASE 1J — `/ultrareview` (new in 4.7)

Prerequisite: Phase 1I pre-launch-auditor + Section 11 browser audit must have passed (zero console errors at all viewports, all file-level FAIL items resolved, all DEFERRED items confirmed in browser audit).

Run `/ultrareview` on the full working tree. This is a Claude Code 4.7 slash command — a dedicated review session that reads changes and flags bugs and design issues a careful reviewer would catch. Pro/Max plans get 3 free per session.

Findings triage:
- BUG-severity → block launch, resolve before demo URL goes to client
- DESIGN-severity → review with Anthony, either fix or explicitly waive (waivers logged in pre-launch-audit.md §Ultrareview Findings with one-line rationale)
- PASS with no findings → launch cleared

Log all findings to `pre-launch-audit.md` under `§Ultrareview Findings`. This is the final gate before the client demo URL is sent.

See [knowledge/patterns/ultrareview-as-pre-launch-gate.md](knowledge/patterns/ultrareview-as-pre-launch-gate.md) for triage detail.

---

## AFTER PROJECT CLOSE — Run /retro

When the project is done (or at any natural milestone), run `/retro` from the
Claude Code CLI terminal inside the project folder. It will:
- Scan `progress.md` + git log for new learnings
- Compare against the Optimus knowledge vault
- Write only new errors, patterns, and retrospective entries — no duplicates
- Flag any toolkit workflow gaps discovered

This closes the loop. Every build makes the next one smarter.

---

Begin. Announce Phase 0 and check for required files now.
