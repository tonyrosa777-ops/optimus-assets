---
name: Stripe Guest Checkout — No Customer Receipt Email
type: error
description: Guest checkout customers don't receive a receipt email by default; requires customer_creation: "always"
---

# Error: Stripe Guest Checkout — No Customer Receipt Email
**Project:** Andrea Abella Marie  
**Date:** Apr 2026  
**Phase:** Shop & Payments — live purchase testing

## Problem
Customer completed a real purchase via Stripe hosted checkout. No receipt email was received. The checkout was in guest mode (no Stripe account created). Stripe only sends receipt emails to Stripe customers, not anonymous guest sessions.

## Root Cause
Stripe hosted checkout defaults to guest mode where no `Customer` object is created. Without a Customer object, Stripe has no entity to send a receipt to — even if the customer provided their email address.

## Solution
Add `customer_creation: "always"` to the Stripe checkout session creation:
```ts
const session = await stripe.checkout.sessions.create({
  mode: "payment",
  customer_creation: "always",  // ← creates a Customer object, enables receipt email
  // ...
});
```

## Prevention
- Always include `customer_creation: "always"` on any Stripe checkout session in `payment` mode
- Add to checkout route boilerplate — this should be the default for every build with a shop
- Verify receipt delivery during live purchase testing (not just test mode)

## Related
- Pattern: [[patterns/stripe-checkout-session-defaults]]
