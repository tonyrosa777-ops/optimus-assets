# Error: Media Asset Placed in Repo Root
**Project:** Enchanted Madison
**Date:** March 2026
**Phase:** Phase 2 (Hero video)

---

## Problem
`hero-forest.mp4` was downloaded and placed in the repository root (`C:\Projects\Enchanted Madison\hero-forest.mp4`) instead of `/public/videos/`. It was never flagged before committing.

## Root Cause
No asset placement rules existed. The video was downloaded manually and dropped wherever felt convenient. Claude didn't flag the incorrect location.

## Solution
All project media must live inside `/public/` organized by type:
- Videos → `/public/videos/`
- Images → `/public/images/`
- Client photos → `/public/photos/`
- Brand assets → `/public/brand/`
- OG images → `/public/og/`

## Prevention
Asset Placement Rules table added to `website-build-template.md`.
Claude must flag any media file not in /public before committing.

## Related
- [[patterns/kling-video-hero]]
- See website-build-template.md → Asset Placement Rules
