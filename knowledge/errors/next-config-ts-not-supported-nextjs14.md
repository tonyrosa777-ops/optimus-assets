# Error: next.config.ts Not Supported in Next.js 14
**Project:** Danielle Thompson
**Date:** Apr 2026
**Phase:** Project setup

## Problem
Project scaffolded with `next.config.ts` (TypeScript). Next.js 14 does not support `.ts` config files — only `.js` or `.mjs`. Results in a silent failure or ignored config depending on version.

## Root Cause
Next.js 15 introduced `next.config.ts` support. Next.js 14 (which this project used) requires `next.config.mjs` for ESM or `next.config.js` for CJS.

## Solution
Rename the file:
```bash
mv next.config.ts next.config.mjs
```
Update the content to use ESM exports:
```js
// next.config.mjs
/** @type {import('next').NextConfig} */
const nextConfig = { ... }
export default nextConfig
```

## Prevention
- When scaffolding a Next.js 14 project, always use `next.config.mjs`
- Check `package.json` for Next.js version before deciding config file extension
- Next.js 15+: `.ts` is fine. Next.js 14 and below: must use `.mjs`

## Related
None
