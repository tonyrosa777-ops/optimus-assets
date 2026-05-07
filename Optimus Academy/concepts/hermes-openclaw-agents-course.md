---
title: Hermes + OpenClaw Agents Course (Julian Goldie)
schema-version: 1
domain: agents
created: 2026-05-06
last-updated: 2026-05-06 21:18
review-by: 2026-11-06
source-references: ["[[../daily/2026-05-06#21:18 — \"FREE Hermes + OpenClaw AI Agents Course: Build & Automate ANYTHING\" by Julian Goldie SEO]]"]
enriched-from: []
level: intermediate
prerequisites: ["[[openclaw-multi-agent-orchestration]]"]
audience: [developer, founder]
tags: [#learning/synthesized, #applies-to/ai-agents, #status/active]
---

# Hermes + OpenClaw Agents Course (Julian Goldie)

> **Concept distilled from:**
> - [[../daily/2026-05-06#21:18 — "FREE Hermes + OpenClaw AI Agents Course: Build & Automate ANYTHING" by Julian Goldie SEO]] — Julian Goldie SEO
>
> **Last updated:** 2026-05-06 21:18

## What it is

Julian Goldie's 5-hour course is a hands-on, opinionated tour of the open-source AI-agent landscape as of late April 2026, anchored on two tools: **Hermes** (a self-improving agent runtime built by Noose Research, MIT-licensed, launched February 2026) and **OpenClaw** (the older orchestration framework by Peter Steinberger, formerly Claudebot/moldbot). The course's combined methodology layers Hermes or OpenClaw underneath orchestration shells (Paperclip "company structure," Multica "team workspace," Hermes Workspace v2) plus a pluggable memory layer (Obsidian, OMI auto-capture, Honcho, Mem-Zero, the LLM-wiki pattern from Karpathy), a community-skills marketplace (agentskills.io / Wonderlay / Claw Hub), and a free-forever cost path through Olama (Ollama) running local models. Julian's empirical claim by chapter 54: Hermes Agent has surpassed OpenClaw on reliability, ease of setup, and rate of improvement; both remain free, both remain open-source, and serious operators run both in parallel.

## When to use

- A founder evaluating multi-agent runtimes for production needs to know how the same patterns are being framed by indie operators (vs. Nate B. Jones's production-grade thesis on OpenClaw, see [[openclaw-multi-agent-orchestration]]).
- Choosing between Hermes vs OpenClaw vs Manis (or Maxclaw, Kimclaw) when local-vs-managed and skill-portability are decision drivers.
- Designing a Tier-3 Marketing Team or Tier-4 Autonomous Employee that needs persistent memory, scheduled tasks, sub-agent delegation, and channel-native messaging without inventing the substrate from scratch.
- Building a personal capture pipeline (Anthony's Optimus Academy) where Karpathy's LLM-wiki pattern (raw sources / wiki / schema with ingest/query/lint operations) maps cleanly onto the existing daily/concept/bridge structure.
- Deciding whether the Optimus canonical Python stack (FastAPI + anthropic SDK direct + Pydantic + supabase-py + Twilio + Personaplex) needs to evolve when Hermes appears to ship five primitives natively (memory, tool registry, observability, approval, plus a fifth: skill compounding).

## Mechanics

### What Hermes is (Noose Research project)

Hermes is an open-source MIT-licensed AI agent runtime published by Noose Research, a research lab Julian positions as builders of foundation models (the Hermes, Nomos, and Psyche model families) rather than a single-developer side project. Hermes launched February 2026. Tagline: "an agent that grows with you." Single-curl install on Linux, macOS, or WSL2. Runs on a $5 VPS, on Docker, over SSH, on Singularity, on Modal, on Daytona (six terminal backends total). Ships with 40+ built-in tools (web search, terminal, file system, browser automation, image gen, TTS, code execution, sub-agent delegation, memory, scheduling), connects to 200+ models through OpenRouter / Noose Portal / OpenAI-compatible endpoints. Native messaging-channel surface in v0.9 covers 16 platforms including Telegram, Discord, Slack, WhatsApp, Signal, email, iMessage (via BlueBubbles relay), WeChat, Matrix, Mattermost. Native Android via Termux. Local web dashboard at `hermes dashboard`. The course names version 0.7 (pluggable memory release), version 0.8 (the "Intelligence Release" on April 8, 2026, with 209 merged PRs), and version 0.9 (the "Everywhere Release") as the milestones that crossed Hermes from "developer toy" to "platform."

### How Hermes self-improves via skills

After completing a complex task (Julian defines complex as "five or more tool calls"), Hermes writes a new skill file describing how it solved the problem. Skills live as folders inside `Hermes/skills` on disk, each containing a `skill.md` document. Two reinforcing loops operate on top of this storage: skills self-improve during use (the agent edits its own `skill.md` after each run that reveals a refinement), and the agent maintains a `memory.md` file with project context plus a `user.md` file modeling how the operator communicates and what they care about. Both files inject into the system prompt at the start of every session. Julian's first-week prescription: do not treat early sessions as productive, treat them as learning sessions where the agent is building memory.md and user.md. By day 3-4 the agent has enough context to stop asking the user to repeat themselves.

The skill registry is efficient at startup: the agent only sees skill names and short descriptions until a skill is actually invoked, so dozens of installed skills do not bloat the system prompt. The discovery surface is `agentskills.io`, an open standard that makes skills installable across Hermes, Claude Code, and Cursor without re-authoring. Community skill libraries include the Awesome-Hermes-Agent curated list (by 0xyk), Claw Hub (the OpenClaw community marketplace, also Hermes-compatible), and Wonderlay Skills (250+ stars, multi-platform). Install pattern: `Hermes skills install wonderlay-skills`, then `Hermes skills browse`. A built-in security scanner runs on any skill before install, checking for data-exfiltration, prompt-injection, destructive commands, and supply-chain issues.

### Hermes vs OpenClaw, Julian's empirical take (April 2026)

Julian's bottom line by chapter 54: "Honestly, I'm over OpenClaw." His diagnosis is that OpenClaw was magical at January 2026 launch ("seemed a lot easier to set up when it first came out"), but successive functionality additions made it "really difficult and technical to use." Specific failures he cites from his own daily use: OpenClaw broke with Telegram three times in a single week; the gateway-token-refresh flow is "super messy and annoying"; updates frequently leave the install in a broken state requiring two hours of debugging; even GPT does not configure properly with OpenClaw despite the reported Steinberger-OpenAI partnership. He still respects Peter Steinberger and acknowledges the maintainer is under stress from user volume. By contrast, Hermes "just works" for him and is iterating faster.

This needs reconciliation against the existing vault concept [[openclaw-multi-agent-orchestration]], which frames OpenClaw as production-grade per Nate B. Jones's April 2026 maturity claim. Both can be true: Nate's claim is about hierarchical multi-agent topology, Docker-per-agent isolation, RPC inter-agent communication, and channel-native behavior at the architecture level. Julian's claim is about daily reliability, ease of setup, and breaking-change frequency at the operator level. The two views agree that OpenClaw is fast-moving and that pinning versions is mandatory; they disagree on whether the experience holds together for a single operator on any given day. For Optimus's evaluation in [[../tools-tracking/openclaw]], Julian's data point is one row in the decision log, not a verdict.

### Multi-agent orchestrators (Paperclip vs Multica vs Hermes Workspace)

Three orchestration shells sit on top of Hermes (or OpenClaw, or both) to coordinate multiple agents:

- **Paperclip** wraps agents into a "company structure" with explicit C-suite roles (CEO, CMO, COO, founding engineer). Each role has a title, a reports-to relationship, a job description, capabilities, and a per-role model assignment. The CEO agent surfaces proposals and questions in an "Inbox" that the human approves or rejects; the CEO then drafts new specialist agents on approval. Built-in primitives: per-agent budgets with auto-stop, scheduled heartbeats, full ticketing audit log, phone-monitorable dashboard. Julian's verdict: best for solo operators who want hierarchical control. The Hermes-specific install path is the "Hermes Paperclip Adapter," which Julian live-installs by pasting the GitHub URL into a Hermes terminal session and asking Hermes to set it up locally.

- **Multica** wraps agents into a "team workspace" with first-class human collaborators (members can be invited, agents have private vs workspace visibility scopes). Linear-style Kanban board (backlog / to-do / in progress / in review / done / blocked) where tasks are assigned to agents, agents post status updates in an inbox, and the board updates as work completes. Persistent skill registry shared across the workspace. Multi-workspace support for multi-tenancy. Julian's verdict: best when real human teammates are part of the loop; both Multica and Paperclip can be "buggy as well sometimes."

- **Hermes Workspace v2** is Noose Research's first-party GUI shell for Hermes specifically. Browser-based, free, open-source, install via Docker (siloed) or local. Surfaces include Chat, Files manager, Operations (grid view, round-table office view, Conductor coordinator), Kanban Tasks board, Profiles (multiple distinct agents per Hermes install), Memory editor, Skills manager, model switcher (cloud vs local toggle), built-in terminal, scheduled jobs view. PWA-installable for desktop and mobile. Two-thousand-plus skills accessible. Julian's strongest UX endorsement of the entire course: "honestly, that's one of the coolest things I've seen" referring to the Operations office visualization.

### Memory architecture (pluggable + Obsidian + OMI + LLM Wiki + OB1)

Julian's recommended memory recipe is layered:

1. **Obsidian as primary backend.** The natural-language wiring instruction is literally "go to obsidian locally and use that as your memory." The user maintains markdown notes for "what we sell," "who I am," "my business," "personal memories." Hermes ingests the vault directly. To scope, instruct Hermes "focus on this folder" or "focus on this specific file" rather than the whole vault.

2. **OMI for auto-capture.** OMI records screen and microphone, generates memory artifacts, and syncs them into Obsidian automatically. The privacy posture is "set your own limits with that," but the upside is zero manual note-taking.

3. **Hermes pluggable memory engine** (shipped in v0.7). Memory becomes a swappable plug-in layer. Six-to-seven supported backends, with Honcho and Mem-Zero named. Setup: `Hermes memory setup`. The engine injects retrieved context before every response and syncs after every interaction.

4. **The LLM-wiki pattern from Andre Karpathy (April 4, 2026).** A persistent, AI-maintained markdown wiki sits between user and raw sources. Three layers: raw sources (immutable, AI reads but never edits), wiki (AI-generated markdown of summaries / entity pages / concept pages / synthesis, AI-owned), schema (config document defining structure and conventions, co-evolved by user + agent). Three operations: ingest (drop a source, AI extracts and updates 10-15 wiki pages in one pass), query (AI synthesizes from wiki, files good answers back as new pages), lint (AI health-checks for contradictions, stale pages, orphans, missing links). Hermes ships LLM wiki as a built-in skill via `/llm wiki <topic>` after `Hermes update`. Karpathy's framing: "the LLM is the programmer, the wiki is the codebase, Obsidian is the viewer."

5. **OB1 (Open Brain)** is the OpenClaw-side memory companion (per [[openclaw-multi-agent-orchestration]]); not addressed by Julian but worth flagging as the parallel path on the OpenClaw side.

### Skill ecosystem and one-click upgrade

The unified skill model: skills are markdown folders, portable across runtimes via the agentskills.io standard, installable from Claw Hub or Wonderlay or any GitHub source via `Hermes skills install <name>`. After installing the Wonderlay library each skill becomes a slash command (`/arxiv`, `/github-pr-workflow`). Julian's portability discipline: maintain a skill backup doc external to any agent runtime, one entry per skill containing description, recreation steps, and reference screenshots. Reasoning: Hermes launched February 2026, OpenClaw January 2026, "something bigger and better than both will ship in the future." Skill backups decouple operator IP from any single runtime.

### Cost model

Real OpenRouter spend Julian reports: $7 in a single morning of "rinsing it" while setting up automations on GLM 5 Turbo. He frames this as worst-case onboarding burn, not steady-state. The brain-plus-local-sub-agent pattern is the cost-control architecture: a hosted brain (Claude / GLM 5 Turbo / MiniMax M2.7) handles orchestration and planning, local Olama models on sub-agents absorb the cheap calls. Free path: Olama + Mimo V2 Pro on Newsportal (free for two weeks via the Noose Research / Xiaomi partnership announced April 7, 2026; one trillion parameters, one million token context) or Quen 3.6+ on OpenRouter (1M token context, free while Alibaba tests at scale). Idle cost on Modal or Daytona is "almost nothing" since the agent hibernates and wakes on demand.

### Use case patterns Julian demos

- **SEO automation.** Hermes scheduled to create a new keyword-targeted landing page every hour, deployed to Netlify subdomains, custom-domain wiring two clicks away. Live demo of bestaiagentcommunity.com ranking #1 on Google for "enterprise SEO ROI calculator" (~600 monthly searches per Ahrefs). Each page ships with SEO meta tags, schema markup, embedded VSL, six CTAs, direct-response copy with social proof, mobile-responsive layout. Powered by the Skill Boss paid plugin.
- **Competitor + content pipeline.** Hourly trending-topics scan, every-4-hour competitor monitor flagging out-performing posts, every-6-hour fresh keyword discovery with intent classification + domain candidates + search volume + headline hooks, on-demand thumbnail / landing page / Reddit draft / Tweet generation.
- **Daily journal.** Anthony-style discipline: copy a template each day, stamp date and day-number, log progress, log skills installed, log to-dos, log shipped work. The journal lives inside Hermes itself.
- **Manim animated explainers.** Hermes's Manim skill writes Python code that renders 3Blue1Brown-style animated math/algorithm/data videos from a single prompt. Demo prompt: "create an explainer using manim about how Hermes agent works." Output: 90-second branded video. Default render below 1080p; 1080p export available but slower.
- **Pab's Avatar Skill.** Real-time face-and-voice avatar via PA Skills Open repo. Avatar joins meetings, generates auto-meeting-notes, preserves the underlying agent's memory and personality. Integrates either via UNIF API (text-to-video digital humans) or WebRTC (low-latency voice/video). Customization at pika.me. Julian's course is partly delivered by his own Pab-style avatar with explicit on-screen disclosure.
- **Website-build race.** Live N=1 demo: same prompt ("create a beautiful fun website plus deploy locally plus give me the localhost address"), same hardware, same backend (MiniMax M2.7 Cloud via Olama). Hermes streams progress updates and finishes faster with a nicer-looking page; OpenClaw runs silently and produces a more basic page slower.
- **Welcome-message agent.** Trigger on new Skool member signup, agent drafts personalized welcome via Gmail through Zapier MCP. Running on Olama locally, $0 marginal cost.

### Failure modes Julian acknowledges

- Hermes self-learning "can sometimes overwrite behaviors you actually liked." Skill regression with no diff is a real risk.
- Hermes has fewer integrations than OpenClaw, "but that is changing fast."
- Hermes's learning is "not always spot-on. Sometimes it learns the wrong lesson from a task."
- The Hermes v0.9 dashboard does not let the user chat directly with the agent (chat is in workspace v2 or terminal or Telegram instead).
- Local models (Gemma 4) are too slow for an agent loop even on Apple M4 Max hardware (~1 minute per response). Cloud models are recommended for the recommended-list backends (Kimmy K2.5 Cloud, Quen 3.5 Cloud, GLM 5.1 Cloud, MiniMax M2.7 Cloud).
- Olama bridge can overwrite an existing Hermes config; back up before swapping.
- Multica and Paperclip are "quite buggy as well sometimes."
- Models break upstream (Julian's GLM 5 outage example): Hermes appears to hang, but the actual fault is the model API. Recovery: open Hermes in terminal, paste error logs, ask Hermes to fix itself ("9 times out of 10"); fall back to Claude Code if self-repair fails.

## Examples

**Install Hermes (one-line on Linux/macOS/WSL2):**
```
curl -fsSL https://raw.githubusercontent.com/nous-research/hermes-agent/main/scripts/install.sh | bash
source ~/.bashrc
Hermes setup
Hermes
```

**Free-forever Olama bridge:**
```
Olama launch Hermes
```
Pick a recommended cloud model (GLM 5.1 Cloud or MiniMax M2.7 Cloud), then talk in terminal or via Telegram.

**Migrate from OpenClaw to Hermes:**
```
Hermes claw migrate          # supports --dry-run to preview
```

**Activate fast mode (priority queue routing for GPT 5.4 + Claude Fast Tier):**
```
/f fast
```

**LLM-wiki pattern:**
```
Hermes update
/llm wiki <research topic>
```

**Discovery prompt template after memory is loaded:**
```
knowing what you know about me, how can you help me?
```

**Memory wiring template:**
```
go to obsidian locally and use that as your memory
focus on this folder
```

**Backup and restore an entire Hermes setup:**
```
Hermes backup
Hermes import
```

## Gotchas

- **OpenClaw star-count discrepancy.** Julian quotes OpenClaw at 340,000-345,000 stars (April 2026); the existing [[../tools-tracking/openclaw]] entry records ~310,000 stars (May 3 capture from nate.b.jones); chunk 24 contradicts itself by stating Hermes at 26,000 stars in one breath and "nearly 2,000 stars" in another. Verify against live GitHub before citing any number externally.
- **Hermes star-count internal inconsistency.** Julian gives 8,100 in one chunk, 11,600 in another, 15,000 in a third, 26,000 in a fourth, 32,000 in a fifth, 106,000 in a sixth. The course is stitched from separately-recorded segments at different dates; treat any single Hermes star-count claim as point-in-time.
- **Julian's "I'm over OpenClaw" framing vs the existing vault concept's "production-grade" framing.** Both can be true. Nate B. Jones's claim is architectural maturity (hierarchical agents, Docker-per-agent, RPC, channel-native behavior). Julian's claim is daily-operator reliability (Telegram broke 3x/week, gateway-token-refresh friction, install regressions). The vault concept needs Julian's data point in its Gotchas section but does not need to flip the verdict.
- **Olama vs Ollama spelling.** Julian writes/says "Olama" / "OAMA" / "Lama" / "Alama" interchangeably across all 25 chunks. This is almost certainly the upstream Ollama project. Vault canonical spelling stays "Ollama" with a one-time note that Julian's "Olama" refers to it.
- **Auto-caption transcription artifacts.** Julian's audio is heavy with mishearings: "Noose Research" → "Nurse Research" / "News Research" / "Nova Research." "Manim" → "Manm" / "Mim" / "Batman." "Claude Sonnet" → "Claude Sonic." "Xiaomi" → "Shaomi" / "Shyomi" / "Jaomi." "MiniMax" → "Beimo" / "Miniax." "Mattermost" → "Matamos." "MCP OAuth 2.1 + PKCE + OSV" → "MCPO orth + OOTH 2.1 + PKC + OSV." "Pab's Avatar Skill" → "PA" / "AI avatar" / "just-an-avatar." Treat any phonetic spelling as suspect; verify canonical names before quoting.
- **Digital-avatar narration vs Julian's direct opinions.** Multiple chapters are narrated by Julian's Pab-style AI avatar with on-screen disclosure ("I am the digital avatar of Julian Goldie"). The avatar's opinions track Julian's framing but are produced by an AI content pipeline. Do not treat avatar-narrated claims as if Julian personally validated each one in real time; they are scripted output.
- **Promotional content loops.** Julian plugs the AI Profit Boardroom (paid Skool community, member counts cited as 2,000 / 2,700 / 2,800 across chunks), AI Success Lab (free, member counts cited as 38,000 / 40,000 / 58,000 across chunks), a 2-hour Hermes course, and a 6-hour OpenClaw course in nearly every chapter. Promotional content gets one home in the daily file ("Promotional inserts" sub-section), not repeated.
- **"Newsportal" / "Noose Portal" / "Nice Portal" / "Nous Portal."** All transcription variants of the same Noose Research model hub. Canonical: Noose Portal (a.k.a. Nous Portal depending on whether the lab is "Noose" or "Nous Research"; the GitHub org slug is unverified in the course audio).
- **Hermes is text-channels-first.** Voice / Twilio Media Streams is not part of the v0.9 surface area, so for Optimus's Tier-2 Voice Receptionist Personaplex remains canonical regardless of any Hermes adoption decision.
- **Recommended Hermes model list skews to Chinese cloud models** (Kimmy, Quen, GLM, MiniMax). For US small-business client deployments, evaluate data-residency and ToS implications before recommending these as defaults.
- **The 16-platform claim partially conflates channels with surfaces.** Julian counts iMessage (BlueBubbles relay), WeChat, WeCom 2 plus the named six (Telegram, Discord, Slack, WhatsApp, Signal, email) as nine messaging platforms; the additional seven that get to "16" are unaccounted for in any single chunk. Likely includes Termux, browser dashboard, terminal, Matrix, Mattermost.
- **Cost numbers are anecdotal.** $7/morning OpenRouter spend, "near zero on Modal/Daytona idle," "5-second loops drop to 1-second on fast mode" are all single data points. None are benchmarks; treat as direction, not measurement.

## Related Concepts

- [[openclaw-multi-agent-orchestration]] — peer concept, cross-link required. This concept covers Julian's empirical hands-on take from late April 2026 with Hermes as the rising challenger and OpenClaw as the declining incumbent. For the architectural deep-dive on OpenClaw itself (hierarchical agent topology, Docker-per-agent isolation, RPC inter-agent communication, multi-channel substrate, OB1 memory companion), see the peer concept. The two concepts disagree at the operator-experience layer (Julian's "I'm over OpenClaw" vs Nate B. Jones's "production-grade") but agree at the architectural layer (multi-channel native, multi-model abstraction, fast-moving dependency surface).

## Updates
