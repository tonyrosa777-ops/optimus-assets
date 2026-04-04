# Error: Generated Assets Not Committed With Task
**Project:** Enchanted Madison
**Date:** March 2026
**Phase:** Phase 2 (Asset generation)

---

## Problem
The fal.ai image generation script ran successfully and produced files in /public/images/, but those files were not committed in the same session. They had to be staged and pushed as a separate follow-up step ("we also need to stage and push all the image updates").

## Root Cause
The atomic commit rule was being applied to code only. Generated binary files were treated as a separate category that didn't need to follow the same rule.

## Solution
Generated files are part of the task that created them. The moment a script writes to /public, commit those files immediately as part of the task commit — not as a follow-up.

Commit message format:
`feat(assets): generate [description] images via fal.ai`

## Prevention
Standing Order #14 added to `CLAUDE.md`:
> Any script that outputs files into /public must commit those files as part of the same task commit. Generated images, videos, and data files are never a separate follow-up step.

## Related
- [[patterns/fal-ai-image-generation]]
- See CLAUDE.md Standing Order #14
