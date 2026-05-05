# Autonomous Business Grounding — Move Identity Discovery Upstream into Intake

## Context

Anjo Services research session anchored to Salem NH because Anthony said "we are salem nh based" mid-prompt. That answer referred to Optimus the agency, not Anjo the client. Claude treated it as fact and ran 12 minutes of deep research against the wrong competitive field. Kimi K2.6, given the same `initial-business-data.md`, ran HomeAdvisor + BuildZoom + Nextdoor lookups by business name, cross-checked against the (978) phone area code, and correctly identified Methuen MA as Anjo's actual base — then pulled real Anjo customer reviews ("These were the nicest guys I think I have ever dealt with", "Fair prices, 5 stars, 5 years") as testimonial seeds.

The earlier framing of this fix ("treat verbal answer as hypothesis, verify in research") was wrong. The right framing is **autonomy**: every LLC, contractor, and service business has a public footprint across registries, directories, and social platforms. The system should find it autonomously rather than asking Anthony to fill `⚠️ NOT FOUND` flags. The goal is fewer flags surfacing to Anthony, not more verification rituals.

The architectural decision: **business-identity grounding belongs in intake, not market-research.** Intake's concern is "what is this business?" — that should include the public footprint, not just the client's own website. Market-research's concern is "what is the market around this business?" — competitors, audience, pricing, SEO. Conflating those produces fragmented artifacts and forces every downstream agent to read two files instead of one.

`initial-business-data.md` becomes the single source of truth: externally-grounded location, base city, service area, ownership, license numbers, social profiles, and review counts — all filled by intake from public sources. Market-research builds on a verified base rather than verifying it.

## The split

- **Intake** finds the FACTS about the business: where, who, when, registered LLC name, license numbers, social profiles, review counts and average stars, photo presence. External, structured, autonomous.
- **Market-research** mines VOICE + MARKET: verbatim quotes from reviews intake already located (for content-writer testimonial voice), audience psychology, competitors, pricing benchmarks, SEO/AEO opportunities. Market positioning, not identity.

## Files to modify

1. `c:\Projects\Optimus Assets\intake-prompt.md` — add external business grounding as a new step (primary work)
2. `c:\Projects\Optimus Assets\market-research-prompt.md` — lighter hardening; assume identity is locked upstream
3. `c:\Projects\Optimus Assets\.claude\agents\onboarding\market-researcher.md` — sync with research prompt

There is no separate intake agent file (verified — only `market-researcher.md` and `design-synthesizer.md` exist under `.claude/agents/onboarding/`). `/intake` runs as a slash-command that reads `intake-prompt.md`. So intake changes land in one file.

## Changes

### 1. intake-prompt.md — Add Step 1.5: External Business Grounding (autonomous)

New step inserted between current Step 1 (gather source material) and current Step 2 (fill `initial-business-data.md`). Runs in BOTH Mode A (URL crawl) and Mode B (raw notes), because every business has external grounding regardless of whether a website exists.

**Goal:** fill every field that is publicly findable about THIS business so the human is asked only for things genuinely private (revenue targets, budget, internal goals, brand values not stated publicly).

**Sequence — search by exact business name (and DBA / common variants if surfaced):**

| Source | What to extract |
|---|---|
| Google Business Profile / Google Maps | Address, base city, phone, hours, services, photo count, review count, avg star, verified status |
| Facebook business page | Location, owner-presence signals, review count, photo presence |
| Yelp | Address, services, review count, avg star |
| HomeAdvisor / Angi (niche-conditional) | License badges, review count, services list |
| Better Business Bureau | Accreditation status, registered name, address, complaint history |
| Nextdoor | Community recommendation presence (count + tone) |
| State business registry (Secretary of State / corp database) | Registered LLC legal name, registered agent, registered address, formation date |
| State licensing database (niche-conditional — MA HIC, NH contractor license, state cosmetology, real estate, etc.) | License numbers, license status, expiration, named license holder |
| Phone area-code lookup | Geographic consistency check against everything above |
| WHOIS for the domain | Registrant address (often privacy-protected; useful when not) |

