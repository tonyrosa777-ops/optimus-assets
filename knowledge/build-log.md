# build-log.md — Optimus Business Solutions
# Cross-Project Knowledge Base
# Location: C:\Projects\Optimus Assets\knowledge\build-log.md
#
# HARD RULES (enforced by CLAUDE.md):
#   - Read this at the start of every build session
#   - Log every resolved error before continuing work
#   - Log every non-obvious pattern or finding at phase completion
#   - Write a retrospective entry at project close

---

## Error Encyclopedia

Known problems with confirmed solutions. Detailed entries in `knowledge/errors/`.

| # | Problem | Project | Date | Entry |
|---|---------|---------|------|-------|
| 1 | Vercel 404 on subdirectory deploy | Enchanted Madison | Mar 2026 | [[errors/vercel-subdirectory-404]] |
| 2 | Nav overflow with >4 links | Enchanted Madison | Mar 2026 | [[errors/nav-overflow-too-many-links]] |
| 3 | Placeholder CTA accepted as phase-complete | Enchanted Madison | Mar 2026 | [[errors/placeholder-cta-accepted-as-complete]] |
| 4 | Generated assets not committed with task | Enchanted Madison | Mar 2026 | [[errors/generated-assets-not-committed]] |
| 5 | Media asset placed in repo root instead of /public | Enchanted Madison | Mar 2026 | [[errors/media-asset-wrong-location]] |
| 6 | /prime loads global template instead of project variables when project-scoped .claude/commands/prime.md doesn't exist | Placed Right Fence | Apr 2026 | [[errors/prime-loads-global-template-instead-of-project]] |
| 7 | Zod v4: `errorMap` renamed to `error` in enum/string params | Enchanted Madison | Mar 2026 | [[errors/zod-v4-errormap-rename]] |
| 7 | Stripe 21: API version changed to `2026-03-25.dahlia`; `shipping_details` moved to `collected_information.shipping_details` | Enchanted Madison | Mar 2026 | [[errors/stripe-21-api-version-dahlia]] |
| 8 | Framer Motion v12: `ease: number[]` (cubic bezier array) rejected in `Variants` — use `"easeOut" as const` or named easing string instead | Sylvia Rich | Apr 2026 | [[errors/framer-motion-v12-ease-type]] |
| 8b | Framer Motion v12: named ease string (`'easeOut'`) inferred as `string` not `Easing` in object literals — TypeScript rejects in Variants; fix: use cubic bezier `[0, 0, 0.2, 1] as const` instead | Where2 Junk | Apr 2026 | (inline fix) |
| 8c | lucide-react: `Facebook` icon was removed from the package — `Export Facebook doesn't exist`; fix: replace with inline SVG path | Where2 Junk | Apr 2026 | (inline fix) |
| 8d | Server Components with `onMouseEnter`/`onMouseOut` event handlers cause prerender crash — `Event handlers cannot be passed to Client Component props`; fix: add `'use client'` as first token. **Exception:** if the component exports `metadata`, it cannot become a Client Component (Next.js prohibits `metadata` in Client Components); use CSS `:hover` in a `<style>` block instead of JS event handlers. See error #27. | Where2 Junk | Apr 2026 | [[errors/server-component-hover-metadata-constraint]] |
| 9 | Turbopack: `"use client"` must be the absolute first token — before imports AND comments. `// comment` then `"use client"` causes build failure | Sylvia Rich | Apr 2026 | [[errors/turbopack-use-client-not-first-token]] |
| 10 | Canvas animation `groundY` breaks after hero flex changes from `items-center` → `items-start` — content pins to top but groundY still scales with H | Placed Right Fence | Apr 2026 | [[errors/canvas-animation-breaks-after-hero-flex-change]] |
| 11 | Mobile viewport height variance (667–932px) causes canvas animation tip to land behind CTA buttons — raw `H * N` groundY not safe without Math.min() cap | Placed Right Fence | Apr 2026 | [[errors/mobile-viewport-height-variance-clips-canvas-animation]] |
| 12 | Sanity Studio SSR crash with Turbopack — `createContext` fires in server context; fix: extract StudioClient as `"use client"` file + `dynamic(ssr:false)` | Placed Right Fence | Apr 2026 | [[errors/sanity-studio-ssr-crash-createcontext-turbopack]] |
| 13 | Vercel deploy blocked after pipeline connected — git committer email didn't match GitHub account; fix: `git config user.email` + empty commit | Danielle Thompson | Apr 2026 | [[errors/vercel-deploy-blocked-git-email-mismatch]] |
| 14 | CTABanner props named `ctaLabel`/`ctaHref` on new page — component interface uses `buttonText`/`buttonHref`; TypeScript build failure on Vercel | Danielle Thompson | Apr 2026 | [[errors/ctabanner-prop-name-mismatch-build-failure]] |
| 15 | `next.config.ts` not supported in Next.js 14 — must use `next.config.mjs` | Danielle Thompson | Apr 2026 | [[errors/next-config-ts-not-supported-nextjs14]] |
| 16 | Rate badge overflow — long policy text in `whitespace-nowrap` pill; fix: use short pointer ("See travel policy"), put detail in notes block | Danielle Thompson | Apr 2026 | [[errors/rate-badge-overflow-whitespace-nowrap]] |
| 17 | Stripe webhook 307 — non-www domain redirects to www; Stripe doesn't follow redirects; webhook silently fails | Andrea Abella Marie | Apr 2026 | [[errors/stripe-webhook-307-www-redirect]] |
| 18 | GHL Private Integration 403 — agency admin token cannot write to location; token exchange endpoint also 401; fix: use GHL Inbound Webhook instead | Andrea Abella Marie | Apr 2026 | [[errors/ghl-private-integration-agency-token-403]] |
| 19 | Contact form empty `onSubmit` — `e.preventDefault()` stub left as placeholder; discovered post-launch when client received no inquiries | Andrea Abella Marie | Apr 2026 | [[errors/contact-form-empty-onsubmit-discovered-post-launch]] |
| 20 | Stripe guest checkout no receipt email — `customer_creation: "always"` required for Stripe to send receipt to guest customers | Andrea Abella Marie | Apr 2026 | [[errors/stripe-guest-checkout-no-receipt-email]] |
| 21 | Printful color-only variant names misparsed as size — 2-part names "Product / Black" assign color to size field; fix: KNOWN_COLORS detection + case-insensitive COLOR_MAP | Andrea Abella Marie | Apr 2026 | [[errors/printful-color-only-variant-misparse]] |
| 22 | Printful CDN image URLs fabricated for products without confirmed scrape URLs — lazy-loaded images appear as SVG placeholders in firecrawl; guessed hash paths 404; use Unsplash until real mockups exist | Cody's Complete Junk Removal | Apr 2026 | [[errors/printful-cdn-image-url-fabricated]] |
| 23 | No global .gitconfig on Windows — fresh Windows install has no ~/.gitconfig; `git config --global user.name` errors; fix: set per-repo identity before first commit | Cody's Complete Junk Removal | Apr 2026 | [[errors/no-global-gitconfig-windows]] |
| 24 | `react-intersection-observer` uses `triggerOnce` not `once` — `once: true` is silently ignored; animations re-trigger on every scroll; fix: `triggerOnce: true` across all animation primitives | Gray Method Training | Mar 2026 | [[errors/react-intersection-observer-triggeronc-not-once]] |
| 25 | Mobile hero text starts mid-screen — `min-h-screen` + `flex items-center` vertically centers content; fine on desktop tall viewport, puts headline dead-center on short mobile screen; fix: `items-start` + `pt-24 md:pt-40` on content div | Sweep Test 1 | Apr 2026 | (inline fix) |
| 26 | JSON `null` vs TypeScript `undefined` in seeded data files — type `string \| undefined` does not accept `null`; fix: omit the field entirely from JSON (absent key = `undefined` in TS) | Where2 Junk | Apr 2026 | [[errors/json-null-vs-typescript-undefined-seeded-data]] |
| 27 | Server Component with `metadata` export cannot use `'use client'` to fix event handler crash — Next.js prohibits `metadata` in Client Components; fix: use CSS `:hover` in `<style>` block instead of JS event handlers | Where2 Junk | Apr 2026 | [[errors/server-component-hover-metadata-constraint]] |
| 28 | Photo placeholder appears in hero instead of 3-layer animation stack — template's split-layout description implied a right-side image slot; fix: hero has NO photo slot; photo belongs in About section; updated CLAUDE.md Hero Architecture Rule and template Section 1 | Helen Grondin | Apr 2026 | (inline fix — CLAUDE.md + template updated) |
| 29 | Hero text invisible against background — wrong color token used for headings; "Where healthcare finally makes sense" unreadable without highlighting; fix: ALL headings use `color: var(--text-primary)` on dark backgrounds; tagline must use `.text-shimmer` class | Helen Grondin | Apr 2026 | (inline fix — CLAUDE.md + template updated) |
| 30 | Second hero CTA links to info session instead of quiz — site.ts `ctaSecondary` pointed to an event link; fix: secondary CTA slot is permanently reserved for `/quiz`; updated CLAUDE.md Hero Architecture Rule and template CTA pair pattern | Helen Grondin | Apr 2026 | (inline fix — CLAUDE.md + template updated) |
| 31 | Testimonials grid orphan rows — 32 testimonials paginated 8 per page in a 3-col grid = 2 full rows + 2 orphans on every page; fix: use 36 testimonials paginated 9 per page (3-col × 3-row = perfect square every page); updated CLAUDE.md and template | Helen Grondin | Apr 2026 | (inline fix — CLAUDE.md + template updated) |
| 32 | Interior pages shipped with static plain headers — only the hero had animations; services, testimonials, booking pages were flat; fix: Page Animation Rule added to CLAUDE.md requiring branded animation on every page | Helen Grondin | Apr 2026 | (inline fix — CLAUDE.md updated) |
| 33 | Behold API integration — 3 compounding bugs: (1) `mediaUrl` is nested under `sizes.medium.mediaUrl` not top-level; (2) Behold UI copies full URL but code prepended base URL again, creating double URL; (3) fallback chain preferred expiring Instagram CDN `mediaUrl` over stable Behold CDN `sizes.*` URLs | Gray Method Training | Apr 2026 | [[errors/behold-api-integration-pitfalls]] |
| 34 | `PhotoPlaceholder` `onError` fires on production even when real image exists — hydration timing issue causes scaffold to swap in placeholder UI; fix: replace `PhotoPlaceholder` with direct `next/image` once real asset is confirmed | Gray Method Training | Apr 2026 | [[errors/photo-placeholder-onerror-fires]] |

