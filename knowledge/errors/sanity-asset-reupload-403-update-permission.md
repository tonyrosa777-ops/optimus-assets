# Error: Sanity Asset Re-upload Fails With "update" Permission Required
**Project:** Andrea Abella Marie
**Date:** Apr 14, 2026
**Phase:** Post-launch content automation

## Problem
Re-running a publish script (after a prior partial success) failed on the image upload step with a 403:

```
ClientError: transaction failed: Insufficient permissions; permission "update" required
  url: https://13idr5es.api.sanity.io/v2024-10-01/assets/images/production
  permission: "update"
  type: insufficientPermissionsError
```

What was confusing: the **first** run of the script uploaded the same image successfully and the script logged the asset ID. The **second** run — with the same file, same token — failed. Nothing had changed between runs.

## Root Cause
Sanity deduplicates image assets by **SHA-1 content hash**. When you upload a file whose bytes are already in the asset library, Sanity does not create a new asset — it treats the call as an update-reference to the existing asset.

That "update" is what the token needs permission for. The Contributor role scope for asset mutations is:
- First upload (new hash): treated as `create` → succeeds
- Re-upload (existing hash): treated as `update` on the existing asset → fails for Contributor

Same API call, different underlying mutation based on whether the content is already in the library.

## Solution
Upgrading to an Editor token solves it outright (Editor has `update` on assets). If you must stay on a Contributor token, add a fallback: catch the 403, look up the existing asset by SHA-1 via GROQ, reuse its ID instead of uploading.

```js
const buf = fs.readFileSync(imagePath);
let assetId;
try {
  const asset = await client.assets.upload("image", buf, { filename });
  assetId = asset._id;
} catch (err) {
  if (err?.statusCode === 403) {
    const sha1 = crypto.createHash("sha1").update(buf).digest("hex");
    const existing = await client.fetch(
      `*[_type=="sanity.imageAsset" && sha1hash==$sha1][0]._id`,
      { sha1 },
    );
    if (!existing) throw err;   // genuinely a permission problem, not a dedup one
    assetId = existing;
  } else {
    throw err;
  }
}
```

This makes the script idempotent under Contributor tokens — first run uploads, any subsequent run transparently reuses. No manual cleanup needed between runs.

## Prevention
- **Make every Sanity-mutating script idempotent from the first commit.** Assume it will be re-run — by you after fixing a bug, by CI, by the client. Design accordingly.
- Cache asset IDs via content-hash lookup, not via script-local memory. The dedup is already happening on Sanity's side; mirror that behaviour in your fallback.
- When a 403 shows up on a second run where the first succeeded, **the file didn't change — Sanity's view of the file did**. Check for dedup/existing-resource conditions before blaming the token.

## Related
- [[sanity-contributor-token-cannot-publish]] — same permission hierarchy surfaces on document mutations
- [[patterns/sanity-blog-post-publish-script]] — reusable script that bakes in this fallback
