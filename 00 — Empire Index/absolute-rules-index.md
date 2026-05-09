# Absolute Rules Index

**Purpose:** canonical enumeration of every CLAUDE.md absolute rule (language: "never," "always," "ever," "no exceptions," "non-negotiable") with verbatim text + anchor + the operational test that detects a violation.

**Used at:** Stage 1B human checkpoint (every build) — orchestrator runs the cross-check procedure at the bottom of this file before approving design-system.md. Also Stage 1H pre-launch-auditor reference.

**Source of truth:** the canonical CLAUDE.md at vault root (`C:\Projects\Optimus Assets\CLAUDE.md`). When a per-project CLAUDE.md says something different, it's a templating drift bug — the canonical wins.

**Maintenance:** when CLAUDE.md gains a new absolute rule, add it here in the same commit. When a rule is softened or removed, archive its row here with a strikethrough + commit hash. **Never delete a row** — historical violations referenced in build-log.md need their target to remain resolvable.

---

## How to read this index

Each rule has four fields:
- **Verbatim** — the exact language from CLAUDE.md (single sentence, copy-paste).
- **Anchor** — CLAUDE.md line reference at time of writing (canonical vault file).
- **Operational test** — what you literally check to catch a violation. A verdict here is binary: PASS or FAIL.
- **Common violation** — the pattern future-you will pattern-match into if not held back by this index.

A rule that fails an operational test is a build failure. Not a discussion, not a tradeoff — a build failure. The orchestrator's job at the Stage 1B checkpoint (and everywhere else this index is invoked) is to run the operational test, not to negotiate the rule's applicability.

---

## §1 — Plan Mode Rule

| Field | Value |
|---|---|
| Verbatim | *"Before writing ANY code — before touching a single file — enter Plan Mode. ... Get alignment on the plan before the first keystroke. This is non-negotiable."* |
| Anchor | CLAUDE.md §"Plan Mode Rule" (line ~17) |
| Operational test | Has the orchestrator presented a written plan and gotten approval before any file edit this session? |
| Common violation | "I'll just make this small change inline" — five edits later you've shipped 200 lines without a plan. |

---

## §2 — Optimus Positioning Rule (premium luxury-modern-2026)

| Field | Value |
|---|---|
| Verbatim | *"Every Optimus site ships as a premium, modern, 2026-era build with UI/UX engineered for conversion. This positioning is non-negotiable regardless of client industry, tier, spend, or market segment."* |
| Anchor | CLAUDE.md §"Optimus Positioning Rule" (line ~258) |
| Operational test | Open the homepage at 1440 + 390. Does it visually compare favorably to Linear / Stripe / Vercel / Raycast / Superhuman? OR does it look like a Bootstrap template? Latter = FAIL. |
| Common violation | Trade-business build defaults to "casual / approachable / friendly" UI tier mistakenly aligned with copy voice. The COPY voice can be casual. The VISUAL presentation is always premium-modern. |

---

## §3 — No flat solid backgrounds, ever

| Field | Value |
|---|---|
| Verbatim | *"No flat solid backgrounds. Ever. Every section background is a gradient with subtle motion by default — this applies to BOTH dark and light sections, across ALL pages, not just the homepage hero."* |
| Anchor | CLAUDE.md §"Homepage Section Architecture Rule" → "Background depth & motion" (line ~791) |
| Operational test | Scroll the full page at 1440 and 390. Every section MUST show a multi-stop radial / conic / mesh gradient. If any section reads as solid fill at any breakpoint = FAIL. |
| Common violation | Long-form text sections (blog body, FAQ, legal) erroneously render flat under the assumption that "static-gradient exception" means "flat is OK." The exception is for MOTION; the gradient is still required. |

---

## §4 — Hero Architecture Rule — No photos in the hero, ever

