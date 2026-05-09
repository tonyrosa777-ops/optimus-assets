# Pattern #67 — Dark-section ink-on-ink gradient recipe

**First shipped:** Ead Financial, Stage 1E Step 4 (`/cpa-for-treatment-centers-maine`, `/cpa-for-contractors-new-england`, `/switching-cpas`), 2026-05-09 commit `a91df6a`.
**Status:** VALIDATED. The exact ink-on-ink counterpart to Pattern #51's cream-dominant addendum. Reuse on every dark page section across cream-dominant Optimus builds.
**Category:** Visual Design / Animation / Motion

---

## Why this pattern exists

Pattern #51 (luxury gradient backgrounds — cream-dominant addendum) documents the canonical recipe for *light* sections on cream-dominant builds. Until Step 4 of the Ead Financial build, no sibling recipe existed for *dark* sections — agents either improvised hex values (Error #29 risk: undefined custom properties resolve to empty string) or copied the homepage `Services.tsx` recipe ad-hoc without a documented contract.

Two failure modes this pattern prevents:

1. **Agent improvises a dark gradient** — picks accent percentages, ellipse geometry, or motion duration that don't match the light-section sibling. Result: dark sections feel disconnected from the rest of the page rhythm. Each Optimus build re-derives the recipe.
2. **Agent uses hardcoded hex values** for the dark surface — bypasses the design-token layer, breaks the cream-vs-dark rebrand path, and may not survive a `--bg-dark` token rename.

This pattern documents the exact recipe so dark sections shipped in any later build (or any later step within Ead Financial) match the light-section cadence and survive token renames.

---

## The canonical recipe

Apply to any section that needs to break the all-light page cascade with one strategic gravity beat — e.g., the highest-stakes paragraph in a niche landing, the conversion-pressure section in a quiz result, the urgency band in a launch announcement.

### CSS

```css
/* outer section element */
.dark-section {
  background: var(--bg-dark);
  position: relative; /* required for the absolute overlay */
  overflow: hidden;   /* contain the orb drift */
}

/* inner positioned-absolute child overlay (CSS-only, prefers-reduced-motion safe) */
.dark-section::before {
  content: "";
  position: absolute;
  inset: 0;
  background-image: radial-gradient(
    ellipse 60% 50% at 50% 52%,
    color-mix(in oklab, var(--accent-on-dark) 14%, var(--bg-dark)) 0%,
    color-mix(in oklab, var(--accent-on-dark) 8%, var(--bg-dark)) 35%,
    var(--bg-dark) 78%
  );
  /* breathing-orb drift via CSS @keyframes on transform + opacity, 22s cycle */
  animation: dark-section-drift 22s ease-in-out infinite;
  pointer-events: none;
}

@keyframes dark-section-drift {
  0%, 100% {
    transform: translate3d(-2%, -1%, 0);
    opacity: 0.92;
  }
  50% {
    transform: translate3d(2%, 1%, 0);
    opacity: 1;
  }
}

/* Accessibility — gradient stays, motion stops (NEVER flat per CLAUDE.md anti-pattern #14) */
@media (prefers-reduced-motion: reduce) {
  .dark-section::before {
    animation: none;
  }
}

/* Text colors inside the dark section */
.dark-section { color: var(--text-on-dark); }
.dark-section .eyebrow,
.dark-section .secondary { color: var(--text-on-dark-secondary); }
```

### Required design tokens (must exist in globals.css)

- `--bg-dark` — base ink-navy fill (e.g., `#0F1B2D` for Ead Financial)
- `--accent-on-dark` — brand accent calibrated for dark surfaces (may be lighter than the light-mode `--accent` to maintain perceptual brightness)
- `--text-on-dark` — primary body color on dark surface (typically near-cream like `#F5EFE6` or `#FAFAF8`)
- `--text-on-dark-secondary` — eyebrow / caption color on dark surface (typically the brand accent or a muted near-cream)

**Critical:** the recipe uses `var(--accent-on-dark)` for the gradient color — NOT `var(--accent)`. The accent token may be calibrated differently for dark surfaces (often lighter to maintain perceptual brightness against the dark base). Substituting `--accent` produces a dimmer, less-visible gradient.

If any of these four tokens is undefined in the consuming codebase, **STOP — do not improvise hex fallbacks.** Undefined custom properties resolve to the empty string, which silently breaks the gradient. Add the tokens to `globals.css` first, then apply this recipe.

### Token name conventions worth knowing

The Ead Financial codebase declares the token names as:
- `--text-on-dark` / `--text-on-dark-secondary`

