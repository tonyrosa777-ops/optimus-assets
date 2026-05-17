# /optimus-review — Multi-Agent Code Review Skill

**Plan saved:** 2026-05-17 by orchestrator during Goddu Imprint Stage 1J
**Status:** ✅ EXECUTED — built end-to-end + smoke-tested + used to clear Goddu Stage 1J in 3 runs (same session)
**Replaces:** Claude Code's `/ultrareview` (CLI-only, 3 free runs lifetime per account, then $5–$20 per run) at project-prime.md Stage 1J
**Touches:** Optimus agent system globally — routed to `C:\Projects\Optimus Assets\` per CLAUDE.md Plan Preservation Rule

---

## Why this exists

`/ultrareview` is a Claude Code CLI feature that runs a parallel fleet of specialist review agents in Anthropic's cloud sandbox, with an independent verification pass that reproduces every finding before it surfaces. It produces high-signal "BUG only, no nits" output and is the documented Stage 1J gate in project-prime.md.

It fails mission-fit for Optimus production:

1. **3 free runs lifetime per account.** Optimus ships multiple client builds per quarter. Burning one quota per project for Stage 1J is unsustainable.
2. **$5–$20 per run after free quota** — contradicts Optimus's core mission ("affordable AI for SMBs"). Every client build pays an Anthropic toll for a step we can replicate locally.
3. **Surface-gated to terminal CLI only.** Not available in the VSCode native extension where most build work happens.
4. **No project knowledge.** /ultrareview cannot read CLAUDE.md, design-system.md, market-intelligence.md, or the absolute-rules-index — meaning it cannot catch the Optimus-specific failures (em-dashes, hero violations, missing testimonials, AEO gaps) that pre-launch-auditor and the human checkpoint exist to catch.

A local equivalent is feasible — we already have the subagent infrastructure, the gsd-code-reviewer pattern, and the pre-launch-auditor as references. It costs $1–4 per run amortized (Sonnet specialists + Opus verifier on a typical project diff), runs unlimited times, and adds 2 Optimus-specific lenses /ultrareview structurally cannot.

This is also drink-own-champagne for the Tier-4 Autonomous AI Employee thesis: Optimus's own quality gate runs on Optimus's own multi-agent architecture, deployed for every client.

---

## Architecture — 8 specialists + 1 verifier

```
Caller (orchestrator or human) → /optimus-review
                                         ↓
                  detect diff scope (branch vs main by default)
                                         ↓
            spawn 8 specialist agents in PARALLEL (single message)
            ┌────────────────────────────────────────────────────┐
            │ 1. correctness     2. security       3. architecture │
            │ 4. tests           5. performance    6. style       │
            │ 7. absolute-rules  8. design-system                 │
            │           (Sonnet 4.6, effort=medium)               │
            └────────────────────────────────────────────────────┘
                                         ↓
                  collect 8 findings JSON files in .optimus-review/
                                         ↓
                       spawn 1 verifier agent (sequential)
                       Opus 4.7, effort=max
                       reads all 8 findings + reproduces each
                       classifies BUG / DESIGN / FALSE-POSITIVE
                                         ↓
                       writes REVIEW.md at project root
                                         ↓
                  caller reads REVIEW.md and triages
