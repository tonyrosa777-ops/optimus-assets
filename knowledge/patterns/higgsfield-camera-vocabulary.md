# Pattern: Higgsfield camera vocabulary + reliability hierarchy
**Category:** AI Assets / Camera Direction / Reliability Reference
**Status:** ACTIVE since 2026-05-17
**First used:** Goddu Imprint hero rebuild — 2026-05-17 (Cinema Studio v2, intimate genre)

## What
Canonical reference for Higgsfield Cinema Studio's full 70+ camera preset catalog + a reliability hierarchy mapping each preset to its first-pass keeper rate, brand register fit (editorial hero vs. ad creative vs. about-section loop), and known failure modes. Derived from Higgsfield's official camera-controls catalog, AI Funnel Insider's 340-clip 2026 review, QuestStudio's cinematic-motion prompt pack analysis, and Optimus's own Goddu pilot trace.

The selection of a camera preset is one of the highest-leverage decisions in any Higgsfield generation. Get the preset right and even a mediocre prompt yields a usable clip. Get it wrong (chained moves, wrong-register choice, wrong subject-camera pairing) and the model produces incoherent output regardless of prompt quality.

## When to Use
Every Higgsfield generate_video call — hero pilot, ad creative pilot, about-section loop, social cutdown. Before calling `mcp__higgsfield__generate_video` with any `camera` or motion descriptor, the orchestrator (or the relevant pilot agent) must look up the preset in this doc and confirm:
1. The preset matches the brand register of the deliverable (editorial hero ≠ ad creative)
2. The preset's first-pass keeper rate is acceptable for the credit budget
3. The subject-camera pairing rule is satisfied (subject-centered moves need attached subject action; environment moves need attached environment description)
4. No chaining is implied (one camera move per shot, full stop)

## Full Camera Vocabulary Glossary

### Dolly family
| Preset | What it does | When to use |
|---|---|---|
| **Dolly In** | Camera physically moves forward toward subject at steady speed | Editorial hero, product reveal, intimate register — Hermès signature move |
| **Dolly Out** | Camera physically moves backward, revealing context | Environmental reveal, "scope of operation" shots |
| **Dolly Left / Dolly Right** | Camera tracks laterally at steady speed | Establishing context, journalism register, parallax reveal |
| **Dolly Zoom In / Out** | Vertigo effect — camera dollies while opposite-direction zoom | Climactic emotional beat in narrative (rare). High failure rate in AI gen |
| **Double Dolly** | Two-direction dolly combined | Rarely useful; experimental |
| **Super Dolly In / Out** | Aggressive, accelerated dolly | Ad hook, high-energy creative |

### Zoom family
| Preset | What it does | When to use |
|---|---|---|
| **Zoom In / Zoom Out** | Focal-length change, no camera movement | Soft register, editorial accent (subtle) |
| **Crash Zoom In / Out** | Hard, sudden zoom snap | Ad hook, attention-grab opener — wrong register for editorial hero |
| **Rapid Zoom In / Out** | Fast continuous zoom | Ad / action register |
| **YoYo Zoom** | In-then-out (or vice versa) oscillation | Ad / TikTok register; never editorial |
| **Eating Zoom** | Zoom approaching to consume/devour framing | Food / product hero (niche use case) |

### Crane / Jib family
| Preset | What it does | When to use |
|---|---|---|
| **Crane Up** | Camera lifts vertically while pointed at subject | Hero reveal, "scope" moment, end of long shot |
| **Crane Down** | Camera lowers vertically | Reverse of Crane Up; intimate descent onto subject |
| **Crane Over The Head** | Crane lifts and tilts forward over subject | Cinematic hero reveal; high risk of mis-framed final |
| **Jib Up / Jib Down** | Shorter-range crane motion | Similar to crane, smaller arc, more controlled |

### Pan / Tilt family
| Preset | What it does | When to use |
|---|---|---|
| **Pan Left / Pan Right** | Camera rotates horizontally on fixed pivot | Environmental reveal, sequence of related subjects |
| **Tilt Up / Tilt Down** | Camera rotates vertically on fixed pivot | Reveal scale (tilt up = "look how tall"); intimate descent (tilt down) |
| **Whip Pan** | Fast snap-pan, motion blur | Ad transition only; never editorial |

### Rotational family
| Preset | What it does | When to use |
|---|---|---|
| **360 Orbit** | Camera circles subject through full revolution | Product reveal; depends heavily on subject clarity + symmetry |
| **3D Rotation** | Camera rotates around subject on multiple axes | Experimental; high incoherence risk |
| **Lazy Susan** | Subject rotates on turntable, camera static | Product hero — Robo Arm is usually preferable |
| **Arc Left / Arc Right** | Camera moves in semicircular arc around subject | Subtle subject reveal; editorial-friendly |

