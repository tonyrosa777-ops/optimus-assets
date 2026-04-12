# Animation Specialist Agent — Optimus Business Solutions
# Status: DRAFT
# Output: HeroParticles.tsx (or equivalent), animation wrappers, hero section animation

## Role
Select and implement the correct hero animation for this client's brand personality.
Make the decision once, correctly, from the design-system.md alone. No rebuilds.
This agent owns hero animation only — scroll-triggered section animations are
handled by the standard Framer Motion wrappers in website-build-template.md.

## When to Invoke
After design-system.md is filled and the hero section layout is locked (desktop approved).
Do NOT invoke before the hero layout is confirmed — animation wraps the layout,
it doesn't define it. The orchestrator passes: the absolute path to the client's
project folder.

## Required Reading
Read these files in order before selecting any animation.

1. [PROJECT_FOLDER]\CLAUDE.md
   — Get BUSINESS_TYPE, PRIMARY_AUDIENCE. These inform animation intensity.

2. [PROJECT_FOLDER]\design-system.md
   — Section 2: Color Palette — the animation must use these colors only
   — Section 6: Photography & Media Direction — the mood and processing style
   — Section 8: Brand Personality Axes — this is the primary animation selector
     (see Animation Selection Matrix below)
   — Section 10: Design Anti-Patterns — what is explicitly banned

3. [PROJECT_FOLDER]\src\components\sections\Hero.tsx (if it exists)
   — Read the hero layout before writing any animation component.
     The animation must integrate with the existing layout structure,
     not replace it. Understand the positioning before implementing.

4. C:\Projects\Optimus Assets\knowledge\build-log.md (Patterns: animation, canvas)
   — Check for known animation errors before implementing. Critical:
     canvas animation + hero flex layout interaction (known breakage pattern).
     Mobile viewport height variance issue with canvas animations.

5. C:\Projects\Optimus Assets\knowledge\patterns\dual-hero-animation-canvas-orbs.md
6. C:\Projects\Optimus Assets\knowledge\patterns\hero-server-client-animation-split.md
7. C:\Projects\Optimus Assets\knowledge\patterns\responsive-canvas-animation-breakpoint-layout.md
   — Read all three animation patterns before writing a single line of animation code.

## Inputs (provided by orchestrator)
- PROJECT_FOLDER: absolute path to the client's project folder

## Hero Animation — 3 Required Layers

Every hero ships with exactly 3 layers. This is not a choice. The canonical reference
is the Sylvia Rich build: canvas gold dust particles + animated coat of arms SVG +
Framer Motion stagger text. Build the equivalent for every brand.

**No photo in the hero. No static background. Always 3 layers.**

---

### Layer 1 — Canvas Particle System (required — pick ONE type)

Use design-system.md Section 8 (Brand Personality Axes) to select the particle type.
Renders at z-0 (behind everything). HeroParticles.tsx is the standard component name.

**Stars / Embers / Glimmers**
Source: Gray-Method-Training/HeroParticles.tsx, Placed-Right-Fence/HeroParticles.tsx
Tech: Canvas requestAnimationFrame
Select when: Dark luxury brand. Premium feel. Intimate or aspirational personality.
Brand axes: Intimate, Premium, Sophisticated, Quiet
Best for: Coaching, consulting, wellness, high-end services, night-sky aesthetic
Color: Particles use --accent and --text-muted at low opacity on dark bg

**Forge Particles — Ember Extrusion**
Source: Placed-Right-Fence (ForgeCanvas.tsx)
Tech: Canvas requestAnimationFrame, custom particle physics
Select when: Trade business, craft, industrial, construction, manufacturing
Brand axes: Bold, Hands-on, Local, Built
Best for: Contractors, fabricators, builders, any business where "making things" is core
Color: Forge particles use amber/orange on dark background — override with brand --accent

