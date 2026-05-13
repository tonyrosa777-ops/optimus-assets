# Pattern: fal.ai parallel-property visual differentiation

**Category:** AI Assets / Visual Design
**First used:** Enchanted Madison — 2026-05-13

## What
When a project has 2+ similar offerings (multiple glamping tents, two coworking floors, three studio rooms, parallel service tiers, etc.), generate distinct fal.ai prompt aesthetics for each so they read as separate brand identities — never as reskins of one master template.

## When to Use

Trigger conditions (any one):
- The project has 2+ properties / units / rooms / tiers that share a category descriptor (e.g., "Luxury Glamping Tent x2," "Studio Apartment x3")
- Real photos exist for one offering but not the other(s), so fal.ai placeholders must hold the gap
- The same fal.ai prompt template would produce visually-identical outputs across multiple sets (defeats brand purpose)
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

```ts
// scripts/generate-property-images.ts
const STYLE = "Photorealistic luxury glamping, romantic atmosphere, Indiana woodland, cinematic composition, National Geographic quality, 16:9";

const JOBS: Job[] = [
  // Property A — warm twilight palette
  {
    outputPath: "images/accommodations/velvet-buck.webp",
    prompt: `${STYLE}, luxury bell-style glamping tent with rich velvet-toned interior visible through open canvas door, secluded woodland clearing at golden twilight, warm amber lantern light, deep green forest backdrop, intimate and inviting, lush bedding, no people`,
  },
  // Property B — deep-night Milky Way palette
  {
    outputPath: "images/accommodations/starlit-buck.webp",
    prompt: `${STYLE}, luxury glamping tent under a sky full of stars and the Milky Way, deep indigo night, warm lantern light glowing from inside, woodland clearing, hot tub steaming, fairy lights, magical atmosphere, no people`,
  },
];
```

**Step 3: Generate the same scene types for each offering** so users can compare apples to apples across properties (exterior, bedroom, hot tub, fire pit, etc.). Total = `properties × scenes`. Enchanted Madison: 2 × 6 = 12 images.

**Step 4: Cost-aware planning.** flux/dev is ~$0.025/image at fal.ai. 12 images = ~$0.30. Budget per property pair: ~$0.30. Approve the cost up-front (or just absorb if under $1) — don't ask for permission on every image.

**Step 5: Hand off to the integrate-photos.mjs script** so any real photos that arrive later overwrite the fal.ai placeholders 1:1 by filename. No code change needed when a property gets real photography.

## Key Rules

1. **Same scene types, different palettes.** If Property A has bedroom + hot tub + firepit shots, Property B needs the same set. Otherwise the gallery counts diverge and one property feels under-photographed.

2. **Style prefix is identical.** "Photorealistic luxury glamping..." stays the same across every property in this build. Photographic register is the brand; only the mood/palette varies per property.

3. **"no people" in every prompt.** AI-generated people in marketing photos read as uncanny on every model as of 2026. Default to environment + product shots; the visitor mentally inserts themselves.

4. **Run non-interactively.** Don't ship the script with a confirmation prompt — that breaks background execution. Use a separate non-interactive runner (`scripts/generate-[scene]-images.ts`) that just executes when invoked.

5. **Distinct aesthetics must be obviously distinct.** A 30% palette shift between two properties looks like inconsistent grading, not intentional. Pick palettes that are 80%+ different on the mood axis: twilight-amber vs deep-night-blue, not amber vs gold.

## Reuse Condition

Applies to every Optimus build with 2+ comparable offerings that share a category but need visual differentiation. Common project types:

- **Hospitality multi-unit** — multiple cabins, glamping tents, treehouses, studios at one property
- **Restaurant chain** — distinct visual identity per location while maintaining brand register
- **Coworking** — different floors / room types / membership tiers
- **Service business multi-package** — service tiers with distinct "vibes" (basic / premium / luxury)
- **Real estate listings** — multiple comparable units at the same development

## Related

- Pattern #4 (build-log Pattern table) — fal.ai image generation from design-system.md prompts (the foundational pattern; this is the per-offering specialization of that)
- Pattern #41 — fal.ai reusable blog image generator (sibling pattern for blog-specific generation)
- Pattern #73 — Stay-prefix photo source-filename convention (companion: how to organize the output paths so they integrate cleanly into stay galleries)
