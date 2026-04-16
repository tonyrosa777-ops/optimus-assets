# Pattern: Reusable fal.ai Blog Image Generator Script
**Category:** AI Assets / Automation
**First used:** Andrea Abella Marie — Apr 10–14, 2026 (proven across 3 blog images)

## What
A single parameterized node script that takes a slug + prompt file, calls fal.ai's `flux-pro/v1.1-ultra` queue endpoint, polls until complete, downloads the result to `public/images/blog/<slug>.png`. Prompts are archived as plain text in `scripts/prompts/<slug>.txt` so they live with the repo.

## When to Use
- Any post-launch content site where blog images are generated ongoing, not one-time
- Brand aesthetic that can be described in a tight paragraph (cinematic editorial, specific palette, consistent composition notes)
- Client doesn't have a photographer on retainer and doesn't need stock photography
- Image aspect ratio and style are consistent across posts (reusing the same generation settings is half the battle)

## How

### 1. Install + env
fal.ai API key in `.env.local` as `FAL_KEY=<key>`. Gitignored.

### 2. Script: `scripts/generate-blog-image.mjs`

```js
import { readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";

const ROOT = resolve(import.meta.dirname, "..");
const env = readFileSync(resolve(ROOT, ".env.local"), "utf8");
const FAL_KEY = env.match(/^FAL_KEY=(.+)$/m)[1].trim();

const args = process.argv.slice(2);
const slug = args[0];
const prompt = args[1] === "--prompt-file"
  ? readFileSync(resolve(ROOT, args[2]), "utf8").trim()
  : args.slice(1).join(" ");

const OUT = resolve(ROOT, `public/images/blog/${slug}.png`);

// Submit to queue endpoint
const submit = await fetch("https://queue.fal.run/fal-ai/flux-pro/v1.1-ultra", {
  method: "POST",
  headers: { Authorization: `Key ${FAL_KEY}`, "Content-Type": "application/json" },
  body: JSON.stringify({
    prompt,
    num_images: 1,
    enable_safety_checker: true,
    safety_tolerance: "2",
    output_format: "png",
    aspect_ratio: "16:9",
    raw: false,
  }),
}).then(r => r.json());

// Poll until COMPLETED, then fetch response, then download image URL to OUT
// (full script: see scripts/generate-blog-image.mjs in andrea-abella-marie repo)
```

### 3. Prompt archive: `scripts/prompts/<slug>.txt`
One paragraph, plain text. Consistent opener ("Cinematic editorial photograph, 16:9 aspect ratio.") then scene, palette, lighting, emotional tone, explicit no-text/no-logos caveat.

### 4. Usage
```bash
node scripts/generate-blog-image.mjs my-post-slug --prompt-file scripts/prompts/my-post-slug.txt
```

## Key Rules

- **Always use the queue endpoint** (`queue.fal.run`) not the sync endpoint. flux-pro/v1.1-ultra can take 10–30s; sync times out inconsistently.
- **Archive prompts in the repo**, not in the terminal history. Future regenerations (style refresh, aspect ratio change, client request for a different scene) depend on knowing what generated what.
- **Consistent prompt opener and closer across all posts** gives you visual coherence across the blog without needing a LoRA or a style guide. Lines that appear in every prompt for Andrea:
  - Opener: "Cinematic editorial photograph, 16:9 aspect ratio."
  - Closer: "Moody chiaroscuro lighting, soft film grain, 85mm lens, shallow depth of field, ultra-realistic, editorial magazine composition. No text, no logos, no recognizable real-world public figures."
  - Palette line: deep royal navy and midnight blue with warm amber and gold highlights (matches site brand)
- **One image at a time**, not `num_images: 4` with a "pick the best" step. The prompt engineering goes into the description, not a lottery. Cheaper too.
- **Filename matches slug exactly** — the publish script can find it without additional config.
- **Never request readable text in the image** (cross-reference [[fal-ai-avoid-text-in-prompts]]).

## Reuse Condition
- Any client with a blog that will keep publishing post-launch
- Any dark-brand cinematic-aesthetic build (the specific prompt scaffold transfers)
- For light-brand or different aesthetic, swap the opener/closer but keep the same script shape

## Related
- [[patterns/fal-ai-image-generation]] — base pattern
- [[errors/fal-ai-avoid-text-in-prompts]] — text rendering is unreliable, avoid
- [[patterns/sanity-blog-post-publish-script]] — companion script that picks up the generated image and publishes the post