NOT:
- `--text-primary-on-dark` / `--text-secondary-on-dark` (a common assumption in agent briefs that doesn't match this codebase)

When authoring agent briefs that cite this pattern, **always grep `globals.css` for the actual token names before naming them in the brief.** The Ead Financial Step 4 spawn brief assumed the longer naming and the agent had to self-correct against the actual declarations. The agent caught it; future briefs should match the actual codebase.

---

## Geometry rationale

The `ellipse 60% 50% at 50% 52%` is the ink-on-ink counterpart of Pattern #51's cream-dominant `ellipse 60% 50% at 50% 52%` — same ellipse dimensions, same center point. Visual rhythm transfers directly between light and dark sections so the page reads as a coherent gradient cadence regardless of which sections are which tone.

The `14% / 8% / 78%` color-mix percentages match Pattern #51's cream-dominant addendum stops. The accent appears at 14% intensity at the ellipse center, fades to 8% at 35% radius, and reaches 0% (pure `--bg-dark`) by 78% radius. This produces a soft brass glow that's perceptually visible without overwhelming the body text legibility.

The 22-second `@keyframes` cycle matches the light-section breathing-orb tempo (Pattern #51 cream-dominant addendum). Mixing tempos across sections breaks the page rhythm — every motion budget on a single page should share the same cycle length unless there's an intentional contrast (e.g., a hero with a 12s aurora sweep above body sections with 22s breathing orbs).

---

## When to use vs. when not to use

**Use this pattern when:**
- A page needs ONE strategic gravity beat to break an all-light cascade
- The narrative weight of the section matches the visual weight (e.g., audit response, deadline, deal-breaking moment)
- The page is otherwise editorial-register / cream-dominant

**Do NOT use this pattern when:**
- The page is dark-dominant overall (use the homepage `Services.tsx` 4%/8% recipe — much subtler gradient on a dark page)
- The section is long-form text (use the static-gradient exception per Pattern #51 — gradient on, motion off)
- The section is form-dense (signup, contact, checkout) — use static gradient

**Cap on usage per page:** at most ONE dark section per page when the page is otherwise light-dominant. More than one creates visual oscillation that competes with the page's hero animation budget. Pattern #51's "max 3 active motion layers visible simultaneously" rule applies — a hero animation + a light section breathing orb + this dark section breathing orb = 3 layers. Do not stack more.

---

## Pattern #51 sibling relationship

This pattern is the **dark-surface counterpart** to Pattern #51's cream-dominant addendum (the `--bg-base` + `--accent` 14%/8% gradient used by `PainPoints.tsx`, `AboutChapters.tsx`, etc.). They share:
- Identical ellipse geometry (`60% 50% at 50% 52%`)
- Identical color-mix percentages (`14% / 8% / 78%`)
- Identical motion vocabulary (breathing orb)
- Identical 22s cycle
- Identical `prefers-reduced-motion: reduce` graceful degradation

They differ ONLY in:
- Base color: `var(--bg-dark)` vs `var(--bg-base)` (cream)
- Accent color: `var(--accent-on-dark)` vs `var(--accent)`
- Text colors: `var(--text-on-dark)` vs `var(--text-primary)`

This sibling relationship makes the recipes interchangeable at the data layer — a `tone: "light" | "dark"` flag on the section data can drive which recipe applies, with Agent A reading the flag and rendering the matching recipe (no creative judgment required). See Ead Financial's `NicheLandingSection.tone` field and `web/src/components/niche/NicheSection.tsx` for the worked implementation.

---

## When to update this pattern

If a future build:
- Calibrates the percentage stops differently (e.g., 16% / 10% / 80%) and the rebrand demonstrates that the new values transfer better → update the canonical percentages here AND in Pattern #51 (they should stay in lockstep).
- Discovers that the 22s cycle clashes with another motion layer → document the alternate cycle as an exception, not a replacement.
- Needs a vertical or off-center variant → add a "Variants" section below; do not replace the canonical recipe.

---

## Failure modes if not followed

- **Hardcoded hex** instead of `var(--bg-dark)` / `var(--accent-on-dark)`: breaks rebrands, breaks dark-mode toggling, breaks token renames.
- **`var(--accent)` instead of `var(--accent-on-dark)`**: dimmer gradient, less-visible accent, may compete with body text contrast.
- **Different ellipse geometry than light-section sibling**: visual rhythm fragmented across the page.
- **No `prefers-reduced-motion` fallback**: accessibility violation.
- **Motion turned off but gradient also dropped (flat dark fill)**: violates CLAUDE.md anti-pattern #14 ("never flat" — gradient stays, motion stops).
- **Two or more dark sections per page on a light-dominant page**: visual oscillation, competes with hero animation budget.

---

## Worked example (production reference)

Ead Financial's `web/src/components/niche/NicheSection.tsx` (commit `a91df6a`) is the canonical implementation. Read this file first when applying the pattern to a new build. The `tone: "light" | "dark"` data flag drives which recipe variant renders; both variants live in the same component for cohesion.

---

## Compatibility notes

- **Compatible with Pattern #51** (luxury gradient backgrounds — cream-dominant addendum) — same parent pattern family. Use Pattern #51 for light sections, this pattern for dark sections, both within a single page.
- **Compatible with Pattern #62** (NichePage type discriminator) — the dark-section flag travels in the data layer alongside the type discriminator without coupling.
- **Compatible with Pattern #66** (Next 16 dynamic-route Promise params) — the dark recipe lives in a section component, not the route, so the route shape is unaffected.
- **Performance budget:** counts as 1 motion layer in Pattern #51's "max 3 active motion layers visible simultaneously" rule. CSS-only — no JavaScript.
- **GPU profile:** uses `transform` + `opacity` for animation (GPU-cheap). No `filter`, no `blur`, no `backdrop-filter` on the animated layer.
