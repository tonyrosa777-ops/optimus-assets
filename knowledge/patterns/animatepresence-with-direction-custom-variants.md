# Pattern #68 — AnimatePresence-with-direction custom variants (Framer Motion v12)

**First shipped:** Ead Financial, Stage 1E Step 5 (`/quiz` 3-phase state machine), 2026-05-10 commit `9e4abf8`.
**Status:** VALIDATED. Reuse on every step-by-step UI surface (quizzes, wizards, multi-step forms, month-grid calendars, pagination).
**Category:** Visual Design / Animation / Motion / React Patterns

---

## Why this pattern exists

Step-by-step UIs (quiz questions, wizard steps, month-grid calendar pagination, multi-step booking flows) need transitions that communicate **direction** — forward navigation should slide one way, back navigation the other way. Without direction-awareness, every transition looks identical and the user loses the spatial mental model of "where am I in the flow."

Framer Motion v12's AnimatePresence supports this via the `custom` prop, which forwards a value to variant functions. The `dir: 1 | -1` parameter convention (1 = forward, -1 = back) is the canonical shape — used in Enchanted Madison's FindYourEscapeWizard (2026-Q1), Ead Financial's QuizClient (2026-05), and now standard for Optimus step-by-step UIs.

This pattern documents the canonical implementation so subsequent agents (Step 6's BookingCalendar month-grid, future wizard surfaces, multi-step Tier-4 onboarding) copy it verbatim instead of improvising direction handling — which is easy to get wrong (forgetting `mode="wait"` causes overlapping cards; forgetting custom prop forwarding silently breaks direction awareness).

---

## The canonical implementation

### Component shape

```tsx
"use client";  // MUST be first token for any component using motion (Error #9)

import { AnimatePresence, motion, type Variants } from "framer-motion";
import { useState, useEffect } from "react";

const slideVariants: Variants = {
  enter: (dir: 1 | -1) => ({ x: dir * 48, opacity: 0 }),
  center: { x: 0, opacity: 1 },
  exit: (dir: 1 | -1) => ({ x: dir * -48, opacity: 0 }),
};

export function StepByStepUI() {
  const [stepIndex, setStepIndex] = useState(0);
  const [direction, setDirection] = useState<1 | -1>(1);
  const [reduceMotion, setReduceMotion] = useState(false);

  // prefers-reduced-motion subscription with change-event handling
  useEffect(() => {
    const mq = window.matchMedia("(prefers-reduced-motion: reduce)");
    setReduceMotion(mq.matches);
    const onChange = (e: MediaQueryListEvent) => setReduceMotion(e.matches);
    mq.addEventListener("change", onChange);
    return () => mq.removeEventListener("change", onChange);
  }, []);

  function goForward() {
    setDirection(1);
    setStepIndex((i) => i + 1);
  }

  function goBack() {
    setDirection(-1);
    setStepIndex((i) => i - 1);
  }

  return (
    <AnimatePresence custom={direction} mode="wait">
      <motion.div
        key={stepIndex}
        custom={direction}
        variants={slideVariants}
        initial="enter"
        animate="center"
        exit="exit"
        transition={
          reduceMotion
            ? { duration: 0 }
            : { duration: 0.28, ease: "easeOut" as const }
        }
        data-step-card  // optional — enables Phase C visual targeting
      >
        {/* step content here */}
      </motion.div>
    </AnimatePresence>
  );
}
```

### Critical rules

1. **`AnimatePresence` MUST receive `custom={direction}`.** Without it, the variant functions can't read the direction parameter and the slide direction will be hardcoded to whatever the function defaults to.
2. **`motion.div` MUST also receive `custom={direction}`** at the inner level. AnimatePresence forwards it, but the inner motion component re-reads it independently for the exit variant (which fires from the OLD component before the NEW one mounts).
3. **`mode="wait"` is required.** Without it, the exit transition of the outgoing card overlaps the enter of the incoming card → both visible simultaneously → broken UX. With `mode="wait"`, AnimatePresence holds the new card off-screen until the old card's exit completes.
4. **`key={stepIndex}` (or equivalent) is required.** Without a stable key per step, React doesn't know to unmount-then-remount the motion.div, so the exit/enter cycle never fires.
5. **`Variants` typing uses `"easeOut" as const`** — Framer Motion v12 strict typing rejects `ease: number[]` cubic bezier arrays inside `Variants` objects (Error #8 cross-project).
6. **Reduced-motion handling collapses to `duration: 0`** — NOT `animate={{}}` skip-render, NOT removing the wrapper. Keep the structural transition (so React still mounts/unmounts the new card cleanly), just skip the visual motion. This preserves all functional behavior identically.
7. **The `dir: 1 | -1` parameter convention** is canonical: 1 = forward (slide right-to-left, exit goes left); -1 = back (slide left-to-right, exit goes right). Match the user's spatial expectation — going forward feels like advancing through pages, going back feels like rewinding.

---

## Worked examples in production

- **Ead Financial QuizClient.tsx** (commit `9e4abf8`) — 3 phase wrappers (intro / question / results) wrapped in single AnimatePresence with phase-specific `key`, `dir` toggles between forward (next question, intro→question, question→results) and back (back button on Q2-Q5).
- **Enchanted Madison FindYourEscapeWizard.tsx** (Q1 2026) — 6-phase wizard, same custom-variants pattern, `dir` toggles via `setDirection(forward ? 1 : -1)`.

---

## When to use vs. when not to use

**Use this pattern when:**
- Multi-step UI (wizards, quizzes, booking calendars with month-grid pagination, multi-step forms)
- The user can navigate both forward and back through a sequence
- Spatial direction awareness aids the mental model (each step feels like a position in the flow)

**Do NOT use this pattern when:**
- One-way reveal animations (use FadeUp scroll trigger from `web/src/components/animations/FadeUp.tsx`)
- Simple show/hide toggles (use opacity transition without AnimatePresence)
- Modal open/close (use ScaleIn or built-in Radix Dialog transitions)
- Tab switching where tabs are peer-positions, not sequential steps (use opacity crossfade, not directional slide)

---

## Reduced-motion contract — non-negotiable

Every implementation of this pattern MUST handle `prefers-reduced-motion: reduce`. The minimum acceptable implementation:

1. **Detect the preference** via `useState + useEffect + matchMedia` with change-event listener (so dynamic OS toggling mid-session is honored — users who toggle accessibility settings while the app is open get the new preference applied immediately).
2. **Collapse the transition duration** to 0 when reduceMotion is true. Functionality identical; visual motion stops.
3. **Do NOT skip the AnimatePresence wrapper** — keep the structural mount/unmount cycle so the component lifecycle remains predictable.
4. **Backdrop / ambient gradients** (separate from the step transitions) get their own `@media (prefers-reduced-motion: reduce)` CSS rule — gradient stays, motion stops (CLAUDE.md anti-pattern #14: NEVER flat).

Skipping reduced-motion handling means accessibility users get a broken-feeling UI with mid-flight motion that ignores their OS preference. Silent failure — no console error, no obvious bug. Compounds across every step-by-step surface in the codebase.

---

## Verification checklist (Phase C in any build that uses this pattern)

- [ ] `AnimatePresence` wraps the swappable content and receives `custom={direction}`.
- [ ] Inner `motion.div` ALSO receives `custom={direction}` and has a `key` that changes per step.
- [ ] `mode="wait"` is set on AnimatePresence.
- [ ] `slideVariants` uses `dir: 1 | -1` parameter convention (1 = forward, -1 = back).
- [ ] Transition uses `"easeOut" as const` or named easing string (NOT `ease: number[]`).
- [ ] `prefers-reduced-motion` subscribed via `matchMedia` + change-event listener.
- [ ] Reduced-motion path collapses transition duration to 0 (NOT removing the wrapper).
- [ ] At runtime: forward navigation slides one direction, back navigation the opposite direction (manual visual check OR `data-step-card` attribute targeting for automated tests).
- [ ] Console clean during transitions (no React key warnings, no AnimatePresence warnings).

---

## Failure modes if not followed

- **`mode="wait"` missing** → exit + enter overlap, two cards visible simultaneously, broken UX.
- **`custom` prop not forwarded to inner motion.div** → exit variant uses default direction (whatever the function defaults to when `dir` is undefined), back-button transitions look identical to forward.
- **Stable `key` missing on motion.div** → React doesn't unmount-then-remount, exit/enter cycle never fires, no transition.
- **`ease: [0.4, 0, 0.2, 1]` (cubic bezier array)** → Framer Motion v12 strict typing rejects this inside Variants → TypeScript build error per Error #8. Use `"easeOut" as const` instead.
- **Reduced-motion ignored** → silent accessibility failure. No console error, no obvious bug, but accessibility users perceive the UI as broken.
- **Forward direction set to -1 (or vice versa)** → spatial mental model inverted. Users feel disoriented. Easy bug — guard with explicit `setDirection(1)` on every forward action and `setDirection(-1)` on every back action; never default.

---

## Compatibility notes

- **Compatible with Pattern #51** (luxury gradient backgrounds) — gradient backdrop stays static during step transitions; only the inner card slides.
- **Compatible with Pattern #66** (Next 16 dynamic-route Promise params) — independent concerns. AnimatePresence works inside any route, dynamic or static.
- **Compatible with Pattern #67** (dark-section ink-on-ink gradient) — step cards can be on dark or light surfaces.
- **Framer Motion version:** v12+ required for the `custom` prop and `Variants` strict typing. Confirmed in Ead Financial codebase at `framer-motion@12.38.0`.
- **Performance:** counts as 1 motion layer in the per-page motion budget (Pattern #51: max 3 active layers visible simultaneously). The AnimatePresence transition is short (~280ms) so it's only briefly on-screen during step changes.

---

## Why direction-awareness matters (UX rationale)

Step-by-step UIs without direction awareness feel disorienting because every transition looks identical regardless of whether the user is advancing or rewinding. Direction-aware transitions match the user's spatial expectation — going forward feels like turning pages in a book (page slides in from the right, the old page exits left); going back feels like rewinding (page slides in from the left, the old page exits right). This is a low-cost, high-impact UX win: the implementation cost is minimal (one extra state variable + variant function parameter), and the user's mental model is preserved across every interaction.

The cost of getting this wrong: users feel disoriented, click-through rates drop on multi-step flows, and abandonment increases at the back-navigation step (because going back doesn't feel like going back). For any conversion-critical multi-step UI (quiz → result, calendar pick → booking, signup → onboarding), this is a 1-hour implementation that materially affects completion rates.
