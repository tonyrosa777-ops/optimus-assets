# Error #3 — Stripe 21: API Version & Shipping Details Breaking Changes

**Project:** Enchanted Madison  
**Date:** March 2026  
**Stripe version:** 21.0.1  

---

## Problem 1: API Version String Changed

**Error:**
```
Type error: Type '"2025-04-30.basil"' is not assignable to type '"2026-03-25.dahlia"'.
```

**Cause:** Stripe 21 bumped the required API version. Each Stripe major version only accepts a single specific API version string — it is hardcoded in the type definitions.

**Fix:** Always check the installed version before writing the apiVersion string:
```bash
cat node_modules/stripe/types/apiVersion.d.ts
# → export const ApiVersion = '2026-03-25.dahlia';
```

Then use that string in both checkout and webhook routes:
```typescript
const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!, {
  apiVersion: "2026-03-25.dahlia",
});
```

---

## Problem 2: `shipping_details` Moved to `collected_information`

**Error:** TypeScript: `Namespace 'Stripe.Checkout.Session' has no exported member 'ShippingDetails'`

**Cause:** In Stripe 21, shipping address collected during checkout is now at:
```
session.collected_information.shipping_details
```
Previously it was at `session.shipping_details`.

**Old code (Stripe 17–20):**
```typescript
const shipping = session.shipping_details;
```

**New code (Stripe 21+):**
```typescript
const shipping = session.collected_information?.shipping_details ?? null;
```

The type is now `Stripe.Checkout.Session.CollectedInformation.ShippingDetails`.

---

## Pattern: Always verify Stripe types at install time

When adding Stripe to a new project:
1. Run `npm install stripe`
2. Immediately check `node_modules/stripe/types/apiVersion.d.ts` for the correct version
3. Check breaking changes in `node_modules/stripe/CHANGELOG.md` before copying webhook handlers from prior projects

---

## Resolution Commits

- `a5c8f49` — feat(shop): build shop architecture with cart, Stripe checkout, and Printful POD
