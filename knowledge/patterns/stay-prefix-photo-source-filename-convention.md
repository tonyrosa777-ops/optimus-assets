# Pattern: Stay-prefix photo source-filename convention

**Category:** Workflow / Asset Management
**First used:** Enchanted Madison — 2026-05-13

## What
Every source photo file is named `[stay-slug]-[scene].ext` (or `[category]-[scene].ext` for non-stay photos), so every `integrate-photos.mjs` mapping is unambiguous and every photo's destination is self-evident from its filename.

## When to Use

Trigger conditions (any one):
- Project has 2+ accommodations / units / locations / service variants that each need their own photo gallery
- Client is emailing real photos in batches over time (not a single curated photoshoot dump)
- Photo destinations include carousels per offering (e.g., `/stays/[slug]`, `/locations/[city]`, `/services/[id]`)
- Existing source filenames mix arbitrary prefixes (Enchanted Madison: "EC," "Glamping," "Tent Site," "Enhanced") which create per-stay assignment ambiguity

Skip when:
- Single-unit business (no per-offering galleries)
- All photos arrive in one professional shoot batch with pre-organized folders

## How

**The convention:**

```
[stay-slug]-[scene-descriptor].[ext]
```

Examples (Enchanted Madison normalization plan):
- `cottage-hot-tub.jpg` (was: "EC Hot Tub.jpg")
- `cottage-bedroom.jpg` (was: "EC Bedroom Summer.jpg")
- `cottage-swing.png` (was: "EC Swing.png")
- `cottage-entrance.jpg` (was: "Entrance.jpg")
- `cottage-outdoor-movie.png` (was: "Outdoor Movie Bed with real bed.png")
- `velvet-buck-bedroom.png` (was: "Enhanced bedroom for glamping.png")
- `bell-tent-tent.png` (was: "Tent Site with tent.png")
- `bell-tent-bathroom.png` (was: "Glamping bathroom.png")
- `bell-tent-kitchen.png` (was: "Glamping kitchen.png")
- `byo-tent-marshmallows.png` (was: "Tent Site Roasting Marshmallows.png")

Non-stay categories follow the same shape (`[category]-[scene]`):
- `proposal-christmas.png` (was: "Christmas Proposal .png")
- `addon-outdoor-movie.png` (was: "Outdoor Movie Bed with real bed.png" — also gets a cottage- prefix for the cottage gallery copy)
- `experience-sunrise-hot-tub.png` (was: "Sunrise Hot Tub Escape.png")
- `madison-guide-broadway-fountain.jpg` (already correct via subfolder)

**Implementation:**

1. **Pre-launch rename pass** — schedule a 15-min call with the client to walk through every source photo together. Rename in-place in `source-photos/`. Confirm each assignment.

2. **integrate-photos.mjs becomes trivial** — the mapping table now reads as direct copies because filename = destination intent:
   ```js
   const JOBS = [
     ["cottage/cottage-hot-tub.jpg", "images/accommodations/cottage/hot-tub.webp"],
     ["cottage/cottage-bedroom.jpg", "images/accommodations/cottage/bedroom.webp"],
     ["bell-tent/bell-tent-bathroom.png", "images/accommodations/bell-tent/bathroom.webp"],
     // ...
   ];
   ```

3. **`source-photos/` subfolder per category** — `source-photos/cottage/`, `source-photos/bell-tent/`, etc. Subfolder + prefix double-encodes the assignment so even if a file gets renamed or moved, the destination is recoverable.

4. **Ledger ledger ledger** — keep `ANGELA-PHOTOS.md` (or `CLIENT-PHOTOS.md`) at project root tracking every source file → destination(s) → page(s) → photographer credit. Update on every new photo drop.

## Key Rules

1. **Stay-slug must match `siteData.stays[].slug` exactly.** No variants. If the slug is `bell-tent`, the prefix is `bell-tent-`, not `belltent-` or `bell_tent_`.

2. **Scene descriptor is kebab-case, no spaces.** `hot-tub`, not `hot tub` or `hotTub`. Avoids shell-quoting and URL-encoding pain.

3. **Trailing whitespace in filenames is forbidden.** Watch for "Christmas Proposal .png" (extra space before extension) and "Swing  at EC.png" (double space) — these silently break integrate scripts that match by exact filename. Rename to remove.

4. **Photographer credit lives in the metadata, not the filename.** If a client requires photo credit display on-page (Madison Guide style), store the credit in the ledger + render via a `siteData.photos[].credit` field. Don't embed in the filename.

5. **One source file per destination scene.** Don't ship duplicate files like `Entrance.jpg` and `Entrance.png` — pick one. Document the other as `Reference only` in the ledger.

## Reuse Condition

Mandatory on every Optimus build with 2+ accommodations / units / locations / variants. Apply during Phase 1 scaffold:
- Add a question to `intake-prompt.md` Section 5 (Forms / Assets): "Do your existing source photos use a stay-prefix convention? If not, we'll rename during integration."
- Scaffold `source-photos/<category>/` subfolder structure during Phase 0.
- Wire ledger creation into project-prime.md scaffold.

## Related

- Pattern #4 (build-log) — fal.ai image generation (sibling: pattern for AI-generated photos; this is the source-photo organization pattern)
- Pattern #72 — fal.ai parallel-property visual differentiation (companion: filename convention applies to fal.ai outputs too)
- Error #62 — Sharp webp conversion drops EXIF orientation (also addresses photo integration script reliability; this pattern + .rotate() fix are the two pillars of a robust integrate-photos.mjs)

## Anti-pattern (what to avoid)

Don't try to parse client-emailed filenames at integration time. The integrate script will get tangled in conditional logic ("if the filename contains 'glamping', is it for Bell Tent or Velvet Buck?") that's error-prone and requires re-decision on every new file. Move the per-stay decision to the rename pass (one-time human judgment), then let the script be a dumb copy.
