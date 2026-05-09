# Pattern #66 — Next 16 dynamic-route Promise params canonical pattern

**First shipped:** Ead Financial, Stage 1E Step 3 (`/services/[slug]`), 2026-05-09 commit `97739f8`.
**Category:** Architecture / Next.js / Dynamic Routing
**Status:** VALIDATED. Reuse on every dynamic-segment route in any Next.js 16 build.

---

## Why this pattern exists

Next.js 16 changed `params` and `searchParams` from synchronous objects to **Promises**. Code that worked in Next 13/14:

```ts
// Pre-Next-16 — BROKEN in Next 16
export default function Page({ params }: { params: { slug: string } }) {
  const { slug } = params;        // synchronous access
}
```

…compiles cleanly in Next 16 with TypeScript flags as expected, but *breaks at runtime* because `params` is now a Promise and synchronous property access yields `undefined`. The failure is silent — no build error, no type error, no warning. The page just renders with bad data or hits `notFound()` for every slug.

This is the highest-friction landmine for any Optimus agent or developer transitioning from training-data-era Next.js patterns to Next 16. Every dynamic-segment route — `/services/[slug]`, `/blog/[slug]`, `/cpa-for-{niche}-{state}`, `/service-areas/[city]` — is exposed.

This pattern documents the canonical shape so subsequent agents copy it verbatim instead of improvising.

---

## The canonical implementation

```ts
// /services/[slug]/page.tsx (or any dynamic route)
import { notFound } from "next/navigation";
import { siteConfig } from "@/data/site";
import type { Metadata } from "next";

// 1. Static-params generator — returns the slug list at build time so
//    each [slug] page is prerendered as a separate HTML file.
export async function generateStaticParams() {
  return siteConfig.services.map((s) => ({ slug: s.slug }));
}

// 2. Per-route metadata — Promise<Metadata> + Promise params.
//    Always destructure via `await params`, NEVER access synchronously.
export async function generateMetadata(
  { params }: { params: Promise<{ slug: string }> }
): Promise<Metadata> {
  const { slug } = await params;
  const service = siteConfig.services.find((s) => s.slug === slug);
  if (!service) return { title: "Service not found" };
  return {
    title: service.name,
    description: service.shortDescription,
  };
}

// 3. Default page export — async function, await params before use.
//    notFound() from "next/navigation" for unknown slugs (404 response).
export default async function ServiceDetailPage(
  { params }: { params: Promise<{ slug: string }> }
) {
  const { slug } = await params;
  const service = siteConfig.services.find((s) => s.slug === slug);
  if (!service) notFound();
  // render service detail using `service`
}
```

### Critical rules

1. **Type signature on `params` is `Promise<...>`, not the bare object.** Both function locations (`generateMetadata` and the default export) type it identically.
2. **Every `params` or `searchParams` access is preceded by `await`.** Destructure once at the top of the function, then use the destructured variables. Do not access `params.slug` directly anywhere — even in conditionals.
3. **Default export is `async`.** It cannot be a regular function because it awaits `params`.
4. **`generateStaticParams` returns an array of plain objects** with the slug field name matching the dynamic-segment folder name. For `[slug]` it returns `{ slug: string }[]`, for `[city]` it returns `{ city: string }[]`.
5. **`notFound()` imports from `next/navigation`** — not from `next` and not from any other path. Calling it short-circuits the rendering path with a 404 response.
6. **`searchParams` follows the identical Promise pattern** when used (most often on filter/pagination pages, quiz result pages, etc.):

   ```ts
   export default async function Page(
     { searchParams }: { searchParams: Promise<{ filter?: string; page?: string }> }
   ) {
     const { filter, page } = await searchParams;
   }
   ```

### Sync-access regression guard

After every dynamic-route addition, the orchestrator runs:

```bash
grep -nE "(params|searchParams)\.\w+" web/src/app/**/*.tsx
```

Every match must be on a line preceded by `await` (or destructured from an awaited variable). The only acceptable miss is a JSDoc warning string that *describes* the anti-pattern. Real-code matches that aren't `await`-prefixed are runtime regressions — fix inline before continuing. This grep is part of the standard Phase C verification gate before any commit that touches dynamic routes.

---

## Why each agent doesn't reinvent this

The Ead Financial Stage 1E Step 3 plan made `[slug]` the first dynamic-route precedent in the codebase. Without this canonical pattern documented:

- Agent B (services) had to read `web/node_modules/next/dist/docs/01-app/01-getting-started/03-layouts-and-pages.md` directly to derive the right shape.
- Future agents (niche-landings `[slug]`, blog `[slug]`, service-areas `[city]`) would each have to do the same derivation, with chance of drift each time.

With this pattern documented:

- Agent briefs cite this pattern by index (`see knowledge/patterns/next-16-dynamic-route-promise-params.md`) and the agent reads the canonical example directly.
- The orchestrator's verification grep is the same across all dynamic routes.
- Drift between routes is impossible because all of them copy the same shape.

---

## When NOT to use this pattern

- **Static routes** (`/about`, `/contact`, `/faq`) do not have `params` and don't need any of this. They can be regular synchronous server components or client components.
- **Pre-Next-16 codebases** still use synchronous `params`. Do not retrofit this pattern onto Next 13/14 — the type signature `Promise<...>` will break those.
- **Route Handlers (`app/api/*/route.ts`)** receive `params` as `Promise<...>` only for Next 16+. Same `await` pattern applies inside handler functions if they access route params.

---

## Worked example pulled from production

`c:/Projects/John-Ead/web/src/app/services/[slug]/page.tsx` (lines 73–115 condensed). 6 services prerendered at build time via `generateStaticParams`. `next build` SSG output: `✓ Generating static pages using 11 workers (15/15) in 549ms`, with all 6 slug paths emitted (`tax-preparation`, `outsourced-accounting`, `tax-strategy-cfo-advisory`, `taxpayer-representation`, `quickbooks-cleanup`, `entity-setup-formation`).

---

## Compatibility notes

- **Compatible with `'use cache'`** (Next 16 caching primitive) — apply to data-fetching helpers used inside the page, not to the page export itself.
- **Compatible with `unstable_instant`** route export — declare on the page file alongside the async default export.
- **Compatible with Cache Components** (configured in `next.config.ts`).
- **Turbopack default** — works under Turbopack at dev and build (Next 16.2+).

---

## Related patterns

- **Pattern #62** — NichePage `type` discriminator for shared `[slug]` route. Sits on top of this pattern: same Promise-params shape, with discriminator-driven schema bundles emitted per page type.
- **Pattern #65** — Proactive `.next/` cache clear in multi-restart sessions. The `.next/` cache caches dynamic-route compilation; clearing pre-empts mysterious Turbopack panics during dynamic-route iteration.

---

## Failure mode if this pattern is not followed

Silent runtime regression. The page compiles, the build passes, the route appears in `next build` output as prerendered. At runtime, the slug is always `undefined`, every page hits `notFound()`, every URL returns 404. There is no console error, no build warning, no TypeScript error — the only signal is "all my dynamic routes 404 in production." The fix is the awaited destructure shown above. Cost of getting this right the first time: zero. Cost of debugging it after a production deploy: ~2 hours per route, plus the deploy rollback.

This is exactly the kind of silent-runtime-regression class that Pattern #65 (proactive cache clear) and the project-prime sync-access grep are designed to catch — but only if the canonical pattern is in the codebase to compare against. This pattern doc is the canonical reference.
