# Huashu-Extracted Critique Rubric + Anti-AI-Slop Checks

**Pattern category:** Workflow / Visual Design / Quality
**First applied:** Optimus cross-project, 2026-05-02
**Source:** Methodology extracted from [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) — `references/critique-guide.md` and `references/content-guidelines.md`. Huashu Design itself is NOT installed as an Optimus skill (license restriction — see `memory/project_huashu-design-deferred.md`). Only the methodology is adopted, with attribution.

---

## What this pattern is

Two narrow methodology adoptions from the Huashu Design skill, integrated into existing Optimus agent files instead of installing the whole skill:

1. **5-dimension critique rubric** — adopted into `animation-specialist.md` Step 2 (harsh critic evaluation) to sharpen hero concept selection from 4 criteria (Brand fit, Visual impact, Technical feasibility, Uniqueness) to 6 (adds Visual hierarchy + Functionality). Catches concepts that are visually impressive but compete with the H1 + primary CTA — the worst failure mode for a conversion-driven hero.

2. **Anti-AI-slop file-level checks** — adopted into `pre-launch-auditor.md` Section 3B (new) as two FAIL/WARN gates: no figurative SVG illustrations of people/scenes, and no left-accent-border on rounded cards. Both are signature low-effort AI aesthetic patterns that read as "generated, not designed."

## Why it works for Optimus

The existing Optimus design pipeline (design-synthesizer → animation-specialist → pre-launch-auditor → Playwright browser audit) already covers brand synthesis, animation selection, and validation. What it didn't have was:

- **Hierarchy/functionality scoring on hero concepts.** Pattern #7 (Placed Right Fence, Apr 2026) noted "budget for 3 full approaches before final" — implies that the existing 4-dimension critic catches some bad concepts but not all. Adding Visual hierarchy + Functionality to the rubric raises the floor on what wins.
- **File-level detection of two specific AI-signature patterns.** Optimus's Positioning Rule already excludes brutalist/playful/retro-futuristic at the design-system stage. But the AI-signature card pattern and figurative SVG illustrations slip in at the component-implementation stage and aren't caught until the browser audit. Section 3B catches them at file level.

## Why we extracted instead of installing

Huashu Design's license ("个人随便用，企业要打招呼" — personal use free, enterprise must ask first) explicitly names "design outsourcing" and "delivery to paying customers" as requiring prior written authorization. Optimus sells $1,500–$5,500 client websites. Installing the skill globally would put every client build in license-violation territory. The methodology — rubric structure and anti-pattern names — is reusable. The skill's components (ios_frame.jsx, deck_stage.js, animations.jsx, audio library) are not.

Of Huashu's 20 design philosophies, ~12 (cyberpunk / joyful playful / fictional UI / art-deco / experimental code-as-painting) are explicitly forbidden by the Optimus Positioning Rule (Pattern #49). The output format (HTML + inline React + MP4 motion + iOS frames) doesn't match the Next.js + Tailwind + TypeScript stack. Recreating selectively is the right move.

## What got changed

### `.claude/agents/build/animation-specialist.md` — Step 2

Existing 4 criteria (Niche relevance, Visual impact, Technical feasibility, Uniqueness) expanded to 6 by adding two dimensions from Huashu's critique-guide.md:

- **Visual hierarchy** — Does the animation lead the eye to the H1 + primary CTA, or compete with them? (1 = competes, 5 = supports)
- **Functionality** — Does every visual element serve the brand metaphor, or is decoration parasitic? (1 = pure decoration, 5 = every element earns its place)

Scoring threshold added: winner needs ≥22 of 30 total AND no single dimension below 3. Concepts where Visual hierarchy or Functionality scored below 3 are auto-rejected — those produce heroes that look impressive in screenshots but bleed conversions in production.

### `.claude/agents/launch/pre-launch-auditor.md` — new Section 3B

Two new file-level gates added between Section 3 (Images and Media) and Section 4 (Forms and Conversion Flows):

- **No figurative SVG illustrations** — FAIL if any inline `<svg>` block depicts people, faces, scenes, or photo-like subjects. Reasoning: hand-drawn AI SVG of people is a flagged AI aesthetic. People belong in real photography or fal.ai output (per Image Generation Rule). Decorative SVG is fine for shapes, dividers, icons, brand marks.
- **No AI-signature left-accent-border card pattern** — WARN if more than 2 components use a left-side accent border (≥3px or `border-l-{N}` Tailwind utility) on rounded cards. Use border-on-all-sides + background tone for emphasis instead.

## How to apply going forward

- **animation-specialist** runs the 6-dimension rubric on every new hero concept selection. The expanded rubric is in the agent file — the agent reads it directly, no orchestrator action required.
- **pre-launch-auditor** runs Section 3B alongside Section 3 file checks. New FAIL/WARN items appear in the standard audit output — no new section in the audit report needed beyond the existing format.
- **Build-log retrospective:** if either gate fires on a real build, log a row in the Build Patterns table (or a row in the Error Encyclopedia if the AI-signature pattern reaches a client demo). After 3 builds with zero hits on either gate, evaluate whether they're worth keeping or have served their purpose.

## When NOT to apply

- Not on existing pages already shipped — these are forward checks, not retroactive sweeps. If a shipped Optimus site has an SVG-of-a-person, leave it. Don't refactor without a real reason.
- Not on internal tooling, Optimus Inc's own marketing site (where intentional figurative SVG might be a deliberate brand choice), or anything outside the per-client website pipeline.

## License posture and re-evaluation trigger

Methodology adoption with attribution is not a license violation — license restricts use of the skill's code, prompts, and assets, not the public design knowledge it documents. If Optimus ever wants the full Huashu skill (deck engine, animation engine + BGM/SFX library, device-frame components, the 20-philosophy library), the trigger is starting to ship deliverables Huashu actually produces well: pitch decks, motion-design MP4s, iOS/Android prototype mockups for Tier-4 Autonomous AI Employee client demos. At that point pursue commercial license via alchaincyf's listed contact channels.
