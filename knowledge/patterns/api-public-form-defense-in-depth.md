# Pattern: API public-form defense-in-depth
**Category:** Security / API / Forms
**First used:** Goddu Imprint — 2026-05-17

## What
Every public API route that sends transactional email from a verified domain (contact form, quiz submit, newsletter signup, booking confirmation) gets a defense-in-depth bundle: Zod schema validation + control-char sanitizer + Origin allowlist + in-memory rate limiter + honeypot field + safe-name sanitization for any auto-reply greeting + independent try/catch separating load-bearing send from courtesy send. Each layer alone is incomplete; the bundle hardens against the abuse classes that the file-level pre-launch-auditor (Stage 1H) and browser audit (Stage 1I) structurally cannot see.

## When to Use
Any new or modified API route in `src/app/api/**/route.ts` that:
- Accepts a POST from a public client (form submission, signup, booking)
- Calls a third-party send API (Resend, Twilio, Stripe checkout) with user-controlled fields interpolated into the payload
- Sends FROM a verified domain (any `noreply@{client-domain}`)

Mandatory on every Optimus build. Stage 1H pre-launch-auditor SECTION 4 should grep for these patterns and FAIL the audit if any are missing.

## How

### Layer 1 — Origin allowlist

```ts
const ALLOWED_ORIGINS = new Set<string>([
  "https://godduimprint.com",
  "https://www.godduimprint.com",
  "http://localhost:3000",
  "http://localhost:3001",
]);

function isAllowedOrigin(request: Request): boolean {
  const origin = request.headers.get("origin") ?? request.headers.get("referer") ?? "";
  if (!origin) return false;  // Empty = non-browser client (curl, scripts, scrapers)
  try {
    return ALLOWED_ORIGINS.has(new URL(origin).origin);
  } catch {
    return false;
  }
}
```

**Critical:** empty Origin/Referer MUST return false. Modern browsers always set Origin on fetch POST. See [[../errors/api-origin-allowlist-accepts-empty-header]].

### Layer 2 — Content-Type guard

```ts
const contentType = request.headers.get("content-type") ?? "";
if (!contentType.toLowerCase().startsWith("application/json")) {
  return Response.json({ success: false, error: "Invalid content type" }, { status: 415 });
}
```

### Layer 3 — Rate limit (in-memory map, per-IP)

```ts
type RateRecord = { timestamps: number[] };
const rateStore = new Map<string, RateRecord>();
const RATE_WINDOW_MS = 10 * 60 * 1000;
const RATE_MAX = 5;

function rateLimit(ip: string): boolean {
  const now = Date.now();
  const rec = rateStore.get(ip) ?? { timestamps: [] };
  rec.timestamps = rec.timestamps.filter((t) => now - t < RATE_WINDOW_MS);
  if (rec.timestamps.length >= RATE_MAX) return false;
  rec.timestamps.push(now);
  rateStore.set(ip, rec);
  // Opportunistic cleanup when map grows
  if (rateStore.size > 100 && Math.random() < 0.01) {
    for (const [k, v] of rateStore.entries()) {
      if (v.timestamps.every((t) => now - t >= RATE_WINDOW_MS)) {
        rateStore.delete(k);
      }
    }
  }
  return true;
}

function getClientIp(request: Request): string {
  const xff = request.headers.get("x-forwarded-for");
  if (xff) return xff.split(",")[0]!.trim();
  return request.headers.get("x-real-ip") ?? "unknown";
}
```

**Trade-off:** in-memory limiter doesn't survive serverless cold starts. Per-instance, so effective limit at N warm Vercel instances is RATE_MAX × N rather than RATE_MAX. Adequate for pre-launch traffic; replace with Upstash Ratelimit + KV when scaling.

### Layer 4 — Zod schema (validates AND filters)

```ts
const Body = z.object({
  name: z.string().min(1).max(120),
  email: z.string().email().max(254),
  phone: z.string().max(40).optional(),
  company: z.string().max(160).optional(),
  message: z.string().min(1).max(5000),
  source: z.enum(["/contact", "/quiz", "/footer-newsletter", "/booking"]).optional(),
});
```

