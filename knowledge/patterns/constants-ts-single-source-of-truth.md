# Pattern: constants.ts as Single Source of Truth for All Site Data
**Category:** Architecture / Maintenance
**First used:** Danielle Thompson — Apr 2026

## What
All site-wide data (phone, email, domain, commission dates, services, testimonials, FAQ, service area towns) lives in a single `src/lib/constants.ts` file. Components import from it rather than hardcoding values.

## When to Use
Any multi-page site where the same data (phone number, pricing, locations, credentials) appears in more than one component. Especially valuable for client sites that will need post-launch data updates.

## How
```ts
// src/lib/constants.ts
export const SITE = {
  phone: '(978) 201-8999',
  phoneTel: 'tel:+19782018999',
  email: 'danielle.thompson8913@outlook.com',
  commission: {
    notarySince: 'May 2025',
    expires: '2032',
  },
}

export const TESTIMONIALS = [ ... ]
export const NOTARY_SERVICES = [ ... ]
export const FAQ_ITEMS = [ ... ]
export const SERVICE_AREA_TOWNS = [ ... ]
```

Components import:
```tsx
import { SITE, NOTARY_SERVICES } from '@/lib/constants'
```

## Key Rules
- Every piece of client-specific data goes here first — never hardcode in a component
- When a client sends an update (phone, dates, prices), only one file changes
- Some components may also have hardcoded instances (copied during rapid build) — audit with grep before claiming "updated site-wide"
- Rate fields in data arrays have rendering constraints — check the UI before setting long values

## Reuse Condition
All client marketing sites. Always.

## Related
- [[errors/rate-badge-overflow-whitespace-nowrap]]
- [[errors/ctabanner-prop-name-mismatch-build-failure]]
