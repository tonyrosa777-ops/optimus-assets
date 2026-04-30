---
name: AI Engineer Roadmap (Anthony Rosa)
description: Year-by-year Python + AI engineering progression, framed as the path to the Tier-4 Autonomous AI Employee product. Aligned to the runway-to-30 window (1,219 days from 2026-04-29 → 2029-08-30).
type: founder-vision
schema-version: 1
last-updated: 2026-04-29
review-by: 2026-10-29
tags: [layer/optimus-os, status/active]
---

# AI Engineer Roadmap

> The technical-skill progression that makes Tier-4 (Autonomous AI Employees) shippable by Year 3 and earns the right to operate at the infrastructure layer Greg Osuri occupies. Aligned to the four-tier upsell ladder in [`north-star.md`](north-star.md).

This is engineering-skill progression. Deployment-infrastructure detail (decentralized GPU compute, GPU sizing, harness selection) lives elsewhere — in [`north-star.md`](north-star.md) for strategic framing, in `Offerings/02 AI Agents/02 Voice Receptionist/personaplex-architecture.md` for voice deployment, and in `Offerings/02 AI Agents/04 Autonomous Employee/python-architecture.md` for Tier-4 deployment.

---

## Year 1 (Age 26 → 27) — Foundation

### Core skills to acquire

**Python — production-grade, not tutorial-level**
- Data structures, OOP, async programming
- File I/O, API clients, error handling
- Type hints throughout — `from __future__ import annotations`, `TypedDict`, `Protocol`

**Anthropic SDK directly (no LangChain wrapper for the basic path)**
- Messages API, streaming, tool use, vision
- System prompts, structured outputs via tool use
- Prompt caching as the default — measure cache hit rate on every system

**Pydantic v2**
- Schema definition, validation, nested models
- `BaseModel` with discriminated unions for tool inputs/outputs
- Using Pydantic with the Anthropic tool-use schema for structured agent outputs
- Pydantic-typed memory schemas (matches the four agent-infrastructure primitives)

**FastAPI**
- Building API endpoints for AI agents (every Optimus backend is FastAPI)
- Request/response models with Pydantic
- Async endpoints, error handling, middleware
- Streaming responses (SSE for Chat Assistant)
- WebSocket endpoints (Voice Receptionist Twilio Media Streams)
- Auto-generated `/docs` (Swagger UI) — this becomes the FastAPI auto-docs requirement in `portfolio-standards.md`

**LangChain (selectively — for agent loops, not the basics)**
- Chains, agents, tools — but not as the foundation. Anthropic SDK is the foundation; LangChain is when agent orchestration becomes complex enough that a graph framework helps.
- Memory types: buffer, summary, vector
- Tool calling and function definitions

**ChromaDB**
- Embedding documents
- Semantic search
- Persistent collections — for early dogfood agent memory before the Supabase + pgvector pattern is wired

**SQLite + supabase-py**
- SQLite for local agent state in dev
- supabase-py for production Postgres + pgvector
- Storing agent outputs and conversation history per the agent-infrastructure memory primitive

**Twilio Media Streams + audio pipeline**
- Programmable Voice + Media Streams WebSocket binary audio
- mulaw ↔ PCM conversion
- 8 kHz ↔ 24 kHz resampling
- Opus encoding/decoding
- Barge-in handling
- This is the bridge between Twilio and Personaplex

**Personaplex 7B (NVIDIA full-duplex S2S model)**
- Docker self-host on local GPU (24 GB VRAM minimum)
- WebSocket / REST integration patterns
- Tool-call orchestration via the FastAPI tier (Personaplex native tool-calling not yet shipped — the Inner Monologue text-channel pattern)
- Voice cloning via short audio sample for per-client persona

### Year 1 portfolio targets

- **3–5 client AI systems on public GitHub.** Each follows `portfolio-standards.md`.
- **DJ Custom Clothing logo pipeline** complete, documented, deployed. Sets the engineering-hygiene reference.
- **Johnny Ead CPA QuickBooks automation** complete, documented, deployed.
- **First FastAPI endpoint live** and accessible (chat backend or marketing team `/run-weekly`).
- **Personaplex + Twilio bridge running on internal calls** — own number, own GPU, own observability.
- **Marketing Team Tier-3 shipped to first paying client.** Sets the agent-architecture reference (the prerequisite template every Tier-4 build inherits).
- **GitHub profile** with real commit history, no empty repos, no tutorial clones.

