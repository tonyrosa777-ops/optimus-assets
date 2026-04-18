# Claude Design — Potential Workflow Integration (Pattern #50)

**Status:** FORWARD-REFERENCE. Not yet integrated into any Optimus build. Pilot first, codify after validation.

**Established:** 2026-04-17 (launched same day as Opus 4.7)
**Availability:** Research Preview for Pro / Max / Team / Enterprise plans (Anthony has access)
**Product URL:** claude.design

## What Claude Design is

Anthropic's new prototyping + visual-design product, powered by Opus 4.7's vision model.

Core capabilities:
- Generates visual artifacts from text descriptions: prototypes, slides, one-pagers, mockups.
- Refines via chat, inline comments, direct text editing, and auto-generated adjustment sliders for spacing / color / layout.
- **Reads a codebase + design files to build a design system** (colors, typography, components), then applies that system consistently to every subsequent project.
- Exports to PDF, shareable URL, PPTX, or sends to Canva.
- **Hands off to Claude Code with a single instruction** — creating a closed exploration → prototype → production-code loop inside the Anthropic stack.

## Why this matters for Optimus specifically

Current Optimus workflow has three friction points Claude Design could target:

1. **No pre-sales visual asset.** [gap-analyzer](.claude/agents/sales/gap-analyzer.md) produces a text-only gap analysis. Sales Pattern S9 (gap analysis as demo opener) runs on verbal delivery alone. A prospect gets nothing to screenshot or forward to their partner after the first call.

2. **No pre-scaffold visual approval.** [design-synthesizer](.claude/agents/onboarding/design-synthesizer.md) outputs design-system.md (a markdown file the client cannot visualize). Client sees the actual design for the first time in the live demo — after ~8 hours of build. Mid-build color/typography/layout revisions become rebuild cycles.

3. **10-concept hero exploration is text-only.** [animation-specialist](.claude/agents/build/animation-specialist.md)'s 10-concepts→critic→winner round happens as written concept descriptions. A harsh critic scoring "forge embers rising" vs "steel hammer arc" in prose is guessing at visual impact. Visual concepts would be easier to pick from.

Claude Design addresses all three.

## Three candidate fits (ranked by value × viability)

### Fit #1 — Pre-scaffold homepage mockup (highest leverage)

**Where it slots:** New gate between Stage 1B (design-synthesizer) and Stage 1C (scaffold) in [project-prime.md](project-prime.md).

**Flow:**
1. design-synthesizer produces design-system.md as today.
2. Orchestrator hands design-system.md + initial-business-data.md + website-build-template.md to Claude Design.
3. Claude Design generates a visual homepage mockup reflecting the brand constitution.
4. Anthony reviews, iterates with client if time permits (OR pre-approves solo).
5. Claude Design's handoff bundle → Claude Code (Stage 1C+ scaffold agents build TO the approved visual, not build-and-iterate).

**Expected win:** fewer mid-build revisions. Current builds average 3-5 color/typography/layout revision commits post-scaffold. If mockup approval is upstream, those cycles collapse.

**Risk:** if Claude Design's handoff-to-Claude-Code produces slop, the "build to mockup" step devolves into reverse-engineering bad code. Must test on one pilot first.

### Fit #2 — Pre-sales pitch deck (lowest risk, fastest payoff)

**Where it slots:** new sales-phase step, after gap-analyzer runs and before the first call.

**Flow:**
1. gap-analyzer produces gap-analysis-[prospect].md as today.
2. Orchestrator hands that file + the prospect's current site URL + Optimus pricing structure to Claude Design.
3. Claude Design produces a 5-6 slide PDF: cover → gap #1-6 visual → competitor side-by-side → mockup of what Optimus would build → pricing tiers → close CTA.
4. Anthony attaches PDF to the discovery email OR brings to the sales meeting.

**Expected win:** makes Sales Pattern S9 (gap analysis as demo opener) into a tangible artifact prospect can forward, screenshot, or share internally. Also: demo-opener becomes deck-reviewed, not narrated-cold.

**Risk:** low. Deck is internal sales collateral — if quality is mediocre, Anthony just doesn't send it. No client-facing exposure without human gate.

### Fit #3 — Visual 10-concept hero exploration (medium leverage)

**Where it slots:** inside animation-specialist Step 1 (brainstorm 10 concepts).

**Flow:**
1. animation-specialist reads design-system.md + business type + brand personality axes as today.
2. Instead of writing 10 text concepts, spawns Claude Design to produce 10 visual concepts directly.
3. Harsh critic scores the 10 VISUAL outputs on niche relevance / impact / feasibility / uniqueness.
4. animation-specialist builds the winner in Next.js + canvas.

**Expected win:** concept selection becomes visual, not textual — harder for a bad concept to win on "sounds good" prose. Token-burn reduction at `effort: xhigh` on the brainstorm round.

