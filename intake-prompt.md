---
name: intake
description: Structured business data intake — client website URL or raw-notes → initial-business-data.md. Mode A (URL crawl) or Mode B (discovery notes). Flags every unfillable field with ⚠️ NOT FOUND for Phase 2 gap resolution.
effort: high
---

# intake-prompt.md — Optimus Business Solutions
# Business Data Intake Command
# Save to: .claude/commands/intake.md → run /intake in Claude Code

---

You are performing the structured business data intake for a new Optimus client project.
Your output is a completely filled `initial-business-data.md` that will be the primary
input for `/market-research` and `/prime`. Every field you can answer from the source
material must be answered. Every field you cannot answer must be flagged — never left
blank and never invented.

---

## HOW TO USE

**Mode A — Client has an existing website:**
```
/intake https://clientwebsite.com
```
You will crawl the full site using Firecrawl, extract all accessible content, and
map it into `initial-business-data.md`.

**Mode B — Client has no website (discovery call or voice note transcription):**
Save the transcript or notes as `raw-notes.md` in the project root, then run:
```
/intake
```
You will read `raw-notes.md` and map it into `initial-business-data.md`.

---

## No cross-field generalization

Do not generalize one field's data into an adjacent field unless the extraction rules table below explicitly says to. Specifically:
- Never infer service radius from the service list (a plumbing company serving Orange County does not imply they also serve LA County).
- Never infer pricing from language like "competitive" or "affordable" — those are marketing words, not numbers. Flag pricing as `⚠️ NOT FOUND — confirm with client` if no concrete numbers appear.
- Never infer years-in-business from "established," "experienced," or "longtime" — those are vague. Flag if no year or duration appears.
- Never infer team size from "our team" or "the crew" — flag unless a headcount is stated.
- Never infer certifications from "licensed and insured" — flag the specific license numbers as `⚠️ NOT FOUND` unless they appear on the site.

When in doubt, flag `⚠️ NOT FOUND — confirm with client`. Over-flagging costs Anthony 1 minute in a Zoom call. Under-flagging (inventing a plausible-sounding value) puts a false claim on the client's site and exposes them to false-advertising liability.

---

## STEP 1 — GATHER THE SOURCE MATERIAL

**If a URL was provided (Mode A):**

1. Use `firecrawl_map` on the root domain to discover all pages
2. Use `firecrawl_scrape` on these priority pages (scrape each in order, stop if content
   is exhausted before reaching lower-priority pages):
   - Homepage
   - About / About Us / Our Story
   - Services / Work With Me / Packages / Programs / Pricing
   - FAQ
   - Contact
   - Any booking, shop, or checkout page
   - Blog index (first page only — for tone/copy style, not content)
   - Any page with testimonials or reviews
3. Concatenate all scraped content into a working document in memory before proceeding

**If no URL was provided (Mode B):**
Read `raw-notes.md` in full. This is your only source material.

---

## STEP 2 — FILL `initial-business-data.md`

Read the existing `initial-business-data.md` template. Fill every field using only
information present in the source material. Apply the extraction rules below for
each section.

Use this notation for any field you cannot fill from the source:
> `⚠️ NOT FOUND — confirm with client`

Do not remove template instruction comments. Do not invent plausible-sounding content.
If something is partially clear, fill what you know and flag the uncertain portion.

---

### Section 1 — Business Overview

| Field | Where to find it |
|-------|-----------------|
| Business Name | Site title, logo alt text, footer, meta title |
| Business Type | Infer from services offered and positioning language |
| Location | Contact page, footer, Google Maps embed, schema markup, address mentions |
| Base city | Where the business is physically located — physical address, Google Maps pin, "located in" mentions. Often different from service area. |
| Service area | The region they actually serve — "serving [area]", "we cover [region]", service area map, ZIP code lists. A contractor in Salem NH may serve all of southern NH + northern MA. |
| Tagline / elevator pitch | Homepage hero headline + subheadline (combine into 1–2 sentences) |
| Years in operation | About page, footer copyright year, "founded in" mentions |
| Current stage | Infer: new domain + thin content = pre-launch; established content + reviews = scaling |
| Brief description | Write 2–3 sentences synthesizing the homepage hero + about page first paragraph |

---

### Section 2 — Core Offering

| Field | Where to find it |
|-------|-----------------|
| Primary service/product | Lead offer on homepage + services page top item |
| Secondary offerings | All remaining items on services/packages page — list every one with its name |
| Pricing | Any price mentioned anywhere on the site — exact numbers, ranges, or "starting at" |
| Delivery format | Services page, FAQ, about page — look for in-person / online / hybrid signals |
| What makes it different | Any "why us", "our difference", "our approach" copy — quote it directly |
| Signature methodology | Named frameworks, processes, or programs with a proper name |
| Service radius | How far do they travel? Look for "within X miles", service area maps, ZIP code lists, "serving [radius]" language. If not stated: `⚠️ NOT FOUND — confirm with client` |
| Travel fee policy | One of: free within X miles / $Y per mile after Z miles / flat travel fee / no travel fee disclosed. Look in pricing, FAQ, and services pages. Important for service-area page content and pricing transparency. If not stated: `⚠️ NOT FOUND — confirm with client` |