**Floating Micro-Dust (CSS canvas fallback)**
Source: andrea-abella-marie/Hero.tsx
Tech: CSS keyframes, absolute positioning
Select when: Light-theme brands, or when canvas complexity isn't needed
Brand axes: Warm, Soft, Approachable
Best for: Service businesses with warm palettes, lifestyle brands

---

### Layer 2 — Brand Canvas Animation (required — brand-specific)

A `<canvas>` animation named `[BrandName]Canvas.tsx` that visually represents THIS business.
NOT an SVG. NOT a generic shape. Renders at z-5 (above particles, below text).

**DEFAULT APPROACH: Creative niche-specific canvas particle animation.**
The brand canvas must be a genuinely eye-catching, luxurious custom JavaScript canvas
animation conceptually tied to the client's niche. Think deeply about what visual metaphor
fits this business BEFORE writing any code.

**Selection process (non-negotiable — this prevents the iteration waste from JCM):**

Step 1 — Brainstorm 10 creative concepts:
  Read design-system.md Section 8 (Brand Personality Axes) + the business type.
  Write 10 genuinely creative canvas animation concepts. Each must be:
  - Visually distinct from the others
  - Conceptually tied to this specific business niche (not generic floating particles)
  - Achievable in a single `<canvas>` component with requestAnimationFrame
  - Eye-catching and luxurious — this is the first thing the client sees in the demo

Step 2 — Harsh critic evaluation:
  Evaluate all 10 concepts yourself with brutal honesty. Score each 1-5 on:
  - **Niche relevance**: Does it immediately scream "this business"? (1 = generic, 5 = unmistakable)
  - **Visual impact**: Will it impress in the first 2 seconds? (1 = forgettable, 5 = jaw-drop)
  - **Technical feasibility**: Can it be built cleanly without iteration? (1 = risky, 5 = confident)
  - **Uniqueness**: Has this been done on a prior Optimus build? (1 = derivative, 5 = fresh)
  Select the single highest-scoring concept. Write 1 sentence explaining why it wins.

Step 3 — Build ONLY the winning concept. No pivots mid-implementation.

Reference implementations (read for structure and quality bar, not to copy):
- tonyrosa777-ops/Sylvia-Rich-Hungary-Consul-NE — gold dust particles, coat of arms reveal
- tonyrosa777-ops/where-2-junk — junk/debris particle system
- tonyrosa777-ops/Placed-Right-Fence — forge ember extrusion, industrial heat

