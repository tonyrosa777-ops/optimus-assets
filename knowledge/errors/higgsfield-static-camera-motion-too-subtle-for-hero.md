# Error: Higgsfield static-camera + ambient-only motion too subtle for hero use case
**Project:** Goddu Imprint
**Date:** 2026-05-17
**Phase:** Stage 1J hero rebuild (Architecture B pilot)

## Problem
Goddu's first Architecture B movie-hero pilot generated a Higgsfield Cinema Studio video with a "locked-off static camera + ambient-motion-only" prompt (light shift + sparse dust motes + barely-perceptible warm tone shift on walnut grain). The composition (pen + tumbler + Pantone book on warm walnut) was technically correct and the still + animation completed cleanly per the prompt. The video shipped to production at steve-goddu.vercel.app (commit `16e6a85`).

User reaction on first live view:
> "you can hardly tell that it was a video... the one little car zooming by in the window in the top corner that you can't even see. It's not clear, nor would anybody know to wait there to see it move."

The motion was so restrained that, in a hero context where the user grants ~1-2 seconds of attention before scrolling, the video read as a static image. The Higgsfield credit (~$1.40 for the 10s 1080p Cinema Studio gen) was effectively wasted on motion no one would notice.

## Root Cause
The prompt direction was correct for a "passive desktop wallpaper" register — Hermès product film loops play behind silent dinner scenes for minutes, and ambient-only motion works in that long-dwell context. The same direction is **wrong for web hero context** where:
- User attention dwell is ~1-2 seconds at the start
- Most users scroll past the hero before even noticing it loops
- Motion needs to read as cinematic, not as imperceptible drift
- The credit is wasted if 99% of visitors never see the motion

Specifically, the original prompt asked for:
- "warm window light from upper-left modulates intensity by ~10% over five seconds then back" (too subtle — 10% modulation across 5s is below perceptual threshold for most users at glance)
- "sparse dust motes drift through the window light beam, 4-6 motes visible across the 10 seconds" (sparse + slow drift = invisible without sustained attention)
- "barely-perceptible warm tone shift on walnut wood grain" (literally below perceptual threshold by definition)
- "Negative: no camera movement of any kind" (removed the strongest tool for grabbing attention — camera move)

Combined: a prompt that explicitly rejected every motion mechanism that would make the video read as a video.

## Solution
For Higgsfield (or any image-to-video) hero generation going forward, the prompt must include AT LEAST ONE motion vector that reads in the first second:
1. **Camera move** — slow zoom in, slow dolly, slight parallax. Cinema Studio handles these well. The "no camera motion" prompt direction is wrong for hero use case.
2. **Subject motion** — pen rolling slightly, Pantone page turning, tumbler condensation forming, etc. Real but restrained.
3. **Aggressive light shift** — at least 25-30% intensity change, not 10%. A passing-cloud light shift only reads when it's actually visible.
4. **Dramatic environmental element** — steam rising from a coffee cup, fabric ruffling in a breeze, a hand placing an object then withdrawing (carefully — must not pull focus from product).

The "static camera + ambient-only" register is acceptable for non-hero contexts (interior page background sections, About-page accent visuals) where dwell time is longer and the motion is meant to feel like presence not impact.

For Goddu specifically: regenerated with slow camera zoom-in (start frame: wider establishing shot; end frame: current composition; 10s push-in) — motion reads on first frame, hero feels cinematic, returning credit-for-value.

## Prevention

**Update Pattern #80 (higgsfield-movie-hero-pipeline.md) "How" Step 4 prompt structure** with the new motion-direction guidance:

> Static camera + ambient-only motion is the WRONG default for hero use case. The hero gets ~1-2 seconds of user attention before scroll. Motion must read in the first second. Pick at least one of:
> - Slow camera push-in (4-8% over 10s) — most cinematic, lowest risk of distracting from product
> - Camera dolly with parallax — 3D depth effect, premium register
> - Aggressive light shift (≥25% modulation) — keeps static camera but motion is unambiguous
> - Subject motion if it makes narrative sense (steam rising, page turning) — risky for loop ergonomics
>
> The "static locked camera + dust motes" register is for non-hero contexts (interior-page background sections, About teaser accents) where dwell time supports subtle motion.

