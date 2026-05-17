# fal.ai / Kling cleanup + Higgsfield cost-gate audit (RESOLVED)

## Context

Two-part workflow sweep across the Optimus vault + global `.claude/` config:

1. **Part 1 — Replace fal.ai + Kling references in workflow files** with Higgsfield MCP equivalents, now that Higgsfield Plus tier has been confirmed by the founder to ship **unlimited Flux 2 + Nano Banana Pro image generation**. This removes fal.ai's only documented advantage (cost-per-image for non-hero stills, previously ~$0.05/img). When Higgsfield gives the same output for $0 marginal cost, the rational choice is to consolidate on the single platform. fal.ai's blog/gallery role disappears; Kling AI's direct-to-web-UI role consolidates under the Higgsfield Kling 3.0 wrapper.

2. **Part 2 — Build the cost-approval gate + simulation-first discipline into the three callable Higgsfield skills.** The PreToolUse hook (`~/.claude/hooks/higgsfield-credit-gate.sh`) is non-blocking and only injects a checklist reminder. The actual enforcement lives in the skills themselves via three mechanisms: (Step 0) the gate reads the active Higgsfield skill before running, (Step 1) balance check halt+confirm if <100cr, (Step 2) high-cost alert + confirm if a single call would consume >50cr. The Seedance "draft-first" routing originally proposed is **rejected and replaced** by a zero-credit **SIMULATION STEP** — Claude text-simulates a 4-frame storyboard (0s/3s/7s/10s) + 5-criterion gap analysis BEFORE any generate_video call, fixes the prompt, re-simulates, and only generates when the simulation passes. Cinema Studio V2 is the tool, not a "final" step downstream of a draft. Credits are spent once, on the right model, after the simulation passes.

User resolutions captured:
- **Case #1 (fal.ai retention):** Replace everywhere. Founder logic: "if I get unlimited Flux on Higgsfield Plus, why would I still use fal.ai?"
- **Case #2 (Flux 2 + Nano Banana cost):** Confirmed unlimited / 0 credits on Plus tier. Update model-selection-matrix to reflect.
- **Case #3 (gate structure):** Senior-engineer decision delegated to me, with constraint "vault consistency is most important for longevity and autonomous goal." → **Hybrid approach.** One shared pattern doc `knowledge/patterns/higgsfield-cost-approval-gate.md` holds the full spec. Each skill gets a one-line inline checklist at each gate moment that points to the pattern doc. This gets DRY (single source of truth survives skill edits) AND locality (agents see the gate-reminder at the right workflow position without scrolling away).

### Founder amendments (architectural corrections — supersede earlier draft)

The user issued 7 amendments at execution time. Each is binding and overrides anything earlier in this plan that conflicts:

**A1 — No draft-first routing. Replace with SIMULATION STEP.** All "Seedance Fast draft before Cinema Studio final" language is removed everywhere. Replaced by a zero-credit text-based simulation: Claude describes the generation frame-by-frame at 0s / 3s / 7s / 10s, then gap-analyzes the prompt against 5 criteria (motion readability in 1-2s, text overlay zone present, no AI-slop triggers, end-frame matches loop intent, brand register consistent across 10s). Fix prompt → re-simulate → only generate when simulation passes. Post-generation: compare actual frames vs. simulation, log divergences as prompt-pattern failures to the vault.

**A2 — The gate reads the active skill at Step 0.** Before balance check, the gate confirms which Higgsfield skill is active (hero / ad / soul-character) and that the matching skill file has been read this session. If no active skill identified → halt and ask user. Updated PreToolUse hook checklist: first question is "Has the active Higgsfield skill file been read in full this session?" Gate then runs (Step 1) balance halt+confirm <100cr, (Step 2) high-cost alert + confirm >50cr (Veo 3 at 58cr, Sora 2 at 40-70cr trigger; Cinema Studio V2 at 25-45cr does NOT). Unlimited image models skip Steps 1+2 entirely; Step 0 always runs.

**A3 — Escalation after 3-5 failed attempts.** Each visual review step gets an "Attempt [N] of 5" counter + escalation block: after 3-5 Cinema Studio V2 failures with prompt adjustments guided by simulation, escalate to a paid troubleshooting alternative (hero: Kling 3.0 6-7cr; ad: Seedance 2.0 25cr; soul-character: Kling 3.0 + Soul ID start_image). Log the failure mode + prompt as a Cinema Studio limitation error in the vault. After 5 total attempts across all models also fail → halt and surface to user with full attempt log + composition redesign recommendation. Never silently burn credits past 5 attempts.

**A4 — Remove all beta-trial expiration-date logic.** Claude can't reliably check the current date, so conditional date logic is unreliable. Cinema Studio V2 is the permanent default. The matrix retains the Kling 3.0 trial + Nano Banana 2 trial as historical notes only: "Was available free via beta trial May 16-23 2026. Now costs N cr/gen." No expiration date logic in any workflow file or skill. The escalation block (A3) references Kling 3.0 / Seedance 2.0 as troubleshooting alternatives without referencing trial state.

**A5 — Provider abstraction rewrite (3 skills).** Each skill's bottom-of-file provider-abstraction note gets the same new language: "fal.ai retired 2026-05-17. If Higgsfield MCP unavailable: for images, use any text-to-image generator with the same prompt as one-off. For video, Kling AI web UI (kling.ai) is the last-resort manual fallback. For programmatic troubleshooting after 3-5 Cinema Studio failures, Kling 3.0 and Seedance 2.0 are available via the Higgsfield MCP per the escalation block."

**A6 — Audit scope expansion.** Batch 4 must also process `end-to-end-workflow.md`. Batch 7 must process ALL 8 optimus-review agents (correctness, security, architecture, tests, performance, style, absolute-rules, design-system), not just the two named earlier.

**A7 — MANDATORY FIRST ACTION in each skill: read the skill file in full.** Before any pre-flight, brainstorm, prompt, simulate, balance check — read the skill. Add this as the absolute first step in each of the three skills, before the existing pre-flight checklist. Gate pattern doc Step 0 enforces this: if the gate is reached without the skill having been read, halt + restart from skill top. PreToolUse hook checklist updated to mirror.

### Higgsfield Plus subscription — ground truth (founder dashboard 2026-05-17)

User provided dashboard screenshots. The actual subscription state is more nuanced than "Flux 2 + Nano Banana = unlimited"; the matrix update must encode the full table:

