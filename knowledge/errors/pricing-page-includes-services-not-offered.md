# Error: Pricing page includes services Optimus doesn't offer
**Project:** Witt's Restoration LLC
**Date:** 2026-04-12
**Phase:** Post-sweep retro fixes

## Problem
The pricing page tier cards and comparison chart included "Google-ready in 60-90 days" and other Google-referencing features. Optimus does not offer Google services (Google Business Profile optimization, Google Ads, Google Analytics setup). The pricing page also used internal/technical feature names ("Blog Architecture," "Interactive Quiz," "Inline Booking Calendar") instead of client-facing names.

## Root Cause
Pricing data in site.ts was written by a content agent that pulled from the template's generic feature list without cross-referencing what Optimus actually offers. Technical names leaked from the build template into client-facing copy.

## Solution
1. Removed all Google-referencing features. Changed "Google-ready in 60-90 days" → "Search-ready in 60-90 days"
2. Renamed all features to client-facing names: Lead-Capture Quiz, Automated Booking Calendar, Professional Blog, Testimonials Showcase, Photo Gallery, Branded Merch Shop

## Prevention
- CLAUDE.md already states "Never include Google Business Profile optimization" — enforce in content-writer agent briefing
- Pricing feature names should be reviewed against a client-facing naming checklist before phase sign-off
- Add to pre-launch auditor: grep pricing page for "Google" — any match is a FAIL

## Related
- CLAUDE.md: "Never include on pricing page" section
