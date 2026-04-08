# Error: Server Component with Metadata Cannot Use 'use client' to Fix Event Handlers
**Project:** Where2 Junk
**Date:** 2026-04-05
**Phase:** Nav + areas index page

## Problem
`/areas/page.tsx` was a Server Component that exported `metadata`. It had `onMouseEnter`/`onMouseLeave` event handlers on `<Link>` elements for hover styling. Next.js prerender crashed:

```
Error: Event handlers cannot be passed to Client Component props.
{href: ..., onMouseEnter: function onMouseEnter, onMouseLeave: ...}
```

The obvious fix (add `'use client'` at the top) was not viable — Next.js does not allow `export const metadata` in Client Components. Adding `'use client'` would break the metadata export.

## Root Cause
Two constraints in conflict:
1. Server Components cannot have JS event handlers
2. Client Components cannot export `metadata`

The existing error #8d assumes the fix is always `'use client'`. That's only valid when the component doesn't export metadata.

## Solution
Use CSS `:hover` rules in a `<style>` block within the Server Component instead of JS event handlers:

```tsx
export default function AreasPage() {
  return (
    <main>
      <style>{`
        .area-card:hover {
          border-color: var(--primary-muted) !important;
          background: var(--bg-elevated) !important;
        }
      `}</style>
      {/* Links get className="area-card" — no onMouseEnter needed */}
    </main>
  );
}
```

Alternatively, extract the interactive grid into a separate `AreasGrid` Client Component and keep the page as a Server Component that imports it.

## Prevention
- If a Server Component needs hover effects AND exports metadata: use CSS `:hover` in a `<style>` block
- Never reach for `'use client'` as the reflex fix when the component exports metadata
- The simpler pattern: any page-level server component should use CSS for hover, not JS event handlers

## Related
- Error #8d — Server Components with event handlers (general case)