**Add to the Architecture B selection process (revised CLAUDE.md Hero Architecture Rule):**

> When selecting the winning composition, also evaluate its motion ergonomics on the dimension "Does the composition support cinematic camera move (zoom/dolly) or aggressive subject motion that reads in the first second?" — if no, the composition is wrong for Architecture B and design-synthesizer should reconsider Architecture A or a different composition.

**Add to the harsh critic agent rubric:**

> 6th scoring criterion (1-5): **Motion readability** — does this composition's natural motion language read in the first 1-2 seconds of attention? Static-camera ambient-only motion = 1-2/5 (only for non-hero contexts). Aggressive camera move OR strong subject motion = 4-5/5. Auto-reject if <3 for hero context.

## Update 2026-05-17 (v2 attempt also failed) — broadened root cause

After the original "motion too subtle" lesson was logged, a v2 attempt used the same composition still as Cinema Studio's `end_image` parameter with a slow-camera-push-in prompt, expecting the model to interpolate the push-in motion backward from the locked end frame. **Result: composition drifted off entirely.** The new desk scene had a different (unbranded) tumbler, no Pantone book (replaced with generic color swatch grid), an added notepad on the left, and a different pen position. The push-in motion was present but the composition wasn't.

**Broader root cause** (discovered via deep Higgsfield documentation research 2026-05-17):

Higgsfield's official prompt guidance states: *"Don't try to change a character AND move the camera in the same prompt — run identity edits first using Seedream or Seedance, then apply camera movement in the video prompt."*

This rule applies equally to composition: **don't combine "change composition / lock end frame" + "execute camera move" in a single video generation prompt.** The model can't reliably do both simultaneously.

Additional findings from the deep research:
- `end_image` role is a soft aesthetic reference, NOT a hard frame lock. Used alone, it gives the model "general direction" and the model generates its own opener + interpolation.
- `start_image` IS a hard composition lock. The model interpolates FORWARD from the exact frame.
- Camera direction belongs in **API parameters** (genre, mode, speed-ramp preset) — Higgsfield's official rule: *"Everything selectable in the UI stays out of the prompt."*
- The prompt should be **scene description only** (subjects, lighting, atmosphere, brand register reference) + ONE camera intent if no preset param available.

## Corrected approach (encoded in optimus-higgsfield-hero-video skill)

The new skill `/optimus-higgsfield-hero-video` encodes the corrected pipeline:
1. `start_image` = the locked composition still (NOT `end_image`)
2. Camera move applied via `genre` parameter (intimate / drama / commercial / etc.) — NOT named explicitly in prompt
3. Prompt = scene description only + brand register name (Hermès / Aesop / Apple / A24) + one motion mechanism + explicit static-subject list
4. Mode = `pro` for hero-grade quality
5. ONE camera move, ONE optional light/atmosphere change, everything else explicitly static
6. Hit-rate reality: plan for 2-4 generations per hero (Kling 3.0 ~1 in 4 keepers, Cinema Studio ~60-70% first pass per AI Funnel Insider 340-clip test)

## Related
- Pattern [[../patterns/higgsfield-movie-hero-pipeline]] — Step 4 already updated with motion-readability gate + correct prompt structure
- Pattern [[../patterns/higgsfield-mcsla-prompt-mastery]] — the MCSLA structure that fixes the prompt-vs-parameter split
- Pattern [[../patterns/higgsfield-camera-vocabulary]] — reliability hierarchy + per-use-case preset matrix
- Pattern [[../patterns/higgsfield-model-selection-matrix]] — Seedance-draft-then-Kling-final workflow (50-70% credit savings)
- Pattern [[../patterns/ai-video-slop-avoidance-checklist]] — 15-point anti-pattern checklist
- Skill `/optimus-higgsfield-hero-video` — the corrected pipeline as a callable orchestration
- CLAUDE.md Hero Architecture Rule §"Architecture B" — needs selection-process update with motion readability dimension
- The cost question: a credit-for-value test for AI generation. If 99% of viewers can't tell the credit was spent, the credit was misspent.
