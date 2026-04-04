# Pattern: Hero Concept Prototyping — Budget for 3 Iterations

**Category:** Workflow / Animation
**First used:** Placed Right Fence — Apr 2026

## What
The hero section takes the most iteration of any section on the site. Budget for 2–3 full concept replacements before the final hero ships. Treat each attempt as a learning, not a failure.

## When to Use
Every project. The hero is the highest-stakes UI surface — it drives first impression, brand perception, and conversion rate. Clients often can't articulate what they want until they see what they don't want.

## How
On Placed Right Fence, the hero went through 4 concepts before the final:
1. **AI before/after static images** — generated fal.ai frames, commissioned Kling video. Removed because static photos lacked energy.
2. **Full-bleed video loop** — cinematic but felt borrowed. Didn't differentiate the brand.
3. **Text-particle animation** — too abstract, no fence craft story.
4. **Canvas 2D forge animation** — pickets rising from forge sparks. Directly visualized the core brand promise. Kept.

Workflow:
1. Scaffold each concept in a standalone component (`HeroVideo.tsx`, `HeroForge.tsx`)
2. Swap into `page.tsx` — don't delete the previous until the new one is approved
3. Get visual approval before starting mobile calibration (calibration is costly if concept changes)

## Key Rules
- Do NOT start mobile/responsive calibration until the desktop concept is approved. Calibration takes 5–10 commits on complex animations.
- Keep prior concept components in the codebase until 2 sessions after approval — clients sometimes revert.
- The most on-brand concept is usually the most specific to the business, not the most technically impressive.

## Reuse Condition
Any project with a non-trivial hero animation or visual treatment. Safe to skip for simple text+image heroes.

## Related
- [[patterns/responsive-canvas-animation-breakpoint-layout]]
