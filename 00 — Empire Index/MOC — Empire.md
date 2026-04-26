# MOC — Empire

Top-level Map of Content. Every major area of the Optimus vault, indexed.

## Offerings — what Optimus sells

`Offerings/` houses the 4 product lines. Website Development is fully productized; the three AI products are in active development under the AI Agents umbrella. Full breakdown in [[MOC — Offerings]].

- [[Offerings/01 Website Development/README]]
- [[Offerings/02 AI Agents/README]]
  - [[Offerings/02 AI Agents/01 Chat Assistant/README]]
  - [[Offerings/02 AI Agents/02 Voice Receptionist/README]]
  - [[Offerings/02 AI Agents/03 Marketing Team/README]]
  - `Offerings/02 AI Agents/shared-knowledge/` — cross-product agent patterns (CRM handoff, LLM routing, voice/chat unification)

## Optimus Inc — the company itself

`Optimus Inc/` is where Optimus operates as its own customer. The Optimus website (built from the same template), the deployed Voice Receptionist answering Optimus's own calls, market intel on Optimus competitors, the social pipeline, and the brand kit all live here. Drink your own champagne — see [[glossary]].

- `Optimus Inc/README.md`
- `Optimus Inc/website/` — the Optimus Business Solutions site
- `Optimus Inc/deployed-agents/` — Optimus's own Chat + Voice + Marketing instances
- `Optimus Inc/market-intelligence/` — competitors, positioning, audience research
- `Optimus Inc/social-pipeline/` — social content queue, calendar, performance
- `Optimus Inc/brand/` — logo, voice guidelines, color tokens, type system

## Optimus Academy — daily personal learning

`Optimus Academy/` is Anthony's learning system. Every day's capture, every course lesson, every atomic concept note, every bridge from learning to offering improvement lives here. Full map in [[MOC — Learning]].

- [[Optimus Academy/README]]
- `Optimus Academy/daily/` — dated entries, one per learning day
- `Optimus Academy/courses/anthropic/`, `courses/nvidia/`, `courses/youtube/`, `courses/books/`
- `Optimus Academy/concepts/` — Zettelkasten-style atomic concept notes
- `Optimus Academy/tools-tracking/` — emerging tools (NemoClaw, OpenClaw, etc.)
- `Optimus Academy/apply-to-optimus/` — bridge notes linking learning to specific offerings

## Empire Index — this hub

`00 — Empire Index/` holds the navigation, the tag schema, and the glossary. Everything else is content; this is the map.

- [[README]] — Start Here
- [[MOC — Empire]] — this file
- [[MOC — Offerings]]
- [[MOC — Learning]]
- [[tag-schema]] — the canonical tag taxonomy
- [[glossary]] — Optimus-specific term definitions

## Workflow templates (vault root)

The constitution and the build pipeline. These files do not move during the reorg — they remain at the vault root because every offering's workflow is anchored to them.

- [[CLAUDE]] — the constitution. Plan Mode rule, Subagent Delegation rule, Always-Built Features, Hero Architecture, Visual QA gate. Read first, every session.
- [[project-prime]] — orchestrator workflow that runs intake → research → scaffold → build → launch
- [[website-build-template]] — tech stack, directory structure, animation patterns, API routes
- [[build-checklist]] — phase-by-phase checklist enforced by `project-prime`
- [[end-to-end-workflow]] — top-level workflow doc

## Prompts (vault root)

The slash-command prompt files. Each one is the canonical text invoked by its corresponding `/command`.

- [[intake-prompt]] — `/intake`
- [[market-research-prompt]] — `/market-research`
- [[retro]] — `/retro`
- `learn-prompt.md` (to be created) — `/learn`, the daily learning capture for Optimus Academy

## Design references (vault root)

- [[frontend-design]] — UI/UX rules, layout, component architecture
- `design-system.md` — brand constitution (per-project, filled per build)
- [[animation-inspiration]]
- [[animated-logo-inspiration]]
- `Revamp logo light.png`

## Per-project files (vault root, filled per build)

These are scaffolded fresh for every client engagement and live at the vault root only during that engagement. They do not represent permanent vault content.

- [[initial-business-data]] — client intake output
- [[market-intelligence]] — research output

## Knowledge base — website-dev memory

`knowledge/` is the existing 108-file website-development knowledge base. It pre-dates the reorg, serves only the website-dev offering, and is referenced by [[CLAUDE]]'s Knowledge Base Rule. Every error solved and pattern discovered on a website build lands here.

- [[knowledge/build-log]] — the master index (Error Encyclopedia, Build Patterns, Project Retrospectives)
- `knowledge/errors/` — detailed per-error postmortems
- `knowledge/patterns/` — reusable build patterns
- `knowledge/retrospectives/` — per-client launch postmortems
- `knowledge/sales/` — sales collateral and pitch material
- `knowledge/onboarding/` — client launch checklists
