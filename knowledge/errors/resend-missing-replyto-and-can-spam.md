# Resend Missing replyTo + CAN-SPAM Compliance

## Problem

Resend emails sent with branded `from` addresses (e.g. `quiz@clientdomain.com`,
`proposals@clientdomain.com`) that are not real inboxes. These addresses exist
only as Resend sending identities on a verified domain — no MX records, no
mailbox behind them.

**Two failures:**

1. **Owner notification missing `replyTo`:** When the business owner receives a
   lead notification and hits Reply, Gmail sends the reply to the `from` address
   (e.g. `quiz@clientdomain.com`). That address can't receive mail. Gmail returns
   `554 5.4.0 < #4.4.1 smtp; The recipient server did not accept our requests to
   connect`. The owner thinks their email is broken. Leads go unanswered.

2. **Auto-reply to customer missing `replyTo`:** When a customer receives the
   auto-reply (e.g. "We received your proposal") and hits Reply, it goes to the
   branded `from` address instead of the owner's real email. Same bounce.

3. **VIP/newsletter welcome email missing CAN-SPAM compliance:** Any email that
   promises future communication ("you'll be the first to know") is marketing
   under CAN-SPAM. Requires: (a) opt-out mechanism, (b) physical mailing address.

## Symptoms

- "Delivery is delayed to these recipients or groups" bounce emails in owner inbox
- `554 5.4.0` errors in Mail Delivery Subsystem notifications
- Owner thinks they need to "log into" the branded email address
- Customers who reply to auto-confirmations never reach the business

## Fix

Every `resend.emails.send()` call must include an explicit `replyTo`:

```typescript
// Owner notification — replyTo = the lead's email
await resend.emails.send({
  from: "quiz@clientdomain.com",
  to: "owner@gmail.com",
  replyTo: leadEmail,          // <-- owner hits Reply, goes to customer
  subject: `New Lead: ${name}`,
  text: emailBody,
});

// Auto-reply to customer — replyTo = the owner's real email
await resend.emails.send({
  from: "angela@clientdomain.com",
  to: leadEmail,
  replyTo: "owner@gmail.com",  // <-- customer hits Reply, goes to owner
  subject: `We got your message, ${name}`,
  text: autoReplyBody,
});
```

For marketing emails (VIP welcome, newsletter), append to the email body:

```
— Owner Name
Business Name
123 Street, City, ST ZIP

—
Don't want to hear from us? Reply to this email with "UNSUBSCRIBE" and we'll remove you from the list.
```

## Launch Checklist

Before any project goes live, audit every API route that calls `resend.emails.send()`:

- [ ] Every owner notification has `replyTo: customerEmail`
- [ ] Every auto-reply has `replyTo: "owner@realemail.com"`
- [ ] Marketing emails (promising future sends) have unsubscribe line + physical address
- [ ] Test: submit every form, check that Reply on every received email goes to the right place

## Project

Enchanted Madison — April 2026

## Discovery

Post-launch. Client saw bounce notifications in Gmail inbox for days before
reporting. Multiple leads (Larry, Deja Gates, Mackenzie) had delayed/failed
reply delivery. Root cause was invisible during development because Resend
sends succeed — the bounce only appears when someone replies.
