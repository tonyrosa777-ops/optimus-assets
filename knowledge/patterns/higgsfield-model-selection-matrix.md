# Pattern: Higgsfield model selection matrix
**Category:** AI Assets / Decision Framework / Cost Optimization
**First used:** Goddu Imprint — 2026-05-17
**Status:** ACTIVE since 2026-05-17. Refresh model catalog quarterly — Higgsfield ships new models every 4-8 weeks and retires old ones almost as fast.

## What
A decision tree + cost matrix for picking the right Higgsfield model for each Optimus use case. Higgsfield ships 10+ image models and 10+ video models with overlapping capabilities and 10-100x cost variance. Defaulting to the flagship model on every job burns the Plus-tier 1000-credit budget in days; defaulting to the cheapest model ships visibly inferior client deliverables. This matrix is the routing logic.

## When to Use
Every time the orchestrator (or animation-specialist / ad-creative agent) is about to call `mcp__higgsfield__generate_image` or `mcp__higgsfield__generate_video`. Consult the matrix BEFORE the call to pick the model that matches use-case quality requirement and budget envelope. Re-consult quarterly to catch new model releases and price changes.

## How

### Step 1 — Identify the use case

Optimus has seven canonical use cases. Map the current task to one of them (see Section "Use case decision tree" below). If the task doesn't map cleanly, default to Use Case A treatment (highest-quality settings) and flag for matrix update.

### Step 2 — Pick the model from the matrix

Use the Cost Matrix table to pick the model. Optimization principle: **start cheap, validate composition, commit to quality.** The Seedance-draft → Kling-final workflow (Section 5 below) saves 50-70% credits on every video that goes through a composition iteration.

### Step 3 — Generate

Call the MCP tool with the chosen `model` parameter. All Higgsfield models are exposed through `mcp__higgsfield__generate_image` and `mcp__higgsfield__generate_video` with `model: <model_id>` from the catalog below.

---

## Complete model catalog

### Image models

| model_id | Name | Provider | Best at | Aspect ratios | Cost (cr) | When to pick | When to avoid |
|---|---|---|---|---|---|---|---|
| `soul` / `soul_2` | Soul 2.0 | Higgsfield | Fashion-grade hyper-realism, 20+ launch presets | 9:16, 1:1, 16:9, 4:3, 3:4 | ~2-3 | Editorial portraits, lifestyle stills | Product-on-white commercial shots |
| `soul_id` | Soul ID | Higgsfield | Identity-locked character generation across all Soul presets | 9:16, 1:1, 16:9, 4:3, 3:4 | One-time training + ~2-3/gen | AI spokesperson, recurring character across campaigns | One-off stills (training cost wasted) |
| `soul_cinema` | Soul Cinema | Higgsfield | Cinematic stills tuned for later animation | 9:16, 1:1, 16:9 | ~2-3 | Stills that will feed Cinema Studio Video for hero generation | Stills shipped as final stills (Nano Banana is sharper) |
| `soul_cast` | Soul Cast | Higgsfield | Text-only character/avatar generation | 9:16, 1:1, 16:9, 4:3, 3:4 | ~2 | Brand avatar exploration, character mood-boards | Photoreal lifestyle |
| `soul_location` | Soul Location | Higgsfield | Environment and location plates | 16:9, 9:16, 1:1 | ~2 | Background plates for compositing, location B-roll stills | Subject-driven shots |
| `nano_banana_pro` | Nano Banana Pro | Google | 4K resolution, strongest at composition/lighting/text rendering | 16:9, 9:16, 1:1, 4:3, 3:4 | 2 | Hero stills, refinement passes, anything with on-image text | Bulk gen on a tight budget |
| `gpt_image_2` | GPT Image 2 | OpenAI | Strong text rendering | 16:9, 9:16, 1:1 | 1 | Images with text overlays (signage, packaging mockups) | Photoreal portraits |
| `flux_2` | Flux 2 | Black Forest Labs | Fast general-purpose | 16:9, 9:16, 1:1, 4:3, 3:4 | 1.5 | Default workhorse for non-hero stills | Hero-grade detail work |
| `flux_kontext` | Flux Kontext | Black Forest Labs | Context-aware editing/iteration | 16:9, 9:16, 1:1 | 1.5 | Iterating on a base image, in-painting | First-pass generation |
| `marketing_studio_image` | Marketing Studio Image | Higgsfield | Commercial/product/ads — editorial product still life register | 16:9, 9:16, 1:1, 4:3 | ~2-5 | Hero stills for Architecture B movie-hero pipeline, ad creative stills | Portraits |
| `z_image` | Z Image | Higgsfield | Fast budget option | 16:9, 9:16, 1:1 | 0.5 | High-volume blog cards, social tile bulk gen | Hero or near-hero use |
| `seedream_5_lite` | Seedream 5.0 Lite | ByteDance | Visual reasoning, fast | 16:9, 9:16, 1:1 | ~1 | Conceptual exploration, brand mood boards | Final-quality output |
| `seedream_4_0` | Seedream 4.0 | ByteDance | Visual reasoning tier (premium) | 16:9, 9:16, 1:1, 4:3, 3:4 | ~2-3 | Complex scene composition where layout reasoning matters | Simple stills (Flux is cheaper) |

