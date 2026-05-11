# Pattern #69 — Seeded demo-mode for third-party APIs

**First shipped:** Ead Financial Step 3 (`/api/contact` Resend integration), 2026-05-09 commit `97739f8`.
**Generalized:** Ead Financial Step 6 (Calendly v2 booking integration), 2026-05-11 commit `36780a8`.
**Status:** VALIDATED at scale across 2 distinct third-party integrations. Reuse on every Optimus build that wraps a paid third-party API.
**Category:** Architecture / Demo Discipline / API Integration

---

## Why this pattern exists

Optimus builds ship to demo before clients have signed up for the third-party services the build depends on. Calendly, Resend, Stripe, Printful, fal.ai, OpenAI — every one of them has a "no-key state" that, if not handled, makes the demo break. A broken demo loses the sale. A demo that needs the salesperson to say "this part will work after you sign up" loses the sale slower but loses it the same way.

Every third-party integration has THREE failure modes that Pattern #69 addresses:
1. **No API key configured yet** (most common during build → demo phase)
2. **Free-tier limits** (Calendly Scheduling API requires paid plan, Stripe webhooks require account verification, Resend has volume caps, etc.)
3. **Transient network failures** (rate limits, brief outages, DNS hiccups during a demo)

A demo that breaks on any of these reads as "the build is half-finished." A demo that smoothly degrades to plausible-looking seeded data reads as "this is what you'll see in production." The pattern below makes the second option the default.

---

## The three-way contract

The pattern has three interlocking layers that all MUST hold:

### Layer 1 — Seeded fallback in the API route when env key is blank

```ts
// /api/calendly/slots/route.ts (illustrative)
export async function GET(request: NextRequest) {
  const params = parseAndValidateQuery(request);  // 400 on validation fail

  const apiKey = process.env.CALENDLY_API_KEY;  // LAZY READ inside handler
  const eventTypeUri = process.env.NEXT_PUBLIC_CALENDLY_EVENT_TYPE_URI;

  // Demo mode: env key blank OR upstream URI not configured
  if (!apiKey || !eventTypeUri) {
    console.info("[SLOTS DEMO]", { date: params.date, tier: params.tier, slotCount: seededSlots(params.date).length });
    return Response.json({
      date: params.date,
      timezone: "America/New_York",
      slots: seededSlots(params.date),
      demo: true,
    });
  }

  // Live mode: call the third-party API
  try {
    const liveSlots = await getCalendlyAvailability({ eventTypeUri, ...params });
    return Response.json({
      date: params.date,
      timezone: "America/New_York",
      slots: liveSlots,
      demo: false,
    });
  } catch (err) {
    // Fallback policy depends on route's risk profile — see Demo-Fallback Policy below
    if (isFreeTierError(err)) {
      console.warn("[SLOTS] Upstream paid-plan limit; falling back to demo");
      return Response.json({ ...seededResponse, demo: true });
    }
    return Response.json({ success: false, error: "Upstream error" }, { status: 502 });
  }
}
```

### Layer 2 — Identical response shape between demo and live

The seeded fallback returns the SAME response shape as the live path. Every field present in the live response is present in the seeded response (with plausible mock values). The only differentiator is the `demo: boolean` flag for orchestrator/dev observability.

```ts
// Both paths return:
{
  date: string;
  timezone: "America/New_York";
  slots: Array<{ startTime: string; label: string }>;
  demo: boolean;           // true in seeded path, false in live path
}
```

If demo and live response shapes diverge, the client has to branch on `demo`, which violates Layer 3 and creates a maintenance burden (every UI feature has to be implemented twice — once for demo, once for live).

### Layer 3 — Client renders identical UI regardless of `demo` flag

The client component reads `demo` ONLY for dev-time observability (logging) — never for branching the rendered UI. The success message a user sees after booking is the same string whether the booking was real or seeded:

```tsx
// BookingConfirmForm.tsx (illustrative)
const onSubmit = async (payload: BookingPayload) => {
  const res = await fetch("/api/calendly/book", { method: "POST", body: JSON.stringify(payload) });
  const data = await res.json();
  if (data.success) {
    // Success state IDENTICAL regardless of data.demo
    setPhase("success");
    return;
  }
  // Error handling
};
```

The user never sees "demo" copy. The user never sees a "this is a placeholder" badge. The build looks production-ready from day one.

---

## Demo-Fallback Policy varies by route's risk profile

A subtle refinement learned in Ead Financial Step 6: NOT every demo-fallback should be silent. The policy depends on the route's risk profile.

### Read-only routes — silent fallback on any non-200

`/api/calendly/slots` (read-only — fetching availability) can silently fall back to seeded data on any upstream non-200 (rate limit, transient network error, account suspension). The user sees a calendar with slots and clicks one. If the underlying availability data was seeded vs live, it doesn't change the user's behavior in the moment; the booking attempt itself will surface any deeper problem.

```ts
catch (err) {
  console.warn("[SLOTS] Upstream error; demo fallback");
  return Response.json({ ...seededResponse, demo: true });
}
```

