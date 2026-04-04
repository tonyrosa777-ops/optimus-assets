# Error: Vercel Deploy Blocked by Git Email Mismatch
**Project:** Danielle Thompson
**Date:** Apr 2026
**Phase:** Deployment setup

## Problem
First commit pushed fine (before Vercel connected). After connecting GitHub → Vercel auto-deploy, all subsequent pushes failed silently — Vercel dashboard showed blocked deploys and sent email alerts. No build error, just rejected pipeline.

## Root Cause
Initial commits were made with `git config user.email "anthony@dev.local"` — a local placeholder that didn't match the GitHub account `tonyrosa777@gmail.com`. Vercel validates that the committer identity matches the connected GitHub account and rejects mismatched pushes.

## Solution
```bash
git config user.email "tonyrosa777@gmail.com"
git config user.name "Tony Rosa"
# Make an empty commit to trigger a clean deploy
git commit --allow-empty -m "Fix git identity — trigger redeploy"
git push
```

## Prevention
- Set correct git identity BEFORE the first commit on every project
- Run `git config user.email` to verify before pushing to any new repo
- Keep a `.gitconfig` entry at global level matching the GitHub account: `git config --global user.email "tonyrosa777@gmail.com"`

## Related
- Not the same as [[errors/vercel-subdirectory-404]] — this is identity/auth, not routing
