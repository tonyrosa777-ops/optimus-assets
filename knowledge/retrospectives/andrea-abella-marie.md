---
name: Andrea Abella Marie — Project Retrospective
type: retrospective
description: Full-stack coaching website with working Printful+Stripe shop, Resend transactional emails, GHL CRM integration, and blog
---

# Andrea Abella Marie — Project Retrospective
**Type:** Trauma-informed mindset coach + energy healing practitioner  
**Client:** Andrea Abella Marie / Inner Peace Project  
**Domain:** coachandreaabellamarie.com  
**Completed:** Apr 2026  
**Build sessions:** ~8 sessions (Mar 10 – Apr 1 2026)  
**Deal value:** $5,500

---

## What Went Well
- Full e-commerce stack shipped and verified end-to-end with a real live purchase — Stripe → webhook → Printful order confirmed → customer receipt → owner alert all working
- Dual fulfillment model (POD auto via Printful + manual Resilience Collection jewelry) handled cleanly in one webhook
- Resend domain verification on GoDaddy via auto-configure worked perfectly — DKIM + SPF green in one click
- Blog architecture with 8 AI-generated posts and images (6 with Andrea's likeness) delivered with no photography required
- Seeded JSON fallback for Printful kept the shop rendering even during API downtime
- `KNOWN_COLORS` variant parser elegantly handled the 2-part vs 3-part naming inconsistency across Printful product categories
- `website-build-template.md` updated with all production-proven shop patterns so next build starts battle-tested

---

## What Didn't
| # | Gap | Fix Applied |
|---|-----|-------------|
| 1 | Snipcart tried first — abandoned after cart button unresponsiveness and complexity | Reverted to custom React Context cart + Stripe hosted checkout |
| 2 | Printful orders landing as Draft — `confirm:true` in body silently ignored | Changed to `?confirm=true` query param |
| 3 | Stripe webhook 307 — non-www domain redirects, Stripe doesn't follow | Updated webhook URL in Stripe Dashboard to www canonical |
| 4 | Color-only variants (tumblers) showing colors as size chips | Built KNOWN_COLORS parser, fixed variant field assignment |
| 5 | "Bottle Green" rendering as gray — missing from COLOR_MAP + casing mismatch | Added to map, made lookup case-insensitive |
| 6 | No customer receipt email on purchase | Added `customer_creation: "always"` to Stripe session |
| 7 | Contact form had empty `onSubmit` — discovered post-launch by client | Built `/api/contact` → Resend route |
| 8 | GHL CRM integration via Private Integration API — 5 failed attempts (403, 401, token exchange) | Switched to GHL Inbound Webhook — no auth required |
| 9 | Resend API key exposed in screenshot during setup | Rotated immediately; new key in Vercel |
| 10 | Printful billing card outdated — first confirmed order payment failed | Andrea updated card in Printful → Billing; retried successfully |

---

## Tools Introduced This Build
| Tool | Purpose | Notes |
|------|---------|-------|
| Resend | Transactional email (owner order alerts + contact form) | Free tier, 3k/month; domain verified via GoDaddy auto-configure |
| Printful API | POD fulfillment via webhook | `?confirm=true` as query param — not body |
| GHL Inbound Webhook | CRM contact creation from external forms | Bypass all Private Integration auth issues |

---

## Changes Made to Toolkit
- `website-build-template.md` Section 7 fully rewritten with production-proven Printful + Stripe + Resend architecture including all gotchas
- 5 new errors logged to Error Encyclopedia
- 4 new patterns logged to Build Patterns
- Pre-launch QA checklist should add: "test every form submit and confirm email delivery"
- Shop QA should add: "test variant picker with at least one apparel AND one drinkware product"
- Stripe webhook setup should add: "confirm canonical www/non-www before registering"
