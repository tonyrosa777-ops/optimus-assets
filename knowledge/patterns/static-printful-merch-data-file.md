# Pattern: Static Printful Merch Data File (Pre-Integration)
**Category:** E-commerce / Printful
**First used:** Cody's Complete Junk Removal — Apr 2026

## What
For clients who want a branded merch shop but aren't yet ready to connect a live Printful account, populate `shop.ts` with real Printful catalog products (accurate names, real base costs, retail markup, actual product page links) and use Unsplash placeholder images. The shop is functional and real-looking; only the images are placeholders.

## When to Use
- Client wants a shop ("t-shirts, hats, mugs with our logo") but hasn't set up Printful yet
- No product mockups exist yet (Printful mockup generator requires a connected store)
- Client is in pre-launch phase and needs the full site to feel complete

## How
1. Scrape `printful.com/custom-products` to get real product names and base prices
2. Select 6–10 products appropriate for the business type (branded merch for service biz = tees, hats, beanies, hoodies, mugs, totes, stickers)
3. Set retail price at 2.5–3× Printful base cost
4. Use confirmed Printful CDN image URLs where visible in scrape; Unsplash for all others
5. Add `// Printful base: $X.XX | [Product Name]` comment on each product for client transparency
6. Add `files.cdn.printful.com` and `static.cdn.printful.com` to `next.config.mjs` image domains

```ts
// Example product entry
{
  slug: 'branded-snapback',
  name: "Cody's Complete Snapback Hat",
  description: 'Otto Cap 125-978 embroidered snapback...',
  price: 34.99,
  // Printful base: $18.09 | Snapback | Otto Cap 125-978
  image: 'https://files.cdn.printful.com/o/upload/product-catalog-img/da/da4d874ba768f357daf131d55e05adfd_l',
  category: 'Hats',
  badge: 'Best Seller',
  inStock: true,
}
```

## Key Rules
- **Never fabricate Printful CDN image URLs** — only use URLs that appear literally in the scrape response. Use Unsplash for everything else. See [[errors/printful-cdn-image-url-fabricated]]
- Comment every product with its Printful base cost — client needs this to understand margins when setting up their account
- Categories should match the filter tabs the shop UI uses — check `shopProducts` category values against the filter component
- When client generates Printful mockups, they just swap the `image` field — no other code changes needed

## Reuse Condition
Any local service business that wants merch. Especially good for businesses with strong brand identity (trades, services, outdoor/active lifestyle). Swap images when client goes live with Printful.

## Related
- [[errors/printful-cdn-image-url-fabricated]]
- [[patterns/printful-variant-name-parser-known-colors]]