**Permanent unlimited (365-day, auto-renewing) — these are the ONLY unlimited models the permanent workflow tracks:**
| Model | Higgsfield label | Matrix `model_id` |
|---|---|---|
| FLUX.2 Pro | `365 Unlimited` Active | `flux_2` |
| Nano Banana | `365 Unlimited` Active | `nano_banana_pro` |
| GPT Image | `365 Unlimited` Active | `gpt_image_2` |
| Seedream 4.5 | `365 Unlimited` Active | not currently in matrix — add `seedream_4_5` row |
| Seedream V5 Lite | `365 Unlimited` Active | `seedream_5_lite` |
| Kling O1 Image | `365 Unlimited` Active | not currently in matrix — add `kling_o1_image` row (image model, not video — distinct from `kling3_0`) |

**No temporary / beta-trial unlimited models tracked.** Per founder instruction 2026-05-17: temporary unlimited windows cause workflow drift (the workflow encodes a free model, the trial expires, the workflow silently starts burning credits). The permanent workflow only references models at their permanent prices. The Higgsfield dashboard's beta-trial widget is for ad-hoc personal use only — never encoded into skills, matrix, or workflow docs.

**Still costs credits (gate applies — permanent prices, no trial logic):**
- Cinema Studio Video V2 (`cinematic_studio_video_v2`) — 25-45 cr — premium, gate required
- Cinema Studio Image (`soul_cinema`) — 2-3 cr — gate disclosure only
- Cinema Studio 3.5 (`cinematic_studio_3_5`) — 30-50 cr — premium, gate required
- Soul 2 / Soul ID training + per-gen — premium for training, disclosure for per-gen
- Marketing Studio Image / Video — 2-5 cr image, 25-60 cr video premium, gate required
- Seedance 2.0 / 2.0 Fast (video) — 25 cr / 17 cr — disclosure required (Fast is the draft tool)
- Veo 3 / Veo 3 Fast — 22-58 cr — premium, gate required
- Sora 2 — 40-70 cr — premium, gate required
- MiniMax Hailuo 02 — 15-25 cr — disclosure required
- WAN 2.5 / 2.6 — 10-18 cr — disclosure required

Plus plan renews May 17, 2027 (renewal date documented at the subscription level — does not change between sessions). Current credit balance should always be checked at runtime via `mcp__higgsfield__balance` before starting a video-gen workflow; the plan does not hardcode a snapshot (any number captured here would be wrong within days).

### Implications this changes in the plan

1. **Use Case D (blog cards) — pick from the 6 permanent unlimited models only.** Default: FLUX.2 Pro for general blog cards. Alternate: Nano Banana Pro for stills with text rendering. Kling O1 Image is the right choice when the still will feed Kling video later (in-family pipeline). All permanent unlimited — no trial-state tracking.
2. **Hero video — Cinema Studio Video V2 is the permanent default at its real price (25-45 cr per gen).** Per A4 the matrix carries no expiration-date logic; per founder instruction the temporary unlimited status of Kling 3.0 is not tracked anywhere in the workflow. Kling 3.0 is a 6-7cr troubleshooting alternative per the A3 escalation block — at its permanent price, every time.
3. **The matrix needs three new rows** (Seedream 4.5, Kling O1 Image, and existing flux_2 / nano_banana_pro / gpt_image_2 / seedream_5_lite cost-column updates). No "historical trial notes" section. No mention of beta trials anywhere.
4. **The cost-gate audit is unchanged.** All the premium video models the gate targets (Cinema Studio V2, Marketing Studio Video, Veo 3, Sora 2, Seedance 2.0) cost credits at their permanent prices. The 6 permanent unlimited image models bypass Steps 1+2; Step 0 (skill read) always runs.

---

## Files to modify (organized by edit batch)

### Batch 1 — New pattern doc (foundation for Part 2) — AMENDED A1+A2+A4+A7

**Create:** `C:\Projects\Optimus Assets\knowledge\patterns\higgsfield-cost-approval-gate.md`

Sections (in order):
- **Why this gate exists** — Goddu v1+v2 credit-burn pattern (composition drift on premium model wasted ~50cr; the SIMULATION step would have caught the drift before any credits were spent).
- **Step 0 — Active-skill confirmation (always runs, applies to images + video).** Identify which Higgsfield skill matches the current task (hero / ad / soul-character). Confirm the matching skill file has been read in full this session. If no skill matches or skill not read: HALT, ask user which skill applies, restart from the top of that skill's workflow. The gate cannot proceed past Step 0 without a confirmed active skill.
- **Step 1 — Balance check (video generation only; unlimited image models skip).** Call `mcp__higgsfield__balance`. If remaining credits <100: halt + warn `⚠️ Credits low ([X] remaining). Confirm before proceeding (y/n).` Never auto-proceed past warning.
- **Step 2 — High-cost alert (single calls >50cr OR batch totals >50cr; Cinema Studio V2 at 25-45cr is EXEMPT and proceeds without confirmation).** If a generation call would consume >50cr (Veo 3 at 58cr, Sora 2 at 40-70cr trigger), surface: `This generation costs ~[N]cr. Current balance [M]cr. Confirm (y/n).` Cinema Studio V2 is the expected default call and does NOT trigger Step 2. **For batch / multi-call generations (storyboard endpoints, multi-variant ad pools, multi-shot pipelines), the threshold is checked against the TOTAL batch cost, not the per-call cost.** A batch of 4 Cinema Studio V2 shots at 35cr each = 140cr total → Step 2 triggers, surface total + confirm batch.
- **The SIMULATION STEP (zero-credit — replaces all "draft model" routing).** Sits inside each skill's workflow, NOT in the gate. The gate doc documents it because every video-gen call must have completed simulation before reaching Step 1. Simulation describes frame 0s / 3s / 7s / 10s, then gap-analyzes prompt against 5 criteria (motion readability in 1-2s, text overlay zone present, no AI-slop triggers, end-frame matches loop intent, brand register holds across 10s). If any gap → fix prompt → re-simulate. Only when simulation passes do credits get spent.

- **SIMULATION OUTPUT FORMAT (verifiable artifact — gate looks for this).** Each skill writes the simulation result to `<project>/.higgsfield-pilot/simulation-<timestamp>.md` (or to stdout / a conversation-block if the project has no `.higgsfield-pilot/` dir). The file is the verifiable artifact:

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

  **Gate verification at Step 0:** before allowing the generate_video call to proceed, the gate confirms the most recent simulation file in `<project>/.higgsfield-pilot/` has a `## Result` line reading `ALL PASS → proceeding to generate.` AND its `## Prompt` block matches the prompt about to be sent (string compare). If no simulation file exists, or its Result is GAP DETECTED, or its prompt doesn't match → HALT, instruct skill to re-run simulation. Image generation with unlimited models is exempt from simulation (zero cost downside on retake).