| Field | Value |
|---|---|
| Verbatim | *"Every hero ships with exactly 3 layers. No exceptions. No photos in the hero, ever — a photo placeholder in the hero is a build failure. The client photo belongs in the About section."* |
| Anchor | CLAUDE.md §"Hero Architecture Rule" (line ~545) |
| Operational test | Open the hero at 1440 and 390. Does any `<img>` / `<Image>` / photo container render anywhere inside the hero `<section>`? If yes = FAIL. |
| Common violation | design-synthesizer cites a competitor pattern (e.g., Claro Advisors single-subject lifestyle) to justify a two-column hero with a photo on the right. Built once on Helen Grondin (Pattern #28); rebuilt on Ead Financial (Error #55). The "movie-hero" full-bleed cinematic backdrop is OK; the "box with a photo in the header" two-column is NEVER OK regardless of which reference site is cited. |

---

## §5 — Hero CTAs always primary=booking, secondary=quiz

| Field | Value |
|---|---|
| Verbatim | *"Primary CTA is always booking. Drives directly to the booking calendar... NEVER 'Call Now' — phone CTA belongs in the nav bar, not the hero. Never 'Learn More' or 'See Our Work.' Secondary CTA is always the quiz. Links to /quiz with label from hero.ctaSecondary. Never a webinar, info session, events page, or external link."* |
| Anchor | CLAUDE.md §"Hero Architecture Rule" (lines ~569-571) |
| Operational test | Inspect Hero.tsx CTA hrefs. Primary must route to `/booking` (or `<BookingCalendar>`). Secondary must route to `/quiz`. Any other destination = FAIL. |
| Common violation | content-writer ships "Call Now" + "Learn More" because the brand brief said "we want phone calls" — fix is phone CTA in nav bar, not hero. Or secondary CTA links to an event / webinar / external page. |

---

## §6 — H1 = tagline always, with shimmer

| Field | Value |
|---|---|
| Verbatim | *"H1 = siteConfig.tagline always, with shimmer. The tagline IS the H1 — emotional hook copy goes in the subheadline, never the H1. The H1 always receives `.hero-shimmer`."* |
| Anchor | CLAUDE.md §"Hero Architecture Rule" (line ~565) |
| Operational test | Inspect Hero.tsx — does H1 render `siteConfig.hero.h1WithEmphasis` (or equivalent tagline field)? Does it carry `.hero-shimmer` class (or equivalent shimmer device, e.g. `EmphasizedText shimmerOnEm`)? If either = FAIL. |
| Common violation | content-writer puts emotional hook in H1 ("Save more on taxes — we'll show you how"), tagline gets demoted to subhead. Or shimmer is omitted because brass color "looks fine on its own." |

---

## §7 — Hero text always readable

| Field | Value |
|---|---|
| Verbatim | *"Hero text must always be readable. Hero headings + body always use `color: var(--text-primary)` (#f5f5f5 on dark builds). If background is dark and text is dark, it's a build failure."* |
| Anchor | CLAUDE.md §"Hero Architecture Rule" (line ~567) |
| Operational test | Read every word in the hero without highlighting at 1440 and 390. If any word requires highlighting to read = FAIL. |
| Common violation | Cream-on-cream builds use `text-secondary` for subhead body (low contrast), or dark builds hardcode a hex that doesn't track the theme variable. |

---

## §8 — Always-Built Features — no exceptions

| Field | Value |
|---|---|
| Verbatim | *"Every project ships with ALL of the following, no exceptions, no client-by-client decisions: [pricing page, interactive quiz, inline booking calendar, testimonials page, blog, shop]."* |
| Anchor | CLAUDE.md §"Always-Built Features Rule" (line ~576) |
| Operational test | At pre-launch audit time: does `/pricing` exist? `/quiz` exist + 2 CTA placements (nav header + homepage block)? `/booking` exist with custom inline calendar (NEVER iframe redirect)? `/testimonials` exist with 36 entries + pagination 9-per-page? `/blog` exist with ≥9 articles? `/shop` scaffolded with seeded fallback? Any "no" = FAIL. |
| Common violation | Sales conversation goes "client said they don't need testimonials" — orchestrator drops testimonials. The rule is no client-by-client decisions: ship all. |

---

## §9 — Pricing page structure non-negotiable

| Field | Value |
|---|---|
| Verbatim | *"Fixed Optimus pricing structure — same on every build, never customized per client: Starter $1,500 / Pro $3,000 / Premium $5,500. Pro gets the 'Most Popular' badge. Starter and Premium are anchors. Premium never gets a badge."* |
| Anchor | CLAUDE.md §"Always-Built Features Rule" → "Pricing Page" (line ~588) |
| Operational test | Open `/pricing`. Three tiers at $1,500 / $3,000 / $5,500. Pro has "Most Popular" badge. Premium has no badge. Any deviation = FAIL. |
| Common violation | Premium gets a "Best Value" badge because it intuitively feels right — kills the anchoring strategy. |

---

## §10 — Pricing page never mentions deposit or Google

| Field | Value |
|---|---|
| Verbatim | *"'Deposit,' 'upfront,' or any payment-split language. The price is the price. Anthony offers deposit splits verbally as a backup close — it is never on the page. Any Google service on any tier — not 'Google Business Profile optimization,' not 'Google Ads setup,' not 'Google Analytics,' not any Google product. Optimus does not offer Google services."* |
| Anchor | CLAUDE.md §"Always-Built Features Rule" → "Never include on pricing page" (line ~605) |
| Operational test | `grep -i "deposit\|upfront\|google" /pricing/page.tsx site.ts` — any match = FAIL. |
| Common violation | content-writer leaks "Google Business Profile optimization" from a generic SEO template. Witt's Restoration (Error #45) shipped with this. |

---

## §11 — Booking calendar always custom inline, never iframe redirect

| Field | Value |
|---|---|
| Verbatim | *"Custom-built calendar UI — a date picker that looks completely native to the site... Lives on a dedicated /booking page AND as a homepage teaser section. NEVER implemented as an href link or Calendly iframe redirect."* |
| Anchor | CLAUDE.md §"Always-Built Features Rule" → "Inline Booking Calendar" (line ~660) |
| Operational test | Inspect /booking page + homepage booking section. Custom React `<BookingCalendar>` component? Or a Calendly iframe / external link? Iframe or link = FAIL. |
| Common violation | "It's just a Calendly iframe with brand colors via URL params, looks fine." Per Error #52-#53 (Collaborative Insights): Calendly's `textColor` is partially broken in dark mode, AND a native pre-picker + Calendly iframe creates double-entry friction that kills conversion. Build the custom UI. |

---

## §12 — Testimonials always 36, 3×3×4 grid

| Field | Value |
|---|---|
| Verbatim | *"36 total. Written by the content-writer agent from scratch... Paginated 9 per page on the /testimonials page (4 pages total = 4 × 9 = 36). Grid is always 3 columns × 3 rows... NEVER use 8 per page... 9 per page is the only number that fills 3 columns perfectly. This is non-negotiable."* |
| Anchor | CLAUDE.md §"Always-Built Features Rule" → "Testimonials Page" (line ~683) |
| Operational test | `/testimonials` page renders exactly 9 entries per page in a 3-col × 3-row grid? Total entries = 36? Any other count or layout = FAIL. |
| Common violation | 32 entries paginated 8-per-page in 3-col grid = 2 full rows + 2 orphans on every page (Helen Grondin Error #31). |

---

## §13 — Zero em dashes in testimonials (string values only)

| Field | Value |
|---|---|
| Verbatim | *"ZERO em dashes (—) in any testimonial. Use commas, periods, ellipses only."* (Em-dash rule scoped to string literals only — JSDoc and line comments are fine.) |
| Anchor | CLAUDE.md §"Always-Built Features Rule" → "Testimonials Page" (line ~691); CLAUDE.md §"Code Standards" / progress.md Stage 1E pre-flight item 1 |
| Operational test | `grep -nE '"\s*[^"]*—[^"]*"' web/src/data/site.ts` (and equivalent for any testimonial-bearing data file) — any match in a STRING value (not a JSDoc/comment) = FAIL. |
| Common violation | content-writer agent treats em dashes as "literary" and lands them in testimonial body or attribution. Or pattern-matches the `[DEMO COPY — pending client review]` marker as license to use em dashes elsewhere. |

---

## §14 — Conversion Flow Rule — never redirect off-domain

| Field | Value |
|---|---|
| Verbatim | *"Never embed third-party redirects that take users off the [BUSINESS_NAME].com domain. All conversion flows (booking, scheduling, purchase, inquiry) must be embedded inline or iframed with seamless visual integration."* |
| Anchor | CLAUDE.md §"Conversion Flow Rule" (line ~837) |
| Operational test | Click every CTA on every page. If any opens `target="_blank"` to a third-party domain (e.g., calendly.com, google.com, hubspot.com) = FAIL. |
| Common violation | "Book a Call" links to `https://calendly.com/<brand>` directly instead of `<BookingCalendar>`. |

---

## §15 — Page Animation Rule — every page is animated

| Field | Value |
|---|---|
| Verbatim | *"Every other page gets ambient effects only — never the full canvas+SVG assembly... Per-page minimums (never static flat)... Shimmer text: `.hero-shimmer` or `.hero-shimmer-sage` on the page H1 — always."* |
| Anchor | CLAUDE.md §"Homepage Section Architecture Rule" → "Animation depth" (line ~742) |
| Operational test | Visit /services, /testimonials, /blog, /about, /contact, /booking, /quiz, every niche landing. Each page must show ambient effects (rising ash particles, twinkles, shimmer, breathing orb). Any page that is fully static = FAIL. |
| Common violation | Interior page agent ships clean typography on flat cream / flat dark and considers the page complete. The hero looks great; everything else looks unfinished — kills the luxury thesis. |

---

## §16 — Subagent Delegation — one level of hierarchy only

| Field | Value |
|---|---|
| Verbatim | *"Orchestrator is the ledger; agents are the executors. ... One level of hierarchy only — non-negotiable."* |
| Anchor | CLAUDE.md §"Agent System Rules" → "Orchestrator is the ledger" (line ~325) |
| Operational test | Inspect agent files in `.claude/agents/` — any agent prompt that spawns another agent? = FAIL. Inspect orchestrator session — any agent that updates progress.md or reads cross-project state? = FAIL. |
| Common violation | A complex agent decides it needs to delegate part of its work to a sub-agent. The hierarchy collapses, state ownership becomes ambiguous. |

---

## §17 — Image Generation Rule — visual review before commit

| Field | Value |
|---|---|
| Verbatim | *"Visual review before commit — non-negotiable. After generating, visually inspect every image before committing... If any image fails visual review, revise the prompt and regenerate. Do not commit artifacts."* |
| Anchor | CLAUDE.md §"Image Generation Rule" (line ~479) |
| Operational test | Pre-commit: every newly-generated `/public/` image opened and visually inspected. Did the orchestrator open each one? If not = FAIL. Any garbled text, deformed subjects, duplicate elements, off-prompt composition = FAIL. |
| Common violation | Bulk generation pipeline runs 16 images, orchestrator commits the batch without opening any. Two have garbled text, one has 7 fingers. |

---

## §18 — Generated assets committed with their task

| Field | Value |
|---|---|
| Verbatim | *"Any script that outputs files into /public must commit those files as part of the same task commit. Generated images, videos, and data files are never a separate follow-up step. Generated assets are part of the task that created them."* |
| Anchor | CLAUDE.md §"Generated Assets Rule" (line ~853) |
| Operational test | After running an asset-generation script: `git status` shows new files. Are they staged + committed in the SAME commit as the script change? If deferred = FAIL. |
| Common violation | "I'll commit the script now and the assets in the next commit so the diff is clean." Two days later the assets are uncommitted and the script can't reproduce them deterministically. |

---

## Cross-check procedure (orchestrator runs at every Stage 1B human checkpoint)

Before approving design-system.md at the end of Stage 1B:

1. **Identify all sections of design-system.md that touch hero, conversion flow, or page architecture.** Sections 5 (composition), 7 (typography device), 11 (sections matrix), 12 (psychology) are the most common touchpoints.

2. **For each touchpoint, run the matching operational test from this index.** Specifically:
   - Section 5 hero composition — check §4 (no photos), §5 (CTA destinations), §6 (H1 = tagline), §7 (text readability).
   - Section 11 Sections Matrix — check §8 (always-built features), §15 (page animation).
   - Any backdrop / motion treatment description — check §3 (no flat solids).

3. **If any test FAILS:** reject design-system.md regardless of how well the agent reasoned about reference patterns to justify the deviation. Reference patterns inform aesthetic + component choices; they cannot override absolute rules. Spawn a correction note back to design-synthesizer with the specific failed test cited verbatim.

4. **If all tests PASS:** approve and proceed to Stage 1C scaffold. Log the cross-check completion in progress.md.

5. **Operational test for the most common violation pattern (hero photo):** "Movie-hero" full-bleed cinematic backdrop = OK. Two-column with photo on right = NEVER OK regardless of which reference site is cited. If the agent's hero composition is "two-column with editorial photo on right," it's a violation — no exception, no Claro citation.

This procedure is also runnable at any other checkpoint (Stage 1D close, Stage 1H pre-launch audit, /retro). Treat any absolute-rule failure as a build failure regardless of how late in the timeline it surfaces.

---

## Cross-references

- `knowledge/patterns/claude-md-absolute-rule-cross-check-at-checkpoint.md` (Pattern #58) — the procedure pattern this index serves.
- `knowledge/errors/claude-md-absolute-rule-override-via-reference-pattern.md` (Error #55) — the prior incident that motivated this index.
- `CLAUDE.md` (vault root) — the canonical source of every verbatim line in this index. When CLAUDE.md changes, update this index in the same commit.
