# Error: CLAUDE.md absolute rule overridden via agent reference-pattern citation

**Project:** Ead Financial
**Date:** 2026-05-08
**Phase:** Stage 1B — design-synthesizer agent + human checkpoint review

## Problem

CLAUDE.md Hero Architecture Rule states verbatim: *"No photos in the hero, ever — a photo placeholder in the hero is a build failure. The client photo belongs in the About section."* That's an absolute rule using the word "ever."

design-synthesizer agent produced design-system.md §5 specifying a **two-column hero with an editorial photo of Johnny in the right panel**, citing market-intelligence.md §8's Claro Advisors reference and the Stage 1A repo scan finding that "every scanned hero is wrong-energy for editorial register." The agent's reasoning was internally consistent: Claro uses single-subject lifestyle photography in the hero; Ead's editorial register matches Claro; therefore Ead's hero takes a photo too.

The orchestrator approved at the Stage 1B human checkpoint. animation-specialist built it as Hero.tsx in Stage 1D (260 lines, fal.ai-placeholder-fallback container, pointer-events-none per build-log #48, the works). User caught the violation at Stage 1D close: *"why are we putting a bio photo in the hero? photo in the hero is only okay if its a movie hero header. we arent doing a box with a photo in the header."*

Net cost: ~3 hours of Stage 1B + 1D work re-spawned, plus the meta-cost of needing a Stage 1B re-review for future builds.

## Root Cause

CLAUDE.md absolute rules ("ever," "always," "never," "non-negotiable") were treated as defaults that reference patterns could override when the agent's chain of reasoning was internally consistent and well-cited. They cannot. The whole point of an absolute rule is that competing arguments don't open it.

Three compounding factors:
1. **Agent reasoning quality masked the violation.** design-synthesizer cited primary sources (market-intelligence.md §8 lines 244–273), framed a deviation rationale (delegating "brand canvas" responsibility to the marquee ribbon), and produced internally consistent §5 prose. The output looked like rigorous synthesis — easy to approve.
2. **Orchestrator did not cross-check against CLAUDE.md absolute rules at the human checkpoint.** The checkpoint reviewed Sections 2 (palette), 6 (photography), 8 (axes), 11 (sections matrix) — not §5 (hero composition) against CLAUDE.md Hero Architecture Rule.
3. **Reference-pattern semantics are seductive.** "Claro does it" reads as evidence; agents and humans both pattern-match on it. But Claro is a reference, CLAUDE.md is the constitution. References inform, they don't override.

## Solution

Two surfaces to fix:

**Immediate (this build):**
- design-system.md §5 corrected to v2 — single-column text-only hero + cream ambient gradient + marquee below. Section 6 photography table retargeted (Hero portrait → About Chapter 1 lead portrait; environmental scenes → mid-page section breaks, NOT page heroes).
- Hero.tsx rewritten — 246 lines, single-column, no photo, single ambient radial-gradient layer.
- Feedback memory written: `~/.claude/projects/c--Projects-John-Ead/memory/feedback_no-photos-in-hero-box.md`.

**Process (every future build):**
- See [[patterns/claude-md-absolute-rule-cross-check-at-checkpoint]] — orchestrator MUST cross-check design-system.md §5 (and any section that touches hero/photo/CTA/conversion-flow) against the corresponding CLAUDE.md absolute rule before approving. The cross-check is a separate verification step, not part of the agent's self-validation.

## Prevention

When an agent's output cites a reference pattern (Claro, Anomaly, AAFCPAs, etc.) to justify a design decision that touches a CLAUDE.md absolute rule:

1. **Identify the absolute rule it touches.** Search CLAUDE.md for the keyword (hero, photo, CTA, deposit, Google, em dash, etc.).
2. **Read the rule's exact language.** Look for "ever," "always," "never," "non-negotiable."
3. **Reject the deviation regardless of citation strength.** Reference patterns inform aesthetic + component choices; they cannot override absolute rules.
4. **Re-spawn the agent with a correction note** if the deviation is structural (per CLAUDE.md Agent System Rules: "Failing agents get re-run with a correction note — not silently passed").

The operational test (per Ead user 2026-05-08): "movie-hero" full-bleed cinematic backdrop where the photo IS the hero canvas may be acceptable in concept. "Box with a photo in the header" — i.e., two-column hero with photo on right — is NEVER acceptable. Reference patterns that look like the second pattern misread the reference; the first is operating in movie-hero mode.

## Related

- [[errors/photo-placeholder-appears-in-hero-instead-of-3-layer-animation-stack]] (Error #28, Helen Grondin) — original instance that produced the absolute rule
- [[patterns/claude-md-absolute-rule-cross-check-at-checkpoint]] — prevention pattern
