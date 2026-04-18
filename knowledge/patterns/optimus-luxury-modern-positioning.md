# Optimus Luxury-Modern Positioning (Pattern #49)

**Established:** 2026-04-17
**Rule owner:** CLAUDE.md §Optimus Positioning Rule
**Applies to:** Every Optimus build, every tier, every industry — no exceptions.

## The positioning

Every Optimus site ships as a **premium, modern, 2026-era build with UI/UX engineered for conversion**.

Trade businesses, luxury hospitality, B2B SaaS, professional services, and personal services all get the same luxury-grade visual floor. The client paid $1,500 Starter or $5,500 Premium — they got different FEATURE SETS, not different DESIGN GRADES. We do not ship budget-looking sites.

## Why this matters

Without this rule codified, design-synthesizer has legitimate license (from frontend-design.md) to pick any aesthetic direction — brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art-deco/geometric, soft/pastel, industrial/utilitarian.

Past Optimus builds converged on luxury-modern only because Anthony steered every design-synthesizer output manually. Under Opus 4.7's more literal instruction-following, that steering gets harder — the agent reads frontend-design.md and thinks "brutalist is an option." This rule removes the option.

## What counts as "luxury-modern-2026-conversion"

**Visual layer (universal across builds):**
- Typography: variable fonts, real type hierarchy, clamp-based scale. No Arial, no Roboto, no default system stack.
- Animation: real motion — 3-layer hero stack, ambient effects on every interior page, Framer Motion scroll-triggered reveals.
- Visual density: generous whitespace, radial-gradient-overlayed dark sections (never flat), subtle-gradient-overlayed light sections.
- Interactions: micro-animation on hover, focus-visible states, skeleton loaders.
- Color: brand-primary + brand-accent + restrained neutrals. No stock-corporate blue, no Bootstrap navy, no purple-gradient-on-white.
- Emoji: YES — as semantic UI icons. Modern premium brands (Linear, Stripe, Vercel, Raycast, Superhuman) use emoji freely. The tension is "emoji vs stock-corporate," not "emoji vs luxury."

**What varies (not scoped by this rule):**
- Copy voice and tone — adapts to the brand's target audience. A fence company's customers sound different from a luxury hotel's customers. See content-writer.md Voice Anchor for the voice layer.
- Feature mix — see Always-Built Features Rule + design-system.md Section 11.
- Specific tokens — color values, fonts, personality axes. design-synthesizer picks these per client.
- Photography direction — design-system.md Section 6.

## Aesthetic directions allowed for Optimus builds

From the frontend-design.md menu, only these are in scope:
- **Luxury / refined** — default for hospitality, professional services, premium trades.
- **Editorial / magazine** — default for content-heavy builds (strong blog strategy, thought leadership).
- **Modern minimal** — restrained, precision-heavy. Default for B2B SaaS, dev tools, fintech.
- **Organic / natural** — premium craft/artisan brands. NOT rustic-folk or farmhouse-budget.
- **Industrial / utilitarian** — only when industry genuinely demands it (construction, heavy machinery, B2B manufacturing). Must still pass the "premium" sniff test.

## Aesthetic directions explicitly banned

These are valid directions in general web design, but they're OFF-POSITIONING for Optimus:
- **Brutalist / raw** — reads unfinished. Optimus is polished, not anti-polish.
- **Retro-futuristic** — wrong category signal. Our clients are present-tense businesses.
- **Playful / toy-like** — undermines conversion gravitas. Visitors need to trust us with money or time.
- **Art-deco geometric maximalism** — niche, dated, hard to scan.
- **Soft pastel** — reads cheap / Canva-template in 2026 aesthetic climate.

A client requesting one of these directions gets steered. The sales pitch is "we produce sites that convert at luxury-tier quality — the direction you're asking for won't hit our performance benchmarks."

## What happens when this rule conflicts with market research

If market-intelligence.md says competitors in this niche all went "playful" or "cheap," that is a DIFFERENTIATION opportunity, not a signal to match. Optimus ships premium in a category that hasn't. Document the gap in design-system.md Section 9 (Competitor Differentiation) and Section 10 (Anti-Patterns — "do not use X because it dominates competitors in this niche").

## How this shows up per-agent

- **design-synthesizer** — Task opening includes the Optimus Positioning Constraint block. Section 1 (Brand Identity) reflects premium-modern positioning. Section 10 (Anti-Patterns) lists the banned aesthetic directions by name.
- **animation-specialist** — already constrained via the 10-concepts + critic gate; concepts must meet "eye-catching and luxurious" criterion.
- **content-writer** — Voice Anchor scope-note clarifies that copy voice varies with brand but the site VISUAL is always luxury-modern.
- **pre-launch-auditor** — Section 1 (dev-only components) already catches most positioning violations; combined with the Visual QA multi-breakpoint audit, layout-grade issues surface.

## Signal that this rule needs enforcement

If a design-system.md output proposes any of the banned directions, that is a design-synthesizer failure. Kick back with correction note: "Optimus Positioning Rule — output must fall within luxury-modern-2026-conversion family. See CLAUDE.md and knowledge/patterns/optimus-luxury-modern-positioning.md."

## Related patterns
- `knowledge/patterns/homepage-dark-light-section-rhythm.md` — visual-rhythm execution detail
- `knowledge/patterns/conversion-first-hero-headline.md` — conversion layer
- `knowledge/patterns/hero-3-layer-stack-and-5-phase-canvas.md` — hero visual contract

## Status
ACTIVE. Applied to every Optimus build from 2026-04-17 onward. Retroactive audits of pre-2026-04-17 builds may surface aesthetic drift — not a retro-fix priority unless flagged during `/retro`.