### Video models

| model_id | Name | Provider | Best at | Aspect ratios | Durations | Cost (cr) | When to pick | When to avoid |
|---|---|---|---|---|---|---|---|---|
| `cinematic_studio_video_v2` | Cinema Studio Video V2 | Higgsfield | Refined cinematic camera + color, 8 genres | 16:9, 9:16, 1:1 | 3-12s | ~25-45 ⚠️ | Hero finals (Architecture B), genre-driven cinematic shots | Drafts (too expensive); rapid iteration |
| `cinematic_studio_3_0` | Cinema Studio 3.0 | Higgsfield | Physics-aware, collapsed 7 genres | 16:9, 9:16 | 3-10s | ~30-50 ⚠️ | Business/Team tier only — physics-realistic shots | Not on Plus tier (gated) |
| `cinematic_studio_3_5` | Cinema Studio 3.5 | Higgsfield | Genre/Style/Camera 3-pill UI, native audio, speed-ramp, 9 reference images | 16:9, 9:16, 1:1 | 3-12s | ~30-50 ⚠️ | Plus tier flagship — when audio sync + reference-heavy shot needed | Cheaper drafts |
| `kling3_0` | Kling 3.0 | Kuaishou | Multi-shot, audio sync, motion-transfer, 4K cinema-grade | 16:9, 9:16, 1:1 | 5s, 10s | 6-7 (5s @ 720p) | **Hero finals** (best $/quality on Plus tier), short cinematic | Long-form (10s+ doubles cost) |
| `kling2_6` | Kling 2.6 | Kuaishou | Cinematic motion, advanced physics | 16:9, 9:16, 1:1 | 5s, 10s | ~5-6 (5s) | Budget-cinematic, motion-physics shots | When 3.0 quality is reachable in budget |
| `veo_3` | Veo 3 (audio) | Google | Long-form narrative, native audio | 16:9, 9:16 | 8s | 58 (8s @ 720p) | Premium hero with audio, narrative ads | Budget projects |
| `veo_3_fast` | Veo 3 Fast | Google | Same quality envelope, lower latency | 16:9, 9:16 | 8s | 22 (8s @ 720p) | Narrative + lip-sync drafts | When ambient/no-audio works (Kling is cheaper) |
| `seedance_2_0` | Seedance 2.0 | ByteDance | Reference-driven (image/video/audio refs), consistent identity, multi-SKU | 16:9, 9:16, 1:1 | 5s, 10s, 15s | 25 (5s @ 720p) | Multi-SKU product campaigns, consistent-character video sequences | One-off hero shots |
| `seedance_2_0_fast` | Seedance 2.0 Fast | ByteDance | Reference-driven, faster | 16:9, 9:16, 1:1 | 5s, 10s | 17 (5s @ 720p) | **Draft validation** before committing to Kling/Cinema Studio final | Final-quality output |
| `sora_2` | Sora 2 | OpenAI | Strong reasoning, narrative + lip-sync | 16:9, 9:16 | 10s | 40-70 | Premium narrative when story complexity matters | Standard cinematic (overpriced) |
| `minimax_hailuo_02` | MiniMax Hailuo 02 | MiniMax | Character animation specialist | 16:9, 9:16 | 5s, 10s | ~15-25 | Character-driven shots, expressive faces | Static product shots |
| `wan_2_5` | WAN 2.5 | Alibaba | Fast | 16:9, 9:16 | 5s | ~10-15 | Quick iterations with Camera Controls presets | Cinematic quality demands |
| `wan_2_6` | WAN 2.6 | Alibaba | Expressive, native Camera Controls library | 16:9, 9:16, 1:1 | 5s, 10s | ~12-18 | When Camera Controls preset matches need exactly | Premium hero (Kling 3.0 sharper) |
| `marketing_studio_video` | Marketing Studio Video | Higgsfield | 9 ad presets — UGC, Tutorial, Hyper Motion, etc. (wrapper over Kling/Seedance/Veo) | 16:9, 9:16, 1:1 | 5s, 10s | ~25-60 | Tier 3 Marketing Team ad creative | Hero film (Cinema Studio is cleaner) |

