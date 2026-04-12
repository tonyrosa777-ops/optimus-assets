# Pattern: End-of-Build Multi-Breakpoint Live Browser Audit
**Category:** Workflow / QA
**Status:** MANDATORY — every build, no exceptions
**First used:** Gray Method Training — 2026-04-10 (Session 4)
**Workflow integration:** CLAUDE.md Visual QA Rule · build-checklist.md Phase 1 step 14 · project-prime.md Stage 1I · website-build-template.md Checklist: Before Launch · pre-launch-auditor.md Section 11

## What

A mandatory pre-ship workflow that runs the dev server and drives Playwright against the live site at **four viewports** — desktop 1440×900 plus mobile 375 / 390 / 428 — plus the scrolled navbar state and the mobile nav drawer, capturing screenshots and reading the console at each breakpoint. Catches **visible-only bugs** that typecheck, lint, and agent file audits cannot see: text wraps, overflow, layout shifts, hydration mismatches, silent console warnings, and animation timing failures.

TypeScript says the code compiles. Tests say the logic works. **Only a browser at the right viewport width tells you the product looks right.** Every Optimus build before this pattern existed shipped at least one visible-only bug that this audit would have caught pre-launch.

## Why this is mandatory

Every prior build had a visible-only bug that typecheck + lint passed. Four of them in the Error Encyclopedia would have been caught by this audit if it had existed at the time:

| Project | Bug | Build-log # | What flavor of bug |
|---------|-----|-------------|---------------------|
| Gray Method Training | `--text-display: 4.5rem` orphaned "More" on its own line at 390px | #37 | fixed-rem display font size |
| Helen Grondin | Hero text invisible against background | #29 | wrong color token on dark bg |
| Danielle Thompson | Rate badge overflow from `whitespace-nowrap` pill | #16 | content longer than container |
| Sweep Test 1 | Mobile hero text starts mid-screen from `items-center` | #25 | vertical centering on min-h-screen |
| Gray Method Training | `PhotoPlaceholder` `onError` fires in production | #34 | hydration-only bug |

All five are visible-only bugs. All five passed typecheck and lint. Every single one would have been caught by this audit. **Skipping the audit is how visible-only bugs ship to production.**

## When to Run

- **Mandatory** at project close, as the final gate before marking a build complete and handing to the client
- Before every `git push` that could affect production visual state
- Before marking any phase complete that touches layout, copy, or hero
- After any change to typography tokens, responsive classes, or component layout
- After any H1 / hero copy change

## Prerequisites

- `mcp__playwright__*` tools available (check with a quick `browser_navigate` to any URL first if unsure)
- Dev server startable from the Next.js app folder
- No existing process already bound to `localhost:3000` — kill it first if there is
- Background task runner available (Claude: `run_in_background: true`)

## How

### 1. Start the dev server (background)

```
cd <project>/<next-app-folder>
npm run dev
```

Run with `run_in_background: true`. **Do not block the session** waiting for it.

It writes output to a temp file. Read the file until you see `✓ Ready in Xms` before doing anything else — navigating before the dev server is ready captures a blank or building page and wastes the audit.

**Save the background task ID.** You need it at the end to stop the server. Put it in scratch notes or progress.md.

### 2. Desktop audit first (1440×900)

```
mcp__playwright__browser_resize(width: 1440, height: 900)
mcp__playwright__browser_navigate("http://localhost:3000")
mcp__playwright__browser_wait_for(text: "<a phrase from new content>")
```

**`wait_for` text rule:** the phrase must only appear **after hydration** — pick a new H1 phrase, a CTA label, an animated stat. Static page shell text (`<title>`, nav items) may appear before hydration and will lie to you. This guarantees the screenshot captures the real rendered state.

### 3. Screenshot + console check at desktop top-of-page

```
mcp__playwright__browser_take_screenshot(filename: "verify-desktop-hero-top.png")
mcp__playwright__browser_console_messages(level: "error")    → expect 0
mcp__playwright__browser_console_messages(level: "warning")  → expect 0
```

**Zero errors, zero warnings.** If anything appears, stop and investigate before continuing — something is wrong with the build. Console noise in dev is a signal of worse noise in prod.

### 4. Scroll the page, screenshot the scrolled nav state

```
mcp__playwright__browser_evaluate(function: "() => { window.scrollTo(0, 400); return window.scrollY; }")
mcp__playwright__browser_take_screenshot(filename: "verify-desktop-nav-scrolled.png")
```

**Use `browser_evaluate` with `window.scrollTo`.** Do not use `browser_navigate` with hash fragments or any scroll parameter — they behave inconsistently across Playwright versions. `window.scrollTo` is the only reliable method.

