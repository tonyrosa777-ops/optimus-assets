# Pattern: Higgsfield movie-hero pipeline
**Category:** AI Assets / Hero Architecture / Workflow
**First used:** Goddu Imprint — 2026-05-17

## What
Single-platform programmatic still + video generation for Architecture B movie-hero, replacing the manual fal.ai (still) + Kling AI (video) two-tool pipeline. Higgsfield via official remote MCP at `https://mcp.higgsfield.ai/mcp` handles both halves in one programmatic flow: text → still (Soul / Flux / marketing_studio_image) → animate (Cinema Studio Video / Kling / Veo 3) → ship mp4 + webm + webp poster.

## When to Use
Every Optimus build where design-synthesizer picks **Architecture B (Movie Header)** at Stage 1B per the revised CLAUDE.md Hero Architecture Rule (2026-05-17). Architecture B is the right choice when:
- Brand axes lean editorial / cinematic / intimate (Goddu: 2/3 intimate · 60% bold · 55% classical)
- Audience evaluates the brand in low-arousal decision contexts where ambient motion + product imagery reads as confident, not loud
- The client's product or operating environment carries visual signal value (Goddu: pen + tumbler + Pantone book = marketing-production capability that no canvas particle system could convey)
- Originality Rule §19 originality vector is easier to land via composition than via a fresh canvas concept

Skip in favor of Architecture A (3-layer particle system) when:
- The brand is service-only with no photographable product or environment (consulting, coaching, professional services with abstract deliverables)
- Audience expects abstract / kinetic motion (modern SaaS, fintech, tech-forward category competitors all use motion graphics)
- Client has a strong existing logo / brand mark that deserves its own reveal moment

## How

### Step 1 — Architecture B selection process (Stage 1B human checkpoint)

