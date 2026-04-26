# Optimus System Guide — End-to-End Operating Manual

## 1. What this guide is

This is the single source of truth for how the Optimus Business Solutions vault is meant to be operated. Audience: Anthony, and any future autonomous Claude instance picking up the vault cold.

It is not a duplicate of [[CLAUDE]]. CLAUDE.md is the constitution — universal rules applied during every build. This guide is the operational manual — the WHY behind the structure and the HOW of the workflows that fill it. CLAUDE.md tells you the rules. This guide tells you how the system works as a system.

If this guide and CLAUDE.md disagree, CLAUDE.md wins on rules. This guide wins on workflow shape and structural intent.

## 2. How to use this guide

- **First encounter:** read top to bottom. The hubs, the killer chain, the workflows, and the autonomous trajectory only make sense as a connected picture.
- **After that:** section-jump for the workflow you need. Each workflow section is self-contained.
- **Before any structural change to the vault:** update the relevant section of this guide first. Then change the files. Then add a Changelog entry. See section 13 (Maintenance protocol). A structural change without a guide update is drift, and audits will flag it.

## 3. The 4 hubs at a glance

The vault has four top-level hubs plus the existing website-dev workflow files at root. Hubs are scoped by purpose, not by tooling.

| Hub | One-line purpose | Index |
|---|---|---|
| `00 — Empire Index/` | Vault navigation, master tag schema, glossary. Start here when you don't know where something lives. | [[00 — Empire Index/README]] |
| `Offerings/` | What Optimus sells. One subfolder per product line: website-dev (productized core), and three in-development AI agent products. | [[Offerings/README]] |
| `Optimus Inc/` | The company itself. Optimus's own marketing site, deployed agent instances, market intelligence, social pipeline, brand. Drink-own-champagne layer. | [[Optimus Inc/README]] |
| `Optimus Academy/` | Daily personal learning hub (~90 min/day). Capture from courses, videos, books, articles. The bridge from learning to revenue. | [[Optimus Academy/README]] |

**Root-level workflow files coexist with the hubs.** The website-dev pipeline ([[CLAUDE]], [[project-prime]], [[website-build-template]], [[build-checklist]], [[intake-prompt]], [[market-research-prompt]], [[end-to-end-workflow]], [[frontend-design]], [[retro]], [[learn-prompt]]) and the entire `knowledge/` folder (errors, patterns, retrospectives, sales, onboarding) all stay where they were before the multi-offering reorg. The hubs were added around the website pipeline. Nothing was migrated. Every existing wikilink and every agent's Required Reading section keeps working without edits.

## 4. The killer chain — how learning compounds into business value

The whole system exists to execute one chain:

> **Source consumed → daily capture → concept synthesis → apply-to-optimus bridge → offering improvement → measurable revenue impact.**

Every workflow below is a step in this chain. Every folder in the vault is a stage of it. If a workflow does not advance the chain, it does not belong in the vault.

A concrete example end to end:

1. **Source consumed.** Today, 2026-04-26, a Julian Goldie video drops on "Obsidian + Claude as a content brain." 32 minutes.
2. **Daily capture.** [[Optimus Academy/daily/2026-04-26]] gets an H2 section with the full detailed notes — every claim, every code snippet, every workflow he describes. Inline Dataview `key:: value` fields under the H2 make the source queryable.
3. **Concept synthesis.** A new file lands at `Optimus Academy/concepts/obsidian-as-content-substrate.md`. One concept per topic. If a related concept already exists, /learn appends an `## Update` section instead of fragmenting.
4. **Apply-to-optimus bridge.** The concept clearly applies to the Marketing Team product — a vault-as-content-brain is exactly what the Self Learning Content Engine is. A bridge note lands at `Optimus Academy/apply-to-optimus/obsidian-as-content-substrate-applied-to-ai-marketing.md`. Status: `not-started`.
5. **Offering improvement.** Three weeks later, the bridge is `verified`. The pattern gets promoted into `Offerings/02 AI Agents/03 Marketing Team/lessons/` (or `shared-knowledge/lessons/` if it benefits all three agent products). The Marketing Team product spec evolves to include "client gets an Obsidian vault + Claude content brain."
6. **Measurable revenue impact.** Six months later, every Marketing Team client onboards with a vault. The capability is in the pricing page, in the sales deck, in the demo.

