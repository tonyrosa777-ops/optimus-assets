# Plan: Anthony Rosa Peer Hub Elevation — Two-Domain Vault Restructure

> **Plan Preservation**: Per CLAUDE.md naming convention, this plan will be copied to
> `C:\Projects\Optimus Assets\anthony-rosa-peer-hub-elevation.md` BEFORE execution begins,
> committed in the same git commit as the implementation. Auto-generated filename is working
> memory only.

---

## Context

The vault today has a single-domain mental model: Optimus Business Solutions (LLC) is the primary
domain, with `anthony-rosa/` positioned as a **subordinate founder-vision layer** that exists to
inform Optimus decisions. `optimus-system-guide.md` Section 3 explicitly states "the founder
layer is not a fifth hub — it is the layer above the hubs."

But Anthony's actual mental model is **two peer domains that overlap**:

- **Optimus** (the LLC) = liability shield + productized services for SMB clients. Mission-bounded:
  bring newest tech to small businesses at affordable prices.
- **Anthony Rosa** (the human) = career, AI engineering skills, automated personal revenue streams
  (trading bot, AI influencer, TikTok shop personal angle), investment thesis (AKT, BTC, crypto,
  retirement modeling), long-term horizons.

**The overlap is the asset.** AI influencer skill ships value into both: Anthony's TikTok Shop
revenue *and* Optimus's client content-creation deliverable. OpenClaw productization on Akash is
an Optimus product *and* a thesis-validator for Anthony's AKT position. Same skill, two revenue
surfaces. This is leverage that's structurally impossible if the vault is single-domain.

Today there is **literally no clean home** in the vault for: AKT/BTC personal investment tracking,
trading bot R&D, AI influencer as a personal revenue project (vs. Optimus client deliverable),
career skill goals not yet applied to Optimus, crypto thesis, retirement modeling. And `/learn`'s
5-zone bridge taxonomy has no target for personal-domain learning — every YouTube video on trading
bot architecture or Akash supply economics either pollutes Optimus Academy bridges with off-mission
entries or has nowhere to land.

This plan elevates `anthony-rosa/` to a peer hub, adds the structural support for the two-domain
model (bridge zone, tag family, system guide updates), and creates the concrete file scaffolding
for personal investments, projects, and skills.

---

## Scope

**In scope:**
- Elevate `anthony-rosa/` from subordinate folder to 5th peer hub
- Create three new subfolders: `investments/`, `projects/`, `skills/` with seed files
- Create `apply-to-anthony-rosa/` as 6th `/learn` bridge zone
- Add `#owner/*` tag family to schema
- Update `optimus-system-guide.md` (the canonical operating manual) FIRST per saved memory
- Update CLAUDE.md (Vault Organization section + bridge-taxonomy line)
- Update `learn-prompt.md` (zone table, routing map, tag mapping)
- Update `apply-to-optimus/README.md` (cross-reference the new sibling zone)
- **Split** the existing `ai-influencer-revenue-pipeline.md` bridge into two single-domain
  bridge files: `apply-to-optimus/ai-influencer-client-offering.md` (Optimus client content
  service angle) and `apply-to-anthony-rosa/ai-influencer-personal-revenue.md` (Anthony's
  personal TikTok Shop revenue angle). Both link back to the same shared concept file —
  concept is the unifying point, bridges are domain-specific applications. (The
  `gtm-engineering.md` multi-H2 precedent applies WITHIN a single zone; cross-zone
  applications get separate files, one per zone.)
- Create `anthony-rosa/plans/` folder (CLAUDE.md references it but it was never created)

**Explicitly out of scope:**
- Reconciling the existing 6-vs-7 tag family miscount across CLAUDE.md, system guide, and schema.
  Plan touches `#owner/*` only; broader audit is a separate change.
- Migrating `wins.md` content into `investments/` (it stays where it is — append-only milestone log
  spans both domains).