**Risk:** Claude Design may not render canvas-animation-appropriate concepts well (the tool is prototype-focused, not motion-focused). Validate on one pilot — if the 10 outputs look like static website sections rather than animation concepts, revert to text brainstorm.

## Non-fits — explicitly out of scope

- **Production code.** Claude Code stays the builder. Claude Design hands OFF to Claude Code; it does not replace it.
- **Copy / voice.** content-writer stays the writer. Claude Design handles visual, not words.
- **Complete site builds.** Optimus ships Next.js + TypeScript + Tailwind + Framer Motion — Claude Design isn't positioned as a full-stack builder and forcing it there would regress the stack.
- **Design-system.md authorship.** design-synthesizer stays the author — its research-backed synthesis from market-intelligence.md + initial-business-data.md is irreplaceable by prompt-to-visual.

## Tradeoffs before codifying

1. **Research Preview status.** Feature surface may change. Any rules baked into CLAUDE.md or project-prime.md this week could be invalidated by a Claude Design update. Forward-reference only until it exits preview.

2. **[Optimus Positioning Rule](../../CLAUDE.md) quality fit (Pattern #49).** Must verify Claude Design outputs land in the luxury-modern-2026-conversion family, not generic AI aesthetic. If the tool defaults to purple-gradient-on-white or Bootstrap-navy-with-rounded-cards, it violates positioning regardless of convenience. Pilot output must pass the [optimus-luxury-modern-positioning.md](optimus-luxury-modern-positioning.md) visual sniff test.

3. **Design-system.md ingestion fidelity.** Claude Design claims it reads codebase + design files to build a consistent design system. Unknown whether that works on our markdown-formatted design-system.md (vs. Figma files or code). If it doesn't understand our format, every project starts from scratch inside Claude Design — kills the efficiency case.

4. **Handoff-to-Claude-Code quality.** New feature, no public track record. If the handoff bundle produces Next.js code that needs 50% rewrite, the "closed loop" becomes two-loops-plus-cleanup.

5. **Free-tier metering.** Usage quota unclear in early coverage. If Claude Design consumes the same 3-per-session budget as `/ultrareview`, Phase 1J could get starved. Measure on first pilot.

6. **Client visibility of mockups.** If Anthony shows a Claude Design mockup to a client BEFORE payment, the mockup becomes a promise. Client sees X in the mockup, then final build produces Y — trust cost. Mitigation: mockups are internal-only until design approval is formally gated in the sales flow, OR the mockup IS the deliverable approved in writing.

## Pilot plan (not yet executed — here for when we're ready)

**Pilot 1 — Fit #2 (lowest risk first):**
- Next prospect that enters gap-analyzer: generate a Claude Design pitch deck from the gap analysis output.
- Success criteria: Anthony rates the deck 7+/10 on "would I actually send this to a prospect." If yes, Fit #2 becomes standard for future sales.
- Measurement: time to produce (target < 15 min), quality (subjective 1-10), did the prospect reference it in the call?
- No workflow change — this is a sales-side experiment.

**Pilot 2 — Fit #1 (if Pilot 1 works):**
- Next real client build after Pilot 1: run design-synthesizer as today, then feed design-system.md to Claude Design, produce a homepage mockup.
- Success criteria: mockup passes Optimus Positioning sniff test AND handoff bundle produces scaffoldable code.
- If both pass: propose new Stage 1B.5 (visual approval gate) in project-prime.md.
- If either fails: note the failure mode in this file, close the pilot, revisit after next Claude Design update.

**Pilot 3 — Fit #3 (lower priority, only if Pilot 1+2 validate quality):**
- Optional. Canvas-animation output quality is the hardest test for Claude Design's scope.

## When to re-evaluate this pattern

- Claude Design exits Research Preview → re-read release notes, pilot if materially improved.
- A specific Optimus-build pain point that one of these three fits would have prevented arises → accelerate pilot timeline.
- A competing tool (Figma Make, Lovable, v0.dev) ships a better version of the pipeline → pilot that instead.

## Related patterns
- `knowledge/patterns/optimus-luxury-modern-positioning.md` (#49) — positioning gate any Claude Design output must pass
- `knowledge/patterns/opus-4-7-api-migration-checklist.md` (#48) — the other forward-reference pattern from this era
- `knowledge/patterns/opus-4-7-prompt-tuning.md` (#47) — prompt retrofit that made Claude Design possible upstream
- `knowledge/sales/sales-patterns.md` S9 — the gap-analysis-as-demo-opener pattern Fit #2 would augment

## Related errors to watch

If we ever pilot Fit #1 and encounter the mockup-to-code slop scenario, log it as a new Error Encyclopedia entry (`claude-design-handoff-slop.md` or similar). That'll tell future us the pipeline isn't ready.
