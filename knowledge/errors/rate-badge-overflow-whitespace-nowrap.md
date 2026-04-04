# Error: Rate Badge Overflows Card with Long Text in whitespace-nowrap Pill
**Project:** Danielle Thompson
**Date:** Apr 2026
**Phase:** Content updates post-launch

## Problem
A service card's rate badge showed overflowing / clipped text. The travel policy rate was set to a long descriptive string: `"Included within 15 mi of Gardner · Travel pay + accommodations beyond"`. The badge uses `whitespace-nowrap` which prevents wrapping, causing the pill to overflow its container.

## Root Cause
The rate field in `NOTARY_SERVICES` array renders directly into a `whitespace-nowrap shrink-0` badge pill. Long strings can't wrap and push the card layout. The field was designed for short pricing strings (e.g. `"$15 per signature"`), not policy descriptions.

## Solution
Shortened the rate to a pointer: `"See travel policy"` — the full policy detail lives in the Pricing Notes section directly below the cards, where there's room to breathe.

## Prevention
- Rate badge field: max ~25 characters. Anything longer needs a pointer ("See pricing", "By quote", "Contact us") with detail in a dedicated notes block
- Before setting any data-driven field value, check how it's rendered (badge? paragraph? table?) to know its length constraints
- If a service has a complex rate, use the description field for nuance and keep the rate badge as a category label

## Related
- [[patterns/constants-ts-single-source-of-truth]]
