# Error: Native date/time pre-picker + Calendly iframe = double entry kills conversion

**Project:** Collaborative Insights
**Date:** 2026-04-20
**Phase:** Phase 9 — Booking (attempted rebuild)

## Problem
After the Calendly iframe's dark-mode text-contrast issue (see [[errors/calendly-dark-mode-textcolor-incomplete]]), an attempt was made to "rebuild native booking UI" — a custom on-brand calendar picker built with site design tokens, with Calendly still handling the final form submission.

Two iterations were tried:

1. **Redirect version:** user picks date + time in native UI → click Confirm → opens Calendly scheduling page in a new tab with `?month=YYYY-MM&date=YYYY-MM-DD` params.
2. **Inline phase-2 version:** user picks date + time in native UI → same page swaps to an embedded Calendly iframe with the date deep-linked.

Both versions had the same fatal flaw: **the user had to pick the date and time again on the Calendly side** because Calendly's public URL params only pre-fill `date` and `month`, not the specific time slot. The user selects 2:00 PM on Thursday in our beautiful calendar, clicks Confirm, and then sees Calendly's own calendar with the same 7 time slots for the same date, where they must click 2:00 PM again.

On a conversion-critical page, doubling the commitment pattern (pick → pick again) is a hard conversion killer. It also confuses users ("did it not save my pick?").

## Root Cause
1. Calendly's documented URL query params for deep-linking cover `month` and `date` but **do not include a `time` or `start_time` param**. The only way to pre-select a specific time slot is via Calendly's internal, unofficial scheduling-service API that the widget itself uses — which is fragile and not a safe integration surface.
2. A custom "pre-picker" design was built before mapping out the full user journey through the third-party tool. The third-party limitation should have been a blocker for the design direction, not a footnote.

## Solution
Revert. Ship Calendly's iframe as the one and only booking UI (no pre-picker). The iframe collects date + time + name + email + phone in one place — one choice per field, no re-entry.

Pair it with [[patterns/calendly-light-stage-section]] (light theme in an ivory stage section) to solve the text-contrast issue without touching the iframe itself.

The reverted `BookingClient.tsx` kept session selector cards + a single Calendly iframe. The native-picker files (`src/lib/calendly.ts`, `src/app/api/calendly/slots/route.ts`, `src/components/BookingCalendar.tsx`) were deleted.

## Prevention
**Conversion-first friction audit BEFORE building any pre-picker, wizard, or multi-step UI on a booking/signup/checkout/quiz page.** Explicitly walk the full journey in the planning response:

1. List every field the user enters.
2. Mark any field the user enters twice with a 🚩.
3. Identify third-party tool limitations that force re-entry.
4. If any 🚩 exists and the tool can't be replaced, the pre-picker design is blocked — polish within the existing third-party UI instead.

For Calendly specifically: do not build pre-pickers. Either embed the iframe directly (light theme, stage section) or switch scheduler to a tool with a real booking API (Cal.com).

See [[patterns/conversion-first-friction-audit]].

## Related
- [[patterns/calendly-light-stage-section]] — the actual fix
- [[patterns/conversion-first-friction-audit]] — the preventative workflow rule
- [[errors/calendly-dark-mode-textcolor-incomplete]] — the problem that triggered the native rebuild attempt