That is the chain. One 32-minute video to a productized capability. The vault structure and the workflows below exist to make this chain frictionless — and eventually, to run it autonomously.

## 5. Workflow 1 — Daily learning (`/learn`)

The most-used workflow in the vault. ~90 min/day target. Cheaper to run /learn three times in a session than to batch a week of learning into one giant capture.

### When to invoke

After consuming any learning material: a YouTube video, an article, a course module, a book chapter, a podcast, a raw note dump. The slash command is defined in [[learn-prompt]] at vault root.

NOT for client-project lessons during a build — those go to `knowledge/build-log.md` via `/retro` after the project closes.

### What `/learn` produces

Three traces per session:

1. **Daily file** at `Optimus Academy/daily/YYYY-MM-DD.md` — the COMPREHENSIVE per-source capture. The daily file IS the source capture. There is no separate `sources/` folder. One H2 section per source consumed that day, with H3 sub-sections (Summary / Key Concepts Extracted / Detailed Notes / Code & Examples / Notable Quotes / Action Items / Open Questions). Inline Dataview `key:: value` fields under each H2 make every source queryable.
2. **Concept file** at `Optimus Academy/concepts/<concept-slug>.md` — the synthesized atomic distillation. ONE concept per TOPIC, not per source. When a new source covers an existing topic, /learn APPENDS an `## Update — date — from [[daily/...]]` section to the existing concept file. The original definition stays stable. New findings stack chronologically under `## Updates`.
3. **Bridge file** at `Optimus Academy/apply-to-optimus/<concept-slug>-applied-to-<offering-slug>.md` — optional. Only when the concept has a clear application to one of the four Optimus offerings. Pure theory, no bridge.

### The rigid identical structure contract

Every file produced by /learn follows a rigid section structure for its file type. Section headers are ALWAYS present, in the same order, even when the section has no content. Empty sections show literally `(none)`. This is non-negotiable.

The reason: predictability beats efficiency. A reader scrolling any concept file knows that gotchas live in `## Gotchas`. They never have to scan to find it. They never wonder if a section was skipped because there was nothing to say or because the author got lazy. `(none)` means "I checked, and there genuinely was nothing for this section."

Every concept and bridge file also has a visible source-attribution blockquote at the top of the body — readers see where this knowledge came from the moment they open the file, without peeking at YAML.

### Key conventions

- **The DAILY file IS the source capture.** No separate `sources/` folder. One H2 per source per day.
- **ONE concept per TOPIC, not per source.** Sub-patterns of a topic live as Mechanics sub-headings inside the concept file, not as separate concept files.
- **Default-to-APPEND on borderline scan-and-decide cases.** False-merge is recoverable (split the concept later). False-fragmentation accumulates and is expensive to undo. When in doubt, append.

### Autonomy bake-ins (live as of 2026-04-26)

Several hooks are baked in from day 1 to avoid retrofit cost when the system goes autonomous in 1-2 years:

- **Dataview inline `key:: value` fields** under every source H2 in daily files. Per-source metadata (publisher, url, duration, domain) becomes machine-queryable.
- **`schema-version: 1`** in YAML on every /learn-produced file. Enables safe migrations later — agents can detect old schemas and convert them without guessing.
- **Deterministic slug rule** in [[00 — Empire Index/tag-schema|tag-schema]]. Lowercase ASCII → non-alphanumeric to `-` → collapse → trim → cap 80. Same input always produces the same slug — without this, scan-and-decide breaks.
- **Controlled `domain:` vocabulary** in tag-schema. 11 starter domains. Free-text domains break "show me all concepts in domain X" Dataview queries the moment a typo or capitalization variant slips in.
- **`captured-by:` field** (`human` or `agent:<name>`). Future-proofs autonomous capture attribution.
- **`review-by:` field** on concepts (default created date + 6 months). Enables nightly stale-knowledge surface — see section 12.
- **Source URL canonical form rule** in tag-schema. YouTube IDs normalized, tracking params stripped. For dedup and queryability.

### How to verify output

[[learn-prompt]] contains the validation checklists for daily files, concept files (CREATE and APPEND paths), bridge files, and cross-references. Run them before commit. The /learn workflow ends with a tag application audit and a commit + push.

### Useful Dataview queries to run weekly

A few of the most useful queries to gut-check learning patterns. The full set lives in section 11.