### Drone / Aerial family
| Preset | What it does | When to use |
|---|---|---|
| **FPV Drone** | First-person view drone, kinetic / immersive | Kinetic ad creative; wrong register for editorial hero |
| **Aerial Pullback** | Camera ascends and pulls back, revealing scope | Environment hero, "place" reveal — risky in complex scenes |
| **Flying Cam Transition** | Drone-style transition between scenes | Ad / kinetic content |
| **Road Rush** | Forward-moving aerial along road | Travel / automotive register |

### Focus / Perspective family
| Preset | What it does | When to use |
|---|---|---|
| **Focus Change** | Smooth focus shift between depth planes | Editorial intimate; depends on depth-map quality |
| **Rack Focus** | Hard focus shift between two subjects | Narrative beats, hand-off moments |
| **Dutch Angle** | Camera tilted off-axis | Tension, unease — wrong register for warm editorial |
| **Fisheye** | Extreme wide-angle distortion | Experimental / stylistic only |
| **Overhead** | Top-down camera | Product flat-lay, food, design hero |
| **Object POV** | Camera attached to object's perspective | Experimental; novelty register |
| **Head Tracking** | Camera locked to subject's head movement | Character-driven content |

### Character-Centered family
| Preset | What it does | When to use |
|---|---|---|
| **Eyes In** | Camera pushes into subject's eyes | Emotional beat; needs character action attached |
| **Mouth In** | Camera pushes into subject's mouth | Dialogue / monologue moments |
| **Snorricam** | Camera rigged to subject's body, moves with them | Action / subjective register; wrong for editorial hero |
| **Hero Cam** | Low-angle, heroic framing of subject | Action ads; aspirational character moments |
| **Handheld** | Slight camera shake mimicking handheld operation | Documentary / intimate register; subtle is fine, dramatic glitches |
| **Bullet Time** | Time-frozen 360 around subject | Climax ad moment; wrong for editorial |
| **Glam** | Beauty-shot framing with slow camera caress | Beauty / luxury product ads |

### Motion Effects family
| Preset | What it does | When to use |
|---|---|---|
| **Low Shutter** | Motion blur from slow shutter | Stylistic ads; rarely editorial |
| **Wiggle** | Subtle vibration | Experimental; rarely useful |
| **Incline** | Tilted forward/backward motion | Ad register |
| **Hyperlapse** | Accelerated time-passage motion | Environment / travel content |
| **Timelapse Glam / Human / Landscape** | Long-duration compression of subject type | About-section ambient (long dwell); never hero |

### Transition family
| Preset | What it does | When to use |
|---|---|---|
| **Through Object In / Out** | Camera passes through an object as transition | Premium ad transitions; simple framing only |
| **BTS** | Behind-the-scenes register simulation | Authenticity ads; niche use |

### Vehicle family
| Preset | What it does | When to use |
|---|---|---|
| **Car Grip** | Camera mounted on car | Automotive content |
| **Car Chasing** | Pursuit-style vehicle camera | Action ads |
| **Buckle Up** | First-person vehicle entry | Automotive ads |
| **Robo Arm** | Programmatic robotic camera arm — smooth, precise, repeatable | Product hero loop staple — best preset across all use cases |

### Static
| Preset | What it does | When to use |
|---|---|---|
| **Static** | Camera does not move; ambient scene motion only | Default for editorial heroes — single most reliable preset |
| **General** | Higgsfield's "no preset, free-form prompt drives motion" mode | Power-user fallback when no preset fits |

## Reliability Hierarchy (Community-Verified)

Sourced from AI Funnel Insider's 340-clip 2026 test, Memorable Studio's Higgsfield review, and Optimus's own pilot traces. Hit rates = first-pass keeper rate (clip is usable without regeneration).

### Most reliable — 60-80% first-pass keeper rate
- **Static** — ~80%. The single most reliable preset across all use cases.
- **Dolly In / Dolly Out** — ~70%. Cinema Studio handles steady linear motion cleanly.
- **Slow Arc Left / Arc Right** — ~65%. Editorial-friendly subject reveal.
- **Robo Arm** — ~75%. Product hero loop staple; precise, repeatable, low artifact rate.
- **Slight Crane Up** — ~60%. Hero reveal moment, low-amplitude.
- **Through Object In** (simple framing) — ~60%. Editorial transition; complex framing drops to ~30%.
- **Tilt Down / Tilt Up** (simple, single direction) — ~65%.
- **Pan Left / Pan Right** (simple, single direction) — ~60%.