Verify in the screenshot:
- Navbar background / blur shifts correctly
- Logo shrinks (if the spec calls for it)
- Sticky elements stay sticky
- No layout shift artifacts at the scroll boundary

### 5. Scroll back to top before switching viewports

```
mcp__playwright__browser_evaluate(function: "() => window.scrollTo(0, 0)")
```

Fresh state for the mobile pass. Resizing with a scrolled viewport mid-audit can produce layout shifts that look like real bugs but are just stale scroll position.

### 6. Hit the three mobile breakpoints — in this order

Order matters. Hit **390 first** because it is the most common real-user viewport — if this is broken, the build fails in its most common condition. Then narrow to 375 to catch wraps, then widen to 428 to catch single-column desktop-layout-leak.

| Order | Width × Height | Device | What it catches |
|-------|----------------|--------|-----------------|
| 1 | **390 × 844** | iPhone 14 / 15 | the most common real user viewport — highest-value screenshot |
| 2 | **375 × 812** | iPhone SE / 13 mini | narrowest active iOS — any wrap or overflow shows here first |
| 3 | **428 × 926** | iPhone 14/15 Pro Max | widest single-column — last place desktop layouts break down |

```
mcp__playwright__browser_resize(width: 390, height: 844)
mcp__playwright__browser_take_screenshot(filename: "verify-mobile-hero-390.png")

mcp__playwright__browser_resize(width: 375, height: 812)
mcp__playwright__browser_take_screenshot(filename: "verify-mobile-375.png")

mcp__playwright__browser_resize(width: 428, height: 926)
mcp__playwright__browser_take_screenshot(filename: "verify-mobile-428.png")
```

**At every mobile width, visually verify:**
- Hero fits above the fold (eyebrow + H1 + tagline + at least primary CTA all visible without scroll)
- H1 has **no orphan lines** — no single word alone on its own line mid-phrase
- No horizontal scroll (the "wider than the viewport" bug is invisible in file audits)
- Touch targets look ≥44px
- Images are not clipped or cut off at the sides
- Emoji renders (not showing as boxes or missing glyphs)
- Console is still 0 errors / 0 warnings at **each** viewport — some warnings only fire on responsive class changes

### 7. Open the mobile nav panel (at 390)

```
mcp__playwright__browser_resize(width: 390, height: 844)
mcp__playwright__browser_snapshot(depth: 3)
# find the "Open navigation menu" button ref from the snapshot
mcp__playwright__browser_click(element: "mobile hamburger", ref: "<ref>")
mcp__playwright__browser_take_screenshot(filename: "verify-mobile-nav-open.png")
```

Verify in the screenshot:
- Nav panel slides in cleanly with its animation
- Logo / branding in panel header matches the desktop nav version
- All links readable with enough contrast
- CTA button visible at the bottom of the panel (not pushed offscreen)
- Background overlay is dark and opaque, not transparent (a see-through overlay is a build failure)

### 8. Close the mobile nav panel — USE THE X INSIDE THE PANEL

```
mcp__playwright__browser_snapshot(depth: 4)
# find the "Close navigation menu" button ref — this is INSIDE the dialog, NOT the original hamburger
mcp__playwright__browser_click(element: "X close button inside the mobile nav dialog", ref: "<new ref>")
```

**GOTCHA — this is a real trap.** Clicking the hamburger button by its original ref when the panel is open causes a 5-second Playwright timeout. The hamburger is still in the DOM at the original ref, but it is now **behind the panel overlay** — Playwright cannot click through an overlaid element. You must target the `<button aria-label="Close navigation menu">` that lives **inside the opened dialog**.

**Always re-snapshot after opening the panel.** The refs change — the panel's own close button has a ref that didn't exist before you opened it.

### 9. If you fix a bug mid-audit, re-verify at every affected breakpoint

Do not just re-check the breakpoint where you noticed the bug. A CSS variable change (for example the `--text-display: clamp()` fix) affects **every viewport**.

After any fix:
- Re-screenshot all four (1440 + 390 + 375 + 428)
- Re-read the console at each viewport — fixes can introduce warnings elsewhere
- Re-open and re-close the mobile nav if the fix touched header or typography tokens

A bug fixed at one breakpoint that regresses another is the worst possible outcome of this audit — it is a confident "fixed" commit that ships a regression.

### 10. Commit fixes with specific messages, push to GitHub

- **One commit per distinct fix.** Do not bundle an H1 rewrite and a responsive type scale fix into one commit — they are independent changes and need independent commit history for future retrospectives.
- Reference the breakpoint where you caught it in the commit body (`caught at 390px during end-of-build audit`).
- Push after every commit — standing rule.

