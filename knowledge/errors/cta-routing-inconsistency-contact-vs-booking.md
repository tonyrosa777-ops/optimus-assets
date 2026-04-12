# Error: CTA Routing Inconsistency — /contact vs /booking
**Project:** JCM Graphics
**Date:** 2026-04-12
**Phase:** Post-sweep polish

## Problem
Primary CTA buttons across the site ("Get a Free Quote", "Request a Quote") were inconsistently routed — some pointed to `/contact`, others to `/booking`. Two separate commits were needed to audit and fix all instances site-wide.

## Root Cause
Multiple agents built pages in parallel during the sweep. Each agent made independent CTA routing decisions. Some defaulted to `/contact` (the form page), others to `/booking` (the calendar/quote request page). No single source of truth for CTA destinations existed in site.ts at build time.

## Solution
1. Audited every CTA button site-wide
2. Enforced hierarchy: primary CTA always routes to `/booking`, secondary CTA always routes to `/quiz`
3. `/contact` is for the contact form — never the primary conversion CTA

Commits:
- `fix(cta): route all "Get a Free Quote" buttons to /booking not /contact`
- `fix(cta): enforce booking/quiz CTA hierarchy site-wide`

## Prevention
- Define CTA routing hierarchy in site.ts as explicit constants: `PRIMARY_CTA_HREF = '/booking'`, `SECONDARY_CTA_HREF = '/quiz'`
- Add to agent briefings: "Primary CTA → /booking, Secondary CTA → /quiz, /contact is NOT a CTA destination"
- Add to pre-launch auditor: verify all primary CTA hrefs point to /booking, not /contact

## Related
- CLAUDE.md Hero Architecture Rule already specifies secondary CTA = /quiz
- This error extends that rule to ALL pages, not just the hero
- Error #3 (placeholder CTA accepted as complete) is adjacent — both are CTA quality gates
