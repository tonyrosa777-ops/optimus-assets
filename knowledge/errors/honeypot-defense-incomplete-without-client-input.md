# Error: Honeypot field defense incomplete — server check without client-side hidden input
**Project:** Goddu Imprint
**Date:** 2026-05-17
**Phase:** Stage 1J BUG fix commit (run-2 fix)

## Problem
Hardening `/api/contact` against spam (Stage 1J BUG-1) added a server-side honeypot check: any request body where `body.website` was a non-empty string would silently 200 (accept and discard, so the bot doesn't learn the trap tripped).

The fix added the server-side check but **never added a corresponding hidden input to ContactClient.tsx**. The form HTML rendered no `website` field. The defense became dead code: bots scraping the form would only fill the visible Name/Email/Phone/Company/Message fields. They'd never include `website` in their POST. The server-side trap never fires for the class of bot it claims to catch.

The route's JSDoc explicitly advertised "Honeypot field silently accepts bot submissions" as a hardening claim. The advertisement materially overstated what the function delivered.

Caught by `/optimus-review` run-2 verifier.

## Root Cause
Honeypot pattern requires **both halves** to function:
1. Server-side: check request body for honeypot field, silently accept if filled (bots don't learn the trap is server-side gated)
2. Client-side: render a visually-hidden input in the form (humans never see it, naive auto-filling bots fill all visible fields)

Shipping only the server half is a half-finished implementation. The advertised defense doesn't exist.

## Solution
Added the visually-hidden client-side input + schema entry + default value to `ContactClient.tsx`:

```tsx
// Schema
website: z.string().max(0).optional(),

// Default value
website: "",

// Hidden input (first form field)
<input
  type="text"
  tabIndex={-1}
  autoComplete="off"
  aria-hidden="true"
  {...register("website")}
  style={{
    position: "absolute",
    left: "-9999px",
    width: "1px",
    height: "1px",
    opacity: 0,
  }}
/>
```

Fixed in commit `467ef0b`.

## Prevention
**Rule for honeypot patterns:** never ship the server-side half without the matching client-side half. If the client-side input lands in a different commit, the server-side check is commented out until the pair lands together.

Inline JSDoc on the route should describe BOTH halves:
```ts
/**
 * Honeypot — humans never see the visually-hidden `website` input in
 * ContactClient.tsx (lines NN-NN). Naive bots auto-fill all inputs and trip
 * this trap. Server returns silent 200 so bots don't learn the trap is
 * server-side gated.
 */
```

Pre-launch-auditor pattern check: grep the project for `website: z.string().max(0)` (or the project's honeypot field name) and verify a matching client-side hidden input exists in the corresponding form component. Add to pre-launch-auditor.md SECTION 4 — Forms and Conversion Flows.

Honeypot is one of several defense-in-depth layers on public form routes. See Pattern [[../patterns/api-public-form-defense-in-depth]] for the full template.

## Related
- Pattern [[../patterns/api-public-form-defense-in-depth]] — the bundled defense-in-depth template
- Error [[api-origin-allowlist-accepts-empty-header]] — companion bug from the same fix batch
- Pattern [[../patterns/iterate-to-clean-n-run-review]] — caught by re-run
