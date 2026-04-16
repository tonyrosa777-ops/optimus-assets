# Pattern: Sanity Blog Post Publish Script (API-first, no Studio UI)
**Category:** CMS / Automation
**First used:** Andrea Abella Marie — Apr 14, 2026

## What
A reusable node script that reads a post JSON from `scripts/posts/<slug>.json`, uploads the matching image from `public/images/blog/<slug>.png` to Sanity, converts the legacy block format to Portable Text, and writes a `blogPost` document via `createOrReplace`. Lets the developer (or an agent) publish a finished post straight from the repo in one command — the client never has to touch Studio for routine publishes.

## When to Use
- CMS-backed blog where posts are written as markdown/JSON in the repo first (polished by an agent or the developer) before being published
- Content pipeline where the publish step is frequent enough that clicking through Studio each time is friction
- Client still wants Studio access for the occasional manual edit — but routine publishing is automated
- A publish step that bundles image generation → polish → publish into one predictable sequence

## How

### 1. File layout
```
scripts/
  posts/
    <slug>.json              ← post content in legacy block format
  prompts/
    <slug>.txt               ← fal.ai prompt
  generate-blog-image.mjs    ← companion image generator
  publish-blog-post.mjs      ← this script
public/images/blog/
  <slug>.png                 ← generated image, matches slug
```

### 2. Post JSON shape (`scripts/posts/<slug>.json`)

```json
{
  "title": "...",
  "excerpt": "...",
  "category": "Nervous System",
  "date": "2026-04-14",
  "readTime": "7 min read",
  "featured": false,
  "imageAlt": "Descriptive alt text for the cover image",
  "body": [
    { "type": "paragraph", "text": "..." },
    { "type": "heading", "text": "..." },
    { "type": "subheading", "text": "..." },
    { "type": "blockquote", "text": "..." },
    { "type": "list", "items": ["...", "..."] }
  ]
}
```

### 3. Script skeleton (`scripts/publish-blog-post.mjs`)

```js
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { createClient } from "@sanity/client";
import dotenv from "dotenv";

dotenv.config({ path: ".env.local" });

const slug = process.argv[2];
const post = JSON.parse(fs.readFileSync(`scripts/posts/${slug}.json`, "utf8"));
const imageBuf = fs.readFileSync(`public/images/blog/${slug}.png`);

const client = createClient({
  projectId: process.env.NEXT_PUBLIC_SANITY_PROJECT_ID,
  dataset: process.env.NEXT_PUBLIC_SANITY_DATASET,
  apiVersion: process.env.NEXT_PUBLIC_SANITY_API_VERSION,
  token: process.env.SANITY_API_EDITOR_TOKEN,  // Editor role required to publish
  useCdn: false,
});

// 1) Upload image (with SHA-1 fallback for re-runs, see Related)
let assetId;
try {
  const asset = await client.assets.upload("image", imageBuf, { filename: `${slug}.png` });
  assetId = asset._id;
} catch (err) {
  if (err?.statusCode === 403) {
    const sha1 = crypto.createHash("sha1").update(imageBuf).digest("hex");
    assetId = await client.fetch(
      `*[_type=="sanity.imageAsset" && sha1hash==$sha1][0]._id`, { sha1 });
    if (!assetId) throw err;
  } else { throw err; }
}

// 2) Convert legacy blocks → Portable Text (deterministic _keys via md5)
function blocksToPortableText(blocks) { /* same shape as migrate-to-sanity.ts */ }

// 3) createOrReplace — deterministic _id = idempotent re-runs
const docId = `blogPost-${slug}`;
await client.createOrReplace({
  _id: docId,
  _type: "blogPost",
  title: post.title,
  slug: { _type: "slug", current: slug },
  excerpt: post.excerpt,
  category: post.category,
  date: post.date,
  readTime: post.readTime,
  featured: post.featured ?? false,
  image: { _type: "image", asset: { _type: "reference", _ref: assetId }, alt: post.imageAlt },
  body: blocksToPortableText(post.body),
});

// 4) Clean up any leftover draft from earlier runs
try { await client.delete(`drafts.${docId}`); } catch {}
```

### 4. Usage
```bash
# 1. Generate the image
node scripts/generate-blog-image.mjs <slug> --prompt-file scripts/prompts/<slug>.txt
# 2. Write scripts/posts/<slug>.json by hand (or from an agent)
# 3. Publish
node scripts/publish-blog-post.mjs <slug>
```

## Key Rules

- **Deterministic `_id`** (`blogPost-<slug>`) + `createOrReplace` = idempotent. Re-running the script updates the document in place. Same pattern as the initial migration script.
- **Editor role token required** to publish directly. Contributor can only create drafts — see [[errors/sanity-contributor-token-cannot-publish]]. Pick the trust model before picking the role.
- **Keep the post JSON in the repo even though Sanity is the source of truth at render time.** The JSON is the *authored* form — if Sanity ever needs to be rebuilt or migrated, re-running this script from the JSON produces the same result.
- **Reuse the Portable Text converter from `migrate-to-sanity.ts`** — don't write a second implementation. Extract to a shared module (`scripts/lib/blocks-to-portable-text.ts`) once the second call site exists.
- **Always clean up the draft of the same ID after publishing** (`client.delete('drafts.' + docId)`). If the author had an in-progress Studio draft, or if an earlier Contributor-token attempt left a draft behind, Studio will show a stale "Draft" badge until you clear it.
- **Alt text goes in the post JSON** (`imageAlt`) — don't skip it. Accessibility + SEO win for free.

## Reuse Condition
- Any Sanity-backed blog where posts are generated/polished outside Studio (by agents, markdown-first workflows, or content teams working in VS Code)
- Pairs naturally with [[patterns/fal-ai-reusable-blog-image-generator]] — the generate+publish sequence becomes a two-command ritual
- The companion idempotent migration pattern already exists: this is the "add one post" version of that flow

## Related
- [[errors/sanity-contributor-token-cannot-publish]] — why Editor token is needed for this variant
- [[errors/sanity-asset-reupload-403-update-permission]] — the SHA-1 fallback handles re-runs cleanly
- [[patterns/fal-ai-reusable-blog-image-generator]] — companion image pipeline
- Andrea Abella Marie retrospective — initial Sanity migration script (bulk) that this extends into a single-post publish tool
