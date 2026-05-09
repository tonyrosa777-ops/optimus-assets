# Luxury Gradient Backgrounds (Pattern #51)

**Rule owner:** CLAUDE.md §Homepage Section Architecture Rule → Background depth & motion
**Applies to:** Every Optimus build, every section, every page.
**Established:** 2026-04-17

## The rule in one sentence
Every section background is a gradient with subtle motion by default; stillness is a content-density exception; never flat solid, ever.

## Why this matters

The Optimus Positioning Rule (Pattern #49) commits every site to luxury-modern-2026-conversion. Luxury-modern 2026 brands don't ship flat-color sections. Reference executions to study:

- **Stripe** — mesh gradients in the hero + aurora-style sweeps behind payment flow screenshots. `background-size: 200% 200%` + `@keyframes` on `background-position` = mesh drift.
- **Vercel** — aurora gradient behind every marketing section, subtle animated conic-gradient layer.
- **Linear** — ambient radial orbs breathing at ~12s cycle, single layer per section.
- **Raycast / Superhuman** — grain-textured gradients that shimmer subtly.

All of these use CSS-only motion. None use JavaScript-driven section backgrounds. None use flat fills as a default.

A flat `background: #0a0a0a;` or `background: #ffffff;` section on an Optimus build reads as unfinished. The visitor doesn't articulate why — they just feel the site is less polished than the Stripes and Linears they're used to. That feeling kills conversion at the trust layer, before any copy lands.

## Motion vocabulary — pick ONE per section

Stacking more than one of these in a single section creates visual noise and burns GPU. Pick the one that fits the section's role and stick with it.

### 1. Breathing orb (most versatile, default choice)

One or two radial blobs positioned at section corners. Scale + opacity oscillate on a ~12s cycle. Works on dark and light backgrounds. Lowest GPU cost.

```css
.section-breathing {
  position: relative;
  background: var(--primary);
  overflow: hidden;
}

.section-breathing::before {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  background:
    radial-gradient(ellipse 60% 50% at 20% 30%, rgba(212, 160, 23, 0.08), transparent 70%),
    radial-gradient(ellipse 50% 60% at 80% 70%, rgba(212, 160, 23, 0.06), transparent 70%);
  animation: breathe 12s ease-in-out infinite;
}

@keyframes breathe {
  0%, 100% { transform: scale(1); opacity: 0.8; }
  50%      { transform: scale(1.05); opacity: 1; }
}

@media (prefers-reduced-motion: reduce) {
  .section-breathing::before { animation: none; }
}
```

When to use: pain points, about, services lists, stats, testimonials, footer-adjacent. Default choice when unsure.

### 2. Mesh drift (premium / hero-adjacent sections)

Multi-color mesh gradient with `background-position` animating slowly across a 2x canvas. Higher visual impact than orbs. Used by Stripe, Vercel.

```css
.section-mesh {
  position: relative;
  background: var(--bg-base);
  overflow: hidden;
}

.section-mesh::before {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  background:
    radial-gradient(at 20% 30%, rgba(212, 160, 23, 0.10) 0%, transparent 50%),
    radial-gradient(at 80% 20%, rgba(190, 100, 60, 0.08) 0%, transparent 50%),
    radial-gradient(at 60% 80%, rgba(100, 140, 180, 0.06) 0%, transparent 50%);
  background-size: 200% 200%;
  animation: mesh-drift 25s ease-in-out infinite;
}

@keyframes mesh-drift {
  0%, 100% { background-position: 0% 0%; }
  50%      { background-position: 100% 100%; }
}

@media (prefers-reduced-motion: reduce) {
  .section-mesh::before { animation: none; background-position: 50% 50%; }
}
```

When to use: hero-adjacent CTA sections, premium feature reveals, pricing page tier cards background (not the card itself). ONE per page max.

### 3. Aurora sweep (dramatic, sparingly)

Diagonal conic gradient sweeping across the section. High visual impact. Reserve for "moment" sections.

```css
.section-aurora {
  position: relative;
  background: var(--primary);
  overflow: hidden;
}

.section-aurora::before {
  content: "";
  position: absolute;
  inset: -20%;
  pointer-events: none;
  background: conic-gradient(
    from 180deg at 50% 50%,
    transparent 0%,
    rgba(212, 160, 23, 0.08) 15%,
    transparent 30%,
    transparent 100%
  );
  animation: aurora-sweep 20s linear infinite;
}

@keyframes aurora-sweep {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}

@media (prefers-reduced-motion: reduce) {
  .section-aurora::before { animation: none; transform: rotate(15deg); }
}
```

When to use: final booking CTA section, hero backup when 3-layer stack isn't used (rare), testimonial featured-quote section. Max ONE per page.

### 4. Grain shimmer (subtlest, text-heavy-adjacent)

Static gradient + animated fine-grain noise overlay. Adds texture without distracting from content. SVG noise is cheap.

```css
.section-grain {
  position: relative;
  background:
    radial-gradient(ellipse at 50% 0%, rgba(212, 160, 23, 0.06), transparent 70%),
    var(--bg-base);
  overflow: hidden;
}

.section-grain::after {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  opacity: 0.4;
  mix-blend-mode: overlay;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='0.9' numOctaves='2'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.5'/%3E%3C/svg%3E");
  animation: grain-shimmer 8s steps(4) infinite;
}

@keyframes grain-shimmer {
  0%, 100% { transform: translate(0, 0); }
  25%      { transform: translate(-2%, 1%); }
  50%      { transform: translate(1%, -2%); }
  75%      { transform: translate(-1%, -1%); }
}

@media (prefers-reduced-motion: reduce) {
  .section-grain::after { animation: none; }
}
```

When to use: editorial sections, blog featured-post hero, about-section photo backdrop, any section where the content is the star and the background is atmosphere.

## Static-gradient exceptions — never flat, just motion-off

Turn motion off (but keep the gradient) when:

1. **Long-form text.** Blog article bodies, legal/privacy/terms pages, FAQ expanded answers — any section where the user is reading for 30+ seconds.
2. **Pricing comparison tables.** Focus belongs on the rows.
3. **Form-dense sections.** Signup, contact, booking details — cognitive load is elsewhere.

Implementation: use the same gradient from the Motion vocabulary, just omit the `animation` property (or set `animation: none`).

```css
.section-text-heavy {
  background:
    radial-gradient(ellipse 60% 50% at 20% 30%, rgba(212, 160, 23, 0.06), transparent 70%),
    var(--bg-base);
  /* no animation — static gradient only */
}
```

Still a gradient. Never flat.

## Performance budget

Non-negotiable thresholds:

- **Max 3 active motion layers visible simultaneously in any viewport.** Hero counts as 1 (canvas particles + ambient orb). Each interior section with a motion layer counts 1. If the user scrolls to a position where 4 motion layers are in-view at once, reduce.
- **CSS-only for section backgrounds.** Never JavaScript-driven animation for section backgrounds. Canvas is reserved for hero (3-layer stack) + intentional interior-page ambient effects.
- **GPU-cheap properties only:** `transform`, `opacity`, `background-position`. Avoid `filter`, `backdrop-filter`, `blur` on animated layers — they force repaints.
- **FPS test:** open the page at 390px in Playwright, scroll at natural speed, measure FPS via Performance API or browser devtools. Must stay ≥50 FPS on a mid-range device simulation.

## Accessibility

Non-negotiable:

- **`prefers-reduced-motion: reduce` must degrade to the STATIC form of the gradient, never to a flat color.** The site still looks premium; it just stops moving. Add the media query to every motion keyframe (see recipes above).
- **Motion frequency cap:** 0.3Hz peak. One visible cycle per 3+ seconds minimum. Faster than that reads as a loading spinner or an error — both brand-damaging for luxury positioning.
- **No motion on elements with `pointer-events: auto` that conflict with reading:** background motion behind a paragraph must be 8s+ cycle and ≤0.12 alpha at peak.

## Common mistakes to avoid

1. **Stacking two motion layers on one section.** Breathing orb + aurora sweep on the same section = visual noise. Pick ONE.
2. **Motion cycles under 4 seconds.** Reads as "loading" or "something's wrong." 8s minimum, 12-30s sweet spot.
3. **`filter: blur(40px)` on the animated layer.** Forces repaint every frame = GPU meltdown on mobile. Use pre-blurred gradient stops instead.
4. **JavaScript-driven section backgrounds.** Requesting animation frame for a background animation wastes the event loop. CSS does this for free on the compositor thread.
5. **Forgetting `prefers-reduced-motion`.** Ship without the media query = WCAG 2.3.3 fail. Every keyframe animation needs the degrade path.
6. **Flat fallback for reduced-motion.** Reducing motion doesn't mean removing the gradient. Keep the gradient, stop the motion.
7. **Using solid-color cards over a gradient section.** Cards should be translucent (`rgba(255,255,255,0.04)` on dark, `rgba(0,0,0,0.02)` on light) so the section's gradient shows through — that's what sells the depth.

## Per-page motion budget examples

**Homepage (max 3 motion layers at once):**
- Hero: 1 layer (particles + breathing orb bundle counts as 1 layer at this granularity)
- Services section: breathing orb (1)
- Stats section: static gradient (0)
- Testimonials: mesh drift (1)
- Quiz CTA: breathing orb (1) — but if user scrolls from testimonials to quiz CTA, briefly 2 are visible — OK, still under 3
- Blog preview: static gradient (0)
- Shop teaser: breathing orb (1)
- Final booking CTA: aurora sweep (1) — this is the "moment" section
- Footer: static gradient (0)

**Interior page (blog article):**
- Header: breathing orb (1)
- Article body: static gradient (0)
- Related posts: breathing orb (1)
- Footer: static gradient (0)

**Interior page (pricing):**
- Header: breathing orb (1)
- Tier cards: static gradient (0)
- ROI calculator: breathing orb (1)
- Comparison chart: static gradient (0)
- Booking CTA: aurora sweep (1)

## Related patterns
- [[patterns/optimus-luxury-modern-positioning]] (#49) — positioning rule this pattern serves
- [[patterns/homepage-dark-light-section-rhythm]] — tone alternation (still applies)
- [[patterns/page-header-ambient-radial-gradient]] — existing interior-page pattern, subset of this rule
- [[patterns/hero-3-layer-stack-and-5-phase-canvas]] — hero visual contract (the hero has its own motion system; this rule applies to everything NOT the hero)

## Cream-dominant addendum (added 2026-05-08, Ead Financial)

The four motion-vocabulary recipes above were calibrated on dark-dominant builds where the gradient lift is provided by a brand-color blob over a near-black ground. **Cream-dominant builds (light-mode-dominant theme — Pattern #59) require a different calibration recipe** because cream-on-cream gradient lift is perceptually under-threshold at the same percentage values that work on dark.

### When this addendum applies

Builds matching **all four** Pattern #59 conditions:
1. Competitor scan documents navy + white + gray saturation in market-intelligence.md
2. Audience makes high-anxiety decisions (threat response per Schmader & Beilock 2012)
3. Editorial / boutique register fits the audience
4. Differentiation thesis depends on visual escape from competitor zone

For these builds, the gradient is brass-tinted cream over base cream — both warm pales of similar lightness. The contrast budget is fundamentally smaller than dark-mode builds.

### Calibration recipe for cream-dominant breathing orb

The default cream-dominant breathing orb under hero / page-header / mid-page CTA sections:

```css
.cream-breathing-orb {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background:
    radial-gradient(
      ellipse 60% 50% at 50% 52%,
      color-mix(in oklab, var(--accent) 14%, var(--bg-base)) 0%,
      color-mix(in oklab, var(--accent) 8%, var(--bg-base)) 35%,
      var(--bg-base) 78%
    );
  will-change: transform, opacity;
  animation: cream-breathing-orb-drift 20s ease-in-out infinite;
}
@keyframes cream-breathing-orb-drift {
  0%, 100% { transform: translate3d(0, 0, 0) scale(1); opacity: 0.85; }
  50%      { transform: translate3d(2.5%, -1.5%, 0) scale(1.04); opacity: 1; }
}
@media (prefers-reduced-motion: reduce) {
  .cream-breathing-orb { animation: none !important; transform: none !important; opacity: 1 !important; }
}
```

### What changed from the dark-mode recipe

| Parameter | Dark-mode breathing orb | Cream-dominant breathing orb |
|---|---|---|
| Center accent percentage | 6-8% | **14%** |
| Mid-stop accent percentage | 3-4% | **8%** |
| Ellipse size | 85% × 70% | **60% × 50%** |
| Center position | 50% 42% | **50% 52%** (under H1 optical center) |

The non-obvious finding: **percentage and geometry interact non-linearly.** A higher accent percentage in a tighter ellipse reads warmer AND less aggressive than a lower accent percentage in a larger ellipse. The larger blob washes out and reads as "flat / empty"; the tighter blob has a focal point and reads as "warm pool / deliberate."

### Empirical history (Ead Financial pre-flight item 9)

Three calibration attempts, two falsified:

1. `--bg-elevated` (~7-9 RGB delta from `--bg-base`) at 12% lift in `~85% × 70%` ellipse → **invisible at 1440 viewport scale.** Lightness delta ~0% perceptually. Falsified by Playwright pass.
2. `accent 7% / 4%` in `85% × 70%` ellipse at `50% 42%` → **still invisible** (oklab L delta center→edge ~1%). Theory said 6-8% was the sweet spot to preserve quiet-pole positioning per Pattern #59 Axis 1; production verification falsified this. Geometry was the missing variable.
3. `accent 14% / 8%` in `60% × 50%` ellipse at `50% 52%` → **at-spec lift.** Lightness delta ~2.5%, b-axis warmth boost makes the warm zone perceptible without reading "yellow stain." This is the working recipe.

See Error #56 + commit 66bc398 for the full pre-flight evidence trail.

### What still applies from the dark-mode recipes above

- **Performance budget:** unchanged. Max 3 active motion layers visible simultaneously, CSS-only, GPU-cheap properties.
- **Accessibility:** unchanged. `prefers-reduced-motion: reduce` degrades to STATIC gradient, never flat.
- **Section purpose dedup:** unchanged. No two adjacent sections share purpose.
- **Mesh drift / aurora sweep / grain shimmer recipes:** the same dark-mode percentages and geometry MAY work on cream-dominant builds, BUT have not been validated. When in doubt, run the cream-dominant breathing orb on cream-dominant builds first; introduce other motion vocabularies only after Playwright-verifying their cream variant.

### Falsifies prior internal guidance

The earlier "6-8% accent mix is the editorial-register sweet spot — below 5% invisible, above 12% reads as yellow stain" guidance (originally documented in Error #56 first-pass) was anchored on theory (Pattern #59 Axis 1 quiet-pole positioning) without empirical verification. The 12% upper bound was correct; the 6-8% sweet-spot floor was wrong at large ellipse sizes. The corrected guidance: **lift % and ellipse size are joint parameters, not independent.** If you tighten the ellipse to ~60%×50%, you can push the lift % up to 14% and still read "warm pool" not "yellow stain." If you keep the ellipse at ~85%×70%, you cannot push the lift % above ~7% before reading "yellow stain" — but at that range the gradient is invisible.

## Status
ACTIVE. Applied to every Optimus build from 2026-04-17 onward. Cream-dominant addendum applied from 2026-05-08 onward. Retroactive application to pre-2026-04-17 live builds is not a priority; apply during the next revision pass on each.
