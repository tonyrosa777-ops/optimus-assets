# Pattern: AI Video Slop Avoidance Checklist
**Category:** AI Assets / Quality Gate / Prompt Engineering
**First used:** Goddu Imprint — 2026-05-17
**Status:** ACTIVE since 2026-05-17. **Platform-agnostic** — applies to Higgsfield, Runway, Kling, Sora, Veo, Pika, and every other text-to-video / image-to-video generator. Applies to every Optimus AI-generated video deliverable.

## What "AI slop" means

AI-generated video that immediately reads as AI to a viewer with a trained eye. Marks the content as cheap / fake / untrustworthy the instant it appears on screen. The viewer doesn't need to know *why* it looks off — they just feel it, and that feeling transfers to the brand. Slop kills luxury positioning faster than a typo on the homepage.

The opposite of slop is "looks like a real production" — footage that reads as if a director, DP, gaffer, and grip team made it on a real set with real equipment. That is the bar Optimus's premium positioning requires per the Optimus Positioning Rule in CLAUDE.md. Every AI-generated video deliverable runs through this checklist before commit. No exceptions.

## The 15-point anti-pattern checklist

### 1. Over-perfect framing
- **Tell:** Subject dead-center, formal symmetry, every edge equally weighted.
- **Why:** Models trained on millions of "well-composed" images regress to the mean — which is centered.
- **Invert:** "Off-thirds composition, intentional negative space on [left/right], subject anchored to lower-third intersection."
- **Severity:** Universal across all models.

### 2. Too-smooth camera motion
- **Tell:** Camera glides like a perfectly-balanced gimbal with no operator input — no micro-tremor, no breathing, no weight.
- **Why:** Default motion synthesis interpolates frame-to-frame on a clean spline.
- **Invert:** "Subtle organic operator-weight, handheld micro-tremor, NOT gimbal-perfect, NOT drone-smooth."
- **Severity:** Universal — particularly bad on Higgsfield Cinema Studio + Runway.

### 3. Oversaturated colors
- **Tell:** Vivid primaries everywhere — saturated reds, electric blues, neon greens.
- **Why:** Models reward "vibrant" images during training.
- **Invert:** "Desaturated, muted, tonal, no primary colors visible. Restricted palette of [3 named neutrals]."
- **Severity:** Universal.

### 4. Impossible bounces / contradicting shadows
- **Tell:** Subject lit from camera-left, but shadow falls camera-left also. Multiple key lights from impossible directions on a single subject.
- **Why:** Model doesn't track a coherent 3D light source — it composites plausible-looking light per region.
- **Invert:** "Single motivated key light from [direction], natural shadow falloff to [opposite direction], no fill."
- **Severity:** Universal — Runway worst, Sora 2 better.

### 5. Skin sheen / porcelain texture
- **Tell:** Faces smoothed to waxy plastic, pores erased, every skin tone slightly luminous.
- **Why:** Beauty-filter bias in training data.
- **Invert:** "Visible skin texture, natural pores, matte finish, no beautification, documentary realism."
- **Severity:** Universal — Kling worst on close-ups.

### 6. Hair-and-fabric morphing across frames
- **Tell:** Individual hair strands or fabric folds re-shuffle between frames; you can see them "swim."
- **Why:** Model can't track high-frequency detail across time.
- **Invert:** Avoid close-ups on hair / loose fabric. Frame wider. "Subject in [structured garment], hair tied back / short."
- **Severity:** Universal — worst on long takes and close-ups.

### 7. Hands as the #1 universal tell
- **Tell:** Six fingers, fused fingers, hands that morph mid-gesture, impossible articulation.
- **Why:** Hands are topologically complex and models have less ground-truth per-pixel.
- **Invert:** Keep hands out of frame, or specify "hands resting still, fingers visible and naturally articulated, framed from wrist." Better: crop hands out entirely.
- **Severity:** Universal — THE single most reliable AI tell. If you see hands as primary subject, scrutinize.

### 8. Eyes-and-teeth glitches
- **Tell:** Direct eye contact reveals mismatched pupils, asymmetric iris detail, teeth that change count or shape between frames.
- **Why:** Same as hands — topologically complex, frame-to-frame inconsistency.
- **Invert:** "Subject looking away from camera, eyes downcast or in profile, mouth closed or in repose."
- **Severity:** Universal — especially bad on Kling and Higgsfield close-ups.

### 9. Stock-video framing
- **Tell:** Centered subject, full-body or mid-shot, even daylight, neutral expression, plain background.
- **Why:** Models default to the most common training composition.
- **Invert:** "Editorial composition — extreme close-up on [detail] OR wide environmental shot with subject as 15% of frame. Specific time of day: [golden hour / blue hour / overcast 4pm]."
- **Severity:** Universal.

