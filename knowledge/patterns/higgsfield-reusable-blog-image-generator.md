# Pattern: Reusable Higgsfield Blog Image Generator
**Category:** AI Assets / Automation
**First used:** Andrea Abella Marie — Apr 10–14, 2026 (originally fal.ai script; ported to Higgsfield MCP 2026-05-17 after fal.ai retirement)

## What
A single reusable pattern for generating blog post images via the Higgsfield MCP. Takes a slug + prompt file, calls `mcp__higgsfield__generate_image` with `model: flux_2` (unlimited on Plus tier), saves the result to `public/images/blog/<slug>.png`. Prompts are archived as plain text in `scripts/prompts/<slug>.txt` so they live with the repo and survive style refreshes.

## When to Use
- Any post-launch content site where blog images are generated ongoing, not one-time
- Brand aesthetic that can be described in a tight paragraph (cinematic editorial, specific palette, consistent composition notes)
- Client doesn't have a photographer on retainer and doesn't need stock photography
- Image aspect ratio and style are consistent across posts (reusing the same generation settings is half the battle)

## How

### 1. No setup needed
Higgsfield MCP is account-scoped via the global `mcp__higgsfield__*` tools. No per-project key, no `.env.local` entry. Plus tier ships Flux 2 unlimited image generation.

### 2. Generation pattern (orchestrator-driven)

```
const slug = "my-post-slug";
const prompt = readFileSync(`scripts/prompts/${slug}.txt`, "utf8").trim();

const image = await mcp__higgsfield__generate_image({
  model: "flux_2",                  // unlimited on Plus tier — 0 cr
  prompt: prompt,
  aspect_ratio: "16:9",             // or "1:1" for cards
});

const outPath = `public/images/blog/${slug}.png`;
await saveTo(outPath, image);
// Commit with the post that uses it (per CLAUDE.md Generated Assets Rule)
```

For published Node-script automation in client repos (post-launch content workflow), wrap the MCP call in a thin Node wrapper that the Sanity publish script can invoke (per `sanity-blog-post-publish-script.md`).

### 3. Prompt archive: `scripts/prompts/<slug>.txt`
One paragraph, plain text. Consistent opener ("Cinematic editorial photograph, 16:9 aspect ratio.") then scene, palette, lighting, emotional tone, explicit no-text / no-logos caveat.

### 4. For text-rendering needs
Swap `model: "flux_2"` for `model: "nano_banana_pro"` — also unlimited on Plus, best text rendering. Still review every result; even Nano Banana garbles non-trivial text strings ~30-50% of the time (per `ai-image-avoid-text-in-prompts.md`).

## Key Rules

- **No FAL_KEY, no fal.ai script.** fal.ai retired 2026-05-17 once Plus tier shipped 6 permanent unlimited image models.
- **MCP calls are synchronous via `mcp__higgsfield__generate_image`** — no queue polling needed for image generation (only video calls go through `job_status` polling).
- **Archive prompts in the repo**, not in the terminal history. Future regenerations (style refresh, aspect ratio change, client request for a different scene) depend on knowing what generated what.
- **Consistent prompt opener and closer across all posts** gives you visual coherence across the blog without needing a LoRA or a style guide. Lines that appear in every prompt for Andrea:
  - Opener: "Cinematic editorial photograph, 16:9 aspect ratio."
  - Closer: "Moody chiaroscuro lighting, soft film grain, 85mm lens, shallow depth of field, ultra-realistic, editorial magazine composition. No text, no logos, no recognizable real-world public figures."
  - Palette line: deep royal navy and midnight blue with warm amber and gold highlights (matches site brand)
- **One image at a time**, not a batch with "pick the best" step. The prompt engineering goes into the description, not a lottery. Free is still wall time.
- **Filename matches slug exactly** — the publish script can find it without additional config.
- **Never request readable text in the image** (cross-reference [[ai-image-avoid-text-in-prompts]]).

## Reuse Condition
- Any client with a blog that will keep publishing post-launch
- Any dark-brand cinematic-aesthetic build (the specific prompt scaffold transfers)
- For light-brand or different aesthetic, swap the opener/closer but keep the same pattern shape

## Related
- [[higgsfield-blog-image-generation]] — base pattern (formerly fal-ai-image-generation.md)
- [[ai-image-avoid-text-in-prompts]] — text rendering is unreliable, avoid
- [[sanity-blog-post-publish-script]] — companion script that picks up the generated image and publishes the post
- [[higgsfield-model-selection-matrix]] — Use Case D for full image-model decision tree
- [[higgsfield-cost-approval-gate]] (Pattern #85) — image generation skip conditions (unlimited models bypass gate Steps 1+2)