---

## Build Patterns That Work

Specific approaches that produced measurable results.

| # | Pattern | Category | Project | Date |
|---|---------|----------|---------|------|
| 1 | Stripe webhook: always use `collected_information.shipping_details` in v21+; `confirm` must be a query param not body field | Payments | Enchanted Madison | Mar 2026 |
| 2 | Cart drawer in SiteHeader (not layout) — avoids layout refactor while making cart globally accessible | Architecture | Enchanted Madison | Mar 2026 |
| 3 | Stripe API version: always check `node_modules/stripe/types/apiVersion.d.ts` for the correct version string; it changes each major release | Payments | Enchanted Madison | Mar 2026 |
| 4 | fal.ai image generation from design-system.md prompts — eliminates need for client photography before launch | AI Assets | Enchanted Madison | Mar 2026 |
| 5 | Kling AI video for hero background loop — cinematic feel for premium brands without a video shoot | AI Assets | Enchanted Madison | Mar 2026 |
| 6 | Responsive canvas animation with `getLayout(W, H)` breakpoint function — centralizes all layout params, enforces Math.min() cap on mobile groundY | Animation / Architecture | Placed Right Fence | Apr 2026 |
| 7 | Hero concept iteration — budget for 3 full approaches before final; don't start mobile calibration until desktop concept is approved | Workflow / Animation | Placed Right Fence | Apr 2026 |
| 8 | Homepage dark/light section rhythm — plan alternation before building any section; 3 consecutive same-background sections always need a flip | Visual Design / UX | Placed Right Fence | Apr 2026 |
| 9 | 3-tier pricing anchoring — set badge: null on premium tier; only middle tier gets a badge; premium's job is anchoring, not converting | Conversion / Pricing | Placed Right Fence | Apr 2026 |
| 10 | `constants.ts` single source of truth — all client data (phone, email, dates, services, testimonials) in one file; components import, never hardcode | Architecture | Danielle Thompson | Apr 2026 |
| 11 | Google Maps iframe without API key — `maps.google.com/maps?q=City,ST&output=embed` works free; no Cloud account needed | Maps / Integration | Danielle Thompson | Apr 2026 |
| 12 | Next.js native OG image — `opengraph-image.tsx` + `ImageResponse` + `readFileSync` for local asset base64; no external service | SEO / Social | Danielle Thompson | Apr 2026 |
| 13 | Calendly inline embed with brand colors — URL params `background_color`, `text_color`, `primary_color`; `NEXT_PUBLIC_` env var; dynamic script load in useEffect | Scheduling | Danielle Thompson | Apr 2026 |
| 14 | One Resend account per client — free tier = 1 domain; don't consolidate multiple clients into one account; each client owns their account | Email / Architecture | Danielle Thompson | Apr 2026 |
| 15 | Printful variant name parser with KNOWN_COLORS — detect color vs size by name lookup, not position; handles 2-part drinkware and 3-part apparel names; case-insensitive COLOR_MAP | E-commerce / Printful | Andrea Abella Marie | Apr 2026 |
| 16 | GHL CRM integration via Inbound Webhook — create workflow with Inbound Webhook trigger + Create Contact action; POST form data to webhook URL; no API key needed; bypasses all Private Integration auth issues | CRM / Integration | Andrea Abella Marie | Apr 2026 |
| 17 | Stripe webhook canonical URL — register at exact canonical domain (www or non-www); Stripe doesn't follow redirects; NEXT_PUBLIC_SITE_URL must match | Payments / Infrastructure | Andrea Abella Marie | Apr 2026 |
| 18 | Stripe checkout session defaults — always include `customer_creation: "always"`, absolute HTTPS image URLs only, cart in metadata.cart JSON | Payments | Andrea Abella Marie | Apr 2026 |
| 19 | Firecrawl existing site capture as project brief — scrape client's current site into structured .md before build; replaces content questionnaire for clients with existing sites | Workflow / Discovery | Cody's Complete Junk Removal | Apr 2026 |
| 20 | Hero server/client animation split — main hero as server component + separate `HeroEffects` client component for decorative animations; keeps `"use client"` boundary tight, SSRs real content | Architecture / Animation | Cody's Complete Junk Removal | Apr 2026 |
| 21 | Static Printful merch data file — populate shop.ts with real Printful products (correct names, base cost, retail markup) + Unsplash placeholder images; swap images when client generates Printful mockups | E-commerce / Printful | Cody's Complete Junk Removal | Apr 2026 |
| 22 | Dual hero animation system — canvas particles (stars + embers + glimmers, rAF loop) + CSS breathing orbs (`@keyframes orb-breathe`, 3 orbs offset phases) + `text-shimmer` headline; luxury dark-brand hero without video | Animation / Visual Design | Gray Method Training | Mar 2026 |
| 23 | ROI Calculator as dev-only pricing sales tool — interactive calculator + comparison chart env-gated (`NEXT_PUBLIC_SHOW_PRICING_TOOLS`); show to client during sales, remove before launch | Conversion / Pricing | Gray Method Training | Mar 2026 |
| 24 | Quiz multi-step lead capture with program recommendation — 3 steps: multi-select problems → single-select goal → lead form → personalized program CTA; quiz answers appended to contact submission | Conversion / Lead Gen | Gray Method Training | Mar 2026 |
| 25 | Demo booking calendar with hash-based seeded availability — `(year*400 + month*31 + day) % 10` maps dates deterministically; fully interactive without backend; Calendly silently integrates when URL env var is set | Conversion / UX / Demo | Where2 Junk | Apr 2026 |
| 26 | Hover-open + click-navigate nav dropdowns — outer container div gets `onMouseEnter/Leave`; inner trigger is `<Link href="/parent">` not `<button>`; hovering reveals sub-pages, clicking navigates to category page | Navigation / UX | Where2 Junk | Apr 2026 |
| 27 | "More" overflow dropdown for crowded desktop nav — `Set(['Gallery','FAQ','Pricing','Shop'])` filtered from main loop, grouped behind `≡ ∨` click-toggle button; primary conversion links stay always visible | Navigation / UX | Where2 Junk | Apr 2026 |
| 28 | Brand Canvas 5-phase pattern — STREAM (particle bezier flow) → RISE (springOut shape extrude) → COOL (heat palette → brand primary) → ARC (secondary element draw) → IDLE (breathe oscillation); springOut = `1 - 2^(-9t) * cos(t*10π*0.68)`; H1 = siteConfig.tagline + shimmer; text left / canvas right split; `canvas.getContext("2d") as CanvasRenderingContext2D` always cast | Animation / Architecture | Helen Grondin | Apr 2026 |
| 29 | Scored quiz lead funnel — data layer (quiz.ts: QuizType, QUIZ_QUESTIONS×8, QUIZ_RESULTS, scoreQuiz); 3 UI phases (intro→question→results); 400ms pendingAnswer glow + auto-advance; direction-aware AnimatePresence; scoreQuiz on Q8 answer, instant results, no email gate; BookingCalendar inline on results screen; client-only Resend notification; Calendly collects user email during booking | Conversion / Lead Gen | Gray Method Training | Apr 2026 |
| 30 | Behold.so Instagram feed — replaces entire Instagram Graph API + Redis token store + monthly cron system with one env var (NEXT_PUBLIC_BEHOLD_FEED_ID); Behold uses camelCase (mediaUrl not media_url); use plain `<img>` not next/image (CDN domain unpredictable); 9-tile placeholder fallback when ID unset; async server component with hourly ISR; NOT required on every build — optional when client has active Instagram | Social / Integration | Gray Method Training | Apr 2026 |