```

### Specialists (parallel — each reads the diff + outputs findings JSON)

The first 6 mirror /ultrareview's documented lenses (per official docs at code.claude.com/docs/en/ultrareview). The last 2 are Optimus-only and are what makes this better-than-/ultrareview for our use case.

1. **correctness** — logic errors, off-by-ones, null/undefined handling, race conditions, type mismatches, unhandled promise rejection, missing `await`, edge cases on boundary inputs
2. **security** — SQL/command/path injection, XSS, hardcoded secrets, insecure crypto, unsafe deserialization, missing input validation, auth/authz gaps, exposed env vars in client bundles, unsafe `dangerouslySetInnerHTML`
3. **architecture** — pattern violations, dependency direction, duplicate abstractions, missing error boundaries, coupling, separation of concerns, premature abstraction, component composition issues
4. **tests** — missing happy-path coverage, missing failure-mode coverage, incorrect assertions, mocked-to-pass anti-pattern, dead tests, tests that don't actually test (e.g. `expect(x).toBeDefined()` on a literal)
5. **performance** — N+1 queries, nested loops on large collections, blocking calls in render paths, unbounded reads, useEffect dependency leaks, missing memoization on expensive computations, bundle-size red flags
6. **style** — language conventions, naming, formatting, console.log/debugger left in code, TODO/FIXME density, unused imports/variables, magic numbers. Lowest signal — filtered hard by verifier (most style findings classified as DESIGN, not BUG).
7. **absolute-rules** (Optimus-only) — reads `C:\Projects\Optimus Assets\00 — Empire Index\absolute-rules-index.md` and tests each of the 15 absolute rules against the diff. Hero composition (§4), CTA destinations (§5), H1 tagline + shimmer (§6), no flat backgrounds (§3), em-dashes (§13), every interior page animated (§15), off-domain redirects (§14), etc. The Pattern #58 cross-check at code-review depth.
8. **design-system** (Optimus-only) — reads the project's `design-system.md` and CLAUDE.md, checks compliance with palette tokens, type scale, brand personality axes, sections matrix, AEO requirements (first-paragraph direct answer in blog posts, FAQPage schema, alt text on every image), voice/tone match against §7 of design-system.md.

### Verifier (sequential — Opus 4.7)

Reads `.optimus-review/findings-*.json` from all 8 specialists. For each finding:
1. Reads the actual file at the cited line range
2. Reproduces the claim: does the bug/violation actually exist at that location?
3. Classifies:
   - **BUG** — verified, blocks launch. The verifier could reproduce the issue.
   - **DESIGN** — subjective or stylistic. Surfaces to human review with rationale.
   - **FALSE-POSITIVE** — verifier could NOT reproduce. Suppressed from output.
4. Writes consolidated `REVIEW.md` at the project root.

This is the critical step. Per /ultrareview docs, verification is what produces high-signal output. Specialists are encouraged to flag aggressively (Sonnet at medium effort tends to produce ~15–30 raw findings on a typical project diff); the verifier filters down to typically ~3–8 BUG + ~5–15 DESIGN with the rest suppressed.

### Diff scope detection

Default behavior in priority order:
1. If `--full` flag passed → review entire working tree
2. If `--commits N` flag passed → review last N commits
3. If `--paths "<glob>"` flag passed → scope to those paths
4. If on a feature branch with `main` (or `master`) reachable → diff against the merge-base of `main`
5. If on `main` directly → diff between HEAD and HEAD~10 (last 10 commits)

The skill explicitly states the scope in REVIEW.md's header so the user can re-run with a different scope if needed.

---

## Files to create

```
C:\Users\Anthony\.claude\agents\optimus-review\
├── correctness.md          (specialist, Sonnet 4.6, effort=medium)
├── security.md             (specialist, Sonnet 4.6, effort=medium)
├── architecture.md         (specialist, Sonnet 4.6, effort=medium)
├── tests.md                (specialist, Sonnet 4.6, effort=medium)
├── performance.md          (specialist, Sonnet 4.6, effort=medium)
├── style.md                (specialist, Sonnet 4.6, effort=low — lowest signal)
├── absolute-rules.md       (Optimus specialist, Sonnet 4.6, effort=medium)
├── design-system.md        (Optimus specialist, Sonnet 4.6, effort=medium)
└── verifier.md             (verifier, Opus 4.7, effort=max)

C:\Users\Anthony\.claude\skills\optimus-review\
└── SKILL.md                (skill entrypoint — orchestration instructions)
```

Each specialist is ~70–100 lines (frontmatter + role + required reading + scope + output format). The verifier is ~150 lines (frontmatter + verification methodology + reproduction protocol + output schema). SKILL.md is ~150 lines (orchestration flow + agent spawn instructions + output triage).

---

## Output format

`REVIEW.md` at project root:

```markdown
# /optimus-review — <project name>
Date: <date>
Diff scope: <branch vs main | last N commits | full tree | paths>
Specialists run: 8 (all completed)
Verifier: Opus 4.7
Raw findings: <N>  Verified: <N BUG> <N DESIGN> <N suppressed>

## BUG Findings (block launch — must resolve)

### BUG-1 — [correctness] — src/foo/bar.ts:42
<one-sentence description>

**Reproduction:** <verifier's reproduction note — what they checked>
**Suggested fix:** <specific change, if obvious>

---

## DESIGN Findings (review with owner — fix or waive)

### DESIGN-1 — [absolute-rules] — src/components/Hero.tsx:18
<one-sentence description>
**Severity:** subjective / style / minor
**Action:** fix in this commit / waive with rationale

---

## Suppressed (verifier classified as false-positive)

