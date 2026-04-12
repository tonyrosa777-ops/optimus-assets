# Gray Method Training — Project Retrospective

**Type:** Women's personal training / online fitness coaching
**Client:** Adam Gray, Coach
**Completed:** Apr 2026 (initial build Mar 29, 2026; follow-up + polish sessions Apr 2026; conversion pass + audit Apr 10, 2026)
**Build sessions:** 4 sessions — initial (28 commits, 2026-03-29) + follow-up (8 commits) + polish (7 commits) + conversion pass + multi-breakpoint audit (2 commits, 2026-04-10)
**Live URL:** gray-method-training.vercel.app (pre-launch — DNS not yet pointed)

---

## What Went Well

- **Single-day full build** — Phases 0–9 completed in one session (28 commits). The pre-built animation library, Sanity integration, and site.ts architecture from prior builds made this possible
- **Hero particle system** — Canvas particles (stars + embers + glimmers) + CSS breathing orbs + text-shimmer headline delivered a luxury opening with no video asset required. Client approved immediately
- **Progress.md discipline** — Session log updated after every phase. Every fix, architectural decision, and blocker documented in real time
- **Commerce migration mid-build** — Recognized that the initial Snipcart implementation was transitional after seeing the Andrea Abella Marie architecture; made the call to migrate to Stripe + custom cart mid-Phase 8. Clean migration with reference repo available
- **All copy in `src/data/site.ts`** — Zero hardcoded strings in JSX. Client can hand this to any developer without hunting through components
- **Pricing page as sales tool** — ROI calculator + comparison chart built and deployed for the sales conversation. Env-gated for pre-launch removal
- **Quiz as conversion infrastructure** — Multi-step quiz routes visitors to right offer; email gate removed in follow-up session to eliminate friction; Calendly inline on results screen captures booking intent while motivation is high
- **Behold.so decision** — When user pushed back on the Instagram Graph API + Upstash + Vercel Cron architecture as too complex, quickly identified and switched to Behold.so (1 env var, no developer app, no cron jobs). The managed service was the right call for a small coaching business
- **LogoParticles hybrid reveal** — dramatic phased canvas animation (converge → hold → explode → idle) for Adam's hand-made gold badge logo, with continuous energy effects (rotating ring pulse, shimmer sweep, sparkle bursts) that dive behind the banner text. Reusable pattern for any future client with a distinctive logo
- **Blog CTA swap** — removed newsletter signup from every blog post, replaced with quiz + booking CTA. Matches Adam's funnel (he sells 1:1 coaching, not drip content)

---

## What Didn't

