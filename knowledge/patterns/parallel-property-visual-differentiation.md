# Pattern: Parallel-property visual differentiation

**Category:** AI Assets / Visual Design
**First used:** Enchanted Madison — 2026-05-13 (originally fal.ai-specific; generalized to Higgsfield 2026-05-17 after fal.ai retirement)

## What
When a project has 2+ similar offerings (multiple glamping tents, two coworking floors, three studio rooms, parallel service tiers, etc.), generate distinct AI image prompt aesthetics for each so they read as separate brand identities — never as reskins of one master template.

## When to Use

Trigger conditions (any one):
- The project has 2+ properties / units / rooms / tiers that share a category descriptor (e.g., "Luxury Glamping Tent x2," "Studio Apartment x3")
- Real photos exist for one offering but not the other(s), so AI-generated placeholders must hold the gap
- The same Flux 2 / Nano Banana prompt template would produce visually-identical outputs across multiple sets (defeats brand purpose)
- Client has explicitly distinguished the offerings in naming/copy (e.g., "Velvet Buck" vs "Starlit Buck") and expects visual distinction to match

Skip when:
- Only one offering of its kind exists (no risk of reskin)
- Real photos exist for every offering already
- Offerings are intentionally identical (e.g., a hotel chain's standard king rooms — sameness is the brand)

## How

**Step 1: Read the naming + copy for each offering.** The names and descriptions carry the aesthetic palette. Examples from Enchanted Madison:
- "Velvet Buck" → velvet, warm tones, twilight, rich interiors
- "Starlit Buck" → stars, Milky Way, deep blue night, lantern light

**Step 2: Codify a shared style prefix + per-offering style suffix.** Keep the photographic register identical (style prefix) so the offerings feel like the same brand; vary only the mood/palette (style suffix) so they read as distinct.

**Step 3: Generate via `mcp__higgsfield__generate_image` with `model: flux_2`** (unlimited on Plus tier — 0 cr per image). Pseudo-flow:

```
const STYLE = "Photorealistic luxury glamping, romantic atmosphere, Indiana woodland, cinematic composition, National Geographic quality";

const JOBS = [
  // Property A — warm twilight palette
  {
    outputPath: "/public/images/accommodations/velvet-buck.webp",
    prompt: `${STYLE}. Luxury bell-style glamping tent with rich velvet-toned interior visible through open canvas door, secluded woodland clearing at golden twilight, warm amber lantern light, deep green forest backdrop, intimate and inviting, lush bedding, no people, no readable text`,
  },
  // Property B — deep-night Milky Way palette
  {
    outputPath: "/public/images/accommodations/starlit-buck.webp",
    prompt: `${STYLE}. Luxury glamping tent under a sky full of stars and the Milky Way, deep indigo night, warm lantern light glowing from inside, woodland clearing, hot tub steaming, fairy lights, magical atmosphere, no people, no readable text`,
  },
];

for (const job of JOBS) {
  const image = await mcp__higgsfield__generate_image({
    model: "flux_2",
    prompt: job.prompt,
    aspect_ratio: "16:9",
  });
  await saveTo(job.outputPath, image);
}
```

**Step 4: Generate the same scene types for each offering** so users can compare apples to apples across properties (exterior, bedroom, hot tub, fire pit, etc.). Total = `properties × scenes`. Enchanted Madison: 2 × 6 = 12 images.

**Step 5: Cost-aware planning.** Flux 2 is 0 cr per image (unlimited on Plus tier). The full 12-image batch is $0 marginal — no per-image cost budget needed. Compare to the previous fal.ai approach (~$0.30 per 12-image batch at $0.025/img). Plus tier unlimited makes scene-coverage decisions purely about wall time and prompt-writing effort, not budget.

**Step 6: Hand off to the integrate-photos.mjs script** so any real photos that arrive later overwrite the AI-generated placeholders 1:1 by filename. No code change needed when a property gets real photography.

## Key Rules

1. **Same scene types, different palettes.** If Property A has bedroom + hot tub + firepit shots, Property B needs the same set. Otherwise the gallery counts diverge and one property feels under-photographed.

2. **Style prefix is identical.** "Photorealistic luxury glamping..." stays the same across every property in this build. Photographic register is the brand; only the mood/palette varies per property.

3. **"no people, no readable text" in every prompt.** AI-generated people in marketing photos read as uncanny on every model as of 2026. Readable text artifacts garble (per `ai-image-avoid-text-in-prompts.md`). Default to environment + product shots; the visitor mentally inserts themselves.

4. **Distinct aesthetics must be obviously distinct.** A 30% palette shift between two properties looks like inconsistent grading, not intentional. Pick palettes that are 80%+ different on the mood axis: twilight-amber vs deep-night-blue, not amber vs gold.

5. **Free retake on unlimited models.** If any image fails the parallel-distinctness test on visual review, regenerate immediately — no cost, no confirmation needed (per `higgsfield-cost-approval-gate.md` skip conditions for unlimited image models).

## Reuse Condition

Applies to every Optimus build with 2+ comparable offerings that share a category but need visual differentiation. Common project types:

- **Hospitality multi-unit** — multiple cabins, glamping tents, treehouses, studios at one property
- **Restaurant chain** — distinct visual identity per location while maintaining brand register
- **Coworking** — different floors / room types / membership tiers
- **Service business multi-package** — service tiers with distinct "vibes" (basic / premium / luxury)
- **Real estate listings** — multiple comparable units at the same development

## Related

- [[higgsfield-blog-image-generation]] — base pattern for image generation (this is the per-offering specialization of that)
- [[higgsfield-reusable-blog-image-generator]] — sibling pattern for blog-specific generation
- [[stay-prefix-photo-source-filename-convention]] — how to organize the output paths so they integrate cleanly into stay galleries
- [[ai-image-avoid-text-in-prompts]] — universal text-rendering caveat
- [[higgsfield-model-selection-matrix]] — Use Case D for image model decisions
