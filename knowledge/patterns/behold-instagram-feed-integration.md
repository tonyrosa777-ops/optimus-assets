# Pattern: Behold.so Instagram Feed Integration

**Category:** Third-Party Integration / Social Media  
**Project:** Gray Method Training  
**Date:** Apr 2026  
**Status:** Validated in production  
**Required on every build:** NO — optional feature, use when client wants live Instagram feed  

---

## What It Is and Why

Behold.so is a managed Instagram feed service that sits between your Next.js app and the Instagram Graph API. Instead of creating a Meta Developer App, managing OAuth tokens, and building a cron job to refresh a 60-day access token — you point Behold at the client's Instagram account once, and Behold handles everything permanently.

The feed is served as a plain public JSON endpoint. Your app fetches it like any other API.

**Zero maintenance surface.** No tokens to rotate, no developer console to manage, no third-party infrastructure to operate. Free tier refreshes every 24 hours — appropriate for most content cadences.

---

## What the Old Approach Required (never do this)

The naïve approach hits the Instagram Graph API directly and requires:

- Meta Developer App creation (client needs a Facebook Business account)
- `INSTAGRAM_ACCESS_TOKEN` — expires every 60 days
- `INSTAGRAM_BUSINESS_ACCOUNT_ID`
- `@upstash/redis` package + `UPSTASH_REDIS_REST_URL` + `UPSTASH_REDIS_REST_TOKEN`
- `src/lib/token-store.ts` — reads/writes token from Redis
- `src/app/api/cron/refresh-instagram/route.ts` — hits Graph API refresh endpoint monthly
- `vercel.json` cron schedule (`"0 0 1 * *"`)
- `CRON_SECRET` env var

**All of that is replaced by one env var with Behold.**

---

## Client Setup (5 minutes, done by client)

1. Client goes to [behold.so](https://behold.so), creates a free account
2. Clicks **Create Feed** → connects their Instagram (Business or Creator account required — personal accounts do NOT work)
3. Instagram OAuth popup appears, client approves
4. Feed is created → client copies the **Feed ID** (random alphanumeric string, e.g. `aBcDeFgHiJkLmNoP`)
5. Client sends you the Feed ID — that is the only thing you ever need from them

---

## Environment Variable

```env
NEXT_PUBLIC_BEHOLD_FEED_ID=aBcDeFgHiJkLmNoP
```

`NEXT_PUBLIC_` is correct — the feed endpoint is already public. The Feed ID is not a secret.
Behold's CDN URL: `https://feeds.behold.so/{FEED_ID}`

---

## Data Layer — `src/lib/instagram.ts`

```ts
export interface BeholdPost {
  id: string;
  mediaType: "IMAGE" | "VIDEO" | "CAROUSEL_ALBUM";
  mediaUrl: string;
  thumbnailUrl?: string;  // VIDEO posts only — use as poster image
  permalink: string;
  caption?: string;
  timestamp: string;
}

// IMPORTANT: Behold uses camelCase (mediaUrl, mediaType, thumbnailUrl)
// The raw Instagram Graph API uses snake_case (media_url, media_type, thumbnail_url)
// These are different. Do not mix them up if refactoring.

export async function fetchInstagramPosts(limit = 9): Promise<BeholdPost[]> {
  const feedId = process.env.NEXT_PUBLIC_BEHOLD_FEED_ID;
  if (!feedId) return [];

  try {
    const res = await fetch(`https://feeds.behold.so/${feedId}`, {
      next: { revalidate: 3600 }, // hourly ISR
    });
    if (!res.ok) return [];
    const data = await res.json();
    return (data as BeholdPost[]).slice(0, limit);
  } catch {
    return []; // always returns safe empty array — never throws
  }
}

export function truncateCaption(caption: string | undefined, maxLen = 100): string {
  if (!caption) return "";
  return caption.length > maxLen ? caption.slice(0, maxLen) + "…" : caption;
}
```

---

## Section Component — `src/components/sections/InstagramFeed.tsx`

Async server component. No client state, no loading flash, no `useEffect`.

```tsx
import { fetchInstagramPosts, truncateCaption, BeholdPost } from "@/lib/instagram";

