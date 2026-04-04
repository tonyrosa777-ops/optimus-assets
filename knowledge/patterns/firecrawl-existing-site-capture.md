# Pattern: Firecrawl Existing Site Capture as Project Brief
**Category:** Workflow / Discovery
**First used:** Cody's Complete Junk Removal — Apr 2026

## What
Before starting a redesign or new build for a client with an existing website, use `firecrawl_scrape` to capture all current site content into a structured `.md` file. This becomes the project's content source of truth.

## When to Use
- Client has an existing website (any platform — WordPress, Wix, Squarespace, etc.)
- Client hasn't filled out a content questionnaire
- You need to know: phone, email, address, services, pricing, testimonials, FAQs, hours, social links
- You want to extract copy from an existing site without manually transcribing it

## How
1. Run `firecrawl_scrape` on each page with `formats: ["markdown", "links"]` and `onlyMainContent: false`
2. Run pages in parallel (home + contact at minimum; add any other visible pages)
3. Compile into `inital-website_data.md` (or similar name) in the project root
4. Structure the file with clear sections: Site Overview, Page-by-Page Content, Pricing, FAQs, Reviews, Contact, Social, Technical Notes
5. Reference this file throughout the build instead of asking the client for content

```ts
// Example scrape call
await firecrawl_scrape({
  url: "https://client-site.com/",
  formats: ["markdown", "links"],
  onlyMainContent: false
});
```

## Key Rules
- Scrape ALL visible pages, not just home — contact pages often have the most structured data (address, hours, email)
- If images are lazy-loaded (common on WordPress), don't trust image URLs from the scrape — they'll be SVG placeholders
- Store the file in the project root alongside CLAUDE.md; commit it so it's part of the build record
- Note the platform (WordPress, Wix, etc.) in the file — informs what can be salvaged vs rebuilt

## Reuse Condition
Any project where client has an existing site. Especially valuable for local service businesses whose content exists but isn't organized for a modern build.

## Related
- [[errors/printful-cdn-image-url-fabricated]] — image lazy-loading problem also applies here
