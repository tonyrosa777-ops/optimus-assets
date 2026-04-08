# Error: JSON null vs TypeScript undefined in Seeded Data Files
**Project:** Where2 Junk
**Date:** 2026-04-05
**Phase:** Shop build — seeded Printful fallback products

## Problem
A seeded JSON fallback file (`printful-seeded-products.json`) had fields set to `null`:
```json
{ "preview_image_url": null }
```
The TypeScript type expected `string | undefined`. TypeScript rejected `null` as not assignable to `string | undefined`, causing a build failure in `ShopClient.tsx`.

## Root Cause
JSON `null` and TypeScript `undefined` are different values. TypeScript types that use `string | undefined` (optional fields) do NOT accept `null` — they accept the absence of the field, not an explicit null assignment.

## Solution
Remove the field entirely from all seeded JSON entries where the value would be `null`:
```json
// WRONG:
{ "preview_image_url": null }

// RIGHT:
{ }
// (field omitted — TypeScript sees it as undefined, which satisfies string | undefined)
```

## Prevention
- Never write `null` in seeded JSON files for optional TypeScript fields
- If a type is `string | undefined`, the JSON entry should simply omit the key
- If a type must accept null, define it as `string | null | undefined` in the interface

## Related
- [[patterns/static-printful-merch-data-file]] — the broader seeded shop pattern
