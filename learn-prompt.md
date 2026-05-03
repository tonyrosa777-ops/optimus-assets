---
name: learn
description: Capture daily learning from any source (YouTube video, course, article, raw notes) into Optimus Academy. The daily file IS the comprehensive per-source capture; concept files are synthesized atomic distillations that grow over time as new sources teach more about the same topic. Every file follows a rigid identical contract with autonomy hooks (Dataview fields, schema-version, deterministic slugs, controlled vocab) baked in from day 1.
effort: medium
---

# /learn — Daily Learning Capture

## Usage

Run from inside `c:\Projects\Optimus Assets\` with the input attached or pasted:

```
/learn                                  # input is whatever the user has pasted/attached
/learn <YouTube URL>                    # fetch transcript first, then process
/learn <TikTok | IG Reel | Shorts URL>  # downloads + transcribes locally via Whisper
/learn <X video URL>                    # same path as TikTok (yt-dlp + Whisper)
/learn <article URL>                    # WebFetch the article, process as text
/learn <topic hint>                     # disambiguates ambiguous input
/learn --no-enrich <URL>                # skip the web-enrichment step (Step 1.7)
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

Read the input fully. Routing depends on the input shape:

**(a) URL detection and transcription.** Detect the URL pattern in the input:

| URL pattern | Routing |
|---|---|
| `youtube.com/watch?v=...` | Use WebFetch to get the transcript (existing behavior, unchanged). |
| `tiktok.com/...`, `vm.tiktok.com/...`, `instagram.com/reel/...`, `instagram.com/p/...`, `youtube.com/shorts/...`, `x.com/.../status/.../video/...` | Invoke the local transcribe helper. Run via Bash: `py -3.11 "Optimus Academy/tools/transcribe-url.py" "<URL>"`. **Use `py -3.11` exactly — never bare `python` or `python3` (Python 3.14 is broken on this machine and shadows 3.11).** Parse the JSON returned on stdout: `{transcript, publisher, title, url, source_date, duration}`. These fields seed the source metadata for Step 1 attribution. The transcript becomes the body the rest of the steps process. |
| Plain article URL (any other http/https URL not matching the patterns above) | Use WebFetch on the URL to get the article body, parse for title/publisher/date from page metadata. |
| No URL (pasted text, raw notes) | Use the input directly as the transcript/notes body; the user provides source metadata in the same message (or you ask for it). |

**Exit-code handling for the transcribe helper:**
- `0` — success; parse JSON, continue
- `1` — runtime error; report stderr to the user verbatim, do not proceed
- `3` — yt-dlp missing → tell user: "Run `py -3.11 -m pip install yt-dlp` then re-run."
- `4` — ffmpeg missing → tell user: "Install ffmpeg (Windows: `scoop install ffmpeg` or `choco install ffmpeg`) then re-run."
- `5` — openai-whisper missing → tell user: "Run `py -3.11 -m pip install openai-whisper` then re-run."
- `6` — wrong Python version → tell user: "Invoke via `py -3.11`, not bare `python`."
- Any other non-zero → report stderr verbatim, do not proceed.

**(b) X (Twitter) handling rule.**
- **Single posts:** skip. A single tweet (≤280 chars) is too short to earn a concept note. If the tweet sparks a real thought, capture the *thought* via paste-text, citing the tweet as inspiration in the source blockquote — do not capture the tweet itself.
- **Threads:** worth capturing. Use the paste-text fallback (no URL detection routes to it). Anthony copies the full thread (top to bottom), pastes into `/learn`, sets `publisher = @handle`, `url = link to first tweet`, `source-type = thread`, `source-date = first tweet date`.
- **Embedded videos:** the URL pattern detection above already routes `x.com/.../status/.../video` through the transcribe helper. No special handling.
- This rule prevents the most common social-media failure mode: fragmenting `concepts/` with single-tweet one-liners.

**(c) Extract source metadata.** From whichever path above, you now have:

- **Source title** — the exact title (from yt-dlp metadata, page meta tags, or user-provided)
- **Source type** — one of: `video`, `article`, `course`, `book`, `podcast`, `notes`, `thread` (X threads)
- **Publisher / author / channel** — who produced it
- **URL** — canonical form per tag-schema.md (strip tracking params, force https, prefer `youtube.com/watch?v=X`). Literal `n/a` if none.
- **Source-date** — `YYYY-MM-DD` or `unknown`
- **Duration** — runtime (e.g. `32 min`) or `n/a`
- **Domain** — controlled vocab from tag-schema.md (`claude-api`, `agents`, `prompt-engineering`, `obsidian`, `evals`, `tooling`, `voice`, `marketing`, `web-dev`, `automation`, `business`, plus extensions: `copywriting`, `sales`, `psychology`, `finance`, `design`, `productivity`, `hiring`, `brand`). If nothing fits, propose adding to the vocab.

**(d) Extract candidate topics** (NOT atomic concepts yet):
- A topic is a named, reusable area of knowledge.
- Sub-patterns of a single topic are NOT separate topics — they live as sub-headings under `## Mechanics` in the parent concept.
- For each topic, note its applicability to any of the five bridge target zones (see Step 4): an Optimus offering, `knowledge/patterns/`, `knowledge/craft/<area>/`, `Optimus Inc/<area>/`, or `Optimus Academy/tools-tracking/`.

### Step 1.5 — Enrichment via web search (when source is shallow)

Short-form sources (TikToks, Reels, Shorts) frequently surface a topic without explaining it deeply enough to evaluate. A 15-second TikTok mentioning "DialogueDB is the new agent memory tool" is real signal but the source itself can't fill out Mechanics / Examples / Gotchas. Enrichment fixes this by augmenting the captured concept with web research — *without* polluting the original source attribution.