**Cross-reference logic:**
- If 2+ sources agree on base city + street address, lock it in.
- If sources disagree (GBP says Methuen, BBB says Lawrence), record all evidence in the field value and flag the discrepancy explicitly with `⚠️ DISCREPANCY — [source A says X, source B says Y]`. Do not silently pick one.
- Phone area-code check: if area code's geographic region disagrees with the discovered base city, flag the contradiction — it's usually a moved-business signal worth surfacing.

**Fields filled by Step 1.5 (overwriting `⚠️ NOT FOUND` from Step 1 wherever external evidence exists):**

- Section 1: Location, Base city, Service area, Years in operation (use registry formation date if more authoritative than the about page)
- Section 2: Service radius (where stated on directories)
- Section 4: Photography available (real photos on FB/IG/Yelp/GBP — describe what's there + where), Logo (higher-quality logo if surfaced externally)
- Section 5: Social profiles (every live link found, not just what was on the client site), Existing forms / lead tools (CTAs Yelp / GBP / FB push)
- Section 7: Testimonials (record platform list + count + avg star — VERBATIM QUOTE pull deferred to market-research where it's mined for voice), Quantifiable results (years operating from registry, total review count across platforms), Certifications (license numbers from state databases — the MA HIC, the CSL, etc.)

**Fields Step 1.5 does NOT touch:**
- Section 3: Pain points, transformation, hesitation, decision triggers — these come from market-research's audience-psychology mining, not from the business's own footprint
- Section 6: Goals, revenue targets, launch dates, constraints — genuinely private
- Section 8: Competitors — market-research's job

**`⚠️ NOT FOUND` discipline after Step 1.5:**
The flag survives only on fields that are GENUINELY not publicly discoverable (revenue targets, internal goals, deeply private values). The bar for surfacing a `⚠️ NOT FOUND — confirm with client` flag is now: "I searched all 10 sources above and found nothing." Sources searched + nothing-found notes get logged in the INTAKE COMPLETE summary so Anthony can see effort was made.

**INTAKE COMPLETE summary update:**

Add to the existing block:

```
External grounding sources searched: [list of 10 sources]
External grounding fills:
  • Section 1 Location: [filled from GBP + state registry]
  • Section 1 Base city: [filled from GBP + BBB]
  • Section 4 Photography: [12 project photos on Yelp + FB]
  • Section 7 Testimonials: [HomeAdvisor 23 reviews 4.9★, Google 41 reviews 4.8★]
  • Section 7 Certifications: [MA HIC #198765 verified live]
Discrepancies flagged: [count + brief description, or "none"]
```

### 2. market-research-prompt.md — Lighter hardening, builds on grounded intake

With identity locked upstream, market-research no longer carries the verification burden. The hardenings that survive:

**a. Drop the planned "Step 0 Location Verification" block.** Identity is intake's job. Research instead opens with a one-line precondition: "Read `initial-business-data.md`. The base city, service area, license numbers, and social profile list are externally grounded — research builds on them. If any of those are still flagged `⚠️ NOT FOUND` in intake's output, surface as `[BLOCKED-ON: Intake grounding incomplete]` and stop."

**b. Add "Real Reviews of THIS Business — verbatim quote pull" to Audience research process.** Intake located the platforms + counts. Research mines them for verbatim language. For every platform intake surfaced (Google, FB, HomeAdvisor, BBB, Nextdoor, Yelp), pull 5–10 verbatim quotes that capture how this audience actually talks. These feed content-writer's testimonials section directly. Even one real quote ("These were the nicest guys I think I have ever dealt with") beats fabricated personas.

**c. Three-tier competitor breakdown in Section 3.** Replace the "3–6 competitors, at least 2 from your own research" block with explicit tiers tagged in the output:
  - `[DIRECT]` — 3-4 head-to-head competitors. Same SERP, same town/region, same price tier. These are who the client actually loses leads to. Discover by searching the queries the buyer searches: "[service] [verified city]", "[service] near [verified city]", "[service] [verified region]" — pull top organic + map-pack results.
  - `[ADJACENT]` — 1-2 same-region different-tier competitors. Useful for boundary mapping.
  - `[BENCHMARK]` — 1 mandatory national best-in-class site. Design-synthesizer aspiration target.

**d. Section 2 persona gate.** Persona must include: first name, specific life situation, tight age window (5-12 year span max), regional-median-grounded income bracket, and one verbatim quote from a real review of this business (from item b). Reject any persona that reads as a demographic bracket.

**e. Section 9 exploit categories.** Three required exploits, each citing a specific finding:
  - **Timing exploit** — when does the audience search? When are competitors unavailable?
  - **Competitor-specific exploit** — named competitor + observed failure + how this client steals from it
  - **Content/AEO exploit** — unanswered high-intent query this client can own with one page

**f. FINAL STEP completion summary additions:**
```
Direct competitors:    [list of [DIRECT] tagged competitors]
National benchmark:    [name + URL]
Real reviews quoted:   [count across all platforms]
Audience verbatim phrases captured: [count]
```

### 3. .claude/agents/onboarding/market-researcher.md — sync

Mirror the research prompt changes:
- Update **Required Reading** note: "Identity (location, license, social) is grounded by intake. Trust intake's output; do not re-verify."
- Add **Section 1.5: Pull verbatim review quotes from platforms intake located**.
- Restructure Section 3 around the three-tier `[DIRECT]/[ADJACENT]/[BENCHMARK]` breakdown.
- Update **Validation** checklist:
  - "Section 2 contains ≥1 verbatim quote per platform intake located OR explicit `Zero verbatim quotes available — [N reviews behind login wall]` note"
  - "Section 3 contains 3-4 [DIRECT], 1-2 [ADJACENT], 1 [BENCHMARK]"
- Update **Handoff** report fields to match the new completion summary.

## Verification

1. **Diff check.** Confirm all changes landed in three files: intake-prompt.md (Step 1.5 + summary update), market-research-prompt.md (5 changes a-f), market-researcher.md (mirror of research changes).

2. **Anjo regression thought-experiment.** Trace the new intake against Anjo:
   - Mode A scrape of anjoservices.com flags Location/Base city/Service area as `⚠️ NOT FOUND` (current behavior).
   - Step 1.5 — search "Anjo Services" across the 10 sources.
     - Google Business Profile: returns address (likely Methuen MA), phone (978) 216-6455, hours, photos, review count.
     - HomeAdvisor: surfaces review count + license badge + verified address.
     - State of Massachusetts business registry: surfaces "Anjo Services LLC" registered name, registered agent, formation year, registered address.
     - State of Massachusetts HIC database: surfaces Tony Squillini's HIC license number.
     - Phone area-code 978 → Merrimack Valley MA → matches discovered base city → PASS.
   - Step 2 fills initial-business-data.md with externally-grounded values.
   - INTAKE COMPLETE summary shows all 10 sources searched, fills produced.
   - When market-research runs, it opens to a complete, verified base. Competitor SERPs return Skillville Corp, JJ Handyman, Dan Hickey from the start. No second-guessing the location.
   The scenario would have been caught at intake, not 12 minutes into research.

3. **Cold-read pass.** Read all three updated files end-to-end as a fresh subagent. Are the 10-source sweep, three-tier competitor structure, and discrepancy-flagging executable without ambiguity? Fix any gaps.

4. **Plan preservation.** Per CLAUDE.md Plan Preservation Rule, copy this plan file to `c:\Projects\Optimus Assets\autonomous-business-grounding-intake.md` BEFORE making any changes. Commit plan + all three file edits in the same git commit so plan and implementation stay linked in git history.

## Out of scope (flagged for later)

- **Re-running Anjo's intake + market-research with the hardened prompts.** Recommended as the immediate next workflow — produces a re-grounded `initial-business-data.md` and a regenerated `market-intelligence.md` for the client build. Not bundled into this plan because the prompt-hardening is the prerequisite work.
- **Consolidating market-research-prompt.md and market-researcher.md.** They duplicate methodology today. Real fix is to make the agent file `Read`-and-defer-to the prompt file (single source of truth). Out of scope here; flagged as a known smell.
- **Tooling / MCP server selection for the 10-source sweep.** The plan describes WHAT to search, not WHICH tool to use for each lookup. WebSearch + WebFetch handle most of it; some niche lookups (state contractor databases) may need direct URL fetches. Tool selection is left to the executing session.
