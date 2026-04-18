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

### DESIGN-severity findings — REVIEW OR WAIVE
Reviewed with Anthony. Either fix or explicitly waive with a one-line rationale.
Examples:
- Pattern deviation from existing code
- Missing accessibility attribute (ARIA, alt text) — fix these usually
- Unconventional structure that isn't wrong but is worth flagging
- Minor UX inconsistency

If waived: log the waiver in `pre-launch-audit.md §Ultrareview Findings` with the one-line rationale. Waivers compound into technical debt — sparingly used.

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
