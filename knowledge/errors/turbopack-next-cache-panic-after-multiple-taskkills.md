# Error #58 — Turbopack `.next/` cache panic on Windows after multiple taskkill cycles

**Project:** Ead Financial
**Date:** 2026-05-08 (Session 2 — Stage 1E pre-flight item 9)
**Severity:** Build/dev blocker (recurring)
**Platform:** Windows + Next.js 16.2.6 + Turbopack
**Indexed in:** `knowledge/build-log.md` Error #58
**Companion pattern:** [[patterns/proactive-next-cache-clear-multi-restart-sessions]] (Pattern #65)

## Symptom

Dev server reports successful start, then panics on every page load:

```
> next dev

▲ Next.js 16.2.6 (Turbopack)
- Local:         http://localhost:3000
✓ Ready in 302ms

 GET / 500 in 6ms (next.js: 3ms, application-code: 4ms)

-----
FATAL: An unexpected Turbopack error occurred. A panic log has been written to
C:\Users\<user>\AppData\Local\Temp\next-panic-<hash>.log.

Failed to write app endpoint /page

Caused by:
- [project]/src/app/globals.css [app-client] (css)
- creating new process
- node process exited before we could connect to it with exit code: 0xc0000142

Debug info:
- Execution of get_written_endpoint_with_issues_operation failed
- Execution of endpoint_write_to_disk failed
- Execution of <AppEndpoint as Endpoint>::output failed
- Failed to write app endpoint /page
- ...
- Execution of <PostCssTransformedAsset as Asset>::content failed
- Execution of evaluate_webpack_loader failed
- creating new process
- node process exited before we could connect to it with exit code: 0xc0000142
-----
```

The Windows `0xc0000142` error code is `STATUS_DLL_INIT_FAILED` — a runtime DLL initialization failure when spawning a child process. Turbopack uses a Node subprocess to evaluate the PostCSS loader chain on `globals.css`. When `.next/` is in a corrupt state, the spawn handshake fails and the entire request blows up.

The error message names `globals.css` as the proximate cause, but **`globals.css` is not the cause.** Editing it, reverting it, or deleting CSS variable references will not resolve the panic. The cause is `.next/` cache state.

## Repro recipe

In a single session:

1. Start `npm run dev` (works).
2. Edit something. Save.
3. `Stop-Process -Id <pid> -Force` (or `taskkill /PID <pid> /F`). Stop the dev server hard.
4. Repeat steps 1–3 two or three more times in the same session.
5. On the third or fourth restart attempt, the panic above appears on every GET.

This was the exact path on Ead Financial pre-flight item 9 — orchestrator killed `next dev` between Playwright passes (verify → fix → verify), and on the post-fix verify the dev server panicked.

## Fix

```powershell
# PowerShell
Get-CimInstance Win32_Process -Filter "Name='node.exe'" |
  Where-Object { $_.CommandLine -match 'next' } |
  ForEach-Object { Stop-Process -Id $_.ProcessId -Force }

Remove-Item web\.next -Recurse -Force

cd web; npm run dev
```

```bash
# Bash (Git Bash / WSL)
# (kill stray node processes first via PowerShell or Task Manager)
rm -rf web/.next/
cd web && npm run dev
```

After the cache clear, Turbopack rebuilds from scratch on the next start (~300ms scaffold cost, negligible) and `globals.css` PostCSS evaluates cleanly.

## Why "kill node + restart" alone is insufficient

`Stop-Process -Force` (or `taskkill /F`) terminates the parent `node.exe` process but does not always release Turbopack's internal locks or guarantee the child PostCSS-loader subprocess shut down cleanly. The next `next dev` start inherits a partial `.next/` write state — incremental compilation metadata, lockfiles, or module graph snapshots — that's no longer self-consistent. The cheapest remediation is wholesale cache clear.

## When this is most likely to surface

- Stage 1E page-by-page work where each page-build triggers a verify → fix loop.
- Stage 1I multi-breakpoint browser audits with multiple dev-server kills during the audit.
- Debug sessions on a single component with many hot-reload iterations followed by a kill.
- Any orchestrator session that runs Playwright passes more than twice with dev-server kills between them.

## Anti-patterns to avoid

- **Do not troubleshoot `globals.css`.** The error message names it as proximate but it is not the cause. Reverting CSS edits, removing custom properties, or simplifying the file will not help.
- **Do not roll back package versions.** This is not a Next.js, Turbopack, or PostCSS version bug — it's a state-corruption bug.
- **Do not `npm install --force`.** Reinstalling dependencies does not clear `.next/`.
- **Do not assume the file you just edited caused it.** Check whether you've killed the dev server multiple times this session first.

## Prevention

See [[patterns/proactive-next-cache-clear-multi-restart-sessions]] (Pattern #65) for the proactive workflow rule. TL;DR: in any session that kills `next dev` more than twice, clear `.next/` before the third start.

## Cross-references

- Build-log Error #58
- Build-log Pattern #65 (companion proactive prevention)
- CLAUDE.md Visual QA Rule (multi-Playwright-pass workflow that triggers this)
- Stage 1I orchestrator execution layer (project-prime.md) — runs the workflow that exposes this most often
