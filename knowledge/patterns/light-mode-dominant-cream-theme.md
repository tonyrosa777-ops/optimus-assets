# Pattern: LIGHT-MODE-DOMINANT cream theme for financial-services / editorial-register builds

**Category:** Visual Design / Theme Architecture
**First used:** Ead Financial — 2026-05-08

## What

A research-justified deviation from the Optimus default dark-theme template: the entire site ships in **LIGHT mode** with a warm cream `#F5EFE6` background as the dominant tone, deep ink navy `#0F1B2D` text, and a single muted brass accent `#B07D2A`. Used when the competitive landscape is saturated with dark-navy-and-white CPA / financial / professional-services brochure sites and the differentiation thesis depends on visual escape from that zone.

Concrete tokens (Ead Financial Section 2 baseline):

```css
:root {
  /* Cream-dominant ground */
  --bg-base: rgb(245, 239, 230);            /* #F5EFE6 — warm cream / off-white */
  --bg-elevated: rgb(238, 230, 218);        /* #EEE6DA — slightly darker cream for section-boundary alternation */
  --bg-card: rgb(255, 252, 246);             /* #FFFCF6 — near-white warm cream for solid card surfaces */

  /* Deep ink text on cream — AAA contrast (~14.8:1) */
  --primary: rgb(15, 27, 45);
  --text-primary: rgb(15, 27, 45);

  /* Single restrained accent */
  --accent: rgb(176, 125, 42);              /* #B07D2A — muted brass / ochre */

  /* Inverse / dark-section variant — used for ~30% of homepage sections per rhythm map */
  --bg-dark: rgb(15, 27, 45);
  --text-on-dark: rgb(245, 239, 230);
  --accent-on-dark: rgb(208, 156, 68);      /* #D09C44 — slightly lifted brass for AA on dark */
}
```

## When to Use

This pattern applies when ALL FOUR conditions are met:

1. **Competitive landscape is saturated with navy + white + gray.** Document via market-intelligence.md §3 / §8 — every direct competitor uses the same dark-blue-and-white palette. (Ead's competitor set: Honeck O'Toole, Pelletier Chase, KDS, Brannen, Derderian, AAFCPAs, Wolf, KLR. All confirmed navy-dominant.)
2. **Audience makes high-anxiety decisions.** Tax, audit, accounting, financial planning, legal — categories where the buyer's amygdala is engaged (threat response per Schmader & Beilock 2012). Warm color temperature reduces perceived threat (Crowley & Hoyer 1994; Mehta & Zhu 2009); cool palettes signal authority but also distance.
3. **Editorial / boutique register wins over institutional.** market-intelligence.md §8 reference site is in the cream/ink/accent space (Claro Advisors, "boutique New England financial firm" zone) — NOT navy-and-white enterprise (AAFCPAs, KLR).
4. **Differentiation lever needs to be visible in 5 seconds.** Cream-dominant is the highest-leverage visual differentiation lever versus a navy-saturated competitor set. A visitor knows in <5 seconds this isn't another generic CPA brochure site.

NOT applicable when:
- Audience is in a low-anxiety / aspirational decision (luxury hospitality, romantic getaway, cosmetics, consumer entertainment) — those builds win on dark-mode mood lighting, not cream-light considered competence
- Competitors are NOT saturated in navy — if competitors already use cream, this isn't a differentiation lever, it's matching
- Industry conventions strongly require dark mode (gaming, certain DTC tech)

## How

Implementation steps for a LIGHT-MODE-DOMINANT build:

