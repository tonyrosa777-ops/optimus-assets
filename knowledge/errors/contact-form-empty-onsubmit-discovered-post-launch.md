---
name: Contact Form Empty onSubmit — Discovered Post-Launch by Client
type: error
description: Contact form onSubmit was an empty stub; client discovered it after launch when no inquiries arrived
---

# Error: Contact Form Empty onSubmit — Discovered Post-Launch by Client
**Project:** Andrea Abella Marie  
**Date:** Apr 2026  
**Phase:** Post-launch client feedback

## Problem
Contact form `onSubmit` handler was:
```tsx
onSubmit={(e) => {
  e.preventDefault();
  // Integration point for n8n webhook
}}
```
Form appeared fully functional — fields, validation, button all worked. The client discovered the problem only when a visitor filled out the form and no message arrived. The email backend was labeled "out of scope" in the original package, but the form UI was built and left with a dead handler.

## Root Cause
Form UI was built and declared complete without a working submission path. "Out of scope" was interpreted as "don't build the backend" but the form stub created a false impression that submission worked.

## Solution
Built `POST /api/contact` route using the already-configured Resend account (same key as order alerts). Form now emails Andrea on every submission with visitor name, email, phone, topic, and message. `replyTo` set to visitor's email so Andrea can reply directly from her inbox.

## Prevention
- Any form with a submit button must either: (a) have a working backend, or (b) have the button visibly disabled/removed and a note explaining why
- Never leave `e.preventDefault()` with a comment as the entire handler — this is a production bug dressed as a placeholder
- Pre-launch QA checklist must include: "test every form submit and confirm delivery"
- Consider making form backend a standard line item rather than an upsell — a form that doesn't submit is worse than no form at all

## Related
- Error: [[errors/placeholder-cta-accepted-as-complete]] (same class of problem)
