# Pattern: Demo Booking Calendar with Hash-Based Seeded Availability
**Category:** Conversion / UX / Demo
**First used:** Where2 Junk — April 2026

## What
A fully interactive multi-step booking calendar widget that looks and feels live — with realistic available/limited/booked slot distribution — but requires zero backend. Uses a deterministic hash function so the same date always shows the same availability status (no flicker on re-render).

## When to Use
- Service business with Calendly/booking engine not yet configured
- Demo presentation requires an interactive calendar (not a placeholder)
- Client needs to show prospects "online booking" before API keys are set
- Any build where NEXT_PUBLIC_CALENDLY_URL is unset at demo time

## How

**Hash function (deterministic by date):**
```ts
function hash(d: Date): number {
  return (d.getFullYear() * 400 + d.getMonth() * 31 + d.getDate()) % 10;
}
```

**Availability mapping (makes weekends busiest — realistic):**
```ts
function getAvail(d: Date): Avail {
  const today = new Date(); today.setHours(0, 0, 0, 0);
  if (d < today) return 'past';
  if (d.getDay() === 0) return 'closed';         // Sundays always closed
  const h = hash(d);
  const dow = d.getDay();
  if (dow === 6) return h < 3 ? 'booked' : h < 6 ? 'limited' : 'available'; // Saturdays busiest
  return h < 2 ? 'booked' : h < 4 ? 'limited' : 'available';
}
```

**Time slot seeding:**
```ts
function getTimeSlots(d: Date): TimeSlot[] {
  const h = hash(d);
  return TIME_SLOTS.map((label, i) => ({
    label,
    avail: (h + i) % 5 === 0 ? 'booked' : (h + i) % 3 === 0 ? 'limited' : 'open',
  }));
}
```

**Dual-mode confirmation modal:**
```tsx
// When NEXT_PUBLIC_CALENDLY_URL is set → embed Calendly iframe
// When unset → show "Josh Is On It." branded demo confirmation
const hasCalendly = Boolean(process.env.NEXT_PUBLIC_CALENDLY_URL ?? '');
```

**Step flow (Where2 Junk used 4 steps):**
1. Calendar grid → pick date
2. Time slot picker → pick window
3. Service type selector → pick job type
4. Location picker → pick service area (or "Other" for out-of-area)

## Key Rules
1. The hash must be purely deterministic — no `Math.random()`, no `Date.now()` in availability calculation
2. Sundays always closed (opacity 0.25, non-clickable) — feels real for a service business
3. Saturdays intentionally busiest — creates urgency
4. When Calendly URL is set, the confirmation modal silently switches to Calendly iframe — zero code change needed at launch
5. The "Other" location chip reveals a text input: "Josh will reach out to confirm" — captures out-of-area leads without rejecting them

## Reuse Condition
Any service business build where the scheduling backend is not yet configured. Works for trades, cleaning, delivery, medical — any appointment-based business.

## Related
- [[patterns/calendly-inline-embed-brand-colors]] — the live Calendly integration this demo bridges to
- [[errors/placeholder-cta-accepted-as-complete]] — why this pattern exists (static placeholders are not acceptable)
