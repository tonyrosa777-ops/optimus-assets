# Optimus Empire Vault — Start Here

This is Anthony Rosa's second-brain vault, holding both the Optimus Business Solutions company layer and Anthony's personal layer. Everything Optimus knows, sells, builds, deploys, and learns lives here, alongside Anthony Rosa's personal investments, automated revenue projects, and career skill progression. The vault has **two domains** that overlap by design — Optimus is the LLC + productized services for SMB clients; Anthony Rosa is the human, the investor, the AI engineer in training. The overlap (e.g., the AI influencer skill that's both a personal revenue stream AND a client content offering) is the leverage point. If you walked in cold and need to know where something lives, this file points you at the right hub in under 30 seconds.

## Top-level map — 5 peer hubs (4 Optimus + 1 Anthony Rosa)

| Hub | Domain | What lives there | Index |
|---|---|---|---|
| `00 — Empire Index/` | both | Navigation, schemas, glossary. The hub you're in. | [[MOC — Empire]] |
| `Offerings/` | Optimus | What Optimus sells. Website Development (productized core) + four AI agent products (Chat / Voice / Marketing / Tier-4 Autonomous AI Employee). | [[MOC — Offerings]] |
| `Optimus Inc/` | Optimus | The company itself — own website, deployed agents, Optimus market intel, social pipeline, brand. | `Optimus Inc/README.md` |
| `Optimus Academy/` | both | Daily personal learning — courses, concepts, applied bridges (`apply-to-optimus/` AND `apply-to-anthony-rosa/`). | [[MOC — Learning]] |
| `anthony-rosa/` | Anthony Rosa | **Personal layer (peer hub).** Career, AI engineer roadmap, portfolio standards, wins log, private journal, **investments/** (crypto thesis, AKT tracker, Bitcoin log), **projects/** (akash-network, ai-influencer, trading-bot — automated personal revenue streams), **skills/** (career skill progression — distinct from Claude Code skills at `.claude/skills/`). | [[anthony-rosa/north-star]] |
| `knowledge/` | Optimus | Existing 108-file website-dev knowledge base — errors, patterns, retros, sales, onboarding. Untouched by the reorg. | [[knowledge/build-log]] |

**Two-domain overlap.** A single concept can apply to both domains — when it does, two single-zone bridge files are created (one in `apply-to-optimus/`, one in `apply-to-anthony-rosa/`), each tagged with one `#owner/*` value, both linking to the same shared concept file. The shared concept is the unifying point. See `Optimus Academy/apply-to-anthony-rosa/README.md` for the cross-zone split rule and the canonical AI influencer example.

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
| Drafted Pydantic schemas / FastAPI endpoint shapes for the Marketing Team Python build | `Offerings/02 AI Agents/03 Marketing Team/python-architecture.md` | `#offering/content-engine` `#status/in-development` |
| Discovered a cross-product agent pattern (e.g. CRM handoff, memory schema, tool-registry shape) | `Offerings/02 AI Agents/shared-knowledge/<pattern>.md` (use `agent-infrastructure.md` if it touches the four primitives) | `#applies-to/ai-agents` |
| Wrote or updated personal vision, technical roadmap, portfolio standards, weekly journal entry | `anthony-rosa/<file>.md` | `#owner/anthony-rosa` `#layer/optimus-os` `#status/active` |
| Tracked a crypto position, BTC/AKT decision, or investment thesis | `anthony-rosa/investments/<file>.md` | `#owner/anthony-rosa` `#status/active` |
| Started or progressed a personal automated revenue project (trading bot, AI influencer personal angle, TikTok Shop personal) | `anthony-rosa/projects/<file>.md` | `#owner/anthony-rosa` `#status/in-development` |
| Set a career skill progression goal (Python, LangChain, FastAPI, etc.) | `anthony-rosa/skills/<file>.md` | `#owner/anthony-rosa` `#status/active` |
| Captured learning that applies to a personal investment, project, or skill (not Optimus) | `Optimus Academy/apply-to-anthony-rosa/<concept-slug>.md` | `#learning/applied` `#owner/anthony-rosa` `#applies-to/anthony-rosa/<area>` `#status/active` |
| Started a custom Tier-4 Autonomous AI Employee build for a paying client | Client-specific repo at `c:\Projects\<client-slug>-employee\` for the implementation; reference spec lives in `Offerings/02 AI Agents/04 Autonomous Employee/` | `#offering/autonomous-employee` `#status/in-development` |
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
