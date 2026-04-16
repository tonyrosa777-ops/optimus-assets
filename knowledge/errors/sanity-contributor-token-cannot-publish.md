# Error: Sanity Contributor Token Cannot Publish Documents
**Project:** Andrea Abella Marie
**Date:** Apr 14, 2026
**Phase:** Post-launch content automation

## Problem
Built a script to publish new blog posts directly to Sanity via API using the client's existing **Contributor** role token. First attempt failed immediately:

```
ClientError: transaction failed: Insufficient permissions; permission "create" required
  statusCode: 403
  url: https://13idr5es.api.sanity.io/v2024-10-01/data/mutate/production
  type: insufficientPermissionsError
```

The token had been created with Sanity's **Contributor** role — assumed (incorrectly) that "Contributor" meant "can create content."

## Root Cause
Sanity's API token permission tiers, ranked ascending:

| Role | Can do |
|------|--------|
| Viewer | Read only |
| **Contributor** | Create/edit **own drafts only** — cannot publish |
| Editor | Full CRUD including publish |
| Administrator | Editor + schema/role management |

"Publishing" in Sanity means writing a document with an `_id` that does **not** start with `drafts.`. A Contributor token is explicitly scoped to draft-only mutations. Creating a non-draft document (even a brand new one) requires the `create` permission, which Contributor lacks.

Additionally, retrying the same script with a `drafts.` prefix partially worked — the draft document creation succeeded — but a second run failed the image re-upload step with `permission "update" required` (separate issue — see [[sanity-asset-reupload-403-update]]).

## Solution
Two valid paths:

### Path A — Editor token (autopublish, no human review)
Create a new token with **Editor** role at `https://www.sanity.io/manage/project/<PROJECT_ID>/api/tokens`, use that in the script, write documents to `blogPost-<slug>` (no `drafts.` prefix).

```js
const docId = `blogPost-${slug}`;  // publishes directly
await client.createOrReplace(doc);
```

### Path B — Contributor token (draft workflow, human publish step)
Keep the Contributor token (less dangerous if leaked). Write to a draft ID. Client reviews in Studio, clicks Publish.

```js
const docId = `drafts.blogPost-${slug}`;  // draft only
await client.createOrReplace(doc);
```

Picking between them:
- **Editor** if the script runs from a trusted place (local dev, CI) and the content has been pre-reviewed before the script runs.
- **Contributor** if the content pipeline involves any unreviewed step (AI draft, client-submitted, etc.) — the Studio "Publish" button becomes the human checkpoint.

For this project we picked Editor because the content is fully polished before the script is invoked.

## Prevention
- **Check the role when creating the token**, not when you hit a 403 later. Sanity's management UI shows role explicitly at creation.
- When writing scripts that mutate Sanity, document the required role in a comment at the top of the script:
  ```js
  // Requires SANITY_API_EDITOR_TOKEN (Editor role).
  // A Contributor token cannot publish; would need drafts.<id> workaround.
  ```
- If designing a content pipeline for a client, **default to Contributor + drafts workflow** unless the client explicitly wants no review step. Trust defaults should lean safer.
- After switching token roles, clean up any leftover draft from the earlier attempt or Studio will show a "Draft" badge alongside the published doc:
  ```js
  await client.delete(`drafts.${docId}`);  // ignore errors if no draft exists
  ```

## Related
- [[sanity-asset-reupload-403-update]] — same permission hierarchy surfaces a different 403 on image re-uploads
- [[patterns/sanity-blog-post-publish-script]] — the reusable script built around this learning
