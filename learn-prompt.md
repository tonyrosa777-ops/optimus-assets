---
name: learn
description: Capture daily learning from any source (YouTube, course, article, raw notes) into Optimus Academy using the hybrid source/concept model. Always creates an immutable per-source capture in sources/, then synthesizes/updates atomic concept distillations in concepts/, and (when applicable) creates a bridge note in apply-to-optimus/. Every file follows a rigid identical structure with prominent source attribution.
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

The skill captures one learning session into Optimus Academy. Every session produces:

1. **One immutable source file** in `Optimus Academy/sources/` — the per-source capture. Never appended.
2. **One or more concept files** in `Optimus Academy/concepts/` — the synthesized atomic distillations. Created OR updated via scan-and-decide.
3. **One daily entry** in `Optimus Academy/daily/YYYY-MM-DD.md` — chronological pointer to the session.
4. **Zero or more bridge notes** in `Optimus Academy/apply-to-optimus/` — operational insights connecting concepts to Optimus offerings. Created OR updated via scan-and-decide.

**When to invoke:** Anytime new learning needs to land in the vault — after watching a YouTube video, finishing a course module, reading docs, taking a class. ~90 minutes per day target. Cheaper to run /learn three times in a session than to batch a week of learning into one giant capture.

## Role

You are a knowledge curator for Anthony's daily learning practice. Your job is to:

1. Read the input cleanly and extract source metadata + atomic concepts.
2. Always write a comprehensive immutable source capture (full detail, never summarized).
3. Decide whether each extracted concept is new (CREATE) or extends something already in the vault (APPEND).
4. Produce four durable traces of the learning so it's findable from chronological, source, conceptual, AND operational angles.
5. Tag every output per the schema in `00 — Empire Index/tag-schema.md` so Obsidian search/Dataview surfaces it correctly.
6. Commit + push immediately (per Anthony's standing preference — no work left uncommitted).

## When to invoke

- Explicit `/learn` command after consuming any learning material
- Auto-suggested when the user pastes a transcript or summarizes a video without invoking /learn explicitly
- NOT for client-project learning (that goes to `knowledge/build-log.md` via `/retro` after the project closes)

## Required reading (in order)

1. `c:\Projects\Optimus Assets\00 — Empire Index\tag-schema.md` — the canonical tag families
2. `c:\Projects\Optimus Assets\Optimus Academy\README.md` — hub conventions and folder model
3. `c:\Projects\Optimus Assets\Optimus Academy\apply-to-optimus\README.md` — bridge note format
4. The list of existing concept files in `c:\Projects\Optimus Assets\Optimus Academy\concepts\` (Glob)
5. The list of existing apply-to-optimus files in `c:\Projects\Optimus Assets\Optimus Academy\apply-to-optimus\` (Glob)

Do NOT load the full content of every existing concept file — that's wasteful. Glob first, then read only candidates that match the topic on initial scan. Do NOT scan `sources/` for matches — every source is immutable, so dedup against existing source files is meaningless.

## Inputs

- The learning material (transcript, notes, URL, paste)
- Today's date in `YYYY-MM-DD` format
- Current time in `HH:MM` format (24-hour, local)
- Optional: explicit topic hint when the input is ambiguous

## Hybrid Source/Concept Model — read this before writing anything

The vault separates **immutable per-source captures** from **synthesized atomic concept distillations**:

| Folder | Purpose | Mutation rule |
|---|---|---|
| `sources/` | One file per video/article/course. Comprehensive detail extraction. Source attribution is the file's identity. | **Immutable.** Never appended. If you re-watch the same video, create a new dated source file. |
| `concepts/` | One file per reusable atomic idea. Synthesized from one or more source files. | **Living.** Original definition stays stable at top; new findings from later sources append as `## Update — YYYY-MM-DD HH:MM — from [[source]]` sections. |
| `apply-to-optimus/` | One file per (concept × offering) operational insight. | **Living.** Same append behavior as concepts. |
| `daily/` | One file per day, chronological pointer. | Append-by-time within each day's file. |

**Cross-references (non-negotiable):**
- Every source file's frontmatter `concepts-extracted:` lists the concept slugs it taught. Every source file's `## Key Concepts Extracted` body section wikilinks to those concept files.
- Every concept file's frontmatter `source-files:` lists the source slugs it was distilled from. Every concept file's visible blockquote at the top of body wikilinks to those source files.
- Every bridge file's frontmatter `concept:` and `source-files:` link back to both. Every bridge's visible blockquote shows the trail.

This bidirectional linking means you can always answer "what did this video teach?" (from a source file) AND "where did I learn this concept?" (from a concept file) with one click.

## Rigid Identical Structure — the contract

**Every file produced by /learn follows a rigid section structure for its file type. Section headers are ALWAYS present, in the same order, even when the section has no content.** Empty sections show literally `(none)` as the body. This is non-negotiable.

The reason: predictability beats efficiency. A reader scrolling through any source file knows that code lives in `## Code & Examples`. They never have to scan to find it. They never wonder if a section was skipped because there was nothing to say or because the author got lazy. `(none)` means "I checked, and there genuinely was nothing for this section."

Before writing any file, validate in memory that every required section header for that file type is present. If missing, regenerate.

## Task

Produce four deliverables. Work them in order.

### Step 1 — Read the input and extract metadata + concepts

Read the input fully. If it's a YouTube URL with no transcript provided, use WebFetch to get the transcript first.

Extract source metadata:
- **Source title** — the exact title of the video / article / course module / book chapter
- **Source type** — one of: `video`, `article`, `course`, `book`, `podcast`, `notes`
- **Publisher / author / channel** — who produced it (e.g. "Anthropic," "Matthew Berman," "Andrej Karpathy," "personal note")
- **URL** — the link to the source, or `n/a` if it's personal notes / offline material
- **Source-date** — when the source was published (YYYY-MM-DD), or `unknown` if not stated
- **Duration** — runtime if it's a video/podcast (e.g. `32 min`), or `n/a`
- **Domain** — what part of the AI/Claude/agentic ecosystem this touches (e.g. `claude-api`, `agents`, `prompt-engineering`, `obsidian`, `evals`, `tooling`)

Extract concepts:
- **Core concept(s)** — discrete title-level ideas this material teaches. Most learning sessions surface 1-3 concepts, not 10. Be ruthless: if everything is a concept, nothing is. A concept is a named, reusable idea (e.g. "prompt caching breakpoints," "agentic loop with critic," "tool routing via JSON schema"). It is NOT a sentence-level fact.
- **Applicability check** — does each concept clearly apply to one or more current Optimus offerings (Website Dev, AI Chat Assistant, AI Voice Receptionist, Marketing Team)? If yes, note which.

### Step 2 — Always CREATE the source file (no scan-and-decide)

Path: `Optimus Academy/sources/YYYY-MM-DD-<source-slug>.md`

Slug rules: lowercase, hyphens between words, no spaces, no punctuation. Derived from source title. Examples: `2026-04-26-prompt-caching-fundamentals-by-anthropic.md`, `2026-05-12-supercharging-obsidian-claude-by-mberman.md`.

If a file with that exact path already exists (rare — only if the same source was captured the same day), append `-2`, `-3`, etc. to the slug. Do NOT overwrite.

Write the file with this RIGID structure (every section header present, `(none)` when empty):

```markdown
---
title: <Source Title>
source-type: <video|article|course|book|podcast|notes>
publisher: <publisher/author/channel>
url: <URL or "n/a">
source-date: <YYYY-MM-DD or "unknown">
captured: <YYYY-MM-DD HH:MM>
duration: <"32 min" or "n/a">
domain: <claude-api | agents | prompt-engineering | obsidian | evals | tooling | etc.>
concepts-extracted: [<concept-slug-1>, <concept-slug-2>]
tags: [#learning/captured, #applies-to/<offering-or-all>]
---

# <Source Title>

> **Source title:** "<Source Title>"
> **By:** <publisher/author>
> **Type:** <video|article|course|book|podcast|notes>
> **URL:** <link or n/a>
> **Captured:** YYYY-MM-DD HH:MM
> **Duration:** <32 min or n/a>

## Summary
<2-3 sentence high-level summary of what this source taught. For fast re-scan months later.>

## Key Concepts Extracted
- [[../concepts/<concept-slug-1>]] — <one-line description of what this concept is>
- [[../concepts/<concept-slug-2>]] — <one-line description>

## Detailed Notes
<COMPREHENSIVE extraction. Pull every valuable detail the transcript / source has to offer. Use ### sub-headings to follow the source's natural structure (chapter markers, section breaks, topic shifts). Do NOT aggressively summarize — the goal is comprehensive capture so future-Anthony can re-read this file instead of re-watching the video.>

### <Sub-topic 1 from the source>
<Detail. Multiple paragraphs OK. Quote specific numbers, claims, mechanics.>

### <Sub-topic 2>
<Detail.>

## Code & Examples
<Code blocks (use fenced ``` with language tags), prompt examples, configs, screenshots described in words. If none: `(none)`>

