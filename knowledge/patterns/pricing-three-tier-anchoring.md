# Pattern: 3-Tier Pricing — Center Tier as Hero, Kill the Premium Badge

**Category:** Conversion / Pricing Psychology
**First used:** Placed Right Fence — Apr 2026

## What
In a 3-tier pricing layout, the middle tier should be the psychological anchor. Removing any "best value" or "full service" badge from the premium tier ensures the eye naturally treats middle as the recommended choice — maximizing conversion to the most accessible price point.

## When to Use
Any 3-tier pricing page where the goal is to push the majority of conversions to the middle tier. Works for service pricing, SaaS plans, and product tiers.

## How
```ts
// WRONG — premium badge competes with growth badge
{ name: "Growth", badge: "Most Popular", price: "$3,000" }
{ name: "Premium", badge: "Full Service", price: "$5,500" }

// RIGHT — only middle gets a badge; premium stands alone
{ name: "Growth", badge: "Most Popular", price: "$3,000" }
{ name: "Premium", badge: null, price: "$5,500" }
```

Additional anchoring mechanics:
- Make the middle card visually larger (extra padding, elevated shadow, gold border)
- Show the entry tier first to establish a low anchor, making the middle look reasonable
- Premium tier exists to make the middle tier look affordable by comparison — it doesn't need a badge to serve this purpose

## Key Rules
- Never badge the premium tier. A badge says "this is where you should land." You want premium to feel aspirational, not recommended.
- The premium tier's job is anchoring, not converting. Design it to look capable, not to look like a deal.
- If the client asks to add a badge to premium ("full service," "white glove," etc.), explain the psychology and redirect to a subtle visual treatment (e.g. a thin gold outline) instead.

## Reuse Condition
Every 3-tier pricing page. This is a one-line fix (set badge: null) that directly impacts conversion rate.
