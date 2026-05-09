# Pattern: NichePage `type` discriminator for shared `[slug]` dynamic route

**Category:** Architecture / SEO Schema / Data Modeling
**First used:** Ead Financial — 2026-05-08

## What

A `type: "vertical" | "funnel"` discriminator field on a `NichePage` data interface that lets a single Next.js dynamic `[slug]` route emit **different JSON-LD schema bundles per page type** while sharing one route file, one section template, and one rendering surface. Replaces both (a) three hand-built `page.tsx` files (one per niche page) and (b) a one-shape-fits-all `[slug]` route that generates the wrong schema for some pages.

## When to Use

When the build has **multiple "niche landing" pages with mostly-similar structure but mixed schema requirements**. Concrete trigger: 2+ `nicheLandings[]` entries where some are SEO-targeted vertical landing pages (FAQPage + Service + Person + LocalBusiness schema bundle) and others are behavioral conversion-funnel pages (HowTo + LocalBusiness schema bundle).

Ead Financial example:
- `/cpa-for-treatment-centers-maine` → SEO niche-vertical → `type: "vertical"` (FAQPage + Service + Person + LocalBusiness)
- `/cpa-for-contractors-new-england` → SEO niche-vertical → `type: "vertical"` (same bundle)
- `/switching-cpas` → behavioral-timing-funnel → `type: "funnel"` (HowTo + LocalBusiness — different shape)

Without the discriminator, two paths both fail:
- **Three hand-built pages**: code duplication (same lossFrame + mechanism + FAQs + CTA shape every time), three sets of schema generation logic, three sets of metadata generators. Future niches add proportional code.
- **One-shape `[slug]` route emitting Service schema for everything**: the `/switching-cpas` page gets Service schema when it should be HowTo schema, breaks the AEO citation case the funnel page exists to win.

## How

Step 1 — extend the `NichePage` interface in `/data/site.ts`:

```ts
export interface NichePage {
  slug: string;

  /**
   * Schema-shape discriminator for the dynamic `[slug]` route generator.
   *
   * - `"vertical"` — SEO-targeted niche page (treatment-center, contractor).
   *   Schema bundle: FAQPage + Service + Person (named author byline) + LocalBusiness.
   *   Hero pattern: lossFrame intro → mechanism sections → trust strip → FAQs → CTA.
   *
   * - `"funnel"` — behavioral / conversion-funnel page (switching-cpas).
   *   Schema bundle: HowTo (step-by-step process) + LocalBusiness.
   *   Hero pattern: timing exploit copy → walkthrough steps → FAQs → CTA.
   */
  type: "vertical" | "funnel";

  speakableSummary: string;       // 40–60 word AEO bait
  eyebrow: string;
  heading: string;                // [em]…[/em] markers for italic-emphasis brass
  subhead: string;
  trustStrip: string[];
  sections: NicheLandingSection[]; // each with lossFrame paragraph + mechanism[]
  faqs: { q: string; a: string }[];
  closingCta: { heading: string; body: string; label: string; href: string };
  metaTitle: string;
  metaDescription: string;
}
```

Step 2 — populate each entry with the correct discriminator value:

```ts
nicheLandings: [
  { slug: "cpa-for-treatment-centers-maine", type: "vertical", /* ... */ },
  { slug: "cpa-for-contractors-new-england", type: "vertical", /* ... */ },
  { slug: "switching-cpas", type: "funnel", /* ... */ },
],
```

Step 3 — branch on `nichePage.type` in the route's schema generator. Single `app/[slug]/page.tsx` file (or a route group that captures niche slugs):

```ts
function buildSchemaBundle(page: NichePage, brand: BrandConfig): SchemaBundle {
  switch (page.type) {
    case "vertical":
      return {
        faqPage: buildFAQPageSchema(page.faqs),
        service: buildServiceSchema(page, brand),
        person: buildPersonSchema(brand),
        localBusiness: buildLocalBusinessSchema(brand),
      };
    case "funnel":
      return {
        howTo: buildHowToSchema(page.sections),  // each section's lossFrame + mechanism becomes a HowTo step
        localBusiness: buildLocalBusinessSchema(brand),
      };
    // TypeScript exhaustiveness check fails build if a future type isn't handled
    default: {
      const _exhaustive: never = page.type;
      return _exhaustive;
    }
  }
}
```

Step 4 — section rendering can stay shared (lossFrame + mechanism + FAQs + CTA structure works for both types). If divergent rendering is ever needed (e.g., `funnel` pages need a numbered step indicator), branch in the page component as well.

## Key Rules

- **The discriminator field is on the DATA interface, not on the route file.** Keeps the route generator pure-functional — `(page: NichePage) → SchemaBundle` — and lets future niches add zero code: adding a 4th entry to `nicheLandings[]` with `type: "vertical"` works immediately.
- **TypeScript exhaustiveness check via `never` in the default branch.** Adding a future type literal (`type: "vertical" | "funnel" | "comparison"`) without updating the `switch` statement fails the build. This is the safety net that distinguishes the discriminator pattern from a stringly-typed enum — if a future maintainer adds a new niche type and forgets the schema generator, build breaks loudly.
- **Each schema bundle reflects the page's AEO target query class.** Vertical pages target navigational/commercial queries ("CPA for treatment center Maine") — Service + FAQPage + Person schema feeds the answer engine. Funnel pages target intent-driven action queries ("how do I switch CPAs") — HowTo schema feeds the same engine but with step-by-step structured data. Mismatched schema kills the AEO citation case, which is the whole reason the page exists.
- **Section content shape is shared, schema shape is divergent.** Both page types have the same `sections[]` array structure — `lossFrame` paragraph + `mechanism[]` items. The `funnel` schema generator interprets each section as a HowTo step; the `vertical` schema generator interprets the FAQs separately and the sections as supporting content. Same data, different schema interpretation.

## Reuse Condition

This pattern applies on every Optimus build with **2+ niche landing pages of mixed schema types**. Triggers:
- Service business with multiple verticals (financial: treatment center + contractor + S-corp)
- Behavioral funnel page on top of SEO niche pages (switching, comparison, cleanup)
- Future build adds a 3rd type (e.g., `type: "comparison"` for "Ead vs Honeck O'Toole" pages with structured Comparison schema)

Less applicable when:
- Only one niche landing page (no schema-shape mismatch problem to solve)
- All niche pages share the same schema bundle (overengineering — just use one route shape)

## Related

- [[patterns/firecrawl-existing-site-capture-as-project-brief]] (Pattern #19) — the niche-content discovery method that feeds this pattern
- design-system.md §11 Sections Matrix — where the niche landing pages are flagged as custom builds
- design-system.md §12 Subsection 6 (Loss-Aversion Framing) — content rules for the `vertical` and `funnel` page types
