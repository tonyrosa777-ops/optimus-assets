---
name: retro
description: Post-project retrospective — populate knowledge/retrospectives/<slug>.md and update knowledge/build-log.md with errors, patterns, and workflow improvements discovered during the project.
effort: high
---

# /retro — Post-Project Retrospective

## Usage

Run from inside the project folder:

```
/retro            # infer slug from current working directory folder name
/retro <slug>     # explicit slug override (use when folder name doesn't match the desired slug)
```

The skill infers the project path from the CWD. It reads the project's `progress.md`, `CLAUDE.md`, and `git log` to source errors, patterns, and workflow improvements. Output lands in `knowledge/retrospectives/<slug>.md` and updated rows in `knowledge/build-log.md`.

**When to invoke:** After project close (demo delivered, revisions complete, payment received) — this is a REQUIRED close step, not optional. Skipping /retro means the cross-project knowledge base doesn't learn from this build.

## Role

Run after a client project closes (demo delivered, revisions complete, payment received). Synthesize the project's lifecycle into a retrospective entry and update the cross-project knowledge base so future builds inherit what was learned.

## When to invoke

- Explicit `/retro` command after a client project reaches "closed" status
- Referenced by Phase 5 close in end-to-end-workflow.md
- After `/gsd:complete-milestone` or equivalent close command

## Required reading (in order)

1. The project's own `CLAUDE.md` (for filled `[BUSINESS_NAME]`, `[DOMAIN]`, client context)
2. The project's `progress.md` (the full session log — every subtask update)
3. Git log of the project repo (`git log --oneline --all`) to identify which commits represent errors resolved vs. features shipped
4. `c:\Projects\Optimus Assets\knowledge\build-log.md` — understand current Error Encyclopedia / Build Patterns / Workflow Improvements format
5. 2-3 existing retrospectives under `c:\Projects\Optimus Assets\knowledge\retrospectives\` to match tone and structure

## Inputs

- Project slug (e.g. `placed-right-fence`) — used for the retrospective filename
- Project path on disk — to read progress.md and git log

## Task

### Slug resolution

If invoked without an explicit slug:
1. Read the basename of the current working directory.
2. Lowercase, replace spaces and underscores with hyphens, strip non-alphanumeric-except-hyphen.
3. Use that as the slug for `knowledge/retrospectives/<slug>.md`.

If invoked with an explicit slug argument, use that literally (do not transform).

If slug resolution produces a filename that already exists at `knowledge/retrospectives/<slug>.md`:
- If the file was last modified > 14 days ago: append to it (project continuation).
- If the file was modified recently: warn the user, request explicit `<slug>` argument to disambiguate.

Produce four deliverables. Work them in order.

### 1. Enumerate errors newly encountered

From progress.md + git log, identify every error that required a fix commit beyond the initial scaffold. For each:
- Short problem title
- Where it manifested (file, browser, deploy, phase)
- Root cause in one sentence
- Resolution summary in one sentence
- Whether it's a one-off vs. likely to recur on future builds

For errors likely to recur (judgment call based on root-cause pattern), create a new entry file at `c:\Projects\Optimus Assets\knowledge\errors\<slug-of-problem>.md` using the format of existing error entries. Do NOT create entries for one-off project-specific errors (e.g. a specific client's typo).

Then add a row to the Error Encyclopedia table in `build-log.md` for each new entry, using the next available Error # (read current max from the table).

**Hallucination safety:** Every error row must trace to a real fix commit in the project repo OR a real entry file you just created. Do not invent errors that were not encountered. If progress.md is sparse and git log is clean, the project may legitimately have zero novel errors — output zero and note why.

### 2. Enumerate patterns newly discovered

From progress.md, identify reusable patterns that emerged in this build. Candidates:
- New component architectures that weren't in website-build-template.md
- New integration patterns (Sanity role, GHL hook, Resend config, fal.ai prompt approach)
- New animation/interaction patterns
- New content-writing or tone discoveries
- New workflow adjustments Anthony made mid-project

For each pattern likely to apply on future builds:
- Add a row to the Build Patterns table in `build-log.md` (use next available Pattern #).
- Create a pattern doc at `c:\Projects\Optimus Assets\knowledge\patterns\<slug>.md` using the existing pattern-doc format (trigger condition, problem solved, implementation outline, file examples, related patterns).

**Hallucination safety:** Every pattern row must trace to a real implementation in the project repo. Do not invent patterns that were not actually used.

### 3. Write the retrospective narrative

Create `c:\Projects\Optimus Assets\knowledge\retrospectives\<slug>.md` with this structure:

```
# <BUSINESS_NAME> — Retrospective

**Launched:** <date>
**Duration:** <days from kickoff to demo>
**Tier sold:** <Starter / Pro / Premium>
**Status:** <closed-paid / closed-revising / closed-churned>

## One-paragraph summary
<What the build was, who the client is, what the demo looked like at close.>

## What went right
<2-4 bullets — patterns to repeat>

## What went wrong
<2-4 bullets — errors to not repeat, process friction, miscommunications>

## Surprises
<Things that weren't in the intake, weren't in market research, but mattered>

## New knowledge added
- Errors: <list of error entries added in Task 1>
- Patterns: <list of pattern entries added in Task 2>

## Workflow improvement candidates
<If this project revealed a repeatable gap in the workflow itself — not a client-specific issue — list the proposed change with the specific file to edit: CLAUDE.md, website-build-template.md, a specific agent file, etc. Orchestrator reviews these; Anthony decides which to apply.>
```

### 4. Update the Workflow Improvements table

In `build-log.md`, if Task 3 surfaced workflow improvement candidates that are actually adopted (vs. just noted), add a row per adoption with: date, change, trigger (what project surfaced it).

## Output

Three files touched/created:
- `knowledge/retrospectives/<slug>.md` (NEW)
- `knowledge/build-log.md` (modified — Error Encyclopedia table, Build Patterns table, Workflow Improvements table)
- 0+ new files under `knowledge/errors/` and `knowledge/patterns/` (one per reusable error/pattern)

## Constraints

- Work from evidence only. progress.md + git log + retrospective format are the source material. Do not invent patterns that weren't used or errors that weren't encountered.
- Error and pattern entries must be genuinely cross-project applicable. One-off client-specific incidents stay in the retrospective narrative, NOT in the Encyclopedia.
- Do not modify the project's own files (site.ts, components, etc.). This agent only writes to the Optimus Assets knowledge base.
- Pattern # and Error # must be next-available integers from the existing build-log.md tables — do not overwrite.

## Validation

Orchestrator checks before unblocking:
- `knowledge/retrospectives/<slug>.md` exists and is non-empty
- build-log.md has N new rows where N matches the count of new error entries + new pattern entries claimed
- Every claimed new error entry file exists under `knowledge/errors/`
- Every claimed new pattern entry file exists under `knowledge/patterns/`

## Handoff

Report:
- Retrospective file path
- Count of new errors added + their titles
- Count of new patterns added + their titles
- Count of workflow improvements proposed (adopted vs. just-noted)
- Any `[MISSING-DATA: <what>]` flags if progress.md was sparse