---

## Project Retrospectives

| Project | Type | Completed | Key Learning |
|---------|------|-----------|--------------|
| Enchanted Madison | Luxury glamping / romantic experience | Mar 2026 | 10 workflow gaps identified and closed. fal.ai + Kling introduced as standard AI asset tools. See [[retrospectives/enchanted-madison]] |
| Placed Right Fence | Fence installation/repair contractor | Apr 2026 | Canvas forge animation locked after 9 iterations. 3 new errors, 4 new patterns. First patterns/ directory created. See [[retrospectives/placed-right-fence]] |
| Danielle Thompson | Notary Public + Justice of the Peace | Apr 2026 | 4 new errors, 5 new patterns. Bio fabrication caused rework. Git identity + rate badge overflow + CTABanner props key lessons. Calendly/Resend/OG image patterns established. See [[retrospectives/danielle-thompson]] |
| Andrea Abella Marie | Trauma-informed coach + energy healing | Apr 2026 | 5 new errors, 4 new patterns. Full Printful+Stripe shop verified end-to-end with real purchase. GHL integration via Inbound Webhook. Stripe webhook 307 + confirm query param + guest receipt + color variant parser all discovered in production. See [[retrospectives/andrea-abella-marie]] |
| Cody's Complete Junk Removal | Junk removal contractor — Dracut, MA / Greater Lowell | Apr 2026 | 2 new errors, 3 new patterns. Firecrawl site capture replaces content questionnaire. Hero server/client animation split introduced. Static Printful merch shop pattern established. No CLAUDE.md/progress.md created — flagged as workflow gap. See [[retrospectives/codys-complete-junk-removal]] |
| Gray Method Training | Women's personal training / online fitness coaching | Apr 2026 | 3 errors, 3 patterns (build) + 2 new errors, 0 new patterns (post-launch). Full build in 1 session (28 commits) + follow-up session. Quiz email gate removed for instant-gratification flow. Behold.so replaces Instagram Graph API + Upstash + Cron. Hero photo replaced PhotoPlaceholder scaffold. See [[retrospectives/gray-method-training]] |
| Sylvia Rich | Honorary Consul of Hungary — New England (5 states) | Apr 2026 (in progress) | Pro package sold. Bilingual (EN/HU formal 3rd person) closed the deal. Domain + Resend set up during meeting. 6 new sales patterns validated (S8–S13). See [[retrospectives/sylvia-rich]] |
| Where2 Junk | Junk removal — Manchester, NH | Apr 2026 (demo-ready, pre-launch) | Full Pro+ build: shop, booking calendar, quiz, blog, 8 service areas, SEO. 2 new errors, 3 new patterns. Demo booking calendar with seeded availability introduced. Nav overflow resolved with More dropdown. Server-component hover CSS fix discovered. See [[retrospectives/where2junk]] |

