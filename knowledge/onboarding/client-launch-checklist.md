# Client Launch Checklist — Optimus Business Solutions
# The exact steps to go from signed invoice to live site.
# Run these in order. Do not skip steps or defer to "later."

---

## Phase 1 — In-Meeting Setup (do during sales meeting, immediately after invoice paid)

### 1A. Domain Purchase (GoDaddy)
1. Go to godaddy.com
2. Search the client's preferred domain name
3. Select `.com` — prefer 1-year unless they want multi-year
4. Remove all add-on upsells (domain protection, email, etc.) at checkout
5. Complete purchase (Apple Wallet auto-fills on Mac — saves time)
6. Note the domain: `____________________`

### 1B. GoDaddy Admin Access
1. In GoDaddy, go to **Account Settings → Delegate Access**
2. Grant admin access to: `anthony@optimusbusinesssolutions.com` (or current Anthony email)
3. This allows DNS configuration to happen remotely after the meeting

### 1C. Resend Account Setup (free tier)
1. Go to resend.com → Get Started
2. Create account with client's **business email** (not personal if possible)
   - Use the console email if available (e.g. hungarianconsulne@gmail.com)
   - Create password: simple but not trivial (e.g. `HCwebsite3%`) — client can change after
3. Verify email (check inbox)
4. Note credentials: email `________________` / password `________________`
   - These go to the client after launch — don't lose them

---

## Phase 2 — Post-Meeting, Before Build (do same day or next morning)

### 2A. Resend Domain Configuration
1. Log into resend.com with client's account
2. Go to **Domains → Add Domain**
3. Enter the purchased domain (e.g. `hungarianconsulne.com`)
4. Click **Auto-configure DNS** — Resend will prompt to sign into GoDaddy
5. Sign into GoDaddy → authorize → Resend auto-creates DKIM + SPF records
6. Verify domain status in Resend: should go green within ~5 minutes
7. Create API key: **API Keys → Create API Key** → name it `[ClientName] Website`
8. Copy the key immediately — it only shows once
9. Note: `RESEND_API_KEY=re_____________________`

### 2B. Add Resend Key to Vercel
1. Go to Vercel → Project → Settings → Environment Variables
2. Add: `RESEND_API_KEY` = the key from step 2A
3. Apply to: Production, Preview, Development
4. Redeploy if the project is already live

### 2C. Test the Contact Form
1. Go to the live site (or preview deployment)
2. Fill out the contact form with a test submission
3. Verify email arrives in client's inbox within 30 seconds
4. If not: check Resend logs → Emails tab → look for error

---

## Phase 3 — DNS to Vercel (do after Vercel project is created and deployed)

### 3A. Connect Domain in Vercel
1. Go to Vercel → Project → **Settings → Domains**
2. Click **Add Domain** → enter the client's domain (e.g. `hungarianconsulne.com`)
3. Also add the www version: `www.hungarianconsulne.com`
4. Vercel will show a prompt — click **Learn More** or **DNS Records**
5. Copy the **A record** values:
   - Type: `A`
   - Name: `@`
   - Value: `76.76.21.21` (Vercel's IP — verify in Vercel's current docs)
6. Also copy the **CNAME record** for www:
   - Type: `CNAME`
   - Name: `www`
   - Value: `cname.vercel-dns.com`

### 3B. Update GoDaddy DNS
1. Log into GoDaddy → **My Domains → DNS**
2. Delete any existing A records pointing to GoDaddy's default parking page
3. Add new A record: Name `@`, Value = Vercel IP from step 3A
4. Add CNAME: Name `www`, Value = `cname.vercel-dns.com`
5. Save changes
6. DNS propagation: usually 5–30 minutes, can take up to 48 hours

### 3C. Verify in Vercel
1. Return to Vercel → Project → Settings → Domains
2. Both domains should show green checkmarks within 30 minutes
3. Test: visit `https://clientdomain.com` — should load the deployed site with SSL

---

## Phase 4 — Environment Variables (Vercel Production)

Add all of these to Vercel → Project → Settings → Environment Variables.
Apply each to: **Production, Preview, Development** unless noted.

```
STRIPE_SECRET_KEY          sk_live_...         (use live key, not test)
STRIPE_WEBHOOK_SECRET      whsec_...           (from Stripe → Webhooks → endpoint)
RESEND_API_KEY             re_...              (from Phase 2A)
PRINTFUL_API_KEY           ...                 (Printful → Settings → API, if shop)
NEXT_PUBLIC_CALENDLY_URL   https://calendly.com/...  (client's booking link)
NEXT_PUBLIC_SITE_URL       https://www.domain.com    (canonical — MUST include https:// — affects OG tags + JSON-LD)
NEXT_PUBLIC_BEHOLD_FEED_ID https://feeds.behold.so/... (if Instagram feed is active)
NEXT_PUBLIC_SHOW_PRICING_TOOLS  false          (removes dev-only pricing tools)
SANITY_PROJECT_ID          ...                 (if blog/CMS is active)
SANITY_DATASET             production
```

**Local `.env.local` mirror** (for development):
```env
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...
RESEND_API_KEY=re_...
PRINTFUL_API_KEY=...
NEXT_PUBLIC_CALENDLY_URL=https://calendly.com/...
NEXT_PUBLIC_SITE_URL=http://localhost:3000
NEXT_PUBLIC_SHOW_PRICING_TOOLS=true
```

---

## Phase 5 — Stripe Webhook Registration

1. Go to Stripe Dashboard → **Developers → Webhooks**
2. Click **Add endpoint**
3. Enter URL: `https://www.yourdomain.com/api/stripe/webhook`
   - CRITICAL: use the canonical domain (with www if that's how it's configured in Vercel)
   - Stripe does NOT follow 301/307 redirects — wrong URL = silent webhook failure
4. Select event: `checkout.session.completed` only
5. Click **Add endpoint**
6. Copy **Signing secret** → add to Vercel as `STRIPE_WEBHOOK_SECRET`
7. Test with Stripe CLI: `stripe listen --forward-to localhost:3000/api/stripe/webhook`

---

## Phase 6 — Pre-Launch Final Check

- [ ] All env vars set in Vercel (see Phase 4)
- [ ] Contact form tested and receiving emails (see Phase 2C)
- [ ] DNS resolving to correct Vercel deployment (see Phase 3C)
- [ ] Stripe webhook registered at canonical URL (see Phase 5)
- [ ] Dev-only components removed: ROI calculator, pricing tools (`NEXT_PUBLIC_SHOW_PRICING_TOOLS=false`)
- [ ] All console.log statements removed
- [ ] Real photos in place (no fal.ai placeholders if client has photography)
- [ ] No `PhotoPlaceholder` components remain — replace with `next/image` once real assets are confirmed (scaffold `onError` can fire on production even when image exists)
- [ ] `NEXT_PUBLIC_SITE_URL` includes `https://` protocol (missing protocol breaks OG tags and JSON-LD structured data)
- [ ] All copy reviewed by client
- [ ] OG image verified (visit site in Twitter Card Validator)
- [ ] Mobile tested on real device (not just responsive mode)
- [ ] Calendly booking flow tested end-to-end

---

## Credentials Handoff (at or after launch)

Give the client a simple document with:
- GoDaddy: their own account (they paid for it)
- Resend: email + password created in Phase 1C
- Vercel: invite them to the project (Settings → Members) as Viewer
- Sanity: invite them to the project as Editor (if CMS is active)
- Note: they own all of this from day one