- Creating retirement/financial modeling spreadsheets — files are scaffolds with frontmatter only.
- Touching the `Akash strict scoping` rule — Akash personal thesis lands in `anthony-rosa/`, but
  Offerings docs stay neutral ("private per-client GPU compute"). Bridge convention enforced.
- Productizing the trading bot or AI influencer — these are personal projects until validation gates clear.

---

## The Synthesis (High-Level Shape)

```
anthony-rosa/                              ← ELEVATED to 5th peer hub
├── north-star.md                          (exists, no edit)
├── ai-engineer-roadmap.md                 (exists, no edit)
├── portfolio-standards.md                 (exists, no edit)
├── wins.md                                (exists, no edit)
├── journal/                               (exists, no edit)
├── plans/                                 (NEW — folder + .gitkeep, fixes existing CLAUDE.md gap)
│
├── investments/                           (NEW)
│   ├── README.md                          (purpose + routing)
│   ├── crypto-thesis.md                   (overall philosophy)
│   ├── akt-tracker.md                     (59,000 AKT @ $0.65, thesis, price targets)
│   └── bitcoin-log.md                     (BTC history, $25k → AKT decision)
│
├── projects/                              (NEW — personal automated revenue streams)
│   ├── README.md                          (purpose + graduation gates pattern)
│   ├── akash-network.md                   (technical research + investment cross-link)
│   ├── ai-influencer.md                   (TikTok Shop angle + cross-link to Optimus deliverable)
│   └── trading-bot.md                     (status, stack, validation gates)
│
└── skills/                                (NEW — career intent layer, NOT knowledge content)
    ├── README.md                          (boundary: skills/ = goals/roadmaps; concepts in Academy)
    └── ai-engineer-progression.md         (career skill goals, gates, why)
```

**6th `/learn` bridge zone:**
```
Optimus Academy/apply-to-anthony-rosa/     (NEW)
├── README.md                              (mirrors apply-to-optimus/README.md structure)
└── (bridge files created on demand by /learn)
```

**Tag schema extension:**
```
#owner/optimus
#owner/anthony-rosa
(notes spanning both domains get both tags)
```

---

## Execution Sequence (Order Matters)

The `optimus-system-guide.md is canonical` saved memory requires the operating manual to be
updated **before** structural vault changes. Sequence is load-bearing:

### Phase A — Operating Manual First
1. Update `optimus-system-guide.md` Sections 3, 4, 6, 10, 13.
2. Update `00 — Empire Index/tag-schema.md` to add `#owner/*` family.
3. Update `00 — Empire Index/README.md` to register the new hub in any nav lists.

### Phase B — Bridge Taxonomy
4. Create `Optimus Academy/apply-to-anthony-rosa/README.md`.
5. Update `learn-prompt.md`: 5-zone table → 6-zone table; routing map; tag mapping.
6. Update `apply-to-optimus/README.md` to cross-reference the sibling zone.
7. Update `CLAUDE.md` Vault Organization section: "FIVE zones" → "SIX zones" + new bridge target +
   add `#owner/*` to tag family list (correcting CLAUDE.md to match schema).

### Phase C — Anthony Rosa Hub Scaffolding
8. Create `anthony-rosa/plans/.gitkeep` (fixes existing CLAUDE.md reference gap).
9. Create `anthony-rosa/investments/` with README.md + 3 seed files.
10. Create `anthony-rosa/projects/` with README.md + 3 seed files.
11. Create `anthony-rosa/skills/` with README.md + ai-engineer-progression.md.

### Phase D — Split the Misclassified Bridge into Two Single-Domain Bridges
12. Read the existing `Optimus Academy/apply-to-optimus/ai-influencer-revenue-pipeline.md` end-to-end.
    Identify which content is personal-revenue-stream (Anthony runs an AI influencer for TikTok
    Shop income) vs. which content is client-offering (Optimus sells AI-influencer-content as a
    service to clients).
13. **Rename** the existing file to `Optimus Academy/apply-to-optimus/ai-influencer-client-offering.md`
    and reframe its content to the client-offering angle ONLY. Update `applies-to::` to point at
    the appropriate Offerings target (likely `Offerings/01 Website Development/` content
    deliverable area). Add `#owner/optimus` to file frontmatter. Update `last-updated`.
