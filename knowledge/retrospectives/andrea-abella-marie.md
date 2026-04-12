---
name: Andrea Abella Marie — Project Retrospective
type: retrospective
description: Full-stack coaching website with working Printful+Stripe shop, Resend transactional emails, GHL CRM integration, and blog
---

# Andrea Abella Marie — Project Retrospective
**Type:** Trauma-informed mindset coach + energy healing practitioner  
**Client:** Andrea Abella Marie / Inner Peace Project  
**Domain:** coachandreaabellamarie.com  
**Completed:** Apr 2026  
**Build sessions:** ~8 sessions (Mar 10 – Apr 1 2026)  
**Deal value:** $5,500

---

## What Went Well
- Full e-commerce stack shipped and verified end-to-end with a real live purchase — Stripe → webhook → Printful order confirmed → customer receipt → owner alert all working
- Dual fulfillment model (POD auto via Printful + manual Resilience Collection jewelry) handled cleanly in one webhook
- Resend domain verification on GoDaddy via auto-configure worked perfectly — DKIM + SPF green in one click
- Blog architecture with 8 AI-generated posts and images (6 with Andrea's likeness) delivered with no photography required
- Seeded JSON fallback for Printful kept the shop rendering even during API downtime
- `KNOWN_COLORS` variant parser elegantly handled the 2-part vs 3-part naming inconsistency across Printful product categories
- `website-build-template.md` updated with all production-proven shop patterns so next build starts battle-tested

---

## What Didn't
| # | Gap | Fix Applied |
|---|-----|-------------|
| 1 | Snipcart tried first — abandoned after cart button unresponsiveness and complexity | Reverted to custom React Context cart + Stripe hosted checkout |
| 2 | Printful orders landing as Draft — `confirm:true` in body silently ignored | Changed to `?confirm=true` query param |
| 3 | Stripe webhook 307 — non-www domain redirects, Stripe doesn't follow | Updated webhook URL in Stripe Dashboard to www canonical |
| 4 | Color-only variants (tumblers) showing colors as size chips | Built KNOWN_COLORS parser, fixed variant field assignment |
| 5 | "Bottle Green" rendering as gray — missing from COLOR_MAP + casing mismatch | Added to map, made lookup case-insensitive |
| 6 | No customer receipt email on purchase | Added `customer_creation: "always"` to Stripe session |
| 7 | Contact form had empty `onSubmit` — discovered post-launch by client | Built `/api/contact` → Resend route |
| 8 | GHL CRM integration via Private Integration API — 5 failed attempts (403, 401, token exchange) | Switched to GHL Inbound Webhook — no auth required |
| 9 | Resend API key exposed in screenshot during setup | Rotated immediately; new key in Vercel |
| 10 | Printful billing card outdated — first confirmed order payment failed | Andrea updated card in Printful → Billing; retried successfully |

---

## Tools Introduced This Build
| Tool | Purpose | Notes |
|------|---------|-------|
| Resend | Transactional email (owner order alerts + contact form) | Free tier, 3k/month; domain verified via GoDaddy auto-configure |
| Printful API | POD fulfillment via webhook | `?confirm=true` as query param — not body |
| GHL Inbound Webhook | CRM contact creation from external forms | Bypass all Private Integration auth issues |

---

## Changes Made to Toolkit
- `website-build-template.md` Section 7 fully rewritten with production-proven Printful + Stripe + Resend architecture including all gotchas
- 5 new errors logged to Error Encyclopedia
- 4 new patterns logged to Build Patterns
- Pre-launch QA checklist should add: "test every form submit and confirm email delivery"
- Shop QA should add: "test variant picker with at least one apparel AND one drinkware product"
- Stripe webhook setup should add: "confirm canonical www/non-www before registering"

---

# Post-Launch Addition — Sanity CMS Migration (Apr 11, 2026)

**Motivation:** Andrea needed to edit her own blog posts and testimonials without calling me every time. Original build had all blog content hardcoded in `src/lib/blog.ts` (1,088 lines) and testimonials hardcoded in two separate client component arrays. Not sustainable.

**Result:** All content editable by Andrea from `coachandreaabellamarie.com/studio`. Zero developer touchpoint required for content updates. Completed in one session.

## Architectural Decision — Embedded vs Standalone Studio

Sanity's onboarding pushes you toward a **standalone Studio** in its own folder (`npm create sanity@latest`). I rejected that path in favor of **embedded Studio** mounted inside the existing Next.js app at `/studio`.

**Why embedded:**
- One repo, one deploy, one login — Vercel already handles it
- Same domain as the site (`coachandreaabellamarie.com/studio`) — no separate subdomain or sanity.studio-hosted URL to explain to the client
- No second deployment pipeline for the client to worry about
- Content collaborators log in with their Sanity account, same as standalone

**Trade-off:** Build time jumped from ~10s to ~51s on Vercel because Sanity Studio is a heavy React admin app bundled into the same Next build. Acceptable for a low-frequency-deploy client site. Escape hatch available if it ever matters: move to sanity.studio-hosted with one click.

## Steps Taken, in Order

1. **Confirmed project coordinates** — project ID `13idr5es`, dataset `production`, both already created in Sanity management panel. (Note: initially misread the ID as `131dr5es` from the onboarding screenshot — cost us one failed migration run. See What Didn't below.)
2. **Added env var scaffolding to `.env.local`** first so client could paste tokens while I worked:
   - `NEXT_PUBLIC_SANITY_PROJECT_ID`
   - `NEXT_PUBLIC_SANITY_DATASET`
   - `NEXT_PUBLIC_SANITY_API_VERSION`
   - `SANITY_API_READ_TOKEN` (for server-side fetches, even though dataset is public)
   - `SANITY_API_WRITE_TOKEN` (for migration only — revoked after)
3. **Installed deps** — `sanity`, `next-sanity`, `@sanity/image-url`, `@sanity/vision`, `@portabletext/react`, `styled-components`, plus `tsx` and `dotenv` as dev deps for migration script. 865 packages total. Next.js 16 + React 19 + Sanity v5 all compatible.
4. **Created schemas** at `src/sanity/schemaTypes/`:
   - `blogPost` — title, slug (with auto-generate from title), excerpt, category (dropdown matching the 6 existing categories), date, readTime, featured, image with alt text + hotspot, body as Portable Text (normal/h2/h3/blockquote/bullet + strong/em/link marks)
   - `testimonial` — name, role, text, stars, placement (multi-select: "page" and/or "carousel"), order for manual sorting
5. **`sanity.config.ts` at project root** — embedded Studio config with custom structure tool grouping Blog Posts + Testimonials in the left sidebar. `basePath: "/studio"`.
6. **Mounted Studio route** at `src/app/studio/[[...tool]]/page.tsx` with the canonical next-sanity pattern (client wrapper `Studio.tsx` + server-component `page.tsx` re-exporting `metadata` and `viewport` from `next-sanity/studio`).
7. **Data layer rewrite** — `src/lib/blog.ts` went from 1,088 lines of hardcoded data to an 86-line Sanity wrapper exposing `getAllPosts`, `getPostBySlug`, `getAllSlugs`, `getRelatedPosts`. New `src/lib/testimonials.ts` for `getPageTestimonials` and `getCarouselTestimonials`. GROQ queries in `src/sanity/queries.ts`.
8. **Refactored all consumer components** — `BlogContent.tsx`, `BlogPreview.tsx`, `BlogPostContent.tsx`, `TestimonialsContent.tsx`, `TestimonialsCarousel.tsx` all changed from "import data directly" to "accept data as props." Page routes (`src/app/blog/page.tsx`, `src/app/blog/[slug]/page.tsx`, `src/app/testimonials/page.tsx`, `src/app/page.tsx`) changed to `async` server components that `await` the Sanity fetchers and pass results down.
9. **Portable Text renderer** — `src/components/PortableTextBody.tsx` with custom components for each block type (normal/h2/h3/blockquote/bullet list) that **exactly mirror the original hardcoded ContentBlock styling** (same Tailwind classes, same inline styles, same `var(--font-*)` tokens). Visual output is pixel-identical after migration.
10. **`next.config.ts`** — added `cdn.sanity.io` to `images.remotePatterns` so `next/image` can fetch Sanity-hosted blog cover images.
11. **Migration script** — `scripts/migrate-to-sanity.ts`. Features:
    - Uses `@sanity/client` directly (not next-sanity) with write token
    - Dry-run mode by default; `--apply` flag required to write
    - **Idempotent** — deterministic `_id` values (`blogPost-<slug>` and `testimonial-<md5-fingerprint>`), uses `createOrReplace`. Safe to re-run any number of times.
    - Converts legacy `ContentBlock[]` to Portable Text with stable `_key` values derived from md5 hashes (required by Sanity for all Portable Text nodes)
    - Uploads cover images from `public/images/blog/` to Sanity CDN via `client.assets.upload`, caches by absolute path so re-used images aren't uploaded twice
    - Normalizes display dates (`"Apr 11, 2026"`) to ISO (`2026-04-11`) before writing
    - Adds `npm run sanity:migrate` script alias
12. **Seed data files** — `scripts/seed-blog-posts.ts` (copied verbatim from original `blog.ts` before I rewrote it) and `scripts/seed-testimonials.ts` (hand-deduped from the two component arrays — 20 from page, 4 unique carousel-only, 3 shared between both via the `placement` array). 24 testimonials total.
13. **Verification script** — `scripts/verify-migration.ts` runs GROQ queries against Sanity post-migration to confirm all 10 posts have image asset references and testimonial placement counts match expectations.
14. **Dry run → apply** — dry run was green, apply wrote 10 posts + 24 testimonials successfully, verify script confirmed all 10 posts had `image.asset` populated.
15. **Local build + dev server** confirmed everything renders end-to-end from Sanity before pushing.
16. **Committed** as `feat: add Sanity CMS for blog posts and testimonials` (commit `9743554`) with targeted `git add` — excluded unrelated pre-existing modifications (`CLAUDE.md`, `website-build-template.md` deletion, `.claude/` directory).
17. **Vercel auto-redeployed** the push. Verified `/studio/[[...tool]]` appeared in the build log route list and all 10 blog slugs statically generated from Sanity.
18. **Post-deploy checklist** with client:
    - Added 3 Sanity env vars to Vercel (all environments — Production, Preview, Development)
    - Added CORS origins at Sanity management: `https://coachandreaabellamarie.com`, `https://www.coachandreaabellamarie.com`, `http://localhost:3000`, all with "Allow credentials" checked (required for Studio browser auth)
    - Revoked write token immediately after migration — cleared value in `.env.local`, deleted at Sanity management panel
    - Invited Andrea as **Editor** (not Administrator — too much power; not Contributor — can't publish)

## What Went Well
- Embedded Studio decision was correct — client never had to learn "separate studio deployment"
- Idempotent migration script meant the wrong-project-ID failure cost us zero data — first apply hit wrong host (401), we fixed the env var, re-ran the identical command, it just worked
- Preserving the `BlogPost` TypeScript type shape meant existing page components needed minimal changes (just prop-drilling instead of imports)
- Portable Text renderer matching the original ContentBlock styling line-for-line meant zero visual regression after the content source swap — same post looked identical before and after
- Placement tags on testimonials cleanly solved the "same content appears in two different places on the site" problem without duplicating documents
- Dry-run default on the migration script caught issues before any writes happened
- Deterministic `_id` values made re-runs safe — no orphaned docs, no duplicates, no cleanup needed after failed attempts
- Client was able to stay in parallel (pasting tokens, clicking through Sanity management UI) while I wrote code — no idle waiting on either side

## What Didn't
| # | Gap | Fix Applied |
|---|-----|-------------|
| 1 | Misread project ID from onboarding screenshot — wrote `131dr5es` (one-three-**one**) instead of `13idr5es` (one-three-**i**). First migration run failed with cryptic `SIO-401-AWH Session does not match project host` 401 | Asked client for screenshot of project dashboard, spotted the `i`, updated `.env.local`, re-ran migration — succeeded in one try |
| 2 | First Vercel redeploy (triggered by env var add) built the **pre-Sanity commit** `7c92af0` because I hadn't pushed the Sanity work yet. Build passed cleanly (no Sanity code = no dependency) but `/studio` route was missing from output. Confused for about 30 seconds before realizing | Committed + pushed Sanity work, Vercel auto-redeployed the new commit, `/studio/[[...tool]]` appeared in route list |
| 3 | TypeScript check failed initially because the backup files I saved (`scripts/backup/orig-carousel.tsx`) included `"use client"` component imports that didn't resolve outside `src/components/` | Deleted backups after extracting the testimonial arrays — backups weren't needed long-term anyway |
| 4 | First edit attempt on `TestimonialsContent.tsx` renamed the hardcoded array to `_legacyTestimonials_unused` as a commented-out stub — violated CLAUDE.md rule against backwards-compat cruft | Re-did the edit to properly delete the array via `awk` script, then confirmed the component took testimonials as a prop cleanly |
| 5 | `verify-migration.ts` first version used top-level `await` which esbuild's cjs output doesn't support under `tsx` | Wrapped in `async function main() { ... } main();` pattern |
| 6 | Windows CRLF warnings on every staged file during `git add` | Cosmetic only — git auto-normalizes line endings, safe to ignore |

## Tools Introduced This Build
| Tool | Purpose | Notes |
|------|---------|-------|
| Sanity CMS v5 | Headless content database for blog + testimonials | Free tier: 20 user seats, 2 public datasets, hosted DB — plenty for a small coaching site |
| `next-sanity` v12 | Next.js ↔ Sanity integration with NextStudio wrapper | Canonical embedded Studio pattern works cleanly with Next 16 App Router + React 19 |
| `@portabletext/react` | Render Portable Text blocks with custom components | Use custom `components.block.*` to match existing design system exactly — don't rely on defaults |
| `tsx` | Run TypeScript files directly without a build step | Dev dep only — for one-off migration scripts. Avoid top-level await under cjs output |
| `dotenv` | Load `.env.local` inside node scripts that don't go through Next's own loader | Only needed for standalone scripts |

## Patterns Worth Remembering
- **When CMS-migrating an existing site, keep the downstream TypeScript types stable.** Our `BlogPost` interface didn't change shape even though the data source did — consumers didn't have to care.
- **Always write migration scripts as idempotent from day one.** Deterministic IDs + `createOrReplace` + dry-run default turns a scary one-shot operation into a safe "run it until it works."
- **For visual parity after a content source swap, port the renderer styles line-for-line before migrating data.** You want the first Sanity-powered pageview to look identical to the last hardcoded pageview. No drift, no "oh also the blockquote looks different now."
- **Embedded Studio > standalone Studio for client sites.** The client doesn't care about Sanity the product — they care about "where do I log in to edit my blog." `yourdomain.com/studio` is a correct answer; `project-slug.sanity.studio` is a confusing one.
- **Sanity's free tier is genuinely usable.** 20 seats is generous. Don't default-upgrade clients to Growth — read the actual plan comparison first. For a small coaching site with 1–2 editors, Free is correct.
- **CORS credentials checkbox is required for Studio on production domains.** Not optional. Without it, the Studio UI will load but auth will silently fail on cross-origin preflight.
- **Add Vercel env vars to all three environments** (Production, Preview, Development) unless there's a deliberate reason not to. Otherwise future preview deploys from branches will mysteriously fail to build.

## Changes Made to Toolkit
- `website-build-template.md` should add a **Section 8: "Content Management"** documenting:
  - When to reach for a CMS vs hardcoded content (rule of thumb: if the client will ever want to edit it without you, CMS from day one)
  - The embedded Sanity pattern as the default
  - The exact env var + CORS + token setup sequence
  - The idempotent migration script pattern
- Build checklist should add: **"Does the client need to edit any content themselves? If yes, CMS belongs in scope from day one, not as a retrofit."** — retrofitting is fine but scoping it upfront is cheaper
- Pre-launch handoff checklist should add: **"Confirm client can log into CMS from production domain, publish a test edit, and see it on the live site within 60 seconds"** — do this *with* the client before declaring the project done
- New error added to Error Encyclopedia: `SIO-401-AWH "Session does not match project host"` = wrong project ID in the token's parent env var, not a token permissions issue
- New pattern added to Build Patterns: **"Idempotent CMS Migration Script"** — deterministic IDs, dry-run default, image upload caching, date normalization, `_key` generation for Portable Text

