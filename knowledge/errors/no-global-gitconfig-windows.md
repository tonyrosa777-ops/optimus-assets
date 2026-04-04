# Error: No Global .gitconfig on Windows — Git User Identity Missing
**Project:** Cody's Complete Junk Removal
**Date:** Apr 2026
**Phase:** Git setup / push to GitHub

## Problem
Running `git config --global user.name` on a Windows machine returned exit code 1 with "unable to read config file 'C:/Users/Anthony/.gitconfig': No such file or directory". The file simply didn't exist — this was a fresh Windows environment with Git installed but never configured globally. Commits would fail or attribute to no identity.

## Root Cause
Global git identity is not set by the Git for Windows installer by default. On a new machine or user account, `~/.gitconfig` doesn't exist until explicitly created. This is distinct from Error #13 (wrong email in existing config).

## Solution
Set identity at the repo level:
```bash
git config user.name "tonyrosa777-ops"
git config user.email "tonyrosa777@gmail.com"
```
(No `--global` flag — sets per-repo config instead.)

## Prevention
**Rule:** Before first commit on any project, always check `git config user.name` and `git config user.email`. If either returns empty or errors, set them before committing. Prefer per-repo config (`--local`) when global is unavailable or untrusted.

Also check: does `~/.gitconfig` exist? If not, the machine has never had git configured globally.

## Related
- [[errors/vercel-deploy-blocked-git-email-mismatch]]
