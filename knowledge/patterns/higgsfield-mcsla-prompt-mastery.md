# Pattern: Higgsfield MCSLA prompt mastery
**Category:** AI Assets / Prompt Engineering / Cinematic Craft
**First codified:** Optimus Assets — 2026-05-17
**Status:** ACTIVE since 2026-05-17

## What
The canonical Optimus prompt skeleton for Higgsfield image + video generation, derived from [OSideMedia/higgsfield-ai-prompt-skill](https://github.com/OSideMedia/higgsfield-ai-prompt-skill) (MIT licensed, attribution-only inspiration — not cloned). MCSLA = **M**odel · **C**amera · **S**ubject · **L**ook · **A**ction. Five slots, every prompt fills every slot, every slot does one job. Combined with the Higgsfield Soul ID Identity-vs-Motion separation rule, 10 named cinematography patterns, 12 reference brand registers, the 15-item AI slop avoidance checklist, and the "expensive look" recipe, this is the prompt-craft layer that distinguishes Optimus hero / ad output from generic AI video slop.

## When to Use
Every Higgsfield generation Optimus runs — both Architecture B movie-heroes ([higgsfield-movie-hero-pipeline.md](higgsfield-movie-hero-pipeline.md)) and ad creative ([optimus-higgsfield-ad-creative](../../skills/optimus-higgsfield-ad-creative.md) skill). The two registers (hero vs. ad) draw from the same MCSLA structure but apply different pattern families, different reference brands, and different motion budgets — never mixed.

## How

### ⭐ The MCSLA structure (canonical Optimus prompt skeleton)

Every Higgsfield prompt slots into five named roles. Missing any slot = unreliable output. The order is fixed; the model parses front-to-back and locks earlier decisions before resolving later ones.

| Slot | Role | What goes here | Example |
|---|---|---|---|
| **M — Model** | The generator engine + mode | Cinema Studio v2 / Soul / Flux / Marketing Studio, plus mode (`pro` vs `std`) and genre param | `cinematic_studio_video_v2`, genre `intimate`, mode `pro` |
| **C — Camera** | Lens + sensor + camera move + focal length + aperture | Anamorphic 35mm, full-frame sensor, slow dolly-in at 3-4% per second, f/2.0 shallow DOF | `Anamorphic 35mm on a full-frame sensor, slow continuous dolly-in over 10s at 3% per second, f/2.0 shallow depth of field` |
| **S — Subject** | The physical thing in frame + its position + its surface context | Single object, two objects, hands+object, environment without people | `Black branded ballpoint pen at rest on raw walnut desk, foil-stamp visible, Pantone book open in background defocused` |
| **L — Look** | Lighting + palette + texture + register reference | Warm tungsten + golden-hour mixed, muted earth palette, subtle analog film grain, Aesop editorial register | `Warm tungsten mixed with low-angle golden-hour daylight from camera-left, muted earth palette (#0F0E0C, #C8A961, #8C7853), 35mm Kodak Portra grain, Aesop campaign register` |
| **A — Action** | What changes over duration + loop behavior + duration | Camera move only / subject micro-motion only / both, plus what does NOT move | `Camera dollies in; pen and Pantone book static, no rotation no tilt, dust motes drift in shaft of light. Static subjects, motion in camera + atmosphere only. 10s duration, freeze-on-end final frame` |

**The slot rule:** if you can't write a specific clause for a slot, the prompt is not ready. "Cinematic" is not a Look — that's a trap word ([§ AI slop avoidance](#ai-slop-avoidance--15-anti-patterns)). "Beautiful lighting" is not a Look. A named DP, a named film stock, a named brand campaign, a named palette — those are Looks.

Source: [OSideMedia/higgsfield-ai-prompt-skill — MCSLA primer](https://github.com/OSideMedia/higgsfield-ai-prompt-skill).

### ⭐ Hero register vs. Ad register — never mixed

These are two distinct registers. Optimus's [optimus-higgsfield-hero-video](../../skills/optimus-higgsfield-hero-video.md) skill uses **hero register only**. The [optimus-higgsfield-ad-creative](../../skills/optimus-higgsfield-ad-creative.md) skill uses **ad register only**. Crossing registers is a quality failure.

| Dimension | Hero register | Ad register |
|---|---|---|
| Reference brands | Hermès, Aesop, Apple product film, Bottega Veneta, The Row, Loewe campaign | TikTok native, Stripe ad, Patagonia challenge, Liquid Death, Notion ad, Linear product reveal |
| Color saturation | Muted, desaturated, earth palette | Saturated, vivid, contrast-pushed |
| Camera motion | Restrained — locked-off, imperceptible push, slow dolly | Motion-rich — whip pans, speed ramps, handheld energy |
| Subject pace | One micro-beat, single emotional note, 5-10s breath | Direct eye contact, multiple beats, sound-off-readable |
| Audio assumption | Plays muted on web, ambient only | Sound-on social, but must read sound-off |
| Cut frequency | Single shot, no cuts | 2-4 cuts per 6s typical |
| Conversion goal | "This brand is considered" — trust, longevity, premium signal | "Watch this now" — stop-scroll, retention, click |

The hero context grants 1-2s of dwell before scroll. The ad context steals 0.3s and earns the next 0.3s if it does. Different physics, different prompt families.

### ⭐ Soul ID Identity-vs-Motion Separation Rule (HARD CONSTRAINT)

[Higgsfield's own documented rule](https://higgsfield.ai/blog/soul-id) for character / Soul ID workflows: identity descriptors live in the Soul ID reference upload; motion / scene / camera descriptors live in the prompt. **Mixing causes identity drift** — the model rebuilds the face every frame instead of locking to the reference, and you get 10 different faces in 10 seconds.

| Goes in SoulId reference (identity layer) | Goes in MCSLA prompt (motion layer) |
|---|---|
| Face structure, jawline, cheekbones | Camera move (dolly, push, hold) |
| Eye color, shape, position | Subject action (turns head, smiles, hands product) |
| Hair color, length, texture, style | Scene context (boutique interior, golden-hour exterior) |
| Skin tone, ethnicity, freckles, marks | Lighting direction + palette |
| Body type, height, posture baseline | Wardrobe (only if scene-specific; baseline wardrobe → reference) |
| Distinguishing features (tattoos, scars, glasses if always worn) | Background / depth context |

**Practical rule:** if a descriptor would apply to the same character in every shot for the rest of their life, it's identity → Soul ID. If it changes shot-to-shot, it's motion → prompt. Crossing the line = identity drift. Goddu's first character pilot violated this and produced 4 different faces over a 10s clip; second pass with strict separation locked identity perfectly.

### 10 named prompt patterns

Each pattern is a complete MCSLA template with placeholders. Pick the pattern that matches the shot's job; don't free-style.

**⭐ Pattern 1 — The Held Breath** (static camera, one subject, one small action, 5s)
- **When:** product hero macro, founder portrait still, single-object reveal
- **Template:** `Cinema Studio v2, genre intimate, mode pro. Locked-off camera, 50mm prime, f/2.8 shallow DOF, eye-level. [SUBJECT] [in/on SURFACE], [palette]. [Lighting source + direction + warmth]. Over 5 seconds: [ONE micro-action — e.g., steam rises from cup / single dust mote drifts / leaf settles]. No other motion. [Register reference — e.g., Aesop campaign register]. 5s duration, freeze-on-end.`
- **Brand-axes fit:** intimate-heavy, classical-heavy, restrained brands
- **Loop ergonomics:** seamless — end frame ≈ start frame
- **Credit cost (Plus tier):** ~5-7 credits

**⭐ Pattern 2 — The Imperceptible Push** (slow dolly-in, <18 inches travel over 8s, Aesop register)
- **When:** hero video where motion must read but never announce itself
- **Template:** `Cinema Studio v2, genre intimate, mode pro. Anamorphic 35mm, f/2.0, slow continuous dolly-in over 8 seconds at 3% per second — total travel approximately 18 inches. Opening: wide of [SCENE], 30% more surface visible than final. Final frame: [LOCKED COMPOSITION verbatim]. Subjects do not move; only the camera. [Aesop / Hermès / Apple product film] register. 8s duration. Medias: end_image anchor.`
- **Brand-axes fit:** any brand leaning classical or intimate
- **Loop ergonomics:** play-once-then-freeze (final frame matches poster)
- **Credit cost:** ~8-10 credits

**Pattern 3 — The Tactile Close-Up** (macro intimacy, product hero)
- **When:** craft / artisan / luxury product where texture is the message
- **Template:** `Cinema Studio v2, genre intimate, mode pro. 90mm macro lens, f/2.8, focus on [TEXTURE — leather grain / fabric weave / metal foil / paper fiber]. Subject fills 70% of frame. [Single-source side light, warm tungsten]. Subtle camera breath — 1% drift over 6 seconds, no pan, no zoom. [Bottega Veneta / Loewe craft campaign] register. 6s duration.`
- **Brand-axes fit:** craft-heavy, premium materials, B2B physical-product
- **Loop ergonomics:** seamless if drift is restrained
- **Credit cost:** ~6-8 credits

**Pattern 4 — The Establishing Hold** (wide that doesn't move, 60% negative space for text overlay)
- **When:** hero where text overlay is the primary content and video is the bed
- **Template:** `Cinema Studio v2, genre intimate, mode pro. Wide 28mm lens, f/4 deep focus, locked-off. [SCENE — interior or exterior establishing], composed with subject in [right/left] third and 60% negative space in [opposite] third for text overlay. [Lighting + palette]. Over 10 seconds: [ambient motion only — light shifts, leaves move, water laps, dust drifts]. No camera motion. [Reference brand] register. 10s, freeze-on-end.`
- **Brand-axes fit:** any — workhorse pattern for content-heavy heroes
- **Loop ergonomics:** seamless ambient
- **Credit cost:** ~7-9 credits

**Pattern 5 — The Cinematic Reveal** (crane/jib up)
- **When:** hero ad register, big reveal moment, architectural or product scale
- **Template:** `Cinema Studio v2, genre spectacle, mode pro. 35mm anamorphic, f/2.8, smooth crane up from ground level to 15 feet over 6 seconds. Opening: tight on [DETAIL]. Final: wide revealing [FULL SCENE / SCALE]. [Roger Deakins / Lubezki naturalistic] lighting register. 6s, no loop.`
- **Brand-axes fit:** bold-heavy, spectacle, architectural, hospitality
- **Loop ergonomics:** does NOT loop — single playback only
- **Credit cost:** ~10-12 credits

**Pattern 6 — The Frame-Through** (slow push through doorway/window/archway)
- **When:** narrative invitation, "step inside" moment, hospitality + boutique retail
- **Template:** `Cinema Studio v2, genre intimate, mode pro. 24mm wide, f/2.8, dolly forward through [DOORWAY / ARCHWAY / WINDOW FRAME]. Opening: framed by the threshold. Final: inside the space, [INTERIOR COMPOSITION]. Smooth motion at 5% per second over 8 seconds. [Warm interior light vs. cooler exterior] for visible threshold crossing. [Loewe / The Row interior] register. 8s.`
- **Brand-axes fit:** hospitality, boutique retail, intimate-classical
- **Loop ergonomics:** does NOT loop
- **Credit cost:** ~9-11 credits

**⭐ Pattern 7 — The Hands-First Story** (commerce/craft, hands as primary subject)
- **When:** craft, artisan, food, ceremony, ritual — hands ARE the brand
- **Template:** `Cinema Studio v2, genre intimate, mode pro. 50mm prime, f/2.0 shallow DOF, locked-off or 1% drift. Hands [PERFORM SPECIFIC ACTION — fold, pour, stitch, sign, hand over]. Hands fill 50% of frame; product fills 30%; 20% surface/context. [Single-source warm light, slight rim from above-back]. Over 6 seconds: [ONE complete action gesture]. No face, no full body. [Hermès craft / Bottega Veneta workshop] register. 6s.`
- **Brand-axes fit:** craft, artisan, hospitality, B2B-with-physical-process
- **Loop ergonomics:** play-once or near-seamless if action returns to rest
- **Credit cost:** ~7-9 credits
- **Critical:** hands are the #1 AI tell. Specify finger count if needed; review every frame.

**Pattern 8 — The Cinema Studio Editorial** (verbatim from Higgsfield blog example library)
- **When:** when in doubt, when first-time use of Cinema Studio, baseline reference
- **Template:** (from [Higgsfield Cinema Studio blog post](https://higgsfield.ai/blog/cinema-studio-launch)) `Cinema Studio v2, genre auto, mode pro. Anamorphic 35mm with 1.85:1 letterbox feel. Subject: [DESCRIBE SUBJECT + WARDROBE + EXPRESSION]. Scene: [LOCATION + TIME OF DAY + WEATHER]. Lighting: [NAMED DP REFERENCE — Roger Deakins naturalistic / Hoyte van Hoytema cool / Bradford Young soft]. Camera: [ONE specific move — slow push / locked / handheld breathing]. Color: [FILM STOCK reference — Kodak Portra 400 / Kodak Vision3 500T / Fuji Eterna]. Duration 8-10s.`
- **Brand-axes fit:** any — diagnostic baseline
- **Loop ergonomics:** depends on camera move
- **Credit cost:** ~8-10 credits

**Pattern 9 — The Texture Drift** (macro fabric/water/dust for ambient B-roll)
- **When:** interior-page ambient, section background, footer accent — never hero
- **Template:** `Cinema Studio v2, genre intimate, mode std. 90mm macro, f/4, locked-off. Pure texture frame: [FABRIC / WATER SURFACE / DUST IN LIGHT BEAM / SMOKE / SAND]. Subtle ambient motion — [ONE behavior — fabric ripples in breeze / water laps / dust drifts in shaft of light]. No subject, no story, no camera motion. [Muted earth palette]. 8-12s, seamless loop.`
- **Brand-axes fit:** any — ambient B-roll bed
- **Loop ergonomics:** seamless (designed for loop)
- **Credit cost:** ~4-6 credits (`std` mode acceptable)

**Pattern 10 — The Twilight Exterior** (architectural establishing, blue hour)
- **When:** location-led brand, hospitality, retail, real estate, B2B with notable HQ
- **Template:** `Cinema Studio v2, genre intimate, mode pro. 24mm wide, f/4, locked-off, eye-level or low-angle. [BUILDING / EXTERIOR SCENE] at blue hour — 20 minutes after sunset, warm interior lights glowing through windows against cool blue sky. Over 8 seconds: ambient motion only — sky gradient slowly deepens, one interior light flicks on. No camera motion, no people on screen. [Christopher Doyle / Bradford Young] palette. 8s.`
- **Brand-axes fit:** location-anchored, hospitality, architectural, premium B2B
- **Loop ergonomics:** seamless ambient
- **Credit cost:** ~8-10 credits

### 12 reference brand visual signatures

Naming a real brand register is more reliable than naming "cinematic." These are Optimus's canonical 12 — each with its visual DNA and an AI prompt approximation.

| Brand | Visual signature | AI prompt approximation |
|---|---|---|
| ⭐ **Aesop** | Apothecary stillness, muted clay + bottle green + bone, single-object hero, daylight-only, no model | `Editorial product still life, single amber bottle on travertine, north-facing daylight, muted clay/bone palette, Kodak Portra 400 grain, Aesop campaign register` |
| ⭐ **Hermès** | Equestrian heritage, saddle leather + signature orange, hands + craft, warm tungsten + golden hour | `Hands stitching leather goods, single-source warm tungsten side light, orange + chestnut + cream palette, 90mm macro, Hermès workshop campaign register` |
| ⭐ **Apple** (product film) | White seamless infinite backdrop, controlled studio light, single-product hero, slow rotation or push-in, no environment | `White infinite backdrop product hero, slow 360 rotation, perfectly controlled multi-source softbox lighting, hyper-clean palette, Apple product film register` |
| **Patagonia** | Documentary-rugged, natural light only, weathered subjects, real environments, earth + rust palette | `Documentary handheld, natural light only, weathered hands working on gear in rugged exterior, earth/rust/forest palette, Patagonia challenge campaign register` |
| **Cartier** | Black velvet jewelry hero, gold/diamond specular highlights, slow rotation, deep blacks | `Single jewelry piece on black velvet, dramatic side-light catching gemstone facets, slow 1% rotation, jet-black background, Cartier campaign register` |
| **Stripe** (ad) | Bright clean studio, gradient backgrounds, product UI hero, tasteful motion graphics, sans-serif typography energy | `Bright clean studio environment, soft gradient backdrop in brand color, product as hero with subtle parallax, Stripe ad campaign register` |
| **Linear** | Dark UI hero, single-source key light, deep blue-gray + electric purple accent, hyper-restrained motion | `Dark editorial product film, single key light, near-monochrome blue-gray palette with one accent color, restrained motion, Linear product reveal register` |
| **Vercel** | Black backdrop, neon edge-lighting, geometric subject, slow reveal, monochrome + 1 vivid accent | `Black seamless backdrop, neon edge-light on subject, monochrome + single vivid accent color, slow push-in reveal, Vercel product film register` |
| **Loewe** | Craft-leather hero, warm Spanish daylight, hands + bag, oak + tan + cream | `Hands handling leather bag in warm Spanish daylight through window, oak/tan/cream palette, 50mm prime f/2, Loewe craft campaign register` |
| **The Row** | Pure restraint, oatmeal + bone + camel, north light, no styling, "the absence of trying" | `Editorial portrait against bone-colored seamless, north-facing daylight only, oatmeal/bone/camel palette, zero styling, The Row campaign register` |
| **Bottega Veneta** | Intrecciato leather weave macro, deep saturated greens + rust + chocolate, intimate scale, hands implied | `Macro weave detail of intrecciato leather, deep saturated green + chocolate + rust palette, single-source dramatic side light, Bottega Veneta campaign register` |
| **A24** (film stills) | Naturalistic palette, slight desaturation, real locations, unstaged composition, often single subject in environment | `Cinematic film still, single subject in real environment, slight desaturation, naturalistic palette, Kodak Vision3 500T, A24 film register` |

Citation rule: every prompt that uses a register name carries an implicit citation to that brand's campaign body of work. Don't name a brand whose work you haven't studied.

### ⭐ AI slop avoidance — 15 anti-patterns

Every Higgsfield generation reviews against this 15-point checklist before ship. One hit = regenerate.

1. **Over-perfect framing** — golden-ratio symmetry on every shot reads as "AI default." Off-center, asymmetric, "imperfect" framing reads as human.
2. **Too-smooth camera motion** — perfectly steady dolly tracks read as CGI. Specify subtle handheld breath (1% drift) or gimbal-natural micro-imperfection.
3. **Oversaturated colors** — AI defaults to vivid. Specify muted, desaturated, "low chroma," named film stock with known palette.
4. **Impossible bounces / contradicting shadows** — light source on left, shadow falling left = fail. Specify single named light source + direction explicitly.
5. **Skin sheen / porcelain texture** — AI faces often look airbrushed. Specify "matte skin, natural pores visible, no retouch, documentary-natural."
6. **Hair-and-fabric morphing** — moving hair and flowing fabric are AI's worst tells. Lock hair (tied back, hat, hood) and avoid loose fabric in motion when possible.
7. **⭐ Hands as #1 tell** — count fingers in every frame, specify hand position explicitly, prefer hands-occluded-by-object compositions.
8. **Eyes-and-teeth glitches** — direct-camera eye contact + smiles = highest failure rate. Prefer profile, side angle, or eyes-on-object compositions.
9. **Stock-video framing** — "diverse team smiling at laptop" energy. Specify named brand register that breaks the default ("Patagonia documentary handheld" not "professional team").
10. **Background characters with same face** — clone-army in background. Specify "no background characters" or "fully out-of-focus crowd, no face details."
11. **⭐ Logo/text in frame** (universal — Higgsfield/Sora/Veo/Runway all fail at text) — never request readable text, logos, signs, screens with text. Specify "no text, no logos, no signs, no screens" in exclusions.
12. **Floating objects / gravity violations** — objects defying physics. Specify "all objects resting on surface, gravity-natural, no levitation."
13. **Motion that does too much in 5s** — three actions in 5s = chaos. One action per 5s for hero; two micro-beats max for ad.
14. **⭐ The "cinematic" trap word** — triggers Higgsfield's default teal-orange mush. NEVER use "cinematic" alone. Name a specific brand register, a specific DP, a specific film stock.
15. **Plastic CGI lighting** — perfectly even three-point setup reads as 3D render. Specify single named light source (north window / single tungsten lamp / golden-hour from camera-left), shadow handling, falloff.

See [ai-video-slop-avoidance-checklist.md](ai-video-slop-avoidance-checklist.md) for the platform-agnostic full version.

### ⭐ The "expensive look" recipe

Per [Higgsfield's official prompt guide](https://higgsfield.ai/blog/prompt-guide) and the [AI Funnel Insider 340-clip test](https://aifunnelinsider.com/higgsfield-cinema-studio-test) — the parameters that drive perceived cinematic quality:

1. **Sensor / lens / focal length / aperture as named parameters** — "anamorphic 35mm on full-frame, f/2.0" beats "shallow depth of field" every time. Name the gear.
2. **Motion logic = genre + speed-ramp + specific camera verb working as a unit** — `genre: intimate` + "slow dolly-in" + "3% per second" produces consistent results; any one alone is hit-or-miss.
3. **Built-in post-production color grading** — Cinema Studio applies a grade after generation. Specify the grade target ("Kodak Vision3 500T" / "Fuji Eterna" / "DI bypass with crushed blacks").
4. **Physics-aware generation engine** — Cinema Studio respects gravity, light direction, depth occlusion better than Soul or Flux. For physical-product hero, Cinema Studio wins.
5. **Name a real DP or film stock** — Higgsfield's own prompt guide cites [Roger Deakins, Denis Villeneuve, Todd Haynes](https://higgsfield.ai/blog/prompt-guide) as proven prompt anchors. Adding "lit by Roger Deakins, shot on Kodak Vision3 500T, graded Todd Haynes Carol register" produces visibly better results than "cinematic, beautiful, moody."

### Optimus-canonical web hero prompt template

```
[OPTIMUS HERO V1.0]

MODEL: Cinema Studio v2 (cinematic_studio_video_v2), genre [intimate / auto / spectacle], mode pro

COMPOSITION: [Wide / medium / macro] of [SUBJECT], [POSITION in frame — right third / center / left third],
[NEGATIVE SPACE percentage and side for text overlay].

LENS: [Focal length — 24mm / 35mm anamorphic / 50mm prime / 90mm macro] on [sensor],
f/[aperture] depth of field, [eye-level / low-angle / high-angle].

LIGHTING: [Single-source / dual-source] [warm tungsten / north daylight / golden-hour / blue-hour]
from [direction — camera-left / above / behind-right], [shadow behavior].

PALETTE: [Hex anchors — e.g., #0F0E0C, #C8A961, #8C7853]. [Film stock reference — Kodak Portra 400 /
Vision3 500T / Fuji Eterna]. [Saturation level — muted / restrained / vivid].

SUBJECT + ACTION: [Object/scene description]. Over [duration] seconds: [ONE micro-action — describe
exactly what changes]. [What does NOT move — explicit static-subject list].

CAMERA MOTION: [Locked-off / slow dolly-in at X% per second / 1% drift / crane up].
[Total travel distance if dolly]. [Motion ends on final composition: REPEAT key composition elements verbatim].

DURATION: [5-10]s. [Loop strategy — freeze-on-end / seamless loop / play-once].

TEXTURE: Subtle analog film grain throughout. [Specific texture beats — dust motes / steam / ripple].

REFERENCE REGISTER: [Named brand campaign — Aesop / Hermès / Bottega Veneta / Apple product film].

EXCLUSIONS: No people, no hands [unless Pattern 7], no text overlays, no readable text anywhere in frame,
no logos, no signs, no screens with text, no floating objects, no extra subjects beyond [explicit list].
```

## Key Rules

- **MCSLA every slot, every prompt** — missing a slot = unreliable output. "Cinematic" alone = AI slop trigger.
- **Hero register and Ad register never mix** — hero skill uses hero patterns; ad skill uses ad patterns. Different physics.
- **Soul ID Identity-vs-Motion separation is HARD** — identity → reference; motion → prompt. Crossing = identity drift.
- **Name brands, DPs, film stocks** — never the word "cinematic" standalone. Specificity beats vibe.
- **15-point slop checklist runs on every generation** — one hit = regenerate. Hands and text are the top two failure modes.
- **The "expensive look" is a parameter recipe, not a vibe** — sensor + lens + aperture + named light source + named film stock + named DP. All five, every time.
- **Pick one of the 10 patterns** — don't freelance. The patterns are battle-tested; novel pattern attempts are 3× regen rate.
- **Exclusions clause is mandatory** — "no people, no hands, no text, no logos" is the baseline. Add scene-specific exclusions for any anti-pattern relevant to the shot.

## Reuse Condition

Every Higgsfield generation Optimus runs — heroes, ads, character work, B-roll, ambient. The MCSLA structure + 10 patterns + 12 brand registers + slop checklist + expensive-look recipe is the prompt-craft layer for ALL Higgsfield work. Hero skill and ad skill apply different pattern subsets but share this pattern doc as their common foundation.

## Related

- [higgsfield-movie-hero-pipeline.md](higgsfield-movie-hero-pipeline.md) — full Architecture B hero workflow that consumes these prompts
- [higgsfield-camera-vocabulary.md](higgsfield-camera-vocabulary.md) — 20-term camera glossary + reliability hierarchy for the Camera slot
- [higgsfield-model-selection-matrix.md](higgsfield-model-selection-matrix.md) — model decision tree for the Model slot
- [ai-video-slop-avoidance-checklist.md](ai-video-slop-avoidance-checklist.md) — 15-point platform-agnostic anti-pattern checklist (expanded form of §AI slop section)
- Skill files: [optimus-higgsfield-hero-video](../../skills/optimus-higgsfield-hero-video.md), [optimus-higgsfield-ad-creative](../../skills/optimus-higgsfield-ad-creative.md), [optimus-higgsfield-soul-character](../../skills/optimus-higgsfield-soul-character.md)
- CLAUDE.md Hero Architecture Rule (revised 2026-05-17) — the rule Higgsfield generations execute against
- CLAUDE.md Originality Rule §19 — composition originality requirement that constrains pattern reuse across builds

## Sources

- [OSideMedia/higgsfield-ai-prompt-skill](https://github.com/OSideMedia/higgsfield-ai-prompt-skill) — MCSLA structure (MIT licensed, attribution-only inspiration, not cloned)
- [Higgsfield official prompt guide](https://higgsfield.ai/blog/prompt-guide) — DP / film stock anchor citations (Roger Deakins, Denis Villeneuve, Todd Haynes)
- [Higgsfield Cinema Studio launch blog](https://higgsfield.ai/blog/cinema-studio-launch) — Pattern 8 verbatim example
- [Higgsfield Soul ID blog](https://higgsfield.ai/blog/soul-id) — Identity-vs-Motion separation rule
- [AI Funnel Insider — 340-clip Cinema Studio test](https://aifunnelinsider.com/higgsfield-cinema-studio-test) — empirical validation of the "expensive look" parameter recipe
- Cinematography craft research synthesis (Optimus Academy, 2026-05) — 10 named patterns + 12 brand register library + 15-point slop checklist
- [Aesop campaign archive](https://www.aesop.com/), [Hermès workshop films](https://www.hermes.com/), [Apple product film library](https://www.apple.com/), [Bottega Veneta campaigns](https://www.bottegaveneta.com/), [Loewe craft campaigns](https://www.loewe.com/), [The Row campaigns](https://www.therow.com/), [A24 film archive](https://a24films.com/) — reference brand visual signatures
