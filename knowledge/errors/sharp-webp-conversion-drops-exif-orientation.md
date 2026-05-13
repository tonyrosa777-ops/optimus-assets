# Error: Sharp webp conversion silently drops EXIF Orientation tag — phone photos render sideways

**Project:** Enchanted Madison
**Date:** 2026-05-13
**Phase:** Client revisions pass (Stage 1I verification)

## Problem
Cottage gallery bedroom photo rendered rotated 90° in production. Ceiling fan on the left, bed on the bottom, comforter looking like it was about to slide off the side of the screen. The source JPG (`source-photos/EC Bedroom Summer.jpg`) opened correctly in every desktop image viewer — bug only appeared after sharp conversion to webp and rendering via `next/image`.

Caught by user during live Playwright pass:
> *"This picture, under the enchanted cottage page itself, needs to be fixed sideways."*

## Root Cause
iPhone and Android cameras frequently store sensor data with a fixed sensor orientation (typically landscape) regardless of how the user held the phone. The "correct" orientation is communicated via an EXIF **Orientation tag** (values 1-8, where 1 = no rotation, 6 = rotate 90° CW, 3 = 180°, 8 = 270° CW, plus 2/4/5/7 for mirroring variants).

Image viewers (Preview, Photos, browser native `<img>`, Lightroom, etc.) honor the EXIF Orientation tag and rotate on the fly. **Sharp's `.webp()` writer drops EXIF metadata by default for output size optimization AND does not auto-apply the rotation tag before writing.** So the rotation instruction is silently lost during conversion, and the raw landscape sensor data is encoded as if it were correctly-oriented landscape.

Result: a portrait photo is rendered rotated 90° in production, with no warning from the script, no console error, and a source JPG that looks fine in every viewer.

## Solution
Add `.rotate()` (no arguments) to the sharp pipeline BEFORE the resize/encode step:

```js
// Before — EXIF rotation silently lost
await sharp(src)
  .resize({ width: MAX_WIDTH, withoutEnlargement: true })
  .webp({ quality: QUALITY })
  .toFile(dest);

// After — EXIF rotation applied, then stripped
await sharp(src)
  .rotate()  // reads EXIF Orientation, applies rotation, strips tag
  .resize({ width: MAX_WIDTH, withoutEnlargement: true })
  .webp({ quality: QUALITY })
  .toFile(dest);
```

`.rotate()` with no angle argument reads the EXIF Orientation tag, applies the rotation, then strips the tag — viewers see correct orientation even after EXIF is dropped. Idempotent: photos with Orientation 1 (already correct) are unchanged.

Re-ran the script on all 26 source photos after the fix. Verified post-fix:
- `bedroom.webp`: 1600×2133 (portrait) — was previously rendering sideways
- `cocktail-bar.webp`, `entrance.webp`, `romance-package.webp`: also corrected to portrait
- Landscape photos (Orientation = 1) unchanged

## Prevention

This is a **class-of-bug** that recurs on every Optimus build that converts client phone photos via sharp. Three preventive measures:

1. **Project scaffold rule** (add to `project-prime.md` Phase 1): every `scripts/integrate-*-photos.mjs` style conversion utility MUST include `.rotate()` in the sharp pipeline as the FIRST operation before resize/encode. Make it part of the canonical script template.

2. **Code-review check**: grep new conversion scripts for `sharp(` calls; flag any that don't include `.rotate()` before the encoder step. Add to pre-launch-auditor checklist.

3. **Mental model**: phone photos always have EXIF; default sharp pipeline always loses EXIF; rotation must be applied OR preserved. Picking "applied via `.rotate()` then strip EXIF" is the only correct choice when targeting next/image (which serves the optimized webp with no metadata anyway).

4. **Audit trigger**: any time a Stage 1I Playwright pass renders a portrait image at landscape aspect ratio (or vice versa), suspect EXIF Orientation. The bug is otherwise invisible — typecheck passes, build passes, no console warning.

## Related
- Pattern: `integrate-*-photos.mjs` canonical script template (add `.rotate()` as required step)
- Error #38 (Witt's Restoration): fal.ai never request readable text — different bug, same family of "image conversion silently produces wrong output"
- Error #34 (Gray Method Training): `PhotoPlaceholder` `onError` fires on production — different bug, related class of "image renders wrong in production but fine in dev"