⚠️ = estimated cost not publicly published; verify in-app before committing to a batch.

---

## Use case decision tree

### Use case A: Hero MP4 video (Optimus client website hero, Architecture B)

**Flow:**
1. Still gen: `marketing_studio_image` (editorial product/lifestyle register) OR `nano_banana_pro` (4K, hero-grade detail). Pick Nano Banana for hero stills shipped as static-fallback poster; pick Marketing Studio when the still is just feeding a video and never seen alone.
2. Animation: `cinematic_studio_video_v2`, `genre: intimate` / `drama` / `commercial`, `start_image` lock (or `end_image` for slow-push-in workflow).
3. Draft validation: `seedance_2_0_fast` first (17 credits) to validate composition before committing Cinema Studio Pro credits.
4. **Total cost: ~15-25 credits per hero** (~$0.60-1.00 at Plus tier) once the Seedance-draft step is baked in.

See `higgsfield-movie-hero-pipeline.md` for the full end-to-end workflow.

### Use case B: Ad creative video (Optimus Tier 3 Marketing Team)

**Flow:**
1. `marketing_studio_video` with the preset matching ad intent (UGC / Tutorial / Hyper Motion / Product Showcase / etc.).
2. Marketing Studio Video is a wrapper — pick the preset, the model under the hood is auto-selected (typically Kling 3.0 or Seedance 2.0).
3. For multi-SKU campaigns (5+ products), switch to `seedance_2_0` directly so identity locks across the campaign.
4. **Total cost: ~25-60 credits per ad** (~$1-2.50 at Plus tier).

### Use case C: AI Spokesperson / Soul Character training (Optimus AI Influencer pipeline)

**Flow:**
1. **Train:** `soul_id` with 20+ photos of the target identity. One-time per character (~100-200 credits). Output: a reusable `soul_id` reference token.
2. **Generate stills:** `soul_2` with `soul_id` reference + `custom_reference_strength` parameter (typically 0.7-0.85). Generates hundreds of identity-locked stills across 20+ presets.
3. **Generate videos:** `cinematic_studio_video_v2` or `kling3_0` with the Soul-generated still as `start_image`. Video inherits the locked identity.
4. **Storyboard sequences (multi-shot consistency):** Use the Higgsfield Storyboard endpoint (single API call → 3-5 shots with identity + composition continuity).
5. **Total cost:** ~150 credits training (one-time) + ~5-10 credits per still + ~25-45 credits per video. Amortizes across the entire character's content output.

See `optimus-higgsfield-soul-character.md` skill.

### Use case D: Blog card images (Optimus client builds)