1. **Override CLAUDE.md default dark theme in design-system.md §2.** Document the deviation explicitly with the four-condition justification ("Theme decision: LIGHT-MODE DOMINANT. This is the single biggest deviation from the Optimus default dark-theme template. Justification: ...").
2. **Specify all 9 core CSS custom properties** (the cream-set + ink + accent tokens above) plus the 5 inverse/dark-section tokens for the ~30% of homepage sections that flip dark per the rhythm map.
3. **Solid `--bg-card` for reusable widgets** per Pattern #55 — translucent `Card variant="dark"` overlays render cream-on-cream invisible on cream-dominant backgrounds (build-log Error #54). Reusable widgets MUST self-render solid surfaces.
4. **Functional state tokens** — `--success` chosen to NOT echo any direct competitor's brand color (e.g., for Ead, success is `#2E6649` muted forest, two shades darker than direct-competitor Brannen's forest green). `--error` is burgundy not fire-engine red, to preserve editorial register.
5. **Photography color grade** matches palette — warm cream highlights, slight desaturation in midtones, deep ink shadows. Reads "library / private wealth office," not "tech startup pastel."
6. **Section rhythm**: ~70% light cream sections, ~30% dark ink sections. Hero is cream. Marquee ribbon is dark ink (the editorial cream→navy contrast moment IS the design intent — see [[patterns/cream-on-cream-ambient-gradient-with-brass-mix]] for the hero backdrop that feeds into this transition).

## Key Rules

- **Deep ink navy is the TEXT color, not a hero background.** The reverse (navy hero + cream text) collapses the differentiation thesis — it lands the build right back in the navy-dominant competitor zone.
- **Single accent only.** Brass + cream + ink is the trio. Adding a fourth accent (teal, rose, sage) muddles the editorial register. Variations within the brass family (lifted brass `--accent-on-dark`, brass-tinted cream for ambient gradients) ARE within scope; new hue additions are not.
- **Per-section gradient is mandatory** even on cream sections (CLAUDE.md anti-pattern #14 — no flat solid backgrounds). See [[patterns/luxury-gradient-backgrounds]] (Pattern #51) for the motion vocabulary; cream sections use brass-tinted cream blob via `color-mix(in oklab, var(--accent) 7%, var(--bg-base))`. NEVER use `--bg-elevated` as a gradient blob center on a cream-only section — it's invisible (build-log Error: cream-on-cream gradient invisible).
- **Build-log Error #54 mitigation is non-negotiable** — every reusable widget (BookingCalendar, QuizCard, FAQAccordion, PricingCalculator) self-renders solid `--bg-card` + 1px `--border-medium` + soft shadow. Translucent overlays from the dark-theme default DO NOT WORK on cream.
- **Compatible with Section 12 Psychological Foundations** ([[patterns/section-12-psychological-foundations-design-system]]) — the cream/ink/brass palette has explicit citation grounding (Crowley & Hoyer 1994; Mehta & Zhu 2009). When client asks "why not navy?", the answer is research, not just competitive scanning.

## Reuse Condition

The next Optimus build that hits all four conditions:
- Competitor scan in market-intelligence.md §3 / §8 documents navy-dominance saturation
- Audience is in threat-response decision frame (financial / legal / health-adjacent)
- Editorial / boutique register fits the audience
- Differentiation thesis depends on visual escape from competitor zone

Likely future fits: financial planners, estate attorneys, boutique consulting, niche legal practices, editorial publications. Less likely fits: standard SMB trade businesses (where dark-mode hero is part of Optimus signature), luxury hospitality (which uses dark to evoke private mood lighting), tech startups.

## Related

- [[patterns/cream-on-cream-ambient-gradient-with-brass-mix]] — the matching hero backdrop recipe for cream-dominant builds
- [[patterns/section-12-psychological-foundations-design-system]] — psychological grounding for the cream-vs-navy palette decision
- [[patterns/luxury-gradient-backgrounds]] (Pattern #51) — the broader gradient-backgrounds rule
- [[patterns/reusable-widget-self-sufficient-surface]] (Pattern #55) — why translucent Card overlays break on cream
- [[errors/reusable-widget-card-variant-mismatch]] (Error #54) — the LMP Financial regression that produced Pattern #55
- [[errors/cream-on-cream-gradient-invisible-at-viewport-scale]] — the calibration error this pattern flags
