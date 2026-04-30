---
name: GitHub Portfolio Standards (Optimus)
description: The structural discipline every Optimus system follows on GitHub. The DJ Custom Clothing logo pipeline is the engineering-hygiene reference; Marketing Team is the agent-architecture reference. The Greg-Osuri test gates the bar.
type: founder-vision
schema-version: 1
last-updated: 2026-04-29
review-by: 2026-10-29
tags: [layer/optimus-os, status/active]
---

# Portfolio Standards

> Every Optimus AI system shipped for a client gets a public GitHub repo with this exact structure. Non-negotiable. The portfolio is the proof — by 30, the GitHub profile is what earns Greg Osuri's respect or doesn't.

---

## 1. Repo naming convention

`optimus-[client-or-product]-[function]`

Examples:
- `optimus-dj-logo-pipeline` — DJ Custom Clothing image-processing pipeline
- `optimus-johnnead-quickbooks-automation` — Johnny Ead CPA bookkeeping automation
- `optimus-marketing-team` — Tier-3 Marketing Team reference implementation
- `optimus-voice-receptionist` — Tier-2 Voice Receptionist reference implementation
- `optimus-chat-assistant` — Tier-1 Chat Assistant reference implementation
- `optimus-employee-[client-slug]` — per-client Tier-4 Autonomous AI Employee builds (one repo per paying Tier-4 client)

Lowercase, hyphen-separated, no underscores.

---

## 2. Required README sections

Every repo's `README.md` has these sections, in this order:

1. **Business problem solved** — 2–3 sentences. What the client needed, what the system does.
2. **Technical architecture overview** — paragraph + reference to the embedded diagram.
3. **Stack and dependencies** — the canonical Optimus stack columns + any client-specific additions.
4. **Setup instructions** — `git clone` to running locally in under 10 commands.
5. **Example input/output** — for an API: a curl call + the response. For an agent: a real interaction trace.
6. **Architecture diagram** — embedded image from `/docs/architecture.png` (see § 3).

The README is what a stranger reads first. It must answer "what is this and should I care?" in under 90 seconds.

---

## 3. `/docs/architecture.png`

Every repo has an architecture diagram committed at `/docs/architecture.png`. Generated from a Mermaid block in `/docs/architecture.md` (so the source is editable + diffable).

The diagram MUST show:
- Data flow from input to output
- Every external service and API involved
- Where Claude / Personaplex / any LLM sits in the pipeline
- The memory / database / state layer
- The deployment environment (FastAPI host, GPU compute target if applicable)

A diagram that hides any of these is incomplete. The Greg-Osuri test asks "could a stranger ship a similar system from this diagram alone?" — if no, fix the diagram.

---

## 4. FastAPI auto-docs OR Postman collection

If the system exposes an API:
- **FastAPI auto-docs at `/docs`** (Swagger UI) is the default — automatic from FastAPI's OpenAPI generation.
- **Postman collection** committed at `/docs/postman.json` is the alternative when Swagger doesn't fit.

Both forms describe every endpoint, every request schema, every response schema. No undocumented endpoints in production.

---

## 5. `/docs/agent-shape.md` — the four primitives ON EVERY REPO

Mandatory file on every repo, even non-agent ones. Forces composability across the portfolio. Sections:

1. **Memory schema** — Pydantic models for episodic / semantic / procedural memory. If the system has no memory, mark "N/A — stateless service" with a one-line reason.
2. **Tool surface** — every tool the system can call, with its Pydantic schema, permissions (read-only vs action-taking · per-client allowlist · rate-limit · approval-required), and which external service it hits. Mark N/A if the system calls no external tools.
3. **Observability hooks** — what gets logged, where (Langfuse trace? Supabase log table?), and how the operator answers "what did the system do today and why."
4. **Approval / sandboxing layer** — pre-action gates for high-stakes operations. If the system is read-only, mark N/A.

By month 18, every Optimus repo exposes the same primitives in the same place. Tier-4 builds inherit them mechanically. This is the difference between "three discrete codebases" and "a composable agent stack."

---

## 6. `/docs/retro.md` — what was learned

After every system ships, a `/docs/retro.md` lands in the repo with four sections:

1. **What was built** — the actual scope that shipped, vs the original intent.
2. **What was learned** — non-obvious findings, surprises, things that took longer than expected.
3. **What would be done differently** — concrete improvements for the next similar build.
4. **Patterns to reuse** — anything worth promoting into `Offerings/02 AI Agents/shared-knowledge/lessons/` or `knowledge/patterns/` (depending on which offering it serves).

The retro is the mechanism that turns one client win into institutional knowledge. Skipping it means every project starts from zero.

---

## 7. Conventional commits

Every commit message follows the conventional commits format:

```
type(scope): short description

Longer body if needed. Why, not what.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
```

Types: `feat` · `fix` · `refactor` · `docs` · `test` · `chore` · `perf`. Scope is the affected module (e.g. `feat(ingest): add parallel document loader`).

This isn't pedantic — it makes `git log --oneline` legible to a stranger, which is part of the portfolio.

---

## 8. The two reference patterns

Every Optimus build follows TWO reference patterns simultaneously:

### Engineering-hygiene pattern — the DJ Custom Clothing logo pipeline

Sets the structural discipline every system inherits:
- FastAPI service shape
- Pydantic schema discipline
- Public GitHub repo with the structure above
- `/docs/architecture.png`, `/docs/agent-shape.md`, `/docs/retro.md`
- Conventional commits

Applies to every Optimus system, agent or not.

### Agent-architecture pattern — Marketing Team (Tier-3, when shipped)

Sets the shape every agent inherits:
- APScheduler cron loops for scheduled work
- Pydantic-typed structured outputs
- Long-horizon state in Supabase via the four agent-infrastructure primitives
- Memory · Tool · Observability · Approval layers wired correctly per `Offerings/02 AI Agents/shared-knowledge/agent-infrastructure.md`

Applies to every Optimus agent (Marketing Team · Voice Receptionist · Tier-4 Autonomous Employee).

**The DJ pipeline is NOT the agent reference** — DJ is image processing, not an agent. Conflating the two patterns would mean assuming "shipped DJ → ready for autonomous." Wrong. DJ teaches engineering hygiene; Marketing Team will teach agent design. Both apply.

---

## 9. GitHub profile standards

- **Profile README** explaining who Anthony Rosa is and what Optimus builds. One paragraph + links to the canonical repos.
- **Pinned repos** — only real systems, no tutorials.
- **Commit message discipline** as above. `git log` is part of the portfolio.
- **No empty repos.** No tutorial clones. No placeholder projects. Every repo has shipped something or is in active build with public commits.

---

## 10. The Greg-Osuri test

The standard to hold every repo to: **if you wouldn't be comfortable showing it to Greg Osuri, it's not done.**

Greg operates at the infrastructure layer of AI. He has seen every level of engineering discipline and the lack of it. The repos that pass his bar:
- Have a clear thesis stated in the README
- Have an architecture diagram you'd want pinned on the wall
- Document the four primitives even when they're N/A
- Show conventional commit hygiene that respects the reader's time
- Ship working systems that real clients pay for

The repos that fail his bar:
- Have a half-written README that says "WIP"
- Show no agent-shape doc on a system that obviously has one
- Have commit messages like "fix stuff" and "wip wip"
- Have no retro after 6 months in production

By 30, the portfolio is what gets the conversation. These standards are the discipline that earns the conversation.
