# Error: Printful CDN Image URLs Fabricated Without Confirmation
**Project:** Cody's Complete Junk Removal
**Date:** Apr 2026
**Phase:** Shop build — product data population

## Problem
When populating `shop.ts` with Printful catalog products, the Printful catalog page was scraped via firecrawl. Most product images loaded as lazy-placeholder SVGs — the actual CDN image paths (`files.cdn.printful.com/o/upload/product-catalog-img/XX/...`) were only visible for a handful of products. For the rest, image URLs were guessed/fabricated based on the confirmed pattern. Those fabricated URLs would 404 in production.

## Root Cause
The firecrawl scrape captured the HTML source before JavaScript-rendered lazy images resolved. Only products with server-side or early-render images exposed real CDN paths. The pattern (`/XX/hash_l`) looks structured enough that fabrication seems plausible, but the hash is unique per product and cannot be guessed.

## Solution
Replaced all fabricated Printful CDN URLs with reliable Unsplash images. Only kept the 3 confirmed CDN URLs (snapback, beanie, mug) that appeared explicitly in the scrape response.

## Prevention
**Rule:** Never fabricate Printful CDN image URLs. If the URL doesn't appear literally in the scrape response, use an Unsplash image as placeholder. Add a comment marking it as placeholder. When client sets up their Printful store and generates mockups, swap in the real mockup URLs at that time.

To get real Printful product images: set `waitFor: 8000` in firecrawl_scrape to allow lazy images to resolve, or use the Printful API's product endpoints which return full image URLs.

## Related
- [[patterns/static-printful-merch-data-file]]
- [[errors/printful-color-only-variant-misparse]]
