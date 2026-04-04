---
name: Printful Color-Only Variant Names Misparsed as Size
type: error
description: 2-part Printful variant names like "Insulated tumbler / Black" assigned color to size field, causing color bubbles to render as size chips
---

# Error: Printful Color-Only Variant Names Misparsed as Size
**Project:** Andrea Abella Marie  
**Date:** Apr 2026  
**Phase:** Shop & Payments — variant picker

## Problem
Tumblers, mugs, and other color-only Printful products showed color options as text size chips ("S", "M", "L" style) instead of color swatches. The colors were not clickable as swatches and the color picker UI broke entirely for these products.

Printful variant names for apparel: `"Unisex Hoodie / S / Black"` → 3 parts → middle = size, last = color ✓  
Printful variant names for drinkware: `"Insulated tumbler / Black"` → 2 parts → last part assigned to `size` field ✗

Additionally, "Bottle Green" rendered as a gray fallback swatch because it wasn't in the COLOR_MAP, and Printful returned it with inconsistent casing ("Bottle green" vs "Bottle Green").

## Root Cause
The variant name parser assumed 2-part names were always `Product / Size`. For drinkware and color-only items, 2-part names are `Product / Color`. No color detection logic existed to differentiate.

## Solution
1. Built `KNOWN_COLORS` set with ~50 color names
2. For 2-part names: check if last segment is in KNOWN_COLORS → assign to color; otherwise assign to size
3. For 3-part names: guard against reversed order using same KNOWN_COLORS check
4. Added "Bottle Green" and other missing colors to COLOR_MAP
5. Made COLOR_MAP lookup case-insensitive via `normalizeKey()` helper

## Prevention
- Printful variant name format is not consistent across product categories — always build the parser with KNOWN_COLORS detection, not positional assumptions
- Test the variant picker with at least one apparel item AND one drinkware/accessory item before declaring shop complete
- COLOR_MAP lookup must always be case-insensitive — Printful casing varies by product

## Related
- Pattern: [[patterns/printful-variant-name-parser-known-colors]]
