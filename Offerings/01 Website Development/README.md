# Website Development

The productized core of Optimus Business Solutions. Every Optimus website ships from the same Next.js template, the same design constitution, and the same always-built feature set. Clients buy a tier; they do not buy bespoke architecture. Customization happens at the brand and copy layer, never at the platform layer.

This is the established business. Around 11 client builds shipped through April 2026. Every existing file at the vault root and every file in `knowledge/` was authored against this offering.

## Pricing

See [[pricing]]. Three tiers: Starter $1,500 / Pro $3,000 (Most Popular) / Premium $5,500. Same on every build, never customized per client.

## Workflow templates (vault root)

These are the files an Optimus website build orchestrates against. Read them in the order listed in `[[CLAUDE]]` Mandatory Pre-Read Protocol.

- [[CLAUDE]] — project rules and the operating constitution for every build
- [[project-prime]] — the orchestrator entry command (variable injection, stage routing)
- [[website-build-template]] — the tech foundation (stack, directory structure, animation patterns, API routes)
- [[build-checklist]] — the human-facing phase schedule
- [[end-to-end-workflow]] — the new-client flow from intake through launch
- [[intake-prompt]] — first-touch business data capture
- [[market-research-prompt]] — competitive + audience research synthesis
- [[frontend-design]] — UI/UX rules (layout, component architecture, visual decisions)
- [[retro]] — post-launch retrospective command
- [[animation-inspiration]] — hero canvas concept reference
- [[animated-logo-inspiration]] — fallback logo-particle pattern reference

## Cross-project knowledge

The central index lives at [[knowledge/build-log]]. Read it before starting any phase. If a similar problem was solved before, the solution is there.

Subfolders (each indexed in the build log):

- `knowledge/errors/` — every error solved, one file per error, with the resolution
- `knowledge/patterns/` — every reusable pattern discovered, one file per pattern
- `knowledge/retrospectives/` — one file per shipped client project
- `knowledge/sales/` — sales-cycle artifacts and learnings
- `knowledge/onboarding/` — client launch checklist and intake artifacts

## No `lessons/` folder here on purpose

Lessons for the website-development offering live in `knowledge/`, where they always have. Around 120 wikilinks already point into that store. Duplicating them under `Offerings/01 Website Development/lessons/` would split the knowledge graph and break those backlinks. This hub is an index into `knowledge/`, not a parallel copy.

The other offerings (Chat Assistant, Voice Receptionist, Marketing Team) DO get their own `lessons/` folders, because they have no prior knowledge store to preserve.

---

#status/active #offering/website-dev
