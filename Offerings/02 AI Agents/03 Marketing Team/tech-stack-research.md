---
schema-version: 1
last-updated: 2026-04-29
tags: [offering/content-engine, status/active]
---

# Marketing Team — Tech Stack

The Tier-3 product. Self Learning Content Engine — weekly cron agent that ingests social performance data, analyzes pillar-by-pillar saturation, and generates a weekly content strategy for the next cycle. **First true scheduled-cron agent in the Optimus stack — sets the agent-architecture pattern every Tier-4 Autonomous Employee build inherits.** Greenfield Python build from day one.

Cross-references:
- [`python-architecture.md`](python-architecture.md) — complete build spec (Pydantic schemas · FastAPI signatures · Mermaid diagram · sequence diagram for the weekly run)
- [`../shared-knowledge/tech-stack.md`](../shared-knowledge/tech-stack.md) — canonical Optimus stack
- [`../shared-knowledge/agent-infrastructure.md`](../shared-knowledge/agent-infrastructure.md) — the four primitives (this product is the first true use case for all four)
- [`../../../anthony-rosa/north-star.md`](../../../anthony-rosa/north-star.md) — founder layer + Drink-Own-Champagne 2027-Q3 milestone (which runs through this product)

---

## Pipeline

The weekly run, triggered every Sunday at 18:00 EST by APScheduler inside the FastAPI service:

1. **Schedule trigger** — APScheduler fires `run_weekly()` on cron `0 18 * * 0`
2. **Performance ingestion** — Supabase read of the 30-day rolling performance table (per-pillar reach, saves, shares, comments, follower delta, completion rate). Data is pushed in by an upstream ingestion path (per-platform native APIs or a third-party aggregator like Phyllo — final ingestion source decided per client at onboarding).
3. **Pillar analysis** — Pydantic-typed aggregation per pillar produces `PillarPerformance` records. Identity-signal detection runs over the 30-day window producing `IdentitySignal` records. Saturation detection runs producing `SaturationSignal` records.
4. **LLM call** — `anthropic SDK` call to Claude (Sonnet for the weekly synthesis; Opus reserved for the monthly deep-eval that runs every 4th week). System prompt + pillar definitions + scoring rubric all use **prompt caching** — they don't change weekly, so the cache hit rate on every call after the first is near 100%. Output enforced as structured JSON via Anthropic's tool-use as structured output.
5. **Strategy output** — `WeeklyStrategy` Pydantic model validated; strategy written to Supabase `strategies` table.
6. **Optional voiceover** — if the client opts in, the strategy headlines feed into a separate ElevenLabs HTTP call for an audio version of the weekly briefing.
7. **Notification** — webhook fires to the client's chosen notification channel (email digest by default; can configure to Slack or SMS).

Total expected runtime per weekly run: 30–90 seconds. APScheduler holds the FastAPI process awake for the duration; there is no separate cron infrastructure.

---

## Pydantic schemas (named — full shapes in `python-architecture.md`)

| Schema | Role |
|---|---|
| `PillarPerformance` | Per-pillar metrics over the 30-day window |
| `WeeklyStrategy` | The generated strategy output for the upcoming week |
| `IdentitySignal` | Detected shifts in audience identity engagement (e.g. "audience increasingly responding to the AI-Empowerment pillar") |
| `SaturationSignal` | Detected pillar saturation (e.g. "Founder-Story posts have saturated; CTR declining 4 weeks running") |

---

## FastAPI endpoints

```
POST /run-weekly                    — manual trigger / cron entry point
GET  /strategy/{week_iso}           — retrieve a generated strategy by ISO week
POST /ingest/performance            — push performance data into the 30-day table
GET  /pillars/{client_id}           — current pillar configuration for a client
PUT  /pillars/{client_id}           — update pillar configuration (admin only)
```

Schedule trigger calls `POST /run-weekly` internally via APScheduler — same code path as a manual trigger.

---

## Why Claude as the LLM

Three reasons Claude (via the anthropic SDK) is the day-one choice — same reasoning that holds for every Optimus agent:

- **Prompt caching.** Anthropic's prompt caching is the most cost-effective option for this workload — pillar definitions and the scoring rubric never change weekly, so cache hit rate is near 100% on every run after the first.
- **Structured output via tool use.** Claude's tool-use-as-structured-output is more reliable than JSON-mode-and-pray for the strict `WeeklyStrategy` schema. Pydantic validation catches schema drift, but the rate of drift is meaningfully lower with tool-use.
- **Single-vendor standardization.** Every Optimus AI agent uses Claude. One SDK, one cost model, one observability surface. Adding a second LLM provider for one product would create operational drift across the four-tier ladder.

