# Pattern: Higgsfield model selection matrix
**Category:** AI Assets / Decision Framework / Cost Optimization
**First used:** Goddu Imprint — 2026-05-17
**Status:** ACTIVE since 2026-05-17. Refresh model catalog quarterly — Higgsfield ships new models every 4-8 weeks and retires old ones almost as fast. **Last refresh: 2026-05-17 — Use Case D rewritten: fal.ai retired as default; FLUX.2 Pro promoted to blog-image default after founder confirmation Higgsfield Plus tier ships 6 permanent unlimited image models. Seedance-draft workflow removed in favor of zero-credit SIMULATION step per `higgsfield-cost-approval-gate.md`.**

## What
A decision tree + cost matrix for picking the right Higgsfield model for each Optimus use case. Higgsfield ships 10+ image models and 10+ video models with overlapping capabilities and 10-100x cost variance. Defaulting to the flagship model on every job burns the Plus-tier 1000-credit budget in days; defaulting to the cheapest model ships visibly inferior client deliverables. This matrix is the routing logic.

## When to Use
Every time the orchestrator (or animation-specialist / ad-creative agent) is about to call `mcp__higgsfield__generate_image` or `mcp__higgsfield__generate_video`. Consult the matrix BEFORE the call to pick the model that matches use-case quality requirement and budget envelope. Re-consult quarterly to catch new model releases and price changes.

## How

### Step 1 — Identify the use case

Optimus has seven canonical use cases. Map the current task to one of them (see Section "Use case decision tree" below). If the task doesn't map cleanly, default to Use Case A treatment (highest-quality settings) and flag for matrix update.

### Step 2 — Pick the model from the matrix