14. **Create** `Optimus Academy/apply-to-anthony-rosa/ai-influencer-personal-revenue.md` with the
    personal-revenue content extracted in step 12. Frontmatter: same `concept::` link to the
    shared concept file (concept is the unifying point), new `applies-to::` pointing at
    `anthony-rosa/projects/ai-influencer.md`, `#owner/anthony-rosa` tag. `value-vector:: revenue`.
15. Both new bridges retain identical `source-references` arrays (same source taught both
    applications). Concept file (in `Optimus Academy/concepts/`) gets no edits — it stays the
    single shared concept; only its `applied-in:` Dataview view will start showing both bridges.
16. If the existing bridge's content is overwhelmingly one angle (e.g., 90% personal revenue,
    only a stub of client offering), the dominant-angle file gets the substantive content and
    the minority-angle file is created as a stub with TODO note for future enrichment — do NOT
    fabricate content to make the split look balanced.

### Phase E — Memory Capture
17. Save new project memory `project_two-domain-vault-model.md` documenting the elevation, the
    overlap principle, the bridge convention (one bridge per zone, shared concept as unifying
    point), the tag ownership schema. Add MEMORY.md index line.
18. Save new feedback memory `feedback_cross-domain-bridge-split.md` documenting the rule:
    when a concept applies to BOTH Optimus and Anthony Rosa domains, create TWO single-zone
    bridge files (not one multi-H2 file). The gtm-engineering multi-H2 pattern is for
    multiple applications WITHIN a single zone only.

### Phase F — Plan Preservation + Commit
19. Copy this plan file to `C:\Projects\Optimus Assets\anthony-rosa-peer-hub-elevation.md`.
20. Single atomic commit: plan + all changes together (Plan Preservation Rule).

---

## Concrete File Touch List

### Files edited (existing)
| File | Change |
|---|---|
| `optimus-system-guide.md` | Sections 3, 4, 6, 10, 13 — see Section Edits below |
| `00 — Empire Index/tag-schema.md` | Add `#owner/*` family after Status row (line ~23) |
| `00 — Empire Index/README.md` | Register 5th hub in any hub list/nav |
| `learn-prompt.md` | Zone table (lines 382-392), routing map (396-420), tag mapping (507-521) |
| `apply-to-optimus/README.md` | Add sibling-zone cross-reference at top, note shared mechanics |
| `CLAUDE.md` | Vault Organization section: hub count, bridge zones count, tag families list |
| `Optimus Academy/apply-to-optimus/ai-influencer-revenue-pipeline.md` | RENAMED to `ai-influencer-client-offering.md`; content reframed to client-offering angle only; `#owner/optimus` added |

### Files created (new)
| File | Purpose |
|---|---|
| `Optimus Academy/apply-to-anthony-rosa/README.md` | Bridge target taxonomy doc (mirrors apply-to-optimus/README.md) |
| `anthony-rosa/plans/.gitkeep` | Activates folder per CLAUDE.md reference |
| `anthony-rosa/investments/README.md` | Purpose + routing + scope boundary |
| `anthony-rosa/investments/crypto-thesis.md` | Overall investment philosophy |
| `anthony-rosa/investments/akt-tracker.md` | AKT position, thesis, price targets, daily-tracking ref |
| `anthony-rosa/investments/bitcoin-log.md` | BTC history + $25k → AKT decision rationale |
| `anthony-rosa/projects/README.md` | Personal automated revenue projects + graduation gates pattern |
| `anthony-rosa/projects/akash-network.md` | Technical research + cross-link to akt-tracker |
| `anthony-rosa/projects/ai-influencer.md` | TikTok Shop angle + cross-link to Optimus deliverable bridge |
| `anthony-rosa/projects/trading-bot.md` | Status, stack thesis, validation gates |
| `anthony-rosa/skills/README.md` | Boundary: skills/ = career intent; concepts in Academy. **First paragraph MUST disambiguate the "skills" namespace** — see Skills Namespace Disambiguation section below. |
| `anthony-rosa/skills/ai-engineer-progression.md` | Career skill goals + gates + why |
| `Optimus Academy/apply-to-anthony-rosa/ai-influencer-personal-revenue.md` | NEW — personal-revenue angle of the AI influencer concept; `#owner/anthony-rosa`; targets `anthony-rosa/projects/ai-influencer.md` |

