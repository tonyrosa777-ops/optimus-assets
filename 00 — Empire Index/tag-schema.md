# Tag Schema

The canonical tag taxonomy for the Optimus vault. Every NEW note (anything created on or after the reorg date 2026-04-26) uses tags from this schema. Existing pre-reorg files are not retroactively retagged — they stay tag-free and remain findable through their existing wikilinks and folder location. Don't waste time backfilling tags on history.

## How to use this schema

Pick from the families below. Most notes carry 2-4 tags: one Offering, one Layer, and a Status. Learning notes add Learning lifecycle and (when relevant) Cross-link tags. Project notes add Stage tags as they move through phases.

If you find yourself wanting a tag that isn't here, stop. Either the schema needs a new entry (edit this file and explain why) or the note needs to be filed differently. Drift is what kills tag systems. New tag families require updating this file in the same commit as their first use.

Nested tags (with `/`) are searchable both by parent and child. `#offering/ai-chat` is found by searching `#offering` (returns all offerings) or `#offering/ai-chat` (returns just chat). `#applies-to/ai-agents` surfaces in all three agent products' hubs at once.

## The schema

| Tag family | Tags | Use |
|---|---|---|
| Offering | `#offering/website-dev` `#offering/ai-chat` `#offering/ai-voice` `#offering/content-engine` `#offering/all` | What part of the business this note belongs to. Use `#offering/all` only for notes that genuinely apply to every product line (rare — usually a process or brand-level note). |
| Layer | `#layer/optimus-os` `#layer/offering` `#layer/client` | Universality scope. `optimus-os` = applies to Optimus the company / universal rules; `offering` = applies to a specific product line; `client` = specific to one client engagement. |
| Learning lifecycle | `#learning/captured` `#learning/synthesized` `#learning/applied` | Where in the personal-learning pipeline. `captured` = raw notes from a course/video/book; `synthesized` = refined into an atomic concept note; `applied` = bridged to an offering improvement. |
| Cross-link | `#applies-to/website-dev` `#applies-to/ai-agents` `#applies-to/ai-agents/chat` `#applies-to/ai-agents/voice` `#applies-to/ai-agents/marketing` | Used in Optimus Academy notes to surface in offering hubs. Nested form `#applies-to/ai-agents` surfaces the note in all three agent products simultaneously. |
| Stage | `#stage/intake` `#stage/research` `#stage/scaffold` `#stage/build` `#stage/launch` `#stage/post-launch` | Where in a project lifecycle. Used on per-client notes and on retrospectives that diagnose a problem at a specific stage. |
| Status | `#status/draft` `#status/active` `#status/archived` `#status/in-development` | Maturity. `draft` = WIP, not yet usable; `active` = current canonical version; `archived` = superseded but kept for history; `in-development` = product is being built. |

## Common tag combinations

Examples to anchor the right intuition.

| Note type | Typical tags |
|---|---|
| New website-dev error postmortem in `knowledge/errors/` | `#offering/website-dev` `#layer/offering` `#status/active` |
| New website-dev pattern in `knowledge/patterns/` | `#offering/website-dev` `#layer/offering` `#status/active` |
| Per-client retro in `knowledge/retrospectives/` | `#offering/website-dev` `#layer/client` `#stage/post-launch` `#status/active` |
| Daily learning entry in `Optimus Academy/daily/` | `#learning/captured` |
| Atomic concept note in `Optimus Academy/concepts/` | `#learning/synthesized` `#status/active` |
| Apply-to-Optimus bridge for a new Chat pattern | `#learning/applied` `#applies-to/ai-agents/chat` `#status/active` |
| Apply-to-Optimus bridge that helps all 3 agent products | `#learning/applied` `#applies-to/ai-agents` `#status/active` |
| In-progress n8n workflow for the Marketing Team | `#offering/content-engine` `#layer/offering` `#status/in-development` |
| Optimus Inc competitor profile | `#layer/optimus-os` `#status/active` |
| New tool being evaluated in `tools-tracking/` | `#learning/captured` `#status/draft` |

## Tag hygiene

- One Status tag per note. Never two.
- One Layer tag per note. Never two — pick the most specific applicable layer.
- Multiple Offering tags are allowed when something genuinely spans products. Most notes are single-offering.
- Stage tags can stack only on retrospectives (one note may diagnose problems across stages).
- Use full nested paths. Write `#applies-to/ai-agents/chat`, not `#chat`. The hierarchy is the value.
- No emoji in tags. No spaces in tags. Lowercase only. Hyphens separate words.

## Schema changes

Edit this file. Note the change date. If a tag is being deprecated, leave it in the table with a strikethrough and a "→ replaced by" note rather than deleting it — old notes referencing the deprecated tag stay searchable.