---

## Sales Patterns

Validated sales process knowledge from real client meetings. Full entries in `knowledge/sales/`.

| # | Pattern | Validated In | Date |
|---|---------|-------------|------|
| S1 | Demo sequence: hero → 1-click flow → gallery → quiz → shop → ROI calc → pricing → close. ROI calc always immediately before pricing. | Placed Right Fence | Apr 2026 |
| S2 | Send invoice during the meeting. Do not wait to follow up. | Placed Right Fence | Apr 2026 |
| S3 | Tax write-off + credit card close: converts price from a cost to a tax event. Works for any business owner. | Placed Right Fence | Apr 2026 |
| S4 | Demo site as pre-payment hook: access unlocks on invoice paid. | Placed Right Fence | Apr 2026 |
| S5 | 15-second response time stat: "if you don't respond within 15 seconds, odds of getting their business drop 50%" — use to close automation upsell. | Placed Right Fence | Apr 2026 |
| S6 | Embed all tools directly in the website (calculators, booking, widgets) — never link out. Frame as SEO traffic retention to client. | Placed Right Fence | Apr 2026 |
| S7 | Three-phase upsell sequence: website → marketing/ads → automation. Only introduce next phase after current is sold and launched. | Placed Right Fence | Apr 2026 |
| S8 | Complete in-meeting onboarding (domain + Resend + DNS access) immediately after invoice paid — removes post-sale friction, saves ~1 week. | Sylvia Rich | Apr 2026 |
| S9 | Gap analysis as demo opener — present 5–6 specific competitor failures before showing the site. Positions as category expert before product reveal. | Sylvia Rich | Apr 2026 |
| S10 | Let client play the quiz during demo — they experience their own customer's journey. More effective than narrating it. | Sylvia Rich | Apr 2026 |
| S11 | AEO (AI Engine Optimization) as urgency trigger — ask if they've searched themselves in ChatGPT. If wrong person comes up, getting live fast becomes a race. | Sylvia Rich | Apr 2026 |
| S12 | Blog = email filter framing — find the client's most common time-wasting inquiry, show an article that answers it. "Your site should answer every question so they don't bother you." | Sylvia Rich | Apr 2026 |
| S13 | Save mobile demo for last — "I didn't even show you the best part." Strong closer, especially when competitors' mobile is broken. | Sylvia Rich | Apr 2026 |

