---
tags: [offering/website-dev, status/in-development]
---

# Optimus Marketing Site

This folder tracks Optimus's own marketing site. The proof that Optimus delivers what it sells.

## Build approach

Built from the same foundation as every Optimus client site. Same `[[../../website-build-template]]`, same `[[../../CLAUDE]]` rules, same agent stack, same Phase 1-9 sweep, same multi-breakpoint browser audit before launch.

Optimus is its first own customer. If the workflow cannot ship Optimus's own site at luxury-modern-2026-conversion quality, it cannot ship a client's. This site is a forcing function.

## Status

| Field | Value |
|---|---|
| Build status | Not yet started |
| Repo | TBD (likely `c:\Projects\optimus-website\` once scaffolded) |
| Domain | TBD |
| Deployed URL | TBD |
| Booking engine | Calendly via custom `BookingCalendar` component (per Always-Built Features Rule) |
| Target launch | TBD |

## Cross-references

- Content direction: [[content-strategy]]
- Brand identity (drives design tokens): [[../brand/README]]
- Chat assistant deployed on this site: [[../ai-agents/chat-assistant/README]]
- Build template: `[[../../website-build-template]]`
- Project rules: `[[../../CLAUDE]]`

## Open decisions

- Domain selection
- Whether to skip the sales-tool `/pricing` page entirely (Optimus's pricing is real, not a sales tool, so the deletion gate in pre-launch-auditor does not apply the same way)
- Hero canvas concept selection (will run the Hero Architecture Rule's 10-concepts-then-critic process when the build kicks off)
