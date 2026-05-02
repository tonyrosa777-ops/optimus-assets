# Agent Model Routing

Every agent file in `.claude/agents/` declares an `effort:` field in its frontmatter. This file is the canonical mapping from `effort` to actual Claude model selection. Orchestrators MUST consult this table before spawning an agent — model choice is never ad-hoc.

## Routing Table

| effort | Model                       | Rationale                                | Currently used by                                                                                  |
|--------|-----------------------------|------------------------------------------|----------------------------------------------------------------------------------------------------|
| max    | `claude-opus-4-7`           | Highest quality, slowest, most expensive — one-shot work that must catch everything | design-synthesizer · pre-launch-auditor                                                            |
| xhigh  | `claude-opus-4-7`           | Quality-critical with deep reasoning     | market-researcher · content-writer · animation-specialist · seo-aeo-specialist · gap-analyzer      |
| high   | `claude-sonnet-4-6`         | Strong reasoning, faster, cheaper        | reserved — not currently used                                                                      |
| mid    | `claude-haiku-4-5-20251001` | Fast, cheap, deterministic transforms    | reserved — not currently used                                                                      |

## Routing Rule

The orchestrator picks the model based on the agent's `effort:` frontmatter field, not by ad-hoc judgement at spawn time. If an agent's quality slips at its current tier, change the agent file's frontmatter — never bypass with a one-off override.

## When to Downshift

An agent currently at `xhigh` whose work is purely deterministic (string substitution, file reorganization, mechanical scaffolding, copy-paste with template fills) can drop to `mid` (Haiku). Document the change in `knowledge/build-log.md` Build Patterns table with: agent name, prior tier, new tier, observed quality post-change.

## When to Upshift

An agent at `high` producing recurring quality issues moves to `xhigh`. Document the upshift reason in `knowledge/build-log.md` — typically a category of failure (hallucinated copy, wrong design tokens, missed validation criteria) that disappears at the higher tier.

## Model ID Source of Truth

Model IDs above are the canonical Claude Code identifiers as of 2026-05-02. If Anthropic ships a newer family, update this file before spawning agents at the affected tier. The session environment block lists current model IDs at session start — verify against that, not against a memorized version.