### Memory updates (post-execution)
| File | Action |
|---|---|
| `memory/project_two-domain-vault-model.md` | NEW — captures the structural shift, overlap principle, ownership tag convention |
| `memory/MEMORY.md` | ADD index line for the new project memory |

---

## Section Edits — `optimus-system-guide.md`

**Section 3 (The 4 hubs + founder layer)** — REWRITE:
- Change heading to "The 5 hubs"
- Update hub table: add `anthony-rosa/` as 5th row alongside the four Optimus hubs
- Replace the "founder layer is not a fifth hub" paragraph with: "The two-domain model — Optimus
  is the LLC and product/service surface; Anthony Rosa is the personal layer holding career,
  investments, and personal automated revenue projects. Overlap is intentional: skills move
  between domains via bridge notes."
- Quote the saved `project_optimus-university.md` and `project_optimus-end-goal-2027-Q3.md` framing
  if relevant for grounding the overlap principle.

**Section 4 (The killer chain)** — MODERATE EDIT:
- Update chain narrative: "Source consumed → daily capture → concept synthesis → bridge to
  applicable hub(s) → improvement in that hub" (was: "→ apply-to-optimus bridge → offering
  improvement").
- Replace "one of the four Optimus offerings" with "any of the bridge zones (Optimus offerings,
  Optimus Inc, Optimus Academy tools, knowledge patterns/craft, OR anthony-rosa investments/
  projects/skills)".

**Section 6 (Promoting concepts)** — MODERATE EDIT:
- Update bridge-ready criteria to acknowledge two-domain routing.
- Document the cross-zone split rule explicitly: when a concept applies to both an Optimus zone
  AND `apply-to-anthony-rosa/`, create TWO single-zone bridge files (one per zone), each with
  ONE `#owner/*` tag, both linking to the same shared concept via `concept::`. The shared
  concept is the unifying point. The `gtm-engineering.md` multi-H2 precedent applies WITHIN a
  single zone only — never across zones.
- Cite the AI influencer split (`ai-influencer-client-offering.md` +
  `ai-influencer-personal-revenue.md`) as the canonical example of cross-domain split.

**Section 10 (Cross-cutting — Tag conventions)** — MINOR EDIT:
- **Update count to "8 tag families."** This is the truthful end-state count: schema currently has
  7 actual families (offering, layer, learning, applies-to, value-vector, stage, status — the
  Phase 1 audit confirmed value-vector exists in the schema even though it's not counted in
  CLAUDE.md or the system guide today), and this change adds `#owner/*` as the 8th. Stating
  anything other than 8 would be a fresh miscount. Add a one-line reconciliation note: "Count
  reconciled this change — value-vector was previously in the schema but uncounted in this
  file. Broader cross-vault tag-count audit remains a separate future change."
- Add `#owner/*` row to families table.
- Document: notes that span both domains carry both `#owner/optimus` AND `#owner/anthony-rosa`.

**Section 13 (Maintenance protocol)** — MINIMAL EDIT:
- Add this restructure to the example list of past structural changes once committed.

---

## Section Edits — `tag-schema.md`

Insert after the Status family row (~line 23), before "Common tag combinations":