- All sources captured this week (have I been showing up?)
- Concepts with 2+ source references (cross-validated topics worth deep work)
- Bridges in `not-started` status (the actionable backlog)

## 6. Workflow 2 — Promoting concepts to offerings (the apply-to-optimus path)

Concepts mature in stages. The bridge note is where a concept stops being learning and starts being a product change.

### Identifying when a concept matures enough to bridge

A concept is bridge-ready when:

- It is concrete enough to point at a specific file path, agent change, or workflow tweak in one of the four offerings.
- The action is more than "we should think about this." It has a verb and a target.
- The benefit is measurable in time, money, conversion rate, or capability.

Pure theory does not get a bridge. "Interesting research paper on multi-agent coordination" is concept-only. "Claude Code's `--continue` flag eliminates context resets between subagent runs, applies to the website-build agent loop" is bridge-ready.

### Writing a bridge note

Bridge notes live at `Optimus Academy/apply-to-optimus/<concept-slug>-applied-to-<offering-slug>.md`. Cross-link to the source concept and the source daily entry. State why it applies to this specific offering. State how to apply it — file paths, agent changes, workflow tweaks at commit-level granularity.

The bridge note documents the discovery. The eventual promoted pattern doc (see below) documents the institutional rule.

### Status progression

A bridge moves through four states. The status field is in YAML; it also appears in the visible body.

| Status | Meaning |
|---|---|
| `not-started` | Bridge written. Action proposed. Nothing changed yet in the offering. |
| `in-progress` | The change is being implemented. A branch exists, an agent is running, or files are being edited. |
| `applied` | The change is in production. The offering behaves differently. Effectiveness not yet validated against real outcomes. |
| `verified` | The change is in production AND has been validated by a real outcome (a client build using it, a measurable metric improvement, an agent that successfully consumed it). |

### Promoting a verified bridge

When a bridge hits `verified`, the institutional knowledge gets promoted out of the Academy and into the offering's permanent knowledge store. The bridge stays — it is the discovery record. The promoted pattern doc is what other Claude sessions and other client builds actually read.

| Offering | Promotion target |
|---|---|
| Website Development | `knowledge/patterns/<pattern-slug>.md` AND a new row in `knowledge/build-log.md` |
| AI Agents — cross-product (chat + voice + marketing) | `Offerings/02 AI Agents/shared-knowledge/lessons/<lesson-slug>.md` |
| AI Agents — single product | `Offerings/02 AI Agents/0X <product>/lessons/<lesson-slug>.md` |

The promoted pattern doc cites the bridge note as its origin. Bidirectional link.

## 7. Workflow 3 — Per-offering hub maintenance

Each offering has a hub folder under `Offerings/`. The hub is where the product's identity, pricing, current state, tech stack, and lessons live.

### When to update offering hub files

| File | Update when |
|---|---|
| `README.md` | Product scope or positioning shifts. New capability added. |
| `pricing.md` | Pricing tiers change. New tier added. Tier benefits revised. (Website-dev pricing is fixed in CLAUDE.md — do not customize per client.) |
| `current-state.md` | Capability inventory shifts. New feature shipped. Old feature removed. |
| `tech-stack-research.md` | Stack decision made. New tool adopted. Old tool deprecated. |

### When to add lessons

After each meaningful project or experiment that produced a reusable insight. The threshold is "would I want a future Claude session to know this before starting similar work?" If yes, write the lesson.

For website-dev, lessons land in `knowledge/patterns/` and `knowledge/errors/` — the long-standing convention from before the multi-offering reorg. Unchanged.

For AI agents, lessons land in one of two places:

- **Cross-product pattern** (applies to chat AND voice AND marketing, or any 2+) → `Offerings/02 AI Agents/shared-knowledge/lessons/`
- **Single-product pattern** (applies only to chat, or only to voice, or only to marketing) → `Offerings/02 AI Agents/0X <product>/lessons/`

When in doubt, file under the single product. It is cheaper to copy a lesson into shared-knowledge later than to fragment a vague generality.

### Per-product subfolder discipline (AI Agents)

Each of the three agent products owns its own tech stack and its own lessons inside its product folder. `01 Chat Assistant/`, `02 Voice Receptionist/`, `03 Marketing Team/` each have their own README, current-state, and lessons. The umbrella `Offerings/02 AI Agents/` folder holds only `shared-knowledge/` and the three product subfolders.

