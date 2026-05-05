---
name: intake
description: Structured business data intake — client website URL or raw-notes → initial-business-data.md. Mode A (URL crawl) or Mode B (discovery notes), plus a mandatory external business grounding sweep across 10 public sources (GBP, FB, Yelp, HomeAdvisor/Angi, BBB, Nextdoor, state business registry, state license database, phone area-code, WHOIS). Goal is autonomy — fill every publicly findable field rather than flagging it for the human.
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

## STEP 1.5 — EXTERNAL BUSINESS GROUNDING (autonomous, mandatory in BOTH modes)

The goal is autonomy. Every LLC, contractor, and service business has a public footprint across registries and directories. Find it. Do NOT flag fields as `⚠️ NOT FOUND` until this step has run and produced nothing.

This step runs in BOTH Mode A and Mode B — every business has external grounding regardless of whether they have a website.

### Sources to search (search by exact business name + DBA / common variants if surfaced):

| Source | What to extract |
|---|---|
| Google Business Profile / Google Maps | Address, base city, phone, hours, services list, photo count, review count, average star, verified status |
| Facebook business page | Location, owner-presence signals (recent posts), review count, photo presence |
| Yelp | Address, services list, review count, average star |
| HomeAdvisor / Angi (or industry-equivalent — Houzz for design, Avvo for legal, Zocdoc for medical, etc.) | License badges shown, review count, services list, verified address |
| Better Business Bureau | Accreditation status, registered name, address, complaint history (count + recency) |
| Nextdoor | Community recommendation presence (count + tone of comments) |
| State business registry (Secretary of State / state corporation database) | Registered LLC legal name, registered agent, registered address, formation date, status (active/forfeit/dissolved) |
| State licensing database (niche-conditional — MA HIC, MA CSL, NH state contractor license, state cosmetology, state real estate, state medical board, etc.) | License numbers, license status, expiration, named license holder |
| Phone area-code lookup | Map area code(s) found in source material to served region — geographic consistency check against everything above |
| WHOIS for the domain (Mode A only) | Registrant name + address (often privacy-protected; useful when not) |

### Cross-reference logic

- **2+ sources agree → lock it in.** If GBP says Methuen and BBB says Methuen, base city is Methuen. Done.
- **Sources disagree → flag the discrepancy.** If GBP says Methuen and BBB says Lawrence, write the field as `Methuen, MA (per GBP + state registry); Lawrence, MA (per BBB) — ⚠️ DISCREPANCY` and let it surface in the summary. Never silently pick one.
- **Phone area-code consistency check.** If the area code's geographic region disagrees with the discovered base city (e.g., 978 area code with claimed location in Salem NH), flag the contradiction explicitly. It's usually a moved-business signal worth surfacing.
- **No external evidence found.** Field gets the standard `⚠️ NOT FOUND — confirm with client` flag, but only after all 10 sources have been searched. Sources searched + nothing-found notes get logged in the INTAKE COMPLETE summary so Anthony can see effort was made.

### Fields filled by Step 1.5 (overwriting `⚠️ NOT FOUND` from Step 1 wherever external evidence exists)

- **Section 1:** Location, Base city, Service area, Years in operation (use registry formation date if more authoritative than the about page)
- **Section 2:** Service radius (where stated on directories)
- **Section 4:** Photography available (real photos on FB / IG / Yelp / GBP — describe what's there + where), Logo (higher-quality logo file if surfaced externally)
- **Section 5:** Social profiles (every live link found, not just what was on the client site), Existing forms / lead tools (CTAs Yelp / GBP / FB push)
- **Section 7:** Testimonials (record platform list + count + average star — VERBATIM QUOTE pull is deferred to market-research where it gets mined for voice), Quantifiable results (years operating from registry date, total review count summed across platforms), Certifications (license numbers from state databases — MA HIC #, CSL #, etc., with verified-active flag)

### Fields Step 1.5 does NOT touch

- **Section 3** — Pain points, transformation, hesitation, decision triggers. These come from market-research's audience-psychology mining, not from the business's own footprint.
- **Section 6** — Goals, revenue targets, launch dates, constraints. Genuinely private; only the human can answer these.
- **Section 8** — Competitors. Market-research's job.

### Discipline

The bar for surfacing a `⚠️ NOT FOUND — confirm with client` flag on a Section 1, 2, 4, 5, or 7 field is now: "I searched all 10 sources above and found nothing." Over-flagging here is the failure mode — every flag that could have been filled by external research is process waste. Under-flagging (inventing a value not actually found in any source) remains the harder failure: false claim → false-advertising risk. So: search hard, fill what you find, flag the rest with the sources searched documented.

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
Fields needing client input: [list every ⚠️ field that survived Step 1.5]
Source: [URL crawled or raw-notes.md]

External grounding sources searched: [list all 10 sources, mark each FOUND / NOT FOUND]
External grounding fills:
  • Section 1 Location:       [e.g. "Methuen, MA — filled from GBP + state registry"]
  • Section 1 Base city:      [e.g. "Methuen, MA — filled from GBP + BBB"]
  • Section 1 Service area:   [e.g. "Merrimack Valley + southern NH — filled from HomeAdvisor service-area map"]
  • Section 4 Photography:    [e.g. "12 project photos on Yelp + 8 on FB"]
  • Section 5 Social profiles:[e.g. "FB, IG, Nextdoor — all linked"]
  • Section 7 Testimonials:   [e.g. "HomeAdvisor 23 reviews 4.9★, Google 41 reviews 4.8★, BBB A+ accredited"]
  • Section 7 Certifications: [e.g. "MA HIC #198765 verified active (expires 2027-08), MA CSL #CS-099887 verified"]
  [List every field that Step 1.5 filled. Empty if nothing was filled externally.]

Discrepancies flagged: [count + brief description, or "none"]
  [e.g. "1 — GBP shows Methuen MA, BBB shows Lawrence MA. Recorded both, flagged."]

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