- **Post-generation divergence logging — destination specified.** After generation, the skill compares actual output frames against simulation predictions. Significant divergence (composition drift, motion mismatch, slop triggered that simulation said wouldn't) is appended to `C:\Projects\Optimus Assets\knowledge\errors\higgsfield-prompt-simulation-divergences.md` per the format spec'd in that file (created in Batch 5). The skill writes the entry inline at the end of its visual-review step.
- **Skip conditions — image generation with unlimited models bypasses Steps 1+2 entirely.** Step 0 (skill read) always runs.
  - Permanent unlimited models (Plus tier 365-day auto-renewing): `flux_2`, `nano_banana_pro`, `gpt_image_2`, `seedream_4_5`, `seedream_5_lite`, `kling_o1_image`. These six are the only exemptions.
  - The exemption list lives in `higgsfield-model-selection-matrix.md` cost columns marked "0 (365 unlimited on Plus tier)". The gate doc references the matrix as the source of truth — never hard-code in two places.
  - No beta-trial / temporary-unlimited language anywhere in this gate doc or any skill. Workflow tracks permanent prices only; trial-state changes are silently absorbed by Step 1 balance check.
- **3-5-attempt escalation (referenced from each skill's visual review step).** After 3-5 Cinema Studio V2 failures, escalate to paid troubleshooting model (Kling 3.0 / Seedance 2.0 / Kling 3.0 with Soul ID per skill). Log Cinema Studio limitation error to vault. After 5 total attempts across all models also fail → halt + surface to user.
- **How to integrate into a skill (one-line inline pointers).** Each skill places a one-line cross-reference at: pre-flight (Step 0 + Step 1), post-prompt pre-gen (SIMULATION reference), pre-generate_video call (Step 2 if >50cr), visual review (attempt counter + escalation).

Also add row to `knowledge/build-log.md` Patterns table as Pattern #85.

Also add row to `knowledge/build-log.md` Patterns table as Pattern #85.

### Batch 2 — Skill simulation + gate integration (Part 2) — AMENDED A1+A2+A3+A5+A7

For each of the three skills, add: MANDATORY FIRST ACTION (A7) → tightened pre-flight (A2 Step 0+1) → SIMULATION STEP (A1) → generate → visual review with attempt counter + escalation (A3). Update provider abstraction note (A5).

**Reading discipline (per founder issue #7 — step numbers in this plan are SHORTHAND, not literal targets):** Claude Code reads each skill file in full at edit time and identifies the correct insertion points by workflow position, NOT by step number. The skills were written in earlier sessions; their internal step numbering may have drifted. Use these workflow-position anchors instead of step numbers:
- "After pre-flight, before any creative work" — MANDATORY FIRST ACTION block goes here (top of skill body, before existing `<process>` block)
- "After Pre-flight Step 1" — tighten existing balance check; insert gate-doc cross-reference
- "After the still has passed visual review AND before the video gen call" — insert SIMULATION STEP (hero + soul-character)
- "After the hook brainstorm AND before the video gen call" — insert SIMULATION STEP (ad-creative)
- "At the visual review step that follows a video gen call" — prepend attempt counter; append escalation block
- "In the `<key_rules_summary>` / `<integration>` / bottom-of-file area" — provider abstraction rewrite

If a skill's workflow has been rearranged since the original session, Claude Code applies the same conceptual edits to whatever the current structure is.

**Modify:** `C:\Users\Anthony\.claude\skills\optimus-higgsfield-hero-video\SKILL.md`
- Insert `<mandatory_first_action>` block at the very top, before `<objective>`: "MANDATORY FIRST ACTION: Read this skill file in full before doing anything else. Do not proceed to Step 1 until this file has been read in the current session. If any pattern doc in `<integration>` has not been read this session, read it now. No exceptions."
- Step 1 Pre-flight: update balance check to `mcp__higgsfield__balance >=100`; if <100 warn+confirm. Add cross-reference: "Gate Step 0 + Step 1 enforced per `knowledge/patterns/higgsfield-cost-approval-gate.md`."
- Step 4 (still gen): if generating via Nano Banana Pro / Flux 2 (unlimited) — no gate block needed. If generating via Marketing Studio Image (~2-5cr) or Soul Cinema (~2-3cr) — insert one-line note: "Per gate pattern: image gen via paid model, balance check from Step 1 still valid."
- **REMOVE the previously-proposed Step 5.5 draft block.** Replace with new Step 5.5 SIMULATION block: "Zero-credit text simulation of the planned video generation. Describe frame 0s / 3s / 7s / 10s + run 5-criterion gap analysis (motion readability in 1-2s / text overlay zone / no AI-slop / end-frame matches loop intent / brand register holds across 10s). If any gap → fix prompt → re-simulate. Only proceed to Step 6 when simulation passes. Full spec in `higgsfield-cost-approval-gate.md`."
- Step 6 (Cinema Studio Video V2 call): NO confirmation prompt for Cinema Studio V2 at 25-45cr (exempted per A2). Inline note: "Cinema Studio V2 is the permanent default — runs without high-cost confirmation. Simulation gate at Step 5.5 is the upstream check."
- Step 7 (visual review): prepend "Attempt [N] of 5." Append escalation block: "If attempts ≥3-5 with prompt fixes guided by Step 5.5 simulation and Cinema Studio still produces unusable output → escalate per `higgsfield-cost-approval-gate.md` 3-5-attempt escalation. Try Kling 3.0 (kling3_0, 6-7cr) with same prompt. If Kling succeeds → log Cinema Studio limitation error to vault. After 5 total attempts across all models → halt + surface to user with full attempt log + recommendation to redesign composition using a different `higgsfield-mcsla-prompt-mastery.md` pattern."
- `<key_rules_summary>` block: REMOVE any "Seedance draft → Kling final" or "Seedance for draft validation" language. Replace cost-reality block with: "Cinema Studio V2 is the tool. Simulate before spending credits. Escalate to Kling 3.0 only after 3-5 Cinema Studio failures."
- `<integration>` block bottom — provider abstraction note REWRITE per A5: "fal.ai retired 2026-05-17. If Higgsfield MCP unavailable: for images, use any text-to-image generator with the same prompt as one-off. For video, Kling AI web UI (kling.ai) is the last-resort manual fallback. For programmatic troubleshooting after 3-5 Cinema Studio failures, Kling 3.0 and Seedance 2.0 are available via the Higgsfield MCP per the escalation block."

**Modify:** `C:\Users\Anthony\.claude\skills\optimus-higgsfield-ad-creative\SKILL.md`
- Insert `<mandatory_first_action>` block at the very top: same A7 language as hero skill.
- Step 1 Pre-flight: balance threshold ≥100, warn+confirm if below. Cross-reference gate doc.
- **REMOVE the previously-proposed Step 3.5 draft block.** Replace with Step 3.5 SIMULATION block: "Zero-credit text simulation of the ad video. For each of the 3 hook variants: frame 0s (HOOK) / frame 1s (HOOK still landing) / frame 3-5s (VALUE BEAT) / frame 5-7s (CTA). Run gap analysis: hook lands in frame 1? sound-off-readable text overlay zone present? CTA frame clear? No AI-slop in the planned shot? Fix prompts → re-simulate. Only proceed to Step 4 when all 3 variants pass simulation."
- Step 4 (Marketing Studio Video call): if model resolves to Marketing Studio Video at 25-60cr → high-cost alert triggers at 51+cr only. Most 9-15s placements land at 25-45cr (no alert). Document inline: "Marketing Studio Video typically 25-45cr per gen — runs without high-cost confirmation. If duration drives cost >50cr, gate Step 2 triggers per `higgsfield-cost-approval-gate.md`."
- Step 5 (visual review): prepend "Attempt [N] of 5." Append escalation block: "After 3-5 failed Marketing Studio Video attempts → escalate to Seedance 2.0 (seedance_2_0, 25cr) with same prompt. Reference-driven model often handles product-heavy ads better. Log failure mode to vault. After 5 total → halt + surface."
- Step 6 (variant batch): REMOVE "variant draft batch via Seedance first" language. Replace with: "Each variant runs the simulation independently. After simulation passes for all 3, generate all 3 variants from the same locked prompts."
- `<integration>` block bottom — provider abstraction note REWRITE per A5: same language as hero skill.

**Modify:** `C:\Users\Anthony\.claude\skills\optimus-higgsfield-soul-character\SKILL.md`
- Insert `<mandatory_first_action>` block at the very top: same A7 language.
- Step 1 Pre-flight: balance ≥100 (matches spec for training), warn+confirm. Cross-reference gate doc.
- Step 3 (training trigger): insert one-time-spend gate block (Soul ID training 50-100cr is a one-time high-cost event — DOES exceed 50cr threshold so Step 2 triggers): "Soul ID training = 50-100cr ONE-TIME spend. Reusable forever at 2-3cr/gen with locked identity. Per gate Step 2: confirm training (y/n). See `higgsfield-cost-approval-gate.md`."
- Step 4 (gen with trained character):
  - Image gen via `soul_2` (~2-3cr) or `soul_location` (~2cr): no gate block needed (under 50cr threshold + balance check from Step 1 still valid).
  - Video gen via `cinematic_studio_video_v2` (~25-45cr): insert pre-call SIMULATION block (A1 — same 4-frame + 5-criterion gap analysis as hero skill). Cinema Studio V2 at 25-45cr does NOT trigger high-cost alert.
  - Add attempt counter + escalation block (A3): "After 3-5 failed Cinema Studio V2 attempts → escalate to Kling 3.0 (kling3_0, 6-7cr) with Soul ID still as start_image. Kling's identity consistency often outperforms Cinema Studio for character-driven shots. Log failure mode to vault. After 5 total → halt + surface."
- Storyboard endpoint workflow position: per-shot SIMULATION block at the same depth as the single-shot generate workflow. **Clarification per issue #8: for batch calls, gate Step 2's 50cr threshold checks TOTAL batch cost, not per-shot cost.** Add explicit gate clarification at the batch surface: "Storyboard batch of N shots at ~Mcr each = ~[N×M]cr TOTAL. Per gate Step 2: if TOTAL >50cr (even when per-shot is <50cr), confirm batch (y/n)." Update the gate doc (Batch 1) to add an inline clarification line at Step 2: "For batch / multi-call generations (storyboard endpoints, multi-variant ad pools), the threshold is checked against the TOTAL batch cost, not the per-call cost."
- `<integration>` block bottom — provider abstraction note REWRITE per A5: same language as hero skill.

### Batch 3 — Model-selection-matrix update (Case #2 resolution, dashboard-aligned, A4-corrected)

**Modify:** `C:\Projects\Optimus Assets\knowledge\patterns\higgsfield-model-selection-matrix.md`

Image-models table — cost-column updates for existing rows:
- `flux_2`: `1.5` → `0 (365 unlimited on Plus tier — auto-renewing)`
- `nano_banana_pro`: `2` → `0 (365 unlimited on Plus tier — auto-renewing)`
- `gpt_image_2`: `1` → `0 (365 unlimited on Plus tier — auto-renewing)`
- `seedream_5_lite`: `~1` → `0 (365 unlimited on Plus tier — auto-renewing)`

Image-models table — NEW rows to add:
- `seedream_4_5` (Seedream 4.5, ByteDance, visual reasoning tier): aspect 16:9/9:16/1:1/4:3/3:4, cost `0 (365 unlimited on Plus tier — auto-renewing)`, when to pick "premium visual-reasoning image gen" / when to avoid "simple stills (Flux 2 is equivalent and faster)"
- `kling_o1_image` (Kling O1 Image, Kuaishou, image model — distinct from `kling3_0` video): aspect 16:9/9:16/1:1, cost `0 (365 unlimited on Plus tier — auto-renewing)`, when to pick "cinematic-register stills that will be animated by Kling video later (in-family pipeline)" / when to avoid "non-Kling video pipelines"

**Do NOT add a `nano_banana_2` row.** Per founder instruction, no trial-related entries in workflow files. A "never use this" row adds confusion, not clarity. If the model becomes permanent unlimited later, the matrix gains a row at that point.

Video-models table — `kling3_0` cost-column at base rate (no date logic, no trial language):
- `kling3_0`: cost stays `6-7 (5s @ 720p)`. Add note in "When to pick" column: "Troubleshooting alternative after 3-5 failed Cinema Studio V2 attempts (per cost-approval-gate escalation block). Excellent face / lip-sync, best for character-driven shots." Add note in "When to avoid" column: "Promoting to workflow default — Cinema Studio V2 is the permanent default per skills."

Use Case D (Blog cards) — rewrite entirely:
```
### Use case D: Blog card images, article headers, social tiles (Optimus client builds)

**Flow:**
1. **Default: Higgsfield FLUX.2 Pro** (model: flux_2) via mcp__higgsfield__generate_image, aspect 16:9 (header) or 1:1 (card). 0 cr — unlimited on Plus tier (365-day, auto-renewing).
2. **For stills with text rendering** (signage, packaging mockups, social tile with logo + headline): Nano Banana Pro (model: nano_banana_pro). Also 0 cr unlimited on Plus.
3. **For premium-reasoning composition** (complex multi-subject scenes): Seedream 4.5 (model: seedream_4_5). Also 0 cr unlimited.
4. **Never use:** Nano Banana 2 (use original Nano Banana Pro as permanent default instead) or paid-credit models (Soul 2, Marketing Studio Image) for blog cards — overspec'd by 4-10x AND/OR cost credits unnecessarily.
5. **Total cost: $0 marginal at Plus tier.** fal.ai retired as the blog-image default as of 2026-05-17 (founder confirmation: Higgsfield Plus tier ships 6 permanent unlimited image models, removing fal.ai's cost-per-image advantage).
```

Cost matrix table sort (sorted by Plus-tier output per $1): two categories only — (1) the 6 unlimited models at the top as "0 cr — unlimited on Plus" rows (Flux 2, Nano Banana Pro, GPT Image, Seedream 4.5, Seedream V5 Lite, Kling O1 Image), (2) per-credit models below sorted by cost ascending. No beta-trial category.

Provider abstraction note — rewrite:
- Remove: "Keep fal.ai (`flux-pro/v1.1`) as documented blog-image fallback"
- Replace with: "fal.ai retired 2026-05-17 — Higgsfield Plus tier ships 6 permanent unlimited image models, removing fal.ai's cost advantage. If Higgsfield MCP fails AND a blog image batch is blocking a client launch: spin up any text-to-image API with the same prompt as a one-off (the prompts in `/scripts/prompts/<slug>.txt` are portable). Higgsfield's documented business continuity risk (X-account suspended early 2026, billing complaints) is mitigated by re-exporting every generated asset to the client repo at generation time."
- Keep: "Re-export every Higgsfield asset to local mp4 / webm / webp on download — never depend on Higgsfield URL hosting."

Header refresh date: bump to 2026-05-17 with note "Use Case D rewritten — fal.ai retired as default; FLUX.2 Pro promoted to blog-image default after founder confirmation Higgsfield Plus tier ships 6 permanent unlimited image models."

Plan-tier-recommendations table: update Plus tier description to "**Optimus default.** 1000 credits/mo + 6 permanent unlimited image models (FLUX.2 Pro, Nano Banana, GPT Image, Seedream 4.5, Seedream V5 Lite, Kling O1 Image) + unlocks Cinema Studio Video V2. Image-gen costs are effectively $0 marginal; credits are spent almost entirely on video (Cinema Studio V2 25-45 cr, Marketing Studio Video 25-60 cr, Seedance 17-25 cr, Kling 3.0 6-7 cr/gen). Covers 30-50 client builds/year of hero video work. Check current balance via `mcp__higgsfield__balance` before each video-gen workflow."

**No "historical trial notes" section in the matrix.** Per founder instruction, the permanent workflow does not track temporary unlimited windows in any document. If a model becomes permanently unlimited later, the matrix row gains a "0 (365 unlimited)" cost — at that point, never before.

**REMOVE the SUPERSEDED workflow doc subsection** `## "Seedance draft → Kling 3.0 final" workflow (verified 50-70% credit savings)`. The simulation step (A1) replaces this workflow entirely. In its place add a new subsection `## SIMULATION-FIRST workflow (replaces all draft-model routing)`: brief summary pointing readers to `higgsfield-cost-approval-gate.md` for the full 4-frame + 5-criterion spec. The "Seedance for video composition validation" pattern is retired.

Update "Key Rules" section near bottom of the matrix: REMOVE the bullet "Start cheap, validate, commit to quality. Default to Seedance 2.0 Fast for any video composition that needs iteration; commit to Kling 3.0 / Cinema Studio Pro / Veo 3 only after composition is locked." REPLACE with: "Simulate before spending. Cinema Studio V2 is the permanent video default. Run the zero-credit text simulation (per `higgsfield-cost-approval-gate.md`) before any generate_video call. Escalate to Kling 3.0 / Seedance 2.0 only after 3-5 Cinema Studio failures, never as a draft step."

### Batch 4 — Vault workflow files (Part 1, fal.ai/Kling replacement)

**Modify:** `C:\Projects\Optimus Assets\CLAUDE.md`
- Rename heading line 472: `## Image Generation Rule (fal.ai)` → `## Image Generation Rule (Higgsfield)`
- Body: replace all "fal.ai" mentions with "Higgsfield Flux 2 / Nano Banana Pro via `mcp__higgsfield__generate_image`." Keep the prompt-quality gate language verbatim (it's tool-agnostic).
- Pre-Task Memory Search list (line 326): replace `fal.ai` with `Higgsfield`.
- Higgsfield Credit-Spend Gate Rule (line 543) provider-abstraction note: remove "fal.ai (`flux-pro/v1.1`) for stills" — replace with "any text-to-image generator with the same prompt as last-resort fallback."

**Modify:** `C:\Projects\Optimus Assets\project-prime.md`
- Lines 327-329 (.env.local scaffold): remove the `FAL_KEY=` block and the comment above it. Replace with: `# Higgsfield AI — image + video generation (Plus tier subscription, MCP endpoint, no per-project key)` and a no-op (the MCP is account-scoped, not project-scoped).
- Lines 347-348 (FAL_KEY warning block): remove entirely.
- Line 700 ("Photo Gallery" — NOT "gallery page" or "fal.ai gallery"): change to ` — NOT "gallery page" or "AI-generated gallery"`.
- Lines 846-867 (Stage 1G FAL.AI KEY REQUIRED hard-pause): replace the entire hard-pause block. New block checks Higgsfield MCP availability via ToolSearch + balance via `mcp__higgsfield__balance` ≥100cr. If balance low: warn+confirm per Gate Step 1. No FAL_KEY check.
- Lines 880-910 (image generation flow): rewrite step 2 (blog cards): "Blog post card images + article header images: Higgsfield Flux 2 via `mcp__higgsfield__generate_image` with `model: flux_2`, `aspect_ratio: 16:9` (header) or `1:1` (card). Unlimited on Plus tier — no credit cost. One card image + one header image per article. 9-10 articles = 18-20 generations total." Step 4 (gallery): same swap. Step 5: replace "fal.ai image" with "AI-generated image."

**Modify:** `C:\Projects\Optimus Assets\website-build-template.md`
- §AI Asset Generation lines 1593-1612 (Blog Card Images — fal.ai): rename heading to "Blog Card Images — Higgsfield Flux 2." Rewrite body to point to `mcp__higgsfield__generate_image` with `model: flux_2`. Remove the fal.ai script template. Add a one-line cross-reference to `higgsfield-model-selection-matrix.md` Use Case D.
- §Architecture B Hero lines 1614-1645: fallback path was "fal.ai (flux-pro/v1.1) for still + Kling AI (web UI) for animation, manual two-tool pipeline." Update to: "Fallback if Higgsfield MCP unavailable: any AI image generator with same prompt + Kling AI web UI for animation (last-resort manual flow per `knowledge/patterns/kling-video-hero.md`)." The kling-video-hero.md pattern doc itself stays unchanged (HISTORICAL).

**Modify:** `C:\Projects\Optimus Assets\build-checklist.md`
- Lines 120-137 (Step 13 assets + FAL_KEY hard-pause): remove FAL_KEY pause. Replace with: "⛔ HUMAN PAUSE: orchestrator confirms Higgsfield MCP available (ToolSearch) + balance ≥100cr (`mcp__higgsfield__balance`). If <100: warn + confirm per `knowledge/patterns/higgsfield-cost-approval-gate.md` Step 1." Replace "fal.ai" with "Higgsfield Flux 2" in all blog/gallery instructions. Update line 124 "Hero: animated canvas/JS (logo-based default) — never a photo, never fal.ai" → "Hero (Architecture A canvas) OR Higgsfield Movie-Hero (Architecture B per Pattern #80) — never a plain photo backdrop."
- Line 214 (Vercel env vars): remove `FAL_KEY (same key used during build — images already generated, key kept for future updates)`. Higgsfield is account-scoped, not project-scoped — no per-project env var needed.

**Modify:** `C:\Projects\Optimus Assets\.claude\agents\launch\pre-launch-auditor.md`
- Lines 136-138 (SECTION 3 fal.ai URL audit): keep the audit check (real-photo replacement intent still valid) but update search target: `Search: [PROJECT_FOLDER]/src for fal.ai, fal-cdn, higgsfield-cdn, higgsfield URLs. WARN if: any AI-generated URLs found — these should be replaced with real photos or kept as intentional AI art.`
- Line 153: "real photography or fal.ai-generated images" → "real photography or AI-generated images (Higgsfield)."

**Modify:** `C:\Projects\Optimus Assets\00 — Empire Index\README.md` line 50
- "fal.ai outputs, deployment artifacts, and screenshots live in their respective client repos" → "AI-generated assets (Higgsfield outputs), deployment artifacts, and screenshots live in their respective client repos."

**Modify:** `C:\Projects\Optimus Assets\retro.md` line 81
- "New integration patterns (Sanity role, GHL hook, Resend config, fal.ai prompt approach)" → "New integration patterns (Sanity role, GHL hook, Resend config, Higgsfield prompt approach)."

**Modify:** `C:\Projects\Optimus Assets\Offerings\01 Website Development\current-state.md`
- Line 15: "card image + header image per article via fal.ai" → "card image + header image per article via Higgsfield Flux 2 (unlimited on Plus tier)."
- Line 43 (stack table): "Image generation | fal.ai" → "Image generation | Higgsfield AI MCP (Flux 2 unlimited, Nano Banana Pro unlimited, Soul / Marketing Studio for premium)."

**Modify:** `C:\Projects\Optimus Assets\knowledge\onboarding\client-launch-checklist.md` line 152
- "no fal.ai placeholders if client has photography" → "no AI-generated placeholders if client has photography."

**Modify (A6 expansion):** `C:\Projects\Optimus Assets\end-to-end-workflow.md`
- Grep for fal.ai + Kling references. For every forward-looking instruction hit, apply the same replacement rules used elsewhere in Batch 4: fal.ai → Higgsfield Flux 2 (or Nano Banana for text-rendering), Kling references in primary-tool position → Higgsfield Cinema Studio V2 (with Kling 3.0 noted as troubleshooting alternative per A3 escalation). Leave historical narrative hits (e.g., "the prior workflow used fal.ai+Kling, replaced 2026-05-17") unchanged — those are factual record.

**Modify:** `C:\Projects\Optimus Assets\anthony-rosa\north-star.md` line 45
- Stack list: remove `fal.ai`, add `Higgsfield AI MCP`. New: "Next.js (App Router) · Tailwind CSS 4 · Framer Motion · Three.js · Sanity CMS · Resend · Stripe · Printful · Vercel · GoDaddy · Higgsfield AI MCP. Every hero ships with three layers..."

### Batch 5 — Vault KNOWLEDGE pattern docs (fal.ai pattern docs migration)

The four `fal-ai-*.md` patterns are forward-looking instructions. Per the full-replacement decision, they should be migrated.

**Rename + rewrite:** `knowledge/patterns/fal-ai-image-generation.md` → `knowledge/patterns/higgsfield-blog-image-generation.md`. Body rewritten for `mcp__higgsfield__generate_image` flow with Flux 2 default. Keep prompt-quality discipline verbatim.

**Rename:** `knowledge/patterns/fal-ai-avoid-text-in-prompts.md` → `knowledge/patterns/ai-image-avoid-text-in-prompts.md`. Body generalized — same principle applies to Higgsfield Flux 2, Nano Banana, Soul, Cinema Studio.

**Rename + rewrite:** `knowledge/patterns/fal-ai-parallel-property-visual-differentiation.md` → `knowledge/patterns/parallel-property-visual-differentiation.md`. Same recipe (identical style prefix + distinct style suffix per offering). Tool reference updated to Higgsfield Flux 2.

**Rename + rewrite:** `knowledge/patterns/fal-ai-reusable-blog-image-generator.md` → `knowledge/patterns/higgsfield-reusable-blog-image-generator.md`. Replace the @fal-ai/client script with an `mcp__higgsfield__generate_image` invocation pattern.

**Update build-log.md Patterns table:** edit row numbers / titles referencing the renamed patterns so cross-references resolve.

**Update cross-references in:**
- `knowledge/patterns/sanity-blog-post-publish-script.md` line 22: "fal.ai prompt" → "Higgsfield prompt"
- `knowledge/patterns/huashu-extracted-critique-rubric.md` line 45: "fal.ai output" → "AI-generated output (Higgsfield)"
- `knowledge/patterns/claude-md-absolute-rule-cross-check-at-checkpoint.md` line 23: already mentions both — change "fal.ai (or Higgsfield Soul)" → "Higgsfield (Flux 2 / Nano Banana / Soul depending on use case)"
- `knowledge/patterns/seeded-demo-mode-for-third-party-apis.md` lines 12, 266: replace fal.ai reference with Higgsfield, note that Higgsfield MCP failures fall through to a "no-image placeholder" rather than seeded fallback (because images aren't generated at request-time during demo).
- `knowledge/patterns/stay-prefix-photo-source-filename-convention.md` lines 86-87: update Pattern #4 / #72 cross-references to renamed patterns

**Modify (Batch 5 expansion):** `knowledge/patterns/higgsfield-mcsla-prompt-mastery.md`
- This doc was written in the same session as the model-selection-matrix and contains the original "Seedance draft → Kling final" workflow language. After the simulation-step adoption (A1), that language is stale. Read the doc in full and:
  - Remove any "use Seedance Fast as draft validation before Kling/Cinema Studio final" instruction
  - Remove any reference to "50-70% credit savings via the draft-then-final workflow"
  - Replace with a one-line pointer: "Validate prompts via the SIMULATION step in `higgsfield-cost-approval-gate.md` before any generate_video call — no draft-model routing."
- Keep the MCSLA structure, 10 named prompt patterns, 12 brand registers, Soul ID Identity-vs-Motion separation rule — all unchanged.

**Create:** `C:\Projects\Optimus Assets\knowledge\errors\higgsfield-prompt-simulation-divergences.md`
- Append-only ledger for post-generation divergence logging (per A1: "compare actual output frames against the simulation; significant divergence is logged as a prompt pattern failure for the vault").
- Format per entry: `## YYYY-MM-DD HH:MM — <skill-name> — <model>` heading, then 4 H3 sub-sections: `### Prompt`, `### Simulation prediction (4 frames + 5-criterion result)`, `### Actual output (4 frames described)`, `### Divergence type + pattern lesson`.
- File header documents purpose + when to write to it + how to triage entries quarterly into the prompt-mastery doc as new "anti-patterns" or "watch-outs."
- Add row to `knowledge/build-log.md` Error Encyclopedia table referencing this new ledger file (not as Error #N — as a meta-resource).

### Batch 6 — Vault build-log.md (forward-looking row updates only)

Per user's rule, leave historical rows alone. But two rows are forward-looking instructions that should reflect the new decision:

**build-log.md row #80 (Higgsfield movie-hero pipeline):** Update the "fal.ai retained for blog card thumbnails" clause to "Higgsfield Flux 2 (unlimited on Plus tier) now handles blog cards + headers + galleries — fal.ai retired as of 2026-05-17 (founder confirmation: Plus tier unlimited Flux changes the economics)."

**build-log.md 2026-05-17 Workflow Improvements row:** Add a follow-up note "Subsequent decision: fal.ai retired entirely after Plus tier unlimited Flux 2 + Nano Banana Pro confirmed — see Pattern #85 cost-approval gate doc + updated model-selection-matrix Use Case D."

All other build-log rows (#4, #5, #38, #41, #69, #72, #83, #84 + Project rows + retrospective references) stay unchanged — they describe what shipped at the time, which is historical fact.

### Batch 7 — Global Claude config (ALL 8 optimus-review agents per A6 + auto-memory + route skill)

**Sweep all 8 optimus-review agent files** at `C:\Users\Anthony\.claude\agents\optimus-review\` — `correctness.md`, `security.md`, `architecture.md`, `tests.md`, `performance.md`, `style.md`, `absolute-rules.md`, `design-system.md`. For each: grep for fal.ai + Kling references, update any forward-looking instruction hits (replace fal.ai → Higgsfield + Kling primary → Cinema Studio V2 with troubleshooting alternative note), leave historical references unchanged.

Confirmed hits from exploration:
- `architecture.md` lines 52, 111: fal.ai in adapter-pattern examples — replace with `(Stripe, Printful, Calendly, Higgsfield, Anthropic, Resend)`.
- `design-system.md` line 78: "fal.ai-generated images" → "AI-generated images (Higgsfield)"

Other 6 agents: explore grep returns no hits, but A6 requires explicit grep of all 8 to confirm — verify with `grep -n "fal\.ai\|FAL_API_KEY\|FAL_KEY\|kling\|Kling"` at sweep time. If new hits appear (e.g., from a refactor since plan exploration), apply same replacement rules.

**Modify:** `C:\Users\Anthony\.claude\projects\c--Projects-Optimus-Assets\memory\MEMORY.md`
- Update index row 4 to point to renamed memory file: `[AI image generation quality](feedback_ai-image-prompt-quality.md) — never skip, write all prompts first, each must be distinct and creative`

**Rename + rewrite:** `C:\Users\Anthony\.claude\projects\c--Projects-Optimus-Assets\memory\feedback_falai-prompt-quality.md` → `feedback_ai-image-prompt-quality.md`
- Body generalized — applies to Higgsfield Flux 2 / Nano Banana / any AI image generator. Keep the "JCM Graphics sweep skipped/rushed image generation" historical context.

**Modify:** `C:\Users\Anthony\.claude\skills\optimus-higgsfield-route\SKILL.md`
- BLOG-IMAGE intent block: rewrite. Old: "NOT Higgsfield, use fal.ai." New: "Use Higgsfield Flux 2 (unlimited on Plus tier) via `mcp__higgsfield__generate_image` with `model: flux_2`. For higher-quality stills with text rendering, use Nano Banana Pro (also unlimited on Plus). Pattern docs to read: `higgsfield-model-selection-matrix.md` Use Case D + `higgsfield-blog-image-generation.md` (formerly fal-ai-image-generation.md). Per cost-approval gate: unlimited image models skip Steps 1+2; Step 0 (skill read) still applies."
- HERO intent block: REMOVE the "Top failure mode #5: Skipping Seedance draft validation — burns 50-70% more credit" bullet (superseded by A1 simulation step). REPLACE with: "Top failure mode #5: Skipping the SIMULATION step before generate_video. Cinema Studio V2 produces unusable output ~30-40% of the time on first call — the zero-credit text simulation catches prompt failures before they spend credits. Required per `higgsfield-cost-approval-gate.md`."
- Provider abstraction note: rewrite per A5 ("fal.ai retired 2026-05-17. If Higgsfield MCP unavailable: for images, use any text-to-image generator with the same prompt as one-off. For video, Kling AI web UI is the last-resort manual fallback. For programmatic troubleshooting after 3-5 Cinema Studio failures, Kling 3.0 and Seedance 2.0 are available via the Higgsfield MCP per the escalation block.").
- Add new intent: AUDIT-EXISTING already exists — keep as-is.

**Modify:** `C:\Users\Anthony\.claude\hooks\higgsfield-credit-gate.sh` (per A2 + A7)

**Confirmed current state (from session-1 read of the hook script):** the script currently contains a 5-point checklist with two items that must be removed:
- Item 4: "CREDIT EFFICIENCY — Did you consider Seedance 2.0 Fast for draft validation before committing to the expensive final model? (Pattern #83 documents 50-70% credit savings via this draft-then-final workflow.)" — confirmed present, will be removed (not a no-op).
- Item 5 (PROMPT QUALITY) language partially preserved but the 5-criterion sub-bullets are absorbed into the SIMULATION-step language.

Edits:
- Reorder the injected checklist so the first question is "Has the active Higgsfield skill file been read in full this session?" (A7).
- Replace current 5-point checklist with the new 3-point post-A1/A2 gate:
  1. Active skill read in full this session? (A7 + Step 0)
  2. Simulation step completed and passed for this generate_video call? (A1)
  3. Balance check passed (>=100cr) and high-cost alert addressed if call >50cr? (A2)
- Remove the Item 4 CREDIT EFFICIENCY block in full (Seedance draft + Pattern #83 reference — both superseded by simulation).
- Remove any "draft via Seedance" / "draft-then-final" language anywhere else in the script.
- Keep hook exit 0 (non-blocking) — discipline is on skills.

---

## Files NOT modified (preserved per user rule)

### Vault HISTORICAL (factual records of past builds)
- All `knowledge/errors/*.md` files (5 files with fal.ai/Kling hits)
- All `knowledge/retrospectives/*.md` files (7 files)
- All `Optimus Academy/daily/*.md`, `concepts/*.md`, `apply-to-*/*.md`, `tools/archive/**/*.md` (append-only capture)
- `knowledge/patterns/higgsfield-movie-hero-pipeline.md` (user explicit: "fallback path mentioning fal.ai and Kling — leave it")
- `knowledge/patterns/kling-video-hero.md` (documented fallback per CLAUDE.md provider-abstraction)
- `knowledge/patterns/higgsfield-camera-vocabulary.md` (cross-reference list of video models, not instruction)
- `knowledge/patterns/ai-video-slop-avoidance-checklist.md` (already platform-agnostic)
- `knowledge/patterns/hero-concept-iteration-budget.md` line 14 (historical iteration narrative)
- `knowledge/build-log.md` rows other than #80 and 2026-05-17 (historical adoption records)

### Global Claude HISTORICAL
- All `~/.claude/plans/*.md` files (12 files — saved plans are historical)
- All `~/.claude/projects/<client>/*` files (CLIENT PROJECT memory — never touch)
- Auto-generated tool-results cache JSON files

### Client projects
- All `C:\Projects\Steve-Goddu\*` files
- Any other `C:\Projects\<client-name>\*` files

---

## Verification (post-edit)

1. **Grep re-run:** same query as exploration (`fal\.ai|FAL_API_KEY|FAL_KEY|kling|Kling` across vault + global Claude). Every remaining hit must be in an explicitly-preserved HISTORICAL file. No fal.ai/Kling instructions in any WORKFLOW file.
2. **Skill self-check:** read each of the three updated skills top-to-bottom. Confirm all 4 gate-step pointers are present at the right workflow positions + the new pattern doc `higgsfield-cost-approval-gate.md` is cross-referenced at every pointer.
3. **Matrix sanity:** read updated `higgsfield-model-selection-matrix.md` Use Case D — Flux 2 + Nano Banana Pro shown as $0 unlimited on Plus tier. Cost matrix table top rows reflect this.
4. **Cross-reference resolution:** rename patterns leave a redirect / are referenced from every doc that links to them. Grep for old pattern filenames to confirm zero broken links.
5. **Build-log integrity:** Pattern #85 row added, rows #80 and 2026-05-17 updated, all other rows untouched.
6. **MEMORY.md index:** points to renamed memory file, no orphan reference.
7. **Commit policy:** per Plan Preservation Rule, this plan file moves to `C:\Projects\Optimus Assets\falai-kling-cleanup-and-cost-gate-audit.md` and is committed in the SAME git commit as all edits — plan + implementation atomic per CLAUDE.md.

---

## Execution order (per founder amendment)

1. **Batch 1** — Create `higgsfield-cost-approval-gate.md` pattern doc (foundation; Batches 2/3/7 reference it)
2. **Batch 3** — Matrix update (Use Case D rewrite + 4 new image rows + unlimited cost columns + historical-notes section + Seedance-draft workflow removal). Batches 2/4/5 reference the updated matrix.
3. **Batch 2 ∥ Batch 4** (parallel) — Skill simulation+gate integration (A1+A2+A3+A5+A7) AND vault workflow files (CLAUDE.md, project-prime.md, website-build-template.md, build-checklist.md, pre-launch-auditor.md, README, retro.md, current-state.md, client-launch-checklist.md, north-star.md, end-to-end-workflow.md). Independent file sets — no edit conflicts.
4. **Batch 5** — KNOWLEDGE pattern doc renames + cross-reference fixes
5. **Batch 6** — build-log.md forward-looking row updates (#80 + 2026-05-17 + new Pattern #85 row)
6. **Batch 7** — Global Claude config (8 optimus-review agents grep+update + MEMORY.md + feedback memory rename + route skill rewrite + PreToolUse hook script update)
7. **Verification grep** — re-run `grep -rn "fal\.ai|FAL_API_KEY|FAL_KEY|kling|Kling"` against vault + global Claude. Every remaining hit must be in an explicitly-preserved HISTORICAL file. Read each updated skill top-to-bottom and confirm: MANDATORY FIRST ACTION block present, SIMULATION step present, attempt counter + escalation block present, provider abstraction note rewritten, no draft-first language remaining, no expiration-date logic.
8. **Plan-file move + commit** — move `C:\Users\Anthony\.claude\plans\gentle-leaping-prism.md` to `C:\Projects\Optimus Assets\falai-kling-cleanup-and-cost-gate-audit.md` (per Plan Preservation Rule + naming convention: kebab-case, value-descriptive). Single atomic git commit containing plan file + all edits per CLAUDE.md.

Total estimated edit count: ~24 files modified (added end-to-end-workflow.md and 6 additional optimus-review agents to sweep scope), ~4 files renamed, 1 new pattern doc created, 1 hook script updated. All atomic within one git commit.
