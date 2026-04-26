# Marketing Team

The Self Learning Content Engine. An n8n workflow that runs every Sunday at 6pm EST, pulls 30-day social media performance from Supabase, scores it across four content pillars (Health / Wealth / Wisdom / Integration), generates the next week's strategy via GPT-4o, and surfaces content gaps, saturation warnings, and identity-conversion signals.

Status: in development as of 2026-04-26. The workflow JSON exists and runs — see [[workflows/self-learning-content-engine]]. Pricing TBD — likely a setup fee plus monthly subscription. Productization gates: client-configurable pillars, automated data ingestion, multi-platform output.

## Why it exists

Most content advice is "post 5 times a week, stay consistent." That doesn't tell you what to post. The Marketing Team closes that loop: it looks at what worked, what didn't, where the audience is saturated, where they're under-served, and writes the strategy for the next 7 days based on data — not based on whatever the client felt like that Sunday.

Three things it does that a content calendar tool doesn't:

1. **Pillar-balanced strategy.** Every week's plan respects the four-pillar split. No drift to all-Wealth or all-Wisdom because that pillar happened to perform last week.
2. **Saturation detection.** When a topic or format starts producing diminishing returns, the engine flags it before the client hits the wall.
3. **Identity-conversion signals.** Saves vs repeat-viewers vs follower-conversion vs comment-quality — these track whether the audience is becoming a community, not just whether the algorithm is showing the post.

## Product spec (v1)

The current implementation, running today:

- **Trigger:** n8n schedule trigger, cron `0 18 * * 0` (Sundays 6pm EST)
- **Data source:** Supabase table with 30-day rolling social performance data (per platform, per post: reach, saves, shares, comments, follows-from-post, completion rate where applicable)
- **Pillars (configurable per client — currently hardcoded to Optimus's own pillars):** Health / Wealth / Wisdom / Integration
- **Strategy generation:** GPT-4o with a prompt that scores recent performance, detects saturation, identifies gaps, and outputs a structured weekly plan
- **Output:** structured strategy written back to Supabase, surfaced via dashboard and weekly digest

What v1 doesn't do yet:

- Automated data ingestion from social platforms (Supabase population is currently manual or semi-automated)
- Direct posting to platforms
- Per-client pillar customization (the framework exists, the UI doesn't)
- Migration to Claude Sonnet/Opus from GPT-4o

## Linked notes

- [[concept-notes]] — marketing-specific concepts (pillar frameworks, identity signals, saturation detection, cross-platform output)
- [[tech-stack-research]] — current stack + things to investigate
- [[workflows/self-learning-content-engine]] — the n8n workflow JSON

## Optimus's own deployed instance

This product is the most dogfooded of the three. Optimus runs its own marketing team on this engine right now:

- [[../../../Optimus Inc/ai-agents/marketing-team/README|Optimus's own marketing-team instance]]

Every weekly strategy that goes into Optimus's own content output came out of this engine. The dogfood instance is also where pillar tuning, saturation thresholds, and prompt iteration happen first.

---

#offering/content-engine #status/in-development
