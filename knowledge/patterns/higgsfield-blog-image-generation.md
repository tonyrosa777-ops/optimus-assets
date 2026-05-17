# Pattern: Higgsfield Blog Image Generation
**Category:** AI Assets
**First used:** Enchanted Madison — March 2026 (originally as fal.ai pattern; renamed + rewritten 2026-05-17 after fal.ai retirement)

---

## Scope

Higgsfield Flux 2 (and Nano Banana Pro for text-rendering stills) is used for:
- Blog post card thumbnails (1:1 or 4:3)
- Blog article header images (16:9)
- Trade business gallery images (4:5 or 3:2)
- Service-card stand-in stills when real client photos are unavailable
- About-page placeholder stills when no real founder photo provided

Do NOT use it for:
- Hero sections — Architecture A canvas hero (animation-specialist) OR Architecture B movie-hero video (Higgsfield Cinema Studio Video V2 per `optimus-higgsfield-hero-video` skill)
- Replacing real client photos that exist — always prefer real photography when provided

## What
Generate brand-matched blog card thumbnails + article headers + gallery images via `mcp__higgsfield__generate_image`. One card + one header per blog article. 12-16 images per trade gallery.

## When to Use
- Blog articles need card thumbnails + header images (every Optimus build)
- Trade business gallery needs job-site images (contractors, painters, fencers, electricians, landscapers, cleaners, builders)
- Client has no provided photography
- Fast turnaround needed before launch

## How

**Setup:** No per-project setup needed. Higgsfield MCP is account-scoped via the global `mcp__higgsfield__*` tools. Plus tier ships 6 permanent unlimited image models (Flux 2, Nano Banana, GPT Image, Seedream 4.5, Seedream V5 Lite, Kling O1 Image) at 0 cr each. No `FAL_KEY` or any equivalent env var.

**Prompt source:** Pull directly from `design-system.md` Section 6 (Photography & Media Direction):
- Shot types required
- Mood and processing style
- Prohibited content
- Aspect ratios

**Generation pattern (orchestrator-driven, no standalone script needed):**

```
For each blog article in /data/site.ts:
  card_prompt   = build_prompt_from_design_system_section_6(article, aspect="card")
  header_prompt = build_prompt_from_design_system_section_6(article, aspect="header")

  card_image = mcp__higgsfield__generate_image({
    model: "flux_2",              // unlimited on Plus tier — default workhorse
    prompt: card_prompt,
    aspect_ratio: "1:1",          // or "4:3" depending on layout
  })

  header_image = mcp__higgsfield__generate_image({
    model: "flux_2",
    prompt: header_prompt,
    aspect_ratio: "16:9",
  })

  visual_review(card_image, header_image)  // free retake on unlimited model
  save_to(f"/public/images/blog/{article.slug}-card.jpg", card_image)
  save_to(f"/public/images/blog/{article.slug}-header.jpg", header_image)
```

For trade galleries:
```
For each of 12-16 distinct prompts:
  image = mcp__higgsfield__generate_image({
    model: "flux_2",
    prompt: gallery_prompt,
    aspect_ratio: "4:5",  // or 3:2 depending on gallery layout
  })
```

For stills with text rendering (signage mockups, packaging, social tiles with logo + headline):
```
image = mcp__higgsfield__generate_image({
  model: "nano_banana_pro",  // also unlimited on Plus, best text rendering
  prompt: prompt,
  aspect_ratio: "16:9",
})
```

**Output location:** `/public/images/blog/[article-slug]-card.jpg` and `[article-slug]-header.jpg`. For gallery: `/public/images/gallery/[scene-slug].jpg`.

## Cost-approval gate handling

Image generation with the 6 permanent unlimited models bypasses gate Steps 1+2 entirely (per `higgsfield-cost-approval-gate.md` skip conditions). Step 0 (active-skill confirmation) still runs — confirm the orchestrator has read this pattern doc + `higgsfield-model-selection-matrix.md` Use Case D at session start.

No balance check needed for the image batch itself (unlimited models don't draw from the 1000 cr/mo pool). The orchestrator does still run an upfront balance check in Stage 1G for any video work that might happen in the same stage (e.g., Architecture B hero generation).

No SIMULATION step needed for image generation — retakes are zero-cost on unlimited models. If an image fails visual review (slop, garbled text, wrong composition), regenerate immediately.

## Key Rules
1. Commit all generated files in the same commit as the generation run — never as a follow-up (per CLAUDE.md Generated Assets Rule).
2. Use `design-system.md` Section 6 as the prompt source — keep imagery on-brand.
3. Name files to match article slugs: `[slug]-card.jpg` + `[slug]-header.jpg`.
4. One card + one header per article — do not generate extras speculatively (free is still wall time).
5. Never request readable text in image prompts (see `ai-image-avoid-text-in-prompts.md`).
6. Default model is `flux_2`. Use `nano_banana_pro` only when text rendering is the primary requirement.
7. Visual-review every image before commit. Free retake on unlimited models — never commit slop.

## Reuse Condition
Every build — blog articles always need card + header thumbnails; trade businesses always need a gallery.

## Related
- [[errors/generated-assets-not-committed]]
- [[ai-image-avoid-text-in-prompts]] — text rendering is unreliable, avoid in prompts
- [[higgsfield-reusable-blog-image-generator]] — automated post-launch publishing pattern (sibling)
- [[higgsfield-model-selection-matrix]] — Use Case D for full image-model decision tree
- [[higgsfield-cost-approval-gate]] (Pattern #85) — image generation skip conditions documented here
- [[parallel-property-visual-differentiation]] — when client has 2+ comparable offerings needing distinct visual identities
- See website-build-template.md → AI Asset Generation
