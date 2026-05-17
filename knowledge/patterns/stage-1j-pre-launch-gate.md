# Stage 1J — Pre-Launch Code Review Gate

**Established:** 2026-04-17 (Opus 4.7 retune) — originally as `/ultrareview` pattern
**Updated:** 2026-05-17 — replaced `/ultrareview` with local `/optimus-review` skill (see [optimus-review-skill.md](../../optimus-review-skill.md))

## What Stage 1J is

The third and final pre-launch gate. Catches bugs and design issues a careful code reviewer would find but that file-level pre-launch-auditor (Stage 1H) and multi-breakpoint browser audit (Stage 1I) structurally cannot see — security vulnerabilities, logic errors, performance regressions, accessibility gaps, missing schema, pattern deviations.

## The tool: /optimus-review

Local multi-agent code review skill at `~/.claude/skills/optimus-review/`. Spawns 8 parallel specialists (correctness, security, architecture, tests, performance, style + Optimus-only absolute-rules and design-system lenses) followed by an Opus 4.7 verifier that reproduces every finding before it surfaces.

- **Unlimited reruns** — no per-run quota, no per-run cost gate
- **~$1–4 per run** in Anthropic API spend
- **~3 min wall time** per run (8 specialists in parallel, verifier sequential)
- **Project-aware** — reads CLAUDE.md, design-system.md, absolute-rules-index.md → catches Optimus-specific violations /ultrareview cannot

Plan + architecture detail: [optimus-review-skill.md](../../optimus-review-skill.md).

### Historical: why we replaced /ultrareview

`/ultrareview` was Claude Code's CLI-only cloud review feature. Three structural fits Optimus could not accept:
1. **3 free runs lifetime per account**, then $5–$20 per run
2. **Terminal CLI only** — not available in VSCode native extension where most build work happens
3. **No project knowledge** — could not read CLAUDE.md, design-system.md, or absolute-rules-index.md

The mission-fit calculus: Optimus ships multiple client builds per quarter. Paying an Anthropic toll for a gate we can replicate locally with project awareness violated the "world's newest tech to SMBs at affordable prices" mission. The replacement was built end-to-end during Goddu Imprint Stage 1J on 2026-05-17.

## When it runs in the Optimus workflow

**Phase 1J — after Phase 1I pre-launch-auditor AND Section 11 multi-breakpoint browser audit both PASS.** Final gate before the demo URL goes to the client.

Order:
1. Phase 1H pre-launch-auditor (file-level checks) → must pass with 0 FAIL
2. Section 11 multi-breakpoint Playwright browser audit (Stage 1I) → must pass at all viewports
3. **Phase 1J `/optimus-review` → must return 0 BUG**
4. Demo URL to client

If any of the three fail, the next does not run. Launch is blocked until resolved.

## Invocation

From the project directory:
```
/optimus-review
```

Default scope: `git diff main...HEAD`. Flags: `--base=<ref>`, `--commits=N`, `--paths=<glob>`, `--full`.

For a meaningful Stage 1J, scope to "the work since the last known-good commit" (typically the last launched state OR the start of the current sprint).

## Output triage — BUG / DESIGN / SUPPRESSED

The verifier classifies every specialist finding:

### BUG-severity findings — BLOCKS LAUNCH

Verified-reproducible issues that would cause incorrect behavior, security risk, data loss, or violate an absolute rule. Examples:
- Logic errors, null/undefined risk, race conditions
- Security: injection, missing auth, hardcoded secrets, phishing relay vectors
- Performance regressions threatening Lighthouse ≥ 90 budget
- Violations of any rule in `00 — Empire Index/absolute-rules-index.md`
- Missing schema markup that breaks AEO citation

Resolution: fix the bug, **re-run `/optimus-review`** to confirm zero BUG findings, then advance to demo. Re-runs are free — always do them.

**Fix-owner routing:**
- `/data/*.ts` (copy, site data, quiz data): delegate to content-writer agent
- `/components/Hero*.tsx`, `/components/*Canvas.tsx`, animation files: delegate to animation-specialist agent
- `/app/sitemap.ts`, `/app/robots.ts`, `/app/**/opengraph-image.tsx`, `JsonLd.tsx`, schema markup: delegate to seo-aeo-specialist agent
- `/app/globals.css`, layout, design tokens: orchestrator fixes inline (no agent)
- `/app/api/**` routes: orchestrator fixes inline
- `/lib/*`, utilities, generic helpers: orchestrator fixes inline

### DESIGN-severity findings — REVIEW OR WAIVE

Verified-to-exist but subjective. Style choices, refactor opportunities, "I'd write this differently" findings. Either fix in the same commit or explicitly waive with a one-line rationale logged in REVIEW.md.