### Conversion-critical routes — surface unexpected failures explicitly

`/api/calendly/book` (conversion-critical — persisting a booking) should fall back to demo ONLY on EXPECTED failure modes (blank API key, paid-plan 403). Any UNEXPECTED upstream failure (500, 401, account suspended) MUST surface as a 502 to the client, with the upstream status code in the response, so the practice owner knows real bookings are silently failing.

```ts
catch (err) {
  if (isFreeTierError(err) || !apiKey) {
    console.warn("[BOOKING] Paid-plan limit or blank key; demo fallback");
    return Response.json({ ...seededBookingResponse, demo: true });
  }
  // Surface unexpected failures — practice owner needs to know real bookings are failing
  console.error("[BOOKING] Unexpected upstream failure", err);
  return Response.json(
    { success: false, error: "Booking failed", upstreamStatus: (err as CalendlyError).status },
    { status: 502 }
  );
}
```

This split was Agent B's architectural call beyond the brief in Step 6. Defensible: silent fallback on conversion-critical routes hides production failures from the people who need to know about them.

**Decision rule:** if silent fallback could mask a production failure that has business consequences (lost bookings, lost orders, lost leads), the route is conversion-critical and unexpected failures MUST surface. If the route is read-only and the user's next action will surface deeper problems anyway, silent fallback is acceptable.

---

## Critical implementation details

### Lazy env-var reads inside handler functions

```ts
// CORRECT — env vars read inside the handler
export async function GET(request: NextRequest) {
  const apiKey = process.env.CALENDLY_API_KEY;  // ← inside function body
  // ...
}

// WRONG — env vars read at module top
const API_KEY = process.env.CALENDLY_API_KEY;   // ← at module top, captures undefined if env loads later
export async function GET(request: NextRequest) {
  // API_KEY may be stale
}
```

Module-top reads can capture undefined in some Next.js dev/prod transitions where env vars load AFTER module evaluation. Lazy reads inside the handler always reflect the current state at request time.

### Deterministic seeded data

Seeded data MUST be deterministic per input so demo runs reproduce. Hash-based selection from a fixed pool:

```ts
// lib/calendly-seeded.ts
function djb2Hash(str: string): number {
  let hash = 5381;
  for (let i = 0; i < str.length; i++) hash = ((hash << 5) + hash) + str.charCodeAt(i);
  return Math.abs(hash);
}

const SLOT_POOL = [9, 10, 11, 13, 14, 15, 16, 17];  // skips 12 lunch
export function seededSlots(date: string): Slot[] {
  const hash = djb2Hash(date);
  const count = countForDayOfWeek(date);  // weighted distribution
  const startIdx = hash % (SLOT_POOL.length - count);
  return SLOT_POOL.slice(startIdx, startIdx + count).map(/* ... */);
}
```

Same date always returns same slots. The user can refresh, navigate away, come back — the slot list is stable.

### Realistic distribution (not uniform)

Uniformly-distributed seeded data reads as suspicious during multi-input demo browsing. Real-world distributions are weighted:
- Calendar availability: heavier midweek (Tue-Thu), lighter Mon/Fri, empty weekends
- Product inventory: heavier popular SKUs, lighter long-tail
- Search results: ranked by relevance, not uniform

Match the seeded distribution to the real-world distribution where the integration matches it. Costs minutes to implement, makes the demo feel lived-in instead of mechanical.

### Console-info pattern for orchestrator/dev observability

Every demo-mode response logs a structured message:

```ts
console.info("[SLOTS DEMO]", { date, tier, slotCount });
console.info("[BOOKING DEMO]", validatedPayload);
```

The prefix (`[SERVICE_NAME DEMO]`) is grep-able. The structured payload is dev-tools-friendly. The orchestrator's Phase C verification reads the dev server stdout to confirm demo mode fired correctly.

### Client-side AbortController for in-flight request cancellation

Multi-step UIs that fetch on user interaction (date pick → slot fetch, search type → results fetch) MUST cancel in-flight requests when the user moves on:

```ts
const fetchAbortRef = useRef<AbortController | null>(null);

async function handleDateClick(dateStr: string) {
  fetchAbortRef.current?.abort();  // cancel any in-flight
  const controller = new AbortController();
  fetchAbortRef.current = controller;

  try {
    const res = await fetch(`/api/calendly/slots?date=${dateStr}`, { signal: controller.signal });
    const data = await res.json();
    // ...
  } catch (err) {
    if ((err as Error).name === "AbortError") return;  // Non-fatal — user moved on
    // Real error handling
  }
}
```

Without this, fast date clicks produce stale slot lists ("why does Tuesday's slot list show Wednesday's slots?") — a class of subtle race-condition bug that only surfaces on slow connections. The seeded path is fast, so the bug rarely surfaces in dev. In production with real Calendly latency, it surfaces constantly.

---

## DST-correct timezone handling for seeded availability

