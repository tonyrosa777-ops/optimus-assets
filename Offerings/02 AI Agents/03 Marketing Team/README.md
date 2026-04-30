# Marketing Team — Tier 3

The Self Learning Content Engine. **The first true scheduled-cron agent in the Optimus stack.** Runs every Sunday at 18:00 EST, pulls 30-day social media performance from Supabase, scores it pillar-by-pillar, generates next week's strategy via Claude (Sonnet weekly · Opus monthly deep-eval), and surfaces content gaps, saturation warnings, and identity-conversion signals.

Tier-3 in the four-tier upsell ladder: **$3,500 setup + $1,497/mo**. Marketing Team is also the **prerequisite template every Tier-4 Autonomous AI Employee build inherits** — the marketing module ships preloaded into every Autonomous Employee.

Cross-references:
- Build spec: [[python-architecture|python-architecture.md]]
- Tech-stack rationale: [[tech-stack-research]]
- Marketing-specific concepts: [[concept-notes]]
- Optimus's own dogfood instance: [[../../../Optimus Inc/ai-agents/marketing-team/README|Optimus's own marketing-team instance]]
- Founder layer: [[../../../anthony-rosa/north-star]]

---

## Why it exists

Most content advice is "post 5 times a week, stay consistent." That doesn't tell you what to post. The Marketing Team closes that loop: it looks at what worked, what didn't, where the audience is saturated, where they're under-served, and writes the strategy for the next 7 days based on data — not based on whatever the client felt like that Sunday.

Three things it does that a content calendar tool doesn't:

1. **Pillar-balanced strategy.** Every week's plan respects the configured pillar split. No drift to all-one-pillar because that pillar happened to perform last week.
2. **Saturation detection.** When a topic or format starts producing diminishing returns, the engine flags it before the client hits the wall.
3. **Identity-conversion signals.** Saves vs repeat-viewers vs follower-conversion vs comment-quality — these track whether the audience is becoming a community, not just whether the algorithm is showing the post.

---

## Product spec

Per the canonical Optimus stack ([`../shared-knowledge/tech-stack.md`](../shared-knowledge/tech-stack.md)) — Python from day one, anthropic SDK direct (no other LLM providers, no visual workflow orchestrators):

| Component | Choice |
|---|---|
| **Backend** | Python · FastAPI · Pydantic v2 · supabase-py |
| **Schedule** | APScheduler cron `0 18 * * 0` (Sundays 18:00 EST) inside the FastAPI service |
| **Data source** | Supabase Postgres — 30-day rolling performance table (per platform, per post: reach, saves, shares, comments, follower delta, completion rate) |
| **Pillars (per-client configurable)** | Stored in Supabase keyed by `client_id`; pillar definitions read at run time |
| **Strategy generation** | anthropic SDK (Claude Sonnet weekly · Opus monthly deep-eval) with prompt caching on pillar definitions + scoring rubric + system prompt |
| **Structured output** | Pydantic `WeeklyStrategy` schema, validated via Anthropic tool-use as structured output |
| **Storage** | Supabase Postgres (strategies table) |
| **Notification** | Webhook (email digest default; Slack/SMS configurable) |
| **Optional** | ElevenLabs HTTP for audio strategy briefings |

Full Pydantic schemas and FastAPI endpoint signatures: [[python-architecture]].

What v1 ships:
- Strategy-only — engine outputs the weekly plan; humans execute
- Per-client pillar configuration (database-driven, not hardcoded)
- Aggregator-driven data ingestion (Phyllo or per-platform native APIs — decision per client at onboarding)

What v1 doesn't do (later expansion):
- Direct posting to platforms — the **Approval primitive** ([`../shared-knowledge/agent-infrastructure.md`](../shared-knowledge/agent-infrastructure.md) § 4) governs every posted item indefinitely; high-stakes external-facing actions never graduate to autonomy

---

## Why this product matters strategically

Marketing Team is the **first true scheduled-cron agent** in the Optimus stack and the **agent-architecture reference pattern** every subsequent Optimus agent (Voice Receptionist, Tier-4 Autonomous Employee) inherits. Specifically:

- Sets the shape of "agent that runs on a schedule, observes state, makes decisions, writes structured outputs to a state store."
- First true exercise of all four agent-infrastructure primitives (memory · tools · observability · approval).
- The Drink-Own-Champagne 2027-Q3 milestone (per [`../../../anthony-rosa/north-star.md`](../../../anthony-rosa/north-star.md) § The Drink-Own-Champagne Milestone) runs through Optimus's own dogfood instance of this product first.

It is also a standalone product — clients who don't need Tier-4's full autonomy can stay at Tier-3 indefinitely.

---

## Linked notes

- [[python-architecture]] — complete build spec (Pydantic schemas · FastAPI signatures · Mermaid diagram)
- [[tech-stack-research]] — stack rationale, ingestion options, why Claude is the LLM
- [[concept-notes]] — marketing-specific concepts (pillar frameworks, identity signals, saturation detection, cross-platform output)
- [[../shared-knowledge/agent-infrastructure]] — the four primitives this product is the first true use case for

---

## Optimus's own deployed instance

This product runs Optimus's own content strategy. The dogfood instance is also where pillar tuning, saturation thresholds, and prompt iteration happen first — before paying clients touch the system.

[[../../../Optimus Inc/ai-agents/marketing-team/README|Optimus's own marketing-team instance]]

By 2027-Q3, Optimus's own marketing pipeline runs autonomously through this product (Drink-Own-Champagne milestone), ahead of the Tier-4 employee taking over coordination of marketing + inbound + scheduling.

---

#offering/content-engine #status/active