Examples:
- Pattern deviation from existing code
- Missing ARIA attribute (fix these usually)
- Minor UX inconsistency
- DRY opportunities across files

**Volume thresholds:**
- DESIGN count 0–5: proceed with review session (~5 min)
- DESIGN count 6–15: focused review session (~15 min). Pre-triage into categories before presenting to Anthony
- DESIGN count > 15: signal that build quality needs cleanup. Return one phase before resuming Stage 1J

**Waiver policy:** a waiver on this project is NOT automatically a waiver on future projects. If a pattern is consistently waived across 3+ builds, promote it to an explicit CLAUDE.md rule or knowledge/patterns entry so it stops surfacing.

### SUPPRESSED findings — VERIFIER FILTERED

The verifier could not reproduce the specialist's claim (line didn't match, file didn't exist, finding was misread) OR the finding was a duplicate of another finding. No action needed; useful for debugging skill calibration.

### Zero BUG + zero DESIGN — LAUNCH CLEARED

REVIEW.md's `[STAGE-1J-RESULT]` block reads `Status: PASS`. Proceed to demo URL send.

## Re-run policy

Every BUG fix batch is followed by a re-run. Unlike `/ultrareview`'s 3-lifetime-runs quota, `/optimus-review` re-runs are free and unlimited. **Always re-run after fixes** — Goddu Imprint Stage 1J ran 3 times to clear (7 BUG → 3 NEW BUG → PASS), and run-2 caught second-order bugs that the run-1 fixes introduced. Skipping the re-run would have shipped real security vulnerabilities.

## Logging format

REVIEW.md is written to the project root by the verifier. Archive prior runs as `REVIEW-stage1j-runN.md` when running multiple times so the audit trail is preserved.

REVIEW.md structure (see verifier.md for the full schema):
```
# /optimus-review — <project>
Date: <date>
Diff scope: ...
Specialists run: 8
Verifier: Opus 4.7
Raw findings: <N>  Verified: <N BUG> <N DESIGN> <N suppressed>

## Summary
BUG: N  DESIGN: N  SUPPRESSED: N

## BUG Findings (block launch — must resolve)
### BUG-1 — [lens] — file:line_range
<description>
**Reproduction:** <verifier's reproduction notes>
**Suggested fix:** <if obvious>

## DESIGN Findings (review with owner — fix or waive)
### DESIGN-1 — [lens] — file:line_range
<description>
**Severity:** subjective / style / minor
**Action options:**
- Fix in this commit: <suggestion>
- Waive with rationale: <suggestion>

## Suppressed (verifier classified as false-positive)
- [lens] file:line — <reason suppressed>

## Handoff (for project-prime.md Stage 1J)
[STAGE-1J-RESULT]
Status: PASS | BUG-FIXES-REQUIRED | DESIGN-REVIEW-REQUIRED
BUGs: N
DESIGNs: N
Suppressed: N
Reviewer: optimus-review verifier (Opus 4.7)
```

## Time budget per run

5 minutes wall clock typical. If a run exceeds 10 min, the verifier likely hit an edge case — check `.optimus-review/findings-*.json` for malformed specialist output, then re-run with `--paths` scope narrowed.

## Why this gate matters

Three audits, three different layers:
- **Stage 1H pre-launch-auditor** — file-level checks: file exists, route wired, schema present, copy in /data/site.ts, no [DEMO COPY] left
- **Stage 1I browser audit** — visible-state checks: no console errors, hero above the fold, no horizontal scroll at 375, mobile nav drawer works
- **Stage 1J /optimus-review** — code-level review: security holes, logic bugs, missing schema, accessibility gaps, perf regressions, project-rule violations

All three find different things. Pre-launch needs all three.

Goddu Imprint's Stage 1J run-1 surfaced 7 BUGs (5 security + 2 performance) that Stages 1H and 1I both passed but couldn't see. CRLF injection in /api/contact, branded-domain phishing relay, no rate limit, 60Hz rAF wakeup on mobile, 100KB+ static-imported into homepage critical bundle. **This is the gate's job.**

## Related patterns
- `knowledge/patterns/end-of-build-multi-breakpoint-browser-audit.md` — the Section 11 browser audit that runs before this gate
- `knowledge/patterns/opus-4-7-prompt-tuning.md` — the 4.7 retune that introduced this gate as `/ultrareview`
- `optimus-review-skill.md` (vault root) — full architecture + smoke-test execution results

## Status
ACTIVE since 2026-04-17 as `/ultrareview`. Replaced with local `/optimus-review` 2026-05-17 (Goddu Imprint Stage 1J). Used on every project from Witt's Restoration onward.
