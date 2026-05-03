---
title: Apply to Optimus
created: 2026-04-26
last-updated: 2026-04-26
tags: [#layer/optimus-os, #status/active]
---

# Apply to Optimus

This folder captures the moments when something learned in Optimus Academy can directly improve an Optimus system, agent, craft, or operations area. One file per insight. Each file explicitly names: the concept (link to the concept note in `[[../concepts/]]`), the source(s) where the concept was learned (daily-anchor wikilinks), the target file/area the insight applies to, **the value vector(s) it serves** (productivity / overhead / revenue), and how to apply it. This is where personal daily learning becomes business value.

## Five bridge target zones — not just offerings

Bridge `applies-to:` targets route to one of five zones depending on where the knowledge would actually integrate. The bridge layer is intentionally broader than the four AI offerings — sales-training feeds copy craft, finance content feeds Optimus Inc operations, marketing psychology feeds CRO, tool reviews feed the internal stack.

| Zone | Folder | When it applies | Folder existence |
|---|---|---|---|
| `Offerings/<offering>/` | Existing offering hub | Concept changes how a productized offering is built or operated | All exist |
| `knowledge/patterns/` | Cross-website-build patterns | Pattern that any client site could reuse | Exists, populated |
| `knowledge/craft/<area>/` | `copywriting`, `psychology`, `sales`, `design` | Cross-cutting craft principle that shapes copy/visuals/sales motion across all builds | Lazy-create on first use |
| `Optimus Inc/<area>/` | `finance`, `operations`, `brand`, `website`, `market-intelligence`, `social-pipeline`, `ai-agents/<tier>/` | Concerns Optimus the company itself, not the offerings | Some exist (`brand`, `website`, `market-intelligence`, `social-pipeline`, `ai-agents/<tier>/`); `finance` and `operations` lazy-create per-area |
| `Optimus Academy/tools-tracking/<tool-slug>.md` | Flat file per tool | Evaluating whether to adopt a tool into Optimus's stack | Folder exists with `.gitkeep`; populates on first real file |

A single concept may produce multiple bridges — one per applicable zone. The bridge schema (concept link, why-it-applies, how-to-apply, value-vector reasoning, status, updates) is identical across all five zones.

## File naming convention

`<concept-slug>-applied-to-<target-slug>.md`

`<target-slug>` is derived from the target file's path (deterministic). Examples:

- `prompt-caching-applied-to-website-dev.md` (offering)
- `agentic-loops-applied-to-ai-voice.md` (offering)
- `pricing-anchor-applied-to-content-writer.md` (`.claude/agents/build/content-writer.md`)
- `pricing-anchor-applied-to-craft-copywriting.md` (`knowledge/craft/copywriting/`)
- `runway-rules-applied-to-optimus-inc-finance.md` (`Optimus Inc/finance/`)
- `langgraph-applied-to-tools-tracking.md` (`Optimus Academy/tools-tracking/langgraph.md`)

One concept can apply to multiple target zones. When that happens, write multiple files — one per target. Do not bundle. Each application has its own mechanism, its own value-vector reasoning, its own implementation steps, and its own status to track.

## Multi-purpose principle — every bridge declares a business outcome

Every bridge MUST declare at least one `value-vector` from `productivity` / `overhead` / `revenue` with concrete reasoning. Multi-valued by default — most bridges serve 2-3 vectors simultaneously.

| Vector | What it means | Examples |
|---|---|---|
| `productivity` | Speed/quality of building, shipping, or operating | New animation pattern that cuts hero-build time 30% • Better critic prompt that improves first-pass quality • SEO checklist that prevents post-launch rework |
| `overhead` | Reduces manual work, context-switching, duplication, error rates | Folder-creation policy that prevents empty-folder noise • Skill that auto-generates boilerplate • Pattern that prevents a recurring error from build-log.md |
| `revenue` | Pricing, conversion, retention, offerings, or new tiers | New pricing-page tactic from a sales source • CRO heuristic that lifts quiz-to-booking conversion • Better cold-email sequence |

**No-bridge stop conditions:** if `/learn` cannot identify (a) a clear target file in the vault that would meaningfully integrate the knowledge AND (b) at least one value vector with concrete reasoning, it does NOT create a bridge — concept note only. Vague bridges pollute the weekly review and dilute the prioritization layer.

## Frontmatter spec

```yaml
---
title: <Concept> applied to <Target>
schema-version: 1
concept: [[../concepts/<concept-slug>]]
source-references: ["[[../daily/YYYY-MM-DD#HH:MM — \"Source Title\" by Publisher]]"]
applies-to: [[<wikilink-to-target-file>]]
created: YYYY-MM-DD
last-updated: YYYY-MM-DD HH:MM
status: not-started
value-vector: [productivity, revenue]    # MANDATORY, multi-valued, at least one of {productivity, overhead, revenue}
expected-impact: medium                  # OPTIONAL, populate when source makes magnitude obvious — small | medium | large
tags: [#learning/applied, #applies-to/<zone-tag>]
---
```

The `source-references:` list grows over time as new sources teach more about the same concept. The `value-vector:` list can also grow during APPEND if a later source reveals an additional vector (e.g., a bridge originally tagged `[productivity]` learns from a new source that the same pattern lifts revenue → becomes `[productivity, revenue]`). Never remove vectors during APPEND.

`schema-version: 1` is mandatory on every bridge file — enables safe future migrations when the structure evolves.

**Tag mapping by target zone:**

| Target zone | Tag |
|---|---|
| `Offerings/01 Website Development/` | `#applies-to/website-dev` |
| `Offerings/02 AI Agents/...` | `#applies-to/ai-agents` (or `#applies-to/ai-agents/{chat,voice,marketing}`) |
| `knowledge/craft/copywriting/` | `#applies-to/craft/copywriting` |
| `knowledge/craft/psychology/` | `#applies-to/craft/psychology` |
| `knowledge/craft/sales/` | `#applies-to/craft/sales` |
| `knowledge/craft/design/` | `#applies-to/craft/design` |
| `Optimus Inc/finance/` | `#applies-to/optimus-inc/finance` |
| `Optimus Inc/marketing/` | `#applies-to/optimus-inc/marketing` |
| `Optimus Inc/operations/` | `#applies-to/optimus-inc/operations` |
| `Optimus Inc/brand/` | `#applies-to/optimus-inc/brand` |
| `tools-tracking/<tool>.md` | `#applies-to/tools/<tool-slug>` |

## Visible blockquote header

Right under the H1, every bridge note carries a visible attribution blockquote so the reader sees the full trail (concept → sources → target → vectors → status) without peeking at YAML:

```
> **Concept:** [[../concepts/<concept-slug>]]
> **Source(s):**
> - [[../daily/YYYY-MM-DD#HH:MM — "Source Title" by Publisher]] — <publisher>
> - [[../daily/<later-date>#HH:MM — "Other Source Title" by Other Publisher]] — <publisher>
> **Applies to:** [[<wikilink-to-target-file>]]
> **Status:** `not-started`
> **Value vector(s):** productivity, revenue
> **Expected impact:** medium
> **Last updated:** YYYY-MM-DD HH:MM
```

Source references use **daily-anchor wikilinks** — `[[../daily/YYYY-MM-DD#<H2 heading text>]]`. The anchor text is the H2 heading from the daily file (Obsidian resolves `[[file#heading]]` natively). This points at the actual H2 capture section inside the daily file, not at a separate source file.

## Body structure — rigid identical contract

Every bridge note follows the same six-section body (plus Updates). **All section headers are always present, in the same order, even when the section has no content.** Empty sections show literally `(none)` as the body. This is non-negotiable — predictability beats efficiency.

### `## What I learned`

Short summary of the concept with a wikilink to the concept note. Do not re-explain the concept here — the concept note is the source of truth. This section just establishes the hook.

### `## Why it applies to <target>`

The concrete mechanism. Why does this concept improve this specific target file or area? What problem does it solve, what cost does it cut, what new capability does it unlock? Be specific. Vague answers ("better quality") are a sign the application isn't real yet.

### `## How to apply it`

Actionable steps. File paths to edit. Agent files to update. Workflow tweaks. Env vars to set. The reader should be able to execute this section without re-reading the concept note. **Important:** bridges to agent files do NOT auto-edit the agent. The bridge is the change-request; Anthony reviews and applies the change manually (per the LEDGER rule — human review of agent edits is mandatory).

### `## Value vector reasoning`

For each vector tagged in `value-vector:`, one sentence on the concrete mechanism. This is what gets reviewed weekly to prioritize bridges by leverage.

Examples:
- `productivity`: every future client site inherits this anchor via content-writer.md, ~10 min saved per pricing-page build
- `revenue`: lifts quiz-to-booking conversion ~5% based on source's cited data
- `overhead`: removes the manual "did I remember to anchor?" check from every build

### `## Status`

One of: `not-started` / `in-progress` / `applied` / `verified`. Mirrored in frontmatter.

- `not-started` — bridge note exists, no implementation yet
- `in-progress` — implementation underway
- `applied` — shipped, working in production
- `verified` — measured and confirmed to deliver the predicted improvement

### `## Updates`

Empty on creation but the header is still present — it is the contract that signals "this is where future findings will land." When a new source adds to this insight, append a `### YYYY-MM-DD HH:MM — <label> — from [[../daily/<date>#<anchor>]]` block here. Decisions made, blockers hit, results measured, new source findings — all stack chronologically. The original `## What I learned` / `## Why it applies` / `## How to apply it` content stays byte-identical from one update to the next; deltas live in `## Updates`.

## Promotion path

When a note here reaches `verified` status, consider promoting the pattern into the appropriate institutional location so it becomes a reusable asset across projects:

- Bridge target was `Offerings/<offering>/...` → promote to `Offerings/<offering>/lessons/<slug>.md`
- Bridge target was a `.claude/agents/<area>/<agent>.md` file → the agent edits already happened during APPLY; promote to `knowledge/patterns/<slug>.md` if the underlying pattern is broader than the agent
- Bridge target was `knowledge/craft/<area>/<slug>.md` → already in the institutional location; mark `verified` and move on
- Bridge target was `Optimus Inc/<area>/<slug>.md` → promote internally if relevant; this is the canonical location for Optimus's own ops
- Bridge target was `tools-tracking/<tool>.md` → if the tool was adopted, promote the adoption pattern to `Offerings/02 AI Agents/shared-knowledge/lessons/<slug>.md` or wherever it's used

The bridge note documents the discovery; the pattern doc documents the institutional rule. Promotion is manual (no autopilot) — Anthony reviews each `verified` bridge and decides whether the underlying pattern earned institutional status.

## Worked example bridges (one per zone)

**Example 1: Bridge to an offering**

`prompt-caching-applied-to-website-dev.md`:

```yaml
applies-to: [[../../Offerings/01 Website Development/README]]
value-vector: [productivity, overhead]
expected-impact: medium
```

**Example 2: Bridge to a craft folder (lazy-create scenario)**

`anchoring-pricing-applied-to-craft-copywriting.md`:

```yaml
applies-to: [[../../knowledge/craft/copywriting/anchoring-pricing]]
value-vector: [productivity]
expected-impact: small
```

The folder `knowledge/craft/copywriting/` did not exist before this bridge; `mkdir -p` creates it.

**Example 3: Bridge to an agent file (highest-leverage scenario)**

`anchoring-pricing-applied-to-content-writer.md`:

```yaml
applies-to: [[../../.claude/agents/build/content-writer]]
value-vector: [productivity, revenue]
expected-impact: medium
```

The bridge describes how to update content-writer.md; Anthony reviews and applies the agent edit manually.

**Example 4: Bridge to Optimus Inc operations (lazy-create scenario)**

`bootstrapped-runway-rules-applied-to-optimus-inc-finance.md`:

```yaml
applies-to: [[../../Optimus Inc/finance/runway-rules]]
value-vector: [overhead, revenue]
expected-impact: large
```

The folder `Optimus Inc/finance/` did not exist before this bridge; `mkdir -p` creates it.

**Example 5: Bridge to tools-tracking (existing-but-empty folder)**

`langgraph-applied-to-tools-tracking.md`:

```yaml
applies-to: [[../tools-tracking/langgraph]]
value-vector: [productivity]
expected-impact: small
```

The folder `Optimus Academy/tools-tracking/` exists with `.gitkeep` but had no real files; this is the first population. After the bridge writes, the `.gitkeep` may optionally be deleted in the same commit.