### Moderately reliable — 40-60%
- **360 Orbit** — ~50%. Depends heavily on subject symmetry + clarity. Works for product reveals on clean backgrounds; fails on cluttered scenes.
- **Crash Zoom** — ~55% for ad hooks (short, percussive use case), ~25% for held editorial register.
- **Focus Change / Rack Focus** — ~45%. Depends on the still's depth-map quality.
- **Handheld** — ~50% subtle, ~25% dramatic. Subtle vibration reads naturally; pronounced shake glitches.

### Less reliable — 20-40%
- **Dolly Zoom In / Out** (Vertigo effect) — ~25%. Model often produces incoherent depth confusion.
- **FPV Drone** — ~35% for simple environments, ~15% on complex scenes.
- **Snorricam** — ~30%. Depends on subject framing.
- **Bullet Time** — ~30%. Time-freeze 360 is a known weak spot for AI video models.
- **3D Rotation** — ~25%. Multi-axis camera moves are unstable.
- **Whip Pan** — ~35%. Motion blur often renders as smearing artifacts.

### Wrong register for editorial hero — banned in `optimus-higgsfield-hero-video`
These presets are ad/action register only. Using them on an editorial hero violates the brand axes for typical Optimus builds (warm, intimate, classical/modern hybrid):
- **FPV Drone** — kinetic / immersive ad register
- **Whip Pan** — ad transition register
- **Crash Zoom** — ad hook register
- **Rapid Zoom** — ad / action register
- **YoYo Zoom** — TikTok / social register
- **Bullet Time** — climax ad register
- **Snorricam** — action / subjective register
- **Dutch Angle** — tension / unease register
- **Fisheye** — experimental / stylistic register

### Multi-layered movements — documented Higgsfield failure mode
**Do not chain camera moves.** The model cannot reliably interpolate two different camera intents in a single 10-second clip. Failure modes include: incoherent depth, jarring direction changes mid-motion, subject distortion at transition points.

**One camera move per shot. Full stop.** If a deliverable needs camera variety, generate multiple clips and cut between them in editorial — never chain in a single prompt.

## Reliability Matrix Per Optimus Use Case

| Camera Preset | Hero Video | Ad Creative | About Section Loop | Notes |
|---|---|---|---|---|
| Static | ✅ Best | ⚠️ Boring | ✅ Best | Single most reliable preset across all use cases |
| Slow Dolly In | ✅ Best | ✅ Good | ✅ Good | The Hermès / editorial register signature move |
| Slow Dolly Out | ✅ Good | ✅ Good | ⚠️ | Reveal of context; good for environmental |
| Crane Up | ✅ Good | ✅ | ✅ Good | Hero reveal moments |
| Robo Arm | ✅ Best | ✅ Best | ✅ Good | Product hero loop staple |
| Arc Left / Right | ✅ Good | ✅ Good | ✅ Good | Subtle subject reveal, editorial-friendly |
| Tilt Down / Up | ✅ Good | ✅ Good | ✅ Good | Simple, single-direction only |
| Pan Left / Right | ✅ Good | ✅ Good | ✅ Good | Simple, single-direction only |
| Focus Change | ⚠️ | ✅ Good | ⚠️ | Depends on depth-map quality |
| Through Object In | ⚠️ | ✅ Good | ❌ | Premium ad transition; simple framing only |
| 360 Orbit | ⚠️ | ✅ Good | ⚠️ | Product reveal; depends on subject clarity |
| Overhead | ⚠️ | ✅ Good | ⚠️ | Flat-lay product, food |
| Handheld (subtle) | ⚠️ | ✅ Good | ⚠️ | Subtle only; dramatic glitches |
| Crash Zoom | ❌ Wrong register | ✅ Best | ❌ | Ad hook only |
| Whip Pan | ❌ Wrong register | ✅ Good | ❌ | Ad transition only |
| FPV Drone | ❌ Wrong register | ✅ Best for kinetic ads | ❌ | Environment / kinetic only |
| Bullet Time | ❌ Wrong register | ✅ Climax moment | ❌ | Climax-moment ad only |
| Snorricam | ❌ Wrong register | ✅ Action | ❌ | Subjective action ad |
| YoYo / Rapid Zoom | ❌ | ✅ Social register | ❌ | TikTok / Reels register only |
| Dolly Zoom | ❌ Unreliable | ⚠️ | ❌ | High incoherence rate |
| Dutch Angle | ❌ Wrong register | ⚠️ | ❌ | Tension register |
| Fisheye | ❌ | ⚠️ | ❌ | Experimental only |
| Timelapse Landscape | ❌ | ⚠️ | ✅ Good | Long-dwell ambient only |

✅ = recommended | ⚠️ = use with caution / depends on subject | ❌ = avoid

## Subject-Camera Pairing Rules

From the Higgsfield WAN camera-control guide, the model needs the prompt to explicitly couple the camera move with subject or environment action. Skipping this pairing is the #1 cause of incoherent output.