## 8. Workflow 4 — Optimus Inc maintenance (drink-own-champagne)

`Optimus Inc/` is the company itself — distinct from `Offerings/` (which is template/IP). Offerings is what we sell. Optimus Inc is what we run.

### Daily competitive intel

Cadence: as findings arrive, not on a strict schedule until the autonomous pulse exists (see section 12). File path: `Optimus Inc/market-intelligence/daily-pulse/YYYY-MM-DD.md`. One file per day. Append within the day's file as new findings land.

### Per-competitor folders

`Optimus Inc/market-intelligence/competitors/<competitor-slug>/`. One folder per major competitor. Each folder holds the competitor's positioning notes, pricing snapshots, feature inventory, and any tactical observations worth keeping over time.

### Tracking dogfood agent instances

`Optimus Inc/ai-agents/{chat-assistant,voice-receptionist,marketing-team}/`. Each subfolder documents Optimus's OWN deployment of that offering — the configuration, the transcripts (chat) or call logs (voice) or content output (marketing), and the tuning notes from running the product against Optimus's own marketing operations. This is the highest-fidelity feedback loop the system has.

### Optimus's own website project

`Optimus Inc/website/` tracks Optimus's own marketing site as a project. The actual repo will live separately (the same way client builds live in their own `c:\Projects\<client-slug>\` repos), but project state, copy decisions, design notes, and post-launch analytics get tracked here.

### Social pipeline

`Optimus Inc/social-pipeline/content-calendar/` for the content calendar. `Optimus Inc/social-pipeline/campaigns/` for active campaign notes. Optimus's own marketing output, planned and executed in the open.

## 9. Workflow 5 — Website development

Brief overview only. The full pipeline lives in [[end-to-end-workflow]] — the `/new-client` orchestrator at vault root. Run `/new-client` from inside a fresh client project folder and the orchestrator runs the entire pre-build through Phase 5 autonomously.

The website-dev workflow continues unchanged from before the multi-offering reorg. Same agents. Same templates. Same `knowledge/` store. Same [[CLAUDE]] constitution.

### Integration with the new hubs

- **Academy concepts can apply to website-dev** via the apply-to-optimus path. A bridge note in `Optimus Academy/apply-to-optimus/<concept>-applied-to-website-dev.md` that reaches `verified` gets promoted into `knowledge/patterns/<pattern>.md` plus a row in `knowledge/build-log.md`. The website-dev pipeline then uses the new pattern automatically on the next build that hits the relevant phase.
- **Each website client retrospective** lands in `knowledge/retrospectives/<client-slug>.md` via `/retro` (defined in [[retro]]). Same as before.
- **Per-client lessons during the build** live in the client repo, not this vault. After launch, `/retro` extracts the durable findings into this vault.

## 10. Cross-cutting — Tag conventions

Reference: [[00 — Empire Index/tag-schema|the master tag schema]]. The full table, controlled `domain:` vocabulary, slug rule, and URL canonical form all live there. Do not duplicate them here.

The 6 tag families:

| Family | When to apply |
|---|---|
| `#offering/*` | Which product line the note belongs to. Most notes carry exactly one. |
| `#layer/*` | Universality scope: `optimus-os` (universal), `offering` (one product), `client` (one engagement). One per note, most-specific applicable. |
| `#learning/*` | Where in the personal-learning pipeline: `captured`, `synthesized`, `applied`. On every Academy note. |
| `#applies-to/*` | Cross-link from Academy notes into offering hubs. Use nested forms (`#applies-to/ai-agents/chat`) for precision. |
| `#stage/*` | Project lifecycle stage. Used on per-client notes and retrospectives. |
| `#status/*` | Maturity: `draft`, `active`, `archived`, `in-development`. One per note. |

Hygiene: tags live in YAML frontmatter arrays only, never as floating inline `#tags` in body text. Inline body tags break Dataview queries that read the YAML field. YAML-only is the contract.

## 11. Cross-cutting — Dataview patterns + example queries

Dataview queryability is baked in from day 1 because autonomous agents need machine-queryable metadata. A nightly stale-knowledge agent (section 12, milestone 1) cannot scan free-form prose for "concepts past their review date." It needs structured fields. Every /learn-produced file exposes those fields.

