---
name: learn
description: Capture daily learning from any source (YouTube video, course, article, raw notes) into Optimus Academy. The daily file IS the comprehensive per-source capture; concept files are synthesized atomic distillations that grow over time as new sources teach more about the same topic. Every file follows a rigid identical contract with autonomy hooks (Dataview fields, schema-version, deterministic slugs, controlled vocab) baked in from day 1.
effort: medium
---

# /learn — Daily Learning Capture

## Usage

Run from inside `c:\Projects\Optimus Assets\` with the input attached or pasted:

```
/learn                          # input is whatever the user has pasted/attached in the conversation
/learn <YouTube URL>            # fetch transcript first, then process
/learn <topic hint>             # disambiguates ambiguous input
```

Every session produces three traces:

1. **Daily file** in `Optimus Academy/daily/YYYY-MM-DD.md` — comprehensive per-source capture. Created if doesn't exist; appended (new H2 section) if today's file already has prior captures.
2. **One concept file** in `Optimus Academy/concepts/<concept-slug>.md` per TOPIC the source touches — created OR updated via scan-and-decide.
3. **Zero or more bridge notes** in `Optimus Academy/apply-to-optimus/<concept-slug>-applied-to-<offering-slug>.md` when the topic has clear application to one of Optimus's four offerings.

**When to invoke:** Anytime new learning needs to land in the vault. ~90 minutes per day target. Cheaper to run /learn three times in a session than to batch a week into one capture.

## Role

You are a knowledge curator for Anthony's daily learning practice. Your job:

1. Read the input cleanly, extract source metadata, normalize the source URL.
2. Write the comprehensive per-source capture into today's daily file (always).
3. Identify the topic(s) the source touches; for each topic, scan-and-decide whether to APPEND to an existing concept or CREATE a new one. Default-to-APPEND when borderline.
4. When the topic has clear application to an Optimus offering, write or update a bridge note.
5. Apply the rigid identical structure contract to every file. Use `(none)` literally for sections that genuinely have no content. Bake in autonomy hooks (Dataview inline fields, schema-version, captured-by, review-by) per the templates below.
6. Tag everything per `00 — Empire Index/tag-schema.md`.
7. Commit + push immediately (per Anthony's standing preference).

## When to invoke

- Explicit `/learn` command after consuming any learning material
- Auto-suggested when the user pastes a transcript or summarizes a video without invoking /learn explicitly
- NOT for client-project learning (that goes to `knowledge/build-log.md` via `/retro` after the project closes)

## Required reading (in order)

1. `c:\Projects\Optimus Assets\00 — Empire Index\tag-schema.md` — canonical tag families, the controlled `domain:` vocabulary, the deterministic slug rule, the source URL canonical form rule
2. `c:\Projects\Optimus Assets\Optimus Academy\README.md` — hub conventions and folder model
3. `c:\Projects\Optimus Assets\Optimus Academy\apply-to-optimus\README.md` — bridge note format
4. The list of existing concept files in `c:\Projects\Optimus Assets\Optimus Academy\concepts\` (Glob)
5. The list of existing apply-to-optimus files in `c:\Projects\Optimus Assets\Optimus Academy\apply-to-optimus\` (Glob)
6. Today's daily file at `c:\Projects\Optimus Assets\Optimus Academy\daily\YYYY-MM-DD.md` (Read if exists)

Do NOT load the full content of every existing concept file — that's wasteful. Glob first, then read only candidates that match the topic on initial scan.

## Inputs

- The learning material (transcript, notes, URL, paste)
- Today's date in `YYYY-MM-DD` format
- Current time in `HH:MM` format (24-hour, local)
- Optional: explicit topic hint when the input is ambiguous

## The folder model — daily IS the source capture

The vault has THREE locations where /learn writes:

| Folder | What lives here | Mutation rule |
|---|---|---|
| `Optimus Academy/daily/` | One file per day. Multiple sources captured the same day → multiple H2 sections in one daily file. Each H2 section is the comprehensive capture for one source (full detail extraction). | New H2 sections append throughout the day; existing H2 sections never modified after creation. |
| `Optimus Academy/concepts/` | One file per topic. Synthesized atomic distillations. | Original definition stays stable at top. New findings from later sources append as `## Update — date — from [[daily/<date>#<anchor>]]` sections. |
| `Optimus Academy/apply-to-optimus/` | One file per (concept × offering) operational insight. | Same append behavior as concepts. |

