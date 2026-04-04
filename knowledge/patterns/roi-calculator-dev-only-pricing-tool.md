# Pattern: ROI Calculator + Comparison Chart as Dev-Only Pricing Sales Tools

**Category:** Conversion / Pricing / Workflow
**First used:** Gray Method Training — Mar 2026

## What

Build an interactive ROI calculator and feature comparison chart into the pricing page during development. Gate both behind an environment variable so they display during the sales conversation with the client, then are removed before the page goes live to the public.

## When to Use

Any service-based client where:
- The investment is $1,500+ and requires justification
- The client may hesitate on price without seeing the math
- The pricing page is not yet finalized but needs to be presented

## How

**ROI Calculator inputs (sliders):**
```ts
const [leads, setLeads] = useState(10);          // monthly leads from site (1-20)
const [closeRate, setCloseRate] = useState(25);  // lead-to-client rate (5-50%)
const [avgValue, setAvgValue] = useState(3000);  // avg client value ($500-10k)
```

**Calculations:**
```ts
const metrics = useMemo(() => {
  const closed = leads * (closeRate / 100);
  const monthly = closed * avgValue;
  return {
    closedPerMonth: closed,
    revenuePerMonth: monthly,
    revenuePerYear: monthly * 12,
    breakEvenMonths: tiers[selectedTier].price / monthly,
    breakEvenClients: tiers[selectedTier].price / avgValue,
  };
}, [leads, closeRate, avgValue, selectedTier]);
```

Use `CountUp` animation on all output values. Package selector tabs let the client switch tiers and see the math recalculate.

**Comparison chart** — feature matrix with ✓ / — per tier. Featured tier column highlighted.

**Environment gate:**
```tsx
// Wrap both tools in an env check
{process.env.NEXT_PUBLIC_SHOW_PRICING_TOOLS === 'true' && (
  <>
    <ROICalculator tiers={tiers} />
    <TierComparisonChart features={features} />
  </>
)}
```

Set `NEXT_PUBLIC_SHOW_PRICING_TOOLS=true` in local `.env.local` during development. Set `=false` or remove before launch.

## Key Rules

- These are sales tools, not public UX — they make the pricing page feel like a spreadsheet for general visitors
- Always document the env flag in `SETUP.md` so the client knows it exists
- The ROI calculator's default slider values should be conservative (not aspirational) so the math feels credible
- Break-even time is the most persuasive output — lead with it in the display layout

## Reuse Condition

Any build where you're selling the website itself to the client AND the client needs to see ROI before committing. Also works for coaching/consulting clients who want to show ROI to their own prospects (the calculator stays visible as a public conversion tool in that case).

## Related

- [[patterns/pricing-three-tier-anchoring]]