These queries also live in [[Optimus Academy/README]] for convenience at the point of use. They live in two places intentionally — this guide is the primary reference; the Academy README is the lookup at the moment you need them.

### 1. All sources by publisher (sorted by date)

Useful for "who am I learning from most often?" and for spotting publishers worth bingeing.

```dataview
TABLE WITHOUT ID
  file.link AS "Daily",
  publisher AS "Publisher",
  title AS "Source",
  domain AS "Domain",
  duration AS "Length"
FROM "Optimus Academy/daily"
FLATTEN file.lists AS source
WHERE source.publisher
SORT file.name DESC, source.publisher ASC
```

### 2. All concepts in a given domain

Filter by `domain` to surface every concept in a topic area. Swap the literal for any controlled-vocab domain.

```dataview
TABLE WITHOUT ID
  file.link AS "Concept",
  last-updated AS "Updated",
  length(source-files) AS "Sources"
FROM "Optimus Academy/concepts"
WHERE domain = "obsidian"
SORT last-updated DESC
```

### 3. Bridges by status (kanban view)

Four queries, one per status, gives a kanban of the apply-to-optimus pipeline.

```dataview
TABLE WITHOUT ID file.link AS "Bridge", concept AS "Concept", offering AS "Offering"
FROM "Optimus Academy/apply-to-optimus"
WHERE status = "not-started"
SORT file.mtime DESC
```

Repeat with `status = "in-progress"`, `status = "applied"`, `status = "verified"` for the other columns.

### 4. Sources captured in last 7 days

Gut-check on consistency. If this returns zero rows, the learning practice slipped this week.

```dataview
TABLE WITHOUT ID file.link AS "Daily", file.mtime AS "Captured"
FROM "Optimus Academy/daily"
WHERE captured >= date(today) - dur(7 days)
SORT captured DESC
```

### 5. Concepts with 2+ source references (cross-validated topics)

Concepts taught by multiple independent sources are the highest-confidence material. These are the ones worth bridging fast and going deep on.

```dataview
TABLE WITHOUT ID
  file.link AS "Concept",
  length(source-files) AS "Source count",
  domain AS "Domain"
FROM "Optimus Academy/concepts"
WHERE length(source-files) >= 2
SORT length(source-files) DESC
```

### 6. Concepts not yet bridged to any offering (the backlog)

Concepts with zero corresponding bridge notes — the "interesting but not yet actionable" pile. Periodically scan this list and ask "is this still pure theory, or has it become bridge-ready?"

```dataview
TABLE WITHOUT ID file.link AS "Concept", domain AS "Domain", created AS "Created"
FROM "Optimus Academy/concepts"
WHERE !any(file.outlinks, (l) => contains(string(l), "apply-to-optimus"))
SORT created DESC
```

### 7. Concepts past their `review-by` date (stale-knowledge surface)

The single most important autonomous query. Concepts go stale. The world moves. A concept written today on Claude API behavior is worth re-validating in 6 months. The nightly stale-knowledge agent (section 12, milestone 1) consumes this query.

```dataview
TABLE WITHOUT ID file.link AS "Concept", review-by AS "Review by", last-updated AS "Last updated"
FROM "Optimus Academy/concepts"
WHERE review-by AND review-by < date(today)
SORT review-by ASC
```

## 12. The autonomous trajectory

The 1-2 year goal is full autonomy. Today everything is manual. Below is the priority order in which workflows get automated. Each milestone has a trigger condition, an expected output, a manual approval step (where one exists), and a failure mode.

### Today: everything is manual

- Capture: human runs /learn after consuming a source.
- Synthesis: /learn does the scan-and-decide and writes the concept file, but a human is in the loop reviewing.
- Bridging: human decides when a concept is bridge-ready.
- Verification: human marks a bridge as `verified` after observing the change in production.
- Promotion: human promotes verified bridges to `knowledge/patterns/` or offering `lessons/`.

The autonomy bake-ins (section 5) make every one of these steps machine-trippable. The next sections describe what gets tripped first.

### Milestone 1 — Nightly stale-knowledge surface

- **Trigger:** Cron, nightly at 03:00 local.
- **Action:** Run query 7 from section 11. For every concept past its `review-by` date, post a digest to a `stale-knowledge.md` review file.
- **Manual approval:** Anthony reviews the digest weekly, decides which concepts to re-validate, deprecate, or extend.
- **Failure mode:** Digest grows unbounded if reviews lag. Mitigation: digest caps at 20 oldest concepts per run.

