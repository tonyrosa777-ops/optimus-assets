# Optimus Empire Vault — Start Here

This is the Optimus Business Solutions knowledge vault. Everything Optimus knows, sells, builds, deploys, and learns lives here. The vault is multi-offering — website development is the productized flagship, but it sits alongside three in-development AI products (Chat Assistant, Voice Receptionist, Marketing Team) and the company's own operating layer (Optimus Inc) and personal learning hub (Optimus Academy). If you walked in cold and need to know where something lives, this file points you at the right hub in under 30 seconds.

## Top-level map

| Hub | What lives there | Index |
|---|---|---|
| `00 — Empire Index/` | Navigation, schemas, glossary. The hub you're in. | [[MOC — Empire]] |
| `Offerings/` | The 4 products Optimus sells. Per-offering READMEs, pricing, SOPs. | [[MOC — Offerings]] |
| `Optimus Inc/` | The company itself — own website, deployed agents, Optimus market intel, social pipeline, brand. | `Optimus Inc/README.md` |
| `Optimus Academy/` | Daily personal learning — courses, concepts, applied bridges. | [[MOC — Learning]] |
| `knowledge/` | Existing 108-file website-dev knowledge base — errors, patterns, retros, sales, onboarding. Untouched by the reorg. | [[knowledge/build-log]] |

Reference docs: [[tag-schema]], [[glossary]].

## Where do I put...?

| If you just... | Put it here | Tag with |
|---|---|---|
| Solved a website-build error | `knowledge/errors/<slug>.md` + new row in `knowledge/build-log.md` | `#offering/website-dev` `#layer/offering` |
| Discovered a reusable website pattern | `knowledge/patterns/<slug>.md` + new row in `knowledge/build-log.md` | `#offering/website-dev` `#layer/offering` |
| Wrapped a client website project | `knowledge/retrospectives/<client-slug>.md` (run `/retro`) | `#offering/website-dev` `#layer/client` |
| Learned a new Claude / AI / agentic concept | `Optimus Academy/concepts/<concept>.md` + entry in `Optimus Academy/daily/<date>.md` | `#layer/optimus-os` `#learning/captured` |
| Watched a course lesson (NVIDIA, Anthropic, YouTube, book) | `Optimus Academy/courses/<source>/<course>/<lesson>.md` | `#learning/captured` |
| Found a way today's learning improves an offering | `Optimus Academy/apply-to-optimus/<bridge>.md` + cross-link into the offering hub | `#learning/applied` `#applies-to/<offering>` |
| Started tracking a new tool (NemoClaw, OpenClaw, etc.) | `Optimus Academy/tools-tracking/<tool>.md` | `#learning/captured` |
| Got asked about a new website feature by a client | Add to `Offerings/01 Website Development/` (feature spec) and cross-reference `knowledge/` for prior patterns | `#offering/website-dev` |
| Built or refined an n8n workflow for the Marketing Team | `Offerings/02 AI Agents/03 Marketing Team/workflows/<name>.json` | `#offering/content-engine` `#status/in-development` |
| Discovered a cross-product agent pattern (e.g. CRM handoff) | `Offerings/02 AI Agents/shared-knowledge/<pattern>.md` | `#applies-to/ai-agents` |
| Started tracking a new Optimus competitor | `Optimus Inc/market-intelligence/competitors/<name>.md` | `#layer/optimus-os` |
| Drafted a new Optimus social post or sales asset | `Optimus Inc/social-pipeline/` or `Optimus Inc/brand/` | `#layer/optimus-os` |
| Wrote a universal rule that applies to EVERY build | Edit `CLAUDE.md` directly (this is the constitution — change it deliberately) | n/a |

If a slot doesn't exist yet, create it. The structure should grow with the work.

## What's NOT in this vault

- **Client project repos.** Actual client builds live at `c:\Projects\<client-slug>\` as their own Next.js codebases. This vault holds the templates and the lessons, not the deliverables.
- **Per-client lessons during the build.** Capture them in the client repo's session notes as you go. After launch, run `/retro` to extract the durable findings into `knowledge/retrospectives/<client-slug>.md` here.
- **Generated assets.** fal.ai outputs, deployment artifacts, and screenshots live in their respective client repos under `/public` — never here.
- **Secrets.** No API keys, no env files. Ever.

## The website-dev workflow is unchanged

The website-dev pipeline that runs every Optimus build still operates exactly as before. `CLAUDE.md` is still the constitution. `project-prime.md`, `website-build-template.md`, `build-checklist.md`, `intake-prompt.md`, `market-research-prompt.md`, `end-to-end-workflow.md`, `frontend-design.md` are all still at vault root and still drive the build. The `knowledge/` folder still receives every solved error and discovered pattern. The reorg added hubs around the website pipeline — it did not move the pipeline.

If you came here to build a website, go to [[CLAUDE]] and run `/new-client`. Nothing changed for you.
