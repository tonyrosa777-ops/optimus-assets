---
name: Stripe Webhook — Always Register at Canonical (www) URL
type: pattern
description: Stripe doesn't follow redirects; webhook URL must exactly match the canonical domain including www prefix
---

# Pattern: Stripe Webhook — Always Register at Canonical (www) URL
**Category:** Payments / Infrastructure  
**First used:** Andrea Abella Marie — Apr 2026

## What
Before registering a Stripe webhook, confirm the canonical domain and use that exact URL — including or excluding www based on what the domain actually serves (not redirects to).

## When to Use
Every project with a Stripe webhook. Confirm canonical URL at project start, before the webhook is registered.

## How

**Step 1 — Confirm canonical domain:**
Open the live site and check the address bar after any redirect settles. Whatever URL shows is the canonical.

**Step 2 — Register webhook at canonical URL:**
```
Stripe Dashboard → Developers → Webhooks → Add endpoint
URL: https://www.yourdomain.com/api/stripe/webhook  ← use the canonical (www or not)
Events: checkout.session.completed
```

**Step 3 — Match env vars:**
```
NEXT_PUBLIC_SITE_URL=https://www.yourdomain.com  ← must match canonical
```

**Step 4 — Verify after first live test:**
Stripe Dashboard → Webhooks → click endpoint → check event log → confirm 200 OK (not 307)

## Key Rules
- Stripe does NOT follow HTTP redirects — any 3xx response = delivery failure
- Non-www → www redirects are the most common trap; always check
- `NEXT_PUBLIC_SITE_URL` and the Stripe webhook URL must both use the same canonical form
- After any domain change or Vercel project rename, re-verify the webhook URL

## Reuse Condition
Every build with Stripe checkout + webhook.

## Related
- Error: [[errors/stripe-webhook-307-www-redirect]]
