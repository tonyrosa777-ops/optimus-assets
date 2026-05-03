---
title: Apply to Optimus
created: 2026-04-26
last-updated: 2026-05-03
tags: [#layer/optimus-os, #status/active]
---

# Apply to Optimus

This folder captures the moments when something learned in Optimus Academy can directly improve an Optimus system, agent, craft, or operations area. **One file per concept** — multiple applications of the same concept live as separate H2 sections inside that one file (mirroring how the daily folder has multiple H2 source-capture sections inside one date-keyed file). Each H2 section explicitly names: the concept (link to the concept note in `[[../concepts/]]`), the source(s) where the concept was learned (daily-anchor wikilinks), the target file/area the application addresses, **the value vector(s) it serves** (productivity / overhead / revenue), and how to apply it. This is where personal daily learning becomes business value.

## File model — daily-mirror, one file per concept

The `apply-to-optimus/` folder mirrors the `daily/` folder's structure exactly:

| Folder | Filename pattern | What lives inside the file |
|---|---|---|
| `daily/` | `YYYY-MM-DD.md` (one file per day) | Multiple H2 source-capture sections, each with full per-source metadata + 7 sub-sections |
| `apply-to-optimus/` | `<concept-slug>.md` (one file per concept) | Multiple H2 application sections, each with full per-application metadata + 6 sub-sections |

**Filename:** just the concept slug. No `-applied-to-<target>` suffix. Same rule as `daily/` (no per-source suffix on filenames). Examples:

- `obsidian-claude-integration.md`
- `gtm-engineering.md`
- `openclaw-multi-agent-orchestration.md`
- `bootstrapped-runway-rules.md`
- `langgraph.md`

**Inside the file:** one `## Applied to <Target Display Name>` H2 section per application. A concept that applies in three places gets one bridge file with three H2 sections. The H2 anchor (e.g., `[[gtm-engineering#Applied to Marketing Team (Tier-3) offering]]`) is the wikilink target for cross-references.

## Five bridge target zones — not just offerings

Bridge `applies-to::` targets (declared at the H2 inline-field level) route to one of five zones depending on where the knowledge would actually integrate. The bridge layer is intentionally broader than the four AI offerings — sales-training feeds copy craft, finance content feeds Optimus Inc operations, marketing psychology feeds CRO, tool reviews feed the internal stack.

| Zone | Folder | When it applies | Folder existence |
|---|---|---|---|
| `Offerings/<offering>/` | Existing offering hub | Concept changes how a productized offering is built or operated | All exist |
| `knowledge/patterns/` | Cross-website-build patterns | Pattern that any client site could reuse | Exists, populated |
| `knowledge/craft/<area>/` | `copywriting`, `psychology`, `sales`, `design` | Cross-cutting craft principle that shapes copy/visuals/sales motion across all builds | Lazy-create on first use |
| `Optimus Inc/<area>/` | `finance`, `operations`, `brand`, `website`, `market-intelligence`, `social-pipeline`, `ai-agents/<tier>/` | Concerns Optimus the company itself, not the offerings | Some exist (`brand`, `website`, `market-intelligence`, `social-pipeline`, `ai-agents/<tier>/`); `finance` and `operations` lazy-create per-area |
| `Optimus Academy/tools-tracking/<tool-slug>.md` | Flat file per tool | Evaluating whether to adopt a tool into Optimus's stack | Folder exists with a real entry; populates per-tool |

A single concept may produce multiple application H2 sections — one per applicable zone — inside the SAME bridge file. The H2 schema (applies-to, status, value-vector, expected-impact, what-i-learned, why-it-applies, how-to-apply, value-vector-reasoning, status, updates) is identical across all five zones.

## Multi-purpose principle — every application H2 declares a business outcome

**Bridge files are the ONLY place Optimus-relationship framing belongs.** Concept files in `concepts/` stay subject-pure — they teach the topic itself, no "we don't adopt this" or "Tier-3/Tier-4 should mirror this." All Optimus-relationship reasoning (where to apply, why it works for Optimus, value-vector mechanics) lives here in the bridge's per-application H2 sections. See `learn-prompt.md` → CREATE path for the full Concept body discipline rules.

Every application H2 MUST declare at least one `value-vector` from `productivity` / `overhead` / `revenue` with concrete reasoning. Multi-valued by default — most applications serve 2-3 vectors simultaneously.

| Vector | What it means | Examples |
|---|---|---|
| `productivity` | Speed/quality of building, shipping, or operating | New animation pattern that cuts hero-build time 30% • Better critic prompt that improves first-pass quality • SEO checklist that prevents post-launch rework |
| `overhead` | Reduces manual work, context-switching, duplication, error rates | Folder-creation policy that prevents empty-folder noise • Skill that auto-generates boilerplate • Pattern that prevents a recurring error from build-log.md |
| `revenue` | Pricing, conversion, retention, offerings, or new tiers | New pricing-page tactic from a sales source • CRO heuristic that lifts quiz-to-booking conversion • Better cold-email sequence |

**No-application stop conditions:** if `/learn` cannot identify (a) a clear target file in the vault that would meaningfully integrate the knowledge AND (b) at least one value vector with concrete reasoning, it does NOT add an application H2 — concept note only. Vague applications pollute the weekly review and dilute the prioritization layer.

## File-level frontmatter spec

The file-level YAML stays minimal — it's the unifying key (concept link, aggregated source-references, aggregated tags). All per-application metadata lives in inline Dataview fields under each H2 section.

```yaml
---
title: <Concept Name> — apply-to-Optimus bridges
schema-version: 1
concept: [[../concepts/<concept-slug>]]
source-references: ["[[../daily/YYYY-MM-DD#HH:MM — \"Source Title\" by Publisher]]"]
created: <earliest application's created date>
last-updated: <most recent application's last-updated>
tags: [#learning/applied, <#applies-to/zone-1>, <#applies-to/zone-2>, ..., #status/active]
---
```

When a new source teaches more about the concept, the same `source-references:` list grows (additive). When a new application is added, `tags:` gain the new application's `#applies-to/<zone>` tag if not already present. `last-updated:` always reflects the most recent change to any application H2 in the file.

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

## Visible blockquote header (file-level)

Right under the H1 the file carries a visible attribution blockquote naming the concept and aggregated sources:

```
> **Concept:** [[../concepts/<concept-slug>]]
> **Source(s):**
> - [[../daily/YYYY-MM-DD#HH:MM — "Source Title" by Publisher]] — <publisher>
> - [[../daily/<later-date>#HH:MM — "Other Source Title" by Other Publisher]] — <publisher>
>
> **Last updated:** YYYY-MM-DD HH:MM
```

Source references use **daily-anchor wikilinks** — `[[../daily/YYYY-MM-DD#<H2 heading text>]]`. The anchor text is the H2 heading from the daily file (Obsidian resolves `[[file#heading]]` natively). This points at the actual H2 capture section inside the daily file, not at a separate source file.

## Per-application H2 section — rigid identical contract

Each `## Applied to <Target>` H2 section follows the same structure. **All six sub-sections are always present, in the same order, even when the section has no content.** Empty sub-sections show literally `(none)` as the body. This is non-negotiable — predictability beats efficiency.

```markdown
## Applied to <Target Display Name>

applies-to:: [[<wikilink-to-target-file>]]
status:: not-started
value-vector:: revenue, productivity
expected-impact:: medium
created:: YYYY-MM-DD
last-updated:: YYYY-MM-DD HH:MM

> **Applies to:** [[<wikilink-to-target-file>]]
> **Status:** `not-started`
> **Value vector(s):** revenue, productivity
> **Expected impact:** medium
> **Last updated:** YYYY-MM-DD HH:MM

### What I learned
<short summary of the concept with a wikilink to the concept note. Hook only — concept note is source of truth.>

### Why it applies to <target>
<concrete mechanism — what about the target benefits from absorbing this concept>

### How to apply it
<actionable steps. file paths. agent prompt edits. workflow tweaks. The bridge is a change-request, not a change — Anthony reviews and applies edits manually.>

### Value vector reasoning
<one sentence per value-vector — concrete mechanism>

### Status
`not-started`

### Updates
<empty on creation, but the header is always present>
```

**Inline Dataview fields under each H2 are mandatory.** The visible blockquote is for humans; the inline fields make per-application metadata queryable in Dataview. Both, no either/or.

**The H2 anchor itself is load-bearing.** Cross-references from concept files, daily files, or other bridges point at specific applications via `[[<concept-slug>#Applied to <Target Display Name>]]`. Choose Target Display Names that are stable and human-readable — they become permanent anchors.

### Sub-section meanings

- `### What I learned` — short summary of the concept with a wikilink to the concept note. Hook only; the concept is the source of truth.
- `### Why it applies to <target>` — concrete mechanism. Why does this concept improve this specific target file or area? What problem does it solve, what cost does it cut, what new capability does it unlock? Be specific. Vague answers ("better quality") are a sign the application isn't real yet.
- `### How to apply it` — actionable steps. File paths to edit. Agent files to update. Workflow tweaks. Env vars to set. The reader should be able to execute this section without re-reading the concept note. **Important:** bridges to agent files do NOT auto-edit the agent. The bridge is the change-request; Anthony reviews and applies the change manually (per the LEDGER rule — human review of agent edits is mandatory).
- `### Value vector reasoning` — for each vector tagged in `value-vector::`, one sentence on the concrete mechanism. This is what gets reviewed weekly to prioritize applications by leverage.
- `### Status` — one of: `not-started` / `in-progress` / `applied` / `verified`. Mirrored in the inline `status::` field.
  - `not-started` — application captured, no implementation yet
  - `in-progress` — implementation underway
  - `applied` — shipped, working in production
  - `verified` — measured and confirmed to deliver the predicted improvement
- `### Updates` — empty on creation but the header is still present — it is the contract that signals "this is where future findings will land." When a new source adds to this application, append a `#### YYYY-MM-DD HH:MM — <label> — from [[../daily/<date>#<anchor>]]` block here. Decisions made, blockers hit, results measured, new source findings — all stack chronologically. The original `### What I learned` / `### Why it applies` / `### How to apply it` content stays byte-identical from one update to the next; deltas live in `### Updates`.

## Adding a new application to an existing bridge file

When `/learn` identifies a new application of a concept that already has a bridge file, the new H2 section appends to that file (it does NOT create a new bridge file). Procedure:

1. Read the existing bridge file in full.
2. Append a new `## Applied to <New Target Display Name>` H2 section at the bottom (after a `---` separator).
3. Bump file-level `last-updated:` to the new application's timestamp.
4. Add the new application's `#applies-to/<zone>` tag to file-level `tags:` if not already present.
5. If the new source-reference is not already in file-level `source-references:`, add it (additive — never remove old sources).

## Adding a new source to an existing application

When the same source teaches more about an existing concept-application pair (e.g., a follow-up YouTube video adds a new gotcha to an already-bridged application):

1. Read the existing application H2 in full.
2. Bump that H2's inline `last-updated::` to the new timestamp.
3. **Information-delta check:** does the new source add anything beyond what the H2 already says in `### What I learned` / `### Why it applies` / `### How to apply it` / `### Value vector reasoning` and prior `### Updates`? Variations always pass; identical/near-verbatim repetition is blocked.
4. If delta exists, append a `#### YYYY-MM-DD HH:MM — <label> — from [[<daily-anchor>]]` block under that H2's `### Updates` sub-section.
5. **Value-vector merge rule:** if the new source reveals an additional value vector not on the existing H2, ADD it to that H2's inline `value-vector::` (e.g., `[productivity]` → `[productivity, revenue]`). Never remove existing vectors during APPEND.
6. Don't touch the original body content of `### What I learned` / `### Why it applies` / `### How to apply it` / `### Value vector reasoning` / `### Status`.
7. Bump file-level `last-updated:` and append the new daily-anchor to file-level `source-references:` if not already present.

## Promotion path

When an application H2 reaches `verified` status, consider promoting the pattern into the appropriate institutional location so it becomes a reusable asset across projects:

- Application target was `Offerings/<offering>/...` → promote to `Offerings/<offering>/lessons/<slug>.md`
- Application target was a `.claude/agents/<area>/<agent>.md` file → the agent edits already happened during APPLY; promote to `knowledge/patterns/<slug>.md` if the underlying pattern is broader than the agent
- Application target was `knowledge/craft/<area>/<slug>.md` → already in the institutional location; mark `verified` and move on
- Application target was `Optimus Inc/<area>/<slug>.md` → promote internally if relevant; this is the canonical location for Optimus's own ops
- Application target was `tools-tracking/<tool>.md` → if the tool was adopted, promote the adoption pattern to `Offerings/02 AI Agents/shared-knowledge/lessons/<slug>.md` or wherever it's used

The application H2 documents the discovery; the pattern doc documents the institutional rule. Promotion is manual (no autopilot) — Anthony reviews each `verified` application and decides whether the underlying pattern earned institutional status.

## Worked examples

**Example 1 — Concept with one application** (simplest case): `obsidian-claude-integration.md`. One H2 section: `## Applied to AI Marketing Team (Tier-3)`. File-level `tags: [#learning/applied, #applies-to/ai-agents/marketing, #status/active]`.

**Example 2 — Concept with two applications**: `gtm-engineering.md`. Two H2 sections: `## Applied to Marketing Team (Tier-3) offering` and `## Applied to Optimus Inc's own outbound pipeline`. File-level `tags: [#learning/applied, #applies-to/ai-agents/marketing, #applies-to/optimus-inc/marketing, #status/active]`. The two H2s share the same source-reference (one TikTok taught both) but each has distinct `applies-to::`, `value-vector::`, and reasoning.

**Example 3 — Concept with two zones (offering + tools-tracking)**: `openclaw-multi-agent-orchestration.md`. Two H2 sections: `## Applied to tools-tracking` and `## Applied to AI Agents — Marketing Team (Tier-3)`. File-level `tags: [#learning/applied, #applies-to/tools/openclaw, #applies-to/ai-agents/marketing, #status/active]`.

**Example 4 — Lazy-created folder target**: `bootstrapped-runway-rules.md` with `## Applied to Optimus Inc finance` H2, `applies-to:: [[../../Optimus Inc/finance/runway-rules]]`. The folder `Optimus Inc/finance/` did not exist before this bridge; `mkdir -p` creates it.

**Example 5 — Tools-tracking target**: `langgraph.md` with `## Applied to tools-tracking` H2, `applies-to:: [[../tools-tracking/langgraph]]`. The folder `Optimus Academy/tools-tracking/` exists; this is the first population for the langgraph tool.