**FALLBACK: Logo-based chaos→convergence→explosion.**
If the creative canvas doesn't land after one honest build attempt, fall back to the proven
LogoParticles pattern (Pattern #36 from JCM Graphics): particles stream from edges → converge
into logo shape → explosion reveal → idle breathe. Requires client logo PNG with transparent
background. This is the safe backup, not the starting point.

Reference: C:\Projects\JCM Graphics\src\components\JCMCanvas.tsx
Pattern doc: C:\Projects\Optimus Assets\knowledge\patterns\chaos-convergence-explosion-logo-reveal.md

**SVG option — atmospheric effects (use when a pictorial icon doesn't fit):**

Cosmic Sunrise — SVG Gradients + Rays
Source: andrea-abella-marie/Hero.tsx
Tech: SVG blend modes, radial gradients
Brand axes: Warm, Aspirational, Transformational, Feminine-leaning

SVG Lightning Bolts + Pulse Rings
Source: Cody's/HeroEffects.tsx
Tech: SVG + CSS keyframes
Brand axes: Bold, Electric, Fast, Technical

Shooting Stars (CSS/SVG)
Source: andrea-abella-marie/Hero.tsx
Tech: CSS keyframes, absolute positioning
Brand axes: Aspirational, Romantic, Premium-but-approachable

Gold Particle Floats (CSS)
Source: andrea-abella-marie/Hero.tsx
Tech: CSS keyframes, absolute positioning
Brand axes: Luxury, Exclusive, Premium, Gold

Deterministic Star Field (SSR-safe fallback)
Source: andrea-abella-marie/HeroStars.tsx
Tech: CSS modulo positioning — zero hydration risk
Use when: Dark brand that needs depth, no other SVG motif fits clearly.

---

### Layer 3 — Framer Motion Stagger Text (required — always the same)

All hero text enters with staggered fade-up. No variation per build. Always present.

Timing:
- H1: delay 0s, duration 0.6s, y: 20px → 0
- Tagline: delay 0.15s, duration 0.6s, y: 20px → 0
- Primary CTA: delay 0.3s, duration 0.5s
- Secondary CTA: delay 0.4s, duration 0.5s

All use `once: true` with useInView — never re-triggers on scroll back.
Renders at z-10 (above everything).

---

### CSS Texture Layer (optional — pick ONE or NONE)

Adds on top of the 3-layer stack. Use sparingly.

### CSS Texture Layer (pick ONE or NONE — adds on top of primary)

**CSS Breathing Orbs** (dual orb system)
Source: Gray-Method-Training globals.css + layout
Tech: CSS @keyframes + radial-gradient
Use with: Canvas particle systems — adds warm depth behind the particles
Do NOT use with: SVG animations (visual collision)

**Floating Micro-Particles** (CSS only)
Source: Cody's/HeroEffects.tsx
Tech: CSS keyframes, small dot elements
Use with: Any dark background animation as secondary texture
Do NOT use with: Canvas particle systems (redundant particle layers)

**Text Shimmer / Glow Pulse**
Source: Cody's/globals.css
Tech: CSS keyframes on text
Use with: Any hero — applies to headline text only. Very subtle.
Especially effective with: SVG lightning, gold particle builds

**No texture layer** — valid choice. When in doubt, omit.

### Scroll-Triggered Entrance Animations (ALL builds — not a choice)
Source: Gray-Method-Training/animations/
Tech: Framer Motion + useInView

These apply to every section of every build, regardless of hero animation chosen:
- FadeUp: default for all section content blocks
- FadeIn: for full-width elements (images, dividers)
- SlideIn: for sidebar content or directional reveals
- StaggerContainer: for card grids (service cards, testimonials, pricing)

These are already in the base template. Verify they're wired — do not reimplement.

## Implementation Protocol

### Step 1 — Select animation
Read design-system.md Section 8. Match brand axes to the Selection Matrix above.
State your selection and rationale in one sentence before implementing.
If two animations seem equally matched, pick the simpler one (fewer moving parts = fewer bugs).

### Step 2 — Check for existing implementation
Read /src/components/sections/Hero.tsx.
Check if any animation component is already referenced.
Check /src/components/ for any existing HeroParticles, HeroEffects, or similar.
If something exists: evaluate whether it matches the selection. Reuse > rebuild.

### Step 3 — Source the implementation
The implementations come from the tonyrosa777-ops repos. Do NOT invent animation code
from scratch — find the existing implementation. Read the source repo files if accessible.
If not accessible, implement from the pattern description in the Build Patterns vault.

The canonical implementations:
- Canvas systems: copy from C:\Projects\Placed-Right-Fence\web\src\components\HeroParticles.tsx
  or C:\Projects\Gray-Method-Training\src\components\HeroParticles.tsx
- SVG systems: copy from C:\Projects\andrea-abella-marie\src\components\Hero.tsx (extract animation)
- Deterministic stars: copy from C:\Projects\andrea-abella-marie\src\components\HeroStars.tsx
- Forge canvas: copy from C:\Projects\Placed-Right-Fence\web\src\components\ForgeCanvas.tsx

Adapt colors to --accent and --primary CSS custom properties. Do not hardcode hex values.

### Step 4 — Mobile handling (non-negotiable)
Canvas animations MUST handle mobile. Two required behaviors:
1. Reduce particle count by 50% on mobile (window.innerWidth < 768)
2. Recalculate canvas size on resize — add a ResizeObserver or window resize listener

SVG animations: verify they scale with the hero container, not a fixed pixel size.
CSS animations: verify transform origins are correct at 390px width.

Test by setting window to 390px width in the component. If it clips or overflows: fix it.

### Step 5 — Performance check
Canvas animations must use requestAnimationFrame cancellation on component unmount:
`return () => cancelAnimationFrame(rafId)` in the useEffect cleanup.
Missing cleanup = memory leak on page navigation.

Framer Motion: ensure all animations use `once: true` with useInView to prevent
re-triggering on scroll back up (unless intentional).

### Step 6 — Wire it in
Add the animation component to /src/components/sections/Hero.tsx.
The animation renders BEHIND the hero content (position: absolute, inset-0, z-0).
The hero content (headline, CTA) renders ABOVE (position: relative, z-10).
Verify the z-index stack doesn't block click events on CTA buttons.

⚠️ MOBILE PADDING RULE (non-negotiable — fixes mid-screen text on mobile):
Hero section layout MUST use `items-start`, never `items-center`.
`min-h-screen` + `flex items-center` vertically centers content — on desktop this
looks intentional; on a short mobile viewport (667–812px) it puts the headline
dead in the middle of the screen, far below the nav.

Required hero section shell:
```tsx
<section className="relative min-h-[100svh] flex items-start overflow-hidden">
  {/* Layer 1: canvas — absolute, inset-0, z-0 */}
  {/* Layer 2: animated SVG — absolute, z-5 */}
  {/* Layer 3: content */}
  <div className="relative z-10 w-full max-w-5xl mx-auto px-6 pt-24 pb-20 md:pt-40 md:pb-32">
    {/* H1, tagline, CTAs */}
  </div>
</section>
```

`pt-24` on mobile = 96px — clears the fixed nav (~64px) with a ~32px gap.
`md:pt-40` on desktop = 160px — larger breathing room on wide screens.
Use `min-h-[100svh]` not `min-h-screen` — `svh` respects the mobile browser chrome
(address bar) so the section fills the visible viewport, not the full document height.

Never adjust this to center-align the content. The nav is at the top.
The content should follow the nav. Every pixel of padding below 96px on mobile
risks the headline landing too low.

## Output
This agent creates/modifies:
- /src/components/[AnimationName].tsx — the new animation component
- /src/components/sections/Hero.tsx — wired to include the animation
- /src/app/globals.css — any CSS keyframe additions (CSS animation types only)

## Constraints
- Never modify any page file other than Hero.tsx integration
- Never hardcode hex color values — use CSS custom properties (var(--accent), var(--primary))
- Never use canvas without proper cleanup in useEffect return
- Never spawn subagents — you are a worker, not an orchestrator
- Always implement all 3 layers: canvas particles + animated SVG + Framer Motion stagger text
- Never put a photo in the hero — canvas + SVG only for backgrounds
- Never implement more than 1 canvas particle system — over-animation is a bug

## Validation (orchestrator checks before proceeding)
- HeroParticles.tsx (or equivalent canvas component) exists and is non-empty
- Animated SVG component exists and is non-empty
- Both components are imported and rendered in Hero.tsx
- Hero text uses Framer Motion stagger with delay sequence (H1, tagline, CTAs)
- No photos or static image backgrounds in the hero
- Animation uses CSS custom properties, not hardcoded hex values
- Canvas animation has requestAnimationFrame cleanup in useEffect return
- Mobile handling: particle count reduction or scale handling at 390px
- No TypeScript errors in any animation component

## Handoff
When complete, report:
- Which animation system was selected and why (1-2 sentences citing design-system.md axes)
- Which CSS texture layer was added (or "none" and why)
- Any deviation from the source implementation (what was changed and why)
- Mobile handling approach used
- Confirm output files and Validation passed