| # | Gap | Fix Applied |
|---|-----|-------------|
| 1 | `once: true` in react-intersection-observer doesn't work — silently ignored; animations re-fired on every scroll | Fixed to `triggerOnce: true` across all animation primitives in Phase 2 |
| 2 | `fs` / `path` imports in `PhotoPlaceholder.tsx` caused Turbopack client bundle error | Replaced with `useState + onError` fallback — no server modules in client files |
| 3 | CLAUDE.md Rule 4 references Snipcart skill as mandatory, but Snipcart was replaced entirely in Phase 8 | Rule not updated during build — workflow gap, needs toolkit update |
| 4 | Phase 10 SEO (JSON-LD, sitemap, alt text) and Phase 11 QA not complete at project close | Still pending — Adam needs to run the pre-launch checklist before going live |
| 5 | Instagram Graph API + Upstash Redis + Vercel Cron — built entire token refresh infrastructure (1 cron, 1 Redis store, 1 API route) then removed it when Behold.so was identified as the simpler solution | Replaced with single Behold env var; Upstash/cron code committed and removed in same session |
| 6 | Quiz shipped with email gate — added friction before results were shown; user explicitly requested removal to maximize instant-gratification conversion | Removed email gate; Q8 auto-advances to results; Calendly at the end captures email during booking |
| 7 | Behold API bugs — 3 compounding issues: `sizes.*` nesting mismatch, double URL construction, CDN priority order reversed | Fixed across 3 sequential commits; real Behold JSON payload analysis was key |
| 8 | `PhotoPlaceholder` `onError` fired on production even with real headshot in place — client couldn't see his own photo on the live site | Replaced with direct `next/image`; scaffold components must not remain after real assets arrive |
| 9 | `NEXT_PUBLIC_SITE_URL` set without `https://` protocol in .env.local — affected OG tags and structured data | Fixed in .env.local; flagged for Vercel env var update |
| 10 | LogoParticles v1 was fuzzy — tried to render the subtitle "ONLINE HEALTH & FITNESS" as a particle grid, which is physically impossible to antialias | Switched to hybrid: particles for assembly only, `drawImage()` crossfade for crisp idle state |
| 11 | Energy overlays (ring pulse, shimmer) washed out the banner text during idle — additive blend modes pushed gold pixels toward white | Added `ctx.clip("evenodd")` exclusion around the text band; tuned bounds 3 times (0.68 → 0.74 → 0.80) before the subtitle was fully protected |
| 12 | Text exclusion bounds took 3 iterations to land — initial estimate of y=0.68 was too shallow for circular badge logos with subtitles; subtitle actually extends to ~0.78 | Final working bounds: y ∈ [0.34, 0.80] for the full banner + subtitle text band |
| 13 | Testimonials shipped with PhotoPlaceholder avatar circles — clients never submitted photos and the initials fallback looked unfinished | Removed the Avatar component entirely. Each card now ends with name + context only |
| 14 | Hero H1 repeated brand name 3x above the fold — "Gray Method" in nav text + H1 ("Gray Method Online Health & Fitness") + giant logo badge on right. H1 burned on brand instead of visitor value | Rewrote H1 to Adam's mission statement ("Stronger. / More energized. / Finally free from the diet cycle."), moved audience qualifier to eyebrow ("Online Coaching for Busy Women"), kept signature tagline. Swapped nav text wordmark for image-only logo since badge already contains the wordmark |
| 15 | `--text-display: 4.5rem` hardcoded in globals.css — the new H1 "More energized." orphaned "More" on its own line at 390px. Typecheck and desktop both clean, only visible bug | Swapped to `clamp(2.5rem, 8vw, 4.5rem)` in both the CSS variable AND matching `@utility` class; one change fixes 11 other components too. Desktop unchanged (clamp hits ceiling ~900px viewport) |
| 16 | Hero H1 was hardcoded in JSX as individual spans — violated the project's own CLAUDE.md rule "no hardcoded copy in JSX" | Moved headline to `site.ts` as `headlineLines` array; JSX now iterates and applies shimmer to `[2]` climax line |
| 17 | No pre-ship visual verification was happening anywhere in the workflow — typecheck passed, tests passed, desktop looked fine. The H1 mobile wrap only surfaced because I manually ran the dev server and Playwright against 375/390/428/1440 as a one-off | Introduced the end-of-build multi-breakpoint live-browser audit as a mandatory workflow step. See [[patterns/end-of-build-multi-breakpoint-browser-audit]] |

---

## Tools Introduced This Build

- **Resend** — email for contact form submissions (established in Danielle Thompson but now standard)
- **Stripe + Printful custom cart** — full Stripe checkout + Printful variant API (already in vault from Andrea Abella Marie; applied fresh to a new build)
- **`react-intersection-observer`** — `triggerOnce` API confirmed (not `once`)
- **`website-build-template.md`** — new project-close deliverable created from this build: reusable architecture doc covering hero, animations, sections, quiz, blog, shop, pricing page pattern
- **Behold.so** — managed Instagram feed service; replaces entire Graph API + Redis token store + cron system with one env var; auto-refreshes token; Behold CDN URLs are stable (no expiry); free plan available

---

## Changes Made to Toolkit

