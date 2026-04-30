---
schema-version: 1
last-updated: 2026-04-29
review-by: 2026-10-29
tags: [offering/all, layer/optimus-os, status/active]
---

# Agent Infrastructure — The Four Primitives

The compounding artifact. Defined once here, used by every Optimus agent (Marketing Team · Voice Receptionist · Tier-4 Autonomous AI Employee). Without these primitives, the upsell tiers become three discrete codebases. With them, the lower three tiers compound naturally into Tier-4 — Tier-4 IS these primitives with an open-source harness on top.

This file is governed by [`../../../anthony-rosa/north-star.md`](../../../anthony-rosa/north-star.md). Cross-reference: [`tech-stack.md`](tech-stack.md) is the canonical Python stack; this file is the canonical agent shape on top of that stack.

---

## 1. Memory store

**Pydantic-typed memory schema in Supabase Postgres + pgvector.** Three layers:

- **Episodic** — events the agent observed or did, timestamped. "On 2026-04-29 14:32, the agent looked up contact `customer_id=42` in the CRM and found a closed-lost record from 2025."
- **Semantic** — facts learned about the client / business / domain, deduplicated. "The client's pricing is $X for tier Y. The client's hours are M–F 9–5. The client's primary KPI is bookings/week."
- **Procedural** — how-to knowledge for repeated tasks. "When a caller asks about pricing, route to the `/quote` tool with their stated job size, then read back the result with the disclaimer about 'final pricing on-site after assessment.'"

**Reference Pydantic shape** (illustrative — actual code is written at first build):

```python
from datetime import datetime
from typing import Literal, Optional
from pydantic import BaseModel, Field

class EpisodicMemory(BaseModel):
    agent_id: str
    client_id: str
    timestamp: datetime
    event_type: Literal["tool_call", "user_message", "agent_message", "approval_gate"]
    payload: dict  # the event-specific structured data
    embedding: Optional[list[float]] = None  # for semantic recall

class SemanticFact(BaseModel):
    agent_id: str
    client_id: str
    fact_key: str  # e.g. "pricing.tier_starter"
    fact_value: str
    source_episodes: list[str] = Field(default_factory=list)  # episode IDs this fact was learned from
    confidence: float  # 0.0–1.0
    last_validated: datetime

class ProceduralPattern(BaseModel):
    agent_id: str
    pattern_name: str  # e.g. "handle_pricing_inquiry"
    trigger_intent: str
    steps: list[dict]  # ordered tool-call template
    success_count: int = 0
    failure_count: int = 0
```

Each memory type lives in its own Supabase table. Episodic + semantic carry pgvector embeddings for retrieval. Procedural is queried by `pattern_name` lookup.

**Used by:**
- Marketing Team — week-over-week strategy continuity (semantic facts about pillar performance · episodic record of every weekly run · procedural patterns for "how to interpret a saturation signal")
- Voice Receptionist — caller history (episodic per call · semantic facts about returning callers · procedural patterns for the qualifying script)
- Tier-4 Autonomous Employee — everything. Memory is the difference between "agent that responds to triggers" and "agent that operates over time."

---

## 2. Tool registry

**Pydantic-typed tool definitions with permissions.** Every tool an agent can call is declared in the registry with:

- The tool's input schema (Pydantic)
- The tool's output schema (Pydantic)
- **Permission tier:** `read-only` vs `action-taking`
- **Per-client allowlist:** which clients have this tool enabled (default: empty — explicit allowlist required)
- **Rate limit:** per-tool, per-client (e.g. `send_email: 5/hour/client`)
- **Approval-required flag:** if true, the action goes through the approval primitive (§ 4) before execution

**Reference Pydantic shape:**

```python
from typing import Literal, Optional
from pydantic import BaseModel

class ToolDefinition(BaseModel):
    name: str  # e.g. "send_followup_sms"
    description: str  # for the LLM's tool-use prompt
    input_schema: dict  # JSON-schema-style, generated from a Pydantic model
    output_schema: dict
    permission_tier: Literal["read-only", "action-taking"]
    requires_approval: bool
    rate_limit_per_client_per_hour: Optional[int]
    allowed_client_ids: list[str]  # explicit allowlist — never wildcard

class ToolCall(BaseModel):
    tool_name: str
    client_id: str
    inputs: dict  # validated against the tool's input_schema
    invoked_by: str  # agent ID
    invoked_at: datetime

class ToolResult(BaseModel):
    tool_call_id: str
    success: bool
    outputs: Optional[dict] = None
    error: Optional[str] = None
    latency_ms: int
```

Tools are not free-form strings the LLM picks. They are typed, permissioned, audited. An agent attempting to call a tool not on its client's allowlist gets a hard rejection at the FastAPI orchestration layer — the LLM never sees the tool as an option.

