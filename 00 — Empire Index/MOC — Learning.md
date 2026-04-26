# MOC — Learning

Optimus Academy is the personal learning system. Every concept Anthony picks up, every course lesson, every emerging-tool experiment, every bridge from "I learned X" to "X improves offering Y" — it all lives in `Optimus Academy/`.

Hub: [[Optimus Academy/README]]

## Active study tracks

These are the streams currently in rotation. New tracks get added to `Optimus Academy/courses/<source>/` when they start.

| Track | Source | Folder |
|---|---|---|
| Claude concepts (deep dives) | YouTube channels, Anthropic docs | `Optimus Academy/courses/youtube/` and `Optimus Academy/concepts/` |
| Anthropic official courses | Anthropic Skilljar, cookbook, Claude API docs | `Optimus Academy/courses/anthropic/` |
| NVIDIA classes | NVIDIA Deep Learning Institute | `Optimus Academy/courses/nvidia/` |
| Agentic AI / autonomous agents | Mixed (papers, YouTube, Anthropic, OpenAI) | `Optimus Academy/concepts/` |
| Books | Whatever's on the desk | `Optimus Academy/courses/books/` |

### Tools being tracked

Emerging tools that aren't yet adopted but are worth watching. Each tool gets one file in `Optimus Academy/tools-tracking/` with: what it is, what problem it solves, current status (watching / piloting / adopted / rejected), and who else is using it.

- NemoClaw — `Optimus Academy/tools-tracking/nemoclaw.md`
- OpenClaw — `Optimus Academy/tools-tracking/openclaw.md`

## The three traces

Every learning capture leaves three traces. This is the discipline that keeps learning from disappearing.

| Trace | File | Purpose |
|---|---|---|
| 1. Daily entry | `Optimus Academy/daily/YYYY-MM-DD.md` | Chronological. What you watched, read, or built today. Index of links to the concept notes you created. |
| 2. Atomic concept note | `Optimus Academy/concepts/<concept>.md` | Zettelkasten-style. One concept per file. Heavily wikilinked. Lives forever, gets revisited. |
| 3. Apply-to-Optimus bridge | `Optimus Academy/apply-to-optimus/<bridge>.md` | Only when applicable. "Concept X improves offering Y by doing Z." Tagged with `#applies-to/<offering>` so it surfaces in the right offering hub. |

If you learned something and didn't write the daily entry, it didn't happen. If you learned something specific and didn't write the concept note, you'll forget the precision and only keep the vibe. If you learned something Optimus could use and didn't write the bridge, the learning evaporates before it ever earns its keep.

## The `/learn` slash command

`learn-prompt.md` (at vault root) codifies the workflow above. Run `/learn` at the end of any learning session — it walks the daily entry, creates the concept notes, and prompts you for the apply-to-optimus bridge if there is one. See [[learn-prompt]].

If `/learn` doesn't exist yet, create it from the workflow above. The slash command is the enforcement mechanism — without it, the three-trace discipline drifts.

## How learning surfaces in offerings

The bridge. This is why the tag schema exists.

When a concept note lands in `Optimus Academy/concepts/` with a clear application to an offering, you create a bridge note in `Optimus Academy/apply-to-optimus/` and tag it with the appropriate `#applies-to/...` tag from [[tag-schema]]. Examples:

- A new Claude prompt-caching pattern that cuts Chat Assistant cost by 60% → `apply-to-optimus/prompt-cache-chat-cost.md` tagged `#applies-to/ai-agents/chat`
- A new conversion-copy framework from a YouTube watch → `apply-to-optimus/<framework>-website-copy.md` tagged `#applies-to/website-dev`
- A multi-agent orchestration pattern that fits both Voice and Marketing → `apply-to-optimus/<pattern>.md` tagged `#applies-to/ai-agents` (the parent tag surfaces in all three agent hubs at once)

Each offering hub maintains a query (Obsidian Dataview or a manual list) that pulls every bridge note tagged for it. So when you open `Offerings/02 AI Agents/01 Chat Assistant/README.md`, you see the running list of "things I've learned that should improve this product." That list is the work backlog.

Without the bridge note, the learning lives in the Academy and never improves the products. The bridge is the load-bearing piece.