### Year 1 revenue + reinvestment target

- **$20,000 MRR by 2027-Q1.** That triggers the 20% reinvestment loop documented in `north-star.md` § 7.

---

## Year 2 (Age 27 → 28) — Depth

### Skills to acquire

**LangGraph — stateful multi-agent workflows**
- Graph-based agent orchestration where the four primitives (memory · tools · observability · approval) are the nodes.
- Per-client agent runtimes for Tier-4.

**RAG systems — full retrieval-augmented generation pipelines**
- pgvector at depth (Supabase already in stack)
- Pinecone, Weaviate as alternatives when scale demands
- Hybrid retrieval (lexical + semantic)
- Reranking

**Fine-tuning — LoRA and QLoRA on open-source models**
- Llama, Mistral, Qwen, Hermes (Nous Research function-calling fine-tunes) as candidates
- Per-client custom-trained variants for Tier-4
- Eval-driven training — never ship a fine-tune that doesn't beat baseline on a held-out set

**Voice pipelines at depth**
- Whisper + ElevenLabs as supplements to Personaplex
- Custom orchestration when platform constraints bite

**Cloud infrastructure**
- AWS or GCP, not just Vercel
- EC2 / Cloud Run for Python services
- S3 / GCS for file storage
- RDS / managed Postgres
- Secrets management (Parameter Store, Secret Manager)

**Docker — containerize every system**
- Multi-stage builds
- Reproducible base images
- Production hardening (non-root user, healthchecks, resource limits)

**Vector databases at depth — Pinecone, Weaviate**

**Open-source models locally — running Llama, Mistral via Ollama**

### Year 2 portfolio targets

- **2–3 multi-agent systems on GitHub** (LangGraph-based).
- **First cloud-deployed Python AI service** (not just Vercel).
- **Contributions to at least one open-source AI project.**
- **Drink-Own-Champagne milestone shipped (2027-Q3)** — Optimus's marketing pipeline + inbound qualification + scheduling runs autonomously without daily attention. The first true Tier-4 dogfood instance, running against Optimus's own operations.

---

## Year 3 (Age 28 → 29) — Specialization

### Strategic choices

Pick **one** specialization and go deep:
- **Autonomous agents** — long-running, tool-using, action-taking. Tier-4 is in this lane by default.
- **Voice AI** — Personaplex tuning, custom voice models, real-time pipelines, low-latency telephony.
- **AI infrastructure** — model serving, orchestration runtimes, decentralized compute (Greg Osuri's lane).

### Skills to acquire

- **Decentralized compute** — private GPU compute marketplace at depth. Understanding the infrastructure stack Greg Osuri built (per [`north-star.md`](north-star.md) § My Idol). Deploying production AI workloads on decentralized GPU markets.
- **Meaningful open-source contribution** — not a typo PR. A feature, a fix, a benchmark, a documented pattern that a project actually merges and references.
- **Building something people use without being paid to build it** — a tool, a benchmark, a reference implementation. Optional: open-source the Tier-4 reference architecture (sanitized of client-specific details).
- **Network inside the real AI engineering community** — speak, write, or publish on a technical topic at least once.

### Year 3 portfolio targets

- **First Tier-4 Autonomous AI Employee shipped to a paying client.** Public reference architecture (sanitized), private client repo with the working system. The artifact that proves "Optimus does autonomous AI employees."
- **GitHub profile** that earns Greg's attention if he ever scrolls through it.

---

## Anti-targets (what NOT to chase)

- **Generic LLM tutorials.** Skip the "build your first chatbot" content. Build real systems for real clients instead.
- **Multi-tenant SaaS for AI workflows.** Optimus is custom-per-client. The moat is private deployment, not a horizontal product.
- **Frontiers I won't ship from.** Reading research papers is fine; chasing every new technique without shipping is procrastination dressed as learning.
- **Tools that don't compound the four primitives.** If a new framework doesn't strengthen memory · tools · observability · approval, it's a distraction this cycle.

---

## How to use this roadmap

- **Quarterly review:** read this file, score progress against each year's targets, update `last-updated` and `review-by`.
- **When choosing what to learn next** — does it advance Year N? If not, defer.
- **When building a client system** — does it produce a portfolio artifact that meets `portfolio-standards.md`? If not, fix the build process before shipping.

The roadmap is not aspirational. It is the path. If a year ends and the targets don't ship, the journal at `journal/` documents why and the roadmap recovers in the next quarter — not in three years.
