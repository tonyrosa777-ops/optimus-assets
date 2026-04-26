---
tags: [layer/optimus-os, status/active]
---

# Social Pipeline — Optimus's Own Marketing Operations

Optimus's own content calendar, active campaigns, and pipeline data. The output side of marketing — what actually gets published.

## Brain vs output

The brain is `[[../ai-agents/marketing-team/README]]`. The Self Learning Content Engine generates strategy: which pillars are working, what topics to cover next, when the audience is saturated on a given theme.

The output is this folder. The strategy from the brain becomes a calendar entry, becomes a campaign brief, becomes a published post. Performance data flows back to the brain to tune future strategy.

If you are working on *what* to say next week, you are in the brain (`marketing-team/`). If you are working on *what is published when across which platforms*, you are here.

## Subfolders

### `content-calendar/`
What Optimus is publishing when, across which platforms. Format TBD — likely a rolling 4-6 week view, one file per week or one file per platform per month, whichever proves easier to maintain.

Tracks:
- Platform (LinkedIn, X, YouTube, Instagram, podcast, blog)
- Pillar (per Optimus pillars in `[[../ai-agents/marketing-team/README]]`)
- Hook + asset type
- Status (drafted / scheduled / published)
- Performance after publish (engagement, leads attributed, reach)

### `campaigns/`
Active campaign briefs and performance reads. A campaign here means a coordinated push around a single theme, launch, offer, or experiment that spans multiple posts and platforms over a defined window.

One folder per campaign. Each contains the brief (objective, audience, channels, dates, assets, success metric) and the post-mortem after it ends (what hit, what missed, what to take into the next one).

## Cadence

- Calendar updated continuously as posts ship and new strategy lands from the Marketing Team
- Campaign briefs: written before campaign start, updated weekly during, post-mortemed within 7 days of end
- Performance feedback to the Marketing Team brain: weekly minimum

## Cross-references

- Strategy brain: `[[../ai-agents/marketing-team/README]]`
- Brand voice the content speaks in: `[[../brand/README]]`
- Competitive intel that informs positioning: `[[../market-intelligence/README]]`
- Site this drives traffic to: `[[../website/README]]`
