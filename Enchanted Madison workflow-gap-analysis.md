# Optimus Workflow Gap Analysis
**Source:** Enchanted Madison build — Session 6/7 transcript debrief
**Purpose:** Every request made AFTER Claude said a phase was complete = a gap to fix

---

## The Gaps (in order they appeared)

### 1. Blog and Shop were never built in Phase 0 planning
**What happened:** Blog architecture and shop architecture had to be explicitly requested mid-build even though both were in website-build-template.md.
**Root cause:** Phase 0 task list didn't force a decision on which sections to INCLUDE vs REMOVE before scaffolding. The "Sections In/Out" decision existed in Task 3 of project-prime.md but wasn't enforced as a blocker before Phase 3 started.
**Fix:** Phase 0 checklist must include a signed-off sections matrix before any code is written.

---

### 2. progress.md not updated after each phase — had to chase it
**What happened:** "did you update the progress.md with that?" — had to ask explicitly.
**Root cause:** The rule exists in CLAUDE.md but wasn't being enforced at session end. Claude was completing tasks and moving to the next one without logging.
**Fix:** Add a mandatory session-close checklist to CLAUDE.md that Claude must output before any session ends.

---

### 3. Interactive forms weren't planned — had to request mid-build
**What happened:** The 3-step Proposal Planner form and Experience Finder quiz were both discovered/requested mid-session when looking at a Google Form the client was using.
**Root cause:** Discovery questions in Path B didn't capture "what forms does the client currently use to collect leads?" — so this context was missing from initial-business-data.md.
**Fix:** Add form/lead capture audit to the discovery voice note prompt.

---

### 4. Nav was broken — had to ask for a redesign
**What happened:** "Navigation bar is all messed up. make a drop down menu."
**Root cause:** Website-build-template.md defines a nav structure but doesn't specify behavior for sites with more than 5 nav links. No rule existed for when to split primary vs dropdown.
**Fix:** Add nav architecture rules to website-build-template.md: if nav.links > 4, split into primary (max 3 conversion-critical) + More dropdown.

---

### 5. Pricing page was a separate request — not part of any phase
**What happened:** Requested a /optimus-pricing internal sales tool page mid-build.
**Root cause:** This is an Optimus-specific deliverable that should exist as a template, not something built from scratch each time.
**Fix:** Create a reusable /optimus-pricing page template in the Optimus toolkit that can be dropped into any client build for the demo, then deleted before launch.

---

### 6. Pricing link in the dropdown was a separate commit
**What happened:** Built the pricing page, then had to separately ask "pricing needs to be in the drop down."
**Root cause:** Claude completed the page without wiring it into the nav — two related tasks treated as independent.
**Fix:** Any new page created must be added to nav and sitemap in the same commit. Rule added to CLAUDE.md.

---

### 7. Booking calendar had to be requested separately
**What happened:** "we need an interactive calendar here, even if it doesn't connect to anything"
**Root cause:** The placeholder "Online booking coming soon" box was accepted as complete. Claude didn't flag it as a conversion gap or suggest a demo-mode interactive placeholder.
**Fix:** Add a rule: every conversion CTA placeholder must be flagged as a blocker and a demo-mode interactive component must be proposed before marking the phase complete.

---

### 8. ROI calculator wasn't animated enough — required a full rewrite
**What happened:** "we need to seriously animate the ROI on this ROI calculator, make it move, make it pop, exaggerate it"
**Root cause:** The first pass was functional but not emotionally compelling. No animation standard existed for sales-tool components.
**Fix:** Add animation requirements to the /optimus-pricing template: all stats must use countUp animation, all value changes must trigger visible motion.

---

### 9. Images had to be staged and pushed separately
**What happened:** "we also need to stage and push all the image updates"
**Root cause:** Images were generated (via fal.ai script) but not committed in the same session. The atomic commit rule was being applied to code but not to generated assets.
**Fix:** Any script that generates files into /public must commit those files immediately as part of the same task.

---

### 10. hero-forest.mp4 was sitting in the repo root — never moved
**What happened:** The video file was in the repo root instead of /public. Never flagged.
**Root cause:** No rule existed for where media assets live. The video was downloaded manually and dropped in the wrong place.
**Fix:** Add asset placement rules to website-build-template.md: all media assets go to /public/[category]/. Claude must flag any asset not in /public.

---

## Summary Table

| # | Gap | Fix Target |
|---|-----|-----------|
| 1 | Blog/shop not planned in Phase 0 | project-prime.md — enforce sections matrix before Phase 3 |
| 2 | progress.md updates had to be chased | CLAUDE.md — mandatory session-close checklist |
| 3 | Forms/lead capture not in discovery | optimus-pre-build-workflow.md — add to voice note prompt |
| 4 | Nav broken with too many links | website-build-template.md — nav split rule (>4 links) |
| 5 | Pricing page built from scratch every time | Optimus toolkit — create reusable /optimus-pricing template |
| 6 | New page not wired into nav automatically | CLAUDE.md — new page = nav + sitemap in same commit |
| 7 | Placeholder CTAs accepted as complete | CLAUDE.md — placeholder rule: must propose demo component |
| 8 | Sales tools not animated enough | /optimus-pricing template — animation requirements |
| 9 | Generated assets not committed immediately | CLAUDE.md — generated files commit rule |
| 10 | Media assets in wrong location | website-build-template.md — asset placement rules |
