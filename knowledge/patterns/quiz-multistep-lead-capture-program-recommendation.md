# Pattern: Quiz Multi-Step Lead Capture with Program Recommendation

**Category:** Conversion / Lead Generation
**First used:** Gray Method Training — Mar 2026

## What

A 3-step animated quiz that segments visitors by pain points and goals, captures their contact info, then presents a personalized program recommendation. Doubles as a lead magnet and a conversion funnel — visitors who complete it have higher intent than form-fill leads.

## When to Use

Any service-based brand with multiple offerings where:
- Visitors arrive with different problems (can't lose weight, low energy, stress, etc.)
- There are 2-4 distinct program tiers or approaches
- The brand wants to qualify leads before a sales call

## How

**Step flow:**
```
Step 0 — Intro screen
  Headline, 3 bullets explaining the quiz, "Start" CTA

Step 1 — Problems (multi-select, 4-6 options with emojis)
  "What's holding you back right now?"
  Continue disabled until ≥1 selected

Step 2 — Goals (single-select, 3-4 options with emojis)
  "What matters most to you?"
  Continue disabled until exactly 1 selected

Step 3 — Lead capture form
  Name (required), Email (required), Message (optional)
  CTA: "Get My Personalized Plan →"

Post-submit — Results screen
  Show selected answers back to the user
  Personalized recommendation based on selections
  Primary CTA: schedule call / book intake
  Secondary CTA: explore programs
```

**Implementation skeleton:**
```tsx
// State
const [step, setStep] = useState(0); // 0=intro, 1=problems, 2=goals, 3=form, 4=result
const [selectedProblems, setSelectedProblems] = useState<string[]>([]);
const [selectedGoal, setSelectedGoal] = useState<string>("");

// Progress bar
const progress = step === 0 ? 0 : ((step - 1) / 3) * 100;

// Step transitions
<AnimatePresence mode="wait">
  <motion.div key={step} variants={stepVariants} initial="hidden" animate="visible" exit="exit">
    {renderStep(step)}
  </motion.div>
</AnimatePresence>

// Form submits to /api/contact with quiz data appended as structured notes
const payload = {
  name, email, message,
  quizProblems: selectedProblems.join(", "),
  quizGoal: selectedGoal,
};
```

**Program recommendation logic** (map answers → program):
```ts
// Simple decision tree or weighted scoring
const recommend = (problems: string[], goal: string): Program => {
  if (goal.includes("habits")) return "group";
  if (problems.includes("drained") || problems.includes("stress")) return "energize-empower";
  return "one-on-one";
};
```

## Key Rules

- Multi-select for problems (people have more than one pain), single-select for goals (forces prioritization)
- Keep each step to a single screen — no scrolling within a step
- Show a visible progress bar — it signals the commitment required and reduces abandonment
- Display the user's selections back in the result screen — it makes the recommendation feel personalized
- Include `quizProblems` and `quizGoal` in the contact form submission so the coach sees context before the call
- Use emojis on option buttons — they're scannable and reduce the cognitive load of reading option text

## Reuse Condition

Any personal brand, coach, or consultant with multiple service tiers. The step structure is universal — only the questions, options, and recommendation logic change per client. Build once, swap data.

## Related

- [[patterns/pricing-three-tier-anchoring]] — quiz recommendation should map to one of the three tiers
