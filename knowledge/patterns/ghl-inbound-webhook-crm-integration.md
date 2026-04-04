---
name: GHL CRM Integration via Inbound Webhook
type: pattern
description: Connect external website forms to GoHighLevel CRM using GHL's native Inbound Webhook workflow trigger — no API key, no auth headaches
---

# Pattern: GHL CRM Integration via Inbound Webhook
**Category:** CRM / Integration  
**First used:** Andrea Abella Marie — Apr 2026

## What
Use GHL's built-in Inbound Webhook workflow trigger to receive contact form submissions and create contacts — bypassing all GHL API authentication complexity entirely.

## When to Use
Any time a website form needs to create or update a contact in a client's GoHighLevel account, especially when you are an agency admin managing a client sub-account (where Private Integration tokens will always be agency-scoped and unable to write to the location).

## How

**In GHL:**
1. Automation → Workflows → Create Workflow → Start from scratch
2. Trigger: **Inbound Webhook**
3. Action: **Create/Update Contact** — map fields:
   - First Name → `{{first_name}}`
   - Last Name → `{{last_name}}`
   - Email → `{{email}}`
   - Phone → `{{phone}}`
4. Action: **Add Tag** → `website-inquiry`
5. Save + Publish → copy the webhook URL

**In the API route:**
```ts
const webhookUrl = process.env.GHL_WEBHOOK_URL;
if (!webhookUrl) return; // non-fatal

await fetch(webhookUrl, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    first_name: firstName,
    last_name: lastName,
    email,
    phone,
    source: "Website Contact Form",
    tags: `website-inquiry,${subject}`,
    message: `Topic: ${subjectLabel}\n\n${message}`,
  }),
});
```

**Vercel env var:** `GHL_WEBHOOK_URL` = the webhook URL from GHL workflow

## Key Rules
- Do NOT attempt GHL Private Integration API tokens from an agency admin account — they will always be agency-scoped and will 403 on location writes
- The webhook URL is public but obscure (unique UUID in URL) — treat it like an API key; store in env vars, never hardcode
- Make this call non-fatal — wrap in try/catch, don't let GHL failure block the email confirmation
- GHL workflows can also trigger automations, SMS follow-ups, pipelines — much more powerful than raw API for this use case

## Reuse Condition
Any client with GoHighLevel who needs website form submissions to appear as contacts in their CRM.

## Related
- Error: [[errors/ghl-private-integration-agency-token-403]]