1. **Add error entry**: `react-intersection-observer-triggeronc-not-once` — `triggerOnce` not `once`
2. **Add pattern entry**: `dual-hero-animation-canvas-orbs` — canvas particles + CSS orbs as luxury hero standard
3. **Add pattern entry**: `roi-calculator-dev-only-pricing-tool` — env-gated ROI tool for sales phase
4. **Add pattern entry**: `quiz-multistep-lead-capture-program-recommendation` — 3-step quiz → program CTA
5. **Update CLAUDE.md Rule 4** — Snipcart reference should be updated to Stripe + Printful custom cart architecture
6. **Consider adding `website-build-template.md` to end-to-end-workflow.md** as a standard project-close deliverable
7. **Add error entry** (follow-up session): `behold-api-integration-pitfalls` — 3 compounding Behold bugs
8. **Add error entry** (follow-up session): `photo-placeholder-onerror-fires` — scaffold must be removed when real asset arrives
9. **Flag workflow gap**: `client-launch-checklist.md` needs `https://` protocol check on `NEXT_PUBLIC_SITE_URL`
10. **Flag workflow gap**: CLAUDE.md Instagram Feed Rules mention Graph API — should recommend Behold.so for small clients
11. **Add error entry** (polish session): `canvas-particle-grid-cannot-render-text` — particle grids can't antialias text, hybrid rendering required
12. **Add error entry** (polish session): `canvas-effect-overlay-washes-out-text` — evenodd clip to protect text bands
13. **Add pattern entry** (polish session): `logo-particles-phased-reveal` — reusable LogoParticles component
14. **Add pattern entry** (polish session): `blog-cta-quiz-book-over-newsletter` — conversion CTA replacement for service businesses with a quiz
15. **Add error entry** (conversion pass session): `fixed-rem-display-font-size-breaks-mobile` — clamp() instead of fixed rem on all display type
16. **Add pattern entry** (conversion pass session): `end-of-build-multi-breakpoint-browser-audit` — MANDATORY pre-ship workflow step. Flag as missing from every prior build
17. **Add pattern entry** (conversion pass session): `clamp-responsive-type-scale` — globals.css display font sizes must clamp, bake into Phase 1 project setup
18. **Add pattern entry** (conversion pass session): `conversion-first-hero-headline` — audit brand-name repetition above the fold; H1 carries outcome not brand
19. **Flag workflow gap (major)**: no Phase / step in any workflow file forced a live browser audit. Every prior Optimus build shipped without multi-breakpoint visual verification. Retroactively the audit would have caught build-log errors #16 (rate badge overflow), #25 (mobile hero text mid-screen), #29 (hero text invisible on background), #34 (photo placeholder fires in prod). Add as mandatory final step.
    **RESOLVED 2026-04-10:** Baked into the toolkit across five files — CLAUDE.md (new Visual QA Rule), build-checklist.md (new Phase 1 step 14 before Phase 2 Launch), project-prime.md (new Stage 1I after Stage 1H Pre-Launch Audit, phase overview table updated to 16 phases), website-build-template.md (new Visual QA subsection in Checklist: Before Launch), and pre-launch-auditor.md (Section 8 mobile check changed from WARN-manual to DEFERRED-to-Section-11, new Section 11 handoff with BLOCKED-ON-SECTION-11 signal). Full playbook at [[patterns/end-of-build-multi-breakpoint-browser-audit]]. Client Revision Pass in both build-checklist.md and project-prime.md now re-runs the audit after every revision batch before re-sending to client.
20. **Flag workflow gap**: `website-build-template.md` Phase 1 (globals.css setup) should mandate clamp() for all display type sizes — not a retrofit

---

## Notes

- The outer planning repo (`c:\Projects\Gray-Method-Training`) holds brand voice, competitive intel, design contract, and master prompt. The actual app lives in the git submodule (`gray-method-training/`). Both have their own `progress.md` — the outer one is a template that stays static; the inner one is the live log
- All 28 commits happened on 2026-03-29 with `tonyrose777-ops` + `claude` as contributors
- 21 Vercel deployments — production is green

See [[retrospectives/andrea-abella-marie]] for the Stripe + Printful commerce architecture this build drew from.
