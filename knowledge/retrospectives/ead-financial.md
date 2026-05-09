# Ead Financial — Project Retrospective

**Type:** CPA practice (tax preparation, outsourced accounting, taxpayer representation)
**Location:** Methuen, MA HQ + Portland, ME revenue concentration; nationwide remote service area
**Tier sold:** Premium ($5,500)
**Build status at retro:** Phase 1 Stages 1A–1D complete + hero correction loop. Stage 1E (multi-week scope) not yet started.
**Completed:** 2026-05-09 (retrospective written between Stage 1D close and Stage 1E spawn — early-retro pattern, captures the design+content layer learnings before the page-build sweep buries them)
**Build sessions:** ~3 active sessions across 2026-05-08 (intake → Phase 0 → Stage 1B → Stage 1C → Stage 1D → mid-stage hero correction → Stage 1E pre-flight calibration)

---

## What Went Well

- **Intake → market-intelligence → design-system flow produced a build-defensible brand constitution.** initial-business-data.md (10 sections including Brand Identity §8, Conversion & Tech §9, Competitive Context §10) + market-intelligence.md (45KB real research, 3-persona framework, 5 custom-build flags, 7-row competitor matrix) + design-system.md (12 sections after the §12 Psychological Foundations addition) compose into a brief that survives client pushback. The "why cream not navy?" question now has a 4-mechanism research answer (Crowley & Hoyer 1994; Mehta & Zhu 2009 + market-intel §8 + audience threat-response framing).

- **Stage 1A repo scan in parallel — 7 agents, single message, single Concurrency Checkpoint.** Universal finding ("every scanned hero is wrong-energy for editorial register") landed in progress.md and informed both the design-synthesizer and animation-specialist briefs. The cost was ~50K tokens of agent work; the value was eliminating ~3 candidate hero approaches that would have been built and rejected. Pattern #19 (Firecrawl existing site capture) at the orchestrator level.

- **content-writer + animation-specialist in true parallel via single-message dual-Agent call** — schema was pre-locked in Stage 1C scaffold (site.ts + quiz.ts interfaces shipped empty before Stage 1D), so the parallel run had zero contract conflicts. content-writer owned `/src/data/*` exclusively; animation-specialist owned `/src/components/sections/*` + `/src/components/ui/*` + `/src/app/page.tsx`. No file overlap.

