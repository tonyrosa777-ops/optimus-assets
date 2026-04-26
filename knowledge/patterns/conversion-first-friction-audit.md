# Pattern: Conversion-first friction audit (booking / signup / checkout / quiz)

**Category:** Workflow / Quality / Conversion
**First used:** Collaborative Insights — 2026-04-20

## What
Before building ANY pre-picker, wizard, multi-step UI, or "enhanced" interaction on a conversion-critical page (booking, signup, checkout, quiz), explicitly audit the full user journey for repetition and friction. Count every field the user enters. Flag anything they enter twice. Name any third-party-tool limitation that forces re-entry. If the flow adds steps without removing any, the design is blocked — polish within the existing flow instead.

## When to Use
Mandatory before writing code on:
- `/booking` or any scheduler embed
- Signup flows (`/signup`, free-trial activation, onboarding)
- Checkout flows (shop checkout, upgrade paywalls)
- Multi-step quizzes and funnels
- Anywhere a visitor is actively trying to convert

Optional but encouraged on any other form-heavy page.

## How
Write this audit into the plan BEFORE the first file is touched. It takes under 5 minutes and prevents days of rework.

**Step 1 — Map the full journey.**
List every field the user will enter across the entire flow, including third-party iframes. Example for a Calendly booking page:

```
Our UI         Third-party (Calendly iframe)
──────────     ─────────────────────────────
Session type   —
Date           Date 🚩
Time           Time 🚩
—              Name
—              Email
—              Phone
—              Notes
```

**Step 2 — Flag every 🚩 re-entry.**
Any field the user touches twice is a red flag. On conversion-critical pages, 🚩 re-entry is a hard blocker, not a cosmetic issue.

**Step 3 — Name the third-party limitation behind each 🚩.**
Example: *"Calendly's deep-link URL params support `date` and `month` but not `time`. Their internal widget API that handles time pre-selection is unofficial and unstable."*

If any 🚩 exists AND the third-party tool cannot be replaced at reasonable cost, the design direction is **blocked**. Do not proceed with a "we'll pick again but quickly!" workaround — users won't.

**Step 4 — Choose one of:**
- (A) Polish within the existing third-party UI (theme tweaks, section framing, clearer pre-step copy). Usually the right answer.
- (B) Replace the third-party tool with one that has a real booking API (e.g. Cal.com instead of Calendly). Bigger scope, real migration, rarely worth it for a single-client polish pass.
- (C) Abandon the pre-picker entirely.

**Step 5 — Say the tradeoff out loud in the plan.**
Example wording to present to the user:
> "Building a native date/time picker would mean users pick twice (once on our UI, once on Calendly's iframe) because Calendly's URL params don't pre-fill the time. That's fatal friction on the conversion-critical page — I recommend against the pre-picker and suggest polishing the iframe instead. If you want full native, we'd need to migrate to Cal.com."

Let the user veto or approve with the tradeoff on the table. Do not discover the tradeoff after the rebuild is done.

## Key Rules
- **Conversion > polish** on these pages. A visually-worse flow with fewer steps beats a visually-better flow with more steps.
- **The third-party limitation is the design constraint, not a footnote.** If Calendly / Stripe / Cal.com can't deliver a capability, that limit sets the ceiling — build within it.
- **Audit the iframe's form too, not just our UI.** The user's journey includes fields inside embeds. A "native pre-picker" that ends with an iframe form is two flows, not one.
- **Do not rely on "the user won't mind picking again."** They will. Especially on free-discovery-call flows where every drop-off is $100+ lost per conversion.

## Reuse Condition
Apply on every Optimus build during:
- Phase 9 (Booking) — mandatory gate before any booking-page refactor
- Phase 10 / 12 UAT — retroactive check if conversion data comes in soft
- Any mid-build "let's make this more branded" request from the client — audit the friction impact first

## Related
- [[errors/native-picker-plus-calendly-double-entry]] — the specific incident that established this rule
- [[patterns/calendly-light-stage-section]] — what we did instead, after this audit
- Project memory: `feedback_conversion_first.md` (per-client) — persists the rule into future Claude sessions on the same client
- CLAUDE.md Core Law — this is a workflow-quality extension of "research-backed decisions only"