**There is NO `sources/` folder.** The daily file IS the source capture. Source attribution lives prominently in each H2's inline Dataview fields + visible blockquote.

## Rigid identical structure — the contract

**Every file produced by /learn follows a rigid section structure for its file type. Section headers are always present, in the same order, even when the section has no content.** Empty sections show literally `(none)` as the body.

The reason: predictability beats efficiency. A reader scrolling through any daily file knows that code lives in `### Code & Examples`. They never have to scan to find it. They never wonder if a section was skipped because there was nothing to say or because the author got lazy. `(none)` means "I checked, and there genuinely was nothing for this section."

**When NOT to use `(none)`:** Don't use it to dodge work. If the source has 3 code examples, all 3 belong in `### Code & Examples`. If the source has zero code examples (a pure theory talk), then `(none)` is correct. The test: did you check, and was there genuinely nothing? Then `(none)`. Did you skip the section because it was a hassle? Then go back and fill it.

## Autonomy bake-ins — non-negotiable from day 1

Every file produced by /learn carries these autonomy hooks. The 1-2 year Optimus goal is full autonomy; retrofit cost on hundreds of historical files is painful. Bake them in now.

| Hook | Where | Why |
|---|---|---|
| `schema-version: 1` | YAML frontmatter on every /learn file | Future migrations can scan + upgrade by version number |
| Inline Dataview `key:: value` fields | Under each H2 source section in daily files | Per-source metadata queryable by Dataview without reading every file |
| Deterministic slugs | Source slugs (in daily H2 anchors), concept filenames, bridge filenames | Same input → same slug. Required for scan-and-decide. Rule in tag-schema.md. |
| Controlled `domain:` vocabulary | `domain:` in concept frontmatter, `domain::` inline in daily H2 fields | Free-text breaks "all concepts in X" queries on the first typo. List in tag-schema.md. |
| `captured-by: <human|agent:name>` | Inline in daily H2 fields | Future-proofs autonomous-vs-manual capture audits |
| `review-by: <YYYY-MM-DD>` (default created+6mo) | YAML frontmatter on every concept file | AI moves fast; nightly autonomous job can surface stale concepts |
| Canonical source URLs | `url::` inline in daily H2 fields, normalized per tag-schema.md | Same source captured twice produces same URL value → enables dedup-by-URL queries |

## Task

Produce three deliverables. Work them in order.

### Step 1 — Read input, extract metadata + topic candidates

Read the input fully. If it's a YouTube URL with no transcript provided, use WebFetch to get the transcript first.

Extract source metadata:
- **Source title** — the exact title of the video / article / course module / book chapter
- **Source type** — one of: `video`, `article`, `course`, `book`, `podcast`, `notes`
- **Publisher / author / channel** — who produced it (e.g. "Anthropic," "Julian Goldie SEO," "Andrej Karpathy," "personal note")
- **URL** — the link to the source. Normalize to canonical form per tag-schema.md (strip tracking params, force https, prefer `youtube.com/watch?v=X`, etc.). If no URL: use literal string `n/a`.
- **Source-date** — when the source was published (YYYY-MM-DD), or `unknown` if not stated
- **Duration** — runtime if it's a video/podcast (e.g. `32 min`), or `n/a`
- **Domain** — pick from the controlled vocabulary in tag-schema.md (`claude-api`, `agents`, `prompt-engineering`, `obsidian`, `evals`, `tooling`, `voice`, `marketing`, `web-dev`, `automation`, `business`). If no existing entry fits, propose adding to the vocab — don't silently invent.