```markdown
| Owner | `#owner/optimus` `#owner/anthony-rosa` | Domain ownership: Optimus LLC vs. Anthony Rosa personal layer. Notes spanning both get both tags. |
```

Update the count statement in the schema's intro if there is one.

---

## Section Edits — `learn-prompt.md`

**Lines 382-392 (5-zone table):** Add 6th row:
```
| `apply-to-anthony-rosa/<area>/` | Anthony Rosa personal hub: investments/, projects/, skills/ | Folder created per this plan |
```

**Lines 396-420 (routing map):** Add routing rules:
- Source about crypto/trading/investing → `apply-to-anthony-rosa/investments/`
- Source about a personal revenue project (trading bot, AI influencer personal angle, TikTok Shop personal) → `apply-to-anthony-rosa/projects/`
- Source about career-skill progression (AI engineering pathway) → `apply-to-anthony-rosa/skills/`
- A single source CAN bridge to BOTH `apply-to-optimus/` AND `apply-to-anthony-rosa/` when the skill applies to both domains (e.g., AI influencer captured today). Same multi-H2 pattern as gtm-engineering.md.

**Lines 507-521 (tag mapping):** Add tag rows:
```
| anthony-rosa/investments/<file> | `#applies-to/anthony-rosa/investments` |
| anthony-rosa/projects/<file>    | `#applies-to/anthony-rosa/projects`    |
| anthony-rosa/skills/<file>      | `#applies-to/anthony-rosa/skills`      |
```

Plus add `#owner/anthony-rosa` to bridge frontmatter when the bridge target is in the personal hub.

---

## Section Edits — `CLAUDE.md`

**Vault Organization (Multi-Offering) section:**
- Update "The 4 hubs" → "The 5 hubs"
- Add `anthony-rosa/` row to hub list with one-line description: "personal layer — career,
  investments, automated personal revenue projects, skill goals. Overlaps with Optimus via
  bridge notes."
- Update `/learn` description: "FIVE zones" → "SIX zones" and add 6th zone path.
- **Tag families list: state explicitly as 8 families** with the full list:
  `#offering/*`, `#layer/*`, `#learning/*`, `#applies-to/*`, `#value-vector/*`, `#stage/*`,
  `#status/*`, `#owner/*`. (CLAUDE.md previously listed 6 — this change reconciles both the
  addition of `#owner/*` AND the previously-uncounted `#value-vector/*` in a single accurate
  end-state. Same reconciliation note as system guide Section 10.)
- Add a "Two-domain model" subsection or paragraph under Vault Organization describing the
  ownership distinction and the overlap-via-bridges principle.
- **Add a one-sentence skills-namespace disambiguation** when describing the `anthony-rosa/`
  hub: "`anthony-rosa/skills/` holds Anthony's personal career skill development (Python,
  LangChain, FastAPI, Personaplex, etc.) — distinct from Claude Code skills at `.claude/skills/`
  and from Optimus build skill instructions used by Claude tools."

---

## Migration: Split `ai-influencer-revenue-pipeline.md` into Two Single-Domain Bridges

**Why split, not multi-H2:** The two-domain model is expressed structurally — each bridge file
lives in ONE domain's apply-to-X folder, with ONE `#owner/*` tag. The cross-domain relationship
is expressed via the SHARED concept file that both bridges link to via `concept::` frontmatter.
This keeps `#owner/*` Dataview queries clean and makes the two-domain architecture visible in
the file tree itself. The `gtm-engineering.md` multi-H2 precedent applies WITHIN a single zone
(multiple H2s, all in `apply-to-optimus/`); cross-zone applications get separate files.

### Step-by-step

**1. Read the existing file end-to-end** at
`Optimus Academy/apply-to-optimus/ai-influencer-revenue-pipeline.md`. Audit which parts of its
content are personal-revenue-stream framing vs. client-offering framing. (Per Phase 1 audit, the
file currently routes to `Optimus Inc/operations/revenue-streams/` — strongly suggests
content is dominantly personal-revenue framed and was misclassified.)

**2. Rename the existing file** to
`Optimus Academy/apply-to-optimus/ai-influencer-client-offering.md`.
- Reframe content to client-offering angle ONLY (Optimus sells AI-influencer-style content
  creation as a service to clients).
- Update `applies-to::` to point at the appropriate Offerings target — likely
  `Offerings/01 Website Development/` content deliverable area, or whichever Offering the
  service maps into. Do NOT keep `Optimus Inc/operations/revenue-streams/` as the target —
  that folder is mis-scoped under the new model.
