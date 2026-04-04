# Gray Method Training — Project Retrospective

**Type:** Women's personal training / online fitness coaching
**Client:** Adam Gray, Coach
**Completed:** Apr 2026 (build shipped Mar 29, 2026 — 1 build day)
**Build sessions:** 1 continuous session (28 commits, all on 2026-03-29)
**Live URL:** gray-method-training.vercel.app

---

## What Went Well

- **Single-day full build** — Phases 0–9 completed in one session (28 commits). The pre-built animation library, Sanity integration, and site.ts architecture from prior builds made this possible
- **Hero particle system** — Canvas particles (stars + embers + glimmers) + CSS breathing orbs + text-shimmer headline delivered a luxury opening with no video asset required. Client approved immediately
- **Progress.md discipline** — Session log updated after every phase. Every fix, architectural decision, and blocker documented in real time
- **Commerce migration mid-build** — Recognized that the initial Snipcart implementation was transitional after seeing the Andrea Abella Marie architecture; made the call to migrate to Stripe + custom cart mid-Phase 8. Clean migration with reference repo available
- **All copy in `src/data/site.ts`** — Zero hardcoded strings in JSX. Client can hand this to any developer without hunting through components
- **Pricing page as sales tool** — ROI calculator + comparison chart built and deployed for the sales conversation. Env-gated for pre-launch removal
- **Quiz as conversion infrastructure** — Multi-step quiz (problems → goals → lead capture → program recommendation) routes visitors to the right offer automatically

---

## What Didn't

| # | Gap | Fix Applied |
|---|-----|-------------|
| 1 | `once: true` in react-intersection-observer doesn't work — silently ignored; animations re-fired on every scroll | Fixed to `triggerOnce: true` across all animation primitives in Phase 2 |
| 2 | `fs` / `path` imports in `PhotoPlaceholder.tsx` caused Turbopack client bundle error | Replaced with `useState + onError` fallback — no server modules in client files |
| 3 | CLAUDE.md Rule 4 references Snipcart skill as mandatory, but Snipcart was replaced entirely in Phase 8 | Rule not updated during build — workflow gap, needs toolkit update |
| 4 | Phase 10 SEO (JSON-LD, sitemap, alt text) and Phase 11 QA not complete at project close | Still pending — Adam needs to run the pre-launch checklist before going live |

---

## Tools Introduced This Build

- **Resend** — email for contact form submissions (established in Danielle Thompson but now standard)
- **Stripe + Printful custom cart** — full Stripe checkout + Printful variant API (already in vault from Andrea Abella Marie; applied fresh to a new build)
- **`react-intersection-observer`** — `triggerOnce` API confirmed (not `once`)
- **`website-build-template.md`** — new project-close deliverable created from this build: reusable architecture doc covering hero, animations, sections, quiz, blog, shop, pricing page pattern

---

## Changes Made to Toolkit

1. **Add error entry**: `react-intersection-observer-triggeronc-not-once` — `triggerOnce` not `once`
2. **Add pattern entry**: `dual-hero-animation-canvas-orbs` — canvas particles + CSS orbs as luxury hero standard
3. **Add pattern entry**: `roi-calculator-dev-only-pricing-tool` — env-gated ROI tool for sales phase
4. **Add pattern entry**: `quiz-multistep-lead-capture-program-recommendation` — 3-step quiz → program CTA
5. **Update CLAUDE.md Rule 4** — Snipcart reference should be updated to Stripe + Printful custom cart architecture
6. **Consider adding `website-build-template.md` to end-to-end-workflow.md** as a standard project-close deliverable

---

## Notes

- The outer planning repo (`c:\Projects\Gray-Method-Training`) holds brand voice, competitive intel, design contract, and master prompt. The actual app lives in the git submodule (`gray-method-training/`). Both have their own `progress.md` — the outer one is a template that stays static; the inner one is the live log
- All 28 commits happened on 2026-03-29 with `tonyrose777-ops` + `claude` as contributors
- 21 Vercel deployments — production is green

See [[retrospectives/andrea-abella-marie]] for the Stripe + Printful commerce architecture this build drew from.
