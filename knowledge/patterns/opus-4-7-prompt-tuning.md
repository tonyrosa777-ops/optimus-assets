# Opus 4.7 Prompt-Tuning Retrofit (Pattern #47)

**Trigger condition:** A new Claude model ships with: (a) more literal instruction-following, (b) less-warm default tone, (c) built-in progress updates that make scaffolding redundant, or (d) tokenizer inflation that changes prefix-read cost.

**Date established:** 2026-04-17 (Opus 4.6 → 4.7 migration)

## The four treatments

Apply all four to every agent and skill prompt file when a qualifying model update lands.

### 1. Replace implicit-generalization language with enumerated lists
Purge phrases: "and anything else relevant," "or similar," "as needed," "etc." Each becomes either (a) an enumerated list of what IS included, or (b) explicit "STOP after the enumerated items" language.

Why: 4.7 interprets literally. "Capture services and anything else relevant" → it captures services, skips the "anything else" as under-specified. 4.6 silently generalized.

### 2. Harden "write yourself" invention permissions
Every place an agent is permitted to invent content becomes explicit: "IF [source field] is empty or marked `⚠️ NOT FOUND`, YOU MUST write the section yourself using [voice anchor], grounded in [what we know]. Mark with `// [DEMO COPY — pending client review]`. Do not skip. Do not leave blank."

Why: 4.7 leaves sections blank under ambiguous permission. 4.6 inferred intent from context and invented.

### 3. Add no-fabrication clauses to every pinned count
Every "exactly N" or "at least N" or "target N" count gets a paired clause: "If only N-2 real items surface after genuine research, output N-2 and document why. NEVER fabricate items to reach a target count. Real and fewer beats padded and target-met."

Why: 4.7 interpreting "exactly 4 gaps" literally could invent a 4th filler gap to hit the count. Hallucination-safety requires explicit permission to fall short of counts when evidence doesn't support them.

### 4. Strip interim-progress scaffolding
Remove narrative instructions like "report status every N steps," "spot check your work," "update the orchestrator on progress." KEEP: structured Handoff blocks, correctness gates (grep X, read Y, verify Z), final output.

Why: 4.7 narrates progress natively. Scaffolding burns tokens and muddles the task.

## Applied-to files (this retrofit)

CLAUDE.md (consolidated), 7 agent files under `.claude/agents/`, 3 root-level skill files (intake-prompt.md, market-research-prompt.md, end-to-end-workflow.md), project-prime.md (minor note), new retro.md. See retrospective on 2026-04-17 retune for details.

## Related patterns
- `knowledge/patterns/opus-4-7-api-migration-checklist.md` — companion pattern for API-client code migration (future upsells).
- `knowledge/patterns/ultrareview-as-pre-launch-gate.md` — new gate added during this retune.

## Signal to watch
If a future Claude model update ships release notes mentioning:
- "more literal instruction-following"
- "built-in progress updates"
- "less warm default tone"
- new tokenizer with known inflation
- "correctly reports missing data"

→ re-run this 4-treatment pattern across the agent + skill prompt stack. Track effort via a new Pattern # row in build-log.md so the retune compounds across model generations.