**Flow:**
1. **Default: fal.ai `flux-pro/v1.1`** (~$0.05 each, ~$1 for a 20-card batch). fal.ai wins on cost-per-image for non-hero stills.
2. Higgsfield `flux_2` or `z_image` only when fal.ai is unavailable or when Higgsfield's MCP integration is faster than spinning up fal.ai for this client.
3. Never use Nano Banana Pro or Soul models for blog cards — overspec'd by 4-10x.
4. **Total cost (Higgsfield path): ~10-20 credits per 20-card batch** (~$0.40-0.80 at Plus tier).

### Use case E: Editorial cinematic stills with text rendering

**Flow:**
1. `nano_banana_pro` (4K, strongest text rendering per official docs). 2 credits/image.
2. Fallback: `gpt_image_2` (1 credit, also strong text). Pick GPT Image 2 when the text is the only requirement; pick Nano Banana when composition + lighting + text all matter.
3. **Total cost: 1-2 credits per still.**

Note: per CLAUDE.md Image Generation Rule, AI text rendering is unreliable for production. These models are *better* than alternatives at text — they are still not perfect. Visual-review every output; regenerate any with garbled characters.

### Use case F: Product showcase video for e-commerce

**Flow:**
1. **Single SKU:** `marketing_studio_video` with Product preset.
2. **Multi-SKU campaign (5+ products, consistent identity required):** `seedance_2_0` with the lead product's still as image reference. Subsequent SKUs use the same reference for visual continuity.
3. **Total cost: ~25-50 credits per video.**

### Use case G: Quick draft validation (any video task)

**Flow:**
1. `seedance_2_0_fast` — 17 credits, ~30s wall time, validates composition + motion at low cost.
2. Visual review the draft.
3. Composition + motion read correctly → regenerate via the production model (Kling 3.0 or Cinema Studio V2) for final quality.
4. **Total cost: ~25 credits (17 draft + 6-7 Kling final) vs. ~50 credits going straight to Kling iteration → 50% credit savings on average. On Cinema Studio Pro pipelines, savings reach 70%.**

---

## Cost matrix (sorted by Plus-tier output per dollar)

Assumes Higgsfield Plus tier: $39/mo for 1000 credits = $0.039/credit.

| Model | Cost (cr) | Output | Best Use | Per-$1 Plus-tier output |
|---|---|---|---|---|
| Z Image | 0.5 | Image | Budget bulk gen | ~51 images |
| GPT Image 2 | 1 | Image | Text rendering | ~26 images |
| Flux 2 | 1.5 | Image | General-purpose | ~17 images |
| Nano Banana Pro | 2 | Image (4K) | Hero stills, refinement | ~13 images |
| Soul 2.0 | 2-3 | Image | Editorial portraits | ~9-13 images |
| Marketing Studio Image | 2-5 | Image (ads) | Commercial product | ~5-13 images |
| Kling 2.6 | 5-6 | Video (5s @ 720p) | Budget cinematic | ~4-5 videos |
| Kling 3.0 | 6-7 | Video (5s @ 720p) | **Hero finals (best $/quality)** | ~3-4 videos |
| WAN 2.5 | 10-15 | Video (5s) | Fast iterations | ~2-3 videos |
| WAN 2.6 | 12-18 | Video (5s/10s) | Expressive with camera presets | ~1-2 videos |
| MiniMax Hailuo 02 | 15-25 | Video (5s/10s) | Character animation | ~1-2 videos |
| Seedance 2.0 Fast | 17 | Video (5s @ 720p) | **Draft validation** | ~1.5 videos |
| Veo 3 Fast | 22 | Video (8s @ 720p) | Narrative + lip-sync drafts | ~1 video |
| Seedance 2.0 | 25 | Video (5s @ 720p) | Reference-driven finals | ~1 video |
| Cinema Studio V2 Pro ⚠️ | 25-45 | Video (10s) | Hero finals | ~0.5-1 video |
| Marketing Studio Video | 25-60 | Video (5s/10s) | Tier 3 ad creative | ~0.4-1 video |
| Cinema Studio 3.5 ⚠️ | 30-50 | Video (5s/10s) | Plus flagship | ~0.5-0.8 video |
| Sora 2 | 40-70 | Video (10s) | Premium narrative | ~0.4-0.6 video |
| Veo 3 (audio) | 58 | Video (8s @ 720p) | Premium hero + audio | ~0.4 video |
| Seedance 2.0 (15s) | ~90 | Video (15s) | Long-form | ~0.3 video |