### 11. Stop the dev server — do not skip this

```
TaskStop(task_id: "<the background task ID from step 1>")
```

**GOTCHA — `mcp__playwright__browser_close` does NOT stop the dev server.** It only closes the browser tab. The Next.js process keeps running in the background, continues to write output to its temp file, and wastes conversation context on every subsequent tool call that reads background task output. You **must** explicitly call `TaskStop` with the task ID you saved in step 1.

If you forgot to save the task ID, list background tasks and kill the npm/next one by process.

## Exit Criteria

The audit passes only when **all** of the following are true:

- [ ] Dev server reached `✓ Ready` before the first navigation
- [ ] Desktop 1440×900 screenshot captured, hero renders correctly
- [ ] Desktop scrolled screenshot captured, nav behavior matches spec
- [ ] Mobile 390 screenshot captured, hero fits above the fold with no orphans
- [ ] Mobile 375 screenshot captured, no wraps or overflow
- [ ] Mobile 428 screenshot captured, no single-column layout breaks
- [ ] Mobile nav panel opened at 390, screenshot captured, overlay is dark/opaque
- [ ] Mobile nav panel closed via the inner X button (not the hamburger)
- [ ] Console returned 0 errors and 0 warnings at **every** viewport
- [ ] Any fixes applied triggered a full re-verify of all four breakpoints
- [ ] Dev server stopped with `TaskStop`, background task confirmed killed

Any unchecked item = audit incomplete = build not ready to ship.

## Key Rules

- **Read the dev server output file before navigating** — confirm `Ready in Xms` first, or you are screenshotting a blank page.
- **Always `browser_wait_for(text)` on post-hydration content** after navigate. Static shell text lies.
- **`browser_close` does not stop the dev server.** `TaskStop` always.
- **Check console at every breakpoint**, not once. Responsive class changes fire new warnings.
- **Hamburger ref is stale when the panel is open.** Click the inner X only.
- **Four breakpoints is the floor, not the ceiling.** Add 768 (tablet) and 1024 (small desktop) for any project with responsive behavior that changes at those widths — blog templates, service area grids, testimonial grids.
- **Ambient page animation check:** while auditing each page, verify the Page Animation Rule is honored — interior pages must not be flat. Flag any static interior header as a build failure and fix before ship.
- **Alternation check:** on the homepage, scroll slowly and verify the Section Alternation Rule — no two adjacent sections share the same background tone.

## What This Catches That Other Checks Don't

- Font size fixed in rem instead of `clamp()` → wraps orphan words on mobile ([[errors/fixed-rem-display-font-size-breaks-mobile]])
- `items-center` on `min-h-screen` hero → text mid-screen on short mobile (build-log #25)
- Long pill badges with `whitespace-nowrap` overflowing on mobile (build-log #16)
- H1 copy that fits desktop grid but wraps awkwardly on mobile grid
- Placeholder components that render in prod because `onError` fires on hydration (build-log #34)
- Hero text invisible against background — wrong color token on dark bg (build-log #29)
- Console warnings from `next/image` sizes, Framer Motion variants, React key warnings
- Scroll-bound animations that fire on every scroll instead of once
- Hover states that only exist on desktop leaving mobile dead zones
- Fixed-width sidebars or columns that cause horizontal scroll on 375
- Canvas hero animations that clip their tip behind CTAs on short mobile viewports (build-log #11)
- Mobile nav overlay that is transparent instead of dark

## Reuse Condition

**Use on every build.** This is the final gate before marking a project complete. No exceptions. No "looks fine on my screen."

For projects with a shop, blog, quiz, or booking flow: extend the audit to cover the key conversion flow at mobile 390 — add the cart drawer open, the quiz in-flight, and the booking calendar with a date selected as additional screenshots. If the conversion flow is broken on 390, the build is not shippable.

## Related

- [[errors/fixed-rem-display-font-size-breaks-mobile]] — the bug this workflow caught on its first use
- [[patterns/clamp-responsive-type-scale]] — the fix produced by the catch
- [[patterns/conversion-first-hero-headline]] — the work this audit was verifying
- CLAUDE.md Visual QA Rule — enforcement layer
- build-checklist.md Phase 1 step 14 — human-facing scheduling layer
- project-prime.md Stage 1I — orchestrator execution layer (the actual playbook runs here)
- website-build-template.md Checklist: Before Launch → Visual QA — template reference layer
- .claude/agents/launch/pre-launch-auditor.md Section 11 — agent handoff to orchestrator-run audit
