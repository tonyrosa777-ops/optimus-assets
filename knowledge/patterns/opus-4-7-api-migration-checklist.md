# Opus 4.7 API Migration Checklist (Pattern #48)

**Trigger condition:** Before shipping any code that imports `@anthropic-ai/sdk` or otherwise calls the Anthropic API directly. Applies to: n8n Claude nodes, Retell voice-AI context prompts, future AI Chat Assistant upsell, API-in-Artifacts code, any custom backend that calls Claude.

**Date established:** 2026-04-17 (reference doc created during Opus 4.7 workflow retune; Optimus has no API-client code today, so this pattern is forward-only).

## Breaking changes — these will 400 your calls

1. **`temperature`, `top_p`, `top_k` are removed.** Setting any of these to a non-default returns HTTP 400. Omit them entirely; guide behavior through prompting.

2. **`budget_tokens` is removed.** Use the `effort` parameter instead.

3. **Adaptive thinking is off by default.** If thinking is desired, explicitly set `thinking: { type: "adaptive" }`. Requests with no thinking field run without thinking.

4. **Thinking content hidden by default.** The `thinking` field in response streams is empty unless the caller sets `"display": "summarized"`. Any UI that rendered reasoning text needs the opt-in.

5. **Prefill-assistant-message still unsupported.** (Carried from 4.6.) Use structured outputs, system-prompt instructions, or `output_config.format` instead.

## Tokenizer change — budget impact

Opus 4.7 uses a new tokenizer. The same input maps to ~1.0-1.45x more tokens depending on content type. Real-world testing showed 1.47x on technical docs and 1.45x on CLAUDE.md-style files — code-heavy prompt content sits at the upper end.

**Practical mitigations:**
- Bump any `max_tokens` ceilings by ~20% across the board (covers tokenizer inflation + more reasoning at higher effort).
- Cache is partitioned per model — switching from 4.6 to 4.7 invalidates the cached prefix. First session starts cold.
- Budget for ~30-45% rate-limit / session-window consumption faster on code-heavy workloads.

## Model ID

Use `claude-opus-4-7` as the model string. Update any hardcoded `claude-opus-4-6`, `claude-opus-4-5`, older model IDs, and `claude-sonnet-4-5` references EXCEPT where Sonnet is intentional (e.g. cheaper sub-agent work).

## New controls worth using

- `xhigh` effort level — between `high` and `max`. Use for judgment-heavy agentic work. Default in Claude Code.
- Task budgets (public beta) — hard cap on token spend for a full agentic loop. Replaces old `budget_tokens`.
- Vision upgrade — images up to 2576px / 3.75MP supported. ~3x more image tokens at full resolution, but pointing/counting/bounding-box detection is meaningfully better.

## When to invoke this checklist

Before the FIRST commit of any Anthropic-SDK-calling code in the Optimus stack. Tape it to the top of the PR description. Don't re-derive.

## Related patterns
- `knowledge/patterns/opus-4-7-prompt-tuning.md` — prompt-level retrofit (applied during this 4.7 retune; no API code existed to migrate).

## Status
FORWARD-REFERENCE. No current Optimus code calls the Claude API directly as of 2026-04-17. This doc exists so the next AI-integration build (chatbot upsell, n8n Claude node, Retell context) inherits the migration knowledge without rediscovering it.
