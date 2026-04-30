---
name: Anthony Rosa — North Star
description: Founder vision document. The why, the what, the where-to. Read upstream of every architectural decision on Optimus AI systems and upsells.
type: founder-vision
schema-version: 1
last-updated: 2026-04-29
review-by: 2026-10-29
tags: [layer/optimus-os, status/active]
---

# Anthony Rosa — North Star

> The founder layer for Optimus Business Solutions. This document is read upstream of every Optimus AI/upsell architectural decision (referenced from `CLAUDE.md` under `## Founder Vision`). Static — updated deliberately. The journal at `journal/` feeds back here on weekly review.

---

## 1. Who I Am

Anthony Rosa. 26 years old. Founder of Optimus Business Solutions, based in Salem, New Hampshire. Living with my grandmother — she gave me the time and space to build something real, and that's the only reason this window exists.

Today is **2026-04-29**. I turn 30 on **2029-08-30**. **1,219 days.** That is the runway. It is the most important period of my life. I will not waste it.

By 30: real AI engineer, real portfolio, real clients, real systems in production, the ability to live anywhere doing work that matters. Only acceptable outcome.

---

## 2. What I've Proven

Between **February 22 and April 29, 2025** — 67 days — I generated **$32,000 in revenue** building custom Next.js websites for local service businesses. Paid off debt. Invested in AKT (Akash Network). $12,000 in savings. Minimal expenses.

The revenue model works. The website pipeline works. The question now is what compounds on top of it — and whether I can become an AI engineer worth Greg Osuri's respect by 30.

---

## 3. The Business — Optimus Business Solutions

Optimus builds high-performance, intelligence-driven websites for local service businesses — trades, coaches, consultants, hospitality — using a proprietary three-phase pipeline:

| Phase | What happens |
|---|---|
| **Phase 0** — Intake + market research | `initial-business-data.md` + `market-intelligence.md` written before a single line of code. Every design decision traces back to research. |
| **Phase 1** — Agent sweep | Parallel Claude Code agents build the entire site — design synthesizer, content writer, animation specialist, frontend, blog, shop, quiz, booking, testimonials, retro, pre-launch audit. |
| **Phase 2** — Launch | DNS, Vercel, Resend, client handoff. Then `/retro` extracts the durable findings into `knowledge/`. |

**Website stack:** Next.js (App Router) · Tailwind CSS 4 · Framer Motion · Three.js · Sanity CMS · Resend · Stripe · Printful · Vercel · GoDaddy · fal.ai. Every hero ships with three layers: HeroParticles + brand-specific canvas + Framer Motion staggered text.

The website is the entry point. **The AI systems are the career.**

---

## 4. The Four-Tier Upsell Ladder

Every upsell is built once, correctly, in Python from day one. Greenfield. No phasing, no migration, no V1/V2.

| Tier | Product | Setup | MRR | What it teaches toward Tier-4 |
|---|---|---|---|---|
| **1** | Chat Assistant | $1,500 | $597 | System-prompt design · streaming · prompt caching · intent detection |
| **2** | Voice Receptionist | $2,500 | $797 | Real-time orchestration · tool calls under latency budget · state across turns |
| **3** | Marketing Team | $3,500 | $1,497 | Scheduled-cron agent loop · structured-output decisions · long-horizon state · *(template every Tier-4 build inherits)* |
| **4** | Autonomous AI Employee | $7,500–15,000 | $2,500–5,000+ | THE PRODUCT — custom-trained agent on open-source harness · per-client private GPU deployment · multi-tool action-taking · long-running observability |

**Total addressable MRR per fully-onboarded client: ~$5,400–7,900/mo.**

**The canonical Optimus stack — every upsell, every system, day one:**
- FastAPI
- anthropic SDK (Claude API direct)
- Pydantic v2
- supabase-py
- Twilio (SMS + voice telephony)
- Personaplex (voice model — full-duplex speech-to-speech)
- Tier-4 only adds: open-source agent harness (OpenClaw / Hermes / Letta / Pydantic AI / LangGraph — selection in `Offerings/02 AI Agents/04 Autonomous Employee/harness-research.md`) + Akash Network for private per-client GPU compute.

n8n is not in this stack in any capacity.

**Why this stack:** Real AI engineering skill compounds when you control the layers underneath. Every backend service in Python → real FastAPI / Pydantic / async expertise. Every agent on the four shared infrastructure primitives → composable agent-shaped components. Every system on a public GitHub repo with an architecture diagram → portfolio that survives any single client. By 30, the GitHub profile is the proof.