- **Section 12 Psychological Foundations addition** (Pattern #61) — user-flagged gap in the original 11-section design-synthesizer output that turned the doc from "competitively-backed" into "psychology-backed." 113 lines of substantive content (audience threat-response, cognitive fluency, 14-row mechanisms map, commitment-escalation, anchoring strategy, loss-aversion framing, pre-launch-auditor checklist, defensibility script). BINDING for Stage 1D content-writer + Stage 1H pre-launch-auditor. Largest-leverage pattern emitted from this build for cross-project reuse.

- **Asymmetric-cost pre-flight calibration** (Pattern #63) — user pushed back on deferring Playwright verification to Stage 1I. Run cost was 15 min, deferred-cost would have been ~3 hr Stage 1I rework. Caught: cream-on-cream gradient invisibility (Error #56), inner column missing `mx-auto` (left-aligned with empty rail), trust microcopy duplicate render. All three fixed inline. Pattern complements (does NOT replace) the canonical Stage 1I audit.

- **NichePage `type` discriminator** (Pattern #62) — pre-Stage-1E scope addition that lets one shared `[slug]` route emit different JSON-LD schema bundles per page type (vertical = FAQPage + Service + Person + LocalBusiness; funnel = HowTo + LocalBusiness). Future niches add zero code while maintaining schema correctness for AEO citation.

- **Atomic git commits with full audit trail.** 6 commits document the build with traceable cause-and-effect: `chore(init):` scaffold → `feat(stage-1d):` parallel-agent output → `fix(hero):` photo removal per CLAUDE.md absolute rule → `chore(stage-1e-prep):` discriminator + extended grep + portrait pin → `fix(hero):` calibration corrections after Playwright verification. Each commit body cites the design-system.md / CLAUDE.md / build-log section that justifies the change.

---

## What Didn't

| # | Gap | Fix Applied |
|---|-----|-------------|
| 1 | design-synthesizer cited Claro Advisors to justify a two-column hero with photo-on-right. Orchestrator approved at Stage 1B human checkpoint without cross-checking against CLAUDE.md Hero Architecture Rule's absolute *"No photos in the hero, ever — a photo placeholder in the hero is a build failure."* User caught at Stage 1D close. Net cost ~3 hr re-spawn. | design-system.md §5 corrected to v2 (single-column text-only + cream ambient gradient + marquee below). §6 Photography retargeted (Hero portrait → About Chapter 1; environmental scenes → mid-page section breaks). Hero.tsx rewritten 246 lines, no photo. Memory file `feedback_no-photos-in-hero-box.md` written. New Pattern #58 codifies the orchestrator absolute-rule cross-check at Stage 1B human checkpoint. |
| 2 | Cream-on-cream gradient using `--bg-elevated` as blob center was perceptually invisible at 1440x900 viewport scale (~7-9 RGB-point delta against `--bg-base`). Hero v2 read as "left-aligned text on flat empty page." | Replaced with brass-tinted cream center via `color-mix(in oklab, var(--accent) 7%, var(--bg-base))`. Larger ellipse (85% 70%) centered at 50% 42%. Inner column also got `mx-auto` for centered single-column composition. New Pattern #60 codifies the recipe. |
| 3 | Trust microcopy rendered duplicate stars and duplicate "· CPA" — site.ts trustMicrocopy hardcoded the prefix and suffix while Hero.tsx ALSO rendered them. Result: "★★★★★ ★★★★★ Trusted by ... · CPA · CPA". Class-of-bug: data layer AND component layer both rendering the same presentational decoration. Will recur on next build's pricing card / stats bar / testimonial attribution / eyebrow label without the prevention rule. | site.ts trustMicrocopy stripped of star prefix and credentials suffix. Hero.tsx remains single source of truth. Inline comment in site.ts documents the contract. New Pattern #64 ([[patterns/single-source-of-truth-for-presentational-decoration]]) codifies the cross-build prevention rule with anti-pattern greps for the Stage 1H pre-launch-auditor. New Error #57 ([[errors/hero-trust-microcopy-double-rendered-decoration]]) documents the Ead instance. |
| 4 | `bash npm run dev > log 2>&1 &` orphaned the Next.js dev server process — the bash background task exited 0 but PID lived on, occupying port 3000 across sessions. Required `Stop-Process -Id <pid> -Force` cleanup before subsequent dev runs. | Pattern documented inline in retro: use `run_in_background: true` directly on the npm command, not bash `&` chaining. Bash `&` orphans on Windows because the parent shell's exit doesn't kill the child Next.js process. |
| 5 | Layout.tsx page title is still default "Create Next App" boilerplate from create-next-app. Visible in browser tab and any SEO crawl during the dev period. | Deferred to Stage 1E layout work. Logged in progress.md "Outstanding for Stage 1E" section. Cheap to fix when Stage 1E nav/layout work runs. |
| 6 | Two new dev-server orphans on port 3000 from prior sessions (different projects: Anjo Services + an unidentified Next.js process at PID 10600) blocked Ead's dev server from binding to port 3000. Ead fell back to port 3001 throughout the verification pass. | Cleaned up via `Stop-Process -Id` per orphan. Workflow note: future builds should check `Get-NetTCPConnection -LocalPort 3000` before starting `npm run dev` to avoid surprise orphan collisions. |

---

## Tools Introduced This Build

- **`color-mix(in oklab, ...)` for editorial gradient stops.** Tailwind v4 + modern CSS color-functions. Used at Hero.tsx ambient backdrop center (7% accent → cream blend) and falloff (4% accent → cream blend). `oklab` produces perceptually uniform mixes for warm-cream blends; `srgb` defaults to muddy mid-stops on cream/brass mixes.
- **Tailwind v4 `@theme inline` token exposition.** Globals.css uses `@theme inline { --color-primary: var(--primary); ... }` block to surface CSS custom properties as Tailwind utility classes (`bg-bg-base`, `text-primary`, `font-display`, etc.). Verified compilation via `npm run build`. Silent failure mode (malformed `@theme inline` → utility classes no-op) caught by build verification, not typecheck.
- **`mcp__playwright__*` tool family for orchestrator-driven calibration verification.** Pattern #33 (end-of-build multi-breakpoint browser audit) is canonical for Stage 1I; Pattern #63 (asymmetric-cost pre-flight calibration) extends the same toolset to mid-build correction loops.
- **Next.js 16 + React 19** (versions 16.2.6 + 19.2.4). Significant deltas from Next 13/14 patterns documented in progress.md: `params` and `searchParams` are now `Promise<{...}>`, `generateMetadata` signature is async-Promise, `unstable_instant` is opt-in route export, `'use cache'` directive, Cache Components flag. Stage 1E agents must read web/AGENTS.md + node_modules/next/dist/docs/01-app/ before writing any route.

---

## Changes Made to Toolkit

- **None mechanical to CLAUDE.md or website-build-template.md** — Ead Financial did not produce a CLAUDE.md edit. The new patterns/errors live in `knowledge/` per the Knowledge Base Rule's "what belongs where" filter ("If a rule does not apply universally, it does not belong [in CLAUDE.md]").

- **Workflow gaps surfaced for orchestrator + design-synthesizer integration** — Section 12 Psychological Foundations should become a required output section in design-synthesizer.md (currently it requires 11; should be 12). Absolute-rule cross-check should become a required Stage 1B human checkpoint step (currently implicit in CLAUDE.md but not in the project-prime.md / design-synthesizer.md handoff). See Phase 6 Workflow Gaps Detected for the candidate edits.

- **`feedback_no-photos-in-hero-box.md` saved to project-scoped memory** — `~/.claude/projects/c--Projects-John-Ead/memory/`. Project-specific memory captures the Ead-particular framing of the absolute-rule lesson; the cross-project version is in [[patterns/claude-md-absolute-rule-cross-check-at-checkpoint]] (Pattern #58).

---

## Cross-Build Reuse Highlights

If the next financial-services / editorial-register build hits all four conditions in [[patterns/light-mode-dominant-cream-theme]] (navy-saturated competitor scan + threat-response audience + editorial register fit + visible-in-5-seconds differentiation thesis), this build's design-system.md becomes a strong starting reference for:
- Section 2 token map (cream-dominant 9-token core + 5-token inverse + 4 functional)
- Section 3 typography (Orpheus serif italic-emphasis + Inter body)
- Section 5 hero composition (single-column text + cream-tinted ambient backdrop + marquee below — NOT photo)
- Section 6 photography direction (editorial real-scene, NOT stock, NOT page-hero)
- Section 8 brand personality axes (~20% quiet, ~10% editorial, ~25% direct)
- Section 12 Psychological Foundations (8-subsection structure ports verbatim)

If the next build has multi-niche-page architecture with mixed schema needs, Pattern #62 (NichePage `type` discriminator) is the starting reference.

If the next build hits a CLAUDE.md absolute-rule violation at design-synthesizer Stage 1B, Pattern #58 (absolute-rule cross-check at human checkpoint) is the prevention reference.
