# Pattern: fal.ai Image Generation
**Category:** AI Assets
**First used:** Enchanted Madison — March 2026

---

## Scope — Blog Post Card Images Only

fal.ai is used **exclusively for blog post card thumbnail images**. Do not use it for:
- Hero sections (always animated SVG)
- About page photos (real client photos or build without)
- Service card images (real client photos or build without)
- OG images (real client photos or build without)

## What
Generate brand-matched blog card thumbnails via the fal.ai Node.js SDK. One image per article.

## When to Use
- Blog articles need card thumbnails
- Client has no provided photography for blog cards
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
// scripts/generate-blog-images.ts
import * as fal from "@fal-ai/serverless-client";
import * as fs from "fs";
import * as path from "path";

fal.config({ credentials: process.env.FAL_KEY });

// One entry per blog article — filename matches the article slug
const images = [
  { prompt: "[brand mood from design-system.md] + [article topic]", filename: "blog-[slug].jpg" },
];

for (const img of images) {
  const result = await fal.run("fal-ai/flux-pro/v1.1", {
    input: { prompt: img.prompt, image_size: "landscape_16_9" }
  });
  // Save to /public/images/blog/
  // Commit immediately after script completes
}
```

**Output location:** `/public/images/blog/[article-slug].jpg`

## Key Rules
1. Commit all generated files in the same commit as the script run — never as a follow-up
2. Use design-system.md Section 6 as the prompt source — keep imagery on-brand
3. Name files to match article slugs: `blog-[slug].jpg`
4. One image per article — do not generate extras speculatively

## Reuse Condition
Every build — blog articles always need card thumbnails.

## Related
- [[errors/generated-assets-not-committed]]
- See website-build-template.md → AI Asset Generation
