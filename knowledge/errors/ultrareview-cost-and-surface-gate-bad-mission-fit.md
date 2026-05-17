# Error: `/ultrareview` cost + surface gate bad mission fit for Optimus
**Project:** Goddu Imprint
**Date:** 2026-05-17
**Phase:** Stage 1J — final code review gate

## Problem
Stage 1J in `project-prime.md` (originally specced at the 2026-04-17 Opus 4.7 retune) called for invoking Claude Code's `/ultrareview` slash command — a cloud-side multi-agent review at the final pre-launch gate. Three structural fits Optimus could not accept were discovered only when trying to use it on Goddu Imprint:

1. **3 free runs lifetime per account**, then $5–$20 per run via "extra usage" billing — Optimus ships multiple client builds per quarter, so the per-client cost would compound indefinitely.
2. **CLI-only.** Not available in the VSCode native extension where most build work happens. The orchestrator can't invoke it programmatically.
3. **No project knowledge.** Cloud agent can't read CLAUDE.md, design-system.md, or `00 — Empire Index/absolute-rules-index.md` — meaning the gate structurally cannot catch the Optimus-specific failures (em-dashes, hero violations, missing testimonials, AEO gaps) the rest of the workflow relies on.

The Stage 1J pattern was specced before any of these structural fits were tested. Goddu hit all three: VSCode extension said "`/ultrareview` isn't available in this environment," and the cost/quota gate violated the "world's newest tech to SMBs at affordable prices" mission.

## Root Cause
At spec time (Apr 17 retune), `/ultrareview` was treated as a free Claude Code feature without verifying:
- Plan-tier gating (Pro/Max only, free runs capped lifetime)
- Surface gating (CLI vs VSCode extension vs other surfaces)
- Project-context isolation (no CLAUDE.md visibility)

Once any one of these surfaces, the gate fails for an entire client build with no graceful path forward beyond "skip Stage 1J and run a manual review."

## Solution
Built a local replacement `/optimus-review` skill — multi-agent code review using subagents on the orchestrator's own infrastructure. 8 parallel Sonnet 4.6 specialists + 1 Opus 4.7 verifier. Unlimited reruns, ~$1–4 per run, project-aware.

Architecture documented in [[../../optimus-review-skill.md]] and [[../patterns/stage-1j-pre-launch-gate]].

## Prevention
Before adopting any Claude Code or Anthropic CLI-introduced workflow gate, verify:
- Plan-tier gating (free vs Pro/Max vs paid)
- Surface availability (CLI, VSCode, JetBrains, web — does it work on the surface the orchestrator runs from?)
- Per-invocation cost model and any usage quotas
- Project-context access (can it read CLAUDE.md? Project-local config? Vault references?)

If any of these fail mission fit, build a local equivalent BEFORE codifying the gate in `project-prime.md`. The cost of building locally is amortized across every future client; the cost of paying Anthropic per-client compounds forever.

## Related
- Pattern [[../patterns/stage-1j-pre-launch-gate]] — the gate as a stage (tool-agnostic)
- [[../../optimus-review-skill.md]] — full architecture of the local replacement
- Pattern [[../patterns/optimus-review-multi-agent-code-review-skill]] — skill architecture summary
