# Pattern #65 — Proactive `.next/` cache clear in multi-restart sessions

**Category:** Workflow / Infrastructure / Windows-Specific
**Project:** Ead Financial
**Date:** 2026-05-08
**Indexed in:** `knowledge/build-log.md` Pattern #65
**Counterpart error:** [[errors/turbopack-next-cache-panic-after-multiple-taskkills]] (Error #58)

## The pattern

In any orchestrator session that kills `next dev` more than twice, clear `web/.next/` **before** the third start — preempt Error #58's Turbopack PostCSS panic instead of recovering from it.

```powershell
# PowerShell — proactive prevention
if ((Get-EventCount 'next-dev-kill') -ge 2) {
  Remove-Item web\.next -Recurse -Force -ErrorAction SilentlyContinue
}
cd web; npm run dev
```

In practice the orchestrator just tracks a kill counter mentally:

> "I've killed `next dev` twice this session. Before the next restart, clear `.next/`."

The cost is one extra `Remove-Item` invocation and ~300ms on the next dev start (Turbopack rebuilds the cache from scratch). The benefit is avoiding 5–15 minutes of Error #58 troubleshooting where the panic message points at `globals.css` rather than the real cause.

## When this fires

- **Stage 1I-style Playwright passes** — every cycle is `start dev → run Playwright → kill dev → make fix → restart dev`. After 2 passes, the third start is at risk.
- **Stage 1E per-page rebuild loops** — orchestrator builds a section, verifies, fixes, restarts. After 2 fix cycles, clear before the third.
- **Debug sessions with hot-reload iteration followed by hard kills** — same shape.
- **Multi-component refactors** — same shape.

## Decision rule

Mental check before any `npm run dev` start:

```
Have I killed `next dev` twice or more in this session?
├─ Yes → `rm -rf web/.next/` before the next start.
└─ No  → start normally.
```

If the answer is unclear, the cost of clearing `.next/` is so low (~300ms) that defaulting to clear is correct. Defaulting to NOT clear costs 5–15 min when Error #58 fires.

## Reactive variant

If `next dev` reports `✓ Ready` then panics on the first GET with the `0xc0000142` / `globals.css` symptom from Error #58:

1. **Immediately** clear `.next/`. Do not troubleshoot `globals.css`. Do not check package versions. Do not roll back CSS edits.
2. Restart `npm run dev`.
3. If panic recurs after a clean cache clear, escalate — there's a real cause (typo, syntax error, package conflict). 99% of the time the clean cache resolves it.

## Why proactive beats reactive

- **Error message misdirection.** The panic message says "Caused by `globals.css`." It is not. Following the false signal sends you down a 15-minute path of looking at CSS code that isn't the problem.
- **Cumulative kill state is invisible.** There's no warning when `.next/` enters the at-risk state. By the time the panic surfaces, you've already lost the thread on whatever you were doing.
- **The cost is 300ms.** Even if the cache clear was unnecessary 90% of the time, you'd still come out ahead.

## Wired into

- CLAUDE.md Visual QA Rule (the multi-Playwright-pass workflow that triggers this most often) — should reference this pattern in the "after dev server kill" subsection.
- `project-prime.md` Stage 1I — orchestrator's Playwright cycle should clear `.next/` between every two passes.
- Stage 1E orchestrator brief — page-by-page rebuild loops include `.next/` clear in the verify-loop checklist.

## Limitations

- **Windows + Turbopack specific.** Linux/macOS dev environments have not surfaced this panic on the same repro path. WSL2 Windows hosts MAY surface it (untested) — assume affected until a clean WSL session disproves.
- **Does not prevent OTHER `.next/` issues** (build cache invalidation, RSC payload mismatches after major version upgrades). This pattern is targeted at the Error #58 symptom specifically.
- **Pre-launch production builds (`next build`) are not affected** — they generate `.next/` from scratch each invocation and don't accumulate state between kills.

## Verified resolution

Ead Financial Session 2 (commit 66bc398) — orchestrator killed `next dev` 4 times during pre-flight verification cycles. After the fourth kill, dev server panicked on every GET with the Error #58 symptom. Cache clear (`Remove-Item web\.next -Recurse -Force`) resolved on the next start in 302ms. No source-code change was needed.

## Cross-references

- Build-log Pattern #65 (this pattern)
- Build-log Error #58 (the symptom)
- [[patterns/asymmetric-cost-pre-flight-calibration]] (Pattern #63 — the workflow context where multi-restart is most common)
- [[patterns/end-of-build-multi-breakpoint-browser-audit]] (Stage 1I — the canonical multi-Playwright-pass workflow)
