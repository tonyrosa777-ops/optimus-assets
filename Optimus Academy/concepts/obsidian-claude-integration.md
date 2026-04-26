---
title: Obsidian + Claude Integration
domain: obsidian
created: 2026-04-26
last-updated: 2026-04-26 11:36
source-files: [2026-04-26-claude-obsidian-is-insane-by-julian-goldie-seo]
tags: [#learning/synthesized, #applies-to/ai-agents/marketing]
---

# Obsidian + Claude Integration

> **Concept distilled from:**
> - [[../sources/2026-04-26-claude-obsidian-is-insane-by-julian-goldie-seo]] — Julian Goldie SEO
>
> **Last updated:** 2026-04-26 11:36

## What it is

The pattern of giving Claude AI access to an Obsidian vault — a folder of plain-text markdown notes with bidirectional wikilinks — so that the vault becomes an "AI second brain" that Claude can read, query, synthesize across, and write back into. Two integration paths exist: lightweight in-note chat via Obsidian plugins (Claudian, Sier) backed by the Claude API, and full vault-level orchestration via [[claude-code-on-vault]] for bulk operations and automation.

## When to use

- You already keep notes (or want to start) and your knowledge is currently scattered across docs, emails, screenshots, and your head
- You want an AI partner that knows your specific business, clients, and history — not a generic ChatGPT session that starts cold every time
- You need to synthesize across many notes (e.g. "find what my best clients have in common," "build a content plan from all my idea fragments")
- You want a personal learning system that knows what you know and what you don't yet know
- You want to own your data in plain text on your own machine, not in a vendor's cloud

## Mechanics

The vault is a folder of `.md` files. Obsidian gives you the editor, the link graph, the search, and the plugin layer. Claude (via API key) becomes the reasoning layer on top.

**Three layers from lightweight to heavyweight:**

1. **In-note chat (plugin path):** Install an Obsidian plugin like Claudian or Sier. Add your Claude API key. Highlight any note, ask a question, get an answer in-place. Good for ad-hoc Q&A within your reading flow. Limited to single-note or small-context queries.

2. **Vault-level orchestration (Claude Code path):** Run [[claude-code-on-vault]] — point Anthropic's terminal tool at the vault folder. Claude now has full read/write access to every note. Issue natural-language commands that span the whole vault: "read everything in this folder, find the X notes, write a new note that synthesizes Y." This is where bulk operations and content generation happen.

3. **Agentic automation (vault watcher path):** Configure Claude Code to *watch* the vault for changes. Every new note triggers a workflow — extract action items, summarize, route to a project file, etc. The vault becomes a live system instead of a static store.

**Critical design choice — separation of source vs synthesis:** without discipline, the vault becomes a swamp. The pattern that works (and matches how Optimus Academy is set up): keep raw inputs (transcripts, raw notes, captured sources) in their own folder as immutable per-source files, and keep synthesized atomic concepts in a separate folder where they can grow over time as new sources contribute. See `Optimus Academy/sources/` vs `Optimus Academy/concepts/`.

## Examples

**Bulk synthesis prompt patterns** (issued to Claude Code pointed at the vault):

```
Look at all my content ideas in this folder. Group them by topic.
Pick the top 20. Write hooks for each one.
```

```
Put together everything on this client. Make a one-page summary.
Tell me what's next.
```

```
Take my notes on <topic>. Quiz me on the key ideas.
Find gaps in my learning.
```

```
Read every note in this folder. Find the ones about marketing.
Make a new note called "master marketing plan." Put all the best
ideas in there. Organize them by traffic, leads, and sales.
```

## Gotchas

- **Cost.** You need either a Claude API key (pay per token) or a Claude subscription. For a constantly-running vault watcher this can add up — model your usage before going all-in on automation.
- **Plugin maturity varies.** Obsidian plugins like Claudian and Sier are community-built. They can be buggy and update on their own cadence. Claude Code (an Anthropic product) is more stable but has a steeper learning curve and requires terminal comfort.
- **Vault size affects latency.** Bulk operations across hundreds or thousands of notes are slow. Be selective with prompts ("look at the marketing folder" beats "look at the whole vault" for routine work).
- **Overwriting risk.** Claude Code can write to any file in the vault. Without an immutability contract for raw captures, an over-eager bulk operation can clobber source material. The Optimus Academy sources/ folder is treated as immutable for exactly this reason — if an automation needs to modify content, it does so in `concepts/` (the synthesis layer), never in `sources/`.
- **The "AI knows you" claim cuts both ways.** Claude only knows what's actually in the vault. If your notes are sparse or out-of-date, your AI second brain reflects that. Garbage in, garbage out — at scale.

## Related Concepts

- [[claude-code-on-vault]] — the heavyweight integration path; required reading for anything beyond in-note Q&A

## Updates

(none)
