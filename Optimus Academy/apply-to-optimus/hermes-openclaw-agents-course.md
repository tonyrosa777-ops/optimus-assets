---
title: Hermes + OpenClaw Agents Course — apply-to-Optimus bridges
schema-version: 1
concept: [[../concepts/hermes-openclaw-agents-course]]
source-references: ["[[../daily/2026-05-06#21:18 — \"FREE Hermes + OpenClaw AI Agents Course: Build & Automate ANYTHING\" by Julian Goldie SEO]]"]
created: 2026-05-06
last-updated: 2026-05-06 21:18
tags: [#learning/applied, #applies-to/tools/hermes, #applies-to/tools/openclaw, #applies-to/ai-agents, #status/active]
---

# Hermes + OpenClaw Agents Course — apply-to-Optimus bridges

> **Concept:** [[../concepts/hermes-openclaw-agents-course]]
> **Source(s):**
> - [[../daily/2026-05-06#21:18 — "FREE Hermes + OpenClaw AI Agents Course: Build & Automate ANYTHING" by Julian Goldie SEO]] — Julian Goldie SEO
>
> **Last updated:** 2026-05-06 21:18

---

## Applied to tools-tracking — Hermes

applies-to:: [[../tools-tracking/hermes]]
status:: not-started
value-vector:: productivity
expected-impact:: medium
created:: 2026-05-06
last-updated:: 2026-05-06 21:18

> **Applies to:** [[../tools-tracking/hermes]]
> **Status:** `not-started`
> **Value vector(s):** productivity
> **Expected impact:** medium
> **Last updated:** 2026-05-06 21:18

### What I learned

Hermes (Noose Research, MIT-licensed, launched February 2026) is a self-improving agent runtime where the agent generates its own reusable skills during work, persists them as `skill.md` folders on disk, and shares them via the agentskills.io open standard. Multi-platform v0.9 surface covers 16 messaging channels including Telegram, Discord, Slack, WhatsApp, Signal, email, iMessage (BlueBubbles relay), Matrix, Mattermost, plus native Android via Termux. Single-curl install on Linux/macOS/WSL2, runs on a $5 VPS or Docker or Modal or Daytona. Concept note: [[../concepts/hermes-openclaw-agents-course]]. Hermes is now a serious peer to OpenClaw on the multi-agent runtime evaluation track and deserves its own tools-tracking entry rather than living buried inside concept prose.

### Why it applies to tools-tracking — Hermes

Hermes is a peer to OpenClaw on Optimus's evaluation track, and OpenClaw already has a tools-tracking entry. Without a Hermes entry of its own, the next time Hermes surfaces (and per Julian's report, Noose Research releases roughly weekly — so it WILL surface) the same "what does an entry actually look like for Hermes?" question repeats and the convention only compounds when both peers are tracked. The folder structure expects one flat file per tool; leaving one of two peers untracked is a process gap, not a deliberate choice.

### How to apply it

1. Create `Optimus Academy/tools-tracking/hermes.md` (this run) with status `evaluating`, the standard 7-criterion adoption-decision checklist, and an opening decision-log entry citing Julian's 5-hour course as the first data point.
2. Add Hermes to the periodic tools-tracking review whenever a formal cadence is established.
3. When a future source surfaces Hermes again, append to the existing entry rather than creating duplicates. Deterministic slug rule keeps this safe.
4. Promote `evaluating` → `adopted` ONLY after the 7-criterion checklist clears via spike-test, not by reading more reviews.

### Value vector reasoning

- `productivity`: tools-tracking exists to compress "should we adopt this?" decisions from ad-hoc rumination to a structured 7-criteria check. Establishing the entry now eliminates the "do we have a Hermes entry?" lookup cost on every future capture, plus structures the Tier-3 spike-test decision against the established checklist before the next surface adds noise. Recurring small gain across every future Hermes capture and every future agent-runtime decision.

### Status

`not-started`

### Updates

(none)

---

## Applied to tools-tracking — OpenClaw

applies-to:: [[../tools-tracking/openclaw]]
status:: not-started
value-vector:: overhead
expected-impact:: small
created:: 2026-05-06
last-updated:: 2026-05-06 21:18

> **Applies to:** [[../tools-tracking/openclaw]]
> **Status:** `not-started`
> **Value vector(s):** overhead
> **Expected impact:** small
> **Last updated:** 2026-05-06 21:18

### What I learned

Julian's late-April-2026 hands-on review reverses the May 3 narrative on OpenClaw's day-to-day operator experience. Configuration validation is breaking; reliability is declining; Telegram broke three times in a single week; gateway-token-refresh flow is "super messy and annoying"; updates frequently leave the install in a broken state requiring two hours of debugging. By chapter 29 Julian declares "I'm over OpenClaw." BUT this is empirical-experience data, not architecture data. Both framings — Nate B. Jones's production-grade architecture (April 2026, hierarchical multi-agent topology, Docker-per-agent, RPC inter-agent comms, channel-native behavior) and Julian's degraded operator experience — can coexist; they describe different layers of the same system. Concept: [[../concepts/hermes-openclaw-agents-course]].

### Why it applies to tools-tracking — OpenClaw

The existing OpenClaw entry's Decision log was a single-source 2026-05-03 snapshot built on Nate B. Jones's framing alone. A serious second-source data point (Julian's 5-hour hands-on course with daily-use specifics) deserves a Decision log entry, not silence — especially because it shifts the URGENCY of OpenClaw evaluation downward without invalidating the architectural maturity claim. Future readers of `openclaw.md` need to see both data points to make an informed call; absent the Julian entry they will assume the May 3 positive framing is current.

### How to apply it

1. Append a new Decision log entry dated 2026-05-06 to `Optimus Academy/tools-tracking/openclaw.md` (this run) summarizing Julian's empirical reliability complaints and explicitly noting the architecture-vs-experience layering so the entry is read correctly.
2. Update the file's `last-updated` field to 2026-05-06.
3. Do NOT change `status` from `evaluating` — the architecture-vs-experience layering means the spike-test option stays open. The verdict is "more data, not less — both views remain on the record."
4. Cross-link the new entry to this bridge file and to the [[../tools-tracking/hermes]] entry so the peer comparison is one click away.

### Value vector reasoning

- `overhead`: keeps the OpenClaw evaluation track honest. The cost of NOT logging this is the next reader assuming the positive May 3 framing is current; that misalignment becomes a real cost when a build decision is made on stale data. Recurring small gain — one log entry now prevents one wrong decision later.

### Status

`not-started`

### Updates

(none)

---

## Applied to AI Agents — shared knowledge (memory architecture lesson)

applies-to:: [[../../Offerings/02 AI Agents/shared-knowledge/agent-infrastructure]]
status:: not-started
value-vector:: productivity, revenue
expected-impact:: medium
created:: 2026-05-06
last-updated:: 2026-05-06 21:18

> **Applies to:** [[../../Offerings/02 AI Agents/shared-knowledge/agent-infrastructure]]
> **Status:** `not-started`
> **Value vector(s):** productivity, revenue
> **Expected impact:** medium
> **Last updated:** 2026-05-06 21:18

### What I learned

Hermes ships a multi-layer memory architecture worth studying as a reference for Optimus's canonical memory primitive. Five distinct layers, each with its own invariant: a pluggable in-runtime memory engine (six-to-seven backends, Honcho and Mem-Zero named, swappable via `Hermes memory setup`); Obsidian-backed long-term storage where the operator maintains markdown notes the agent ingests directly with folder-level scope; OMI for auto-capture (continuous wearable input — screen and microphone — feeding generated memory artifacts into Obsidian); the LLM-wiki pattern from Andre Karpathy (April 4, 2026) layered as raw sources / wiki / schema with three operations — ingest, query, lint — co-evolved by user + agent; and OB1 (Open Brain) as the OpenClaw-side cross-tool memory companion. Each layer has a distinct invariant: durability vs ergonomic capture vs cross-tool portability. Concept: [[../concepts/hermes-openclaw-agents-course]].

### Why it applies to AI Agents — shared knowledge

Optimus's canonical agent-infrastructure document defines four primitives, including a memory store. The current memory store is described in terms of Pydantic + Supabase + pgvector — a single-layer architecture optimized for queryable typed records. Hermes's multi-layer pattern is more ambitious, and at least the "auto-capture upstream layer" idea (OMI feeding Obsidian, or analogously a wearable / screen-recorder feeding the agent's persistent context) is novel enough to consider for the canonical document — especially for Tier-4 Autonomous Employees where the agent is replacing a knowledge worker and persistent operator-context is the difference between "useful" and "indispensable." The LLM-wiki pattern is also a candidate scaffold for how Tier-4 agents persist learned-from-work knowledge between sessions without re-paying the discovery cost each time.

### How to apply it

1. Read [[../../Offerings/02 AI Agents/shared-knowledge/agent-infrastructure]] (existing canonical doc) end-to-end before any edit. The memory-store primitive's current spec is the baseline.
2. Note in its memory-store section the alternative multi-layer approach surfaced by this concept — pluggable in-runtime memory + long-term backing store + auto-capture upstream layer + LLM-wiki scaffolded knowledge base. Frame it as an option to evaluate, not an adoption.
3. Spike-test whether multi-layer memory provides material lift on a representative Optimus Tier-3 workflow before adopting it as canonical. Measure: persistence quality across sessions, operator-context retention, ops cost of running the extra layers, integration friction with the existing four primitives (memory, tools, observability, approval).
4. If the spike-test shows real lift, update `agent-infrastructure.md`'s memory-store section to describe both single-layer (current default) and multi-layer (Hermes-inspired) options with explicit selection criteria — Tier-3 might stay single-layer while Tier-4 adopts multi-layer, or per-client-segment selection might be the right cut.
5. Per the LEDGER rule, no auto-edits to `agent-infrastructure.md` from this bridge. The bridge is a change-request; Anthony reviews the spike-test results and applies any canonical change manually in a deliberate commit.

### Value vector reasoning

- `productivity`: clearer memory architecture options reduce design overhead on every Tier-3 and Tier-4 build. Today every build re-derives "what memory pattern fits this client?" from first principles; an enriched canonical doc with two named patterns and selection criteria compresses that decision.
- `revenue`: better operator-context persistence is plausibly worth premium pricing on Tier-4 Autonomous Employee deployments where the agent is replacing a knowledge worker. An agent that remembers the operator's preferences, prior decisions, and ongoing project state across sessions is a fundamentally different product from one that re-asks every Monday — and pricing reflects that gap.

### Status

`not-started`

### Updates

(none)
