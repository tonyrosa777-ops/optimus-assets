---
title: Apply to Optimus
created: 2026-04-26
last-updated: 2026-04-26
tags: [#layer/optimus-os, #status/active]
---

# Apply to Optimus

This folder captures the moments when something learned in Optimus Academy can directly improve an Optimus offering. One file per insight. Each file explicitly names: the concept (link to the concept note in `[[../concepts/]]`), the source(s) where the concept was learned (links to source files in `[[../sources/]]`), the offering it improves (link to the offering hub), and how to apply it. This is where personal daily learning becomes business value.

## File naming convention

`<concept-slug>-applied-to-<offering-slug>.md`

Examples:

- `prompt-caching-applied-to-website-dev.md`
- `agentic-loops-applied-to-ai-voice.md`
- `multi-agent-orchestration-applied-to-ai-marketing.md`

One concept can apply to multiple offerings. When that happens, write multiple files — one per offering. Do not bundle. Each application has its own mechanism, its own implementation steps, and its own status to track.

## Frontmatter spec

```
---
title: <Concept> applied to <Offering>
concept: [[../concepts/<concept-slug>]]
source-files: [<YYYY-MM-DD-source-slug-1>, <YYYY-MM-DD-source-slug-2>]
offering: [[../../Offerings/<offering-path>/README]]
created: YYYY-MM-DD
last-updated: YYYY-MM-DD HH:MM
status: not-started
tags: [#learning/applied, #applies-to/<offering>]
---
```

The `source-files:` list grows over time. When a later source teaches more about the same concept and that new finding strengthens (or modifies) the application, the bridge note's `## Updates` section captures the delta and the new source slug joins this frontmatter list.

## Visible blockquote header

Right under the H1, every bridge note carries a visible attribution blockquote so the reader sees the full trail (concept → sources → offering → status) without peeking at YAML:

```
> **Concept:** [[../concepts/<concept-slug>]]
> **Source(s):**
> - [[../sources/YYYY-MM-DD-<source-slug-1>]] — <publisher>
> - [[../sources/YYYY-MM-DD-<source-slug-2>]] — <publisher>
> **Offering:** [[../../Offerings/<offering-folder>/README]]
> **Status:** `not-started`
> **Last updated:** YYYY-MM-DD HH:MM
```

## Body structure — rigid identical contract

Every bridge note follows the same five-section body. **All section headers are always present, in the same order, even when the section has no content.** Empty sections show literally `(none)` as the body. This is non-negotiable — predictability beats efficiency.

### `## What I learned`

Short summary of the concept with a wikilink to the concept note. Do not re-explain the concept here — the concept note is the source of truth. This section just establishes the hook.

### `## Why it applies to <offering>`

The concrete mechanism. Why does this concept improve this specific offering? What problem does it solve, what cost does it cut, what new capability does it unlock? Be specific. Vague answers ("better quality") are a sign the application isn't real yet.

### `## How to apply it`

Actionable steps. File paths to edit. Agent files to update. Workflow tweaks. Env vars to set. The reader should be able to execute this section without re-reading the concept note.

### `## Status`

One of: `not-started` / `in-progress` / `applied` / `verified`. Mirrored in frontmatter.

- `not-started` — bridge note exists, no implementation yet
- `in-progress` — implementation underway
- `applied` — shipped, working in production
- `verified` — measured and confirmed to deliver the predicted improvement

### `## Updates`

Empty on creation but the header is still present — it is the contract that signals "this is where future findings will land." When a new source adds to this insight, append a `### YYYY-MM-DD HH:MM — <label> — from [[../sources/<source-slug>]]` block here. Decisions made, blockers hit, results measured, new source findings — all stack chronologically. The original `## What I learned` / `## Why it applies` / `## How to apply it` content stays byte-identical from one update to the next; deltas live in `## Updates`.

## Promotion path

When a note here reaches `verified` status, consider promoting the pattern into the appropriate offering hub's `lessons/` folder OR (for website-dev) into `knowledge/patterns/` so it becomes a reusable asset across projects. The bridge note documents the discovery; the pattern doc documents the institutional rule.