---

## 5. The End Goal

**Autonomous AI employees for SMB and mid-market.** Purpose-built agents that run continuously, take actions, and operate like a member of staff. Privately deployed per client — same custom-per-client model as Optimus's websites and workflows today.

Think OpenClaw or Hermes class — but Optimus builds and deploys them privately for each business that buys Tier 4.

**Akash Network is the infrastructure layer that makes this possible:**
- **Private GPU compute** for each client's agents — their data, their model, their compute. Not a multi-tenant SaaS.
- **No dependency** on OpenAI or Anthropic cloud rate limits, content policies, or pricing changes outside our control.
- **Decentralized, censorship-resistant, cost-effective at scale** as the agent fleet grows.
- **Direct alignment with Greg Osuri's thesis** — the infrastructure layer of AI, the same place I want to operate from by 30.

**Akash hosts:**
- Personaplex voice models (per client, private)
- Autonomous agent runtimes (long-running, always-on)
- Any open-source models needed for client-specific fine-tuning
- The entire private AI-employee stack, per business

**The 3-year destination.** The four-tier upsell ladder is the path:
- Chat Assistant teaches **agent design** — system prompts, streaming, intent detection.
- Voice Receptionist teaches **real-time AI orchestration** — tool calls under latency, state across turns, audio I/O.
- Content Engine teaches **multi-agent autonomous workflows** — scheduled cron loops, structured outputs over long horizons, long-running state.
- Tier-4 Autonomous AI Employees is what all three become at scale — custom-trained, custom-tooled, custom-deployed per client.

Tier 4 is not a vague future state. It is the productized destination, with a folder spec already written in `Offerings/02 AI Agents/04 Autonomous Employee/`. The path between here and there is a sequence of paying clients, not a research project.

---

## 6. The Drink-Own-Champagne Milestone

**By the end of 2027-Q3, Optimus's own operations run on its own autonomous AI employee.** Not "we use the tools we sell" hand-waving — concrete: marketing pipeline + inbound qualification + scheduling all running autonomously, without daily attention.

This is the strongest sales signal that exists. "We run our own company on this" beats every case study, every slide, every demo. By 2027-Q3, every Tier-4 prospect can see Optimus's own employee on Optimus's own marketing site, working in public.

Calendar deadline. Not "someday." If 2027-Q3 slips, the slip is documented in `wins.md` with a reason and a recovered date. No fuzzy timelines on the asset that anchors every Tier-4 sale.

---

## 7. The Reinvestment Loop

At **$20,000 MRR** (target: end of Year 1, 2027-Q1), **20% of net revenue** goes to dedicated R&D on the Tier-4 Autonomous AI Employee product:
- Compute for evals and dogfood instances
- Model evaluations across open-source candidates (Llama, Mistral, Qwen, Hermes fine-tunes)
- Harness fine-tuning experiments
- Akash Console / private GPU deployment iteration

Without this loop, Tier-4 stays "someday." With it, Tier-4 has a funded R&D path that compounds while client work pays the rent. The 80% that remains keeps the lights on, retains earnings, and builds the runway. The 20% buys the destination.

---

## 8. The Moat

By 2028, fifty other shops will be selling something they call "autonomous AI employees." What makes Optimus's version win?

1. **Per-client private deployment on Akash.** Their data, their model, their compute. No multi-tenant SaaS. No "we promise we won't train on your data" — you own the training, you own the GPU lease, you own the weights. This is a structural moat the SaaS shops can't match without rebuilding their infrastructure.
2. **Tightly integrated with Optimus's existing website + booking + CRM + content stack.** Plug-in for current clients, not a separate product to evaluate. The Marketing Team module pre-loaded into every Tier-4 build means every Optimus client sees the upsell as expansion, not a new vendor.
3. **Two-plus years of dogfood data nobody else has.** Optimus operates on its own AI employees from 2027-Q3 onward. By 2029, that's 24+ months of "the founder runs his company on this" proof — every other shop will be selling promises.
4. **Verticalized to SMB service businesses** (trades, hospitality, coaches, consultants), not horizontal enterprise SaaS. Optimus knows these businesses cold from the website work — the Tier-4 employee inherits that domain knowledge. Horizontal competitors will struggle to match it.

