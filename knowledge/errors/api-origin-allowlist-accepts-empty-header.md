# Error: API Origin allowlist returns true on empty Origin/Referer header
**Project:** Goddu Imprint
**Date:** 2026-05-17
**Phase:** Stage 1J BUG fix commit (run-2 fix)

## Problem
Hardening `/api/contact` against spam-relay (Stage 1J BUG-1) added an `isAllowedOrigin()` check that allowed POSTs from godduimprint.com/www/localhost and rejected everything else. The initial fix included a hedge for "edge runtimes that strip Origin":

```ts
const origin = request.headers.get("origin") ?? request.headers.get("referer") ?? "";
if (!origin) {
  // Same-origin form submissions may omit Origin in some edge runtimes;
  // accept when absent rather than blocking real users. Rate limit still applies.
  return true;
}
```

That hedge was wrong. Modern browsers (Chrome, Safari, Firefox) all set `Origin` on `fetch POST` to a non-GET endpoint. The empty-header population in production is **non-browser clients**: curl, Python `requests`, headless scripts, scraper bots. Which is exactly the abuse class the allowlist was meant to block.

A curl POST with no Origin/Referer would pass the allowlist, hit the rate limiter (5/IP/10min), and burn through 5 spam relays per session per IP before the rate limit blocked it.

Caught by `/optimus-review` run-2 verifier.

## Root Cause
The "edge runtime might strip Origin" hedge was speculative — no Optimus deploy target has ever observed this. Vercel preserves Origin end-to-end. The check was hardening for a phantom failure mode while waving through the real abuse mode.

## Solution
Reject when Origin/Referer is empty:

```ts
if (!origin) return false;
```

Modern-browser clients set Origin on fetch POST as a hard guarantee. The empty-header population is the abuse class. Fixed in commit `467ef0b`.

## Prevention
**Rule for API allowlist checks on public form routes:**
- Origin/Referer empty → reject (browser-class hardening)
- Origin set + matches allowlist → accept
- Origin set + doesn't match allowlist → reject (403 Forbidden)

The "accept on empty for edge-runtime quirks" hedge is incorrect for any Optimus deploy target (Vercel). If a future edge runtime is observed to strip Origin, narrow the exception to a User-Agent browser-signature match — never blanket-accept empty.

For defense-in-depth on public form routes, pair Origin allowlist with:
- Rate limit (5/IP/10min in-memory, or Upstash Ratelimit + KV in production)
- Honeypot field (server-side check + client-side hidden input — both halves required per Error #67)
- Zod schema validation
- Control-char sanitizer before any string interpolation into email subject/body
- Optional: Cloudflare Turnstile or hCaptcha for human verification

See Pattern [[../patterns/api-public-form-defense-in-depth]] for the full hardening template.

## Related
- Pattern [[../patterns/api-public-form-defense-in-depth]] — the bundled defense-in-depth template
- Error [[honeypot-defense-incomplete-without-client-input]] — companion bug from the same fix batch
- Pattern [[../patterns/iterate-to-clean-n-run-review]] — caught by re-run
