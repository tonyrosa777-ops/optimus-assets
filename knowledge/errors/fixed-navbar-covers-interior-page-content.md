# Error: Fixed Navbar Covers Interior Page Content
**Project:** JCM Graphics
**Date:** 2026-04-12
**Phase:** Post-sweep polish

## Problem
Interior pages (services, about, blog, etc.) had their top content hidden behind the fixed-position navbar. The hero page was fine because it's full-viewport, but every other page started its content at y=0, directly under the opaque nav bar.

## Root Cause
The `<Header>` component uses `position: fixed` (or `sticky` with top-0) to stay visible on scroll. Interior page content starts at the top of the document flow — the fixed nav sits on top of it. No global offset was applied to the `<main>` content area.

## Solution
Added a global `nav-height` offset to the layout so all interior pages clear the fixed navbar. Applied as padding-top or margin-top on the main content wrapper, using the same height value as the navbar.

Commit: `fix(layout): add global nav-height offset so interior pages clear fixed navbar`

## Prevention
- Add `pt-[var(--nav-height)]` or equivalent to the `<main>` element in `layout.tsx` during scaffold phase — not as a polish fix
- Include in `website-build-template.md` scaffold checklist: "main content clears fixed nav"
- The hero section is exempt (full-viewport) but every other page needs the offset

## Related
- This is invisible during hero-only development — only surfaces when interior pages are built and viewed in browser