**Auto-trigger when ANY of the following are true** (otherwise skip enrichment):
- Source duration < 60 seconds OR transcript word count < 200
- Source mentions a specific named tool / framework / library / SDK / agent that does NOT yet have a concept file in `concepts/`
- Borderline scan-and-decide case in Step 3 (the source is too thin to confidently choose CREATE vs APPEND)
- The user explicitly passed `--enrich` (force-enrich even if conditions don't trigger)

**Auto-skip when ANY of the following are true:**
- The user passed `--no-enrich` (explicit opt-out for personal/contextual sources)
- Long-form source (full YouTube > 5 min, article > 1000 words) — it's already rich
- Topic exists in `concepts/` AND scan-and-decide says HIGH MATCH — just append the new source reference, no enrichment needed

**Enrichment procedure (when triggered):**
1. Identify the canonical name of the topic / tool / concept the source surfaces (e.g., "DialogueDB", "agentic memory store").
2. Run 2-3 WebSearch queries — vary the angle:
   - `"<topic> documentation"` (find authoritative source)
   - `"<topic> review"` OR `"<topic> vs <closest existing concept>"` (find evaluative content)
   - `"<topic> when to use"` OR `"<topic> tradeoffs"` (find Gotchas substrate)
3. Read the top 3-5 results via WebFetch. Cap total enrichment work at 5 fetches to avoid bloat.
4. Synthesize the enriched info into the concept's Mechanics / Examples / Gotchas sections. Keep the original transcript content distinct — enrichment fills the rich technical detail the original source lacked.
5. **Source attribution split:** the daily file's H2 section credits ONLY the original source (the TikTok), not the enrichment URLs. The concept file's frontmatter gets a NEW `enriched-from:` field listing the enrichment URLs:
   ```yaml
   enriched-from: ["https://docs.example.com/...", "https://news.example.com/..."]
   ```
6. Tag the concept with `#learning/enriched` in addition to `#learning/synthesized` so it's queryable in Dataview.

**Why the source-attribution split matters:** if both the TikTok AND the enrichment URLs were credited equally on the daily file, future "show me everything I learned from TikTok creator X" queries would return enrichment URLs that have nothing to do with creator X. Enrichment is *concept-level* augmentation, not *capture-level* re-attribution.

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
enriched-from: []   # populated only when Step 1.5 enrichment fires; list of URLs read via WebSearch/WebFetch
tags: [#learning/synthesized, #applies-to/<offering-or-zone>]
# Forward-compat fields for future Optimus University compilation (all OPTIONAL):
level: <foundational | intermediate | advanced>   # pedagogical difficulty; populate when source makes it obvious
prerequisites: []                                  # wikilinks to concepts learner needs first; only fill when source explicitly references them
audience: []                                       # multi-valued from {founder, developer, marketer, client, optimus-internal}
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

**Forward-compat field decision rules** (all three optional — leave blank when ambiguous):

- **`level`**: `foundational` if the source teaches a primitive ("what is anchoring"). `advanced` if it builds on assumed primitives ("how anchoring interacts with loss aversion in 3-tier pricing"). `intermediate` is the default when ambiguous. Omit entirely if you genuinely cannot judge.
- **`prerequisites`**: only fill when the source explicitly references another concept that already exists in `concepts/`. Do NOT invent prerequisites the source doesn't reference. Empty list `[]` is fine.
- **`audience`**: multi-valued from `{founder, developer, marketer, client, optimus-internal}`. A copywriting tactic universally useful → `[founder, marketer]`. A developer-only Next.js pattern → `[developer]`. If unsure → omit. Better blank than wrong.

These fields are the substrate for future Optimus University compilation. They turn `concepts/` into a Dataview-queryable course library — `"foundational copywriting concepts targeting founder audience, ordered by prerequisite depth"` → course outline. Adding the fields after the fact is 10× the cost of adding them at capture time.

**`enriched-from:` field:** populated ONLY when Step 1.5 enrichment fires. Lists the URLs read via WebSearch/WebFetch to augment the concept beyond the original source. Empty list `[]` when enrichment didn't fire.

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
5. **Information-delta check** (the dedup gate):
   - Read what the existing concept already covers in its `## What it is` / `## When to use` / `## Mechanics` / `## Examples` / `## Gotchas` sections AND in any prior `## Updates` blocks.
   - Compare the new source's content against what's already there.
   - **Block ONLY identical/near-verbatim repetition.** If the new source says the same thing already in the concept (same point, same example, same gotcha — just different wording), do NOT add an `## Updates` block. The `source-references:` list still gets the new daily-anchor (so the concept tracks every source that taught it), but no body content change.
   - **Variations always pass.** A new angle on a known principle, a new example of a known pattern, a new gotcha not previously listed, a new mechanism, a new use case, a contradiction worth noting — these are all NEW information and ALWAYS earn an `## Updates` block. Variations are never rejected.
   - When in doubt: append. False-restate (slightly redundant Updates block) is recoverable later by editing. False-suppress (omitting a real variation) loses information permanently.
6. If the information-delta check passed (new info present), append a new block under the existing `## Updates` section:
   ```markdown
   ### YYYY-MM-DD HH:MM — <short label> — from [[../daily/YYYY-MM-DD#HH:MM — "Source Title" by Publisher]]
   <The delta — what this source added beyond what the concept already had. Specific. Cite which `#### sub-topic` of the daily section if applicable. Focus on the new angle, new example, new gotcha, or new mechanism — NOT a re-summary of what was already there.>
   ```
7. Do NOT modify any of: `## What it is`, `## When to use`, `## Mechanics`, `## Examples`, `## Gotchas`, `## Related Concepts` body content. The top stays stable; new findings live only in `## Updates`.
8. Optionally bump `review-by:` to a fresh ~6-months-out date if this update materially refreshes the concept. Otherwise leave it alone.
9. If Step 1.5 enrichment fired during this APPEND run, also update the concept's `enriched-from:` frontmatter list with the new enrichment URLs (preserve any existing entries; this is additive).

### Step 4 — Bridge note(s): route to one of FIVE target zones (not just offerings)

Bridges are NOT scoped to the four Optimus offerings only. The captured topic is broader than AI tooling — sales training feeds copy craft, finance content feeds Optimus Inc operations, marketing psychology feeds CRO, tool reviews feed the internal stack. The bridge layer routes to wherever the knowledge would actually integrate.

**Two stop conditions that turn this into a no-op (concept-only, no bridge):**

1. **No clear target.** If you cannot point to a specific existing-or-soon-to-exist file in the vault that would meaningfully integrate this knowledge, do NOT create a bridge. A vague bridge is dead weight in the weekly review.
2. **No clear value vector.** Per the multi-purpose principle, every bridge MUST declare at least one of `productivity` / `overhead` / `revenue` with concrete reasoning. If you cannot map the concept to at least one vector ("this lifts conversion because…", "this cuts build time because…"), the concept goes to `concepts/` only.

When in doubt, skip the bridge. The user can add one later by editing the concept's `Updates` section once both target AND value vector become clear. Prefer no bridge over a vague bridge in either dimension.

#### The five bridge target zones

Every captured concept's `applies-to:` wikilink points to one of these zones. A single concept may produce multiple bridges — one per applicable zone:

| Zone | Folder | Folder existence at capture time |
|---|---|---|
| `Offerings/<offering>/` | Existing offering hub (`Offerings/01 Website Development/`, `Offerings/02 AI Agents/...`) | All exist |
| `knowledge/patterns/` | Cross-website-build patterns | Exists, populated |
| `knowledge/craft/<area>/` | Cross-cutting craft: `copywriting`, `psychology`, `sales`, `design` | **Does NOT exist** for any `<area>` — lazy-create on first use |
| `Optimus Inc/<area>/` | Optimus the company itself: `finance`, `operations`, `brand`, `website`, `market-intelligence`, `social-pipeline`, `ai-agents` | Some exist (`brand`, `website`, `market-intelligence`, `social-pipeline`, `ai-agents/<tier>/`); `finance` and `operations` do NOT exist — lazy-create per-area |
| `Optimus Academy/tools-tracking/<tool-slug>.md` | Flat file per tool, single-file format (not a subfolder) | Folder exists with `.gitkeep`; first real file populates it |

**Folder creation rule before any bridge write:** verify the parent folder exists via Bash `Test-Path` (PowerShell). If absent, `New-Item -ItemType Directory -Force` (or `mkdir -p`) creates it. Never assume existence. Never preemptively scaffold empty folders.

#### Concrete routing map (source topic → primary + secondary targets)

Use this table to pick `applies-to:` targets. Most rows produce 1-3 bridges, never 0 (unless both stop conditions trigger).

| Source topic | Primary bridge target | Secondary bridge target |
|---|---|---|
| **Sales / cold outreach tactics** | `.claude/agents/sales/gap-analyzer.md` | `knowledge/craft/sales/<slug>.md` (lazy-create) |
| **Copywriting craft** (headlines, CTAs, hooks, structure, tone) | `.claude/agents/build/content-writer.md` | `knowledge/craft/copywriting/<slug>.md` (lazy-create) |
| **Marketing psychology / cognitive bias** | `.claude/agents/build/content-writer.md` AND `.claude/agents/onboarding/design-synthesizer.md` | `knowledge/craft/psychology/<slug>.md` (lazy-create) AND/OR `Optimus Inc/brand/<slug>.md` if it changes Optimus's own marketing voice |
| **CRO / landing page conversion** | `.claude/agents/build/content-writer.md` AND `.claude/agents/onboarding/design-synthesizer.md` | `knowledge/patterns/<slug>.md` |
| **Visual design / UI craft** | `.claude/agents/onboarding/design-synthesizer.md` AND `.claude/agents/build/animation-specialist.md` | `knowledge/craft/design/<slug>.md` (lazy-create) AND/OR `frontend-design.md` |
| **SEO / AEO / discoverability** | `.claude/agents/build/seo-aeo-specialist.md` | `knowledge/patterns/<slug>.md` |
| **Market research / discovery patterns** | `.claude/agents/onboarding/market-researcher.md` | `knowledge/patterns/<slug>.md` |
| **QA / launch / pre-deploy checks** | `.claude/agents/launch/pre-launch-auditor.md` | `knowledge/patterns/<slug>.md` AND/OR `knowledge/errors/<slug>.md` |
| **Finance / runway / pricing strategy for Optimus** | `Optimus Inc/finance/<slug>.md` (lazy-create) | `optimus-system-guide.md` if vault operations change |
| **Hiring / team / org design** | `Optimus Inc/operations/<slug>.md` (lazy-create) | None |
| **Optimus's own marketing / brand voice** | `Optimus Inc/brand/<slug>.md` (folder exists, write directly) | None |
| **Optimus's own website / content strategy** | `Optimus Inc/website/<slug>.md` (folder exists) | `.claude/agents/build/content-writer.md` if it generalizes |
| **Competitive intelligence on Optimus's market** | `Optimus Inc/market-intelligence/<slug>.md` (folder exists) | None |
| **Social media pipeline / Optimus's own social** | `Optimus Inc/social-pipeline/<slug>.md` (folder exists) | None |
| **Optimus's own deployed AI agents** (drink-own-champagne) | `Optimus Inc/ai-agents/<tier>/<slug>.md` (folders exist for chat-assistant, voice-receptionist, marketing-team, autonomous-employee) | Mirror to `Offerings/02 AI Agents/0X/lessons/` if generalizable |
| **Tool reviews / new framework / new SDK** | `Optimus Academy/tools-tracking/<tool-slug>.md` (write directly into existing folder) | `optimus-system-guide.md` only if adopting changes vault ops; OR a Tier-3/Tier-4 `lessons/` file if agent-framework candidate |
| **Vault operations / Obsidian workflow / capture process** | `optimus-system-guide.md` (vault root canonical operating manual) | None |
| **General AI news** (model release, API change, industry trend) | **No bridge — concept note only** unless actionable | If actionable → `optimus-system-guide.md` AND/OR `Offerings/02 AI Agents/0X/lessons/` |
| **Productivity tools for Anthony's own workflow** | `Optimus Inc/operations/personal-stack.md` (lazy-create, append-only single file) | None |

**Worked examples for the four most common source types:**

1. **Sales-training TikTok** — concept: pricing anchor tactic → Bridge A → `.claude/agents/build/content-writer.md` (`value-vector: [productivity, revenue]`); Bridge B → `knowledge/craft/copywriting/anchoring-pricing.md` (`value-vector: [productivity]`).
2. **Finance YouTube** — concept: bootstrapped runway rule → Bridge → `Optimus Inc/finance/runway-rules.md` (`value-vector: [overhead, revenue]`). No other zone applies.
3. **AI tool review** — concept: new agent framework features → Bridge A → `Optimus Academy/tools-tracking/<tool-slug>.md` (`value-vector: [productivity]`); Bridge B (only if Tier-3/Tier-4 candidate) → `Offerings/02 AI Agents/shared-knowledge/lessons/<slug>.md` (`value-vector: [productivity, revenue]`).
4. **Marketing psychology article** — concept: cognitive bias used in CRO → Bridge A → `.claude/agents/build/content-writer.md` (`value-vector: [productivity, revenue]`); Bridge B → `.claude/agents/onboarding/design-synthesizer.md` (`value-vector: [productivity, revenue]`); Bridge C → `knowledge/craft/psychology/<slug>.md` (`value-vector: [productivity]`).

#### CREATE path — new bridge

Run scan-and-decide on `Optimus Academy/apply-to-optimus/*.md` first — if a bridge for this concept+target pair already exists, APPEND instead of duplicating.

Path: `Optimus Academy/apply-to-optimus/<concept-slug>-applied-to-<target-slug>.md`

Target slug examples: `content-writer`, `gap-analyzer`, `optimus-inc-finance`, `optimus-inc-brand`, `tools-tracking-langgraph`, `craft-copywriting`, `craft-psychology`. Slug is derived deterministically from the target file path.

```markdown
---
title: <Concept Name> applied to <Target>
schema-version: 1
concept: [[../concepts/<concept-slug>]]
source-references: ["[[../daily/YYYY-MM-DD#HH:MM — \"Source Title\" by Publisher]]"]
applies-to: [[<wikilink-to-target-file>]]
created: YYYY-MM-DD
last-updated: YYYY-MM-DD HH:MM
status: not-started
value-vector: [<one-or-more-of: productivity, overhead, revenue>]    # MANDATORY, multi-valued
expected-impact: <small | medium | large>                             # OPTIONAL, populate when source makes magnitude obvious
tags: [#learning/applied, #applies-to/<zone-tag>]
---

# <Concept Name> applied to <Target>

> **Concept:** [[../concepts/<concept-slug>]]
> **Source(s):**
> - [[../daily/YYYY-MM-DD#HH:MM — "Source Title" by Publisher]] — Publisher
> **Applies to:** [[<wikilink-to-target-file>]]
> **Status:** `not-started`
> **Value vector(s):** <productivity, overhead, revenue — list which apply>
> **Expected impact:** <small | medium | large | unset>
> **Last updated:** YYYY-MM-DD HH:MM

## What I learned
<1-2 sentence summary with link to the concept note>

## Why it applies to <target>
<Concrete mechanism — what about the target file/agent/area today benefits from absorbing this concept>

## How to apply it
<Actionable steps. File paths. Agent prompt edits. Workflow tweaks. The bridge does NOT auto-edit the target file — Anthony reviews this section and applies the change manually. This is the change-request, not the change.>

## Value vector reasoning
<For each tagged value vector, one sentence on the concrete mechanism. Examples:
- `productivity`: every future client site inherits this anchor via content-writer.md, ~10 min saved per pricing page build
- `revenue`: lifts quiz-to-booking conversion ~5% based on source's cited data
- `overhead`: removes the manual "did I remember to anchor?" check from every build>

## Status
`not-started`

## Updates
<Empty on creation. Future updates from later sources land here.>
```

**Section headers mandatory:** What I learned / Why it applies / How to apply it / Value vector reasoning / Status / Updates.

**Tag mapping by target zone** (use the right `#applies-to/*` tag for the bridge):

| Target zone | Tag |
|---|---|
| `Offerings/01 Website Development/` | `#applies-to/website-dev` |
| `Offerings/02 AI Agents/...` | `#applies-to/ai-agents` (or `#applies-to/ai-agents/{chat,voice,marketing}` for tier-specific) |
| `knowledge/craft/copywriting/` | `#applies-to/craft/copywriting` |
| `knowledge/craft/psychology/` | `#applies-to/craft/psychology` |
| `knowledge/craft/sales/` | `#applies-to/craft/sales` |
| `knowledge/craft/design/` | `#applies-to/craft/design` |
| `Optimus Inc/finance/` | `#applies-to/optimus-inc/finance` |
| `Optimus Inc/marketing/` | `#applies-to/optimus-inc/marketing` |
| `Optimus Inc/operations/` | `#applies-to/optimus-inc/operations` |
| `Optimus Inc/brand/` | `#applies-to/optimus-inc/brand` |
| `tools-tracking/<tool>.md` | `#applies-to/tools/<tool-slug>` |

#### APPEND path — existing bridge

Same dedup nuance as concept-append (Step 3): only block IDENTICAL/near-verbatim repetition; variations always pass.

1. Read the existing file in full.
2. Bump `last-updated`. Add to `source-references:` list. Add wikilink to visible blockquote.
3. **Information-delta check:** does the new source add anything beyond what the bridge already says in `## What I learned` / `## Why it applies` / `## How to apply it` / `## Value vector reasoning` and prior `## Updates`? Variations (new angle, new application step, new vector reasoning, contradictory data) always pass. Identical/near-verbatim repetition is blocked — `source-references:` still grows but no body change.
4. If delta exists, append a `### YYYY-MM-DD HH:MM — <label> — from [[<daily-anchor>]]` block under `## Updates`.
5. **Value-vector merge rule:** if the new source reveals an additional value vector not on the existing bridge, ADD it to `value-vector:` (e.g., a bridge originally tagged `[productivity]` learns from a new source that the same pattern lifts revenue → becomes `[productivity, revenue]`). Never remove existing vectors during APPEND.
6. Don't touch the original body content of `## What I learned` / `## Why it applies` / `## How to apply it` / `## Value vector reasoning` / `## Status`.

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
