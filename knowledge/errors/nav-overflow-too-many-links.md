# Error: Nav Overflow — Too Many Links
**Project:** Enchanted Madison
**Date:** March 2026
**Phase:** Phase 2 (Page build)

---

## Problem
Navigation bar broke the layout and required a full redesign mid-build. The site had 6+ nav items which overflowed on desktop and completely broke on mobile.

## Root Cause
No rule existed for when to split navigation into primary + dropdown. The nav was built with all links at the top level because there was no architecture decision made upfront.

## Solution
Split navigation: maximum 3 conversion-critical links in primary nav + remaining links in a "More" dropdown.

Primary nav items (conversion-critical only):
- The booking/reservation action
- The main services/offerings page
- Contact

Everything else goes under dropdown: About, Blog, FAQ, etc.

## Prevention
Rule added to `website-build-template.md` Nav section:
> If total nav links > 4: primary nav = max 3 items + "More" dropdown. Never let nav overflow or wrap at 390px.

## Related
- [[patterns/nav-architecture]] (if created)
- See website-build-template.md → Navigation → Nav Link Count Rule
