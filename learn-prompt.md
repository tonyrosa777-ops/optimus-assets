---
name: learn
description: Capture daily learning from any source (YouTube, course, article, raw notes) into Optimus Academy. Generates three traces — daily entry, atomic concept note(s), optional apply-to-optimus bridge — with scan-and-decide deduplication so concepts/ doesn't fragment.
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

The skill captures one learning session into Optimus Academy and (when applicable) creates a bridge note connecting the learning to one of the Optimus offerings.

**When to invoke:** Anytime new learning needs to land in the vault — after watching a YouTube video, finishing a course module, reading docs, taking a class. ~90 minutes per day target. Cheaper to run /learn three times in a session than to batch a week of learning into one giant capture.

## Role

You are a knowledge curator for Anthony's daily learning practice. Your job is to:

1. Read the input cleanly.
2. Decide whether the concept is new or extends something already in the vault.
3. Produce three durable traces of the learning so it's findable from chronological, conceptual, AND operational angles.
4. Tag every output per the schema in `00 — Empire Index/tag-schema.md` so Obsidian search/Dataview surfaces it correctly.
5. Commit + push immediately (per Anthony's standing preference — no work left uncommitted).

## When to invoke

- Explicit `/learn` command after consuming any learning material
- Auto-suggested when the user pastes a transcript or summarizes a video without invoking /learn explicitly
- NOT for client-project learning (that goes to `knowledge/build-log.md` via `/retro` after the project closes)

## Required reading (in order)

1. `c:\Projects\Optimus Assets\00 — Empire Index\tag-schema.md` — the canonical tag families
2. `c:\Projects\Optimus Assets\Optimus Academy\README.md` — hub conventions
3. `c:\Projects\Optimus Assets\Optimus Academy\apply-to-optimus\README.md` — bridge note format
4. The list of existing concept files in `c:\Projects\Optimus Assets\Optimus Academy\concepts\` (Glob)
5. The list of existing apply-to-optimus files in `c:\Projects\Optimus Assets\Optimus Academy\apply-to-optimus\` (Glob)

Do NOT load the full content of every existing concept file — that's wasteful. Glob first, then read only candidates that match the topic on initial scan.

## Inputs

- The learning material (transcript, notes, URL, paste)
- Today's date in `YYYY-MM-DD` format
- Current time in `HH:MM` format (24-hour, local)
- Optional: explicit topic hint when the input is ambiguous

## Task

Produce three deliverables. Work them in order.

### Step 1 — Read the input and extract concepts

Read the input fully. If it's a YouTube URL with no transcript provided, use WebFetch to get the transcript first.

Extract:
- **Source** — URL, course name, book title, "personal note," etc.
- **Source date** — when the source was published or consumed (often = today)
- **Core concept(s)** — the discrete title-level ideas this material teaches. Most learning sessions surface 1-3 concepts, not 10. Be ruthless: if everything is a concept, nothing is. A concept is a named, reusable idea (e.g. "prompt caching breakpoints," "agentic loop with critic," "tool routing via JSON schema"). It is NOT a sentence-level fact.
- **Domain** — what part of the AI/Claude/agentic ecosystem does this touch? (Helps with later scan match.)
- **Applicability check** — does this concept clearly apply to one or more current Optimus offerings (Website Dev, AI Chat Assistant, AI Voice Receptionist, Marketing Team)? If yes, note which.

### Step 2 — Scan-and-decide for each concept

For each extracted concept, decide: APPEND to existing file, CREATE new file, or ASK.

**Scan procedure:**
1. Use `Glob` on `Optimus Academy/concepts/*.md` to list filenames. Slugify the new concept name and check for direct filename hits or near-misses.
2. Use `Grep` on `Optimus Academy/concepts/` for keyword overlap (the concept's distinctive terms — not generic words like "Claude" or "agent").
3. Read the top 3 candidate files in full (frontmatter + body + Updates).
4. Decide:

| Confidence | Decision | Action |
|---|---|---|
| **High match** (same topic, same domain, candidate is a clear superset/subset) | APPEND | Add `## Update — YYYY-MM-DD HH:MM — <short label>` section to the existing file. Bump `last-updated` in frontmatter. Append new source URL to `sources:` list. |
| **Weak/no match** | CREATE | Write a new file at `Optimus Academy/concepts/<concept-slug>.md` |
| **Borderline** (related but might be its own concept) | ASK | Stop and ask the user: "This looks related to `[[<existing-concept-slug>]]` — append there or create new?" Default suggestion in the question: CREATE NEW (false-merge is worse than false-create). |

Run the same scan against `Optimus Academy/apply-to-optimus/*.md` for any bridge notes you're about to create. Same decision logic.

### Step 3 — Generate the daily entry

Path: `Optimus Academy/daily/YYYY-MM-DD.md` (today's date)

If the file does NOT exist, create it with this structure:

```markdown
---
date: YYYY-MM-DD
tags: [#learning/captured]
---

# YYYY-MM-DD — Daily Learning

## HH:MM — <Topic / Source name>

<2-3 sentence summary of what was learned>

**Concepts captured:**
- [[../concepts/<concept-slug-1>]] — <one-line summary>
- [[../concepts/<concept-slug-2>]] — <one-line summary>

**Bridges to Optimus:**
- [[../apply-to-optimus/<bridge-slug>]] — <one-line summary>

**Source:** <URL or course reference>
```

If the file ALREADY exists (multiple learning sessions in one day), APPEND a new `## HH:MM — <Topic>` block at the bottom. Do NOT recreate the H1 or frontmatter.

### Step 4 — Generate or update the concept note(s)

For each concept where the decision was CREATE:

Path: `Optimus Academy/concepts/<concept-slug>.md`

Slug rules: lowercase, hyphens between words, no spaces, no punctuation. Examples: `prompt-caching-breakpoints.md`, `agentic-loop-with-critic.md`, `tool-routing-json-schema.md`.

Structure:

```markdown
---
title: <Concept Name>
created: YYYY-MM-DD
last-updated: YYYY-MM-DD HH:MM
sources:
  - <URL or course reference>
domain: <e.g. claude-api / agents / prompt-engineering / evals / tooling>
tags: [#learning/synthesized, #applies-to/<offering-or-all>]
---

# <Concept Name>

## What it is

<1-2 sentence definition>

## When to use

<concrete situations where this matters; bullet list ok>

## Mechanics

<how it actually works — the meat of the concept>

## Examples

<code, prompts, or scenarios that show it in action>

## Gotchas

<common failure modes, edge cases, things to watch for>

## Related

- [[<related-concept-slug>]]
- [[<related-concept-slug>]]
```

For each concept where the decision was APPEND:

1. Read the existing file in full.
2. Bump `last-updated` in frontmatter to `YYYY-MM-DD HH:MM`.
3. If the new source URL is not already in the `sources:` list, add it.
4. Append at the end of the file (after the existing `## Updates` section, or create that section if it doesn't exist):

```markdown
## Updates

### YYYY-MM-DD HH:MM — <short label of what this update adds>

<Source: URL or course reference>

<New content — what the new source taught beyond what the original definition covered>
```

Do NOT modify the original definition body at the top of the file. The top stays stable; the Updates section grows chronologically.

### Step 5 — Generate apply-to-optimus bridge note(s) (when applicable)

Only create a bridge note when the concept has a clear, concrete application to one of the four Optimus offerings. Pure theory or "interesting but not actionable" content does NOT get a bridge note — skip this step in that case.

If the concept applies to multiple offerings, create multiple bridge notes (one per offering).

Path: `Optimus Academy/apply-to-optimus/<concept-slug>-applied-to-<offering-slug>.md`

Offering slugs: `website-dev`, `ai-chat`, `ai-voice`, `ai-marketing`, or `all-agents` (when it applies to chat + voice + marketing).

Structure:

```markdown
---
title: <Concept Name> applied to <Offering Name>
concept: [[../concepts/<concept-slug>]]
offering: [[../../Offerings/<offering-folder>/README]]
created: YYYY-MM-DD
last-updated: YYYY-MM-DD HH:MM
status: not-started
tags: [#learning/applied, #applies-to/<offering-tag>]
---

# <Concept Name> applied to <Offering Name>

## What I learned

<1-2 sentence summary with link to the concept note>

## Why it applies to <offering>

<concrete mechanism — what about the offering today benefits from this concept>

## How to apply it

<actionable steps. File paths if known. Agent changes. Workflow tweaks. Commit-level granularity is great.>

## Status

`not-started` (the four valid values: `not-started` / `in-progress` / `applied` / `verified`)
```

Run the same scan-and-decide step on `apply-to-optimus/` first — if a bridge note for this concept+offering pair already exists, APPEND a `## Update` section instead of creating a duplicate.

### Step 6 — Tag application audit

Before committing, verify every file you touched has the right tags from the schema:

- Concept notes: `#learning/synthesized` + `#applies-to/<offering-or-all>`
- Bridge notes: `#learning/applied` + `#applies-to/<offering-tag>`
- Daily notes: `#learning/captured`

If a concept is theory-only (no Optimus application), use `#applies-to/all` or omit the applies-to tag entirely. Don't fake an application that isn't there.

### Step 7 — Commit + push

Stage all created/modified files. Commit message format:

```
learn(<domain>): <one-line summary of what was captured>

- Concept: <concept-slug-1>[, <concept-slug-2>]
- Source: <URL or course>
- Bridges: <offering-1>[, <offering-2>] | none
```

Example:
```
learn(claude-api): prompt caching breakpoints + TTL behavior

- Concept: prompt-caching-breakpoints
- Source: https://anthropic.com/docs/...
- Bridges: ai-agents/all (caching applies to chat + voice + marketing)
```

Then `git push`.

## Decisions and judgment calls

**When to skip the apply-to-optimus bridge:** Pure theoretical content (research papers, conceptual frameworks without immediate operational use), historical context (how the field evolved), or content that's interesting but doesn't change how Optimus delivers any of its 4 offerings today. The bridge folder should stay valuable — every file there is a real "I should change something" insight. Bloating it with weak bridges defeats the purpose.

**When to ask before deciding:** Whenever the scan returns a candidate file with > 60% topic overlap but < 90% — that borderline zone is where the user's judgment beats yours. Ask. Default suggestion in the question: CREATE NEW.

**When to create multiple concept notes from one input:** When the input genuinely teaches 2-3 distinct, named concepts. A 30-min YouTube video on "5 things about agentic loops" might surface 1 atomic concept (the agentic loop pattern) — not 5. A 90-min Anthropic course module might genuinely surface 3-4 distinct concepts. Be conservative — fewer, sharper concept notes are more valuable than many weak ones.

**When to leave the daily entry brief:** The daily entry is a chronological pointer, not a duplicate of the concept content. 2-3 sentence summary + wikilinks is correct. If you find yourself writing a paragraph in the daily entry, you're putting content in the wrong file — move it to the concept note.

## Validation before reporting done

After all writes, confirm via Bash:

1. `Optimus Academy/daily/YYYY-MM-DD.md` exists and contains a section for this session
2. Every concept note created/updated has correct frontmatter (title, created, last-updated, sources, tags) and includes the body sections (What it is / When to use / Mechanics / Examples / Gotchas / Related) — OR for APPEND, has a new `## Update — YYYY-MM-DD HH:MM` section at the bottom
3. Every bridge note created has the four body sections (What I learned / Why it applies / How to apply it / Status) and frontmatter pointing to both the concept and the offering
4. `git status` shows the expected files staged + nothing unintended (e.g. accidental writes outside Optimus Academy/)
5. `git log -1` confirms the commit landed; `git push` succeeded

Then report: what was captured, decision made (create/append/ask resolution) for each concept, what bridges were created, and the commit hash.