Use the Cost Matrix table to pick the model. Optimization principle: **simulate before spending.** Run the zero-credit text-based SIMULATION step (per `higgsfield-cost-approval-gate.md`) before any generate_video call — describe frame 0s/3s/7s/10s, run the 5-criterion gap analysis, fix the prompt until simulation passes, then generate once. Cinema Studio V2 is the permanent video default. Escalate to Kling 3.0 / Seedance 2.0 only after 3-5 Cinema Studio failures (per the gate's escalation block), never as a draft step.

### Step 3 — Generate

Call the MCP tool with the chosen `model` parameter. All Higgsfield models are exposed through `mcp__higgsfield__generate_image` and `mcp__higgsfield__generate_video` with `model: <model_id>` from the catalog below.

---

## Complete model catalog

### Image models

| model_id | Name | Provider | Best at | Aspect ratios | Cost (cr) | When to pick | When to avoid |
|---|---|---|---|---|---|---|---|
| `flux_2` | FLUX.2 Pro | Black Forest Labs | Fast general-purpose, high quality | 16:9, 9:16, 1:1, 4:3, 3:4 | **0 (365 unlimited on Plus tier — auto-renewing)** | **Default for blog cards, article headers, social tiles, gallery images** — Optimus default workhorse | Hero-grade detail work where Nano Banana's text rendering matters |
| `nano_banana_pro` | Nano Banana | Google | 4K resolution, strongest at composition/lighting/text rendering | 16:9, 9:16, 1:1, 4:3, 3:4 | **0 (365 unlimited on Plus tier — auto-renewing)** | Hero stills, refinement passes, anything with on-image text or signage/packaging mockups | Bulk gen where Flux 2 is equivalent (Flux 2 is faster) |
| `gpt_image_2` | GPT Image | OpenAI | Strong text rendering | 16:9, 9:16, 1:1 | **0 (365 unlimited on Plus tier — auto-renewing)** | Images with text overlays when Nano Banana isn't a fit | Photoreal portraits |
| `seedream_4_5` | Seedream 4.5 | ByteDance | Visual reasoning tier (premium), complex scene composition | 16:9, 9:16, 1:1, 4:3, 3:4 | **0 (365 unlimited on Plus tier — auto-renewing)** | Complex multi-subject scenes where layout reasoning matters | Simple stills (Flux 2 is equivalent and faster) |
| `seedream_5_lite` | Seedream V5 Lite | ByteDance | Visual reasoning, fast | 16:9, 9:16, 1:1 | **0 (365 unlimited on Plus tier — auto-renewing)** | Conceptual exploration, brand mood boards, lightweight reasoning | Final hero-grade output |
| `kling_o1_image` | Kling O1 Image | Kuaishou | Cinematic-register stills in the Kling family | 16:9, 9:16, 1:1 | **0 (365 unlimited on Plus tier — auto-renewing)** | Stills that will be animated by Kling video later (in-family pipeline keeps register coherent) | Non-Kling video pipelines |
| `soul` / `soul_2` | Soul 2.0 | Higgsfield | Fashion-grade hyper-realism, 20+ launch presets | 9:16, 1:1, 16:9, 4:3, 3:4 | ~2-3 | Editorial portraits, lifestyle stills, Soul ID identity-locked stills | Product-on-white commercial shots |
| `soul_id` | Soul ID | Higgsfield | Identity-locked character generation across all Soul presets | 9:16, 1:1, 16:9, 4:3, 3:4 | One-time training ~50-100 + ~2-3/gen | AI spokesperson, recurring character across campaigns | One-off stills (training cost wasted) |
| `soul_cinema` | Soul Cinema | Higgsfield | Cinematic stills tuned for later animation | 9:16, 1:1, 16:9 | ~2-3 | Stills that will feed Cinema Studio Video for hero generation | Stills shipped as final stills (Nano Banana is sharper) |
| `soul_cast` | Soul Cast | Higgsfield | Text-only character/avatar generation | 9:16, 1:1, 16:9, 4:3, 3:4 | ~2 | Brand avatar exploration, character mood-boards | Photoreal lifestyle |
| `soul_location` | Soul Location | Higgsfield | Environment and location plates | 16:9, 9:16, 1:1 | ~2 | Background plates for compositing, location B-roll stills | Subject-driven shots |
| `flux_kontext` | Flux Kontext | Black Forest Labs | Context-aware editing/iteration | 16:9, 9:16, 1:1 | 1.5 | Iterating on a base image, in-painting | First-pass generation |
| `marketing_studio_image` | Marketing Studio Image | Higgsfield | Commercial/product/ads — editorial product still life register | 16:9, 9:16, 1:1, 4:3 | ~2-5 | Hero stills for Architecture B movie-hero pipeline, ad creative stills | Portraits |
| `z_image` | Z Image | Higgsfield | Fast budget option | 16:9, 9:16, 1:1 | 0.5 | High-volume bulk gen when unlimited models are constrained (rare) | Hero or near-hero use |
| `seedream_4_0` | Seedream 4.0 | ByteDance | Visual reasoning tier (premium, predecessor to 4.5) | 16:9, 9:16, 1:1, 4:3, 3:4 | ~2-3 | When Seedream 4.5 specifically unavailable | Simple stills (Flux 2 is unlimited and equivalent) |

### Video models

| model_id | Name | Provider | Best at | Aspect ratios | Durations | Cost (cr) | When to pick | When to avoid |
|---|---|---|---|---|---|---|---|---|
| `cinematic_studio_video_v2` | Cinema Studio Video V2 | Higgsfield | Refined cinematic camera + color, 8 genres | 16:9, 9:16, 1:1 | 3-12s | ~25-45 ⚠️ | Hero finals (Architecture B), genre-driven cinematic shots | Drafts (too expensive); rapid iteration |
| `cinematic_studio_3_0` | Cinema Studio 3.0 | Higgsfield | Physics-aware, collapsed 7 genres | 16:9, 9:16 | 3-10s | ~30-50 ⚠️ | Business/Team tier only — physics-realistic shots | Not on Plus tier (gated) |
| `cinematic_studio_3_5` | Cinema Studio 3.5 | Higgsfield | Genre/Style/Camera 3-pill UI, native audio, speed-ramp, 9 reference images | 16:9, 9:16, 1:1 | 3-12s | ~30-50 ⚠️ | Plus tier flagship — when audio sync + reference-heavy shot needed | Cheaper drafts |
| `kling3_0` | Kling 3.0 | Kuaishou | Multi-shot, audio sync, motion-transfer, 4K cinema-grade | 16:9, 9:16, 1:1 | 5s, 10s | 6-7 (5s @ 720p) | **Troubleshooting alternative after 3-5 failed Cinema Studio V2 attempts** (per `higgsfield-cost-approval-gate.md` escalation block) — excellent face / lip-sync, best for character-driven shots | Promoting to workflow default — Cinema Studio V2 is the permanent default per skills |
| `kling2_6` | Kling 2.6 | Kuaishou | Cinematic motion, advanced physics | 16:9, 9:16, 1:1 | 5s, 10s | ~5-6 (5s) | Budget-cinematic, motion-physics shots | When 3.0 quality is reachable in budget |
| `veo_3` | Veo 3 (audio) | Google | Long-form narrative, native audio | 16:9, 9:16 | 8s | 58 (8s @ 720p) | Premium hero with audio, narrative ads | Budget projects |
| `veo_3_fast` | Veo 3 Fast | Google | Same quality envelope, lower latency | 16:9, 9:16 | 8s | 22 (8s @ 720p) | Narrative + lip-sync drafts | When ambient/no-audio works (Kling is cheaper) |
| `seedance_2_0` | Seedance 2.0 | ByteDance | Reference-driven (image/video/audio refs), consistent identity, multi-SKU | 16:9, 9:16, 1:1 | 5s, 10s, 15s | 25 (5s @ 720p) | Multi-SKU product campaigns, consistent-character video sequences | One-off hero shots |
| `seedance_2_0_fast` | Seedance 2.0 Fast | ByteDance | Reference-driven, faster | 16:9, 9:16, 1:1 | 5s, 10s | 17 (5s @ 720p) | Reference-driven shots where Seedance is the right primary tool (rare) | As a "draft model" before Cinema Studio — the zero-credit SIMULATION step per `higgsfield-cost-approval-gate.md` replaces this workflow |
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
1. Still gen: `nano_banana_pro` (unlimited on Plus tier, 4K, strongest at composition + text rendering) OR `marketing_studio_image` (~2-5 cr, editorial product/lifestyle register). Default to Nano Banana — it's unlimited AND best-in-class for hero stills. Pick Marketing Studio Image only when its specific commercial-product register is the visual target.
2. **SIMULATION step** per `higgsfield-cost-approval-gate.md` — zero-credit text simulation of frame 0s/3s/7s/10s + 5-criterion gap analysis. Fix prompt → re-simulate → only proceed when ALL PASS.
3. Animation: `cinematic_studio_video_v2`, `genre: intimate` / `drama` / `commercial`, `start_image` lock. Cinema Studio V2 is the permanent default. 25-45 cr per call (does NOT trigger Step 2 high-cost alert — Cinema Studio V2 is exempt).
4. **Total cost: 25-45 cr per hero** (~$1.00-1.80 at Plus tier) for the typical first-pass success. If Cinema Studio V2 fails after 3-5 attempts with simulation-guided prompt fixes, escalate to Kling 3.0 (6-7 cr) per the gate's escalation block.

See `higgsfield-movie-hero-pipeline.md` for the full end-to-end workflow + `higgsfield-cost-approval-gate.md` for the gate + simulation discipline.

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

### Use case D: Blog card images, article headers, trade gallery, social tiles (Optimus client builds)

**Flow:**
1. **Default: Higgsfield FLUX.2 Pro** (`model: flux_2`) via `mcp__higgsfield__generate_image`. Aspect 16:9 for headers, 1:1 for cards, 4:5 or 3:2 for trade gallery. 0 cr — unlimited on Plus tier (365-day, auto-renewing).
2. **For stills with text rendering** (signage mockups, packaging, social tile with logo + headline): Nano Banana Pro (`model: nano_banana_pro`). Also 0 cr unlimited on Plus.
3. **For premium-reasoning composition** (complex multi-subject scenes): Seedream 4.5 (`model: seedream_4_5`). Also 0 cr unlimited on Plus.
4. **Never use:** Nano Banana 2 (use original Nano Banana Pro as permanent default instead) or paid-credit models (Soul 2, Marketing Studio Image) for blog cards / gallery — overspec'd by 4-10x AND/OR cost credits unnecessarily.
5. **Total cost: $0 marginal at Plus tier.** fal.ai retired as the blog-image default 2026-05-17 (founder confirmation: Higgsfield Plus tier ships 6 permanent unlimited image models, removing fal.ai's cost-per-image advantage).
6. **Gate handling:** image generation with the 6 permanent unlimited models bypasses gate Steps 1+2 entirely. Step 0 (active-skill confirmation) still runs per `higgsfield-cost-approval-gate.md`. No balance check, no high-cost confirmation, no SIMULATION step (zero-cost retake on failure).

### Use case E: Editorial cinematic stills with text rendering

**Flow:**
1. `nano_banana_pro` (4K, strongest text rendering per official docs). 0 cr — unlimited on Plus tier.
2. Alternate: `gpt_image_2` (also unlimited on Plus). Pick GPT Image 2 when the text is the only requirement; pick Nano Banana when composition + lighting + text all matter.
3. **Total cost: $0 marginal at Plus tier.**

Note: per CLAUDE.md Image Generation Rule, AI text rendering is unreliable for production. These models are *better* than alternatives at text — they are still not perfect. Visual-review every output; regenerate any with garbled characters (free retake on unlimited models).

### Use case F: Product showcase video for e-commerce

**Flow:**
1. **Single SKU:** `marketing_studio_video` with Product preset.
2. **Multi-SKU campaign (5+ products, consistent identity required):** `seedance_2_0` with the lead product's still as image reference. Subsequent SKUs use the same reference for visual continuity.
3. **Total cost: ~25-50 credits per video.**

### Use case G: Pre-generation prompt validation (any video task)

**Flow:**
1. **SIMULATION step** per `higgsfield-cost-approval-gate.md` — zero-credit text-based 4-frame storyboard (0s/3s/7s/10s) + 5-criterion gap analysis. Replaces the previously-recommended Seedance-draft validation workflow.
2. If simulation reveals gaps (motion not readable in 1-2s, text-overlay zone missing, AI-slop trigger present, end-frame doesn't match loop intent, brand register drift) → fix prompt → re-simulate.
3. Only when simulation passes ALL criteria → call the production model (Cinema Studio V2 25-45 cr default, or escalation alternative after 3-5 failures).
4. **Total cost: ~25-45 credits per hero** (Cinema Studio V2 default) with ~70-80% first-pass success after simulation discipline. Compare to old Seedance-draft workflow (~25-91 cr depending on iteration count) — simulation is both cheaper AND faster (no Seedance wall time).

---

## Cost matrix (unlimited models on top, then per-credit models sorted by cost)

Assumes Higgsfield Plus tier: $39/mo for 1000 credits + 6 permanent unlimited image models = $0.039/credit on paid models, $0 marginal on unlimited.

**Unlimited (Plus tier 365-day auto-renewing — zero marginal cost):**

| Model | Cost | Output | Best Use |
|---|---|---|---|
| FLUX.2 Pro | 0 (unlimited) | Image | **Default blog cards / headers / gallery / general workhorse** |
| Nano Banana | 0 (unlimited) | Image (4K) | Hero stills, text rendering, signage mockups |
| GPT Image | 0 (unlimited) | Image | Text-overlay-heavy stills |
| Seedream 4.5 | 0 (unlimited) | Image | Complex multi-subject composition |
| Seedream V5 Lite | 0 (unlimited) | Image | Mood boards, lightweight reasoning |
| Kling O1 Image | 0 (unlimited) | Image | Stills feeding Kling video later (in-family pipeline) |

**Per-credit (sorted by cost ascending):**

| Model | Cost (cr) | Output | Best Use | Per-$1 Plus-tier output |
|---|---|---|---|---|
| Z Image | 0.5 | Image | Bulk gen when unlimited models constrained (rare) | ~51 images |
| Flux Kontext | 1.5 | Image | Iterating on base image, in-painting | ~17 images |
| Soul 2.0 | 2-3 | Image | Editorial portraits with Soul ID identity-lock | ~9-13 images |
| Soul Cinema | 2-3 | Image | Stills tuned for later Cinema Studio animation | ~9-13 images |
| Soul Location | 2 | Image | Environment / location plates | ~13 images |
| Soul Cast | 2 | Image | Brand avatar / character mood-boards | ~13 images |
| Marketing Studio Image | 2-5 | Image (ads) | Commercial / product editorial | ~5-13 images |
| Seedream 4.0 | 2-3 | Image | When Seedream 4.5 specifically unavailable | ~9-13 images |
| Kling 2.6 | 5-6 | Video (5s @ 720p) | Budget cinematic | ~4-5 videos |
| Kling 3.0 | 6-7 | Video (5s @ 720p) | Troubleshooting alternative after 3-5 Cinema Studio failures (per gate escalation) | ~3-4 videos |
| WAN 2.5 | 10-15 | Video (5s) | Fast iterations with Camera Controls presets | ~2-3 videos |
| WAN 2.6 | 12-18 | Video (5s/10s) | Expressive with camera presets | ~1-2 videos |
| MiniMax Hailuo 02 | 15-25 | Video (5s/10s) | Character animation specialist | ~1-2 videos |
| Seedance 2.0 Fast | 17 | Video (5s @ 720p) | Reference-driven shots where Seedance is primary tool (rare) | ~1.5 videos |
| Veo 3 Fast | 22 | Video (8s @ 720p) | Narrative + lip-sync (does NOT trigger gate Step 2) | ~1 video |
| Seedance 2.0 | 25 | Video (5s @ 720p) | Reference-driven finals, ad troubleshooting alt | ~1 video |
| Cinema Studio V2 Pro | 25-45 | Video (10s) | **Permanent video default — Architecture B hero, Soul character video** (EXEMPT from gate Step 2) | ~0.5-1 video |
| Marketing Studio Video | 25-60 | Video (5s/10s) | Tier 3 ad creative (triggers gate Step 2 at high end) | ~0.4-1 video |
| Cinema Studio 3.5 | 30-50 | Video (5s/10s) | Plus tier flagship when audio sync needed (triggers gate Step 2 at high end) | ~0.5-0.8 video |
| Sora 2 | 40-70 | Video (10s) | Premium narrative (triggers gate Step 2) | ~0.4-0.6 video |
| Veo 3 (audio) | 58 | Video (8s @ 720p) | Premium hero + audio (triggers gate Step 2) | ~0.4 video |
| Seedance 2.0 (15s) | ~90 | Video (15s) | Long-form (triggers gate Step 2) | ~0.3 video |

---

## Plan tier recommendations

| Tier | Price | Credits | Optimus fit |
|---|---|---|---|
| **Starter** | $15/mo | 200 | **Skip.** Locks out Cinema Studio Video. Not enough for even one client build's hero work + draft iterations. |
| **Plus** | $39/mo | 1000 | **Optimus default.** 1000 credits/mo + 6 permanent unlimited image models (FLUX.2 Pro, Nano Banana, GPT Image, Seedream 4.5, Seedream V5 Lite, Kling O1 Image) + unlocks Cinema Studio Video V2. Image-gen costs are effectively $0 marginal; credits are spent almost entirely on video (Cinema Studio V2 25-45 cr, Marketing Studio Video 25-60 cr, Seedance 17-25 cr, Kling 3.0 6-7 cr/gen). Covers 30-50 client builds/year of hero video work. Check current balance via `mcp__higgsfield__balance` before each video-gen workflow. |
| **Ultra** | $99/mo | 3000 | When scaling Tier 3 Marketing Team — 5+ clients running paid social, ~600 credits/mo per client for ongoing ad creative. |
| **Business** | $62-89/seat/mo | varies | When Optimus has multiple operators / outsourced creative team. Adds Cinema Studio 3.0 (physics-aware) gating. |

Current Optimus account: **Plus tier ($39/mo, 1000 credits/mo)** with 6 permanent unlimited image models active. Re-evaluate at 800 credits/mo sustained video-gen usage → Ultra upgrade signal.

---

## SIMULATION-FIRST workflow (replaces all draft-model routing)

The single highest-leverage cost optimization in the entire Higgsfield workflow. Use on every video generation, regardless of which final model is targeted.

**Step 1:** Write the finalized MCSLA prompt (per `higgsfield-mcsla-prompt-mastery.md`).
**Step 2:** Run the **zero-credit SIMULATION** per `higgsfield-cost-approval-gate.md` — text-describe frame 0s / 3s / 7s / 10s. Then run the 5-criterion gap analysis: motion readable in 1-2s, text-overlay zone present, no AI-slop triggers, end-frame matches loop intent, brand register holds across 10s.
**Step 3:** If any gap → fix prompt → re-simulate. Iterate until simulation passes all 5 criteria (still zero cost).
**Step 4:** Only when simulation passes → call the production model (Cinema Studio V2 default at 25-45 cr).
**Step 5:** After generation, extract actual frames via ffmpeg and compare against simulation. Significant divergence logged to `knowledge/errors/higgsfield-prompt-simulation-divergences.md`.
**Step 6:** If output still unusable, count the attempt. After 3-5 failed Cinema Studio V2 attempts, escalate to Kling 3.0 / Seedance 2.0 / Kling 3.0 + Soul ID per the gate's escalation block (per skill).

**Why this replaces Seedance-draft routing:**
- Seedance Fast at 17 cr per draft was only a 24-38% savings on Cinema Studio Pro pipelines, and ZERO savings (negative) on Kling 3.0 pipelines.
- The simulation step is **0 cr** and runs in seconds. The savings are 100% of the draft cost.
- Cinema Studio V2 first-pass success rate goes from ~30-40% (no upstream check) to ~70-80% (simulation-guided prompts).
- Net economics: Cinema Studio V2 default at 25-45 cr × ~1.3 attempt average ≈ 32-58 cr per hero vs. old Seedance-draft workflow at ~91 cr for the same outcome.

**The Seedance-as-draft pattern is retired.** Seedance 2.0 (`seedance_2_0`) remains a valid ad-creative troubleshooting alternative per the 3-5-attempt escalation block, NOT a routine draft step.

---

## Provider abstraction note (business continuity)

Higgsfield has documented business continuity risk:
- X account suspended early 2026 (visibility outage)
- Refund / billing complaints in late 2025 reviews
- Pricing-page SPA shell makes static price scraping unreliable (third-party trackers like imagine.art and vo3ai are more accurate)
- Model catalog churns every 4-8 weeks — Cinema Studio 2.0 → V2 → 3.0 → 3.5 in under a year

**Mitigation:**
- fal.ai retired 2026-05-17 — Higgsfield Plus tier ships 6 permanent unlimited image models, removing fal.ai's cost advantage. If Higgsfield MCP fails AND a blog-image batch is blocking a client launch: spin up any text-to-image API with the same prompt as a one-off (the prompts in `/scripts/prompts/<slug>.txt` are portable).
- Keep Kling AI direct via kling.ai web UI as the last-resort video fallback (manual flow per `knowledge/patterns/kling-video-hero.md` — bypasses Higgsfield entirely)
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
- **Kling AI direct (last-resort video fallback)**: https://kling.ai

---

## Key Rules

- **Simulate before spending.** Cinema Studio V2 is the permanent video default. Run the zero-credit SIMULATION step (per `higgsfield-cost-approval-gate.md`) before any generate_video call. Escalate to Kling 3.0 / Seedance 2.0 only after 3-5 Cinema Studio failures, never as a draft step.
- **Blog cards / headers / gallery use unlimited models.** Default `flux_2` (FLUX.2 Pro) via `mcp__higgsfield__generate_image` — 0 credits, unlimited on Plus tier. Use `nano_banana_pro` for stills with text rendering. fal.ai retired 2026-05-17.
- **Soul ID training is a one-time investment.** Amortize across hundreds of generations — never train Soul ID for a one-off still. Training triggers gate Step 2 (>50 cr).
- **Marketing Studio Video is a wrapper.** When the preset matches, it's the right tool. When the preset doesn't quite fit, drop down to the underlying model (Kling 3.0 / Seedance 2.0) for finer control.
- **Verify per-call costs in-app before committing batches.** Cost columns reflect typical ranges; verify the in-app cost preview on the first call of each new model in each new aspect/duration combo.
- **Batch totals trigger gate Step 2, not per-call cost.** A batch of small calls can easily exceed the 50 cr threshold while every individual call is under it.
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
- `higgsfield-cost-approval-gate.md` (Pattern #85) — Step 0/1/2 gate + SIMULATION step + 3-5-attempt escalation that this matrix routes to
- CLAUDE.md Image Generation Rule (Higgsfield) — overall image generation discipline (post-fal.ai retirement)
- CLAUDE.md Originality Rule (§19) — every Higgsfield-generated asset must satisfy originality; model choice is downstream of originality vector selection
