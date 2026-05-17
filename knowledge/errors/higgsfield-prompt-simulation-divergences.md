# Higgsfield Prompt Simulation Divergences — Append-Only Ledger

**Category:** AI Assets / Prompt Discipline / Quality Gate
**First codified:** 2026-05-17
**Status:** ACTIVE — append-only ledger; quarterly triage into `knowledge/patterns/higgsfield-mcsla-prompt-mastery.md` as new anti-patterns or watch-outs.

## Purpose

This file is the destination for post-generation divergence logging required by the cost-approval gate's SIMULATION step (per `knowledge/patterns/higgsfield-cost-approval-gate.md`). Every Higgsfield video generation runs a zero-credit text-based simulation BEFORE the generate call fires. After generation, the skill compares the actual output (4 frames extracted via ffmpeg at 0s / 3s / 7s / end) against the simulation's predictions. Significant divergence — composition drift, motion mismatch, slop triggered that simulation said wouldn't appear — is logged here.

Over time, this ledger surfaces patterns:
- Which compositions Cinema Studio V2 consistently struggles with
- Which prompt patterns simulation predicts accurately vs. miss
- Which brand-register references hold across the simulation → generation gap and which drift
- Which models (Cinema Studio V2 vs. Kling 3.0 vs. Seedance 2.0) actually produce what the prompt asks for

Quarterly triage promotes recurring failure modes into `higgsfield-mcsla-prompt-mastery.md` as named anti-patterns + into `higgsfield-camera-vocabulary.md` as reliability-hierarchy updates.

## When to write to this file

The orchestrator (or invoked skill) writes a new entry whenever:
- Actual generation diverges meaningfully from the simulation's `## Frame X` predictions
- An AI-slop trigger the simulation said "PASS" actually appears in the output (composition drift, hand glitch, garbled text, etc.)
- A camera move described in the prompt produces materially different motion than simulation predicted
- A brand register name in the prompt produces a different visual register in the output
- 3-5-attempt escalation fires (Cinema Studio failed despite simulation-guided prompt fixes)

Do NOT write an entry for:
- Aesthetic preferences that differ but don't represent failure (the simulation said "warm lighting" and the output IS warm but slightly cooler than imagined — that's fine)
- First-pass success that matches simulation predictions (this is the expected case and doesn't need logging)
- Image generation (simulation step doesn't apply to images — they're unlimited and free to retake)

## Entry format

```markdown
## YYYY-MM-DD HH:MM — <skill-name> — <model>

### Prompt
<verbatim final prompt that was sent>

### Simulation prediction (4 frames + 5-criterion result)
Frame 0s: <what simulation predicted>
Frame 3s: <what simulation predicted>
Frame 7s: <what simulation predicted>
Frame 10s: <what simulation predicted>

Gap analysis result: ALL PASS (or list which criteria simulation said FAIL — should be empty for entries logged here, since FAIL would have blocked the generate call)

### Actual output (4 frames described)
Frame 0s: <description of actual frame 0s screenshot>
Frame 3s: <description>
Frame 7s: <description>
Frame end: <description>

### Divergence type + pattern lesson
- **Divergence type:** [composition drift / motion mismatch / slop triggered / camera-move mismatch / brand-register drift / other]
- **Specific divergence:** <what differed>
- **Hypothesized cause:** <what about the prompt or model produced this>
- **Pattern lesson for future prompts:** <generalizable lesson that could feed into mcsla-prompt-mastery anti-patterns>
- **Skill attempt count at failure:** [N of 5]
- **Escalation taken:** [none / escalated to Kling 3.0 / escalated to Seedance 2.0 / halted to user]
```

## Quarterly triage process

Every 3 months (or when the ledger exceeds ~20 entries):
1. Read all entries written since last triage.
2. Group by divergence type and by model.
3. Identify clusters — same failure mode appearing 3+ times = candidate for promotion to `higgsfield-mcsla-prompt-mastery.md` as a named anti-pattern.
4. Identify model-specific clusters — same model consistently failing on the same composition class = candidate for `higgsfield-camera-vocabulary.md` reliability-hierarchy demotion + a routing note in `higgsfield-model-selection-matrix.md` "When to avoid" column.
5. Identify prompt patterns that consistently SUCCEED across many entries — these are confirmation, not failure-driven learning, but worth promoting into mcsla-prompt-mastery as "validated patterns" so they get reused.
6. Archive triaged entries to a yearly subfile (`higgsfield-prompt-simulation-divergences-2026.md`) so the active ledger stays scannable.

---

## Entries

(append below — newest at top)

<!--
EXAMPLE ENTRY (delete this comment block once first real entry is written):

## 2026-06-15 14:32 — optimus-higgsfield-hero-video — cinematic_studio_video_v2

### Prompt
[verbatim prompt]

### Simulation prediction
Frame 0s: Warm walnut desk with pen in foreground, tumbler background-right, Pantone book at right edge. Golden-hour light from upper-left, soft shadows.
Frame 3s: Slow dolly-in continues. Pen stays foreground. Light has warmed ~15% as cloud passes outside window.
Frame 7s: Composition holds. Slight specular glide on pen's gold accent.
Frame 10s: End-frame matches Frame 0s for seamless loop.

Gap analysis: ALL PASS.

### Actual output
Frame 0s: Composition matches simulation closely.
Frame 3s: DRIFT — tumbler has shifted ~10% to the left. New small object (a notebook?) has appeared at lower-right.
Frame 7s: DRIFT continues — Pantone book is now half off-frame.
Frame end: Composition has drifted ~40% from start — would not loop cleanly.

### Divergence type + pattern lesson
- Divergence type: composition drift
- Specific divergence: Subjects moved despite explicit "what is static" prompt clause; new object appeared
- Hypothesized cause: Cinema Studio V2 with start_image lock still drifts on long static-camera compositions when "what is static" prompt clause is too implicit. Need more aggressive "every visible subject is locked in position" language.
- Pattern lesson: Add explicit "no object enters or leaves the frame at any point during the 10s loop" to negative prompt clause. This is candidate anti-pattern for mcsla-prompt-mastery.md "Composition Drift Prevention" section.
- Skill attempt count at failure: 2 of 5
- Escalation taken: Re-prompted with stronger static-lock language, regenerated as attempt 3, succeeded.
-->