Per the revised Hero Architecture Rule:
1. Read project's `design-system.md` §8 (Brand Personality Axes) + §12 (Psychological Foundations).
2. Brainstorm **5 conceptually distinct compositions** of cinematic shots that convey the business's product / environment / moment-of-use. Each composition: distinct subject + lighting + camera angle + mood. Originality Rule §19 must hold — no composition can re-skin a prior Optimus build's hero.
3. Spawn the harsh critic agent (per Pattern #56 huashu-extracted-critique-rubric) to score 5 on: niche relevance, visual impact, originality vs. prior Optimus builds, brand-axes fit, looping ergonomics. Auto-reject if Originality or Looping <3. Pick winner with ≥18/25.
4. Confirm winner with human at Stage 1B checkpoint.

### Step 2 — Higgsfield MCP setup (one-time, user-scope)

From any directory:
```powershell
claude mcp add --transport http --scope user higgsfield https://mcp.higgsfield.ai/mcp
```

Use `--scope user` (NOT `--scope local`) so the MCP is available across every Optimus build, not project-bound to your home directory. Then authorize via Claude Code's `/mcp` interface or `claude mcp auth higgsfield` — browser OAuth flow.

Verify: `claude mcp list` shows `higgsfield: https://mcp.higgsfield.ai/mcp (HTTP) - ✓ Connected`.

Subscription: Higgsfield Plus tier ($39/mo, 1,000 credits/month) is the recommended Optimus tier — Plus unlocks Cinema Studio Video which Starter ($15/mo) does NOT include. At ~25 credits per hero pilot (including retakes), $39/mo amortizes to ~$0.50 per build.

### Step 3 — Generate the still

Use `mcp__higgsfield__generate_image` with `marketing_studio_image` (the documented default for commercial/product) at `aspect_ratio: "16:9"` for full-bleed web hero.

Prompt structure (Optimus editorial register):
```
Editorial product still life photograph. Composition: [SUBJECT DESCRIPTION
INCLUDING ALL OBJECTS, THEIR POSITIONS, AND BRAND-SPECIFIC SIGNALS]. [LIGHTING
DIRECTION + WARMTH]. [LENS — 35mm equivalent, shallow DOF, sharp foreground,
defocused background]. Subtle analog film grain throughout. Cinematic editorial
register like a luxury watch brand product film or Hermes campaign still. Warm
tungsten and golden-hour daylight mixed lighting. Mood: refined, intimate,
considered, [PROJECT-SPECIFIC MOOD]. 16:9 widescreen for web hero. No people,
no hands, no text overlays, no readable text anywhere in frame.
```

The "no readable text anywhere in frame" clause is mandatory — AI image models garble text (Error #38 from build-log: "fal.ai: never request readable text in prompts").

Poll status: `mcp__higgsfield__job_status` with `sync: true` waits up to ~25s for terminal state. Typical image gen: 10-20s.

Visual review the still per CLAUDE.md Image Generation Rule before proceeding. Common failure modes: garbled text, deformed subjects, composition not matching prompt intent. Re-generate with adjusted prompt if needed (credit cost: ~2-5 credits per re-roll).

### Step 4 — Animate the still

**⚠️ MOTION READABILITY IS A HARD GATE (revised 2026-05-17 post-Goddu).** Goddu's first Architecture B pilot used "static camera + ambient-only motion" (light shift + dust motes) and the user reaction was immediate: *"you can hardly tell that it was a video... It's not clear, nor would anybody know to wait there to see it move."* See [[../errors/higgsfield-static-camera-motion-too-subtle-for-hero]].

**Lesson:** in a hero context the user grants ~1-2 seconds of dwell time before scrolling. Motion that doesn't read in the first second is wasted credit. The "static camera + dust motes" register works for passive desktop wallpapers and long-dwell ambient backgrounds — NOT for conversion-critical web heroes.

For hero use case, the prompt MUST include at least one of these motion mechanisms (in decreasing order of cinema-studio reliability):
1. **Slow camera push-in (zoom-in)** — start wider, end on the locked composition. Cinema Studio + `genre: intimate` handles this cleanly. Push-in at 3-4% per second over 10s. Use `medias[].role: end_image` (not `start_image`) to anchor the final frame to the poster. Loop strategy: play-once-then-freeze on the final frame (`onEnded={(e) => e.currentTarget.pause()}` in Hero.tsx; no `loop` attribute). The frozen final frame matches the poster — no visual jump.
2. **Slight camera dolly with parallax** — premium register, but risks AI-warping the subjects. Use only for stronger compositions with clean depth separation.
3. **Aggressive light shift** (≥25-30% modulation, not 10%) — keeps static camera but motion is unambiguous. Cinema Studio's light handling is inconsistent at this magnitude though; ~30% regen-risk.

The static-camera + ambient-only register is for non-hero contexts only: About-page accents, interior page background sections, footer ambient. Long-dwell contexts where subtle motion has time to read.

Higgsfield generate_video call:

Use `mcp__higgsfield__generate_video` with `cinematic_studio_video_v2` (Cinema Studio — the refined cinematic camera + color model). Pass the still as `start_image` via `medias`:

```json
{
  "model": "cinematic_studio_video_v2",
  "prompt": "[STATIC CAMERA + AMBIENT-MOTION-ONLY PROMPT — see below]",
  "genre": "intimate",
  "mode": "pro",
  "aspect_ratio": "16:9",
  "duration": 10,
  "medias": [{"value": "<still_job_id>", "role": "start_image"}]
}
```

Critical params:
- `genre: "intimate"` — Cinema Studio's intimate genre matches Optimus's typical 2/3-intimate brand axis. Other options: action, horror, comedy, western, suspense, spectacle, auto. Pick the genre that maps to the client's bold/classical/intimate axis position.
- `mode: "pro"` — premium quality for hero-grade output. `std` is cheaper but visibly lower quality at hero scale.
- `duration: 10` — 10-second loop is the Optimus standard. Cinema Studio supports 3-12s.
- `medias[].role: "start_image"` — passes the still as the opening frame so animation starts from a known good composition.

Prompt structure (slow camera push-in — default for hero context, post-Goddu lesson):
```
Editorial product film, slow continuous dolly push-in over 10 seconds. Opening
frame: wide establishing shot of [COMPOSITION DESCRIPTION] with approximately
30% more [SURFACE/CONTEXT] visible around the subject than the final composition.

Over 10 seconds, the camera dollies forward at a steady 3-4 percent per second,
gradually closing in on [PRIMARY SUBJECT]. Final frame must land exactly on the
locked composition: [REPEAT KEY COMPOSITION ELEMENTS verbatim from the still
generation prompt].

Static subjects — [LIST EACH OBJECT] do not move. No rotation, no tilt, no
parallax distortion. No people, no hands, no text overlays, no logos. Shallow
depth of field maintained throughout; [PALETTE DESCRIPTION] stable. Final frame
composition is non-negotiable — it must match the poster still for seamless
freeze-on-end behavior.

Cinematic, [BRAND-AXES MOOD WORDS], [REGISTER] register.
```

Pass `medias: [{value: <still_job_id>, role: "end_image"}]` (note: `end_image` not `start_image` — Cinema Studio interpolates the camera move BACKWARD from the locked end frame, so the still anchors the final composition, not the first frame).

Loop strategy: **play-once-then-freeze** (NOT autoplay loop). The 10s push-in lands on the still composition; the video pauses on its own final frame, which is visually identical to the poster image. Hero.tsx implementation:

```tsx
<video
  autoPlay muted playsInline
  preload="metadata"
  poster="/images/hero-poster.webp"
  onEnded={(e) => e.currentTarget.pause()}
  // NO loop attribute
>
  <source src="/videos/hero-loop.webm" type="video/webm" />
  <source src="/videos/hero-loop.mp4" type="video/mp4" />
</video>
```

Cinema Studio in `pro` mode for 10 seconds takes 60-180s wall time. Poll with `mcp__higgsfield__job_status` `sync: true`.

### Step 5 — Visual review the video

Cinema Studio sometimes adds camera motion despite the prompt. Verify before shipping:
```bash
mkdir -p .higgsfield-pilot
curl -s -o .higgsfield-pilot/hero-loop-source.mp4 '<video URL from job_status>'
ffmpeg -y -i .higgsfield-pilot/hero-loop-source.mp4 -ss 0 -vframes 1 .higgsfield-pilot/frame-00s.jpg -loglevel error
ffmpeg -y -i .higgsfield-pilot/hero-loop-source.mp4 -ss 5 -vframes 1 .higgsfield-pilot/frame-05s.jpg -loglevel error
ffmpeg -y -i .higgsfield-pilot/hero-loop-source.mp4 -ss 9 -vframes 1 .higgsfield-pilot/frame-09s.jpg -loglevel error
```

Read each frame and verify:
- Static camera holds (no dramatic pan/zoom between frames)
- Composition preserved (subjects in same positions)
- Light shift visible but subtle
- Loop ergonomics — frame 0 vs frame 9 should be near-identical for seamless autoplay loop
- No new objects, no people / hands, no garbled text

If video fails review, regenerate with adjusted prompt (often: stronger STATIC CAMERA emphasis in opener) or fall back to `mode: "std"` for cheaper retakes during iteration.

### Step 6 — Encode for production

Higgsfield mp4 output is high bitrate (~6-7MB for 10s 1080p). Optimize for web:
```bash
# Slim mp4 (H.264, web-optimized)
ffmpeg -y -i web/public/videos/hero-loop-source.mp4 \
  -c:v libx264 -crf 28 -preset slow -movflags +faststart -an \
  web/public/videos/hero-loop.mp4

# Webm (VP9, smaller than mp4 for Chrome/Firefox)
ffmpeg -y -i web/public/videos/hero-loop-source.mp4 \
  -c:v libvpx-vp9 -crf 33 -b:v 0 -an -row-mt 1 \
  web/public/videos/hero-loop.webm

# Webp poster (still frame, for <video poster> + LCP)
ffmpeg -y -i .higgsfield-pilot/hero-still-v1.png \
  -c:v libwebp -quality 82 \
  web/public/images/hero-poster.webp
```

Typical compression results (Goddu trace): 6.9MB original mp4 → 524KB optimized mp4 (-92%) + 321KB webm + 52KB webp poster. Total hero asset payload ~373KB best case, ~576KB worst case. Lighthouse-safe.

`-an` (no audio) drops the audio track entirely — web heroes autoplay muted, so audio is wasted bytes.

### Step 7 — Wire into Hero.tsx as full-bleed movie-hero

Replace any prior Architecture A canvas hero with:

```tsx
"use client";

import { motion } from "framer-motion";
import { useInView } from "react-intersection-observer";
import { siteConfig } from "@/data/site";

export default function Hero() {
  const { ref, inView } = useInView({ triggerOnce: true, threshold: 0.1 });
  // ...existing siteConfig destructure + renderH1 logic...

  return (
    <section
      className="relative min-h-[100svh] overflow-hidden flex items-center"
      style={{ background: "var(--bg-base)" }}
    >
      {/* Layer 1: Full-bleed video backdrop (z-0, hidden under reduced-motion) */}
      <video
        className="absolute inset-0 w-full h-full object-cover z-0 motion-reduce:hidden"
        autoPlay
        loop
        muted
        playsInline
        preload="metadata"
        poster="/images/hero-poster.webp"
        aria-hidden="true"
      >
        <source src="/videos/hero-loop.webm" type="video/webm" />
        <source src="/videos/hero-loop.mp4" type="video/mp4" />
      </video>

      {/* Layer 1b: Poster fallback for reduced-motion users */}
      <img
        src="/images/hero-poster.webp"
        alt=""
        className="absolute inset-0 w-full h-full object-cover z-0 hidden motion-reduce:block"
        aria-hidden="true"
      />

      {/* Layer 2: Dual-axis gradient overlay for 4.5:1 text contrast */}
      <div
        className="absolute inset-0 z-[5] pointer-events-none"
        style={{
          background: [
            "linear-gradient(to bottom, rgba(15,14,12,0.20) 0%, rgba(15,14,12,0) 25%, rgba(15,14,12,0) 55%, rgba(15,14,12,0.75) 100%)",
            "linear-gradient(to right, rgba(15,14,12,0.65) 0%, rgba(15,14,12,0.35) 30%, rgba(15,14,12,0.05) 55%, rgba(15,14,12,0) 75%)",
          ].join(", "),
        }}
      />

      {/* Layer 3: Content overlaid on LEFT side */}
      <div ref={ref} className="relative z-10 max-w-[1400px] mx-auto px-6 w-full pt-24 pb-20 md:pt-40 md:pb-32">
        <div className="max-w-2xl flex flex-col gap-7">
          {/* eyebrow, H1 with hero-shimmer + textShadow, subhead, CTAs, trustMicrocopy */}
        </div>
      </div>
    </section>
  );
}
```

Critical Hero.tsx rules for Architecture B:
- `autoPlay muted loop playsInline` on `<video>` — required for mobile Safari + Chrome muted autoplay
- `poster` attribute = webp — used for LCP first paint while video loads
- `preload="metadata"` — keeps initial bytes low; full video loads on user-initiated play OR via browser eager-load on connection
- Separate `<img>` fallback with `motion-reduce:block hidden` — when prefers-reduced-motion is on, video is hidden via `motion-reduce:hidden` and the still img takes over (never falls through to flat color per CLAUDE.md §3)
- Gradient overlay achieves 4.5:1 contrast — dual-axis (bottom-fade + left-fade) is the Optimus default; tune per composition's empty space
- Text container `max-w-2xl` on LEFT — the still composition typically has product on the right and empty surface on the left; text reads cleanest against the darker-left-fade. If a composition reverses (product left, empty right), flip the gradient + text positioning.
- `textShadow` on H1 + subhead + microcopy — additional contrast over the video where the gradient alone isn't sufficient

## Key Rules

- **Originality Rule §19 binding** — each Architecture B build must have a distinct composition. Pen + tumbler + Pantone is Goddu's; the next B build cannot copy. Each composition is unique to the client's product mix / operating environment.
- **5 compositions brainstormed before generation**, not after. The harsh critic agent picks the winner. Skipping the brainstorm → generating the first idea is how clones happen.
- **Static camera + ambient motion only** — the looping web header context demands restraint. Camera moves don't loop; ambient light shift + dust motes do.
- **No readable text in prompts** — applies to both still and video generation (Pattern #38 from build-log). Brand marks should be embossed / subtle, not stamped text.
- **Visual review every generation** — both stills and videos. Frame extraction at 0s/5s/9s catches camera-motion failures Cinema Studio sometimes adds despite static-camera prompts.
- **ffmpeg encoding mandatory** — never ship Higgsfield's raw mp4 output. 6-7MB → 500KB is a free perf win.
- **Webm + mp4 source pair** — webm wins for Chrome/Firefox bandwidth; mp4 for Safari (which doesn't support libvpx-vp9 webm).
- **Webp poster is hero LCP** — the first paint is the poster image, not the video. Optimize aggressively (52KB webp from a 2.7MB PNG is typical).
- **prefers-reduced-motion → poster img, never flat color** — CLAUDE.md §3 no-flat-backgrounds applies to the hero under reduced-motion too.

## Reuse Condition

Every Optimus build where design-synthesizer picks Architecture B at Stage 1B. The pattern is now the canonical movie-hero workflow.

Architecture A (3-layer particle system) builds skip this pattern entirely — they use the existing animation-specialist canvas workflow.

## Cost / Time

Per pilot (still + video + 1-2 retakes for either):
- ~5-7 credits for still gen (marketing_studio_image)
- ~7-10 credits per video gen (cinematic_studio_video_v2 pro mode, 10s)
- Total: ~15-25 credits = **~$1.50-2.50 per build at Plus tier rate** (1000 credits / $39/mo)

Wall time:
- Still gen: 10-20s
- Video gen: 60-180s (Cinema Studio pro mode)
- Frame extraction + visual review: ~2 min
- ffmpeg encoding (webm + slim mp4 + webp): ~30s
- Hero.tsx rewrite: ~10 min (templated above)
- **Total end-to-end: ~15-25 min** vs. ~45-60 min for the manual fal.ai+Kling pipeline

## Goddu Imprint trace (canonical example)

2026-05-17 Stage 1J hero rebuild — replaced JCM Pattern #36 clone (Architecture A) with movie-hero (Architecture B) per Originality Rule §19 violation.

**Composition selection:**
- 5 compositions brainstormed: A) Marketing director's desk (pen+tumbler+Pantone), B) Pen foil-stamp production close-up, C) Folded branded apparel stack, D) Embroidery machine mid-stitch, E) Executive gift tableau
- Harsh critic (Pattern #56) scored 25/25 max
- Winner: **Composition A — 24/25.** B and D auto-rejected on looping ergonomics (action verbs don't loop). C and E scored lower on niche signal + brand-axes fit.
- Originality vector: pen+tumbler+Pantone-book triad is unique to Goddu's product mix; no prior Optimus build composition

**Generation:**
- Still: `marketing_studio_image`, 16:9, 1376×768, ~14s wall time. Job `a704ec73-82c5-4f96-8564-c86ef49aae3d`. Visual review PASSED first try.
- Video: `cinematic_studio_video_v2`, genre=intimate, mode=pro, 16:9, 10s, 1344×768, ~2min40s wall time. Job `be734fe2-c91b-4155-893f-5f922ce66bc0`. Frame review PASSED (restrained motion, composition holds, no people/hands/artifacts).

**Encoding:**
- mp4: 6.9MB → 524KB (-92%, libx264 crf 28 preset slow, no audio)
- webm: 321KB (libvpx-vp9 crf 33, no audio)
- poster: 2.7MB PNG → 52KB webp (-98%)

**Wire-in:**
- Hero.tsx rewritten as full-bleed movie-hero (~210 lines, down from ~206 of the prior split-grid Hero + 1077 lines deleted across HeroParticles.tsx + GodduCanvas.tsx)
- Net: −1214 / +179 in Goddu commit `16e6a85`

**Cost:** ~14 credits total (~$1.40 at Plus tier rate)

## Related

**Callable Optimus skills (use these instead of executing the pipeline manually):**
- [[../../../Users/Anthony/.claude/skills/optimus-higgsfield-hero-video/SKILL.md]] — `/optimus-higgsfield-hero-video` — the canonical end-to-end orchestration for Architecture B hero video generation. Encodes corrected approach from Goddu v1+v2 failures.
- [[../../../Users/Anthony/.claude/skills/optimus-higgsfield-ad-creative/SKILL.md]] — `/optimus-higgsfield-ad-creative` — Marketing Studio ad creative workflow (Tier 3 upsell). DIFFERENT register than hero — never mix.
- [[../../../Users/Anthony/.claude/skills/optimus-higgsfield-soul-character/SKILL.md]] — `/optimus-higgsfield-soul-character` — Soul ID training + character management for AI spokesperson / influencer pipelines.

**Supporting Optimus pattern docs:**
- [[higgsfield-mcsla-prompt-mastery]] — MCSLA structure (Model · Camera · Subject · Look · Action) + 10 named prompt patterns + 12 brand register library + Soul ID Identity-vs-Motion separation rule
- [[higgsfield-camera-vocabulary]] — 20-term camera glossary + reliability hierarchy (most reliable / risky / wrong-register) + per-use-case preset matrix
- [[higgsfield-model-selection-matrix]] — Higgsfield model decision tree + cost matrix + "Seedance draft → Kling final" workflow
- [[ai-video-slop-avoidance-checklist]] — platform-agnostic 15-point anti-pattern checklist

**Existing Optimus rules + patterns this pipeline executes against:**
- CLAUDE.md Hero Architecture Rule (revised 2026-05-17) — the rule this pattern executes against
- CLAUDE.md Originality Rule (§19 in absolute-rules-index) — the rule that triggered the Goddu rebuild
- Pattern #56 (huashu-extracted-critique-rubric) — the harsh critic methodology used for composition selection
- Pattern #61 (Section 12 Psychological Foundations) — the research-citation requirement for composition selection rationale
- Pattern #58 (claude-md-absolute-rule-cross-check-at-checkpoint) — the Stage 1B cross-check that the critic enforces
- Pattern #38 (fal.ai never request readable text) — applies to Higgsfield prompts identically
- `optimus-review-skill.md` (vault root) — Stage 1J gate that would catch a Higgsfield-rebuilt hero violating any absolute rule

**Error documentation:**
- [[../errors/higgsfield-static-camera-motion-too-subtle-for-hero]] — Goddu v1 failure (motion below perceptual threshold for hero dwell window) + v2 failure (composition drift from combining camera + composition change in same prompt)
