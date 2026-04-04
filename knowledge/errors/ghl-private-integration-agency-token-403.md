---
name: GHL Private Integration — Agency Token 403 on Location Write
type: error
description: Agency admin creating a GHL Private Integration from within a sub-account still generates an agency-level token that cannot write to that location
---

# Error: GHL Private Integration — Agency Token 403 on Location Write
**Project:** Andrea Abella Marie  
**Date:** Apr 2026  
**Phase:** Post-launch — GHL CRM integration

## Problem
GHL Private Integration created from Settings → Private Integrations while navigated into a client sub-account (location). Token used for `POST /contacts/` with `locationId` in body. GHL returned:
```
403 {"statusCode":403,"message":"The token does not have access to this location."}
```
Attempted to exchange token via `/oauth/locationToken` endpoint — returned:
```
401 {"statusCode":401,"message":"The token is not authorized for this scope."}
```
Five separate code attempts (v1 API, v2 API, agency token, token exchange, optional locationId) all failed with auth errors.

## Root Cause
When an agency admin navigates into a sub-account and creates a Private Integration, GHL creates an **agency-level token** regardless of the navigation context. Agency tokens require explicit scope grants and token exchange to access specific locations — and the token exchange endpoint itself requires an OAuth scope not granted by default in Private Integrations.

## Solution
Abandon the Private Integration API approach entirely. Use **GHL Inbound Webhooks** instead:
1. GHL → Automation → Workflows → Create Workflow
2. Trigger: Inbound Webhook
3. Action: Create/Update Contact (map fields from webhook payload)
4. Save + Publish → copy webhook URL
5. POST form data to that URL from the API route — no auth required

## Prevention
- Do not use GHL Private Integration API tokens from an agency admin account to write to client sub-accounts — the token will always be agency-scoped
- For any GHL contact creation from an external website, use the **Inbound Webhook** approach from day one — it's simpler, requires no auth, and is the GHL-recommended pattern for external forms
- If API access is truly needed, the location user (not agency admin) must create the integration from their own login

## Related
- Pattern: [[patterns/ghl-inbound-webhook-crm-integration]]
