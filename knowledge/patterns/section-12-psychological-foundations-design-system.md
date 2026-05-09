# Pattern: Section 12 Psychological Foundations — design-system.md addition

**Category:** Design Documentation / Defensibility / Content-Writer Briefing
**First used:** Ead Financial — 2026-05-08

## What

A 12th section added to design-system.md (after the canonical 11 sections defined by design-synthesizer.md) that maps each design decision to its **behavioral mechanism citation**. Converts a design system from "competitively-backed" (decisions cite "Claro does this" / "competitors don't use this") to **psychology-backed** (decisions cite Kahneman & Tversky, Ariely, Thaler, Brehm, Cialdini, Festinger, Sweller, Reber/Schwarz/Winkielman, et al.).

## When to Use

Mandatory addition to design-system.md on builds where ANY of these apply:
- Audience makes high-anxiety decisions (financial, legal, health, audit, compliance)
- The build will be defended under client pushback ("why these specific colors?")
- content-writer's Stage 1D copy needs framing anchors that go beyond "the reference site does this"
- The pre-launch-auditor needs a checklist of psychological mechanisms to verify in shipped code (not just file existence)

Optional but high-leverage on every other Optimus build — converts design-system.md from a competitive snapshot into a permanent training reference.

## How

Section 12 has 8 subsections in order:

### 1. The audience's emotional state — design for [decision frame]
One paragraph naming the dominant decision frame (threat-response for tax/audit; aspirational for travel/luxury; loss-frame for contractor/insurance/bonding). Cites Schmader & Beilock 2012 for threat-response cognitive load.