### 10. Background characters with same face
- **Tell:** Three people in the background, all with subtly the same face.
- **Why:** Model replicates a face template instead of generating distinct identities.
- **Invert:** "Single subject in frame, no background characters." Or specify distinct descriptors per character if multi-subject is unavoidable.
- **Severity:** Universal — Sora 2 + Veo 3 worst on multi-character scenes.

### 11. Logo / text in frame — UNIVERSAL FAIL
- **Tell:** Any signage, label, screen text, or logo renders as garbled glyphs.
- **Why:** Diffusion models cannot synthesize legible glyph sequences. Higgsfield, Sora 2, Veo 3, Runway, Kling — all of them.
- **Invert:** "No readable text anywhere in frame. No signage, no labels, no screens, no logos visible. If brand mark is required, leave space and composite in post."
- **Severity:** Universal. Hard fail every model. Already enforced by CLAUDE.md Image Generation Rule.

### 12. Floating objects / gravity violations
- **Tell:** A cup hovers a millimeter above the table. A pen's shadow doesn't touch the desk. Subjects sit on surfaces with no contact patch.
- **Why:** Model doesn't simulate physics — it pastes objects into compositions.
- **Invert:** "All objects resting on surface with visible contact shadow. Gravity-consistent, physical objects with weight."
- **Severity:** Universal — Pika worst, Veo 3 best.

### 13. Motion that does too much in 5 seconds
- **Tell:** Camera pushes in, then dollies left, then a subject enters, then light changes — all in one 5-second clip.
- **Why:** Prompt over-specification + model's tendency to satisfy every named action.
- **Invert:** One motion vocabulary per clip. "Slow push-in over 10 seconds. Nothing else moves." Specify what does NOT move alongside what does.
- **Severity:** Universal.

### 14. The "cinematic" trap word
- **Tell:** Triggers default teal-orange color grade, blown-out highlights, anamorphic flare, lens distortion.
- **Why:** "Cinematic" is the most-tagged label in training data and resolves to a Hollywood-trailer aesthetic mush.
- **Invert:** Never write bare "cinematic." Replace with a specific named brand register: "Hermès editorial register," "Aesop tactile register," "Apple product film register," "Wes Anderson centered symmetry," "Roger Deakins natural light."
- **Severity:** Universal.

### 15. Plastic CGI lighting
- **Tell:** Light wraps evenly around every surface, no falloff, no shadow side, subjects feel lit from inside.
- **Why:** Model averages light across the subject for "good exposure."
- **Invert:** "Strong directional key from [direction], unlit shadow side allowed to fall to near-black, no fill light, dramatic falloff."
- **Severity:** Universal — particularly bad on Runway.

## Inversion patterns quick-reference

| Anti-pattern | Inversion prompt language |
|---|---|
| Over-perfect framing | "off-thirds composition, intentional negative space" |
| Too-smooth motion | "subtle organic operator-weight, handheld micro-tremor, NOT gimbal-perfect" |
| Oversaturated colors | "desaturated, muted, tonal, no primary colors visible" |
| Impossible shadows | "single motivated key from [direction], natural falloff, no fill" |
| Skin sheen | "visible skin texture, matte finish, documentary realism" |
| Hair / fabric morph | frame wide, avoid loose hair / fabric close-ups |
| Hand tells | crop hands out, or "hands at rest, naturally articulated" |
| Eye / teeth glitches | "looking away from camera, mouth closed or in repose" |
| Stock framing | "extreme close-up on [detail]" OR "wide environmental, subject 15% of frame" |
| Same-face backgrounds | "single subject only, no background characters" |
| Logo / text | "no readable text anywhere in frame, composite brand mark in post" |
| Floating objects | "all objects resting with visible contact shadow, gravity-consistent" |
| Over-busy motion | "one motion only over [N] seconds, [everything else] does not move" |
| "Cinematic" trap | replace with named register: "Hermès editorial / Aesop tactile / Apple product film" |
| Plastic CGI lighting | "strong directional key, shadow side falls to near-black, no fill" |

## The "looks expensive" inverse recipe

Five elements to ADD to every Optimus prompt by default — these invert the slop pattern at the source:

