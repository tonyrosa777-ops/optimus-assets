# Pattern: fal.ai Image Generation
**Category:** AI Assets
**First used:** Enchanted Madison — March 2026

---

## What
Generate custom, brand-matched images via the fal.ai Node.js SDK running in the terminal. Eliminates the need for professional photography before launch.

## When to Use
- Client has no professional photography
- Sections need custom imagery that stock photos won't fit
- Brand requires a specific mood/style that needs to be consistent across the site
- Fast turnaround needed before launch

## How

**Setup:**
```bash
npm install @fal-ai/serverless-client
# Add to .env.local:
FAL_KEY=your_fal_api_key
```

**Prompt source:** Pull directly from `design-system.md` Section 6 (Photography & Media Direction):
- Shot types required
- Mood and processing style
- Prohibited content
- Aspect ratios

**Script pattern:**
```ts
// scripts/generate-images.ts
import * as fal from "@fal-ai/serverless-client";
import * as fs from "fs";
import * as path from "path";

fal.config({ credentials: process.env.FAL_KEY });

const images = [
  { prompt: "[brand mood from design-system.md] + [specific scene]", filename: "hero-main.jpg" },
  { prompt: "[brand mood] + [section descriptor]", filename: "section-stays.jpg" },
];

for (const img of images) {
  const result = await fal.run("fal-ai/flux/schnell", {
    input: { prompt: img.prompt, image_size: "landscape_16_9" }
  });
  // Save to /public/images/
  // Commit immediately after script completes
}
```

**Output location:** `/public/images/[section]-[descriptor].jpg`

## Key Rules
1. Commit all generated files in the same commit as the script run — never as a follow-up
2. Use design-system.md Section 6 as the prompt source — keep imagery on-brand
3. Name files descriptively: `[section]-[descriptor].jpg` not `image-1.jpg`
4. Generate hero image first — validate brand feel before generating the rest

## Reuse Condition
Every build where client photography is absent or insufficient for a premium feel.

## Related
- [[errors/generated-assets-not-committed]]
- See website-build-template.md → AI Asset Generation