Then 3 numbered "decision moments" with design rules each — pricing comparison, booking calendar open, quiz completion (or equivalents for the build's conversion architecture).

### 2. Cognitive fluency — the bedrock principle
One paragraph citing Reber, Schwarz & Winkielman 2004: easier-to-read text is judged more truthful, the speaker more competent. Then bullet-list 4–6 typography/color/copy decisions in design-system.md and map each to a fluency claim:
- Reading column width → Bringhurst 1992; Tinker 1963 (50–75 char optimum)
- Cream over pure white → blue-light glare reduction
- Serif headline + clean sans body → high-fluency editorial pairing
- No em dashes in voiced copy → published-author signal vs phone-review register

### 3. Behavioral mechanisms — one-line citation per major decision
A 14-row table mapping decision → mechanism → source. Required rows (adapt the cell content to the build):
- Palette choice (warm vs cool color temperature in audience emotional state — Crowley & Hoyer 1994; Mehta & Zhu 2009)
- Italic-emphasis on ONE word per headline (single focal point — Yarbus 1967; Rayner 1998)
- Reading column width (Bringhurst 1992; Tinker 1963)
- Solid vs translucent surfaces (figure/ground separation — Wertheimer 1923; Palmer 1999)
- Transparent flat-fee pricing (uncertainty reduction — Kahneman & Tversky 1979)
- 3-tier "Most Popular" decoy (asymmetric dominance + default bias — Ariely 2008; Thaler & Sunstein 2008)
- Premium tier as anchor (Tversky & Kahneman 1974)
- Self-diagnosis quiz (IKEA effect + effort justification — Norton/Mochon/Ariely 2012; Festinger 1957)
- Mutual-fit philosophy / boundary copy (reactance + scarcity — Brehm 1966; Cialdini 1984)
- 36 testimonials vs thin (quantity-as-quality social proof — Cialdini 1984; Salganik et al. 2006)
- Editorial photography over stock (authenticity bias + in-group ID — Tajfel & Turner 1979; Pennycook & Rand 2019)
- Phone visible in nav (friction reduction — Norman 1988)
- Button radius (shape psychology — Bar & Neta 2006)
- Quiet motion budget (cognitive resource preservation — Sweller 1988)

### 4. Commitment-escalation strategy — the [conversion lever] is the build's strongest psychological mechanism
For Optimus builds, this is usually the quiz. Cite Bem 1972 (self-perception change), Festinger 1957 (effort justification + cognitive consistency), and bullet 3 binding rules for the content-writer:
- Diagnostic framing, not promotional
- Result screen restates user's prior answers BEFORE presenting the recommendation
- Tier-specific BookingCalendar inline at result-completion (no extra clicks)

### 5. Anchoring strategy — pricing matrix beyond the "Most Popular" badge
3-tier psychological roles spelled out: Starter feels like a save-money choice that obviously gives less, Pro is the rational middle with social proof, Premium exists to anchor (it is BAIT, not a primary conversion target). Bind content-writer's pricing copy to "everything in Starter, plus..." (loss-frame from Starter) AND "the most popular choice for [audience band]" (social proof) on Pro tier.

### 6. Loss-aversion framing — [niche page 1 + niche page 2]
For builds with niche landing pages where the audience makes decisions under loss frame (contractors fearing bonding loss, treatment centers fearing certification loss, etc.), cite Kahneman & Tversky's prospect theory (losses ~2× gains). Bind content-writer to: **every section of these pages opens with what the prospect stands to LOSE before resolving with the firm's mechanism. Never reverse.**

Include 3-row before/after table demonstrating the binding (gain-frame ❌ vs loss-frame ✅).

### 7. Pre-launch-auditor checklist (Stage 1H derivative — 10 binary checks)
Convert each of Sections 4 + 5 + 6 binding rules into a binary checklist item the pre-launch-auditor agent can verify in shipped code. Examples:
- ☐ Pricing matrix renders 3 tiers visible in <3 seconds, no clicks. Pro has badge. Premium does not.
- ☐ Quiz result screen restates user's answers BEFORE presenting tier (consistency mechanism)
- ☐ Niche landings open every section with loss vector before mechanism (loss-frame audit pass)
- ☐ Reusable widgets render solid `--bg-card` not translucent overlays (figure/ground fluency pass)
- ☐ Body line-length 50–75 chars across breakpoints (reading-column fluency pass)
- ☐ Zero em dashes in voiced copy (phone-review register pass)

### 8. Defensibility under client pushback
A scripted answer to a likely client question. Format:
> "When [client name] asks 'why [decision], not [obvious alternative]?', the answer is no longer 'competitors don't use them.' The answer becomes: '[mechanism explanation citing source]. The competitive analysis is in market-intelligence.md §X; the psychological mechanism is in design-system.md §12.'"

The client pushback script is the artifact that makes Premium tier ($5,500) defensible. Without §12, the answer is "Claro does it" — which is not what Premium is supposed to buy.

## Key Rules

- **Adapt subsection content to the build, but keep all 8 subsections present.** The 14-row mechanisms map (Subsection 3) is the most build-specific — palette + photography + framing rules vary; the structure (decision → mechanism → source) is portable.
- **Cite primary sources, not aggregator articles.** Kahneman & Tversky 1979, Ariely *Predictably Irrational* 2008, etc. — academically credible. Avoid "according to a UX article on Medium..."
- **§12 is BINDING for Stage 1D content-writer.** The diagnostic framing, anchoring, and loss-frame rules in subsections 4–6 are not aspirational — they're rules the content-writer agent must follow. Cite §12 in the content-writer agent's spawn brief explicitly.
- **§12 is BINDING for Stage 1H pre-launch-auditor.** The 10 binary checks in Subsection 7 become validation criteria the auditor verifies in shipped code, not just in design-system.md.
- **Length budget: ~600–1100 words.** Long enough to substantiate; short enough to scan. Ead Financial's §12 was 113 lines (~1100 words including the table). Below 400 words is "header with gestures, not real grounding" — fails the user's stated test for substance.

## Reuse Condition

Every Optimus build going forward. design-synthesizer.md should be updated to require Section 12 in its 12-section output spec (currently 11). For builds in low-anxiety categories (luxury hospitality, romantic getaway, consumer entertainment), the threat-response framing in Subsection 1 shifts to aspirational-decision framing, but the structure stays.

The pattern is highest-leverage on:
- Financial / legal / health / compliance builds (threat-response audience)
- Builds with explicit competitor pricing-pressure where Premium tier defensibility matters
- Builds where content-writer would otherwise default to "competitors do this" copy framing
- Builds where pre-launch-auditor needs psychological-mechanism checks beyond file-existence verification

## Related

- [[patterns/light-mode-dominant-cream-theme]] — palette decisions in §12 Subsection 3 mechanisms map
- [[patterns/optimus-luxury-modern-positioning]] (Pattern #49) — composes with §12; positioning + psychology together
- [[patterns/luxury-gradient-backgrounds]] (Pattern #51) — motion budget rule cited in §12 Subsection 3
- [[patterns/reusable-widget-self-sufficient-surface]] (Pattern #55) — figure/ground fluency cited in §12 Subsection 3
