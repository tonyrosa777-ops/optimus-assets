# Error: Sanity Studio SSR Crash — createContext with Turbopack

**Project:** Placed Right Fence
**Date:** Apr 2026
**Phase:** Blog/CMS infrastructure (Session 4–5)

## Problem
Build was failing with a `createContext` error during SSR when the Sanity Studio was embedded at `/studio`. The error surfaced as a server-side crash during Next.js build with Turbopack enabled. The studio would not render and the entire route failed.

## Root Cause
`NextStudio` (from `next-sanity/studio`) uses React context internally. When the studio component was imported directly in a page file that also contained server-side exports, Turbopack's strict server/client boundary enforcement caused the `createContext` call to execute in a server context where it isn't valid.

## Solution
Two-file pattern: extract the studio into a dedicated client component file, then import it into the page with `dynamic()` to prevent SSR:

**`StudioClient.tsx`** (new file — must be first and only content):
```tsx
"use client";
import { NextStudio } from "next-sanity/studio";
import config from "../../../sanity.config";
export default function StudioClient() {
  return <NextStudio config={config} />;
}
```

**`page.tsx`** (studio route):
```tsx
import dynamic from "next/dynamic";
const StudioClient = dynamic(() => import("./StudioClient"), { ssr: false });
export default function StudioPage() {
  return <StudioClient />;
}
```

## Prevention
Any time you embed a third-party component that uses React context (Sanity Studio, rich-text editors, drag-and-drop libraries) in a Next.js App Router route:
1. Extract it into a dedicated `SomethingClient.tsx` file with `"use client"` as the absolute first line
2. Import with `dynamic(..., { ssr: false })` in the page file
3. Never co-locate server exports (generateMetadata, etc.) in the same file as context-heavy client components

## Related
- [[errors/turbopack-use-client-not-first-token]]