- [style] src/foo.ts:99 — line 99 doesn't exist in file (specialist hallucinated)
- [tests] src/bar.test.ts:7 — assertion is testing the function under test, not a literal
```

This matches /ultrareview's output schema closely so the Stage 1J workflow in project-prime.md doesn't need rewriting beyond swapping the invocation command.

---

## project-prime.md Stage 1J update

Current Stage 1J text invokes `/ultrareview` and includes a graceful-degradation block for "if `/ultrareview` is not available." Replace with:

```diff
- 1. Invoke `/ultrareview` from the Claude Code CLI inside the project folder.
+ 1. Invoke `/optimus-review` from inside the project folder. The skill spawns
+    8 specialist agents in parallel (correctness, security, architecture, tests,
+    performance, style + Optimus-only absolute-rules and design-system lenses)
+    followed by an Opus 4.7 verifier that reproduces every finding.

- 2. Capture the output. `/ultrareview` returns findings classified BUG / DESIGN / PASS.
+ 2. Read REVIEW.md at the project root. Findings classified BUG / DESIGN / suppressed.
```

Plus removal of the `/ultrareview` cost/quota/availability warnings (no longer apply).

---

## Build sequence

1. Write 9 agent files at `C:\Users\Anthony\.claude\agents\optimus-review\` (1 file at a time — they share a template but each has distinct scope)
2. Write SKILL.md at `C:\Users\Anthony\.claude\skills\optimus-review\SKILL.md`
3. Update project-prime.md Stage 1J section
4. Save THIS plan file (already done above)
5. Smoke test: run `/optimus-review` on Goddu Imprint's current branch
6. If smoke test produces clean output → mark skill VALIDATED, complete Goddu Stage 1J using the new skill
7. Commit everything atomically: `feat(optimus-review): multi-agent code review skill replacing /ultrareview at stage 1j`

---

## Cost / time estimates

**Per run (typical project diff):**
- 8 specialists × Sonnet 4.6 × ~5K tokens diff context + ~3K tokens output = ~64K tokens total ≈ $0.50–1.50
- 1 verifier × Opus 4.7 × ~30K tokens (8 findings JSONs + file reads for reproduction) = ~$0.50–2
- **Total: ~$1–4 per run** vs. /ultrareview's $5–20
- **Time: ~3 min wall clock** (specialists parallel, verifier sequential)

**Build cost (one-time):**
- ~1,150 lines of new content across 10 files + project-prime.md edit
- Estimated 2–3 hours focused work

**Lifetime value:**
- Replaces /ultrareview at every Optimus client build (~6–10 builds/year at scale)
- Catches Optimus-specific failures /ultrareview cannot
- Drink-own-champagne reference for Tier-4 Autonomous AI Employee architecture

---

## Risks / open questions

1. **False-positive rate.** Sonnet specialists at medium effort tend to over-flag. Verification is the mitigation, but if specialists collectively produce 50+ raw findings on a typical diff, verifier latency balloons. Mitigation: cap specialists at "top 5 findings per category" in their output schema.

2. **Verifier cost overrun.** If the verifier reads too many files to reproduce findings, Opus tokens add up. Mitigation: pass the verifier the specific file:line range, not the whole file — verifier reads ~20 lines of context per finding.

3. **Diff scope edge cases.** First commit, no main branch, detached HEAD, monorepo subdirectories. Mitigation: fall back to "full tree" with a warning logged in REVIEW.md.

4. **Skill discoverability.** Skills in `~/.claude/skills/` are not auto-listed everywhere. Mitigation: register in project-prime.md Stage 1J + add a row to `knowledge/build-log.md` Patterns table after the smoke test passes.

5. **Maintenance.** When /ultrareview itself evolves (Anthropic adds lenses, changes verification), we need to track and port. Mitigation: schedule a quarterly re-read of code.claude.com/docs/en/ultrareview and update specialists if Anthropic publicly documents architecture changes.

---

## Verification checklist (executed 2026-05-17)

- [x] All 9 agent files exist and have valid YAML frontmatter (correctness 138 lines + 7 delegated + verifier 340 lines)
- [x] SKILL.md exists at `~/.claude/skills/optimus-review/SKILL.md` and references all 9 agents
- [x] project-prime.md Stage 1J updated in BOTH the master at `C:\Projects\Optimus Assets\project-prime.md` AND the Goddu local copy at `c:\Projects\Steve-Goddu\.claude\commands\prime.md` — `/ultrareview` references removed, cost/quota/CLI graceful degradation blocks removed
- [x] Plan file committed alongside Goddu's Stage 1J commits (this file)
- [x] Smoke test on Goddu Imprint produced REVIEW.md across 3 runs
- [x] Smoke test caught REAL issues that file-level pre-launch-auditor + browser audit both missed (7 BUGs run-1, 3 NEW BUGs run-2, then PASS run-3)
- [ ] knowledge/build-log.md Patterns table updated with the new skill — TODO next /retro pass
- [ ] CLAUDE.md (Optimus Assets root) updated to reference the new skill in the Subagent Delegation Rule — TODO when next project hits Stage 1J

---

## Execution results (Goddu Imprint smoke test — same session)

**Skill performance on a real Stage 1J:**

| Run | Scope | Raw findings | Verified | Wall time | Outcome |
|-----|-------|--------------|----------|-----------|---------|
| 1 | last 4 commits / 2036 line diff / 18 files | 23 | 7 BUG / 11 DESIGN / 5 suppressed | ~12 min | BUG-FIXES-REQUIRED |
| 2 | run-1 fix commits / 704 line diff / 7 files | 12 | 3 BUG / 8 DESIGN / 1 suppressed | ~7 min | BUG-FIXES-REQUIRED |
| 3 | run-2 fix commit / 77 line diff / 3 files | 0 | 0 BUG / 0 DESIGN / 0 suppressed | ~2 min | **PASS ✅** |

**What the skill caught that file-level audit + browser audit missed (run-1):**
- 5 security bugs in `/api/contact` (no rate limit, CRLF injection, branded-domain phishing relay, sequential await coupling, missing email validation)
- 2 performance bugs threatening Lighthouse ≥ 90 (GodduCanvas rAF 60Hz wakeup on mobile, BookingCalendar static-imported into homepage critical bundle)
- The pre-launch-auditor PASSED `/api/contact` because the file existed + had a `resend.emails.send` call. The browser audit PASSED because there were no console errors. Neither could see CRLF injection or missing rate limit. **Exactly the gap Stage 1J is meant to fill.**

**What the skill caught about its own fixes (run-2):**
- Verifier surfaced 3 NEW BUGs introduced BY commit B (the run-1 fix commit) — proving the verification pass works on second-order bugs, not just initial state.

**What ran clean (both runs):**
- Optimus-only lenses (absolute-rules, design-system) returned 0 findings on all runs, confirming Stages 1H + 1I genuinely cleaned the Optimus-specific concerns.

**Cost:** ~$8 estimated total for 3 runs (under the cost of a single `/ultrareview` invocation).

**Time-to-clear from concept to clean PASS:** ~4 hours including building the 10-file skill from scratch + 3 runs + 2 rounds of fix-and-re-review. Future projects: ~5-15 minutes per run, depending on diff size.

---

## Lessons for future projects (added 2026-05-17 post-execution)

1. **Verifier deduplication works as designed.** Sonnet specialists over-flag at medium effort (run-1 produced 23 raw; verifier suppressed/downgraded 16 of them to DESIGN or false-positive). The verifier's job-as-signal-filter is the critical value-add over a single-agent review.

2. **Optimus-only lenses are quiet but earn their slot.** absolute-rules and design-system returned 0 across all 3 runs — but their job is to backstop the documented absolute-rule cross-check and design-system.md compliance. The check ran successfully each time; absence of findings just means Stages 1B + 1H + 1I cleaned those concerns thoroughly.

3. **Specialists can flag issues their own previous run created.** Run-2 catching the half-shipped honeypot (server check without client input) and the empty-Origin pass-through was a critical signal — without re-running, those would have shipped as production vulnerabilities even though commit B was explicitly meant to fix them. The pattern: ALWAYS re-run /optimus-review after fix batches.

4. **Diff scope matters for budget.** Run-1 had a 2036-line diff that took ~12 min and ~150K tokens per specialist. Run-3's 77-line diff finished in ~2 min total. Tight scope produces faster, more focused reviews. The `--commits=N` flag is the lever.

5. **PNG-onload regressions are real even when latent.** Run-2 BUG-1 (`loopActive` invariant violation in the PNG branch) is unreachable in Goddu's current state (no `src=` prop), but the verifier correctly classified it BUG. The reasoning: any future logo PNG asset would activate the bug. Run-2 caught a latent-but-real future-foot-gun the file-level checks couldn't see.

6. **`replace_all=true` is dangerous.** The run-2 BUG-1 root cause was my use of `replace_all=true` on the GodduCanvas pattern `buildParticles();\n        rafId = ...` — the PNG-onload branch had different indentation (10 spaces vs 8) and didn't match. Either use explicit per-site Edit calls OR confirm all occurrences share exact whitespace before using `replace_all`.

7. **Tool-search "before adding" works.** When I needed `TodoWrite` mid-session, `ToolSearch` loaded it cleanly. Same flow worked for the deferred tool fetch.