## Notable Quotes
<Verbatim memorable lines from the source. Format each as a blockquote with attribution: `> "quote text" — speaker, timestamp if known`. If none: `(none)`>

## Action Items
<Concrete things to try, build, or change as a result of this source. One bullet per item. If none: `(none)`>

## Open Questions
<Things this raised that weren't answered — research backlog. If none: `(none)`>

## Related Sources
<Wikilinks to related source files in the vault. If none: `(none)`>
```

**Section headers are mandatory.** All nine: Summary / Key Concepts Extracted / Detailed Notes / Code & Examples / Notable Quotes / Action Items / Open Questions / Related Sources. Plus the visible blockquote at the top of body. Plus the YAML frontmatter.

When the input is short (a 2-paragraph paste) or sparse (raw notes from a single session), the `Detailed Notes` section can be brief — but it MUST still exist. If a video literally has no code, `## Code & Examples` shows `(none)`. Don't pad.

**Source files are immutable.** Once written, never go back and append. New findings on the same topic from later sources update the *concept* files, not the source files.

### Step 3 — Scan-and-decide for each extracted concept

For each concept identified in Step 1:

**Scan procedure:**
1. Use `Glob` on `Optimus Academy/concepts/*.md` to list filenames. Slugify the new concept name and check for direct filename hits or near-misses.
2. Use `Grep` on `Optimus Academy/concepts/` for keyword overlap (the concept's distinctive terms — not generic words like "Claude" or "agent").
3. Read the top 3 candidate files in full (frontmatter + body + Updates).
4. Decide:

| Confidence | Decision | Action |
|---|---|---|
| **High match** (same topic, same domain, candidate is a clear superset/subset) | APPEND | Add a `## Update` section to the existing concept file. See append details below. |
| **Weak/no match** | CREATE | Write a new concept file using the rigid concept structure. See create details below. |
| **Borderline** (related but might be its own concept) | ASK | Stop and ask the user: "This looks related to `[[<existing-concept-slug>]]` — append there or create new?" Default suggestion: CREATE NEW (false-merge is worse than false-create). |

#### CREATE path — new concept file

Path: `Optimus Academy/concepts/<concept-slug>.md`

```markdown
---
title: <Concept Name>
domain: <claude-api | agents | obsidian | etc.>
created: <YYYY-MM-DD>
last-updated: <YYYY-MM-DD HH:MM>
source-files: [<YYYY-MM-DD-source-slug>]
tags: [#learning/synthesized, #applies-to/<offering-or-all>]
---

# <Concept Name>

> **Concept distilled from:**
> - [[../sources/YYYY-MM-DD-<source-slug>]] — <publisher>
>
> **Last updated:** YYYY-MM-DD HH:MM

## What it is
<1-2 sentence definition. Stable. Doesn't change when new sources arrive.>

## When to use
<Concrete situations where this matters. Bullet list ok.>

## Mechanics
<How it actually works — the meat. Sub-headings ### allowed.>

## Examples
<Code, prompts, scenarios. If none: `(none)`>

## Gotchas
<Failure modes, edge cases, common mistakes. If none: `(none)`>

## Related Concepts
<Wikilinks to related concept files. If none: `(none)`>

## Updates
<Empty on creation. Future updates from later sources land here.>
```

**Section headers mandatory:** What it is / When to use / Mechanics / Examples / Gotchas / Related Concepts / Updates. Plus visible blockquote at top of body. Plus YAML frontmatter. The `## Updates` section is empty on creation but the header is still present — it's the contract that signals "this is where future findings will land."

#### APPEND path — existing concept file

1. Read the existing file in full.
2. Bump frontmatter `last-updated` to `YYYY-MM-DD HH:MM`.
3. Append the new source slug to frontmatter `source-files:` list.
4. Add a new wikilink to the visible blockquote at top of body:
   ```
   > - [[../sources/YYYY-MM-DD-<new-source-slug>]] — <publisher>
   ```
5. Append a new block under the existing `## Updates` section:
   ```markdown
   ### YYYY-MM-DD HH:MM — <short label> — from [[../sources/YYYY-MM-DD-<source-slug>]]
   <What this new source added beyond the original definition. Specific. Cite which `### sub-topic` of the source if applicable. Don't restate what the source file already covers — just the *delta* this source brings to the concept.>
   ```
6. Do NOT modify any of: `## What it is`, `## When to use`, `## Mechanics`, `## Examples`, `## Gotchas`, `## Related Concepts` body content. The top stays stable; new findings live only in `## Updates`.

### Step 4 — Apply-to-Optimus bridge note(s) (when applicable)

Only create a bridge note when the concept has a clear, concrete application to one of the four Optimus offerings. Pure theory or "interesting but not actionable" content does NOT get a bridge note — skip this step in that case.

If the concept applies to multiple offerings, create multiple bridge notes (one per offering).

Run scan-and-decide on `Optimus Academy/apply-to-optimus/*.md` first — if a bridge for this concept+offering pair already exists, APPEND a `## Update` section instead of duplicating.

#### CREATE path — new bridge

Path: `Optimus Academy/apply-to-optimus/<concept-slug>-applied-to-<offering-slug>.md`

Offering slugs: `website-dev`, `ai-chat`, `ai-voice`, `ai-marketing`, or `all-agents` (when it applies to chat + voice + marketing).

```markdown
---
title: <Concept Name> applied to <Offering Name>
concept: [[../concepts/<concept-slug>]]
source-files: [<YYYY-MM-DD-source-slug>]
offering: [[../../Offerings/<offering-folder>/README]]
created: YYYY-MM-DD
last-updated: YYYY-MM-DD HH:MM
status: not-started
tags: [#learning/applied, #applies-to/<offering-tag>]
---

# <Concept Name> applied to <Offering Name>

> **Concept:** [[../concepts/<concept-slug>]]
> **Source(s):**
> - [[../sources/YYYY-MM-DD-<source-slug>]] — <publisher>
> **Offering:** [[../../Offerings/<offering-folder>/README]]
> **Status:** `not-started`
> **Last updated:** YYYY-MM-DD HH:MM

## What I learned
<1-2 sentence summary with link to the concept note>

## Why it applies to <offering>
<Concrete mechanism — what about the offering today benefits from this concept>

## How to apply it
<Actionable steps. File paths if known. Agent changes. Workflow tweaks. Commit-level granularity is great.>

## Status
`not-started`

## Updates
<Empty on creation. Future updates land here.>
```

**Section headers mandatory:** What I learned / Why it applies / How to apply it / Status / Updates. Plus visible blockquote. Plus frontmatter.

#### APPEND path — existing bridge

Same pattern as concept-append: bump `last-updated`, add to `source-files:` list, add wikilink to visible blockquote, append a `### YYYY-MM-DD HH:MM — <label> — from [[<source>]]` block under `## Updates`. Don't touch the original `## What I learned` / `## Why it applies` / `## How to apply it` / `## Status` content.

### Step 5 — Update cross-references

After all concept and bridge files are written/updated:

1. **Update the source file's `concepts-extracted:` frontmatter** with the resolved concept slugs (whether they were created or updated). Update the source file's `## Key Concepts Extracted` body section with the wikilinks.
2. **Verify each touched concept file's `source-files:` frontmatter** includes the new source slug.
3. **Verify each touched bridge file's `source-files:` frontmatter** includes the new source slug.

Bidirectional linking is the load-bearing invariant — every source knows what concepts came from it; every concept knows what sources fed it.

### Step 6 — Generate the daily entry

Path: `Optimus Academy/daily/YYYY-MM-DD.md`

If the file does NOT exist, create with this structure:

```markdown
---
date: YYYY-MM-DD
tags: [#learning/captured]
---

# YYYY-MM-DD — Daily Learning

## HH:MM — <Topic / Source short-name>

<2-3 sentence summary of what was learned in this session>

**Source captured:** [[../sources/YYYY-MM-DD-<source-slug>]] — "<Source Title>" by <publisher>

**Concepts touched:**
- [[../concepts/<concept-slug-1>]] — created
- [[../concepts/<concept-slug-2>]] — updated (added findings on <topic>)

**Bridges to Optimus:**
- [[../apply-to-optimus/<bridge-slug>]] — created
- (or `(none)` if no actionable application)
```

If the file ALREADY exists (multiple learning sessions in one day), APPEND a new `## HH:MM — <Topic>` block at the bottom. Do NOT recreate the H1 or frontmatter.

### Step 7 — Tag application audit

Before committing, verify every file you touched has the right tags from the schema:

- Source files: `#learning/captured` + `#applies-to/<offering-or-all>`
- Concept files: `#learning/synthesized` + `#applies-to/<offering-or-all>`
- Bridge files: `#learning/applied` + `#applies-to/<offering-tag>`
- Daily files: `#learning/captured`

If a concept is theory-only (no Optimus application), use `#applies-to/all` or omit the applies-to tag entirely. Don't fake an application that isn't there.

### Step 8 — Commit + push

Stage all created/modified files. Commit message format:

```
learn(<domain>): <one-line summary of what was captured>

- Source: [[<source-slug>]] — "<title>" by <publisher>
- Concepts: <slug-1> (created), <slug-2> (updated)
- Bridges: <offering-1>[, <offering-2>] | none
```

Example:
```
learn(obsidian): Obsidian + Claude integration patterns

- Source: [[2026-04-26-supercharging-obsidian-claude-by-mberman]] — "Supercharging Obsidian + Claude" by Matthew Berman
- Concepts: obsidian-claude-integration (updated), claude-canvas-as-thinking-space (created)
- Bridges: ai-agents/marketing (Obsidian as content-strategy substrate)
```

Then `git push`.

## Decisions and judgment calls

**When to skip the apply-to-optimus bridge:** Pure theoretical content (research papers, conceptual frameworks without immediate operational use), historical context (how the field evolved), or content that's interesting but doesn't change how Optimus delivers any of its 4 offerings today. The bridge folder should stay valuable — every file there is a real "I should change something" insight. Bloating it with weak bridges defeats the purpose.

**When to ask before deciding (concept scan):** Whenever the scan returns a candidate file with > 60% topic overlap but < 90% — that borderline zone is where the user's judgment beats yours. Ask. Default suggestion in the question: CREATE NEW.

**When to create multiple concept notes from one source:** When the source genuinely teaches 2-3 distinct, named concepts. A 30-min YouTube video on "5 things about agentic loops" might surface 1 atomic concept (the agentic loop pattern) — not 5. A 90-min Anthropic course module might genuinely surface 3-4 distinct concepts. Be conservative — fewer, sharper concept notes are more valuable than many weak ones. The source file captures the full detail regardless; concepts are the *reusable distillations*.

**When the input is sparse:** If raw notes are only a few paragraphs, the source file's `## Detailed Notes` section will be brief — that's fine. The structure contract requires the section *exists*; it does not require minimum content length. `(none)` for genuinely empty sections is correct.

**When NOT to use `(none)`:** Don't use `(none)` to dodge work. If the source has 3 code examples, all 3 belong in `## Code & Examples`. If the source has zero code examples (a pure theory talk), then `(none)` is correct. The test: did you check, and was there genuinely nothing? Then `(none)`. Did you skip the section because it was a hassle? Then go back and fill it.

**When to leave the daily entry brief:** The daily entry is a chronological pointer, not a duplicate of the source content. 2-3 sentence summary + wikilinks is correct. If you find yourself writing a paragraph in the daily entry, you're putting content in the wrong file — move it to the source's `## Detailed Notes`.

## Validation before reporting done

Before committing, validate every file you wrote:

**Source file checklist:**
- Frontmatter has all 10 fields (title, source-type, publisher, url, source-date, captured, duration, domain, concepts-extracted, tags)
- Visible blockquote under H1 has all 6 fields (Source title, By, Type, URL, Captured, Duration)
- All 9 body sections present in order: Summary / Key Concepts Extracted / Detailed Notes / Code & Examples / Notable Quotes / Action Items / Open Questions / Related Sources
- Empty sections show `(none)`, not omitted

**Concept file checklist (CREATE):**
- Frontmatter has all 6 fields (title, domain, created, last-updated, source-files, tags)
- Visible blockquote at top has source distillation list + last updated
- All 7 body sections present: What it is / When to use / Mechanics / Examples / Gotchas / Related Concepts / Updates
- `## Updates` section is empty on creation but the header is present

**Concept file checklist (APPEND):**
- Frontmatter `last-updated` bumped
- Frontmatter `source-files:` list grew
- Visible blockquote at top got a new line for the new source
- New `### YYYY-MM-DD HH:MM — <label> — from [[<source>]]` block exists under `## Updates`
- Original `## What it is` / `## When to use` / `## Mechanics` / `## Examples` / `## Gotchas` body content is BYTE-IDENTICAL to before

**Bridge file checklist:** Same pattern as concept (CREATE: 5 sections + Updates; APPEND: bump + append-only).

**Daily entry checklist:**
- File exists at `Optimus Academy/daily/YYYY-MM-DD.md`
- Contains a `## HH:MM — <Topic>` block for this session
- Wikilinks to source + concepts + bridges (or `(none)` for bridges if not applicable)

**Cross-reference checklist:**
- Source file's `concepts-extracted:` frontmatter matches the concepts touched
- Each touched concept file's `source-files:` includes the new source slug
- Each touched bridge file's `source-files:` includes the new source slug

**Git checklist:**
- `git status` shows the expected files staged + nothing unintended
- `git log -1` confirms the commit landed
- `git push` succeeded

Then report: source captured, concepts touched (with create/append/ask resolution), bridges created (or none), and the commit hash.
