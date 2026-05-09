# Pattern: Asymmetric-cost pre-flight calibration before next build stage

**Category:** Workflow / Quality / Cost-Aware Verification
**First used:** Ead Financial — 2026-05-08

## What

A workflow rule for deciding whether to verify a recently-rebuilt component **NOW** (before downstream work starts) or **LATER** (during the canonical end-of-build audit). The rule: when the cost of catching a regression now is asymmetric to the cost of catching it later (e.g., 15 min Playwright check now vs. 3 hr rework after Stage 1E builds dependent content on top), **always run the cheap check now**. Stage 1I multi-breakpoint browser audit is the wrong place to catch hero-composition issues because by that time the surrounding page content masks the diagnostic signal.

## When to Use

This pattern fires when ALL THREE conditions are met:
1. **A component was recently rebuilt** (correction, refactor, version bump) and confidence in its v2 state is unverified.
2. **Downstream stages will build dependent content on top of the component** before the canonical end-of-build audit runs.
3. **The verification cost is asymmetric** — running the check now is at least 5–10× cheaper than catching the same regression at the canonical audit.

Examples that trigger:
- Hero composition rebuilt mid-Stage-1D after a CLAUDE.md violation correction. Stage 1E will build nav, footer, sections, testimonials, pricing, blog, etc. on top. By Stage 1I the hero is buried in surrounding content; you can't tell if it's reading sparse or correctly subordinate. **Verify now.**
- Tailwind v4 `@theme inline` block written for the first time. Stage 1D agents will start consuming the tokens. If `@theme inline` is malformed, classes silently no-op. **Verify now via `npm run build` before agents land any consumer code.**
- A pricing tier card data shape changed mid-build (e.g., single `price` field → hybrid `setupPrice` + `monthlyPrice`). Stage 1E ROICalculator will compute against the new shape. **Verify now via TypeScript exhaustiveness + a test render.**

## How

Decision procedure for "verify now vs defer to Stage 1I":

1. **Estimate the now-cost.** Typically:
   - Playwright screenshot pass: ~15 min (dev server + 2–4 viewports + visual judgment)
   - `npm run build` typecheck + token compile: ~2 min
   - Targeted unit/component test: ~10 min

2. **Estimate the later-cost if a regression slips through.** Typically:
   - Hero/composition regression caught at Stage 1I: 1–3 hr (Stage 1E built dependent surrounding content; Stage 1I diagnosis is harder; Stage 1E rework on top of the fix is the multiplier)
   - Token-compile regression caught at Stage 1D: 30 min – 2 hr (agents wrote consumer code against broken tokens; must re-run agents OR manually patch consumers)
   - Tier-card data-shape regression caught at Stage 1H: 2–4 hr (ROICalculator + ComparisonTable + downstream copy all wrote against wrong shape)

3. **Compute the cost ratio.** If later-cost / now-cost ≥ 5, **verify now**. If the ratio is below 5, deferring is acceptable.

4. **Diagnostic loses signal once you add context.** Even when the cost ratio is borderline (e.g., 3:1), prefer verifying now if the canonical audit happens against a complete page where the surrounding context masks the diagnostic. Hero-composition is the canonical example: at Stage 1I the hero sits next to nav, marquee, sections, testimonials, pricing — eye can't tell whether the hero feels sparse or correctly subordinate to a now-rich page.

5. **Run the verification in isolation.** For visual checks: take screenshots of the hero alone (no surrounding sections built yet) at the target breakpoints. For build checks: `npm run build` against the current state, before agents land downstream consumers. For data-shape checks: `npx tsc --noEmit` + a smoke render.

6. **Apply fixes inline if found.** Calibration regressions caught at this stage are usually 1–3 line fixes (gradient color stop tweak, `mx-auto` add, etc.). Don't escalate them into a re-spawn of the agent that produced them — orchestrator-inline fix is the right scope.

7. **Document calibration values inline.** Once a calibration value is locked (e.g., `7%` accent mix in cream gradient), comment the rationale next to the value: `/* Calibrated 2026-05-09 after Playwright pass showed 12% lift was invisible. */`. Future maintainers tuning the same value get the cost-history.

## Key Rules

- **The cheap check resolves uncertainty; the deferred check accumulates risk.** Asymmetric bets where the cheap side resolves uncertainty get taken every time. The 12× cost ratio (15 min vs 3 hr) is not unusual for hero/component verification.
- **Stage 1I is the wrong place to catch composition issues** — by then the page has nav + footer + sections + testimonials + pricing on top of the hero. You can't tell if the hero feels sparse or correctly subordinate to a richer page. Diagnostic loses signal once context is added.
- **Verify in isolation, not against the eventual full page.** A hero that reads sparse on its own may still feel correct once surrounded by other sections — but if it's wrong, the wrongness is invisible against the busy backdrop. The point of the check is to catch the wrongness in isolation.
- **The pre-flight is not a substitute for Stage 1I.** Stage 1I still runs, still does the multi-breakpoint full-page audit, still performs OS-level reduce-motion toggle. The pre-flight catches the regression class that Stage 1I has lost the signal to detect.
- **Don't pre-flight every component, only the unverified-link-in-the-chain.** If every other locked artifact has been validated against its contract (design-system.md, content layer, schema, agent outputs), the recently-changed component is the only piece that could regress silently. That's the one to pre-flight.

## Reuse Condition

This pattern applies whenever a component is rebuilt mid-build and downstream stages will start consuming it before the canonical audit. Most common triggers:
- Hero composition correction (CLAUDE.md absolute rule violation, photo-vs-no-photo decision, two-column vs single-column resolution)
- Token / theme system change (Tailwind v4 `@theme inline` first use, palette token rename)
- Data-shape change (pricing tier shape, quiz tier discriminator, NichePage type field)
- Animation system swap (Framer Motion v11 → v12 ease type change, canvas → CSS-only fallback)

## Related

- [[patterns/end-of-build-multi-breakpoint-browser-audit]] (Pattern #33) — the canonical Stage 1I audit this pre-flight complements (does NOT replace)
- [[patterns/claude-md-absolute-rule-cross-check-at-checkpoint]] — the Stage 1B human checkpoint pattern; this pattern is its post-correction follow-up when a Stage 1B rejection produces a Stage 1D rebuild
- [[errors/cream-on-cream-gradient-invisible-at-viewport-scale]] — the calibration error this pattern caught on Ead Financial (would have been ~3 hr Stage 1I rework without the pre-flight)
