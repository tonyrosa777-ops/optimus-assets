---
name: Printful Variant Name Parser with KNOWN_COLORS
type: pattern
description: Parse Printful variant names correctly across apparel (3-part) and drinkware/accessories (2-part) using a KNOWN_COLORS set for detection
---

# Pattern: Printful Variant Name Parser with KNOWN_COLORS
**Category:** E-commerce / Printful  
**First used:** Andrea Abella Marie — Apr 2026

## What
A variant name parser that correctly separates `size` and `color` from Printful's inconsistent naming formats using a known-colors set rather than positional assumptions.

## When to Use
Any time Printful sync product variants are fetched and displayed in a UI with separate size chips and color swatches. Always use this — never assume positional parsing.

## How

```ts
const KNOWN_COLORS = new Set([
  "Black", "White", "Navy", "Navy Blue", "Red", "Forest Green", "Military Green", "Bottle Green",
  "Storm", "Sport Grey", "Dark Heather", "Heather", "Maroon", "Ash", "Sand",
  "Royal", "Royal Blue", "Purple", "Orange", "Gold", "Yellow", "Pink", "Light Pink",
  "Charcoal", "Light Blue", "Vintage White", "Carolina Blue", "Heather Blue", "Olive",
  "Brown", "Chocolate", "Burgundy", "Mustard", "Cream", "Cranberry", "Dark Navy",
  "Slate", "Mint", "Coral", "Teal", "Indigo", "Green", "Blue", "Grey", "Gray",
  "Silver", "Rose Gold", "Rose", "Lavender", "Sky Blue", "Cobalt", "Aqua",
]);

function parseVariantName(name: string): { size: string; color: string } {
  const parts = name.split(" / ").map((p) => p.trim());

  if (parts.length === 1) return { size: parts[0], color: "" };

  if (parts.length === 2) {
    // "Insulated tumbler / Black" → color=Black, size=""
    // "S / Black" → size=S, color=Black
    const [a, b] = parts;
    if (KNOWN_COLORS.has(b)) {
      return { size: KNOWN_COLORS.has(a) ? "" : a, color: b };
    }
    return { size: b, color: a };
  }

  // 3+ parts: "Unisex Hoodie / S / Black"
  const candidate1 = parts[parts.length - 2];
  const candidate2 = parts[parts.length - 1];
  if (KNOWN_COLORS.has(candidate2)) return { size: candidate1, color: candidate2 };
  if (KNOWN_COLORS.has(candidate1) && !KNOWN_COLORS.has(candidate2)) {
    return { size: candidate2, color: candidate1 };
  }
  return { size: candidate1, color: candidate2 };
}
```

Color map lookup must be case-insensitive:
```ts
const normalizeKey = (k: string) =>
  k.toLowerCase().replace(/\b\w/g, (c) => c.toUpperCase());

const getColorHex = (color: string): string =>
  COLOR_MAP[color] ?? COLOR_MAP[normalizeKey(color)] ?? "#999999";
```

## Key Rules
- Never parse by position alone — Printful format differs by product category
- Always make COLOR_MAP lookup case-insensitive — Printful casing is inconsistent
- Test variant picker with both apparel (3-part) AND drinkware/accessories (2-part) before declaring complete

## Reuse Condition
Any project with Printful POD products that has a variant picker UI with color swatches + size chips.

## Related
- Error: [[errors/printful-color-only-variant-misparse]]