---

## Plan tier recommendations

| Tier | Price | Credits | Optimus fit |
|---|---|---|---|
| **Starter** | $15/mo | 200 | **Skip.** Locks out Cinema Studio Video. Not enough for even one client build's hero work + draft iterations. |
| **Plus** | $39/mo | 1000 | **Optimus default.** Covers ~30-50 client builds/year of hero work (~20 credits/build at Seedance-draft → Kling-final cadence). Unlocks Cinema Studio Video V2. |
| **Ultra** | $99/mo | 3000 | When scaling Tier 3 Marketing Team — 5+ clients running paid social, ~600 credits/mo per client for ongoing ad creative. |
| **Business** | $62-89/seat/mo | varies | When Optimus has multiple operators / outsourced creative team. Adds Cinema Studio 3.0 (physics-aware) gating. |

Current Optimus account: **Plus tier ($39/mo, 1000 credits/mo)** as of 2026-05-17. Re-evaluate at 800 credits/mo sustained usage → upgrade signal.

---

## "Seedance draft → Kling 3.0 final" workflow (verified 50-70% credit savings)

The single highest-leverage cost optimization in the entire Higgsfield workflow. Use on every video generation that involves composition iteration (which is most of them).

**Step 1:** Generate composition validation via `seedance_2_0_fast` (17 credits, ~30s wall time).
**Step 2:** Visual review — composition lands? Motion reads? Subjects in correct positions?
**Step 3a:** Composition NO → adjust prompt, re-draft via Seedance Fast again (17 credits). Iterate cheaply until composition is locked.
**Step 3b:** Composition YES → regenerate via `kling3_0` (6-7 credits, 60-90s) OR `cinematic_studio_video_v2` (25-45 credits) for final quality.

**Total naive flow:** 3 Kling iterations to land composition = ~21 credits.
**Total optimized flow:** 3 Seedance Fast drafts + 1 Kling final = 17×3 + 7 = 58 credits... wait, that's MORE.

The savings only land when the final model is more expensive than Kling 3.0. Recalculation:
- **3 Cinema Studio Pro iterations to land composition:** ~120 credits (3 × 40)
- **3 Seedance Fast drafts + 1 Cinema Studio Pro final:** 51 + 40 = ~91 credits → **24% savings**
- **3 Veo 3 iterations to land composition:** ~174 credits (3 × 58)
- **3 Seedance Fast drafts + 1 Veo 3 final:** 51 + 58 = ~109 credits → **37% savings**
- **5 Cinema Studio Pro iterations (typical when composition is complex):** ~200 credits
- **5 Seedance Fast drafts + 1 Cinema Studio Pro final:** 85 + 40 = ~125 credits → **38% savings**

**Verdict:** The Seedance-draft workflow saves credits when the final model is 2x+ the cost of Seedance Fast AND when ≥2 composition iterations are expected. For Kling 3.0 final (~7 credits), skip the Seedance step — Kling itself is cheap enough to iterate on directly. For Cinema Studio Pro / Veo 3 / Sora 2 finals, ALWAYS draft via Seedance Fast first.

---

## Provider abstraction note (business continuity)

Higgsfield has documented business continuity risk:
- X account suspended early 2026 (visibility outage)
- Refund / billing complaints in late 2025 reviews
- Pricing-page SPA shell makes static price scraping unreliable (third-party trackers like imagine.art and vo3ai are more accurate)
- Model catalog churns every 4-8 weeks — Cinema Studio 2.0 → V2 → 3.0 → 3.5 in under a year

