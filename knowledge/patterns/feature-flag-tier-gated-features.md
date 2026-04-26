# Pattern: Feature-flag tier-gated features (instead of deleting)

**Category:** Architecture / Sales / Post-Sale Workflow
**First used:** Collaborative Insights — 2026-04-20

## What
When the client selects a tier below Premium, **hide** the tier-exclusive feature behind a feature flag rather than deleting the scaffolded code. The feature stays in the repo; flipping a `NEXT_PUBLIC_*_ENABLED=true` env var in Vercel + a redeploy reveals it. Cheap to turn back on if the client upgrades, no re-scaffolding cost.

Default example: shop (Premium-only). If client buys Pro, the scaffold (`src/lib/cart.tsx`, `CartDrawer`, seeded products, Printful/Stripe routes, `/shop` page) stays in place but:
- `Shop` nav link filtered out of header
- Cart icon hidden (both desktop and mobile)
- `/shop` route returns `notFound()`
- Sitemap already excluded it

## When to Use
- Any feature that the Optimus tier gate includes/excludes (currently: shop + email automation + Stripe payment — all Premium-only per pricing-packages.md)
- Any time a client signs at a lower tier than the "always-scaffold-everything" CLAUDE.md rule produced
- NOT for features the client explicitly rejects as out-of-scope — those should be fully removed to avoid future confusion

## How

```ts
// src/lib/feature-flags.ts — new file, one per project
export const isShopEnabled =
  process.env.NEXT_PUBLIC_SHOP_ENABLED === "true";

// Add one constant per tier-gated feature as needed:
// export const isEmailAutomationEnabled = process.env.NEXT_PUBLIC_EMAIL_AUTOMATION_ENABLED === "true";
// export const isStripeCheckoutEnabled = process.env.NEXT_PUBLIC_STRIPE_CHECKOUT_ENABLED === "true";
```

Then gate the 3 canonical touch points:

```tsx
// 1. Nav filter
const navLinks = allNavLinks.filter(
  (link) => link.href !== "/shop" || isShopEnabled,
);

// 2. Visible affordance (cart icon)
{isShopEnabled && <CartButton />}

// 3. Route
// src/app/shop/page.tsx
export default function ShopPage() {
  if (!isShopEnabled) notFound();
  return <ShopContent />;
}
```

**To reveal later:** add `NEXT_PUBLIC_SHOP_ENABLED=true` to the project's Vercel env vars (Production + Preview + Development) → trigger a redeploy. Zero code changes.

## Key Rules
- **Feature flag is `NEXT_PUBLIC_*`.** It gates UI visibility, not access to secret operations. Real secrets (Printful API key, Stripe secret) are still server-only env vars and gate the actual data layer separately.
- **Default to `false` when env var is absent.** `process.env.FOO === "true"` style — not `!== "false"`. Missing env var = feature off.
- **Leave the CartProvider mounted in layout.tsx.** It reads from localStorage on mount; unmounting it would throw away any cart state if the flag flips back on mid-session. Mounted-but-hidden is fine.
- **Route still returns 404, not redirect.** `notFound()` is cleaner for SEO than `redirect("/")` — absent feature should look like it doesn't exist.
- **Document the flag in a short code comment.** Specifically: the env var name, what it controls, and "to reveal: set in Vercel + redeploy."

## Reuse Condition
Apply on every build where:
- The client purchased Pro (not Premium) AND
- The Optimus scaffold included a tier-gated feature they didn't buy

Also: whenever a feature is built ahead of client approval for upsell purposes (e.g., shop shown in demo, then deferred to post-launch upsell).

Do **not** apply when the feature is truly scope-excluded and won't be revisited — delete those cleanly.

## Related
- [[patterns/post-sale-pricing-page-archive]] — same post-sale workflow, for the /pricing page itself
- CLAUDE.md `Always-Built Features Rule` → Shop → "Decision gate (after scaffold)" — this pattern is the "client did not buy Premium" branch, changed from "delete" to "flag-off" for reversibility
