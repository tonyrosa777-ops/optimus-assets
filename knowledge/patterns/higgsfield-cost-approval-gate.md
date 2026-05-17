# Pattern: Higgsfield Cost-Approval Gate

**Category:** AI Assets / Cost Engineering / Workflow Discipline
**First codified:** 2026-05-17 (post-Goddu Imprint v1+v2 credit-burn pattern)
**Status:** ACTIVE — binding on every Higgsfield generate_image / generate_video call across every Optimus skill and workflow.

## What

A three-step pre-spend gate (Step 0 + Step 1 + Step 2) plus a zero-credit **SIMULATION STEP** that runs inside each skill before any video-generation call. The gate is the discipline that survived Goddu v1+v2 — where composition drift on a premium model burned ~50 credits before the orchestrator noticed. The simulation step is the upstream check the gate enforces: catch the prompt failure in text, before any credits are spent.

The gate has three real steps + one upstream check it enforces:

- **Step 0 — Active-skill confirmation** (always runs, applies to images + video)
- **Step 1 — Balance check** (video-generation only; the 6 permanent unlimited image models skip)
- **Step 2 — High-cost alert** (single calls >50 credits OR batch totals >50 credits; Cinema Studio V2 at 25-45 cr is exempt)
- **The SIMULATION STEP** — lives in the skill workflow; the gate verifies its output before allowing video generation

## When to Use

Every `mcp__higgsfield__generate_image` or `mcp__higgsfield__generate_video` call across every Optimus skill, workflow file, or ad-hoc invocation. No exceptions for client builds. The only skip-zone is personal experiments outside client deliverables — and even then, the discipline catches expensive mistakes early.

## How

### Step 0 — Active-skill confirmation (always runs)

Before any other step runs, the orchestrator (or the skill itself if invoked directly) identifies which Higgsfield skill matches the current task:

- Hero video for an Optimus client build → `~/.claude/skills/optimus-higgsfield-hero-video/SKILL.md`
- Ad creative for paid social / Marketing Studio → `~/.claude/skills/optimus-higgsfield-ad-creative/SKILL.md`
- Soul ID training or generation with a trained character → `~/.claude/skills/optimus-higgsfield-soul-character/SKILL.md`
- Routing question / unclear intent → `~/.claude/skills/optimus-higgsfield-route/SKILL.md` first, then matched skill

Then confirm:

1. **The matching skill file has been read in full this session.** If not, HALT, read the skill, restart the skill's workflow from the top.
2. **All pattern docs in the skill's `<integration>` section have been read this session.** If not, read them now.
3. **If no skill matches the task** — HALT, ask the user which skill applies before proceeding. Never proceed past Step 0 without an active confirmed skill.

This step has no API call and costs nothing. It catches the most common credit-waste pattern: agent or orchestrator jumps straight to `mcp__higgsfield__generate_*` without loading the corrected approach from the skill suite.

### Step 1 — Balance check (video generation only)

Skip for image generation with the 6 permanent unlimited models (see Skip Conditions below). For all video generation and for paid image models (Soul 2, Soul Cinema, Marketing Studio Image, etc.):

```
balance = mcp__higgsfield__balance()
if balance < 100:
  surface to user:
    "⚠️ Credits low ([balance] remaining). Confirm before proceeding (y/n)."
  WAIT for explicit user confirmation. Do not auto-proceed.
```

If balance is 100+, proceed silently to Step 2.

### Step 2 — High-cost alert (single call >50 cr OR batch total >50 cr)

Look up the planned model in `higgsfield-model-selection-matrix.md`. If the cost column is `>50 cr` per call:

```
surface to user:
  "This generation costs ~[N] cr. Current balance [balance] cr. Confirm (y/n)."
```

**Cinema Studio V2 at 25-45 cr is EXEMPT** — it is the expected default video tool. Step 2 does not trigger for Cinema Studio V2 single calls. Models that DO trigger Step 2: Veo 3 (58 cr), Sora 2 (40-70 cr), Cinema Studio 3.5 (30-50 cr at the upper end), Marketing Studio Video at long durations (25-60 cr at the upper end).

**For batch / multi-call generations** (storyboard endpoints, multi-variant ad pools, multi-shot pipelines), the threshold is checked against the **TOTAL batch cost**, not the per-call cost. A batch of 4 Cinema Studio V2 shots at 35 cr each = 140 cr total → Step 2 triggers, surface total + confirm batch. A batch of 3 Marketing Studio Video ad variants at 35 cr each = 105 cr total → Step 2 triggers.

### The SIMULATION STEP (zero-credit, replaces all "draft model" routing)

