# Error: PhotoPlaceholder onError Fires on Production When Real Image Exists
**Project:** Gray Method Training
**Date:** Apr 2026
**Phase:** Hero image deployment

## Problem
Adam's professional headshot was correctly placed in `public/images/hero-adam.jpg`, committed, and deployed to Vercel. The hero section was wired through `PhotoPlaceholder` with an `onError` fallback. The image deployed successfully (confirmed by direct URL access), but on the live site the hero showed the placeholder UI — not the photo. The `onError` callback was firing even though the image was present.

## Root Cause
`PhotoPlaceholder` was designed for the case where a photo *might not exist yet* during development. It wraps `<img>` with an `onError` handler that swaps to a placeholder state. In production environments, timing differences in when the DOM mounts versus when the image fully loads can trigger `onError` in edge cases — particularly when the parent component re-renders or there are hydration timing issues between server-rendered HTML and the client-side React takeover.

The component was never intended to be the long-term solution for production photography; it was a development scaffold.

## Solution
Remove `PhotoPlaceholder` entirely from any slot where a real image is confirmed. Replace with direct `next/image`:

```tsx
// Remove:
import PhotoPlaceholder from "@/components/ui/PhotoPlaceholder";
<PhotoPlaceholder src="/images/hero-adam.jpg" ... />

// Replace with:
import Image from "next/image";
<Image
  src="/images/hero-adam.jpg"
  alt="Coach Adam Gray — Gray Method Training"
  width={2000}
  height={1429}
  sizes="(max-width: 1280px) 45vw, 560px"
  priority
  className="w-full h-auto object-cover object-top"
/>
```

## Prevention
- `PhotoPlaceholder` is a **development scaffold only** — it should never remain in production code when a real asset exists
- When a client delivers photography, replace `PhotoPlaceholder` with direct `next/image` immediately — do not leave the scaffold in place
- During the pre-launch QA checklist, verify every `PhotoPlaceholder` has been replaced with a confirmed asset
- If the placeholder is intentionally permanent (truly missing photo), use the placeholder's initials/icon fallback directly — not the `onError` wrapper

## Related
- [[errors/media-asset-wrong-location]] — related: assets must land in `/public/images/`
