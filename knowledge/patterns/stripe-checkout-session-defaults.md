---
name: Stripe Checkout Session — Required Defaults for Every Build
type: pattern
description: Baseline Stripe checkout session settings that must always be included — customer_creation, canonical redirect URLs, absolute image URLs only
---

# Pattern: Stripe Checkout Session — Required Defaults for Every Build
**Category:** Payments  
**First used:** Andrea Abella Marie — Apr 2026

## What
A set of non-obvious Stripe checkout session settings that must always be included. Omitting any of them causes silent bugs discovered only during live testing.

## When to Use
Every build with a Stripe hosted checkout session.

## How

```ts
const session = await stripe.checkout.sessions.create({
  payment_method_types: ["card"],
  mode: "payment",
  customer_creation: "always",     // ← REQUIRED: enables receipt email for guest checkout
  line_items: items.map((item) => ({
    price_data: {
      currency: "usd",
      product_data: {
        name: item.name,
        // Only pass images if they are absolute HTTPS URLs
        // Relative /public paths cause Stripe to silently drop the image
        ...(item.image?.startsWith("http") ? { images: [item.image] } : {}),
      },
      unit_amount: Math.round(item.price * 100),
    },
    quantity: item.quantity,
  })),
  success_url: `${process.env.NEXT_PUBLIC_SITE_URL}/shop?success=true`,
  cancel_url: `${process.env.NEXT_PUBLIC_SITE_URL}/shop`,
  // Store cart in metadata — webhook reads this to create fulfillment order
  metadata: {
    cart: JSON.stringify(cartItems),
  },
});
```

## Key Rules
- `customer_creation: "always"` — without this, guest customers get no receipt email
- Images must be absolute HTTPS URLs — `/public/image.jpg` will be silently ignored by Stripe
- Always store full cart in `metadata.cart` as JSON — this is how the webhook knows what to fulfill
- `success_url` and `cancel_url` must use `NEXT_PUBLIC_SITE_URL` — never hardcode domain

## Reuse Condition
Every build with Stripe checkout. Copy this as the starting template.

## Related
- Error: [[errors/stripe-guest-checkout-no-receipt-email]]
- Pattern: [[patterns/stripe-www-canonical-webhook-url]]
