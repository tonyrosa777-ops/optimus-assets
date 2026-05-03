---
title: Obsidian + Claude Integration — apply-to-Optimus bridges
schema-version: 1
concept: [[../concepts/obsidian-claude-integration]]
source-references: ["[[../daily/2026-04-26#11:36 — \"Claude Obsidian is INSANE!\" by Julian Goldie SEO]]"]
created: 2026-04-26
last-updated: 2026-04-26 11:36
tags: [#learning/applied, #applies-to/ai-agents/marketing, #status/active]
---

# Obsidian + Claude Integration — apply-to-Optimus bridges

> **Concept:** [[../concepts/obsidian-claude-integration]]
> **Source(s):**
> - [[../daily/2026-04-26#11:36 — "Claude Obsidian is INSANE!" by Julian Goldie SEO]] — Julian Goldie SEO
>
> **Last updated:** 2026-04-26 11:36

---

## Applied to AI Marketing Team (Tier-3)

applies-to:: [[../../Offerings/02 AI Agents/03 Marketing Team/README]]
status:: not-started
value-vector:: revenue, productivity
expected-impact:: medium
created:: 2026-04-26
last-updated:: 2026-04-26 11:36

> **Applies to:** [[../../Offerings/02 AI Agents/03 Marketing Team/README]]
> **Status:** `not-started`
> **Value vector(s):** revenue, productivity
> **Expected impact:** medium
> **Last updated:** 2026-04-26 11:36

### What I learned

The [[../concepts/obsidian-claude-integration]] pattern — vault of plain-text notes plus Claude API plus optional Claude Code orchestration — works as a complete content-strategy substrate. Goldie's third "advanced move" describes generating five YouTube scripts in his voice from a research folder in 10 minutes, replacing what used to be a week of manual work. The vault is the substrate; Claude is the engine; the prompt is the policy.

### Why it applies to AI Marketing Team

The Marketing Team offering's current implementation uses **n8n + Supabase + GPT-4o** running weekly to score 30-day content performance and generate strategy recommendations (per `[[../../Offerings/02 AI Agents/03 Marketing Team/tech-stack-research]]`). It's a strong stack for *strategy generation from quantitative performance data*, but it does not currently address:

1. **Content generation in a client's voice** — Goldie's "use my style, use my hooks, make them punchy" workflow is precisely the gap between "here's the strategy" and "here's the post draft." Right now Optimus delivers the strategy; the client still has to write.
2. **Per-client knowledge persistence** — n8n + Supabase stores performance metrics, not client-specific brand voice, prior posts, or research artifacts. An Obsidian vault per client (or a vault per pillar within a client) gives the system durable context that improves outputs over time.
3. **Research-to-content automation** — many clients have bookmarks, articles, transcripts, and ideas they never act on. An Obsidian vault as an intake hopper plus Claude Code as the writer turns that backlog into shippable drafts on demand.

The strongest framing: **Obsidian + Claude is not a replacement for the n8n strategy engine — it's the natural complement on the *output* side.** Strategy engine says "this week, post about X for the Health pillar." Obsidian + Claude says "given X, the client's voice notes, and the research folder, here are three drafts."

### How to apply it

**Phase 1 — Validate internally on Optimus's own marketing (drink own champagne):**
- Stand up `Optimus Inc/social-pipeline/content-calendar/` as the Optimus-side vault for content drafts (already scaffolded per the Empire reorg)
- Add a `research/` subfolder where ideas, articles, transcripts, and Optimus-specific raw material live
- Invoke Claude Code (or the existing `/learn` workflow's underlying patterns) to generate weekly drafts from the research folder + the most recent Self Learning Content Engine strategy output
- Track time-to-draft and quality vs current process

**Phase 2 — Spec the productized version:**
- Decide whether Obsidian is the right substrate for clients or whether a custom vault-like UI (markdown files in a per-client folder, served through the Optimus dashboard) is cleaner
- If Obsidian: document the per-client vault layout (intake/, research/, drafts/, published/, analytics/) and the Claude Code orchestration prompts
- If custom: build the same folder model but inside the Optimus stack so the client never sees Obsidian directly
- Either way: the per-client vault becomes the second deliverable of the Marketing Team offering, alongside the strategy engine

**Phase 3 — Write the orchestration prompts:**
- "Voice extraction" — given a folder of past client posts, summarize the client's voice, hooks, sentence patterns, taboo phrases (one-time per client, refreshed quarterly)
- "Draft generation" — given a strategy directive + research folder + voice profile, output three draft variations
- "Critique loop" — given a draft + voice profile, score it against voice match, hook strength, and pillar alignment; suggest revisions
- These live in `Offerings/02 AI Agents/03 Marketing Team/workflows/` alongside the existing self-learning-content-engine.json

**Phase 4 — Decide on integration cadence:**
- Manual invoke (client logs in, clicks "generate this week's drafts")
- Watcher mode (drafts auto-generate when the strategy engine outputs a new weekly plan)
- Hybrid (auto-generated weekly drafts + on-demand regeneration)

**Phase 5 — Pricing and packaging:**
- Currently the Marketing Team offering is in development with TBD pricing. The Obsidian + Claude integration could be: (a) bundled into the base offering, (b) a separate "Voice Engine" upsell, or (c) the differentiator that pulls clients up from a passive strategy report into active draft delivery
- Decision blocked on validating Phase 1 internally

### Value vector reasoning

- `revenue`: Obsidian + Claude as the content-output layer is a candidate differentiator that pulls clients from passive strategy reports (commodity output) into active draft delivery (premium output) — meaningful uplift potential on Tier-3 close rate and ARPU once productized.
- `productivity`: voice-aware draft generation cuts the client's manual writing time from week-scale to minutes — Goldie's source claim of "10 minutes vs all week" is the upper bound; even at half that, it's a force multiplier on every Marketing Team engagement.

### Status

`not-started`

### Updates

(none)
