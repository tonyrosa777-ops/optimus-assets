---
name: Stripe Webhook 307 — www Redirect Breaks Delivery
type: error
description: Stripe webhook registered on non-www domain that redirects to www — Stripe doesn't follow redirects, webhook silently fails
---

# Error: Stripe Webhook 307 — www Redirect Breaks Delivery
**Project:** Andrea Abella Marie  
**Date:** Apr 2026  
**Phase:** Shop & Payments — live purchase testing

## Problem
Stripe webhook registered as `https://coachandreaabellamarie.com/api/stripe/webhook`. The domain redirects non-www → www. Stripe sent the event, the server returned HTTP 307, Stripe did not follow the redirect and marked the delivery as failed. No Printful order was created. No owner alert was sent. No errors in code — the bug was invisible until checking Stripe Dashboard → Webhooks → event log.

## Root Cause
Stripe does not follow HTTP redirects for webhook delivery. If the registered URL returns any 3xx, Stripe marks it as a delivery failure and will retry with exponential backoff — eventually marking the endpoint as failed.

## Solution
1. In Stripe Dashboard → Webhooks → find the endpoint → Edit
2. Update URL to the canonical domain: `https://www.coachandreaabellamarie.com/api/stripe/webhook`
3. Update `NEXT_PUBLIC_SITE_URL` in Vercel to `https://www.coachandreaabellamarie.com` (with www) to match

## Prevention
- At project start, confirm the canonical domain (www vs non-www) before registering the webhook
- Register webhook URL at the exact canonical URL — never the redirecting version
- After deploying, check Stripe Dashboard event log immediately after a test purchase to confirm 200 OK

## Related
- Pattern: [[patterns/stripe-www-canonical-webhook-url]]
