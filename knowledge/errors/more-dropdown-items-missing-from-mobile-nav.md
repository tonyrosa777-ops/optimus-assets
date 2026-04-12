# Error #38 — Desktop "More" Dropdown Items Missing from Mobile Nav Drawer

**Project:** JCM Graphics
**Date:** April 2026
**Severity:** User-facing — pages unreachable on mobile
**Caught by:** Human review of browser audit screenshots (NOT by the orchestrator running the audit)

## Problem

The Header component uses a `MORE_LABELS` Set to filter certain nav links (Gallery, FAQ, Shop) into a desktop-only "More" overflow dropdown. This prevents nav overflow when there are 10+ links.

The mobile nav drawer, however, renders links from two sources:
1. `navigation.links` array from site.ts (Services, Gallery, About, Testimonials, Blog, Contact)
2. Hardcoded links for Service Areas and Booking

Items in the `MORE_LABELS` Set were excluded from `navigation.links` on desktop (correct) but the mobile drawer never compensated by adding them back. Result: Shop and FAQ were completely unreachable on mobile.

## Root Cause

The "More" dropdown pattern (build-log pattern #27, introduced in Where2Junk) was designed for desktop only. When the mobile drawer was built, it iterated `navigation.links` and added a few hardcoded extras, but nobody checked whether the More-filtered items were accounted for.

## The Real Failure — Orchestrator Missed It During Audit

The multi-breakpoint browser audit (Stage 1I) captured a screenshot of the open mobile nav drawer (`verify-mobile-nav-open.png`). The screenshot clearly showed all nav links — and Shop was visibly absent. The orchestrator looked at the screenshot, verified the drawer opened and closed, checked console errors, and marked the audit PASSED.

**The orchestrator had the evidence in front of it and did not catch the missing link.**

This means the browser audit checklist needs a harder gate: not just "drawer opens, overlay is dark, X closes" but an explicit link-count verification step.

## Fix

Explicitly added every link from the More set (Shop, FAQ) as hardcoded `<Link>` elements in the mobile drawer section of Header.tsx.

## Prevention

Add this mandatory check to the Stage 1I browser audit playbook:

**Mobile nav drawer link verification (NEW — added after JCM Graphics):**
- After opening the mobile drawer and taking a screenshot, snapshot the drawer's accessibility tree
- Count the number of nav links in the drawer
- Compare against the known route list (from sitemap.ts or a mental count of all pages)
- If any route is missing from the mobile drawer, FAIL the audit
- Specifically: cross-check any desktop "More" dropdown items against mobile drawer links

Also: when using the More dropdown pattern on any future build, always add the same links to the mobile drawer in the same commit. The More pattern creates a desktop/mobile divergence that must be resolved at build time, not caught at audit time.
