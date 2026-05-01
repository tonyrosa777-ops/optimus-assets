# vercel-subdirectory-404
**Author:** Optimus Business Solutions  
**Type:** Deployment Fix — Reusable  
**Validated:** Enchanted Madison build, March 2026

---

## Description

Fixes the `NOT_FOUND` / 404 error on Vercel when a Next.js app lives inside a subdirectory of the repo. This is a **three-layered problem** — fixing only one layer is not enough. All three must be resolved in the correct order.

**Trigger this skill when:**
- Vercel deployment succeeds (build logs show output) but the live URL returns 404 on every route
- The build time is suspiciously short (e.g., 158ms) — this means Vercel served nothing
- The repo root contains planning docs or config files alongside the app folder
- `package.json` is not at the repo root
- Redeploying from the Vercel dashboard doesn't fix it

---

## The Three Layered Problems

### Problem 1 — Framework Preset is null
Vercel didn't detect the project as Next.js. Even if `next build` runs, without the Framework Preset set to Next.js, Vercel never applies the `@vercel/next` routing adapter. It has no idea how to serve the output. Every route returns 404.

**Symptom:** Build completes but all pages 404. Build log shows output but no routes are recognized.

---

### Problem 2 — Root Directory not set
The repo has planning/config files at the root and the actual Next.js app inside a subdirectory. Vercel builds from the repo root by default — no `package.json` there, nothing to serve.

```
repo-root/                ← Vercel builds from here by default
  CLAUDE.md
  progress.md
  design-system.md
  your-app-name/          ← actual Next.js app is here
    package.json
    src/
    next.config.ts
```

**Symptom:** Build time is extremely short (under 1 second). Vercel found nothing at the root.

---

### Problem 3 — Dashboard "Redeploy" reuses a stale snapshot
When you click **Redeploy** in the Vercel dashboard, it does NOT re-fetch from GitHub. It reuses the source snapshot from the previous deployment. So if Root Directory was already set to `your-app-name` when you redeploy, Vercel looks for `your-app-name/your-app-name/` inside the cached snapshot — that path doesn't exist — and the build fails with "directory does not exist."

**Symptom:** You've already set Root Directory correctly in the dashboard, but redeploying still fails or still 404s.

---

## The Fix — Execute in This Exact Order

### Step 1 — Set Framework Preset
Vercel Dashboard → Project → **Settings → Build & Deployment Settings**  
→ **Framework Preset** → select **Next.js**

This applies the `@vercel/next` routing adapter so Vercel knows how to serve pages.

---

### Step 2 — Set Root Directory
Same settings page:  
→ **Root Directory** → type the exact name of your app subfolder (e.g., `enchanted-madison`)

This points Vercel at the directory containing `package.json` instead of the repo root.

> **Do not rely on `vercel.json` as the fix.** If the project is already linked in the Vercel dashboard, the dashboard Root Directory setting takes priority over `vercel.json`. Use the dashboard.

---

### Step 3 — Push a new commit to GitHub
**Do NOT click Redeploy in the dashboard.** Push an actual commit instead.

```bash
git add .
git commit -m "fix(deploy): trigger fresh Vercel build after root directory fix"
git push
```

This forces Vercel to do a **fresh clone** of the repo rather than reuse the stale snapshot from a previous deployment. The fresh clone correctly resolves the subdirectory path and builds clean.

**This step is non-negotiable.** Dashboard redeploy will fail even after Steps 1 and 2 are correct because it reuses the old snapshot.

---

## How to Confirm It Worked

| Signal | Broken | Fixed |
|--------|--------|-------|
| Build time | ~158ms (serving nothing) | 20–30 seconds (full Next.js build) |
| Build log | No routes, no output | "X routes generated" |
| Live URL | 404 on every route | Site loads correctly |
| Framework detected | None / null | Next.js |

The jump from 158ms to 25 seconds with 18 routes generated is the exact confirmation signal from the validated fix.

---

## Prevention — Do This Before First Deploy on Any New Project

When creating a new Vercel project where the Next.js app lives in a subdirectory:

1. Vercel Dashboard → **Add New Project** → import the repo
2. **Before clicking Deploy**, expand Build & Deployment Settings
3. Set **Framework Preset** → Next.js
4. Set **Root Directory** → your app subfolder name
5. Then deploy

Setting both before the first deploy eliminates all three problems before they can occur.

---

## Why `vercel.json` Alone Doesn't Reliably Fix This

`vercel.json` with `{ "rootDirectory": "subfolder" }` works only when creating a brand new Vercel project that has never been deployed. For existing projects:

- The dashboard Root Directory setting overrides `vercel.json`
- Dashboard redeploy reuses a stale snapshot regardless of what's in `vercel.json`
- The framework adapter still won't be applied unless Framework Preset is set in the dashboard

Use the dashboard settings + a fresh git push. That's the only combination that works reliably.

---

## Version History

| Date | Notes |
|------|-------|
| March 2026 | Initial version — incorrect, based on `vercel.json` assumption |
| March 2026 | Rewritten from validated fix on Enchanted Madison build — three root causes identified and confirmed |
| 2026-04-30 | Integrity Chimney build hit this exact failure. `project-prime.md` step 6 had instructed creating `vercel.json` with `rootDirectory` at the repo root — Vercel ignored the unknown key, framework auto-detection failed (project.framework = null), and zero deployments were ever queued (deployments.count = 0). After deletion of the bogus vercel.json + setting Root Directory = `website` + Framework Preset = Next.js in the dashboard, the next git push deployed cleanly in 63s. Side-finding: when settings are changed AFTER an existing deployment exists, the dashboard surfaces a "Configuration Settings in the current Production deployment differ from your current Project Settings" banner — fix by pushing a fresh commit (an empty `git commit --allow-empty` is sufficient), which triggers a redeploy that picks up the new project settings. `project-prime.md` step 6 has been rewritten to forbid creating a root-level vercel.json. |
