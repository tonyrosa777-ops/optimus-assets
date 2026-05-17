# Pattern: Sweep methodology after tool replacement
**Category:** Workflow / Documentation Hygiene
**First used:** Goddu Imprint — 2026-05-17

## What
When replacing a tool or workflow gate referenced across multiple Optimus toolkit files (project-prime.md, build-checklist.md, website-build-template.md, end-to-end-workflow.md, CLAUDE.md, pattern docs, agent files, audit artifacts), the **entry-point swap is not sufficient**. A grep-driven sweep across all operative references is mandatory before the swap is "done." Otherwise, the next client build will hit a stale supporting doc that points back to the replaced tool.

## When to Use
Whenever any of these change:
- A slash command name (e.g., `/ultrareview` → `/optimus-review`)
- A workflow gate's tool of choice (e.g., `/optimus-review` someday replaced with something else)
- A canonical file path (e.g., `knowledge/patterns/<old-name>.md` renamed to `<new-name>.md`)
- A workflow stage's invocation pattern (e.g., new env var, new prompt format)
- A pattern file or agent file that's referenced from multiple supporting docs

Mandatory when the entry-point change is to a high-traffic file (project-prime.md Stage section, CLAUDE.md absolute rule, pre-launch-auditor agent).

## How

### Step 1 — Replace the entry point

Update the most visible reference first — the file the orchestrator reads directly (project-prime.md Stage section, CLAUDE.md rule, agent prompt). Commit this change separately so the swap is git-bisectable.

### Step 2 — Grep operative references

```bash
# In each repo that may reference the old tool/path:
cd "C:\Projects\Optimus Assets"
grep -rni "old-tool-name\|old-pattern-name" --include="*.md" .

# Also Goddu (or whichever client repo you're in):
cd "c:\Projects\Steve-Goddu"
grep -rni "old-tool-name\|old-pattern-name" --include="*.md" .
```

Read each match in context. Classify each as:

| Category | What it looks like | Action |
|---|---|---|
| **Operative** | "Run `/old-tool-name`", "see `knowledge/patterns/<old-name>.md`", "use the OLD-TOOL gate" — instructions to a future caller | Update to new tool/name |
| **Historical** | "Replaces `/old-tool-name`", "originally introduced as `/old-tool-name` 2026-04-17", commit message context | Keep — correct migration documentation |
| **Stale audit artifact** | An old Stage 1H or Stage 1J output that pre-dates the swap | Update to reflect resolved state, not the old tool's name |

### Step 3 — Update operative references

For each operative reference, edit in place. Common files for Optimus tool/gate swaps:
- `project-prime.md` (vault master) + every client repo's `.claude/commands/prime.md`
- `build-checklist.md`
- `website-build-template.md`
- `end-to-end-workflow.md`
- `CLAUDE.md` (vault and per-client copies)
- `.claude/agents/launch/pre-launch-auditor.md` (SECTION X handoff blocks especially)
- `knowledge/patterns/<related-pattern>.md` (cross-references)
- `pre-launch-audit.md` (per-client audit artifacts, if pre-dating the swap)

### Step 4 — Rename pattern files for tool-agnostic future-proofing

If the OLD tool's name was in a pattern filename (`knowledge/patterns/ultrareview-as-pre-launch-gate.md`), rename to tool-agnostic (`stage-1j-pre-launch-gate.md`). The pattern describes the **gate**, not the tool — surviving tool changes.

```bash
# Use git mv for proper history tracking (or Write new + git rm old)
cd "C:\Projects\Optimus Assets"
git mv knowledge/patterns/ultrareview-as-pre-launch-gate.md knowledge/patterns/stage-1j-pre-launch-gate.md
# Then update the pattern's content to describe the gate concept + name the current tool
```

### Step 5 — Rename handoff tokens for tool-agnostic future-proofing

If agent files emit handoff blocks with tool-specific tokens (`HANDOFF-TO-ULTRAREVIEW`), rename to stage-specific (`HANDOFF-TO-STAGE-1J`). Surviving tool changes again.

Update everywhere the token appears:
- The agent file that emits the block
- The orchestrator that reads the block (project-prime.md Stage section)
- Validation rules in the agent's own Output schema
- Documentation pattern docs that quote the block format

### Step 6 — Commit per repo

Two commits typically: one per repo. Each commit message lists the operative changes vs the file deletions/renames, and references the entry-point swap commit hash.

## Key Rules
- **Entry-point swap alone is not "done."** A user can ask "is it replaced everywhere it applies?" and you must be able to answer YES truthfully, citing the sweep.
- **Grep is the gate.** Visual code review of supporting docs misses references. `grep -rni` against the old token across the vault and per-client repo is the only reliable detection.
- **Categorize before editing.** Historical references documenting the migration are correct context — stripping them loses the rationale. Only operative references get updated.
- **Rename for tool-agnostic future-proofing.** Pattern files and handoff tokens that name the specific tool become stale on the next swap. Rename to stage-specific names so a future tool change is content-only.
- **Run the sweep in a single session.** If you defer the sweep, the next client build that hits one of the un-updated supporting docs will follow stale instructions. The swap effectively didn't happen until the sweep completes.

## Reuse Condition
Every Optimus toolkit change that replaces a tool, gate, or canonical file path. Specifically:
- Future Stage 1J tool change (replacing `/optimus-review` with something else)
- Any agent name change
- Any pattern file rename
- Any CLAUDE.md rule rewrite that references specific tools
- Any future workflow stage renumbering

## Goddu Imprint trace
- 2026-05-17 morning: built `/optimus-review` skill + updated Stage 1J entry point in project-prime.md (vault + Goddu)
- Mid-day: user asked "so ultrareview in the optimus workflow has been replaced officially everywhere it applies with optimus review?"
- Honest answer: NO — only the entry point. Audit revealed 11 vault files + 7 Goddu files still referenced `/ultrareview` operatively.
- Sweep applied:
  - Vault commit `73c89ff` — 8 files (pre-launch-auditor.md SECTION 12 + HANDOFF templates, build-checklist.md, website-build-template.md, end-to-end-workflow.md, CLAUDE.md, opus-4-7-prompt-tuning.md link, new stage-1j-pre-launch-gate.md, deleted ultrareview-as-pre-launch-gate.md)
  - Goddu commit `1dea5dd` — 5 files (CLAUDE.md, website-build-template.md, pre-launch-audit.md stale HANDOFF block, progress.md forecast line, deleted stale project-prime.md root copy)
- Renamed `HANDOFF-TO-ULTRAREVIEW` → `HANDOFF-TO-STAGE-1J` everywhere for tool-agnostic future-proofing
- Renamed `ultrareview-as-pre-launch-gate.md` → `stage-1j-pre-launch-gate.md` for same reason

## Related
- Pattern [[stage-1j-pre-launch-gate]] — the renamed pattern file
- [[../../optimus-review-skill.md]] — the replacement tool's plan
- Pattern #46 (vault build-log) — No deferred cleanup rule (companion discipline)