If the seeded data includes time-of-day labels in a specific timezone (e.g., "9:00 AM Eastern"), the corresponding ISO start_time MUST be the correct UTC equivalent for that day. Naive `new Date(year, month, day, hour, 0)` constructs in the SERVER's timezone — which on Vercel is UTC — and produces wrong UTC ISO strings.

Correct approach: probe-and-diff via `Intl.DateTimeFormat`:

```ts
function localTimeToUtcIso(year: number, month: number, day: number, hour: number, tz: string): string {
  // Construct a tentative Date in UTC, then probe the tz-local time it represents
  const tentative = new Date(Date.UTC(year, month, day, hour, 0));
  const tzLocalString = tentative.toLocaleString("en-US", { timeZone: tz, hour: "numeric", hour12: false });
  const tzLocalHour = parseInt(tzLocalString, 10);
  // Calculate offset and adjust
  const offsetHours = hour - tzLocalHour;
  return new Date(Date.UTC(year, month, day, hour + offsetHours, 0)).toISOString();
}
```

Test with a known DST-transition date to confirm. EDT/EST transitions are the most common gotcha for US-East-Coast practices.

---

## Compatibility notes

- **Compatible with Pattern #66** (Next 16 dynamic-route Promise params) — independent concerns. API routes can be static (GET/POST handlers without dynamic segments) or dynamic (`[slug]/route.ts`); both work with this pattern.
- **Compatible with Pattern #68** (AnimatePresence-with-direction) — multi-step UIs that fetch on transitions benefit from BOTH patterns: Pattern #68 for the transitions, Pattern #69 for the seeded fallback when the third-party isn't configured.
- **Recurs across Optimus stack:**
  - **Calendly** — booking (Step 6)
  - **Resend** — contact form transactional email (Step 3)
  - **Stripe + Printful** — shop (Step 9 — pending, but the pattern applies: seeded products + seeded checkout response)
  - **fal.ai** — blog images (Stage 1G — different pattern actually since fal.ai is build-time, but the seeded-fallback discipline applies when generation fails)
  - **OpenAI / Anthropic** — Tier-2/3/4 agent products — both have "no-key" demo modes that should follow this pattern

---

## When NOT to use this pattern

- **Server-side-only operations with no UI surface** (cron jobs, webhook handlers receiving inbound events) — there's no demo to preserve, no client to fool. Either the integration works or it logs an error and moves on.
- **Hard-key-required integrations** where seeded fallback would mislead the user into thinking something worked when it didn't (e.g., authentication endpoints — never mock a successful auth in demo mode).
- **Build-time data fetches** (Next.js `generateStaticParams`, ISR fetches) — these run at build time, not request time. If the API key is missing at build time, fail the build loudly so the developer fixes it; don't ship seeded data into the production HTML.

---

## Failure modes if not followed

- **Demo breaks at the worst moment** — the prospect is excited, they click the calendar, "Network error" appears, the salesperson scrambles to explain. Lost sale.
- **Demo shows obviously fake data** — uniformly-distributed slots, generic placeholder copy ("Sample Product 1"), 1990s-era stock photos. Reads as "the build isn't finished." Lost sale slower but lost the same way.
- **Live mode silently runs in demo** — env vars set wrong but client UI doesn't expose it. Real bookings fail; the practice owner doesn't know for weeks. Pattern violation: demo flag should be observable in dev console at minimum.
- **Stale data from race conditions** — fast user interactions produce wrong-looking results. Class of bug that's invisible on local seeded data and surfaces only in production.

---

## Worked examples in production

- **Ead Financial `/api/contact/route.ts`** (commit `97739f8`) — Resend integration. When `RESEND_API_KEY` is blank, route logs `[CONTACT FORM DEMO]` with full validated payload + returns `{ success: true, demo: true }`. Client renders identical "Thanks. We'll be in touch within one business day." regardless. (Step 3 — first instance of the pattern in this codebase.)
- **Ead Financial `/api/calendly/slots/route.ts` + `/api/calendly/book/route.ts`** (commit `36780a8`) — Calendly v2 integration. `/slots` silent fallback on any error (read-only). `/book` silent fallback only on blank key + 403 (paid-plan); other unexpected failures surfaced as 502 (conversion-critical). Day-of-week-weighted seeded slot counts. AbortController on date-click slot fetch. DST-correct UTC ISO conversion. (Step 6 — generalized the pattern + added the conversion-critical refinement.)

---

## Why this pattern compounds across the build

The first integration costs ~3 hours to implement properly with the seeded fallback path. The second integration (using this pattern as reference) costs ~1 hour. The third costs ~30 minutes. The pattern compounds because:

- The seeded data shape is predictable per integration type (calendar availability, product list, transactional email response, etc.)
- The route handler structure is identical (lazy env read → branch on key → seeded vs live → identical response shape)
- The client component never branches on demo
- The orchestrator's Phase C verification reuses the same `[SERVICE_NAME DEMO]` log pattern

Step 9's shop agent should reference this pattern doc directly for Stripe + Printful integration, saving ~2 hours of pattern re-derivation.
