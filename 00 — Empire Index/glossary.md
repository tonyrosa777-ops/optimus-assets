# Glossary

Optimus-specific terms. If a future-Anthony or a future-agent encounters one of these and isn't sure what it means, this is the resolution table. Add to it whenever a new term enters the working vocabulary.

## Pricing tiers (Website Development)

- **Starter** — $1,500. Core pages + canvas+SVG animated hero + FAQ page. The floor. No badge.
- **Pro** — $3,000. Most Popular. Starter plus blog architecture, quiz lead capture, booking calendar, gallery page, testimonials page. This is the sell. The Pro tier gets the badge on the pricing page; Starter and Premium do not.
- **Premium** — $5,500. Pro plus shop. Premium never gets a badge — its job is to anchor Pro as the reasonable choice. Anthony rarely sells Premium directly; it sells Pro.

Pricing rules per [[CLAUDE]]: no deposit / upfront / split-payment language on the pricing page (Anthony offers splits verbally as a backup close, never on the page). No Google services on any tier ever — Optimus does not sell anything Google-branded.

## Offerings

- **Website Development** — the flagship productized offering. Three tiers above. Built with the Optimus website-build pipeline (Next.js App Router + Tailwind CSS 4 + Framer Motion).
- **AI Chat Assistant** — embeds in Optimus-built websites. Brand-themed widget, qualifies leads, routes to booking. In development.
- **AI Voice Receptionist** — answers inbound calls, manages CRM contacts, books appointments directly into the client's calendar. In development. Optimus's own deployed instance answers Optimus phone calls.
- **AI Marketing Team / Content Engine** — n8n-driven autonomous marketing pipeline. Runs Sundays 6pm EST. Powers social content, scored by 4 pillars. In development.

## Hubs

- **Empire Index** — `00 — Empire Index/`. The navigation hub. Holds [[README]], [[MOC — Empire]], [[MOC — Offerings]], [[MOC — Learning]], [[tag-schema]], this glossary.
- **Offerings** — `Offerings/`. The 4 product hubs. What Optimus sells.
- **Optimus Inc** — `Optimus Inc/`. Optimus the company — its own website, deployed agents, market intel, social pipeline, brand kit.
- **Optimus Academy** — `Optimus Academy/`. The personal learning system. Daily entries, courses, atomic concept notes, apply-to-Optimus bridges.

## Workflow & process

- **`/learn`** — the slash command that captures a learning session into Optimus Academy. Leaves three traces: a daily entry, an atomic concept note, and (when applicable) an apply-to-Optimus bridge. The slash command is the enforcement mechanism for the three-trace discipline. Codified in `learn-prompt.md` at vault root.
- **`/intake`** — runs `intake-prompt.md`. Client intake for a new website project.
- **`/market-research`** — runs `market-research-prompt.md`. Builds the per-project `market-intelligence.md`.
- **`/new-client`** — runs `end-to-end-workflow.md`. The full pipeline kickoff for a new website engagement.
- **`/retro`** — runs `retro.md`. Post-launch retrospective. Extracts durable findings into `knowledge/retrospectives/<client-slug>.md` and updates the build-log encyclopedia.

## Concepts & architecture

- **3-layer hero stack** — the mandated hero architecture for every Optimus website. Layer 1: HeroParticles canvas. Layer 2: BrandCanvas (custom brand-named `<canvas>` running the 5-phase lifecycle STREAM → RISE → COOL → ARC → IDLE). Layer 3: Framer Motion stagger text. Defined in [[CLAUDE]] under Hero Architecture Rule. No photos in the hero, ever — the client photo belongs in About.
- **Always-Built Features** — the feature set every Optimus website ships with regardless of tier-purchased status: Pricing Page (sales tool, deleted before launch), Interactive Quiz, Inline Booking Calendar, Testimonials Page (36 testimonials, paginated 9 per page), Blog (9-10 articles minimum), Shop (always scaffolded, decision gate after). Defined in [[CLAUDE]].
- **Self Learning Content Engine** — the n8n workflow that powers the AI Marketing Team offering. Runs Sundays 6pm EST. Stack: Supabase + GPT-4o. Scores generated content by 4 pillars: Health / Wealth / Wisdom / Integration. Workflow JSON lives at `Offerings/02 AI Agents/03 Marketing Team/workflows/self-learning-content-engine.json`.
- **Drink your own champagne** — the Optimus Inc operating principle. Optimus uses its own products: the Optimus website is built from the same website-build template that ships to clients; the Voice Receptionist deployed for Optimus is the same product Optimus sells; Optimus's marketing runs on the same Content Engine offered to clients. If a product isn't good enough for Optimus to use, it isn't good enough to sell.
- **Luxury-modern-2026-conversion positioning** — every Optimus site ships as a premium, modern, 2026-era build with UI/UX engineered for conversion. Non-negotiable across every tier and industry. The tier scopes feature mix, never visual floor. Full pattern in `knowledge/patterns/optimus-luxury-modern-positioning.md`.

## Vault & note-taking conventions

- **MOC** — Map of Content. An index note that wikilinks to its domain. [[MOC — Empire]] is the top-level MOC; [[MOC — Offerings]] and [[MOC — Learning]] are sub-domain MOCs. Pattern from the Obsidian community — adopted to keep navigation explicit rather than relying on folder browsing.
- **Zettelkasten** — the atomic-concept-note style used in `Optimus Academy/concepts/`. One concept per file. Heavily wikilinked. Each note is small enough to revisit and dense enough to teach back from. The opposite of long-form notes that try to capture an entire course in one file.
- **Three traces** — the discipline that every learning capture leaves a daily entry, an atomic concept note, and (when applicable) an apply-to-Optimus bridge. See [[MOC — Learning]] for the full workflow.
- **Apply-to-Optimus bridge** — a note in `Optimus Academy/apply-to-optimus/` that explicitly maps a learned concept to an offering improvement. Tagged with `#applies-to/<offering>` so it surfaces in the right offering hub. Without the bridge, learning never earns its keep on the product side.

## Tag families

Full schema in [[tag-schema]]. Quick reference:

- `#offering/...` — which product the note belongs to
- `#layer/...` — universality scope (optimus-os / offering / client)
- `#learning/...` — where in the learning pipeline (captured / synthesized / applied)
- `#applies-to/...` — used in Academy notes to surface in offering hubs
- `#stage/...` — project lifecycle stage
- `#status/...` — note maturity
