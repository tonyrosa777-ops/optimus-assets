# Current State — Website Development

Snapshot as of 2026-04-26. The offering is established, productized, and continuously refined. Around 11 client projects have shipped — see `knowledge/retrospectives/` for the full list.

## Productized — every build ships these

The Always-Built Features Rule in [[CLAUDE]] is enforced by the pre-launch-auditor agent. None of these are optional and none are decided per client.

| Feature | What ships |
|---|---|
| Pricing Page (sales tool) | Three tiers, ROI calculator, comparison chart, inline booking CTA per tier. Deleted before launch. |
| Lead-Capture Quiz | 8-question max, 4 archetypes named per client audience, scored result with inline `<BookingCalendar />` on the result screen. Two-layer architecture: pure data layer in `src/data/quiz.ts`, UI in `src/app/quiz/QuizClient.tsx`. |
| Automated Booking Calendar | Custom-branded `<BookingCalendar />` component. Calendly API backend. Demo-mode seeded fallback if `CALENDLY_API_KEY` is unset. Lives at `/booking` and as a homepage teaser section. Never an iframe. |
| Testimonials Page | 36 testimonials, paginated 9 per page across 4 pages. 3×3 grid. Zero em dashes. Written by the content-writer agent in target-audience voice. |
| Professional Blog | 9-10 articles minimum, full SEO/AEO foundation, card image + header image per article via fal.ai. |
| Shop scaffold | CartProvider, CartDrawer, Printful client + API routes, Stripe checkout + webhook routes, seeded products fallback. Wired into `layout.tsx` on every build. Decision gate runs after scaffold: Premium → wire keys; not Premium → delete. |
| 3-layer Hero | HeroParticles + brand-named Canvas + Framer Motion stagger text on every homepage. Brand canvas selected via 10-concept brainstorm → critic agent → single winner (no mid-build pivots). |
| Visual QA gate | Playwright multi-breakpoint browser audit (1440 / 390 / 375 / 428 + nav drawer) before any build is marked complete. |

## In-progress productization

These are still bespoke per client and identified during intake. Candidates for productization once the pattern is clear across more builds:

- **Industry-specific service taxonomy** — each client gets a custom service mapping. TBD whether to ship pre-built taxonomies for the most common verticals (trades, hospitality, professional services, healthcare).
- **CRM / lead routing** — currently Calendly notifications only. TBD: opinionated default for which CRM to integrate with for Pro and Premium tiers.
- **Bilingual support** — has shipped on at least one project (see `knowledge/`). Not yet a tier-level feature.
- **Content pillars + editorial calendar** — blog topics are derived from market-intelligence.md per build. TBD whether to ship a default 12-month editorial framework.

## Tech stack

The full stack reference lives in [[website-build-template]]. Quick reference:

| Layer | Tooling |
|---|---|
| Framework | Next.js (App Router), TypeScript strict |
| Styling | Tailwind CSS 4 + PostCSS, design tokens as CSS custom properties in `globals.css` |
| Animation | Framer Motion + react-intersection-observer + custom canvas |
| Booking | Custom UI + Calendly API |
| Email | Resend |
| Payments | Stripe (Premium tier only) |
| Print-on-demand | Printful (Premium tier only) |
| CMS (blog) | Sanity |
| Image generation | fal.ai |
| Deploy | Vercel |
| Icons | Native emoji only — no Lucide, no Heroicons, no react-icons |

## Continuous refinement

The offering is the same 11 projects' worth of accumulated learning. Every shipped project triggers a `/retro` that adds rows to `knowledge/build-log.md`:

- **Error Encyclopedia** — every novel error solved, one detailed file in `knowledge/errors/`
- **Build Patterns** — every non-obvious finding, one file per pattern in `knowledge/patterns/`
- **Project Retrospectives** — one row per project, file in `knowledge/retrospectives/`

When a pattern proves out across multiple projects, it gets promoted into [[CLAUDE]] or [[website-build-template]] as a universal rule. The most recent example: gradient + motion backgrounds on every section (Pattern #51, codified in CLAUDE.md Homepage Section Architecture Rule).

---

#offering/website-dev #status/active