- Add `#owner/optimus` to file frontmatter tags.
- Bump `last-updated`.
- If the existing content is overwhelmingly personal-revenue framed, this file becomes a stub
  with a TODO note for future enrichment when the client offering is genuinely productized.
  Do NOT fabricate balance.

**3. Create new file**
`Optimus Academy/apply-to-anthony-rosa/ai-influencer-personal-revenue.md`.
- Frontmatter: same `concept::` link as the original (shared concept), `applies-to::`
  → `[[../../anthony-rosa/projects/ai-influencer]]`, `#owner/anthony-rosa`,
  `#status/active`, `#applies-to/anthony-rosa/projects`.
- Same `source-references` array as the renamed file (same source taught both applications).
- Content: the personal-revenue framing — Anthony's TikTok Shop revenue stream, avatar AI
  + voice + Claude orchestration as a personal automated pipeline.
- `value-vector:: revenue`.
- Bump `last-updated`.

**4. Concept file gets NO edits.** The shared concept in `Optimus Academy/concepts/` stays
single — it's the unifying point. Its `applied-in:` Dataview view will simply now show both
bridges in its results.

**5. No fabricated content.** If one angle's content is thin in the original, the corresponding
new file is created as a stub with a clear TODO. Better honest than balanced-looking.

---

## Skills Namespace Disambiguation (Required First Paragraph of `anthony-rosa/skills/README.md`)

The word "skills" appears in three different vault namespaces and confusing them will route
content to the wrong place in future `/learn` sessions. The README at `anthony-rosa/skills/README.md`
MUST open with this disambiguation (exact wording or close paraphrase, not optional):

> **Scope of this folder.** `anthony-rosa/skills/` holds Anthony Rosa's personal career skill
> development as an AI engineer — Python production-grade practice, LangChain, FastAPI, Pydantic,
> Anthropic SDK fluency, Personaplex audio, and similar progression goals and roadmaps. These
> are career intent and learning targets, not knowledge content.
>
> **What this folder is NOT.** This folder is distinct from:
> - **Claude Code skills** at `.claude/skills/` — those are tool/instruction files Claude Code
>   loads when invoking `/<skill-name>`. Different system, different purpose.
> - **Optimus build skill instructions** referenced by Claude tools during builds (the
>   skill-creator system, frontend-design, etc.) — those are Claude-executable instructions,
>   not human career-progression notes.
> - **Optimus Academy concepts** — those are the actual knowledge content (the "what" of a
>   skill: how Pydantic v2 works, what FastAPI dependency injection does). Concepts are
>   ingested via `/learn` and live in `Optimus Academy/concepts/`. This folder holds the
>   "why I'm learning this and where I am on the path"; concepts hold the substance.
>
> **Naming pattern for files in this folder:** `<skill-area>-progression.md`
> (e.g., `ai-engineer-progression.md`, `python-progression.md`). Each file:
> goals → gates / milestones → current status → why this matters for career.

This block goes verbatim (or near-verbatim with phrasing tweaks for tone) at the top of the
README before any other content. Without it, a future session will eventually create
`anthony-rosa/skills/some-claude-skill.md` thinking it's a Claude Code skill home, and the
namespace will fragment.

---

## Verification (How to Test End-to-End)

Once execution completes:

1. **Hub elevation visible:**
   ```
   ls "c:\Projects\Optimus Assets\anthony-rosa\"
   ```
   Should show: north-star.md, ai-engineer-roadmap.md, portfolio-standards.md, wins.md, journal/,
   **plans/** (NEW), **investments/** (NEW), **projects/** (NEW), **skills/** (NEW).

2. **Bridge zone exists:**
   ```
   ls "c:\Projects\Optimus Assets\Optimus Academy\apply-to-anthony-rosa\"
   ```
   Should show: README.md.

3. **System guide declares 5 hubs (not 4):**
   ```
   grep -n "5 hubs\|five hubs" "c:\Projects\Optimus Assets\optimus-system-guide.md"
   grep -n "founder layer is not a fifth hub" "c:\Projects\Optimus Assets\optimus-system-guide.md"
   ```
   First grep returns matches; second grep returns nothing (the denial sentence was inverted).

4. **Tag schema has #owner/* family:**
   ```
   grep -n "#owner/" "c:\Projects\Optimus Assets\00 — Empire Index\tag-schema.md"
   ```
   Returns at least 2 matches (`#owner/optimus`, `#owner/anthony-rosa`).

5. **`/learn` knows about the 6th zone:**
   ```
   grep -n "apply-to-anthony-rosa" "c:\Projects\Optimus Assets\learn-prompt.md"
   ```
   Returns multiple matches (zone table, routing map, tag mapping).

6. **CLAUDE.md updated:**
   ```
   grep -n "SIX zones\|6 zones\|five hubs\|5 hubs" "c:\Projects\Optimus Assets\CLAUDE.md"
   grep -n "FIVE zones" "c:\Projects\Optimus Assets\CLAUDE.md"
   ```
   First returns matches; second returns no match.

7. **AI influencer bridge split correctly into two single-domain files:**
   ```
   ls "c:\Projects\Optimus Assets\Optimus Academy\apply-to-optimus\ai-influencer-client-offering.md"
   ls "c:\Projects\Optimus Assets\Optimus Academy\apply-to-anthony-rosa\ai-influencer-personal-revenue.md"
   ls "c:\Projects\Optimus Assets\Optimus Academy\apply-to-optimus\ai-influencer-revenue-pipeline.md"
   ```
   First two exist. Third does NOT exist (renamed). Both new files declare the SAME `concept::`
   link in frontmatter (shared concept). Each declares ONE `#owner/*` tag (not both).

8. **Smoke test the `/learn` skill** with a hypothetical personal-domain source (verbal walk-through,
   not actual /learn run): "if I capture a YouTube video on Akash supply economics today, where does
   the bridge land?" Expected answer: `apply-to-anthony-rosa/investments/` (or projects/ if it's
   about deployment patterns). Walk through the routing-map decision tree to confirm the new zone
   is reachable.

9. **Akash strict-scoping memory still honored:**
   ```
   grep -rn "Akash" "c:\Projects\Optimus Assets\Offerings\02 AI Agents\01 Chat Assistant" "c:\Projects\Optimus Assets\Offerings\02 AI Agents\03 Marketing Team"
   ```
   Should return ZERO matches (Akash named only in the three approved files; the personal hub
   references don't leak into Optimus product docs).

10. **Plan preserved:**
    ```
    ls "c:\Projects\Optimus Assets\anthony-rosa-peer-hub-elevation.md"
    ```
    Exists.

11. **Tag count states "8 tag families" in both files:**
    ```
    grep -n "8 tag families" "c:\Projects\Optimus Assets\optimus-system-guide.md"
    grep -n "8 tag families\|eight tag families" "c:\Projects\Optimus Assets\CLAUDE.md"
    grep -n "6 tag families\|7 tag families" "c:\Projects\Optimus Assets\optimus-system-guide.md" "c:\Projects\Optimus Assets\CLAUDE.md"
    ```
    First two return matches; third returns NO matches (no stale counts left).

12. **Skills namespace disambiguation present in README:**
    ```
    grep -n "Claude Code skills\|distinct from\|.claude/skills" "c:\Projects\Optimus Assets\anthony-rosa\skills\README.md"
    ```
    Returns multiple matches (the disambiguation block is in place).

13. **CLAUDE.md mentions the skills-namespace distinction:**
    ```
    grep -n "anthony-rosa/skills" "c:\Projects\Optimus Assets\CLAUDE.md"
    ```
    Returns matches that include disambiguation context (not just a folder reference).

14. **Single atomic commit** — `git log -1 --stat` shows the plan file + all touched files in one
    commit per Plan Preservation Rule.

---

## Critical Files for Reference During Execution

- `optimus-system-guide.md` — sections to edit, exact line ranges from Phase 1 audit
- `learn-prompt.md` lines 382-392, 396-420, 445-453, 507-521 — exact patches
- `Optimus Academy/apply-to-optimus/README.md` lines 35-41, 79-93 — sibling-doc structure to mirror
- `Optimus Academy/apply-to-optimus/gtm-engineering.md` — multi-H2 multi-application pattern reference
- `00 — Empire Index/tag-schema.md` line 23 — insertion point
- `CLAUDE.md` lines 134-180 (Vault Organization section) + line 140 ("FIVE zones") — touch points

---

## Memory Captures (Post-Execution)

After commit, save:

**`memory/project_two-domain-vault-model.md`** (project type)
- Two-domain model: Optimus = LLC/products, Anthony Rosa = personal/investments/career
- Anthony Rosa elevated to 5th peer hub (was subordinate founder layer)
- Overlap is the asset, mediated by bridge notes
- `#owner/*` tag family for cross-domain queries
- 6 `/learn` bridge zones (was 5)
- Akash strict-scoping memory continues to apply: bullish in personal hub, neutral in Offerings
- AI influencer is the canonical multi-domain skill example, split across two single-domain
  bridges (personal revenue + client offering) sharing one concept

**`memory/feedback_cross-domain-bridge-split.md`** (feedback type)
- **Rule:** when a concept applies to BOTH Optimus and Anthony Rosa domains, create TWO
  single-zone bridge files (not one multi-H2 file). Each file declares ONE `#owner/*` tag.
  Both files link to the same shared concept via `concept::` — the concept is the unifying
  point.
- **Why:** keeps `#owner/*` Dataview queries clean. Makes the two-domain architecture visible
  in the file tree. Each bridge stays single-domain; cross-domain relationship is encoded via
  the shared concept they both link back to.
- **How to apply:** `gtm-engineering.md` multi-H2 precedent applies WITHIN a single zone only
  (e.g., two H2s both inside `apply-to-optimus/` for a single concept that has multiple
  Optimus applications). Cross-zone applications get separate files. Source-references arrays
  in both files are typically identical (same source taught both applications).

**`memory/MEMORY.md`** — index lines added for both new memories.

---

## Risks & Mitigations

| Risk | Mitigation |
|---|---|
| `/learn` skill misroutes after change | Smoke test with verbal walk-through (verification step 8) before next real /learn call |
| `optimus-system-guide.md` update introduces inconsistency vs. CLAUDE.md | Both files updated in same commit; verification grep step 3 + 6 catches drift |
| Akash personal bullishness leaks into Optimus product docs | Verification step 9 + saved memory `akash-strict-scoping.md` is referenced in projects/akash-network.md frontmatter |
| AI influencer split misallocates content between the two bridges | Step 1 reads existing file end-to-end before deciding which angle dominates; if one angle is stub-only, that file is a stub with TODO — no fabrication |
| AI influencer split breaks `applied-in:` queries on the concept file | Both new bridges declare the SAME `concept::` link; concept file gets no edits; Dataview just shows both bridges in its applied-in view |
| `anthony-rosa/plans/` empty .gitkeep gets overlooked | Listed in verification step 1 |
| Tag count discrepancy (CLAUDE.md says 6, schema has 7+1) | Plan note: correct CLAUDE.md to "7 → 8" in same change. Existing 6-vs-7 mismatch noted but not fully audited (out of scope). |

---

## Out-of-Scope Follow-Ups (Future Plans)

- Full audit of tag family count consistency across CLAUDE.md, system guide, schema (existing
  6-vs-7 mismatch predates this plan).
- Populate seed files with substantive content (this plan creates frontmatter + scaffold only).
- Bridge migrations of any other Optimus Inc bridges that should actually be anthony-rosa
  bridges (audit pass after restructure lands).
- Optimus University curriculum or branding work (2027-2028 horizon per saved memory).
- Productization gates for trading bot / AI influencer (separate decisions later).
