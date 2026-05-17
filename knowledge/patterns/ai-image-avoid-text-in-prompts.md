# Pattern: Avoid text rendering in AI image prompts
**Category:** AI Assets
**First used:** Witt's Restoration LLC — 2026-04-12 (originally as fal.ai-specific pattern; generalized 2026-05-17 — same rule applies across Higgsfield Flux 2, Nano Banana Pro, Soul, Cinema Studio, and every other diffusion model)

## What
AI image generation models cannot reliably render readable text. Prompts requesting text on signs, stamps, stickers, or labels produce garbled characters. This is a fundamental limitation of diffusion architectures, not a per-tool issue.

## When to Use
Every AI image generation prompt — Higgsfield Flux 2, Nano Banana Pro, Soul, Cinema Studio Video, Marketing Studio, GPT Image — anywhere a scene might include signage, packaging, or any readable text element.

## How
- Never request readable text in prompts (no "REJECTED stamp," no "sign that says X," no "label reading Y")
- If the scene concept requires text (e.g., inspection sticker), describe the SCENE without the text: "a mechanic inspecting rust damage with a clipboard" instead of "a rejection sticker with REJECTED text"
- For text-heavy needs (signage mockups, packaging, social tiles with logo + headline), use Nano Banana Pro (best text-rendering model on the matrix) and accept that you'll regenerate 2-4 times to land legible text — even then, treat baked-in text as suspect.
- Always review generated images visually before committing — garbled text is the #1 artifact.
- For text that MUST be exactly correct (brand wordmark, headline copy), composite it in post (Figma / Photoshop / SVG overlay in the React component) rather than asking the model to render it.

## Key Rules
- "REJUPED" instead of "REJECTED" is a real example of what happens.
- Regenerating the same prompt produces different garbled text, not correct text.
- The fix is always to rewrite the prompt to avoid text entirely OR composite the text in post.
- Nano Banana Pro is the strongest text-rendering model (documented per `higgsfield-model-selection-matrix.md`) — but "strongest" still means "wrong ~30-50% of the time" for non-trivial strings.

## Reuse Condition
Every project that uses AI for image generation (all Optimus builds). Applies to images AND to the still frames inside generated videos (Cinema Studio Video, Marketing Studio Video, Kling, Sora, Veo).

## Related
- [[higgsfield-blog-image-generation]] — base pattern for blog card / header / gallery generation
- [[higgsfield-model-selection-matrix]] — Use Case E (editorial cinematic stills with text rendering)
- [[ai-video-slop-avoidance-checklist]] — "readable text artifact scan" is one of the 5 post-generation review points