Sonnet for the weekly run; Opus for the monthly deep-eval (every 4th week, deeper reasoning over the 90-day window).

---

## Per-client pillar configuration

Pillars are not hardcoded into the agent. They live in Supabase, keyed by `client_id`:

```
client_pillars
├── client_id: str
├── pillar_name: str
├── pillar_definition: str  (the 1–2 sentence definition the LLM uses)
├── pillar_examples: list[str]  (3–5 anchor posts that exemplify the pillar)
└── pillar_saturation_threshold: float  (CTR decline rate that triggers saturation flagging)
```

Onboarding flow includes a pillar-design step (template library + custom). The strategy prompt becomes parameterized — pillar definitions get read at run time, not baked into the prompt at deploy time.

---

## Data ingestion

Productization blocker — clients won't manually export performance data weekly. Options at first paying client:

| Source | Approach |
|---|---|
| **Instagram** | Meta Graph API (Business accounts only). Rate limits + permission complexity. |
| **TikTok** | TikTok Display API + Business API. Limited metric exposure on Display API. |
| **LinkedIn** | Marketing Developer Platform. Approval gate. |
| **Twitter/X** | API v2. Cost concerns post-2023 pricing. |
| **All-of-the-above via aggregator** (Phyllo, Insense, similar) | Pay for the integration layer instead of building it |

**Lean for v1:** aggregator (Phyllo or similar) for IG + TikTok; native APIs for LinkedIn + Twitter where aggregator coverage is weak. Decision finalized at the first onboarding.

---

## Direct posting (later — not first build)

Strategy-only is the first build. Direct posting (engine outputs strategy → drafts → human approves → engine posts) is a later expansion, requiring:
- Approval UI (likely a custom Optimus admin dashboard built on the same FastAPI service)
- Same platform APIs as ingestion, write-side
- Image/video asset pipeline (likely fal.ai for stills; TBD for short-form video)

When direct posting ships, the **Approval primitive** in [`../shared-knowledge/agent-infrastructure.md`](../shared-knowledge/agent-infrastructure.md) § 4 governs every post. No silent autonomous posting — high-stakes (external-facing) actions stay approval-gated indefinitely.

---

## What this product teaches toward Tier-4 Autonomous AI Employee

This product is the **prerequisite template every Tier-4 build inherits.** The marketing module ships preloaded into every Autonomous Employee. Specifically, Marketing Team teaches:

- **Scheduled-cron agent loop.** The shape of "agent that runs on a schedule, observes state, makes decisions, writes structured outputs to a state store" — this IS the bones of an autonomous agent. Tier-4 employees inherit this shape and expand it across multiple scheduled tasks per agent.
- **Structured-output decisions over long horizons.** Pydantic-typed `WeeklyStrategy` outputs that build on prior weeks' outputs (week N's strategy references week N–1's saturation signals). Tier-4 employees do this across more decision domains.
- **Long-horizon state in Supabase via the four agent-infrastructure primitives.** Marketing Team is the first true use case for **all four primitives**:
  - **Memory store** — episodic (every run logged) · semantic (pillar saturation patterns over 90 days) · procedural (how to respond to a saturation signal)
  - **Tool registry** — Supabase reads, Supabase writes, ElevenLabs voiceover, notification webhook — all permissioned, rate-limited, typed
  - **Observability layer** — every weekly run gets a Langfuse trace · cache hit rate per LLM call · strategy quality scored on a rubric
  - **Approval layer** — direct posting (when v2 ships) goes through approval gates
- **Prompt-caching discipline at scale.** Pillar definitions and scoring rubric cached. Cache hit rate measured. Tier-4 cost economics depend on this discipline.

The Drink-Own-Champagne milestone (2027-Q3) runs through Optimus's own Marketing Team instance specifically — which means by 2027-Q3 this product must be production-hardened on the Optimus dogfood instance before it ships to paying Tier-3 clients.

---

## Status

**Scoped, build in progress.** Will be the first true Optimus agent shipped — the agent-architecture reference pattern. Full build spec lives in [`python-architecture.md`](python-architecture.md). Optimus's own dogfood instance tracked at [`../../../Optimus Inc/ai-agents/marketing-team/README.md`](../../../Optimus%20Inc/ai-agents/marketing-team/README.md).

#offering/content-engine #status/active