**Used by:** every agent that calls tools (Marketing Team's Supabase reads/writes · Voice Receptionist's CRM/calendar/SMS · Tier-4's full action surface).

---

## 3. Observability layer

**Every agent action logged to Supabase** with: `agent_name` · `tool_called` · `inputs` · `outputs` · `latency_ms` · `success/failure` · `reasoning_trace` (the agent's chain-of-thought or tool-use rationale, when available).

**Default trace UI: Langfuse.** Cloud-hosted by default; self-hosted via Docker if a client demands it. Per-trace cost is low at the volumes Optimus will operate at; the value of "what did the agent do today, why" is high.

**Fallback: direct Supabase logging** with a custom dashboard. Use this when:
- Langfuse cost gets wrong for a particular client volume (rare under Optimus's scale targets)
- A client has a strict no-third-party-data policy (Tier-4 enterprise clients)
- Local dev / first-build before Langfuse is set up

**Reference Pydantic shape:**

```python
class ObservabilityEvent(BaseModel):
    agent_id: str
    client_id: str
    timestamp: datetime
    event_type: Literal["tool_call", "llm_call", "approval_request", "approval_granted", "approval_denied", "error"]
    duration_ms: int
    inputs: dict
    outputs: Optional[dict]
    metadata: dict  # cache hit rate, token counts, model used, etc.
```

**Mandatory metrics every agent emits:**
- Cache hit rate per LLM call (per `tech-stack.md` § Prompt caching)
- Token counts per call (input cached · input non-cached · output)
- Tool call success rate per tool per day
- Approval-gate trigger rate (how often is this agent asking for approval?)

The "what did the agent do today" surface is the difference between "agent in production" and "agent we trust in production." A Tier-4 client paying $2,500-5,000/mo expects to see this surface. Building it as a primitive means every product gets it for free.

---

## 4. Approval / sandboxing layer

**Pre-action gates for high-stakes operations.** Defaults:

- **First 30 days of any deployment:** all `action-taking` tools (per the tool registry permission tier) require human approval. The agent surfaces an `ApprovalRequest`; a human reviews; the agent proceeds or gets denied. This is the human-in-the-loop period.
- **Days 31–60:** read-only-tier autonomy. Action-taking tools still require approval. The agent has demonstrated correctness on observation tasks.
- **Days 61–90:** graduated autonomy on individual tools based on observed correctness. A tool with ≥98% approval-granted rate over the prior 30 days can be promoted to autonomous. The promotion is a deliberate flip in the tool registry by a human.
- **Day 91+:** full autonomy on graduated tools. Non-graduated tools stay approval-gated indefinitely.

**Reference state machine:**

```python
from typing import Literal
from datetime import datetime

class ApprovalRequest(BaseModel):
    request_id: str
    agent_id: str
    client_id: str
    tool_call: ToolCall  # the proposed action
    rationale: str  # the agent's reason for proposing this action
    requested_at: datetime
    deadline: Optional[datetime]  # for time-sensitive actions

class ApprovalDecision(BaseModel):
    request_id: str
    decision: Literal["approve", "deny", "modify"]
    decided_by: str  # human user ID, or "auto" if a tool is fully graduated
    decided_at: datetime
    modification: Optional[dict] = None  # if modify: the adjusted tool inputs
    rationale: Optional[str] = None  # why this decision

class ToolPromotion(BaseModel):
    tool_name: str
    client_id: str
    promoted_at: datetime
    promoted_by: str
    prior_approval_rate: float  # the metric that justified promotion
    sample_size: int
```

**High-stakes actions that always stay approval-gated** regardless of graduation:
- Sending external emails to non-self addresses
- Moving CRM records to closed-won / closed-lost
- Posting publicly to social
- Charging cards or invoking payment APIs
- Deleting data
- Anything irreversible

**Used by:** Tier-4 Autonomous Employee primarily (its whole product story is "human-in-the-loop graduating to autonomy"). Marketing Team uses approval for direct-posting tools (when v2 ships). Voice Receptionist uses approval less centrally because most of its tool calls happen during a live call where the human caller is the implicit approver.

---

## How the four primitives compound into Tier-4

Tier-4 Autonomous AI Employee = the four primitives + an open-source agent harness (OpenClaw / Hermes / Letta / Pydantic AI / LangGraph — selection in [`../04 Autonomous Employee/harness-research.md`](../04%20Autonomous%20Employee/harness-research.md)).

The harness adds:
- A reasoning loop on top of the memory store
- Multi-step plan generation
- Cross-tool sequencing
- Long-running task management

But the bottom layer — what gets remembered, what tools can be called, what gets logged, when humans intervene — is the same shape every Optimus agent uses. That's why a client who has Marketing Team for 6 months can upgrade to Tier-4 without throwing away anything: the same memory store extends, the same tool registry expands, the same observability dashboard adds new agent IDs, the same approval workflow extends to new actions.

This compounding is the entire reason these four primitives exist as a shared spec instead of being re-invented per product.

---

## Status

Reference spec. Implementation begins when the first agent product is built in Python — likely Marketing Team (Tier-3) as the first true scheduled agent. The Pydantic shapes here become the actual schemas in that build's `/python/optimus_marketing_team/memory.py`, `/tools.py`, `/observability.py`, `/approval.py` modules.

#offering/all #layer/optimus-os #status/active
