# Error: Duplicate CTA sections back-to-back on homepage
**Project:** Witt's Restoration LLC
**Date:** 2026-04-12
**Phase:** Post-sweep retro fixes

## Problem
The bottom of the homepage had two nearly identical CTA sections rendered back-to-back: BookingPreview ("Ready to Get Started?") and FinalCTA ("Ready to Get It Fixed?"). Same intent, same button targets, different words. Looked like a broken page with repeated content.

## Root Cause
Both sections were created by different agents during the parallel homepage build. BookingPreview was a booking calendar placeholder, FinalCTA was the closing CTA. Both independently chose similar headlines and CTA targets. No orchestrator check verified that adjacent sections had distinct purposes.

## Solution
Removed BookingPreview entirely. Kept FinalCTA as the single strong closing section. Adjusted background to maintain dark/light alternation.

## Prevention
- Homepage section rhythm map (already required by CLAUDE.md) should include a "purpose" column: each section must have a distinct conversion intent
- Pre-launch auditor should flag any two adjacent sections with similar headlines or identical CTA hrefs
- Agent briefings for homepage sections should include "check what the section above and below you does — don't duplicate intent"

## Related
- Error #41: CTA routing inconsistency (same category — CTA management)
- Pattern #8: homepage dark/light section rhythm