- **Subject-centered moves** (Eyes In, Mouth In, Snorricam, Head Tracking) want a character action attached.
  Example: "actor raises hand as dolly zooms in" — NOT "dolly zoom in on actor"
- **Environment-revealing moves** (Pan, Crane, FPV Drone, Aerial Pullback) want what becomes visible.
  Example: "as the camera pans right, skyscrapers light up at dusk" — NOT "pan right across skyline"
- **Static + ambient motion** requires explicit statement of what does NOT move plus what DOES move.
  Example: "the pen, tumbler, and Pantone book remain perfectly still; warm tungsten light slowly shifts and dust motes drift in the foreground" — NOT just "static product still life"
- **Robo Arm / programmatic moves** want the path described literally.
  Example: "robo arm sweeps in a slow 90-degree arc from camera-right to camera-left, holding subject framed center" — NOT "robo arm shot of product"

## Speed-Ramp Presets (Cinema Studio 3.5 — Stack on Top of Camera)

Cinema Studio 3.5 introduced 8 speed-ramp presets that operate independently of camera moves. These modulate the temporal feel of the clip without changing camera intent.

| Preset | What it does | When to use |
|---|---|---|
| **Linear** | Constant speed throughout | Editorial register, hero default |
| **Auto** | Higgsfield decides | Avoid for hero — unpredictable register |
| **Flash In** | Fast start, slows to normal | Ad transitions, attention hooks |
| **Flash Out** | Normal start, fast finish | Ad exits, transitions to next scene |
| **Slow-mo** | Sustained slow-motion | Luxury / emotional emphasis |
| **Bullet Time** (speed ramp variant) | Time-stretched climax moment | Climax / hero reveal moment in ads |
| **Impact** | Hard cuts on beat | Ad register, music-driven cuts |
| **Ramp Up** | Accelerates throughout | Energy build in ads |

**Optimus default for editorial heroes: Linear.** Slow-mo is acceptable for emotional/luxury beats but should be reserved — overuse reads as "perfume ad."

## Failure Mode Warnings

1. **Don't chain camera moves.** Combining orbiting + crash zoom + FPV in a single prompt produces incoherent output. ONE camera move per shot. If multiple moves are needed, generate multiple clips and cut in editorial.

2. **Don't combine camera move + composition change in the same prompt.** This was the Goddu v2 failure mode — instructing the camera to dolly while also describing a different composition for the end frame caused the model to morph subjects mid-clip. Lock the composition first, then describe a camera move that respects that locked composition. If composition needs to change, that's a different shot.

3. **Don't put camera preset in the prompt text if there's a parameter for it.** Higgsfield rule: "Everything selectable in the UI stays out of the prompt." If you're passing `camera: "dolly_in"` as a parameter, don't also write "the camera dollies in" in the prompt — this double-encodes the intent and produces over-aggressive interpretation. Use prompt text for subject + environment + lighting only.

4. **Don't trust Auto speed ramp for hero deliverables.** It picks an unpredictable register. Always specify Linear (or Slow-mo for explicit luxury beats).

5. **Don't pair a wrong-register preset with editorial prompt language.** Asking for "Whip Pan" with prompt "intimate editorial register, restrained motion" produces dissonance. Match preset register to prompt register.

## Sources

- Higgsfield camera controls catalog: https://higgsfield.ai/camera-controls
- Higgsfield WAN camera control guide: https://higgsfield.ai/blog/WAN-AI-Camera-Control-Your-Guide-to-Cinematic-Motion
- QuestStudio cinematic motion prompt pack: https://queststudio.io/blog/cinematic-motion-prompt-pack
- AI Funnel Insider 2026 Higgsfield review (340-clip test): https://aifunnelinsider.com/higgsfield-ai-review-2026/
- Memorable Studio Higgsfield review (referenced in AI Funnel Insider community methodology)
- Goddu Imprint Stage 1J hero rebuild trace (2026-05-17) — Optimus internal pilot using `cinematic_studio_video_v2` with implicit static-camera preset, intimate genre, pro mode

## Related Patterns

- [higgsfield-mcsla-prompt-mastery.md](higgsfield-mcsla-prompt-mastery.md) — prompt structure (Mood, Composition, Subject, Lighting, Action) that pairs with this camera vocabulary
- [higgsfield-model-selection-matrix.md](higgsfield-model-selection-matrix.md) — which Higgsfield model (Soul, Flux, Cinema Studio v2, Kling, Veo 3) to invoke for which deliverable
- [higgsfield-movie-hero-pipeline.md](higgsfield-movie-hero-pipeline.md) — end-to-end Architecture B movie-hero workflow that uses this camera vocabulary at Step 4
- [ai-video-slop-avoidance-checklist.md](ai-video-slop-avoidance-checklist.md) — pre-ship verification checklist that catches camera-move failure modes documented here