**Note:** Copy pricing exactly as shown on the site. Do not round or estimate.
If no pricing is public, write: `⚠️ NOT FOUND — confirm with client`

---

### Section 3 — Target Audience

| Field | Where to find it |
|-------|-----------------|
| Ideal client description | "Who this is for", "designed for", "I work with" sections; hero subheadline |
| Geography | Location mentions in copy, "serving [area]", "clients across [region]" |
| Pain before finding business | Pain-point copy in hero, services page, FAQ — extract exact phrases |
| Transformation after | Result language, testimonials, outcome-focused headlines — extract exact phrases |
| Where they spend time online | Not usually on the site — write `⚠️ NOT FOUND — fill in market-research step` |
| What they search for | Meta descriptions, page titles, any SEO-visible keyword signals |
| What makes them hesitate | FAQ objection handling, "you might be wondering" sections, guarantee copy |
| What triggers their decision | Urgency language, limited availability, seasonal signals, scarcity copy |

---

### Section 4 — Brand Identity

| Field | Where to find it |
|-------|-----------------|
| Tone of voice | Read 10+ sentences of copy and describe the voice in 2–4 adjectives |
| Brand values | About page "our values", "we believe", "our mission" sections |
| Brand personality | Write one sentence synthesizing the tone + values + positioning |
| Visual references | Not findable from scrape — write `⚠️ NOT FOUND — confirm with client` |
| Colors currently in use | Extract primary/secondary hex codes from CSS or visible design if accessible |
| Fonts in use | Check font-family in page source or visible type specimens |
| Logo available | If site has a logo image: "yes — [describe it]". If text-only: "text mark only" |
| Photography available | Describe the type and quality of photos used on the site |

---

### Section 5 — Conversion & Tech

| Field | Where to find it |
|-------|-----------------|
| Domain | The URL itself |
| Primary conversion goal | What does the main CTA button do? Booking widget / form / phone / shop? |
| Booking or conversion tool | Look for embedded widgets. Known tools: Calendly, Acuity, Lodgify, OwnerRez, Shopify, Square, SimplyBook, Mindbody. Check iframes and script sources. |
| Schema type | Infer from business type. Common mappings: lodging → LodgingBusiness; local trade or service → LocalBusiness; coaching/consulting → ProfessionalService; restaurant → Restaurant; retail → Store; medical → MedicalBusiness. |
| Existing website | The URL (already known) |
| Existing analytics | Look for GA4 tags, Meta pixel, or other tracking in page source |
| Existing forms / lead tools | Look for Google Form iframes, Typeform embeds, Jotform links, survey links, quiz widgets — check iframe src attributes and linked forms in CTAs. List every one with its URL/type. These reveal custom build requirements. |
| Social profiles | Footer social icons, about page, contact page — list all with handles |

---

### Section 6 — Goals & Timeline

These fields are almost never on a public website. Write for all:
> `⚠️ NOT FOUND — confirm with client`

Exception: if a "coming soon" page or launch date is mentioned, capture it.

---

### Section 7 — Social Proof & Content Assets

| Field | Where to find it |
|-------|-----------------|
| Testimonials | Testimonials page, homepage quotes, review widgets — copy verbatim with names |
| Quantifiable results | "X clients served", "X years experience", "X star rating", "featured in X" |
| Press/media mentions | Footer logos, press page, "as seen in" sections |
| Certifications | About page, footer badges, credentials sections |
| Awards | About page, homepage proof section |
| Instagram handle | Footer, social links, any embedded feed |

**Copy up to 5 testimonials verbatim.** Include the name and any context (title, location, date).

---

### Section 8 — Competitive Context

Not usually findable from the client's own site.
Write for all fields:
> `⚠️ NOT FOUND — will be researched in market-intelligence step`

Exception: if the client's copy directly references competitors by name, note them.

---

## STEP 3 — WRITE THE OUTPUT

Overwrite `initial-business-data.md` with the fully filled version.
Preserve the template structure exactly — do not add or remove sections.
Preserve the instruction comments at the top of the file.

After writing the file, output a completion report:

```
INTAKE COMPLETE
───────────────
Sections fully filled:      [count] / 8
Fields needing client input: [list every ⚠️ field]
Source: [URL crawled or raw-notes.md]

Custom builds flagged:
  [List any features in Sections 2 or 5 that fall outside the Optimus
   base template (shop, blog, quiz, Instagram, hero, services, testimonials,
   pricing). E.g. reservation system, membership portal, live availability
   widget, multi-step application, custom gallery, map integration.
   If none identified: "Base template sufficient."]

Next step: run /market-research
```

---

Begin now. Confirm the intake mode, gather the source material, then fill and write
`initial-business-data.md`. Do not proceed to any other task.
