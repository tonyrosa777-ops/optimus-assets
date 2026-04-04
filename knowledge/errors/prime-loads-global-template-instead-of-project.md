# Error: /prime Loads Global Template Instead of Project-Specific Version
**Project:** Placed Right Fence
**Date:** April 2026
**Phase:** Phase 0 (session start)

---

## Problem
Running `/prime` inside a client project loaded the generic global template from `~/.claude/commands/prime.md` with unfilled `[BUSINESS_NAME]`, `[DOMAIN]`, etc. placeholders — instead of the project-specific version with real variables. Claude had no project context and had to re-read all files from scratch.

## Root Cause
Two causes:

1. **`/new-client` was not used** — the project was set up manually. `/new-client` Phase 4 automatically creates a project-scoped `.claude/commands/prime.md` with all 10 variables filled. When skipping `/new-client`, this step gets skipped too.

2. **Global command takes precedence when no project-scoped version exists** — Claude Code checks `~/.claude/commands/` globally. Without a `.claude/commands/prime.md` at the project root, it always falls back to the generic template.

## Solution
After Phase 0 completes (variables filled, design-system.md created), manually create the project-scoped command file:

```bash
mkdir -p "C:/Projects/[project-folder]/.claude/commands"
```

Then copy `project-prime.md` to `.claude/commands/prime.md` and replace all 10 `[VARIABLES]` with the real project values. Claude Code prioritizes the project-level `.claude/commands/prime.md` over the global one when running inside that project folder.

## Prevention
Added to `project-prime.md` Phase 0 checklist as a required step:
> `- [ ] .claude/commands/prime.md created with all 10 variables filled`

## Key Distinction
- `~/.claude/commands/prime.md` → global fallback, generic template, never has real project data
- `[project]/.claude/commands/prime.md` → project-scoped, filled variables, used during the build

## Related
- See `project-prime.md` Phase 0 checklist
- See `end-to-end-workflow.md` Phase 4 (this step is automated when using `/new-client`)
