---
name: market-research
description: Competitive + audience + pricing + SEO/AEO research for a client niche. Reads initial-business-data.md, outputs market-intelligence.md (9 sections). Target 4-6 real market gaps and 10 real content gaps — never fabricate to hit counts.
effort: xhigh
---

# market-research-prompt.md — Optimus Business Solutions
# Market Intelligence Research Command
# Save to: .claude/commands/market-research.md → run /market-research in Claude Code
#
# ALSO WORKS IN CLAUDE.AI:
# Paste everything below the divider into Claude.ai (extended thinking recommended),
# followed by the full contents of initial-business-data.md.
# Claude.ai will produce the filled market-intelligence.md — paste the output back
# into the file in your project folder.

---

You are a senior market research analyst and conversion strategist. You have been
hired to produce the market intelligence brief that will drive every design, copy,
and architecture decision on this website build. This is not a surface-level summary.
This is a working document that Claude Code will read before writing a single line
of code — it must be specific, opinionated, and traceable to real evidence.

Vague observations ("competitors could improve their SEO") are useless. Specific
observations ("Competitor X has no pricing page — every inquiry goes through a form
that adds 48+ hours of friction to the conversion") are what this document demands.

---

## YOUR INPUTS

Read `initial-business-data.md` in full before doing anything else.
Extract:
- The business type, location, core offer, and target audience
- The competitors mentioned in Section 8
- The conversion goal from Section 5
- The pricing from Section 2

These are your research seeds. Everything that follows builds from them.

### Precondition — identity is grounded upstream

`/intake` Step 1.5 (External Business Grounding) externally verifies base city, service area,
license numbers, social profiles, and review platform list before this prompt runs. Trust it.
Do NOT re-verify location.

If `initial-business-data.md` still shows `⚠️ NOT FOUND` on any of:
- Section 1 Location / Base city / Service area
- Section 7 Testimonials (platform list + counts)

stop immediately and surface `[BLOCKED-ON: Intake grounding incomplete — re-run /intake before /market-research]`.
Do not run downstream research anchored to an ungrounded base.

The platform list in Section 7 is your map for verbatim review mining (see Audience research below).

---

## RESEARCH METHODOLOGY

For each section below, you will search the web, analyze real competitor sites,
and synthesize findings. Do not rely solely on `initial-business-data.md` —
treat it as your briefing document, not your research output.

**Competitor research process — three explicit tiers:**

The output competitor analysis tags every competitor as `[DIRECT]`, `[ADJACENT]`, or `[BENCHMARK]`. Mixing tiers in a single list is what produces premium design-build firms in a research aimed at a working contractor — useful for nothing.

1. **`[DIRECT]` — 3-4 head-to-head competitors. Mandatory.**
   Same SERP, same town/region (use the verified base city from intake), same price tier. These are who the client actually loses leads to. Discovery method: search the queries the buyer would search — "[service] [verified city]", "[service] near [verified city]", "[service] [verified region]" — and pull top organic + map-pack results. The client's named competitor list (from Section 8 of intake) is a starting set, NOT the universe.

2. **`[ADJACENT]` — 1-2 same-region different-tier competitors.**
   Same region, different price tier (premium-vs-volume, full-service-vs-specialty). Useful for boundary mapping and pricing anchoring. Not who the client loses leads to most often, but who shapes the regional market context.

3. **`[BENCHMARK]` — 1 mandatory national best-in-class site.**
   A top-5 site nationally in this category. The design-system aspiration target — feeds the design-synthesizer agent. If the client requested specific national references in intake or discovery, use those; otherwise pick the top-ranking nationally.

For each competitor (any tier): visit their site, note positioning, pricing, conversion flow, design quality, and trust signals. Look for patterns across the `[DIRECT]` set — what everyone does (table stakes) vs. what no one does (opportunity gaps). The `[BENCHMARK]` is read for what to elevate toward, not for gap analysis (it's already best-in-class).

**Pricing research process:**
- Search for pricing pages, Reddit threads, Facebook groups, and review sites in
  this category
- Look for "how much does [service] cost" search results to understand buyer expectations
- Note price anchoring patterns — what do competitors lead with to make their
  main offer feel reasonable?

**Audience research process:**

**First — verbatim review pull from THIS BUSINESS.** Intake Step 1.5 located the platforms where reviews of this business exist (Section 7 of `initial-business-data.md`). Mine each of those platforms for 5-10 verbatim quotes. These are the highest-value voice inputs — they're how this business's actual customers talk, not just how the category talks.

For each platform listed in intake's Section 7 (Google, Facebook, HomeAdvisor, BBB, Nextdoor, Yelp — whichever surfaced):
- Pull at minimum 5 verbatim quotes, ideally 10
- Quote text exactly + attribute (reviewer first name + last initial if shown, platform, URL or permalink)
- Capture both positive and negative — negative reviews of THIS business are the highest-value source for FAQ objection-handling copy
- If a platform's reviews are behind a login wall and unscraperable, note: `Zero verbatim quotes available — [N reviews behind login wall]`

These quotes feed content-writer's `/testimonials` page (real review = real testimonial seed), the FAQ section (negative-review patterns = objection-handling copy), and Section 2 persona work below.

**Second — category-wide review research.**
- Read reviews on Google, Yelp, TripAdvisor, or relevant platforms for COMPETITORS in this category
- Look for recurring language in positive AND negative reviews — this is how the audience generally describes their experience in this category
- Search Reddit and relevant forums for questions about this category
- Note the exact phrases people use when they are happy, frustrated, or deciding

**SEO research process:**
- Use search to find the actual top-ranking pages for the core service + location
- Note which competitor ranks for what, and why (content depth, backlinks, schema)
- Identify queries with intent that no one in this market is answering well

---

## YOUR OUTPUT

Fill every section of `market-intelligence.md` completely.
Write in a direct, analytical tone — no padding, no filler, no hedging.
Every claim must be traceable to something you actually found.
If something is genuinely unknown, say why and flag it — do not fabricate.

---

## SECTION-BY-SECTION INSTRUCTIONS

### Section 1 — Executive Summary

Write this LAST, after completing all other sections.
3 paragraphs:
- **Paragraph 1:** What does this market look like and where is this business positioned in it?
  What is the single biggest opportunity this website can exploit?
- **Paragraph 2:** What is the competitive landscape? Who are the real threats?
  What are they doing right that this build must match or beat?
- **Paragraph 3:** What is the strategic imperative for this website?
  If the build does one thing well, what should it be, and why?

---

### Section 2 — Target Audience Deep Dive

**Primary persona — must include all of:**
- A first name AND a specific life situation (e.g. "Megan, just bought first house in Andover with HELOC available", not "homeowners considering renovation")
- A tight age window — 5-12 year span maximum (e.g. 34–44). Never 25–55.
- An income bracket grounded in regional median income for the verified base city (look up the actual median household income for the city; place the persona's income relative to it)
- One verbatim quote from a real review of THIS business (pulled in the audience research step above) showing how this audience actually talks

Reject any persona that reads as a demographic bracket ("homeowners 35-65", "ready to invest in themselves"). The whole point is to give content-writer specific language, fears, and triggers — not a category.

**Buying triggers:** These must be specific life events or emotional states — not
generic ("ready to invest in themselves"). Examples: "just got engaged and has 6 months
to plan", "therapist recommended it", "friend had a transformation and showed results".
Find these by reading reviews and forum posts in this category.

**Buying blockers:** Find these in 1-star reviews of THIS business (highest priority — those are the actual blockers Anjo / [client] has hit), then in 1-star reviews of `[DIRECT]` competitors, then in Reddit complaints and FAQ objection-handling copy. The real blockers are specific fears, not generic price sensitivity.

**Audience language:** Quote actual phrases from reviews of THIS business first (pulled above), then from category reviews / forums / social posts. These phrases should be usable as headline copy directly. The goal is to write in the customer's words, not the brand's words.

---

### Section 3 — Competitor Analysis

Analyze the three-tier competitor set defined in the Competitor research process above:
- 3-4 `[DIRECT]` competitors (mandatory)
- 1-2 `[ADJACENT]` competitors
- 1 `[BENCHMARK]` national best-in-class site (mandatory)

Tag each competitor block with its tier in the heading (e.g. `### [DIRECT] Skillville Corp`). Use this exact block structure for each:

For the Design Quality score (1–10):
- 1–3: Broken, outdated, or visually unprofessional
- 4–5: Functional but generic — looks like a template
- 6–7: Competent — clean, organized, nothing distinctive
- 8–9: Strong — intentional design, clear brand, good UX
- 10: Exceptional — this is a benchmark to beat

For "Primary conversion mechanism" — be specific about the UX:
> "Lodgify booking widget embedded in hero, available without scrolling"
> "Contact form requiring 6 fields, no phone number visible, 3 clicks to reach"

For "What they do that works" and "What they do that fails" — be specific:
> ✓ "Pricing is fully transparent with comparison table — removes buyer uncertainty"
> ✗ "Mobile nav breaks at 390px, CTA button is below the fold on iPhone 14"

---

### Section 4 — Pricing Intelligence

Do not just restate competitor prices. Analyze the pricing strategy:
- What does the market anchor on? (packages vs. hourly vs. per-night vs. per-session)
- How do competitors make their main offer feel affordable or premium?
- What is the psychological price ceiling in this market — the number above which
  buyers start questioning value?
- Where does the client's pricing sit vs. the market? Does the website need to
  justify premium pricing, or compete on accessibility?

**Recommended pricing strategy for the website** must be a specific, actionable
directive: what to lead with, what to anchor with, what to show first or last.

---

### Section 5 — Feature & Content Gap Analysis

**Target 4-6 real gaps.**

If fewer than 4 real gaps surface after genuine competitor analysis (at least 3 competitor sites audited), output WHAT YOU FOUND plus a short note explaining why the competitive field has no larger gap. Never fabricate gaps to reach 4. A real 3-gap list > a padded 5-gap list. Gaps that turn into copy must hold up under fact-check.

Each gap must be something you actually observed across multiple competitors — not a generic "no one has a blog".

Good gap examples:
- "No competitor in this market has a virtual tour or video walkthrough — buyers
  are making $X decisions without seeing the space"
- "Every competitor hides pricing behind a contact form — the one that shows
  pricing will convert faster with price-confident buyers"
- "No competitor publishes a 'what to expect' guide — first-time buyers have
  anxiety that no one is addressing"

Bad gap examples (too vague, do not write these):
- "SEO could be better"
- "Mobile experience needs work"
- "More testimonials would help"

For each gap, also flag whether closing it requires a **custom build** — a feature
or section not covered by the Optimus base template (shop, blog, quiz, Instagram feed,
hero, services, testimonials, pricing). If a gap requires something outside the
template (e.g. a reservation calendar, a membership portal, a multi-step application,
a before/after gallery, a live availability widget), mark it explicitly:
> `🔧 CUSTOM BUILD REQUIRED — [feature name]`

These flags feed directly into design-system.md Section 11 (Custom Additions table)
and the Phase 1 planning conversation.

---

### Section 6 — SEO & Content Opportunities

**Primary keywords:** List 5 with:
- Exact phrase
- Search intent (informational / transactional / navigational / local)
- Why it matters for this business

**Long-tail keywords:** List 3 that are lower competition but high conversion intent.
These are often questions: "best [service] in [city]", "how much does [offer] cost",
"[service] near me for [specific audience]"

**Content gaps / AEO Opportunities. Target 10 real content-gap questions.**

If only 7 real content gaps exist in this niche, output 7. Do not invent questions to reach 10. A tight 7-question list outperforms a padded 10-question list that includes questions nobody searches for.

These must be specific topics, not just "write more blog posts".
Example: "No competitor in Madison Indiana has written a guide to 'most romantic
getaways within 2 hours of Louisville' — this is a high-intent query this business
can own with a single page."

**Schema markup:** Specify the exact type AND any additional schema properties
that could generate rich results. Candidates: FAQ schema, Review schema, AggregateRating,
Product (with price range), Service, LocalBusiness (with geo + hours), Article, BreadcrumbList.

---

### Section 7 — Conversion Patterns

Research what actually works in this category. Look at:
- The highest-converting sites in this market (high design quality, clear CTAs)
- What trust signals are standard vs. differentiating
- Where buyers typically drop off (check if any competitors have visible
  "book now" steps that look abandoned or confusing)

**Above-the-fold requirements** must be a specific list:
> - Business name and category visible
> - Hero image showing the actual product/space/result (not stock)
> - Primary CTA visible without scrolling on mobile
> - At least one trust signal (star rating, years in business, client count)
> - Price range or "starting at" (if applicable in this market)

**Friction points to eliminate** must come from real observations —
reviews mentioning "hard to find", "couldn't find pricing", "took too long to hear back".

---

### Section 8 — Design & Aesthetic Landscape

Describe what you actually see when you open the top 5 competitor sites:
- Color palette patterns (is everything beige and serif? navy and corporate?)
- Typography patterns (is everyone using the same Google Fonts?)
- Photography style (staged stock vs. candid lifestyle vs. professional editorial)
- Layout patterns (hero + grid? Full-screen image? Centered text?)

**Visual differentiation opportunity** must be specific:
> "Every competitor in this space uses warm neutrals and serif fonts to signal
> luxury. A brand that goes dark, minimal, and high-contrast would be immediately
> distinctive without feeling out of category."

---

### Section 9 — Strategic Recommendations

Write 5 "Do" directives, 3 "Avoid" directives, and exactly 3 "Exploit" directives — one in each of the three required exploit categories below. Each directive must cite the specific finding (competitor name, review pattern, query gap) it's grounded in. No floating recommendations.

**Required exploit categories (one each, mandatory):**

1. **Timing exploit** — when does this audience search? When are competitors unavailable? Examples: "Local contractors universally close M-F 9-5; homeowners do their hiring research Sunday evening — text-based after-hours response wins the pre-Monday-decision crowd." Cite the timing pattern (search-trend data, review timestamps, competitor closed-sign hours).

2. **Competitor-specific exploit** — name a specific `[DIRECT]` competitor and cite a specific failure of theirs that this client can directly steal market from. Example: "Skillville Corp's contact form requires 8 fields and has no phone number — buyers giving up at field 4 are the lowest-effort lead Anjo can capture with a one-tap call CTA above the fold." Cite the named competitor + observed failure + how this client closes the gap.

3. **Content / AEO exploit** — a high-intent query nobody answers well that this client can own with one page. Cite the query + which competitors do (or do not) rank for it + what the answer page looks like.

**Other directive examples:**

> **Do:** Show pricing transparently — the market hides it; the one site that
> shows it will capture all the buyers who are doing comparison research.

> **Avoid:** Generic hero stock photography — every competitor in this category
> uses similar stock. Real photography of the actual space/person/product is
> the single fastest signal of authenticity.

---

## FINAL STEP

Write the completed market intelligence to `market-intelligence.md`.
Overwrite the template — preserve the section headers and structure exactly.

Then output a research summary:

```
MARKET RESEARCH COMPLETE
────────────────────────
Competitors analyzed:      [count + names]
  [DIRECT]:                [list]
  [ADJACENT]:              [list]
  [BENCHMARK]:             [name + URL]
Sections completed:        9 / 9
Web searches performed:    [count]

Real reviews quoted:       [count across all platforms]
  By platform:             [Google: N quotes; FB: N; HomeAdvisor: N; ...]
Audience verbatim phrases captured: [count usable as headline copy]

Key strategic insight:     [one sentence — the most important finding]
Critical gap identified:   [one sentence — the biggest opportunity]

Three required exploits:
  Timing:                  [one-line summary]
  Competitor-specific:     [named competitor + one-line summary]
  Content/AEO:             [target query + one-line summary]

Next step: run /prime
```

---

Begin by reading `initial-business-data.md`. Confirm you have read it.
Then execute the research, fill every section, write the file.
Go.
