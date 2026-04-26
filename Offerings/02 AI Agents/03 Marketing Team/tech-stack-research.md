# Marketing Team — Tech Stack Research

This product has a working v1, so this file is more "current implementation + roadmap" than pure investigation. Cross-product tech defaults live in [[../shared-knowledge/tech-stack]].

## Current implementation (running today)

| Layer | Tool | Notes |
|---|---|---|
| **Orchestrator** | n8n | Workflow JSON in [[workflows/self-learning-content-engine]]. Self-hosted or n8n Cloud. |
| **Data store** | Supabase | 30-day rolling performance table + strategy output table. Postgres. |
| **LLM** | OpenAI GPT-4o | Strategy generation. Pre-dates Optimus's broader Anthropic-first stance. |
| **Schedule** | n8n schedule trigger | Cron `0 18 * * 0` — Sundays 6pm EST. |
| **Prompt** | Embedded in n8n node | Scoring rubric + pillar definitions + weekly strategy output schema. |

## Things to investigate

### Migrate strategy generation to Claude

GPT-4o is in production and works. But Optimus standardizes on Anthropic everywhere else. Migration questions:

- **Claude Sonnet vs Opus** for the strategy generation step. Opus likely warranted — this is multi-input synthesis with real reasoning, not extraction.
- Prompt-caching the pillar framework + scoring rubric (those don't change weekly) for cost savings on every run.
- Output schema validation via Anthropic's tool use as structured output, instead of JSON-mode-and-pray.
- Side-by-side eval: run the same week's data through GPT-4o and Claude, blind-compare strategy quality before flipping the switch.

### Automate data ingestion

Currently the Supabase performance table is populated manually or semi-automated. Productization blocker — clients won't manually export performance data weekly.

Options:

| Source | Approach |
|---|---|
| **Instagram** | Meta Graph API (Business accounts only). Rate limits + permission complexity. |
| **TikTok** | TikTok Display API + Business API. Limited metric exposure on Display API. |
| **Twitter/X** | API v2. Cost concerns post-2023 pricing. |
| **LinkedIn** | Marketing Developer Platform. Approval gate. |
| **All of the above via aggregator** | Phyllo, Insense, or similar — pay for the integration layer instead of building it. Cost-of-build vs cost-of-aggregator tradeoff. |

Lean for v1 productization: aggregator (Phyllo or similar) for IG + TikTok, native APIs for LinkedIn + Twitter where the aggregator coverage is weaker.

### Direct posting (v2, not v1)

Engine outputs strategy + drafts → human approves → engine posts. Adds:

- Approval UI (Sanity? custom Optimus admin?)
- Same platform APIs as ingestion, write-side
- Image/video asset pipeline (likely fal.ai for stills, TBD for short-form video)

V2 problem. V1 ships strategy-only.

### Per-client pillar configuration

Already discussed in [[concept-notes]]. Tech-side:

- Pillar definitions move from hardcoded n8n node into Supabase table keyed by client
- Onboarding flow needs a pillar-design step (template library + custom)
- Strategy prompt becomes parameterized — read pillar definitions at run time

### Hosting

n8n is fine for now. Re-evaluate if:
- We hit n8n's per-execution timeout limits with longer Claude reasoning
- We want to colocate this with the per-client Vercel deployments
- We need finer-grained CI/CD for prompt iteration than n8n's UI provides

---

#offering/content-engine #status/active