If a Tier-4 design decision doesn't reinforce one of these four moats, surface the tradeoff before committing.

---

## 9. Real Projects in Progress

### DJ Custom Clothing — logo pipeline (active build)

Python image processing pipeline: Vectorizer.ai + Pillow + OpenCV + Claude API vision. Logo analysis, color separation, JPEG → EPS conversion. Expanding into a full print shop vertical SaaS product over time.

**This is the engineering-hygiene reference, not the agent-architecture reference.** DJ pipeline sets:
- FastAPI service shape
- Pydantic schema discipline
- Public GitHub repo (`optimus-dj-logo-pipeline`)
- `/docs/architecture.png`
- `/docs/retro.md`
- `/docs/agent-shape.md` (marked N/A for non-agent sections)
- Conventional commits

The pattern transfers to every subsequent Optimus system. Every Tier-1/2/3/4 upsell inherits this structural discipline. **It does NOT transfer to agent architecture** — DJ is image processing, not an agent. The first true agent will be Marketing Team (Tier 3) — that one sets the agent-architecture pattern (cron loop · structured outputs · long-horizon state · the four agent-infrastructure primitives). Both patterns matter; the distinction is intentional.

### Johnny Ead CPA — QuickBooks automation (next)

Automated bookkeeping workflows for an expanding CPA practice. Python + QuickBooks API + Claude API for document processing. Real accounting automation, not a demo.

### Marketing Team (when shipped) — agent-architecture reference

Sets the shape every agent inherits: APScheduler cron · Pydantic-typed structured outputs · long-horizon state in Supabase via the four agent-infrastructure primitives (memory · tools · observability · approval). Drink-Own-Champagne instance runs through this product.

---

## 10. My Idol — Greg Osuri

Greg built **Akash Network** — decentralized compute infrastructure for the entire AI industry. I hold AKT. I study how he thinks. He operates at the **infrastructure layer** of AI, not the application layer. That is the long-term direction, and Akash is the bridge.

The path to that altitude:
- Ship real systems for real clients (the four-tier ladder).
- Build deep Python and AI engineering foundations (`ai-engineer-roadmap.md`).
- Understand how models, agents, memory, and compute actually work — not as abstractions but as code I've written and shipped.
- Contribute meaningfully to open source as the skills mature.
- Deploy Tier-4 on Akash from day one. Build a real-world case study of "this agent runs an SMB on decentralized GPU compute." That's an artifact Greg's ecosystem doesn't have yet.

By 30, the GitHub profile, the Tier-4 product, and the Akash deployment record together earn the conversation. That's the bar.

---

## 11. The Technical Roadmap

Year-by-year skill progression toward the Tier-4 Autonomous AI Employee product. See [`ai-engineer-roadmap.md`](ai-engineer-roadmap.md) for the full breakdown.

The short version:
- **Year 1 (26–27)** — Foundation: Python production-grade · anthropic SDK · Pydantic · FastAPI · LangChain · ChromaDB · Twilio Media Streams + audio pipeline · Personaplex Docker on local GPU.
- **Year 2 (27–28)** — Depth: LangGraph · RAG · LoRA/QLoRA · cloud infrastructure · Docker · vector DBs at depth · open-source models locally. **Drink-Own-Champagne ships.**
- **Year 3 (28–29)** — Specialization: pick a vertical (autonomous agents · voice AI · or AI infrastructure). Decentralized compute. Open source contribution. **First Tier-4 ships to a paying client.**

---

## 12. GitHub as a Portfolio

Every shipped Optimus system gets a public GitHub repo with the standard structure. See [`portfolio-standards.md`](portfolio-standards.md) for the full rules.

The DJ Custom Clothing logo pipeline is the engineering-hygiene reference implementation. Every subsequent repo matches its structure. **The Greg-Osuri test:** if you wouldn't show it to him, it's not done.

---

## 13. The Why

My grandmother gave me time. **Time is the only thing you cannot buy back.** I am using it to build skills that compound for 40 years, not income that disappears when I stop working.

Three years from now, the runway is over. The version of me that exists on 2029-08-30 will be one of two people: a solo developer who built websites for local businesses and made decent money, or a real AI engineer with a real portfolio, real clients, real systems running on decentralized infrastructure, and the standing to operate at the layer Greg operates at.

**Only the second outcome is acceptable.** Every architectural decision, every product choice, every hour of code written between now and then either compounds toward that destination or doesn't. This document is the test.
