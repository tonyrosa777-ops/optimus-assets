# /ultrareview as Pre-Launch Gate

**Established:** 2026-04-17 (Opus 4.7 retune)

## What /ultrareview is

A Claude Code 4.7 slash command. Dedicated review session that reads through working-tree changes and flags bugs + design issues a careful code reviewer would catch. Pro/Max plans get 3 free per session.

## When it runs in the Optimus workflow

**Phase 1J — after Phase 1I pre-launch-auditor AND Section 11 multi-breakpoint browser audit both PASS.** This is the final gate before a demo URL goes to the client.

Order:
1. Phase 1I pre-launch-auditor (file-level checks) → must pass
2. Section 11 multi-breakpoint Playwright browser audit → must pass
3. **Phase 1J `/ultrareview` → must pass**
4. Demo URL to client

If any of the three fail, the next does not run. Launch is blocked until resolved.

## Invocation

From the project directory:
```
/ultrareview
```

Runs against the full working tree diff since the last known-good commit (typically the last launched state).

## Graceful degradation

`/ultrareview` is not guaranteed available on every Claude Code session. Three failure modes + handling:

### Mode 1 — Command not available in this Claude Code version
Symptom: `/ultrareview` returns "unknown command" or no response.

Handling:
1. Log to `pre-launch-audit.md §Ultrareview Findings`:
   ```
   Run date: <date>
   Result: SKIPPED — /ultrareview not available in this Claude Code session
   Fallback: Manual PR review required before demo URL sent to client
   ```
2. Log to progress.md: "Stage 1J SKIPPED (manual PR review required)."
3. Advance to Phase 2 with WARN — do NOT block indefinitely.

### Mode 2 — Free-tier quota exhausted
Symptom: Pro/Max plans get 3 free `/ultrareview` per session. If quota hit, command returns quota error.

Handling:
1. Log to `pre-launch-audit.md §Ultrareview Findings`:
   ```
   Run date: <date>
   Result: PARTIAL — free-tier quota exhausted after <N> runs this session
   Fallback: Remaining review done manually OR deferred to next session start (quota resets)
   ```
2. If the build is time-sensitive (client demo tonight): proceed to Phase 2 with WARN + manual review note.
3. If not time-sensitive: defer demo URL send to next session and re-run `/ultrareview` after quota reset.

### Mode 3 — Timeout (>20 minutes)
Symptom: `/ultrareview` runs past reasonable budget on large working trees.

Handling:
1. Terminate the command at 20 minutes.
2. Log to `pre-launch-audit.md §Ultrareview Findings`:
   ```
   Run date: <date>
   Result: TIMEOUT after 20 minutes
   Fallback: Manual PR review (divide working tree by directory, spot-check)
   ```
3. Advance to Phase 2 with WARN.

Across all three modes: NEVER block the launch chain indefinitely on a review tool that's unavailable. WARN, log, and proceed with a manual-review backstop. The cost of a stuck build chain is higher than the cost of one under-reviewed demo.

## Output triage — BUG / DESIGN / PASS

`/ultrareview` returns findings classified by severity.

### BUG-severity findings — BLOCKS LAUNCH
Must be resolved before the demo URL is sent. Examples:
- Logic errors, wrong variable references, null-access risk
- Unhandled promise rejection, missing try/catch at system boundary
- Regression in tested behavior
- Security vulnerability
- Clear data-loss risk

Resolution: fix the bug, re-run `/ultrareview` to confirm zero BUG findings, then advance to demo.

**Fix-owner routing:**
- `/data/*.ts` (copy, site data, quiz data): delegate fix to content-writer agent
- `/components/Hero*.tsx`, `/components/*Canvas.tsx`, animation files: delegate fix to animation-specialist agent
- `/app/sitemap.ts`, `/app/robots.ts`, `/app/**/opengraph-image.tsx`, `JsonLd.tsx`, schema markup: delegate fix to seo-aeo-specialist agent
- `/app/globals.css`, layout, design tokens: orchestrator fixes inline (no agent)
- `/app/api/**` routes: orchestrator fixes inline
- `/lib/*`, utilities, generic helpers: orchestrator fixes inline

After fixes are applied, re-run `/ultrareview` to confirm zero BUG findings. Budget 1 re-run; if BUG findings persist after fix + re-run, escalate to Anthony for manual review rather than burning more free-tier runs.

### DESIGN-severity findings — REVIEW OR WAIVE
Reviewed with Anthony. Either fix or explicitly waive with a one-line rationale.
Examples:
- Pattern deviation from existing code
- Missing accessibility attribute (ARIA, alt text) — fix these usually
- Unconventional structure that isn't wrong but is worth flagging
- Minor UX inconsistency

If waived: log the waiver in `pre-launch-audit.md §Ultrareview Findings` with the one-line rationale. Waivers compound into technical debt — sparingly used.

**Volume thresholds:**
- DESIGN count 0-5: proceed with review session (~5 min).
- DESIGN count 6-15: proceed with focused review session (~15 min). Pre-triage into categories before presenting to Anthony.
- DESIGN count > 15: signal that the build quality needs cleanup. Return one phase (to content-writer, animation-specialist, or seo-aeo-specialist depending on cluster) before resuming Stage 1J.

**Waiver policy:** a DESIGN finding waived on this project is NOT automatically waived on future projects. Each build starts fresh. If a pattern is consistently waived across 3+ builds, promote to an explicit CLAUDE.md rule or knowledge/patterns/ entry so it stops surfacing as a finding.

### PASS with no findings — LAUNCH CLEARED
Log "`/ultrareview` PASSED at HEAD=<sha>" in pre-launch-audit.md §Ultrareview Findings and proceed to demo URL send.

## Logging format

All findings (BUG, DESIGN, or PASS) land in `pre-launch-audit.md` under the new section `§Ultrareview Findings`:

```
## §Ultrareview Findings

**Run date:** 2026-04-17
**HEAD sha:** abc1234
**Result:** BUG=2 DESIGN=3 PASS=N/A

### BUG findings
1. [file:line] — <finding> — <resolution commit sha>
2. ...

### DESIGN findings
1. [file:line] — <finding> — FIXED in <sha> | WAIVED: <rationale>
2. ...
```

## Why this gate matters

The file-level auditor catches structural gaps. The browser audit catches layout/console issues. `/ultrareview` catches the subtle code-review layer: pattern inconsistencies, easy-to-miss bugs, accessibility gaps. All three find different things. Pre-launch needs all three.

## Related patterns
- `knowledge/patterns/end-of-build-multi-breakpoint-browser-audit.md` — the Section 11 browser audit that runs before this one.
- `knowledge/patterns/opus-4-7-prompt-tuning.md` — the 4.7 retune that added this gate.

## Status
ACTIVE since 2026-04-17. Used on every project from Witt's Restoration onward.
