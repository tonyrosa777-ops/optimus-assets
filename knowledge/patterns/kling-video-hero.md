# Pattern: Kling AI Video Hero
**Category:** AI Assets
**First used:** Enchanted Madison — March 2026

---

## What
Generate a cinematic hero background video loop using Kling (kling.ai web app). Gives premium/luxury brands an immersive first impression without stock footage or a video shoot.

## When to Use
- Premium or luxury brand where static hero feels flat
- Client has no existing hero video
- Brand mood in design-system.md calls for atmospheric, environmental visuals
- Budget doesn't allow professional videography

## How (Manual Process — not automatable via API)

1. **Write the scene prompt** from design-system.md:
   - Brand identity statement (Section 1)
   - Photography & Media Direction (Section 6): mood, setting, prohibited content
   - Example prompt: *"Slow aerial drift over misty forest glamping tents at golden hour, warm candlelight glowing through tent fabric, romantic and intimate atmosphere, cinematic quality, no people"*

2. **Generate in Kling** (kling.ai):
   - Mode: Standard or Pro depending on quality needed
   - Duration: 5–10 seconds (loops seamlessly)
   - Download as MP4

3. **Place the file:** `/public/videos/hero-[descriptor].mp4`

4. **Implement in hero component:**
```tsx
<video
  autoPlay
  muted
  loop
  playsInline
  poster="/images/hero-fallback.jpg"  // REQUIRED — static fallback
  className="absolute inset-0 w-full h-full object-cover"
>
  <source src="/public/videos/hero-forest.mp4" type="video/mp4" />
</video>
```

5. **Commit** the .mp4 to `/public/videos/` immediately

## Key Rules
- Always include `poster` attribute with a static fallback image (for reduced-motion, slow connections, iOS background tab)
- Always use `autoPlay muted loop playsInline` — missing any of these breaks behavior on mobile
- Flag Kling as a **Phase 0 deliverable** in progress.md: "Hero video needed — generate in Kling before Phase 2 starts"
- File must go to `/public/videos/` — never the repo root

## Reuse Condition
Any premium/luxury brand where the hero section is the primary first impression and a static image feels insufficient.

## Related
- [[errors/media-asset-wrong-location]]
- See website-build-template.md → AI Asset Generation
