# Pattern: Iterate-to-clean N-run code review
**Category:** Workflow / Quality Gate
**First used:** Goddu Imprint — 2026-05-17

## What
At a code review gate (`/optimus-review` or any multi-agent review), the gate is not "PASS once" — it's "PASS on the latest commit." Every BUG fix batch is followed by a re-run on the fix commit itself. The clean run is the only acceptable Stage 1J close state. Goddu Imprint cleared in 3 runs: 7 BUGs → 3 NEW BUGs → 0 BUGs.

## When to Use
Every `/optimus-review` invocation at Stage 1J. **Always re-run after a fix batch — never close on the first run's PASS-after-fixes claim** unless the fix batch was a single-line trivial change.

Specifically applies when:
- Run-N surfaces BUGs that require fix commits
- Fix commit touches 3+ files OR introduces new API/security surface
- Fix commit changes whitespace, indentation, or pattern-matched code (see [[../errors/edit-replace-all-silently-misses-indentation-variants]])

Skip the re-run only when:
- Run-N is the first run AND returns 0 BUGs cleanly
- Fix is a 1-line content change with no code logic touch

## How
1. Run `/optimus-review` (default scope: `git diff main...HEAD` or `--commits=N` for the recent work)
2. If REVIEW.md shows `Status: BUG-FIXES-REQUIRED` → fix all BUGs in one commit (or commit batch if fix-owners differ)
3. **Re-run `/optimus-review`** with scope tightened to the fix commit (e.g., `--commits=1`)
4. Read run-N+1's REVIEW.md
5. Archive prior REVIEW.md as `REVIEW-stage1j-runN.md` before each new run
6. Repeat until `Status: PASS` (0 BUG / 0 DESIGN with all surfaced design fixed or waived)

The re-run is free (unlike `/ultrareview`'s 3-lifetime-run quota). ~$1–4 + ~3 min per re-run. The cost of a forgotten BUG that ships to a client is dramatically higher.

## Key Rules
- **Fix commits introduce second-order bugs.** Goddu's run-2 caught 3 NEW BUGs in run-1's fix commit (`replace_all` indentation miss in GodduCanvas, empty-Origin pass-through in route.ts, half-shipped honeypot). All three would have shipped without the re-run.
- **Scope the re-run to the fix commit, not the original full diff.** Tight scope = faster specialists, fewer false positives, cleaner verifier output. `--commits=1` after a fix batch is the canonical pattern.
- **Archive every run's REVIEW.md.** `REVIEW-stage1j-runN.md` archives create the audit trail. The final `REVIEW.md` always reflects the latest run (clean PASS for the close commit).
- **Never close on assumed-clean.** Per CLAUDE.md "No deferred cleanup" rule — if a BUG fix touches code, run the review again. "I'm sure that fixed it" is not an acceptable substitute.

## Reuse Condition
Every Optimus client build's Stage 1J. The pattern is now codified in `project-prime.md` Stage 1J section ("Re-run policy: Re-running `/optimus-review` after a BUG fix batch is the default and free. Don't skip the re-run to save time.").

Applies generically to any multi-agent or multi-stage code review tool: if the tool has a verification step (`/optimus-review`'s Opus 4.7 verifier, future tools, CI/CD review bots), iterate-to-clean is the right close discipline.

## Goddu Imprint trace (canonical example)

| Run | Scope | Raw findings | Verified | Status | Triggered |
|-----|-------|--------------|----------|--------|-----------|
| 1 | last 4 commits (Stages 1G/1H/1I) — 2036-line diff / 18 files | 23 | **7 BUG** / 11 DESIGN / 5 suppressed | BUG-FIXES-REQUIRED | initial Stage 1J invocation |
| 2 | run-1 fix commits (commit A skill infra + commit B 7 BUG fixes) — 704-line diff / 7 files | 12 | **3 NEW BUG** / 8 DESIGN / 1 suppressed | BUG-FIXES-REQUIRED | re-run after commit B |
| 3 | run-2 fix commit (commit B2 3 NEW BUG fixes) — 77-line diff / 3 files | 0 | **0 BUG** / 0 DESIGN / 0 suppressed | PASS ✅ | re-run after commit B2 |

Total cost: ~$8 estimated for all 3 runs combined. Time: ~22 min wall-clock. 10 BUGs surfaced + resolved that the file-level audit (Stage 1H) and browser audit (Stage 1I) both PASSED but structurally couldn't see.

## Related
- Pattern [[stage-1j-pre-launch-gate]] — the gate this runs at
- Pattern [[optimus-review-multi-agent-code-review-skill]] — the tool that runs the review
- Error [[../errors/edit-replace-all-silently-misses-indentation-variants]] — class-of-bug iterate-to-clean catches
- [[../../optimus-review-skill.md]] — full skill architecture
