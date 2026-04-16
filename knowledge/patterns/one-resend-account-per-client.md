# Pattern: One Resend Account Per Client (Free Tier Management)
**Category:** Email / Third-party Integration
**First used:** Danielle Thompson — Apr 2026

## What
Each client gets their own free Resend account rather than adding multiple clients to a single agency account. The free tier includes 1 verified sending domain — sufficient for one client site.

## When to Use
- Client site has a contact form that sends email via Resend
- You're managing multiple client sites and have already used your own Resend free domain slot
- Resend Pro ($20/mo) is not justified for a basic contact form use case

## How
1. Create account at resend.com with client's email address
2. In Resend → Domains → Add the client's domain (e.g. `clientdomain.com`)
3. Add the DNS records Resend provides (SPF, DKIM, CNAME) to the client's DNS registrar
4. Create API key → name it `[ClientName] Website` → copy `re_...` key
5. Add to Vercel: `RESEND_API_KEY` = the key
6. Set `OWNER_EMAIL` in Vercel → the business owner's real inbox (e.g. `owner@gmail.com`).
   Set `RESEND_FROM_EMAIL` in Vercel → the branded sending address (e.g. `hello@clientdomain.com`).
   In code, every API route reads these from env — never hardcode:
```ts
await resend.emails.send({
  from: process.env.RESEND_FROM_EMAIL!,
  to: process.env.OWNER_EMAIL!,
  replyTo: leadEmail,  // REQUIRED — see Error #50
  subject: `New Lead: ${name}`,
  text: body,
});
```

## Key Rules
- Resend free tier: 1 domain, 3,000 emails/mo, 100/day — plenty for a contact form
- Adding a second domain to your own free account requires upgrading to Pro ($20/mo)
- Each client owns their account — cleaner separation of billing, data, and access
- The `from` address domain must match a verified Resend domain or sends will be rejected
- Client can change password later — you set up the account, hand over credentials

## Reuse Condition
Every client site with a contact form using Resend.

## Related
- [[errors/ctabanner-prop-name-mismatch-build-failure]]
