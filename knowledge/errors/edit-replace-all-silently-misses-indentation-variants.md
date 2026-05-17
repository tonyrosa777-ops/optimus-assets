# Error: `Edit` tool's `replace_all=true` silently misses indentation variants
**Project:** Goddu Imprint
**Date:** 2026-05-17
**Phase:** Stage 1J BUG fix commit (run-1 fixes)

## Problem
Fixing BUG-5 (GodduCanvas rAF rescheduling at 60Hz when hidden) required adding `loopActive = true;` before three `rAF` ignition sites:
- Line 761 (PNG `onload` success branch, inside `if (octx) { ... }` — extra indent level)
- Line 769 (PNG `onerror` fallback branch)
- Line 778 (text-only `readyHandler` branch)

Used `Edit` with `replace_all=true` and pattern `buildParticles();\n        rafId = requestAnimationFrame(draw);`. Tool reported "All occurrences were successfully replaced."

But the PNG-onload path was at 10 spaces of indentation while the other two were at 8. The replace_all match was anchored at 8 spaces, so the deeper-nested PNG branch was silently skipped. The fix shipped with the invariant broken on one of three sites.

Latent today on Goddu (no `src=` prop passed, PNG branch unreachable), but a future logo PNG asset would activate the bug — every viewport resize would spawn parallel rAF chains, the exact failure mode BUG-5 was supposed to eliminate.

Caught by `/optimus-review` run-2 verifier on the BUG fix commit.

## Root Cause
`replace_all=true` on a string with leading whitespace anchors to ONE specific indentation level. Multiple call sites with the same code body but different indentation depths look identical to a human reviewer scrolling the file, but are distinct strings to the matcher.

The fix relied on visual inspection ("I see three matching patterns") rather than whitespace-exact matching ("does the literal 14-character leading-whitespace prefix differ across sites").

## Solution
Surgical Edit call: read the file at the missed location (PNG-onload branch), confirm the exact indentation, write a separate `Edit` for that single site with full surrounding context. Fixed in commit `467ef0b`.

## Prevention
Before using `Edit` with `replace_all=true` on a multi-call-site pattern:
1. **Grep first**: `Grep` the file for the exact pattern. Count occurrences.
2. **Verify whitespace match**: read each occurrence's surrounding context (5 lines above + below). Confirm leading-whitespace prefix is identical across all sites.
3. **If whitespace varies**: use multiple explicit `Edit` calls, one per site, with enough context to make each match unique. Do NOT rely on `replace_all=true`.

Default workflow rule for the orchestrator: when the same code block needs to change at N sites in one file AND the file has nesting, prefer N explicit `Edit` calls over one `replace_all=true`. The cost is N tool calls vs. 1 — but the cost of a latent bug from a silent miss is far higher.

Optimus-specific application: every Stage 1J fix batch that touches a recurring code pattern (multi-route security hardening, multi-component animation guards, multi-test assertion updates) MUST be re-reviewed via `/optimus-review` after the fix commit. The re-run is free and catches exactly this class of regression.

## Related
- Pattern [[../patterns/iterate-to-clean-n-run-review]] — the re-run policy that caught this
- Pattern [[../patterns/raf-visibility-guard-for-conditionally-hidden-parents]] — the underlying BUG-5 fix