Extract **candidate topics** (NOT atomic concepts yet):
- A topic is a named, reusable area of knowledge (e.g. "Obsidian + Claude integration," "prompt caching," "agentic loops"). Most sources touch 1-2 topics; a wide-ranging course module might touch 3.
- Sub-patterns of a single topic are NOT separate topics. ("Claude Code on a vault" is a sub-pattern of "Obsidian + Claude integration," not its own topic, until a future source teaches Claude Code applied to non-Obsidian contexts.)
- For each topic, note its applicability to Optimus offerings (Website Dev, AI Chat Assistant, AI Voice Receptionist, Marketing Team).

### Step 2 — Write the daily file capture

Path: `Optimus Academy/daily/YYYY-MM-DD.md`

**If today's file does NOT exist**, create it with this structure:

```markdown
---
date: YYYY-MM-DD
schema-version: 1
tags: [#learning/captured]
---

# YYYY-MM-DD — Daily Learning

[capture H2 sections go here — see template below]
```

**If today's file ALREADY exists**, append a new H2 capture section at the bottom (after any existing capture sections). Do NOT recreate the H1 or frontmatter.

**Per-source capture H2 template (rigid — apply identically every time):**

```markdown
## HH:MM — "Source Title" by Publisher

publisher:: Publisher Name
source-type:: video
url:: <canonical-url-or-n/a>
source-date:: <YYYY-MM-DD or unknown>
captured:: YYYY-MM-DD HH:MM
captured-by:: human
duration:: <duration or n/a>
domain:: <controlled-vocab-from-tag-schema>
concepts-touched:: [[../concepts/concept-slug-1]], [[../concepts/concept-slug-2]]
bridges-created:: [[../apply-to-optimus/bridge-slug]] | (none)

> **Source title:** "Source Title"
> **By:** Publisher Name
> **Type:** video
> **URL:** <canonical-url>
> **Captured:** YYYY-MM-DD HH:MM
> **Duration:** <duration>

### Summary
<2-3 sentence high-level summary for fast re-scan months later>

### Key Concepts Extracted
- [[../concepts/concept-slug-1]] — one-line description
- [[../concepts/concept-slug-2]] — one-line description

### Detailed Notes
<COMPREHENSIVE extraction. Pull every valuable detail. Use #### sub-headings to follow the source's natural structure (chapter markers, section breaks). Do NOT aggressively summarize — the goal is comprehensive capture so future-Anthony can re-read this section instead of re-watching the video.>

#### <Sub-topic 1 from the source>
<Detail. Multiple paragraphs ok. Quote specific numbers, claims, mechanics.>

#### <Sub-topic 2>
<Detail.>

### Code & Examples
<Code blocks with language tags, prompt examples, configs, screenshots described in words. If none: `(none)`>

### Notable Quotes
<Verbatim memorable lines. Format: `> "quote" — speaker, timestamp if known`. If none: `(none)`>

### Action Items
<Concrete things to try, build, or change as a result. One bullet per item. If none: `(none)`>

### Open Questions
<Things this raised that weren't answered. Research backlog. If none: `(none)`>
```

If multiple sources are captured the same day, separate them with a horizontal rule (`---`) between H2 sections. The visible blockquote at the top of each H2 section is the source-attribution contract — readers see attribution the moment they scroll to that capture.

**Inline Dataview fields (the `key:: value` block) are mandatory.** The visible blockquote is for humans; the inline fields are for Dataview. Both, no either/or.

### Step 3 — Topic-recognition + concept scan-and-decide

For each candidate topic identified in Step 1:

**Scan procedure:**
1. Use `Glob` on `Optimus Academy/concepts/*.md` to list filenames. Slugify the topic name per the deterministic slug rule (tag-schema.md) and check for direct filename hits or near-misses.
2. Use `Grep` on `Optimus Academy/concepts/` for keyword overlap (the topic's distinctive terms — not generic words like "Claude" or "agent").
3. Read the top 3 candidate files in full (frontmatter + body + Updates).
4. Decide using this matrix:

| Confidence | Decision | Action |
|---|---|---|
| **High match** (same topic, same domain, candidate is a clear superset/subset) | APPEND | Add a `## Update` section to the existing concept file. See append details below. |
| **Weak/no match** | CREATE | Write a new concept file using the rigid concept structure. See create details below. |
| **Borderline** (related but might be its own topic) | ASK | Stop and ask the user: "This looks related to `[[<existing-concept-slug>]]` — append there or create new?" Default suggestion: APPEND. |

**The default flips toward APPEND.** False-merge (folding new info into an adjacent concept) is recoverable later by splitting. False-fragmentation (creating a new concept file when an existing one would have absorbed the topic) accumulates and degrades the synthesis layer faster. Sub-patterns of an existing topic stay as sub-headings inside that concept's `## Mechanics`, NOT as separate concept files.

#### CREATE path — new concept file

Path: `Optimus Academy/concepts/<concept-slug>.md`

```markdown
---
title: <Concept Name>
schema-version: 1
domain: <controlled-vocab-from-tag-schema>
created: YYYY-MM-DD
last-updated: YYYY-MM-DD HH:MM
review-by: <YYYY-MM-DD ~6 months ahead>
source-references: ["[[../daily/YYYY-MM-DD#HH:MM — \"Source Title\" by Publisher]]"]
tags: [#learning/synthesized, #applies-to/<offering-or-all>]
---

# <Concept Name>

> **Concept distilled from:**
> - [[../daily/YYYY-MM-DD#HH:MM — "Source Title" by Publisher]] — Publisher
>
> **Last updated:** YYYY-MM-DD HH:MM

## What it is
<1-2 sentence definition. Stable. Doesn't change when new sources arrive.>

## When to use
<Concrete situations where this matters. Bullet list ok.>

## Mechanics
<How it actually works — the meat. ### sub-headings allowed for sub-patterns.>

## Examples
<Code, prompts, scenarios. If none: `(none)`>

## Gotchas
<Failure modes, edge cases, common mistakes. If none: `(none)`>

## Related Concepts
<Wikilinks to related concept files. If none: `(none)`>

## Updates
<Empty on creation. Future updates from later sources land here.>
```

**Section headers mandatory:** What it is / When to use / Mechanics / Examples / Gotchas / Related Concepts / Updates. The `## Updates` section is empty on creation but the header is still there — it signals "this is where future findings will land."

**`review-by:` is created date + ~6 months.** AI moves fast; concepts written today might be stale in 6 months. The autonomous nightly stale-knowledge job (planned) will scan for concepts past their review-by date.

**`source-references:` uses daily-anchor wikilinks** — `[[../daily/YYYY-MM-DD#HH:MM — "Source Title" by Publisher]]`. The anchor text is the H2 heading text from the daily file (Obsidian resolves `[[file#heading]]` natively). Use this format for both the YAML field AND the visible blockquote at the top of body.

#### APPEND path — existing concept file

1. Read the existing file in full.
2. Bump frontmatter `last-updated` to `YYYY-MM-DD HH:MM`.
3. Append the new daily-anchor wikilink to frontmatter `source-references:` list.
4. Add a new wikilink line to the visible blockquote at top of body:
   ```
   > - [[../daily/YYYY-MM-DD#HH:MM — "Source Title" by Publisher]] — Publisher
   ```
5. Append a new block under the existing `## Updates` section:
   ```markdown
   ### YYYY-MM-DD HH:MM — <short label> — from [[../daily/YYYY-MM-DD#HH:MM — "Source Title" by Publisher]]
   <What this new source added beyond the original definition. Specific. Cite which `#### sub-topic` of the daily section if applicable. Don't restate what the daily capture already covers — just the *delta* this source brings to the concept.>
   ```
6. Do NOT modify any of: `## What it is`, `## When to use`, `## Mechanics`, `## Examples`, `## Gotchas`, `## Related Concepts` body content. The top stays stable; new findings live only in `## Updates`.
7. Optionally bump `review-by:` to a fresh ~6-months-out date if this update materially refreshes the concept. Otherwise leave it alone.

### Step 4 — Apply-to-Optimus bridge note(s) (when applicable)

Only create a bridge note when the topic has a clear, concrete application to one of the four Optimus offerings. Pure theory or "interesting but not actionable" content does NOT get a bridge note — skip this step in that case.

If the topic applies to multiple offerings, create multiple bridge notes (one per offering).

Run the same scan-and-decide on `Optimus Academy/apply-to-optimus/*.md` first — if a bridge for this concept+offering pair already exists, APPEND a `## Update` section instead of duplicating.

#### CREATE path — new bridge

Path: `Optimus Academy/apply-to-optimus/<concept-slug>-applied-to-<offering-slug>.md`

Offering slugs: `website-dev`, `ai-chat`, `ai-voice`, `ai-marketing`, or `all-agents` (when it applies to chat + voice + marketing simultaneously).

```markdown
---
title: <Concept Name> applied to <Offering Name>
schema-version: 1
concept: [[../concepts/<concept-slug>]]
source-references: ["[[../daily/YYYY-MM-DD#HH:MM — \"Source Title\" by Publisher]]"]
offering: [[../../Offerings/<offering-folder>/README]]
created: YYYY-MM-DD
last-updated: YYYY-MM-DD HH:MM
status: not-started
tags: [#learning/applied, #applies-to/<offering-tag>]
---

# <Concept Name> applied to <Offering Name>

> **Concept:** [[../concepts/<concept-slug>]]
> **Source(s):**
> - [[../daily/YYYY-MM-DD#HH:MM — "Source Title" by Publisher]] — Publisher
> **Offering:** [[../../Offerings/<offering-folder>/README]]
> **Status:** `not-started`
> **Last updated:** YYYY-MM-DD HH:MM

## What I learned
<1-2 sentence summary with link to the concept note>

## Why it applies to <offering>
<Concrete mechanism — what about the offering today benefits>

## How to apply it
<Actionable steps. File paths if known. Agent changes. Workflow tweaks. Commit-level granularity is great.>

## Status
`not-started`

## Updates
<Empty on creation. Future updates from later sources land here.>
```

**Section headers mandatory:** What I learned / Why it applies / How to apply it / Status / Updates.

#### APPEND path — existing bridge

Same pattern as concept-append: bump `last-updated`, add to `source-references:` list, add wikilink to visible blockquote, append a `### YYYY-MM-DD HH:MM — <label> — from [[<daily-anchor>]]` block under `## Updates`. Don't touch the original `## What I learned` / `## Why it applies` / `## How to apply it` / `## Status` content.

### Step 5 — Update cross-references

After all concept and bridge files are written/updated:

1. **Update the daily H2 section's `concepts-touched::` inline field** with the resolved concept wikilinks (whether they were created or updated).
2. **Update the daily H2 section's `bridges-created::` inline field** with the bridge wikilinks (or `(none)` if no bridge was created).
3. **Verify each touched concept file's `source-references:` frontmatter** includes the new daily-anchor wikilink.
4. **Verify each touched bridge file's `source-references:` frontmatter** includes the new daily-anchor wikilink.

Bidirectional linking is the load-bearing invariant — every source knows what concepts it touched; every concept knows what daily captures fed it.

### Step 6 — Tag application audit

Before committing, verify every file you touched has the right tags from the schema:

- Daily files (file-level YAML): `#learning/captured`
- Concept files: `#learning/synthesized` + `#applies-to/<offering-or-all>`
- Bridge files: `#learning/applied` + `#applies-to/<offering-tag>`

Tags live in YAML frontmatter arrays only, never as floating inline `#tags` in body text. If a concept is theory-only (no Optimus application), use `#applies-to/all` or omit the applies-to tag entirely. Don't fake an application that isn't there.

### Step 7 — Commit + push

Stage all created/modified files. Commit message format:

```
learn(<domain>): <one-line summary of what was captured>

- Source: [[YYYY-MM-DD#HH:MM — "Source Title" by Publisher]] (in daily file)
- Concepts: <slug-1> (created|updated), <slug-2> (created|updated)
- Bridges: <offering-1>[, <offering-2>] | none
```

Example:
```
learn(obsidian): Obsidian + Claude integration patterns

- Source: [[2026-04-26#11:36 — "Claude Obsidian is INSANE!" by Julian Goldie SEO]]
- Concepts: obsidian-claude-integration (created)
- Bridges: ai-marketing (Obsidian + Claude as content engine substrate)
```

Then `git push`.

## Decisions and judgment calls

**When to skip the apply-to-optimus bridge:** Pure theoretical content (research papers, conceptual frameworks without immediate operational use), historical context (how the field evolved), or content that's interesting but doesn't change how Optimus delivers any of its 4 offerings today. The bridge folder should stay valuable — every file there is a real "I should change something" insight. Bloating it with weak bridges defeats the purpose.

**When to ask before deciding (concept scan):** Whenever the scan returns a candidate file with > 50% topic overlap but < 90% — that borderline zone is where the user's judgment beats yours. Ask. Default suggestion: APPEND to existing.

**When to create multiple concept files from one source:** When the source genuinely teaches 2-3 distinct, INDEPENDENT topics — not when it covers one topic with many sub-patterns. A 30-min YouTube video on "5 things about agentic loops" surfaces ONE topic (the agentic loop pattern). A 90-min Anthropic course module on "Building production agents" might genuinely surface 2-3 distinct topics (agentic loops + tool routing + eval design). Be ruthless. Sub-patterns live as `### sub-headings` under the parent concept's `## Mechanics`, not as separate files.

**When the input is sparse:** If raw notes are only a few paragraphs, the daily section's `### Detailed Notes` will be brief — that's fine. The structure contract requires the section *exists*; it does not require minimum content length. `(none)` for genuinely empty sections is correct.

**When to leave the `### Summary` brief:** The summary is a fast-rescan device. 2-3 sentences. If you find yourself writing a paragraph in the summary, you're putting content in the wrong section — move it to `### Detailed Notes`.

## Validation before reporting done

Before committing, validate every file you wrote:

**Daily file (today's `YYYY-MM-DD.md`) checklist:**
- File-level YAML frontmatter has `date:`, `schema-version: 1`, `tags: [#learning/captured]`
- One H2 section per source captured today
- For each H2 section:
  - Inline Dataview fields (publisher, source-type, url, source-date, captured, captured-by, duration, domain, concepts-touched, bridges-created) all present
  - Visible blockquote with source attribution (Source title, By, Type, URL, Captured, Duration) present
  - All 7 H3 sections present in order: Summary / Key Concepts Extracted / Detailed Notes / Code & Examples / Notable Quotes / Action Items / Open Questions
  - Empty H3 sections show `(none)`, not omitted

**Concept file checklist (CREATE):**
- Frontmatter has all 8 fields (title, schema-version, domain, created, last-updated, review-by, source-references, tags)
- `domain:` value is from the controlled vocab in tag-schema.md
- `review-by:` is created date + ~6 months
- Visible blockquote at top has source distillation list + last updated
- All 7 body sections present in order: What it is / When to use / Mechanics / Examples / Gotchas / Related Concepts / Updates
- `## Updates` section is empty on creation but the header is present

**Concept file checklist (APPEND):**
- Frontmatter `last-updated` bumped
- Frontmatter `source-references:` list grew (now includes new daily-anchor)
- Visible blockquote at top got a new line for the new daily-anchor source
- New `### YYYY-MM-DD HH:MM — <label> — from [[<daily-anchor>]]` block exists under `## Updates`
- Original `## What it is` / `## When to use` / `## Mechanics` / `## Examples` / `## Gotchas` body content is BYTE-IDENTICAL to before

**Bridge file checklist:** Same pattern as concept (CREATE: 5 sections + Updates; APPEND: bump + append-only).

**Cross-reference checklist:**
- Daily H2 section's `concepts-touched::` inline field matches the concepts touched
- Each touched concept file's `source-references:` includes the new daily-anchor
- Each touched bridge file's `source-references:` includes the new daily-anchor

**Slug determinism check:** Source slug used in the daily H2 anchor matches the deterministic rule from tag-schema.md. Concept and bridge filenames follow the same rule.

**URL canonicalization check:** The `url::` value matches the canonical form from tag-schema.md (no tracking params, normalized YouTube format, etc.).

**Git checklist:**
- `git status` shows the expected files staged + nothing unintended
- `git log -1` confirms the commit landed
- `git push` succeeded

Then report: source captured (with daily-anchor), topics touched (with create/append/ask resolution), bridges created (or none), and the commit hash.
