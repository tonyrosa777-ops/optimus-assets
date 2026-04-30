---
schema-version: 1
last-updated: 2026-04-29
review-by: 2026-07-29
tags: [offering/autonomous-employee, status/in-development]
---

# Harness Research — Tier-4 Autonomous AI Employee

The open-source agent harness sits on top of the four agent-infrastructure primitives ([`../shared-knowledge/agent-infrastructure.md`](../shared-knowledge/agent-infrastructure.md)) and provides:
- A reasoning loop on top of the memory store
- Multi-step plan generation
- Cross-tool sequencing
- Long-running task management

The bottom layer (memory · tools · observability · approval) is identical across every Tier-4 build. The harness is the layer that varies — selected per client based on the eval criteria below.

This file is the **comparison + first-build selection log.** Populated when the dogfood instance kicks off (planned 2027-H1), then iterated as paying Tier-4 clients land.

---

## Candidates to evaluate

### OpenClaw
- **What it is:** TBD — Anthony is tracking this; characteristics to confirm at evaluation time. (Possibly `NemoClaw`-adjacent given prior tools-tracking notes.)
- **Initial impression:** Anthropic is tracking it; worth a thorough first look.

### Hermes (Nous Research)
- **What it is:** Family of function-calling fine-tunes on Llama-class base models. Strong reputation for tool-use reliability on open weights.
- **License:** Apache-class on the fine-tunes; underlying base license varies.
- **Strengths:** Production-grade tool-calling on open-weight models. Self-host friendly.
- **Concerns:** Not a full agent harness on its own — provides the model layer, not the orchestration layer. Pairs naturally with Pydantic AI or LangGraph for the graph.

### Letta (formerly MemGPT)
- **What it is:** Long-term memory architecture, agent-native. Built specifically around the memory primitive.
- **Strengths:** Memory model aligns with our episodic/semantic/procedural shape. Could be the cleanest fit for the memory primitive specifically.
- **Concerns:** Smaller community than LangChain/LangGraph. Lock-in risk if the project's memory model diverges from our schema.

### Pydantic AI
- **What it is:** Agent framework from the Pydantic team. **Pydantic-native by design.**
- **Strengths:** Direct alignment with the entire Optimus stack — every schema is already Pydantic, every tool definition is already Pydantic. Lowest friction integration. Active development by the Pydantic core team.
- **Concerns:** Newer than LangChain/LangGraph. Multi-agent orchestration is less mature.

### LangGraph
- **What it is:** Graph-based multi-agent orchestration on top of LangChain. Stateful, durable, checkpointable workflows.
- **Strengths:** Production-proven at scale. Strong multi-agent patterns. Integrates with the four primitives via custom nodes.
- **Concerns:** LangChain dependency surface is heavy. We selectively use LangChain Python on the backend per `tech-stack.md`, but LangGraph pulls in more.

### CrewAI / AutoGen
- **What they are:** Multi-agent role coordination frameworks (CrewAI: persona-based; AutoGen: Microsoft research).
- **Strengths:** Strong for "team of specialized agents" patterns.
- **Concerns:** Less aligned with our "one custom-trained employee per client" framing. Possibly relevant when a Tier-4 client needs a sub-team of agents inside a single employee deployment.

---

## Evaluation criteria

Each candidate scored against these criteria when evaluation runs:

| Criterion | Why it matters |
|---|---|
| **Memory primitives compatibility** | Does the harness use a memory model compatible with our Pydantic-typed episodic/semantic/procedural shape? Or does it impose its own that we'd have to translate to/from? |
| **Tool registry compatibility** | Does the harness consume Pydantic-typed tool definitions with permissions, allowlists, rate-limits? Or does it want free-form function signatures? |
| **Observability hooks** | Does the harness expose the agent's reasoning trace, tool-call inputs/outputs, latency per step — in a form Langfuse can ingest? |
| **Approval/sandboxing support** | Does the harness support pre-action gates? Or are we wrapping the entire harness in an approval shell? |
| **Self-host viability on the chosen GPU deployment target** | Per [`python-architecture.md`](python-architecture.md). Can it deploy in Docker on a single GPU per client, or does it require infrastructure we don't want to operate? |
| **License compatibility with private-deployment commercial use** | Apache-2 / MIT / BSD-3 are clean. AGPL is not viable for client-private deployments. |
| **Maintenance burden per-client** | Does each Tier-4 build inherit the harness cleanly, or does each client need bespoke harness work? |

---

## First-build selection (TBD)

When the dogfood instance kicks off (planned 2027-H1, ahead of the 2027-Q3 Drink-Own-Champagne milestone), this section gets populated with:
- The selected harness
- Score breakdown per criterion above
- Rationale for the selection
- The two runners-up and why they didn't win (so a re-eval has the prior context)
- The eval data: same task suite run against multiple candidates, rubric-graded outputs

The first-build selection is the reference choice for subsequent Tier-4 clients. Re-evaluation happens when a client has a constraint that the reference choice doesn't serve well, or when a candidate ships a major version that changes the score sheet meaningfully.

---

## Why this file exists now if the selection is later

Three reasons to write the comparison surface NOW even though the decision lands later:

1. **The eval criteria themselves matter** — they encode what Optimus values in a harness, which encodes our agent design philosophy. Writing them down now forces clarity on what "good" looks like before any vendor pitch can bias the choice.
2. **Each candidate's strengths/concerns** above are first-pass impressions that will get tested. Recording them now lets a future evaluation see what was true of these tools in 2026-Q2 vs. what changed by 2027-H1.
3. **The decision is deferred, not avoided.** This file is the artifact that makes "we'll pick the harness at first build" a real plan instead of a punt.

---

## Open questions

| Question | Status |
|---|---|
| **OpenClaw — what is it actually?** | Need a thorough first look from Anthony's tools-tracking; recheck quarterly until the project is characterized. |
| **Hermes 4 / next-gen function-calling fine-tunes** | New releases land regularly; recheck before the dogfood eval kicks off. |
| **Decentralized GPU lease pricing for harness deployment** | Pricing has been volatile as the decentralized compute marketplace matures. Confirm at eval time per `python-architecture.md` § Deployment options (Option 3). |
| **Multi-tenant vs. per-client deployment economics** | At what client count does running 50 separate per-client containers stop making cost sense? Calculation deferred to scale. |

---

## Status

**Scoped, populated with first-pass impressions. First-build selection happens at dogfood instance kickoff (2027-H1).**

#offering/autonomous-employee #status/in-development