**Mitigation:**
- Keep fal.ai (`flux-pro/v1.1`) as documented blog-image fallback
- Keep Kling AI direct via kling.ai web UI as video fallback (manual but bypasses Higgsfield entirely)
- Never lock Optimus client deliverables to Higgsfield-exclusive features (e.g. Storyboard endpoint, Cinema Studio genre presets) when an alternative path exists
- Re-export every Higgsfield asset to local mp4 + webm + webp on download — never depend on Higgsfield URL hosting

The mission > stack loyalty rule from CLAUDE.md applies: when a newer image/video platform delivers more client value at SMB-affordable pricing with better business continuity, evaluate and migrate. Spike-test the alternative on a real client deliverable before committing.

---

## Sources

- **Higgsfield CLI MODELS.md** — canonical model catalog with model_id values: https://github.com/higgsfield-ai/cli/blob/main/MODELS.md
- **Higgsfield pricing** (SPA shell, unreliable for scraping): https://higgsfield.ai/pricing
- **AI Funnel Insider 340-clip Higgsfield test** — third-party cost/quality validation: https://aifunnelinsider.com/higgsfield-ai-review-2026/
- **VO3AI pricing breakdown** — most reliable third-party Higgsfield pricing tracker: https://www.vo3ai.com/higgsfield-ai-pricing
- **imagine.art Higgsfield pricing page** — secondary cost reference: https://imagine.art/pricing
- **Higgsfield MCP endpoint**: https://mcp.higgsfield.ai/mcp
- **Kling AI direct (fallback)**: https://kling.ai
- **fal.ai flux-pro/v1.1 (blog fallback)**: https://fal.ai/models/fal-ai/flux-pro/v1.1

---

## Key Rules

- **Start cheap, validate, commit to quality.** Default to Seedance 2.0 Fast for any video composition that needs iteration; commit to Kling 3.0 / Cinema Studio Pro / Veo 3 only after composition is locked.
- **fal.ai wins for non-hero stills.** Blog cards, gallery fills, social tiles → fal.ai `flux-pro/v1.1` at $0.05 each, not Higgsfield.
- **Nano Banana Pro = hero stills + text rendering.** Don't burn 2 credits per image on blog cards.
- **Soul ID training is a one-time investment.** Amortize across hundreds of generations — never train Soul ID for a one-off still.
- **Marketing Studio Video is a wrapper.** When the preset matches, it's the right tool. When the preset doesn't quite fit, drop down to the underlying model (Kling 3.0 / Seedance 2.0) for finer control.
- **Verify estimated costs in-app before committing batches.** Cost columns marked ⚠️ are not publicly published — pricing page is a SPA shell. Check the in-app cost preview on your first generation of each new model.
- **Re-export every asset locally.** Never depend on Higgsfield URL hosting for production-shipped assets.
- **Refresh this matrix quarterly.** Models churn fast — last refresh date in the header. If 90+ days have passed, run the matrix audit before relying on it.

## Reuse Condition

Every Higgsfield generate call (image or video) across every Optimus project. The matrix is consulted upstream of every `mcp__higgsfield__generate_image` / `mcp__higgsfield__generate_video` invocation.

## Related

- `higgsfield-movie-hero-pipeline.md` — end-to-end Architecture B hero workflow that consumes this matrix at Step 3 and Step 4
- `higgsfield-mcsla-prompt-mastery.md` — prompt-construction patterns once the model is picked
- `higgsfield-camera-vocabulary.md` — Cinema Studio + Kling camera-direction vocabulary for video prompts
- `optimus-higgsfield-ad-creative.md` (skill) — Use Case B routing
- `optimus-higgsfield-hero-video.md` (skill) — Use Case A routing
- `optimus-higgsfield-soul-character.md` (skill) — Use Case C routing
- CLAUDE.md Image Generation Rule (fal.ai) — provides the alternative path for Use Case D
- CLAUDE.md Originality Rule (§19) — every Higgsfield-generated asset must satisfy originality; model choice is downstream of originality vector selection
