# Pattern: CLAUDE.md absolute-rule cross-check at design-synthesizer human checkpoint

**Category:** Workflow / Quality Gate
**First used:** Ead Financial — 2026-05-08

## What

A mandatory orchestrator-level verification step at every design-synthesizer human checkpoint: **before approving design-system.md, cross-check every section that touches a CLAUDE.md absolute rule against that rule's verbatim language.** Reject any deviation regardless of how well the agent reasoned about reference patterns to justify it.

## When to Use

Mandatory at the Stage 1B human checkpoint of every Optimus build (the design-synthesizer agent's output review). Also applies retroactively if any later stage agent (animation-specialist, content-writer, frontend-developer) cites a reference pattern to justify deviating from a structural Optimus default.

## How

The cross-check is a 6-question audit by the orchestrator at the human checkpoint:

| design-system.md section | CLAUDE.md absolute rule to verify against |
|---|---|
| §5 Hero composition | Hero Architecture Rule — *"No photos in the hero, ever — a photo placeholder in the hero is a build failure."* + 3-layer stack (HeroParticles + BrandCanvas + stagger text) + primary CTA always booking + secondary CTA always quiz + phone never in hero. |
| §5 CTA pair | Hero Architecture Rule — primary CTA always booking, secondary always quiz. NEVER "Call Now," "Learn More," info session, or external link. |
| §6 Photography | Image Generation Rule — fal.ai prompts must be specific, distinct, grounded in §6. NEVER request readable text in prompts. NO stock photography. |
| §11 Pricing tier card | Always-Built Features Rule — "Most Popular" badge ONLY on Pro tier. Premium has NO badge (its job is anchoring). NEVER deposit/payment-split copy. NEVER any Google service on any tier. |
| §11 Booking | Conversion Flow Rule + Always-Built Features Rule — Custom BookingCalendar component (NOT iframe). Inline embed only, never href redirect. |
| §11 Testimonials | Always-Built Features Rule — exactly 36 testimonials in 3-col × 3-row × 4 pages = 9 per page. NEVER 32 paginated 8 (orphan rows). ZERO em dashes in voiced copy. |

Procedure:
1. Read design-system.md §5, §6, §11 in full
2. For each section above, locate the CLAUDE.md absolute rule and read its verbatim language
3. Identify any deviation in the design-system.md output
4. For each deviation, ask: *"Did the agent cite a reference pattern (Claro, Anomaly, AAFCPAs, etc.) to justify it?"*
5. **If deviation + reference-pattern citation exists:** REJECT. Re-spawn design-synthesizer with correction note. Do NOT approve at human checkpoint regardless of internal consistency of the agent's argument.
6. **If deviation has no reference-pattern citation but does have a market-intelligence.md research basis:** still REJECT for absolute rules. Reference patterns and research findings inform aesthetic + component choices; they cannot override absolute rules.

## Key Rules

- **Absolute rules use language like "ever," "always," "never," "non-negotiable."** Search CLAUDE.md for these tokens to enumerate the absolute-rule set.
- **Reference patterns inform, they don't override.** Claro Advisors uses single-subject lifestyle photography in the hero. That is true. CLAUDE.md says no photos in the hero. That is also true. The first does not override the second. They coexist by virtue of context: Claro is a wealth-management firm with a different content stack; Optimus's Hero Architecture Rule is grounded in cross-build evidence (Helen Grondin Error #28, etc.) that doesn't change because a single competitor does it differently.
- **The cross-check is separate from the agent's self-validation.** The agent self-validates against its agent file's Required Reading list and Validation Criteria. The orchestrator validates against CLAUDE.md absolute rules. Both happen.
- **Operational test for hero-photo questions specifically:** "movie-hero" full-bleed cinematic backdrop where the photo IS the hero canvas may be acceptable IF a real production photo is available. "Box with a photo in the header" — two-column with photo on right — is NEVER acceptable, regardless of which reference site is cited. References that look like the second misread their reference; movie-hero references operate in mode-1.

## Reuse Condition

Every Optimus build, every design-synthesizer human checkpoint, with no exceptions. Becomes more important when:
- The market-intelligence.md research recommends a niche-specific deviation that could touch an absolute rule (e.g., financial-services builds tempted by Claro hero, real-estate builds tempted by Compass hero)
- The agent's output is internally consistent and well-cited (the seductive case where rejection feels like overruling rigorous work)
- The aesthetic is editorial / boutique / luxury (these registers most often look like they "want" reference-pattern fidelity)

## Related

- [[errors/claude-md-absolute-rule-override-via-reference-pattern]] — the Ead Financial instance that produced this pattern
- [[errors/photo-placeholder-appears-in-hero-instead-of-3-layer-animation-stack]] (Error #28) — the original Helen Grondin error that codified the no-photos-in-hero absolute rule
- CLAUDE.md Hero Architecture Rule — the absolute rule itself
- CLAUDE.md Always-Built Features Rule — additional absolute rules to cross-check
- CLAUDE.md Conversion Flow Rule — additional absolute rules
