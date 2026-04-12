# Pattern: Blog CTA — Quiz + Book Over Newsletter Capture
**Category:** Conversion / Content
**First used:** Gray Method Training — Apr 2026

## What
At the end of every blog article, replace the traditional "subscribe to our newsletter" CTA with a two-action card: primary CTA takes them to the scored quiz, secondary CTA opens the calendar booking link. No email capture, no "get our best content", no drip sequence.

## When to Use
- Client has a working scored quiz that routes to personalized program recommendations
- Client has a calendar booking link (Calendly, Cal.com, etc.)
- The business model is 1:1 coaching / consulting / high-ticket services where the goal is to book a conversation, not build a newsletter list
- Blog traffic is top-of-funnel — readers are researching, not ready to buy
- The client doesn't have existing email infrastructure (no ConvertKit, Mailchimp, etc.)

## How

Replace `<NewsletterSignup />` at the end of the blog post template with a simple card:

```tsx
<div className="mt-16 pt-10 border-t border-white/5">
  <div className="rounded-2xl bg-gray-elevated border border-gold/20 p-8 md:p-10">
    <p className="font-mono text-xs text-gold tracking-widest uppercase mb-4">
      Ready to put this into practice?
    </p>
    <h3 className="font-display font-semibold text-2xl md:text-3xl text-gray-text leading-tight mb-3">
      Stop reading about it. Start doing it.
    </h3>
    <p className="font-body text-gray-text-2 mb-8 max-w-md">
      Take the 2-minute quiz to find out which [program] fits where you are right now —
      or book a free call and we'll figure it out together.
    </p>
    <div className="flex flex-wrap gap-4">
      <Button href="/quiz" variant="gold" size="lg">
        Find My Program
      </Button>
      <Button
        href={process.env.NEXT_PUBLIC_CALENDLY_URL ?? "/contact"}
        variant="ghost"
        size="lg"
        external={!!process.env.NEXT_PUBLIC_CALENDLY_URL}
      >
        Schedule a Free Call
      </Button>
    </div>
  </div>
</div>
```

## Key Rules
- **Headline must be direct and slightly confrontational** — "Stop reading about it. Start doing it." is deliberately blunt. Soft headlines ("Want to learn more?") kill the CTA.
- **Primary CTA is the quiz, not the booking** — the quiz is lower friction (no commitment, 2 minutes, feels like a tool) and routes to the best-fit program. Booking is higher intent and belongs as the secondary option for ready-to-buy readers.
- **Booking button uses `external` prop** — opens Calendly in a new tab so the blog post stays open. If no Calendly URL env var is set, fall back to `/contact` as internal link.
- **No email field anywhere** — the friction of filling out an email for "content" kills conversion. The quiz collects the email naturally during the Calendly step after results.
- **Copy must reference the actual client offering** — replace `[program]` with the real program name (e.g. "Gray Method program"). Generic copy underperforms.
- **Use on EVERY blog post** — this is the blog post template, not a per-post decision.

## Reuse Condition
Use this pattern on any client build where:
- A scored quiz already exists (see [[patterns/quiz-multistep-lead-capture-program-recommendation]] and [[patterns/scored-quiz-lead-funnel]])
- The client has ≤3 core offerings that map to quiz outcomes
- The client is selling services, not products
- The client does NOT have an existing email marketing program worth preserving

If the client has a legitimate email list and wants to grow it, keep the newsletter CTA and add the quiz+book card as a secondary block. Don't remove email capture from a working funnel.

## Related
- [[patterns/scored-quiz-lead-funnel]] — the quiz this CTA routes to
- [[patterns/calendly-inline-embed-brand-colors]] — the calendar this CTA opens
