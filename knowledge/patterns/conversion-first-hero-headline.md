# Pattern: Conversion-First Hero Headline — Brand in the Badge, Value in the H1
**Category:** Conversion / Copy
**First used:** Gray Method Training — 2026-04-10

## What

Audit the hero above-the-fold for brand-name repetition and replace a brand-name H1 with an outcome-led mission statement in the client's own voice. The nav logo, the hero logo badge, the page title, and the footer already carry the brand. The H1 is the most valuable real estate on the page and should answer *"what's in it for me?"* for the visitor, not repeat the company name.

## When to Use

- On every build, as a final hero pass before launch
- Audit trigger: count how many times the brand name appears above the fold. **3 or more = rewrite the H1.**
- Especially when the client has a circular badge logo (round logos almost always contain a wordmark, so placing any text "brand name" near them causes double-exposure)
- When the current H1 reads like a brochure header ("Brand Name — What We Do") rather than a reader-facing promise

## How

### 1. Audit the above-the-fold for repetition

At 1440×900, count visible brand-name instances:

- Navbar text logo → 1
- Navbar image logo (if it contains wordmark text) → 1
- Hero H1 → potentially 1
- Hero side logo badge → potentially 1
- Hero eyebrow (if it contains brand) → potentially 1

**≥3 = rewrite required.** The Gray Method audit found 3: nav text + H1 ("Gray Method Online Health & Fitness") + giant logo badge.

### 2. Rewrite the H1 using the brand voice doc

Pull the mission statement from `adam-gray-brand-voice.md` (or equivalent). The client's literal mission statement — usually a 1-sentence paragraph somewhere in Section 3 of a brand voice doc — is almost always a better H1 than whatever is currently rendered.

**Before (Gray Method):**
```
Eyebrow: "Online Health & Fitness Coaching"
H1:      "Gray Method Online Health & Fitness"
```
→ Brand appears 3x above the fold. H1 says nothing about what the visitor gets.

**After (Gray Method):**
```
Eyebrow: "Online Coaching for Busy Women"
H1:      "Stronger. / More energized. / Finally free from the diet cycle."
```
→ Brand appears 1x (the logo badge). Eyebrow qualifies audience. H1 delivers 3 outcomes from Adam's mission statement verbatim.

### 3. Split jobs between eyebrow and H1

| Slot | Job | Example |
|------|-----|---------|
| **Eyebrow** | Qualify the audience (who this is for) | "Online Coaching for Busy Women" |
| **H1** | Deliver the outcome (what the visitor gets) | "Stronger. / More energized. / Finally free from the diet cycle." |
| **Tagline** | Philosophy / differentiator (why this one) | "There is no black and white, everyone is different..." (anti-system framing) |

Each slot carries one job. The eyebrow qualifies (audience), the H1 promises (outcome), the tagline differentiates (philosophy).

### 4. Emphasize the climax line

If the H1 is three short sentences, shimmer (or otherwise visually emphasize) the last one. It's the emotional payoff. Split the copy across three grid lines:

```tsx
<motion.h1 className="font-display text-display leading-[1.05]">
  <span className="block">{hero.headlineLines[0]}</span>
  <span className="block mt-1">{hero.headlineLines[1]}</span>
  <span className="block text-shimmer">{hero.headlineLines[2]}</span>
</motion.h1>
```

Store `headlineLines` as an array in `site.ts` — never hardcoded in JSX (per CLAUDE.md "no hardcoded copy in JSX" rule).

### 5. Swap the navbar wordmark for image-only if the logo already contains text

If the logo PNG/SVG already contains the wordmark (common for round badge logos), the navbar should be **image-only, no adjacent text span.** Text + logo-with-text = "Gray Method" literally side-by-side-by-side.

- Logo image shrinks on scroll (56 → 44px is a good range)
- Add `drop-shadow` on hover for premium feel
- Apply the same treatment in `MobileNav.tsx` header

## Key Rules

- **Never put the brand name in the H1** unless the brand is a verb ("Squarespace your ideas") or the brand is unknown enough that it needs re-exposure in the H1. Almost always neither applies.
- **Pull H1 copy from the brand voice doc.** The mission statement is the candidate. The "what clients say" section is the backup. Don't invent copy — mine it.
- **Qualify audience in the eyebrow, not the H1.** Eyebrow is where to put "for busy women / for solo founders / for teams of 20+." Frees H1 for pure outcome language.
- **Count brand instances above the fold before every launch.** If ≥3, rewrite. No exceptions.
- **Audit the logo badge contents.** If it has a wordmark inside, the navbar goes image-only. Side-by-side text + wordmark-in-logo is literal duplication.
- **Verify visual impact at 375 / 390 / 428** ([[patterns/end-of-build-multi-breakpoint-browser-audit]]) — a long H1 that fits desktop may wrap badly on mobile. Use [[patterns/clamp-responsive-type-scale]] so clamp handles this automatically.

## Reuse Condition

Every build with a hero H1 and a branded badge/logomark. This is a pre-launch pass, not a mid-build activity — by the time you're auditing this, the hero is already built and your job is to improve the copy, not redesign the layout.

Skip only if:
- The client's brand is totally unknown and absolutely needs naming in the H1 (rare, and you can still usually relegate it to the eyebrow instead)
- The brand is a playful brand-verb ("Let's Gray Method your fitness")
- The H1 is already outcome-led and you're auditing just to confirm

## Related

- [[patterns/end-of-build-multi-breakpoint-browser-audit]] — the audit that verifies the rewrite across breakpoints
- [[patterns/clamp-responsive-type-scale]] — ensures long H1s don't break on mobile
- Helen Grondin hero rules in build-log (tagline shimmer, no photo in hero, second CTA = quiz) — this pattern is the copy-strategy companion to those architecture rules
- Adam Gray brand voice doc: Section 3 "Mission" → the literal source of the winning H1
