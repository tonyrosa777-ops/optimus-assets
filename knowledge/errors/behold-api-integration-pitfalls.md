# Error: Behold API Integration Pitfalls
**Project:** Gray Method Training
**Date:** Apr 2026
**Phase:** Instagram feed integration (Phase 6 rewrite)

## Problem
Three separate bugs hit back-to-back during the Behold.so Instagram feed integration:

**Bug 1 — Sizes nesting mismatch**
The Behold API v2 nests image URLs under `sizes.medium.mediaUrl`, not at the top level. Initial code assumed flat `mediaUrl` on each post object, resulting in empty strings for all image URLs — the feed rendered placeholders even with a valid Feed ID.

**Bug 2 — Double URL construction**
Behold's UI shows the full feed URL (`https://feeds.behold.so/FT4dGHFQI7MOPZ0ZbQDL`), not just the bare ID. The env var was set to the full URL, but the code was constructing: `https://feeds.behold.so/${feedId}`, resulting in `https://feeds.behold.so/https://feeds.behold.so/...`. The fetch silently returned an empty response.

**Bug 3 — CDN priority order reversed**
After fixing the nesting, the `mediaUrl` fallback chain was still wrong: `post.mediaUrl` (Instagram CDN with expiry tokens like `scontent-sof1-*.cdninstagram.com`) was preferred over `post.sizes?.medium?.mediaUrl` (stable Behold CDN at `behold.pictures/...`). Instagram CDN tokens expire, causing images to break within hours.

## Root Cause
- **Bug 1**: Behold's own documentation example implied flat `mediaUrl`; actual API response uses a `sizes` object with size variants
- **Bug 2**: The Behold UI copy button copies the full URL, not the bare ID — reasonable assumption to env-var the full URL; code didn't account for this
- **Bug 3**: The fallback chain was written with `post.mediaUrl` first before the `sizes.*` chain was added; when `BeholdPostRaw` type was added the priority wasn't reassessed

## Solution
**Bug 1**: Add a `BeholdPostRaw` interface with the actual `sizes` shape and normalize in the fetcher:
```typescript
interface BeholdPostRaw {
  sizes?: {
    small?: BeholdSize;
    medium?: BeholdSize;
    large?: BeholdSize;
    full?: BeholdSize;
  };
  mediaUrl?: string; // Instagram CDN (legacy/fallback only)
}
```

**Bug 2**: Add a URL guard at the top of `fetchInstagramPosts`:
```typescript
const feedUrl = feedId.startsWith("https://")
  ? feedId
  : `https://feeds.behold.so/${feedId}`;
```

**Bug 3**: Correct priority order — prefer stable Behold CDN, fall back to Instagram CDN only when `sizes` are absent:
```typescript
mediaUrl:
  post.sizes?.medium?.mediaUrl ??
  post.sizes?.large?.mediaUrl ??
  post.sizes?.full?.mediaUrl ??
  post.sizes?.small?.mediaUrl ??
  post.mediaUrl ?? // last resort — Instagram CDN, may expire
  "",
```

## Prevention
1. When integrating a new API, paste a real response payload into the conversation before writing types — never trust documentation examples alone
2. Always guard env vars that may contain a full URL vs. a bare ID: `value.startsWith("https://") ? value : baseUrl + value`
3. When building a URL fallback chain, explicitly comment which source is most stable — review priority order before committing
4. Behold returns `sizes.medium.mediaUrl` (stable CDN) AND `mediaUrl` (Instagram CDN); always prefer the `sizes.*` chain

## Related
- [[patterns/behold-instagram-feed]] — full Behold.so integration pattern
