# Pattern: Avoid text rendering in fal.ai image prompts
**Category:** AI Assets
**First used:** Witt's Restoration LLC — 2026-04-12

## What
AI image generation models (FLUX Schnell, FLUX Pro) cannot reliably render readable text. Prompts requesting text on signs, stamps, stickers, or labels produce garbled characters.

## When to Use
Every fal.ai image generation prompt — especially for blog cards, headers, gallery images, and any scene that might include signage.

## How
- Never request readable text in prompts (no "REJECTED stamp," no "sign that says X," no "label reading Y")
- If the scene concept requires text (e.g., inspection sticker), describe the SCENE without the text: "a mechanic inspecting rust damage with a clipboard" instead of "a rejection sticker with REJECTED text"
- Use FLUX Pro v1.1 for higher quality when regenerating failed images
- Always review generated images visually before committing — garbled text is the #1 artifact

## Key Rules
- "REJUPED" instead of "REJECTED" is a real example of what happens
- Regenerating the same prompt produces different garbled text, not correct text
- The fix is always to rewrite the prompt to avoid text entirely

## Reuse Condition
Every project that uses fal.ai for image generation (all Optimus builds)

## Related
- Pattern #4: fal.ai image generation from design-system.md prompts