export default async function InstagramFeed() {
  const posts = await fetchInstagramPosts(9);
  const isEmpty = posts.length === 0;

  return (
    <section className="py-20 bg-[var(--bg-base)]">
      <div className="container mx-auto px-4">
        <h2 className="font-display text-3xl text-center mb-12">Follow Along</h2>
        <div className="grid grid-cols-3 gap-2">
          {isEmpty
            ? Array.from({ length: 9 }).map((_, i) => <PlaceholderTile key={i} />)
            : posts.map((post) => <PostTile key={post.id} post={post} />)
          }
        </div>
      </div>
    </section>
  );
}

function PostTile({ post }: { post: BeholdPost }) {
  const isVideo = post.mediaType === "VIDEO";
  const isCarousel = post.mediaType === "CAROUSEL_ALBUM";
  const imgSrc = isVideo ? (post.thumbnailUrl ?? post.mediaUrl) : post.mediaUrl;

  return (
    <a href={post.permalink} target="_blank" rel="noopener noreferrer"
      className="relative aspect-square overflow-hidden group block">
      {/* Use plain <img> not next/image — Behold CDN domain isn't stable enough for remotePatterns */}
      <img src={imgSrc} alt={truncateCaption(post.caption, 40)}
        loading="lazy" className="w-full h-full object-cover transition-transform duration-300 group-hover:scale-105" />

      {/* Carousel indicator */}
      {isCarousel && (
        <div className="absolute top-2 right-2 text-white text-xs">⧉</div>
      )}

      {/* Hover overlay */}
      <div className="absolute inset-0 bg-black/60 backdrop-blur-sm opacity-0 group-hover:opacity-100
        transition-opacity duration-300 flex flex-col items-center justify-center p-3 text-center">
        <span className="text-2xl mb-2">📷</span>
        <p className="text-white text-xs leading-tight">
          {truncateCaption(post.caption, 100)}
        </p>
      </div>
    </a>
  );
}

function PlaceholderTile() {
  return (
    <div className="aspect-square bg-[var(--bg-card)] flex items-center justify-center">
      <span className="text-[var(--text-muted)] text-2xl">📷</span>
    </div>
  );
}
```

**Why `<img>` not `next/image`:** Behold proxies images through their own CDN. The exact domain isn't predictable without testing a specific account, and adding a wildcard to `remotePatterns` is a security risk. For a 3×3 grid of small thumbnails, native lazy-loading is the right tradeoff.

---

## API Route — `src/app/api/instagram/route.ts`

Thin wrapper for any client component that needs the feed at runtime.
The section component bypasses this and calls `fetchInstagramPosts` directly server-side.

```ts
export const revalidate = 3600;

export async function GET() {
  const posts = await fetchInstagramPosts(12);
  return NextResponse.json({ posts });
}
```

---

## Fallback Behavior

| State | What renders |
|-------|-------------|
| Feed ID not set | 9 placeholder tiles |
| Behold fetch fails | 9 placeholder tiles |
| Feed ID set, posts returned | Live 3×3 grid with hover overlays |

The section never breaks or collapses regardless of integration state. Always render 9 tiles.

---

## Env Var Summary

| Var | Scope | What |
|-----|-------|------|
| `NEXT_PUBLIC_BEHOLD_FEED_ID` | `.env.local` + Vercel | Feed ID from Behold dashboard |

That's the only variable. One var replaces the entire Graph API + Redis + cron infrastructure.

---

## When to Use

- Client has an active Instagram presence and wants it on the site
- Client has a Business or Creator Instagram account (not personal)
- Client can spend 5 minutes doing the Behold OAuth flow
- You want zero ongoing maintenance on the integration

## When NOT to Use

- Client only has a personal Instagram account (Behold won't work)
- Client wants real-time feed (free tier is 24h refresh — paid plans are faster)
- Client refuses to connect a third-party service to their Instagram

---

## Reference Implementation

`c:\Projects\Gray-Method-Training\src\` — `lib/instagram.ts`, `components/sections/InstagramFeed.tsx`, `app/api/instagram/route.ts`