See full detail: [[sales/sales-patterns]] and [[sales/sales-language]]

---

## Workflow Improvements Implemented

Changes made to the Optimus toolkit as a result of project learnings.

| Date | Change | Trigger |
|------|--------|---------|
| Mar 2026 | Renamed `design-contract.md` → `design-system.md` | Naming drift across toolkit files caused aliasing hacks |
| Mar 2026 | Added `intake-prompt.md` and `market-research-prompt.md` as global slash commands | Workflow referenced prompts that didn't exist as commands |
| Mar 2026 | Replaced `optimus-pre-build-workflow.md` with `end-to-end-workflow.md` | Manual checklist replaced with fully autonomous Claude command |
| Mar 2026 | Added `build-log.md` knowledge base + Obsidian vault | Learnings from each build were lost when next project started |
| Mar 2026 | Changed progress.md update rule from end-of-session to after-every-subtask | Context exhausted mid-build on Enchanted Madison leaving progress.md undocumented |
| Mar 2026 | 10 gaps from Enchanted Madison closed — nav rule, CTA placeholder rule, asset commit rule, sections matrix BLOCKER, forms intake field, AI asset generation docs (fal.ai + Kling) | Enchanted Madison build debrief gap analysis |
| Apr 2026 | Added Plan Mode Rule + Subagent Delegation Rule + Skill Creation Rule to CLAUDE.md — plan before building, delegate tasks to subagents, create skills from new patterns | Workflow consolidation after Sylvia Rich + PRF sales meetings |
| Apr 2026 | Added Calendly + Google Maps + Homepage Teaser Rule to website-build-template.md — standard booking widget, service area map, every page gets a homepage teaser | Workflow consolidation |
| Apr 2026 | Created `knowledge/onboarding/client-launch-checklist.md` — exact step-by-step for Resend domain setup, DNS→Vercel configuration, env vars, Stripe webhook, pre-launch checklist | Workflow consolidation — steps previously tribal knowledge |
| Apr 2026 | Em dash rule added to CLAUDE.md Content Standards — never use em dash (—) in testimonials; humans don't type them, it's an AI/copywriter tell | Observed in copy review |
| Apr 2026 | Hero mobile padding rule added to animation-specialist.md and project-prime.md — `items-center` on hero section causes mid-screen text on mobile; must use `items-start` + `pt-24 md:pt-40` | Sweep Test 1 |
| Apr 2026 | Hero Architecture Rule hardened — added explicit "no photo in hero ever" + "photo belongs in About section only"; template Section 1 split-layout removed photo slot | Helen Grondin build sweep |
| Apr 2026 | Tagline shimmer made mandatory in CLAUDE.md and template — `text-shimmer` CSS class on hero tagline every build; hero text contrast check added as pre-phase-complete gate | Helen Grondin build sweep |
| Apr 2026 | Second hero CTA locked to quiz — secondary button always `/quiz`, never info sessions or external links; updated CLAUDE.md Hero Architecture Rule | Helen Grondin build sweep |
| Apr 2026 | Testimonials count changed 32→36, pagination changed 8→9 per page — 8 per page in 3-col grid creates orphan rows; 9 fills exactly 3×3 on every page; updated CLAUDE.md and template | Helen Grondin build sweep |
| Apr 2026 | Page Animation Rule added to CLAUDE.md — every interior page must ship with a brand-appropriate animation in its header; static plain pages are a build failure | Helen Grondin build sweep |
