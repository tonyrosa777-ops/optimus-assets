# Collaborative Insights — Project Retrospective

**Type:** Spiritual consulting and ascension guidance
**Location:** Texas (online delivery via Zoom)
**Client:** Lesley Ledbetter
**Completed:** 2026-04-20 (post-sale polish + delivery pass)
**Build sessions (approx):** 3 — initial demo build (commit 83176ee, pre-sale), domain/email/booking integrations (2026-04-14), post-sale polish + booking iteration (2026-04-20)

---

## What Went Well
- Sale closed at **Pro tier** ($3,000). Client chose Pro after demo review.
- Resend wiring for contact + newsletter landed cleanly in one commit (0975dc4); all API routes Zod-validated with HTML-escaped user input and 4-state UI (idle/loading/success/error).
- Calendly v1 integration (react-calendly `InlineWidget`) wired in <1 session (ef8cd85) with session selector for 2 event types.
- Blog images auto-generated via fal.ai Flux Pro v1.1 (dark/gold Rembrandt lighting, no stock spiritual imagery) — all 9 articles shipped with hero JPGs in `/public/images/blog/` (commit 7b61c23). Pattern #41 (fal.ai reusable blog image generator) + Pattern #40 (blog index above-fold) both applied cleanly.
- Brand canvas hero (sacred-geometry eye, 24 orbital particles in IDLE, 60 stream particles in STREAM, concentric sacred geometry rings) delivered the luxury dark-brand feel the design system promised.
- Post-sale cleanup was methodical: pricing page archived to `pricing-packages.md` (not deleted from history), shop feature-flagged (not deleted — reversible if client upgrades to Premium), Leslie's headshot integrated once the asset arrived.
- **Final booking UX nailed the light-stage pattern** — tonal break from dark hero to ivory booking section reads as intentional "step into the light" moment, and the Calendly widget is finally readable.

---

## What Didn't

| # | Gap | Fix Applied |
|---|-----|-------------|
| 1 | Calendly dark-mode `pageSettings.textColor` ignored by Calendly's internal CSS — secondary text elements (date headers, month label, weekday labels, time-zone label, footer links) all rendered in un-readable low-contrast blue-gray regardless of the hex passed | Abandoned dark-mode Calendly. Switched to light theme in an ivory `#F5F0EB` stage section. See [[errors/calendly-dark-mode-textcolor-incomplete]] + [[patterns/calendly-light-stage-section]] |
| 2 | Native date/time pre-picker rebuild caused double-entry conversion killer — user selected date+time in our on-brand UI, then had to select date+time AGAIN inside the Calendly iframe because URL params pre-fill date only, not time | Reverted the native picker. Deleted `src/lib/calendly.ts`, `api/calendly/slots/route.ts`, `components/BookingCalendar.tsx`. Documented as [[errors/native-picker-plus-calendly-double-entry]] + [[patterns/conversion-first-friction-audit]]. User feedback: *"the main point of the site is to convert"* — saved to project memory as feedback rule |
| 3 | Homepage `AboutTeaser` shipped with 🪖 emoji + "Professional headshot pending" placeholder, never wired to `about.photo`; homepage `BlogPreview` rendered 📖 emoji blocks even though matching blog hero JPGs already existed in `/public/images/blog/` for the same slugs | Wired `about.photo` into AboutTeaser, swapped the emoji blocks in BlogPreview for `<img src={/images/blog/${slug}.jpg}>`, made cards full-card clickable links to each post (commit 9c5d8d1) |
| 4 | `AboutClient.tsx` guard condition `about.photo !== "/images/leslie-headshot.jpg"` was designed to show the placeholder when `about.photo` matched the default sentinel path — but when the real photo was uploaded AT that exact path, the same condition silently kept the placeholder showing | Simplified the render: always show `<img src={about.photo}>`. The sentinel-path-equals-target-path anti-pattern would have shipped to launch without this catch |
| 5 | Client's actual photo file was found at `website/About-photo.png` (repo root, capital-A name) instead of `website/public/images/…` — the "asset in wrong location" class from Error #5 recurred, found only because the user pointed it out | Moved to `website/public/images/leslie-headshot.png`, updated `site.ts`, integrated. Pre-launch auditor should grep repo root for image extensions as part of Phase 13 checklist |
| 6 | Booking widget went through **6 iterations** before landing the light-stage fix (Calendly dark → textColor FFFFFF → textColor gold → native pre-picker redirect → native pre-picker inline iframe phase-2 → revert → final light-stage). Would have been 1 iteration if the Calendly dark-mode limitation was known going in | Patterns #52 + #54 added to vault. Default Calendly theme for future Optimus builds is now "light in a stage section" — dark mode requires an explicit opt-in and contrast override plan |
| 7 | GitHub remote URL case drift (`leslie-ledbetter` → `Leslie-Ledbetter`) caused user to perceive pushes weren't landing. Pushes worked because GitHub auto-redirects, but Vercel confirmations required MCP to verify | Fixed local remote URL casing. Workflow: when GitHub flags `This repository moved` during push, update local remote same day — don't let the drift accumulate |
| 8 | `progress.md` last updated 2026-04-09, but three subsequent sessions (domain update, Calendly integration, Resend wiring, pricing/shop cleanup, photo, booking rework) shipped commits without progress.md updates | No fix applied to progress.md this session (out of scope); but flagging: the after-every-subtask progress.md rule (CLAUDE.md) is being skipped on polish passes. Orchestrator should enforce it or the rule should be amended to "after every commit that ships to main" |

---

## Tools Introduced This Build
None new — all existing toolkit:
- `react-calendly` (Danielle Thompson baseline)
- `resend` (Enchanted Madison baseline)
- fal.ai Flux Pro v1.1 (Andrea Abella baseline)
- Vercel MCP (used this session to verify production deploys — useful pattern for any time the user asks "did my push land?")

---

## Changes Made to Toolkit

| # | Change | Location |
|---|--------|----------|
| 1 | Added Error #52 — Calendly dark-mode textColor incomplete | build-log.md + `errors/calendly-dark-mode-textcolor-incomplete.md` |
| 2 | Added Error #53 — native picker + Calendly = double entry | build-log.md + `errors/native-picker-plus-calendly-double-entry.md` |
| 3 | Added Pattern #52 — Calendly light-stage section (default Calendly theme for dark-brand builds) | build-log.md + `patterns/calendly-light-stage-section.md` |
| 4 | Added Pattern #53 — Feature-flag tier-gated features (shop scaffolding stays in repo behind `NEXT_PUBLIC_SHOP_ENABLED`) | build-log.md + `patterns/feature-flag-tier-gated-features.md` |
| 5 | Added Pattern #54 — Conversion-first friction audit (mandatory pre-build step for booking/signup/checkout/quiz changes) | build-log.md + `patterns/conversion-first-friction-audit.md` |
| 6 | Saved project-level feedback memory — `feedback_conversion_first.md` in the project's auto-memory directory | `C:/Users/Anthony/.claude/projects/c--Projects-Leslie-Ledbetter/memory/` |

Workflow gap recommendations for CLAUDE.md / website-build-template.md / pre-launch-auditor.md listed in Phase 6 below.