1. **Name a specific brand register** — "Hermès editorial," "Aesop tactile," "Apple product film," "Roger Deakins natural light," "Wes Anderson centered symmetry." NOT bare "cinematic."
2. **Name a specific lens + aperture** — "35mm at f/5.6," "85mm at f/2.8 with shallow DOF," "24mm wide at f/8." NOT "cinematic camera."
3. **Name a specific motivated light source** — "window light from camera-left," "tungsten desk lamp at frame-right," "golden-hour rake from camera-back-right." NOT "good lighting" or "soft light."
4. **Name a specific color palette** — "bone, taupe, deep umber," "ink-black, ivory, brushed pewter," "moss green, aged brass, oat linen." NOT "warm" or "moody."
5. **Specify what does NOT move + what does NOT appear** — kills the model's instinct to over-add. "No people, no hands, no text. Only [subject] moves. Background is still."

## Detection check — run before commit

After generation, before staging the file for commit, run this 5-point detection sweep:

1. **Hands check.** Does any frame have hands as primary subject? If yes, freeze each hand-frame and inspect — count fingers, check articulation, watch the transitions. Re-generate if anything reads wrong.
2. **Text check.** Does any frame contain readable text, signage, screens, or logos? If yes, regenerate without text and composite the brand mark in post.
3. **Physics check.** Freeze playback at 25%, 50%, 75%. Does anything float, hover, or sit without a contact shadow? Do objects move in ways gravity wouldn't allow?
4. **Shadow check.** Pick the brightest subject in frame. Trace its shadow. Does the shadow direction match the key light direction? If multiple shadows from one subject from contradicting directions = AI error, regenerate.
5. **Color grade check.** Does it look "AI-default" — teal shadows + orange highlights, hyper-vivid, slightly luminous? If yes, prompt with a named brand register and regenerate.

## Spotting AI slop in others' work

The NPR AI slop quiz (Nov 2025) showed that even experts get duped 30%+ of the time when asked to identify AI vs. real video. Berkeley iSchool's Hany Farid (interviewed in the NPR piece) identifies the same expert-eye markers documented above: hands, hair-and-fabric morphing, eye glitches, gravity violations, multiple-faces-same-person.

This is useful for two Optimus workflows:
- **Client conversations.** When clients send "I want a video like this competitor's," run their reference through the 15-point checklist. If the reference is slop, surface that — competitors using slop is competitive advantage for Optimus's premium positioning.
- **Design-system.md research.** When researching a vertical's visual register, distinguish "real production references" from "AI-generated references." The latter are unreliable as design north stars because they encode AI defaults the client will end up looking like.

**Optimus deliverable test:** would a viewer who's never heard of AI suspect this is AI? If yes, regenerate. If no, ship.

## Platform-specific addenda

- **Higgsfield Cinema Studio:** extra-watch for "model invents own composition" when `end_image` is used as soft reference instead of `start_image`. Goddu v2 failure mode — model reinterpreted the composition rather than locking to it. Always anchor with `start_image` for hero work.
- **Runway:** better at human motion than most, but produces the heaviest "cinematic teal-orange" wash by default. Always specify named palette + named register to override.
- **Kling 3.0:** best face / lip-sync of any current model. Worst at multi-subject scenes — characters merge or share faces. Single-subject only unless you can afford 5+ regens.
- **Sora 2:** "reasoning model creatively expands anything you omit." Under-specified prompts drift heavily. Over-specify what does NOT appear / does NOT move.
- **Veo 3:** rotating product renders are reliable. Complex multi-character scenes drift. Strong for product film, weak for narrative.

## Sources

- NPR AI slop quiz (Nov 2025): https://www.npr.org/2025/11/30/nx-s1-5610951/fake-ai-videos-slop-quiz
- Berkeley iSchool Hany Farid interview: https://www.ischool.berkeley.edu/news/2025/how-spot-ai-video-slop-even-experts-get-duped-hany-farid-tells-npr
- The Week tips for spotting AI slop: https://theweek.com/tech/tips-for-spotting-ai-slop
- Higgsfield Cinema Studio prompt guide: https://higgsfield.ai/blog/Prompt-Guide-to-Cinematic-AI-Videos
- Higgsfield Sora 2 prompt guide: https://higgsfield.ai/sora-2-prompt-guide

## Related patterns

- [higgsfield-mcsla-prompt-mastery.md](higgsfield-mcsla-prompt-mastery.md) — prompt language patterns for Cinema Studio.
- [higgsfield-movie-hero-pipeline.md](higgsfield-movie-hero-pipeline.md) — references this checklist in Step 7 visual review.
- All three `optimus-higgsfield-*` skills (`optimus-higgsfield-hero-video`, `optimus-higgsfield-ad-creative`, `optimus-higgsfield-soul-character`) — each references this checklist in their visual review steps.
- CLAUDE.md Image Generation Rule — the policy-level rule this checklist operationalizes for video.
