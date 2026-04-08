# Pattern: Homepage Section Dark/Light Alternation Rhythm

**Category:** Visual Design / UX
**First used:** Placed Right Fence — Apr 2026

## What
On long homepages with 6+ stacked sections, alternating between dark and light backgrounds prevents visual monotony and creates natural scroll anchors that help users perceive distinct content zones.

## When to Use
Any homepage that stacks 5+ section components vertically. Especially critical when sections share similar card-based layouts — without background contrast they blur together.

## How
Assign backgrounds before building individual sections:

1. **Map the section order first** — list every section vertically
2. **Mark dark/light** — strict alternation: ZERO adjacent sections may share the same background type
3. **Dark sections:** `background: var(--primary)` (`#0D0D0D`) — cards use `rgba(255,255,255,0.04-0.05)` bg, `rgba(255,255,255,0.08)` border
4. **Light sections:** `background: var(--bg-base)` or `var(--bg-elevated)` — standard card styling

Placed Right Fence final rhythm:
```
Hero          → dark (primary)
Services      → light
QuizCTA       → dark
Gallery       → light (needs photo contrast)
Blog          → dark  ← had to flip
About         → light
Trust         → dark  ← had to flip
Testimonials  → light
FAQ           → dark  ← had to flip
ServiceAreas  → light
Shop          → dark
```

3 sections had to be flipped mid-build because the initial assignment created 3 consecutive light sections. Plan the rhythm before writing a single line of CSS.

## Key Rules
- Gallery/photo sections should almost always be light — dark background competes with image content
- Dark sections need `SectionHeading` component to receive a `dark` prop for white text
- Never use pure white (`#fff`) for dark-section card backgrounds — use `rgba(255,255,255,0.04)` for subtle separation
- Set the rhythm on paper (or in a comment block in page.tsx) before coding

## Reuse Condition
Every homepage with 5+ sections. This pattern costs 0 dev time to plan correctly upfront and costs 3–5 refactor commits to fix after the fact.