Caps field length BEFORE interpolation. Validates email format. Rejects malformed source enum values (prevents header injection via the email subject's `[${source}]` template).

### Layer 5 — Honeypot (BOTH client and server halves)

**Server:** check raw body BEFORE Zod parse so bot submissions with extra fields don't 400:

```ts
if (
  raw &&
  typeof raw === "object" &&
  "website" in raw &&
  typeof (raw as Record<string, unknown>).website === "string" &&
  ((raw as Record<string, string>).website ?? "").length > 0
) {
  return Response.json({ success: true, confirmation: `OK-${Date.now()}` });
}
```

Silent 200 — bot doesn't learn the trap is server-side gated.

**Client (ContactClient.tsx or equivalent — MUST ship in same commit, see [[../errors/honeypot-defense-incomplete-without-client-input]]):**

```tsx
const ContactSchema = z.object({
  // ...other fields
  website: z.string().max(0).optional(),
});

// In form defaultValues:
website: "",

// First form field, before Name input:
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

### Layer 6 — Control-char sanitizer (strips CRLF before interpolation)

```ts
function stripControlChars(s: string): string {
  return s.replace(/[\r\n\t\0]/g, " ").trim();
}

// Apply to every field before any email interpolation:
const name = stripControlChars(validated.name);
const email = stripControlChars(validated.email);
// ...etc
```

Prevents header injection (e.g., `name = "Attacker\r\nBcc: many@victims.com"` corrupting the subject header).

### Layer 7 — Safe-name for auto-reply greeting

```ts
function safeName(s: string): string {
  return stripControlChars(s)
    .replace(/[^a-zA-Z0-9 '\-\.]/g, "")
    .slice(0, 120);
}

// In auto-reply:
const greetingName = safeName(name) || "there";
text: `Hi ${greetingName},\n\n...`,
```

The auto-reply sends FROM your verified domain TO the lead's email. Without sanitization, an attacker-controlled `name` field becomes a phishing payload signed by your DKIM. Stripping to alphanumeric + apostrophe + hyphen + period preserves legitimate names ("Mary O'Brien-Smith", "J. Edgar Hoover") while defanging payloads.

### Layer 8 — Independent try/catch (owner notification vs auto-reply)

```ts
// Owner notification (load-bearing — failure → 502)
try {
  await resend.emails.send({ from, to: ownerEmail, replyTo: email, ... });
} catch {
  console.error("[CONTACT] Owner notification failed");
  return Response.json({ success: false, error: "..." }, { status: 502 });
}

// Auto-reply (courtesy — failure must NOT 502)
try {
  await resend.emails.send({ from, to: email, replyTo: ownerEmail, ... });
} catch {
  console.warn("[CONTACT] Auto-reply failed; owner notification already succeeded.");
}

return Response.json({ success: true, confirmation: `LEAD-${Date.now()}` });
```

A flaky auto-reply must never 502 the API and lose the owner notification (lead). The owner email is load-bearing; the auto-reply is decorative UX.

## Key Rules
- **Every layer is mandatory.** Skipping any one creates an exploitable gap. Goddu's run-1 had ZERO layers; run-1 verifier surfaced 5 security BUGs in the route.
- **Both halves of honeypot must ship together.** Server check without client input = dead code defense. See [[../errors/honeypot-defense-incomplete-without-client-input]].
- **In-memory rate limiter is a v1 fallback.** Production hardening: replace with Upstash Ratelimit + KV via `@upstash/ratelimit` + `@upstash/redis`. Document the swap in the route's header JSDoc.
- **CAPTCHA is layer 9 (deferred).** Cloudflare Turnstile or hCaptcha adds human verification. Recommended before public launch for any client with non-trivial inbound volume. Phase 2 hardening.
- **Pattern #44 (replyTo discipline) still applies.** Owner notification `replyTo` = lead's email; auto-reply `replyTo` = owner's email. The defense-in-depth bundle does NOT replace replyTo correctness.

## Reuse Condition
Every Optimus client build. Apply to:
- `/api/contact/route.ts` (mandatory — every build has a contact form)
- `/api/quiz/route.ts` (if quiz emails landing data — currently quiz doesn't, but if a future build does)
- `/api/newsletter/route.ts` (if newsletter signup)
- `/api/booking/*` (mostly handled by Calendly's own form, but any custom booking webhook)
- Any future custom webhook route that sends email from the client's verified domain

## Pre-launch-auditor SECTION 4 additions
Stage 1H pre-launch-auditor should grep `src/app/api/**/route.ts` for:
- `resend.emails.send` calls WITHOUT a `rateLimit(` call earlier in the handler → FAIL
- `Body.safeParse(` or equivalent Zod parse on the request body → FAIL if missing
- `stripControlChars(` on every field that gets interpolated into email subject/text → FAIL if missing
- `isAllowedOrigin(` call → FAIL if missing
- Server-side honeypot check (`website.length > 0`) WITHOUT matching client-side hidden input in the corresponding form component → FAIL

## Related
- Error [[../errors/api-origin-allowlist-accepts-empty-header]] — empty-Origin gap
- Error [[../errors/honeypot-defense-incomplete-without-client-input]] — half-shipped honeypot
- Pattern #44 (vault build-log) — Resend replyTo discipline (CAN-SPAM)
- Pattern [[iterate-to-clean-n-run-review]] — caught all 3 of this pattern's birth-defect bugs
- Pattern [[stage-1j-pre-launch-gate]] — the gate that catches misses of this pattern