### Milestone 2 — Weekly competitive intel pulse

- **Trigger:** Cron, weekly Monday 06:00.
- **Action:** Agent scans configured competitor sources (their websites, blogs, social, pricing pages) for changes since last pulse. Writes findings into `Optimus Inc/market-intelligence/daily-pulse/YYYY-MM-DD.md`.
- **Manual approval:** None for capture. Anthony reviews the daily-pulse file when convenient. Material findings get promoted into the relevant `competitors/<slug>/` folder.
- **Failure mode:** Source site changes shape, scraper breaks silently. Mitigation: pulse logs every source it scanned + diff size; zero-diff weeks across all sources triggers an alert.

### Milestone 3 — Auto-bridge surfacing

- **Trigger:** New concept file lands (file-system event or post-/learn hook).
- **Action:** Agent reads the new concept's `What it is` + `Mechanics` sections plus each offering's README/current-state. Scores concept-to-offering fit. For any score above threshold, drafts a bridge note in `apply-to-optimus/` with status `draft` (a new pre-not-started status).
- **Manual approval:** Anthony reviews drafts and either promotes to `not-started` (real bridge) or deletes (false positive).
- **Failure mode:** Threshold too low produces noisy backlog; too high misses real bridges. Mitigation: threshold tunes from rejection rate over the first 30 drafts.

### Milestone 4 — Cross-source theme detection

- **Trigger:** Cron, weekly.
- **Action:** Agent scans `concepts/` for two failure modes — fragmentation (multiple concepts that should consolidate into one with `## Update` sections) and clustering (groups of concepts that suggest a missing parent concept needs to crystallize).
- **Manual approval:** Anthony reviews proposed merges and proposed new parent concepts.
- **Failure mode:** Aggressive merging destroys provenance. Mitigation: agent never executes a merge — it only proposes one with the diff. Human runs the merge.

### Milestone 5 — Auto-promotion proposals

- **Trigger:** Bridge note status flips to `verified`.
- **Action:** Agent drafts the promoted pattern doc — for website-dev into `knowledge/patterns/<slug>.md` plus a row in `knowledge/build-log.md`; for AI agents into the appropriate `lessons/` subfolder. Cross-links to the bridge.
- **Manual approval:** Anthony reviews the drafted pattern doc, edits, commits.
- **Failure mode:** Promoted patterns drift from the bridge content. Mitigation: agent diffs bridge body against drafted pattern at promotion time and flags any new claims that did not appear in the bridge.

The trajectory: each milestone removes one human-in-the-loop step. By milestone 5, the chain in section 4 runs end-to-end with the human only validating proposed changes. That is the 1-2 year goal.

## 13. Maintenance protocol — when to update this guide

This guide is the canonical record of how the system is supposed to work. The files are the implementation.

**Update this guide BEFORE making any structural change to the vault.** Examples of structural changes:

- New top-level folder or hub
- Renamed convention (e.g. `sources/` collapsed into `daily/`)
- New workflow or `/slash-command` introduced
- New autonomy hook added to /learn
- New offering added to `Offerings/`
- New tag family or substantial schema change

Procedure:

1. Edit the relevant section here. State the new shape.
2. Add an entry to the Changelog at the bottom with the date, the change, and the commit hash.
3. Make the structural change in the same commit (or the next sequential commit referencing this guide's update).

A structural change without a guide update is treated as drift. Audits will surface it.

## 14. Glossary cross-reference

Terminology lives at [[00 — Empire Index/glossary]]. Do not duplicate definitions here. If a term is missing from the glossary, add it there.

## 15. Changelog

- 2026-04-26 — Initial vault scaffold (Empire Index + Offerings + Optimus Inc + Optimus Academy). Commit ea4033d.
- 2026-04-26 — /learn workflow introduced (initial sources/concepts/bridges/daily model). Commit 1371a99.
- 2026-04-26 — /learn restructured: sources collapsed into daily; topic-recognition tightened; autonomy bake-ins added (Dataview inline fields, schema-version, deterministic slugs, controlled domain vocab, captured-by, review-by, URL canonicalization, example Dataview queries). Concepts consolidated. System guide introduced. Commit <pending>.
