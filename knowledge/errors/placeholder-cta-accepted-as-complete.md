# Error: Placeholder CTA Accepted as Phase-Complete
**Project:** Enchanted Madison
**Date:** March 2026
**Phase:** Phase 2 (Conversion flows)

---

## Problem
A static "Online booking coming soon" box was built and the phase was marked complete. The client had a booking tool (Lodgify) that needed to be embedded — the placeholder created a conversion gap that had to be caught and fixed later with an explicit request.

## Root Cause
No rule required an interactive placeholder before a phase sign-off. "Something is better than nothing" thinking let a non-functional CTA pass as done.

## Solution
Every primary conversion flow must have a demo-mode interactive component before a phase is closed:
- Booking → embedded calendar widget (even if not connected) or Lodgify/Acuity iframe
- Inquiry → react-hook-form with success state
- Purchase → product page with Add to Cart (even if Stripe not wired)

If the real tool isn't ready, build a convincing placeholder that mimics the interaction.

## Prevention
Standing Order #13 added to `CLAUDE.md`:
> Placeholder CTAs are blockers, not completions. Every primary conversion flow must have a demo-mode interactive component before the phase is marked complete. Flag it and propose the component before closing.

## Related
- See CLAUDE.md Standing Order #13
- website-build-template.md → Conversion Flow patterns