Sits inside each skill's workflow between "prompt is finalized" and "generate_video is called." The gate at Step 0 verifies that a passing simulation exists before allowing the call to proceed. Image generation is exempt — zero-cost retake on unlimited models means the simulation overhead isn't worth it.

The skill writes the simulation result to `<project>/.higgsfield-pilot/simulation-<timestamp>.md` (or to stdout / a conversation-block if the project has no `.higgsfield-pilot/` dir). This is the **verifiable artifact** the gate looks for:

```markdown
# Simulation — <skill-name> — <model> — <timestamp>

## Prompt
<verbatim final prompt about to be sent>

## Frame 0s
<composition, lighting, subject positions>

## Frame 3s
<what has changed; is motion readable yet?>

## Frame 7s
<mid-point; composition drift check>

## Frame 10s
<end-frame; matches start-frame for loop / matches still for freeze?>

## Gap analysis
- Motion readable in 1-2s: PASS / FAIL — <reasoning>
- Text overlay zone present: PASS / FAIL — <reasoning>
- No AI-slop triggers: PASS / FAIL — <reasoning>
- End-frame matches loop intent: PASS / FAIL — <reasoning>
- Brand register holds across 10s: PASS / FAIL — <reasoning>

## Result
ALL PASS → proceeding to generate.
-or-
GAP DETECTED → fixed prompt, re-simulating (attempt N).
```

**Gate verification at Step 0:** before allowing the `generate_video` call to proceed, the gate confirms the most recent simulation file in `<project>/.higgsfield-pilot/` has a `## Result` line reading `ALL PASS → proceeding to generate.` AND its `## Prompt` block matches the prompt about to be sent (string compare). If no simulation file exists, or its Result is GAP DETECTED, or its prompt doesn't match → HALT, instruct skill to re-run simulation.

**Post-generation divergence logging.** After generation, the skill compares actual output frames (extracted via ffmpeg at 0s / 3s / 7s / end) against the simulation predictions. Significant divergence — composition drift, motion mismatch, slop triggered that simulation said wouldn't appear — is appended to `C:\Projects\Optimus Assets\knowledge\errors\higgsfield-prompt-simulation-divergences.md` per the format documented in that file. The skill writes the entry inline at the end of its visual-review step. Quarterly, the divergence log is triaged into `higgsfield-mcsla-prompt-mastery.md` as new anti-patterns or watch-outs.

### 3-5-attempt escalation (referenced from each skill's visual review step)

If the visual review fails after 3-5 attempts with prompt fixes guided by simulation gap analysis, the skill escalates to a paid troubleshooting alternative:

- **Hero video:** try Kling 3.0 (`kling3_0`, 6-7 cr/5s) with the same prompt. If Kling succeeds, the failure was Cinema Studio model-specific, not a prompt failure. Log the specific prompt + failure mode to `knowledge/errors/higgsfield-prompt-simulation-divergences.md` as a Cinema Studio limitation entry.
- **Ad creative:** try Seedance 2.0 (`seedance_2_0`, 25 cr) with the same prompt. Reference-driven model may handle composition better for product-heavy ads.
- **Soul-character video:** try Kling 3.0 with the Soul ID still as `start_image`. Kling's identity consistency may outperform Cinema Studio for character-driven shots.

After 3-5 attempts on the troubleshooting model also fail, **halt and surface to the user** with: the original prompt, all attempt results, and a recommendation to redesign the composition from scratch using a different pattern from `higgsfield-mcsla-prompt-mastery.md`. Never silently burn credits iterating past 5 total attempts across all models.

Each skill's visual review step prepends `Attempt [N] of 5.` and appends the escalation block.

---

## Skip conditions

Image generation with the 6 permanent unlimited models bypasses Steps 1+2 entirely. Step 0 (skill read) always runs:

- `flux_2` (FLUX.2 Pro) — 365 unlimited on Plus tier, auto-renewing
- `nano_banana_pro` (Nano Banana) — 365 unlimited on Plus tier, auto-renewing
- `gpt_image_2` (GPT Image) — 365 unlimited on Plus tier, auto-renewing
- `seedream_4_5` (Seedream 4.5) — 365 unlimited on Plus tier, auto-renewing
- `seedream_5_lite` (Seedream V5 Lite) — 365 unlimited on Plus tier, auto-renewing
- `kling_o1_image` (Kling O1 Image) — 365 unlimited on Plus tier, auto-renewing

The exemption list lives in `higgsfield-model-selection-matrix.md` cost columns marked `0 (365 unlimited on Plus tier — auto-renewing)`. The gate doc references the matrix as the source of truth — never hard-code the list in two places. If a model becomes permanently unlimited later, the matrix row gains a `0 (365 unlimited)` cost and the gate exemption follows automatically.

