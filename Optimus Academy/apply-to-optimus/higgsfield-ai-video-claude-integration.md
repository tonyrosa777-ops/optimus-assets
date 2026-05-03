---
title: Higgsfield AI Video — Claude MCP Integration — apply-to-Optimus bridges
schema-version: 1
concept: [[../concepts/higgsfield-ai-video-claude-integration]]
source-references: ["[[../daily/2026-05-03#17:28 — \"you can basically make ANY video or image directly out of claude now ...\" by midirbot]]"]
created: 2026-05-03
last-updated: 2026-05-03 17:28
tags: [#learning/applied, #applies-to/website-dev, #applies-to/optimus-inc/marketing, #status/active]
---

# Higgsfield AI Video — Claude MCP Integration — apply-to-Optimus bridges

> **Concept:** [[../concepts/higgsfield-ai-video-claude-integration]]
> **Source(s):**
> - [[../daily/2026-05-03#17:28 — "you can basically make ANY video or image directly out of midirbot now ..." by midirbot]] — midirbot
>
> **Last updated:** 2026-05-03 17:28

---

## Applied to animation-specialist agent

applies-to:: [[../../.claude/agents/build/animation-specialist]]
status:: not-started
value-vector:: productivity, revenue
expected-impact:: large
created:: 2026-05-03
last-updated:: 2026-05-03 17:28

> **Applies to:** [[../../.claude/agents/build/animation-specialist]]
> **Status:** `not-started`
> **Value vector(s):** productivity, revenue
> **Expected impact:** large
> **Last updated:** 2026-05-03 17:28

### What I learned

Higgsfield's MCP server (launched 2026-04-30) exposes 30+ video and image models inside Claude with start-and-end-frame interpolation, Soul-trained consistent characters, and Cinema Studio camera controls — see [[../concepts/higgsfield-ai-video-claude-integration]]. The integration collapses the existing multi-tool hero-video pipeline (fal.ai start image + fal.ai end image + Kling video) into one Claude conversation. This makes "AI-generated video hero" a viable alternative branch to the existing 3-layer canvas hero pattern.

### Why it applies to animation-specialist agent

The `animation-specialist` agent is the executor of the Hero Architecture Rule (CLAUDE.md). Today its decision tree is constrained to the 3-layer canvas pattern: HeroParticles + brand-specific canvas + Framer Motion stagger text. It runs the 10-concept brainstorm → harsh-critic agent → build-winner workflow, with the LogoParticles fallback for failed attempts.

Higgsfield-in-Claude introduces a **second valid hero architecture** that the animation-specialist's decision tree should branch to when a brand fits it better. The branch is real because:

1. **Some brands fit AI-video heroes better than canvas heroes.** Luxury hospitality (Enchanted Madison reference), travel, cinematic storytelling brands, fashion, food/beverage aesthetic-led — all suit a 10-15s cinematic hero MP4 more naturally than a particle/canvas system.
2. **Canvas hero builds carry meaningful engineering time.** The 10-concept brainstorm + critic + build-winner cycle takes hours per project even when it goes well. A Higgsfield-generated hero (start frame + end frame + animate) takes minutes once the brand prompt is dialed in.
3. **Mission-fit alignment** (per `feedback_mission-trumps-stack-loyalty.md`): the goal is bringing newest tech to small businesses at affordable prices. A video hero generated for $5-10 is more SMB-affordable than custom canvas code, AND lands a more premium-feeling output for many brand fits. Both directions point at adoption-as-an-option (not adoption-as-replacement).

The animation-specialist agent should evaluate brand fit during its decision phase, then route to either:
- **3-layer canvas hero** (existing pattern) — for brands where dynamic interactivity, particle metaphor, abstract motion, or domain-specific canvas storytelling fits the brand voice. Trades, professional services, complex SaaS, technical brands.
- **AI-video hero** (new pattern via Higgsfield) — for brands where cinematic storytelling, environment-driven emotion, talent-on-camera (talking-head), or product-on-model rendering fits better. Hospitality, luxury, food/beverage, fashion, travel, lifestyle, wellness.

### How to apply it

This is an agent edit + a Hero Architecture Rule extension in CLAUDE.md. Three concrete files change:

**1. Edit `.claude/agents/build/animation-specialist.md`** to add a decision-phase branch:

- Before the existing 10-concept brainstorm, add a step: **"Evaluate hero architecture fit."** Read `initial-business-data.md` and `design-system.md` Section 8 (brand personality axes). Decide between two architectures:
  - **3-layer canvas hero** (current default) — particle/canvas/SVG pattern.
  - **AI-video hero** (new branch) — Higgsfield-in-Claude generated 10-15s cinematic MP4.
- Document the decision criteria. Suggested rubric: brand voice (storytelling vs. abstract), industry conventions (luxury hospitality leans video, technical SaaS leans canvas), client preference (ask if uncertain), motion budget (the AI-video hero counts as 1 motion layer per the Homepage Section Architecture Rule motion budget — within budget regardless).
- After the decision, route to the appropriate workflow:
  - Canvas branch: existing 10-concept brainstorm → critic → build winner (no change).
  - Video branch: NEW workflow — 5-concept brand-aligned scene brainstorm → critic → Higgsfield prompt construction (start frame + end frame) → animate via Cinema Studio + Kling 3.0 → compress + embed.

**2. Edit CLAUDE.md "Hero Architecture Rule"** to add the AI-video branch:

- Replace "Every hero ships with exactly 3 layers" with "Every hero ships with one of two valid architectures: (a) 3-layer canvas pattern, or (b) AI-video hero pattern." Document each.
- The 3-layer canvas spec stays as currently written.
- Add a new sub-section: **"AI-video hero pattern."** Spec:
  - 10-15 second compressed MP4, 16:9, 4K source compressed to web target (under ~2MB if possible).
  - Generated via Higgsfield MCP in Claude using start-and-end-frame interpolation, Cinema Studio for cinematic camera moves.
  - Layered in the hero with H1 + subheadline + CTAs as text overlays (Framer Motion stagger preserved).
  - Performance budget: video file size capped, lazy-loaded with poster fallback for slow connections, autoplay muted on hero load.
  - Decision criteria: brand voice fit, industry convention, client preference. Animation-specialist agent owns the decision.
- Keep the "primary CTA is always booking, secondary is quiz" rule unchanged regardless of architecture.

**3. Create `knowledge/patterns/ai-hero-video-pipeline.md`** (companion of bridge application #3 below) — the institutional pattern doc for the AI-video hero workflow.

This bridge is a change-request, not a change. Anthony reviews and applies the agent edits + CLAUDE.md edit manually.

### Value vector reasoning

- `productivity`: collapsed pipeline (start frame + end frame + animate, all inside one Claude conversation) saves meaningful engineering time per build. Canvas hero workflow = 10 concepts brainstormed + critic + 1 winner built (custom code). AI-video workflow = 5 scenes brainstormed + critic + 1 winner generated. Estimate ~2-4 hours saved per build that routes to the video branch, compounding across every Optimus client engagement.
- `revenue`: better brand-fit hero for video-suited industries (hospitality, luxury, food/beverage, fashion, travel) lifts perceived premium positioning, supporting higher Pro / Premium tier close rates. The Enchanted Madison-class outputs become repeatable rather than bespoke. Each upgraded close from Starter ($1,500) → Pro ($3,000) → Premium ($5,500) is a real revenue lift; if AI-video heroes meaningfully widen the addressable Premium segment by industry coverage, the lift compounds.

### Status

`not-started`

### Updates

(none)

---

## Applied to Optimus Inc marketing pipeline

applies-to:: [[../../Optimus Inc/social-pipeline/README]]
status:: not-started
value-vector:: revenue, productivity, overhead
expected-impact:: large
created:: 2026-05-03
last-updated:: 2026-05-03 17:28

> **Applies to:** [[../../Optimus Inc/social-pipeline/README]]
> **Status:** `not-started`
> **Value vector(s):** revenue, productivity, overhead
> **Expected impact:** large
> **Last updated:** 2026-05-03 17:28

### What I learned

Higgsfield-in-Claude — see [[../concepts/higgsfield-ai-video-claude-integration]] — gives Optimus access to 30+ image and video models for under $40/month. Anthony's raw thoughts at capture explicitly asked to brainstorm every additional way to use this in marketing beyond the hero use case. This bridge is the brainstorm landing zone for Optimus's own social-pipeline + marketing assets.

### Why it applies to Optimus Inc marketing pipeline

The `Optimus Inc/social-pipeline/` folder is where Optimus's drink-own-champagne marketing pipeline lives. Today it's largely placeholder — see the GTM-engineering bridge ([[gtm-engineering#Applied to Optimus Inc's own outbound pipeline]]) for the broader pipeline build. The 2027-Q3 milestone requires Optimus to run its own marketing autonomously, including content creation. Higgsfield-in-Claude is a candidate substrate for the content-creation layer specifically.

The brainstorm — every marketing surface where Higgsfield lands real value:

| Marketing surface | Asset type | Higgsfield path |
|---|---|---|
| **Optimus website hero** (own site) | 10-15s cinematic MP4 | Start+end frame interpolation, Cinema Studio dolly |
| **Service-page hero animations** (per offering) | 8-12s loops | One per offering: Chat Assistant / Voice Receptionist / Marketing Team / Autonomous Employee, each with brand-aligned scene |
| **Pricing page section dividers** | 3-5s subtle motion loops | Light, ambient, brand-coherent |
| **About / founder intro** | Talking-head with custom audio | Soul training for founder consistency across multiple intro contexts |
| **Blog post header animations** | 8-12s topic-relevant loops | Replaces static fal.ai blog headers; one Higgsfield prompt per article instead of two static images |
| **Social media — TikTok / Reels / Shorts** | 10-15s vertical (9:16) | Daily/weekly cadence; one model preset per topic vertical |
| **Social media — LinkedIn videos** | 10-15s landscape (16:9) | Founder-led + B2B-positioned |
| **Paid ad creative** (when paid acquisition starts) | Multiple variants per campaign | Kling 3.0 tier ($0.60-1.00/video) lets variant testing be cheap |
| **Email marketing** | Animated openers / GIFs | Light loops embedded in transactional + nurture emails |
| **Quiz result page videos** (premium feature) | Personalized 10-15s per archetype | Each archetype gets cinematic confirmation video |
| **Booking confirmation videos** | Thank-you / next-steps animation | Embedded in confirmation emails |
| **Pre-launch teaser videos** | 8-15s cinematic teases | For new offerings, new clients, milestone announcements |
| **Behind-the-scenes content** | 10-15s lifestyle/process content | Daily/weekly social cadence |
| **Service explanation videos** | Short cinematic explainers per offering | Sit on the offering README pages, social, sales decks |
| **Sales-deck embedded videos** | 8-15s contextual loops | Per-prospect customizable if Soul-trained on prospect's brand reference |
| **Pitch deck cover slides** | 5s animated brand opener | One asset reused across all pitch decks |
| **Onboarding flow visual content** | Per-step animations | New client onboarding, internal-tool onboarding |

The pattern: anywhere Optimus today defaults to static visuals or has nothing visual, Higgsfield-in-Claude makes animated alternatives cheap and fast enough to be the new default.

### How to apply it

**Phase 1 — Drink-own-champagne pilot.** Before pushing this into client builds, deploy the Higgsfield workflow on Optimus Inc itself for 30+ days, per `feedback_mission-trumps-stack-loyalty.md` Phase 4 evaluation gate.

1. Subscribe to Higgsfield Plus ($34/month) — covers experimentation budget for ~30-90 production renders depending on model selection.
2. Generate the **Optimus marketing-site hero video** as the first deliverable. 10-15s cinematic, 16:9, brand-aligned scene (TBD — needs design-synthesizer pass). Validates the hero pipeline end-to-end.
3. Generate **one service-page hero per offering** (4 total: Chat Assistant, Voice Receptionist, Marketing Team, Autonomous Employee). Validates the per-offering scaling.
4. Run the **founder-intro talking-head video** using Soul training. Validates the consistent-character feature for repeat use.
5. Generate **3-5 social media videos** per week for 30 days. Validates the social-pipeline cadence.
6. Track total time, total credit spend, output quality, deployment friction. Land results in this H2's `### Updates` sub-section.

**Phase 2 — Pipeline integration.** If Phase 1 validates:

1. Document the workflow in `Optimus Inc/social-pipeline/higgsfield-content-pipeline.md` (lazy-create file inside existing folder).
2. Wire scheduling — the GTM-engineering bridge already proposes APScheduler for Optimus's outbound; the same scheduler could trigger weekly social-content generation runs.
3. Establish the brand-prompt corpus: a documented set of brand-aligned visual descriptors, color palettes, lighting moods, scene archetypes that the Higgsfield prompts pull from for consistency across runs.

**Phase 3 — Productize for clients.** If Phase 2 stabilizes for Optimus's own ops, the same pipeline pattern transfers to Tier-3 Marketing Team client builds (the offering's productized content layer). Cross-reference: [[obsidian-claude-integration#Applied to AI Marketing Team (Tier-3)]] proposes vault-based content drafts; Higgsfield would add the visual layer that the Marketing Team's strategy outputs reference.

This bridge is a change-request, not a change. Anthony reviews and applies the pilot manually.

### Value vector reasoning

- `revenue`: Optimus Inc's own marketing site quality is the most public test of brand voice — a higher-quality, more cinematic, more frequent content output drives inbound discovery, lifts conversion on the marketing site, and feeds the GTM-engineering outbound pipeline with stronger creative. Each marginal lift in inbound or in close rate compounds toward the 2027-Q3 drink-own-champagne milestone.
- `productivity`: cinematic content production today is either expensive (hire a video producer) or absent (Optimus ships static visuals only). Higgsfield-in-Claude collapses video production to a Claude-conversation workflow that Anthony or a future Marketing Team agent can run without specialist video skills. The per-asset time budget drops from "days" or "never" to "minutes."
- `overhead`: replacing a multi-tool video pipeline (Photoshop + Premiere + DaVinci + manual asset management) with one Claude conversation removes coordination overhead, asset version-control overhead, and the cognitive load of context-switching between specialist tools.

### Status

`not-started`

### Updates

(none)

---

## Applied to client-build hero architecture pattern

applies-to:: [[../../knowledge/patterns/ai-hero-video-pipeline]]
status:: not-started
value-vector:: productivity, revenue
expected-impact:: medium
created:: 2026-05-03
last-updated:: 2026-05-03 17:28

> **Applies to:** [[../../knowledge/patterns/ai-hero-video-pipeline]]
> **Status:** `not-started`
> **Value vector(s):** productivity, revenue
> **Expected impact:** medium
> **Last updated:** 2026-05-03 17:28

### What I learned

The Higgsfield-in-Claude pipeline — see [[../concepts/higgsfield-ai-video-claude-integration]] — and Anthony's existing fal.ai+Kling pipeline (referenced from the Enchanted Madison build) both produce the same shape of output: a 10-15 second cinematic MP4 that serves as a website hero alternative to the 3-layer canvas pattern. This needs an institutional pattern doc so any future client build can reference a canonical workflow rather than rediscovering it.

### Why it applies to client-build hero architecture pattern

The `knowledge/patterns/` folder is where cross-client website-build patterns live (folder exists, populated). Today there is no pattern doc for AI-video heroes — the Enchanted Madison workflow lives only in Anthony's head. Without a pattern doc:

- Each future build that wants a video hero rediscovers the workflow from scratch.
- The animation-specialist agent (per bridge application #1 above) has nothing to reference when routing to the video branch.
- Future captures on different AI video tools (Kling-specific, Sora-specific, Runway-specific) have no canonical home to land in for cross-tool comparison.

A pattern doc named `knowledge/patterns/ai-hero-video-pipeline.md` becomes the institutional reference: "here is how to ship a Higgsfield-driven (or Kling-driven) hero video in an Optimus client build."

### How to apply it

Create `knowledge/patterns/ai-hero-video-pipeline.md` with the following structure:

1. **Decision criteria** — when to use AI-video hero vs. 3-layer canvas hero. Brand-voice rubric, industry conventions, client preference defaults. Mirrors the criteria documented in animation-specialist (bridge application #1).

2. **Higgsfield-in-Claude pipeline (recommended default after drink-own-champagne validates).** Step-by-step:
   - MCP setup link to concept doc.
   - Prompt design for start frame: brand-aligned scene, lighting, composition, framing.
   - Prompt design for end frame: same scene + camera/composition shift.
   - Animate parameters: duration (10-15s), motion type (dolly-in, pan, crane), model selection (Kling 3.0 default for cost; Sora 2 / Veo 3.1 for premium quality on luxury builds).
   - Output handling: download MP4, compress to web target (HandBrake or equivalent — target <2MB), embed in hero with poster fallback.

3. **fal.ai + Kling pipeline (legacy reference).** Step-by-step from the Enchanted Madison workflow — kept as a fallback or alternative if Higgsfield is unavailable / unstable / over-budget for a specific build. Documents the manual cross-tool flow.

4. **Hero integration spec** — how the AI-video hero composes with the rest of the Optimus hero: H1 + subheadline + CTAs as Framer Motion stagger overlays on top of the video; performance budget; lazy-load + poster fallback; muted autoplay; motion-budget compliance per the Homepage Section Architecture Rule.

5. **Brand-voice prompt library** — accumulate Optimus-class brand-prompt patterns over multiple builds. Luxury hospitality template, technical SaaS template, hospitality-trades template, etc. Each new client build that uses the video hero contributes its prompt back to this library.

6. **Cross-references** — concept note, animation-specialist agent, CLAUDE.md Hero Architecture Rule extension, Homepage Section Architecture Rule motion budget.

This bridge is a change-request, not a change. Anthony reviews and creates the pattern doc when bridge application #1 (animation-specialist edit) is also being applied — the pattern doc and the agent edit ship in the same commit.

### Value vector reasoning

- `productivity`: institutional pattern doc means each future video-hero build inherits a documented workflow rather than rediscovering it. Estimate ~30-60 min saved per build that uses the pattern, compounding across the cadence of client engagements.
- `revenue`: documented workflow lets the animation-specialist agent (post bridge #1 edit) confidently route brands to the video-hero branch when fit is right. Better brand-fit heroes lift perceived premium positioning per the bridge #1 reasoning, supporting higher tier close rates.

### Status

`not-started`

### Updates

(none)