**No beta-trial / temporary-unlimited language anywhere in this gate doc or any skill.** The permanent workflow tracks permanent prices only. Trial-state changes are silently absorbed by Step 1 balance check.

---

## How to integrate into a skill (the one-line inline pointers)

Each Higgsfield skill places concise inline pointers at the relevant workflow positions. These point back here for the full spec — never duplicate the gate logic in a skill.

| Skill position | Inline pointer |
|---|---|
| Top of skill body, before `<process>` | "MANDATORY FIRST ACTION: Read this skill file in full before doing anything else. Per `higgsfield-cost-approval-gate.md` Step 0." |
| Pre-flight (after existing checks) | "Balance check per gate Step 1: `mcp__higgsfield__balance() >= 100`; if below, warn+confirm. See `higgsfield-cost-approval-gate.md`." |
| After prompt is finalized, before any generate_video call | "Run SIMULATION step per `higgsfield-cost-approval-gate.md`. Write `<project>/.higgsfield-pilot/simulation-<timestamp>.md` with the 4 frames + 5-criterion gap analysis. Only proceed when Result is ALL PASS." |
| Before any generate_video call to a model >50 cr | "High-cost alert per gate Step 2: surface model + cost + balance, confirm before proceeding. Cinema Studio V2 at 25-45 cr is EXEMPT." |
| Before any batch / multi-call generation | "Batch total check per gate Step 2: sum the per-call costs across the batch; if total >50 cr, surface total + confirm batch." |
| Visual review step | "Attempt [N] of 5. After 3-5 failed attempts, escalate per the gate doc 3-5-attempt block." |
| Bottom-of-skill provider-abstraction note | "fal.ai retired 2026-05-17. If Higgsfield MCP unavailable: any text-to-image generator with same prompt as one-off. For video, Kling AI web UI as last-resort. For programmatic troubleshooting after 3-5 Cinema Studio failures, Kling 3.0 and Seedance 2.0 via the Higgsfield MCP per the escalation block." |

---

## Key Rules

- **Simulate before spending.** The single highest-leverage discipline in the gate. Cinema Studio V2 produces unusable output ~30-40% of the time on first call; the zero-credit text simulation catches the prompt failure before the credits are spent. Required upstream of every generate_video call.
- **Cinema Studio V2 is the permanent video default.** It does NOT trigger Step 2. Escalate to Kling 3.0 / Seedance 2.0 only after 3-5 failures, never as a draft step.
- **Step 0 always runs.** Image generation with unlimited models is exempt from Steps 1+2, but Step 0 (skill read) never skips. Most credit-waste comes from skipping the skill, not from missing the cost check.
- **Batch totals trigger Step 2, not per-call cost.** A batch of small calls can easily exceed the 50 cr threshold while every individual call is under it.
- **Divergence logging is non-optional.** Every post-generation comparison gets logged when the actual output deviates significantly from the simulation. Quarterly triage feeds back into `higgsfield-mcsla-prompt-mastery.md` as anti-pattern guidance.
- **No conditional date logic.** Claude cannot reliably check the current date. The workflow tracks permanent prices only.

## Reuse Condition

Every Higgsfield generate call across every Optimus skill, workflow file, project, and personal-experiment context. The gate is the discipline that makes the unlimited Plus tier actually unlimited — without it, the 1000 cr/month video budget burns in days to wrong-prompt iterations.

## Related

- `higgsfield-model-selection-matrix.md` — source of truth for which models are unlimited / paid + cost columns
- `higgsfield-mcsla-prompt-mastery.md` — prompt structure + named patterns + brand registers (the upstream that the simulation step gap-analyzes against)
- `higgsfield-camera-vocabulary.md` — camera move reliability hierarchy (informs the "motion readable in 1-2s" gap criterion)
- `ai-video-slop-avoidance-checklist.md` — informs the "no AI-slop triggers" gap criterion
- `higgsfield-prompt-simulation-divergences.md` (error ledger) — destination for post-generation divergence logging
- `~/.claude/hooks/higgsfield-credit-gate.sh` — PreToolUse hook that surfaces the 3-question checklist before any generate call; non-blocking, discipline is in the skill
- `~/.claude/skills/optimus-higgsfield-hero-video/SKILL.md` — integrates this gate per the table above
- `~/.claude/skills/optimus-higgsfield-ad-creative/SKILL.md` — integrates this gate per the table above
- `~/.claude/skills/optimus-higgsfield-soul-character/SKILL.md` — integrates this gate per the table above
- `~/.claude/skills/optimus-higgsfield-route/SKILL.md` — routes to the right skill before any gate step runs
