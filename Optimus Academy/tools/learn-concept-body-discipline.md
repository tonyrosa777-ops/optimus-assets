# Concept-Purity + Enrichment-Substance Rules for /learn (Accio Capture Cleanup + Skill Hardening)

## Context

The latest `/learn` capture (Accio 2.0 TikTok) revealed TWO related structural gaps in the skill:

**Gap 1 — concept body is not subject-pure.** The prompt enforces folder routing, structure templates, dedup logic, and autonomy bake-ins, but does NOT enforce **subject-purity** in concept files. As a result, `accio-2-alibaba-sourcing-agent.md` baked Optimus-relationship framing throughout its body — "Optimus does not adopt this tool", "DO NOT propose adopting Accio in any client build", "Optimus's Tier-3/Tier-4 builds should mirror this", "the value here is the agentic pattern it exemplifies, not the product itself." Concept layer is subject knowledge for awareness, period. Optimus-relationship reasoning belongs in a SEPARATE bridge file in `apply-to-optimus/` only when there's a concrete value vector. If Optimus's scope ever shifts (e.g., into e-commerce someday), a contaminated concept becomes useless — its body is full of "we don't use this" disclaimers from a prior strategic moment.

**Gap 2 — enrichment effort doesn't land as body substance.** The current skill says "synthesize the enriched info into Mechanics / Examples / Gotchas" but doesn't enforce that enriched facts must MATERIALIZE in the body. The Accio capture ran 3 WebSearches + 5 enrichment URLs, but the concept body was diluted by Optimus framing — so the user's read was that "none of the web search data was even captured." The token spend on enrichment is justified ONLY by deep subject substance landing in the body. URLs in `enriched-from:` frontmatter are bibliography, not substance. If enrichment ran but the body grew by fewer than ~5 substantive subject facts beyond what the transcript said, enrichment was wasted.

Both gaps share the same fix philosophy: the concept body is for **deep, dense, subject-level knowledge.** Nothing else competes for that space.

The `obsidian-claude-integration.md` concept stayed clean on Gap 1 (one borderline pedagogical mention of Optimus Academy, defensible). It also has dense body content. The Accio concept failed both: contaminated body AND under-leveraged enrichment.

This plan: (1) rewrite the Accio concept subject-pure AND maximally absorbing the enrichment data, (2) lightly fix today's daily file H2, (3) add BOTH rules to the `/learn` skill prompt and Academy READMEs so they survive future captures, (4) save a combined feedback memory.

## Recommended Approach

### Step 1 — Rewrite the Accio concept (subject-pure AND enrichment-dense)

File: `c:\Projects\Optimus Assets\Optimus Academy\concepts\accio-2-alibaba-sourcing-agent.md`

Tone reference: `c:\Projects\Optimus Assets\Optimus Academy\concepts\obsidian-claude-integration.md` — describes its subject directly, with sub-section sub-headings, dense Mechanics/Examples/Gotchas. Mentions Optimus only once pedagogically.

**1a — Subject-purity edits (strip Optimus framing):**
- **Title:** `Accio — Alibaba's End-to-End AI Sourcing Agent` (drop "Vertical-Ownership" framing — that was Optimus-architectural language).
- **What it is:** delete the "Optimus does not adopt this tool" sentence. Two clean sentences: what Accio is, who it's by, headline scale.
- **When to use:** rewrite for Accio's actual users — solo entrepreneurs validating product ideas, SMEs sourcing physical products, B2B buyers running RFQs across multiple Chinese marketplaces, first-time importers who want unit-economics visibility before committing to MOQs. Drop the entire "CONCEPT (vertical-ownership pattern) is a reference exemplar for [Tier-3/Tier-4]" block.
- **Mechanics:** keep the 7-step workflow. Remove the "Optimus's Tier-3/Tier-4 builds should mirror this" sentence. Remove "This mirrors the Optimus Tier-3 Marketing Team thesis." Remove "useful UX pattern for any Optimus-built agent."
- **Gotchas:** keep the first 5 subject-pure ones. DELETE the entire "Not in Optimus's stack — DO NOT propose adopting Accio in any client build" gotcha (bridge concern, not a topic gotcha).
- **Related Concepts / Updates:** keep `(none)` placeholders.

Frontmatter:
- Drop `audience: [founder, optimus-internal]` → set `audience: []` (or omit). Audience for an Accio knowledge note is anyone learning about agentic sourcing tools.
- Keep `enriched-from:` URLs, `level: intermediate`, `domain: agents`, `review-by: 2026-11-02`.

**1b — Enrichment-substance expansion (pull every useful fact from the 5 enrichment URLs into the body):**

The body must absorb ALL of the following enrichment facts. Each enrichment URL needs to contribute substance, not just sit in `enriched-from:`. Where each fact lands:

| Enriched fact | Where it lands in the rewritten concept |
|---|---|
| Accio = world's first B2B AI sourcing engine; positioned as conversational, intent-driven (not keyword-driven); functions like a "junior procurement specialist you can talk to" | What it is — defining sentence |
| Two SKUs: consumer Accio app (App Store + Google Play) + enterprise Accio Work | What it is — product surface |
| 10M+ monthly active users; 230k+ online stores powered globally | What it is — scale |
| Built on Alibaba's own Qwen open-source LLM + DeepSeek-R1 + GPT-4o, fine-tuned on 25 years of trade data (billions of listings, millions of supplier profiles) | Mechanics → Underlying tech stack |
| Connects to 1.5M+ verified suppliers, 7,600+ wholesale categories, 400M+ products across Alibaba, 1688, Taobao, AliExpress | Mechanics → Underlying tech stack |
| Accio Work launched 2026-03-24 with "agent fleets" — pre-configured cross-functional squads (analyst + creator + logistics expert agents) dynamically assembled per task, run in parallel | Mechanics → Pre-configured team-of-agents (Accio Work) — keep but de-Optimus |
| Accio Work claim: build a functioning online store in 30 minutes | Mechanics → Pre-configured team-of-agents (Accio Work) |
| Drives execution through Telegram + WhatsApp for marketing automation and logistics oversight | Mechanics → Underlying tech stack |
| Per MIT Tech Review hands-on: Accio "blows away" general AI tools like ChatGPT for product research and sourcing analysis | Examples or a new "Independent reviews" subsection in Mechanics |
| Per MIT Tech Review hands-on: Accio surfaces margin analysis in-line ($6.71 wholesale hoodie example, 200–300% target retail margin band, MOQ range visible at decision time) | Mechanics → Margin transparency subsection |
| Vietnam T-shirt example: agent evaluates suppliers on operational history, international experience, production capacity, local market presence, track record, and certifications | Examples — keep |
| Negotiation tactic Accio surfaces: written commitment for 3–5 recurring orders can reduce MOQ by 25–40% (shifts supplier risk perception from one-time small order to predictable revenue stream) | Mechanics — new subsection on negotiation surface |
| Spot-goods low-margin warning: when buying spot goods, MOQ is low/zero but it's a low-margin business, prone to product homogeneity and fierce price competition | Gotchas — new entry on spot-goods tradeoff |
| Lower-than-standard MOQs often hide: higher unit prices, inconsistent material quality from subcontractor variance, longer production times, potential compliance issues | Gotchas — expanded MOQ tradeoff entry |
| Strongest at product ideation + sourcing; weakest at marketing (advertising, social outreach) per MIT Tech Review | Gotchas — keep |
| Locked to Alibaba's data and supplier network — not useful for non-Alibaba ecosystems (Western suppliers, regional B2B) | Gotchas — keep |
| "Automate 70% of manual sourcing tasks" claim is from Alibaba PR, not independently measured | Gotchas — keep |
| No public developer API surfaced in coverage — Accio is app/web-locked | Gotchas — keep |

Target body density after rewrite: ~1,200–1,800 words (current contaminated version is ~900 words including Optimus filler; subject-pure + fully enriched should grow by 30–50%, not shrink).

### Step 2 — Lightly clean today's daily file H2

File: `c:\Projects\Optimus Assets\Optimus Academy\daily\2026-05-02.md`

Per your decision to edit-now: rewrite the `#### Why this matters as an agentic-pattern exemplar` subsection (currently lines 51–55) to keep the agentic observation but drop the Tier-4 / north-star reference. Replacement subsection title + one short paragraph: `#### Why the agentic shape matters` describing single-agent-owns-the-vertical pattern with the artifact-threading observation, no Optimus name, no Tier-4 reference.

Daily-file frontmatter and other H2 sections: untouched.

### Step 3 — Add BOTH rules to the /learn skill

File: `c:\Projects\Optimus Assets\learn-prompt.md`

Insert a new paragraph block in the **Step 3 → CREATE path — new concept file** section, immediately after the `## Updates` line of the template block, BEFORE the "Forward-compat field decision rules" block.

Wording (final draft, both rules together since they share the same body-discipline philosophy):

> **Concept body discipline (non-negotiable, two rules).**
>
> **Rule 1 — Subject-purity.** Concept body teaches the topic itself for the user's awareness — what it is, how it works, when its actual users would use it, examples drawn from the topic's domain, gotchas about the topic. Zero Optimus-relationship framing in the body: no "Optimus does/doesn't adopt this", no "Tier-3/Tier-4 builds should mirror this", no "this is for our Marketing Team agent", no client-build advisories. If the concept has clear Optimus application, that goes in a SEPARATE bridge note in `apply-to-optimus/` per Step 4. Subject-pure concepts stay useful if Optimus's scope shifts later (e.g., into e-commerce, hardware, retail).
>
> **Rule 2 — Enrichment must materialize as body substance.** When Step 1.5 enrichment fires, every URL added to `enriched-from:` MUST contribute at least one substantive subject fact to the body (Mechanics, Examples, or Gotchas — not just a citation in passing). The frontmatter `enriched-from:` field is bibliography, NOT substance. If enrichment ran but the body grew by fewer than ~5 substantive subject facts beyond what the original transcript said, enrichment was wasted — go back and pull more facts before writing. Token spend on web searches is justified ONLY by deep subject knowledge landing in the body.
>
> **Reference tone:** `obsidian-claude-integration.md` describes Obsidian + Claude on its own terms with dense Mechanics sub-sections, code examples, and seven gotchas — that's the floor for body density and subject-purity. The `accio-2-alibaba-sourcing-agent.md` rewrite (post this skill update) is a second reference: ~1,500-word subject-dense concept with no Optimus framing in the body and every enriched URL contributing real facts.

### Step 4 — Mirror the rule in the Academy READMEs

Files:
- `c:\Projects\Optimus Assets\Optimus Academy\README.md` — add a one-line cross-reference under the existing "Concept file structure" section pointing to the subject-purity rule in `learn-prompt.md`.
- `c:\Projects\Optimus Assets\Optimus Academy\apply-to-optimus\README.md` — add a one-line note at the top of "Multi-purpose principle" reinforcing that the bridge is the ONLY place Optimus-relationship framing belongs; concept files stay subject-pure.

Both edits are short cross-references, not duplicate rule statements. Single source of truth lives in `learn-prompt.md`.

### Step 5 — Save a feedback memory (safety net, both rules)

File: `C:\Users\Anthony\.claude\projects\c--Projects-Optimus-Assets\memory\feedback_concept-body-discipline.md`

Per the auto-memory feedback type. Single combined memory covering BOTH rules since they share the same "body real estate is for subject substance" philosophy:

- **Rule:** /learn concept body has two non-negotiable disciplines: (1) subject-purity — zero Optimus-relationship framing in the body, that goes in bridges; (2) enrichment-substance — every `enriched-from:` URL must contribute at least one substantive body fact, frontmatter is bibliography not substance.
- **Why:** Accio capture incident — body got dominated by Optimus disclaimers AND the user's read was that "none of the web search data was even captured" because contaminated body crowded out the enriched substance. Either failure mode wastes the capture: contamination makes the concept stale when scope shifts, under-enrichment wastes the token spend on web searches.
- **How to apply:** Whenever /learn writes a concept file, audit the body before commit: (a) grep for `Optimus`, `Tier-1..4`, `Marketing Team`, `our agent`, `client build`, "we don't adopt" — any hit means strip and consider a bridge; (b) count substantive facts that came from enrichment vs the transcript — if fewer than ~5 enrichment-sourced facts in the body, enrichment was wasted, go back and pull more.

Add the index line to `MEMORY.md`.

### Step 6 — Save the plan to the vault (Plan Preservation Rule)

Per the CLAUDE.md Plan Preservation Rule: this plan touches the `/learn` AI capture pipeline, so its canonical copy lives at:

`c:\Projects\Optimus Assets\Optimus Academy\tools\learn-concept-body-discipline.md`

Copy the contents of `C:\Users\Anthony\.claude\plans\okay-so-we-have-snoopy-ripple.md` (this file — Claude Code's working memory) to that vault path BEFORE the commit. The auto-generated working file stays where it is for this session; the vault copy is the durable artifact that gets versioned alongside the code it changed.

Filename rationale: `learn-concept-body-discipline.md` is kebab-case, describes the value delivered (a discipline rule applied to /learn), not the process. The auto-generated `okay-so-we-have-snoopy-ripple.md` is the working name and is NOT the canonical artifact.

### Step 7 — Commit + push (single atomic commit)

**Inventory of work touched (8 files total, 6 in the commit):**

In the git commit (vault-side):
1. `Optimus Academy/concepts/accio-2-alibaba-sourcing-agent.md` (rewrite per Step 1)
2. `Optimus Academy/daily/2026-05-02.md` (edit per Step 2)
3. `learn-prompt.md` (add rules per Step 3)
4. `Optimus Academy/README.md` (cross-reference per Step 4)
5. `Optimus Academy/apply-to-optimus/README.md` (cross-reference per Step 4)
6. `Optimus Academy/tools/learn-concept-body-discipline.md` (canonical plan per Step 6)

NOT in the git commit (outside the repo, in `~/.claude/projects/c--Projects-Optimus-Assets/memory/`):
7. `feedback_concept-body-discipline.md` (new memory per Step 5)
8. `MEMORY.md` (add index line per Step 5)

Pre-stage check: `git status` must show exactly the 6 vault files dirty (no surprise additions, no missing files). Stage them by name explicitly — never `git add .` or `git add -A`. Then commit + push immediately per the always-push memory.

Suggested message:
```
fix(learn): enforce concept body discipline; rewrite Accio capture

Two new rules added to /learn skill, both surfaced by Accio capture incident:

- Rule 1 — Subject-purity: concept body teaches the topic itself; zero
  Optimus-relationship framing in body (belongs in apply-to-optimus bridges).
- Rule 2 — Enrichment must materialize as body substance: every enriched-from
  URL contributes at least one substantive subject fact to body. Frontmatter
  is bibliography, not substance.

Files:
- Rewrite concepts/accio-2-alibaba-sourcing-agent.md (subject-pure +
  absorbs every fact from the 5 enrichment URLs into Mechanics/Examples/Gotchas)
- Light edit daily/2026-05-02.md H2 to drop Tier-4 reference from one subsection
- Add Concept body discipline block to learn-prompt.md CREATE path
- Mirror in Academy README + apply-to-optimus README (cross-references only)
- Save canonical plan to Optimus Academy/tools/learn-concept-body-discipline.md
```

## Critical Files

**In the git commit (6 files):**

| File | Change |
|---|---|
| `Optimus Academy/concepts/accio-2-alibaba-sourcing-agent.md` | Rewrite per Step 1a (subject-purity) + 1b (absorb every enrichment fact); tighten frontmatter `audience` |
| `Optimus Academy/daily/2026-05-02.md` | Rewrite one subsection in the Accio H2 (other H2 sections untouched) |
| `learn-prompt.md` | Insert Concept body discipline block (Rule 1 + Rule 2) in CREATE path |
| `Optimus Academy/README.md` | One-line cross-reference under Concept file structure |
| `Optimus Academy/apply-to-optimus/README.md` | One-line note under Multi-purpose principle |
| `Optimus Academy/tools/learn-concept-body-discipline.md` | Canonical plan file (Plan Preservation Rule) |

**Outside the git commit (memory, in `~/.claude/projects/c--Projects-Optimus-Assets/memory/`):**

| File | Change |
|---|---|
| `feedback_concept-body-discipline.md` | New feedback memory covering both rules |
| `MEMORY.md` | Add index line for the new memory |

## Reference Patterns

- **Tone reference for the Accio rewrite:** `Optimus Academy/concepts/obsidian-claude-integration.md` — clean subject-pure body with sub-sections, examples, gotchas.
- **Bridge handles Optimus framing correctly:** `Optimus Academy/apply-to-optimus/obsidian-claude-integration-applied-to-ai-marketing.md` — gap analysis + 5-phase application reasoning lives here, NOT in the concept.
- **Slug + URL canonical rules:** `00 — Empire Index/tag-schema.md` (already followed in current Accio capture; no change).

## Verification

End-to-end check after the commit lands:

1. **Subject-purity check on `concepts/accio-2-alibaba-sourcing-agent.md`** — read end-to-end and grep the body (between `# Accio` H1 and `## Updates`) for these forbidden tokens:
   - `Optimus`, `Tier-1`, `Tier-2`, `Tier-3`, `Tier-4`, `Marketing Team`, `Autonomous Employee`, `north-star`, `client build`, `our agent`, `our stack`
   - Expected: zero matches in body. (Frontmatter `enriched-from:` URLs and the visible blockquote "Concept distilled from" wikilink to the daily file are infrastructure, not body content — exempt.)

2. **Enrichment-substance check on the same file** — for each of the 5 URLs in `enriched-from:`, confirm the body contains at least one substantive fact attributable to that source (e.g., MIT Technology Review URL → margin transparency $6.71 hoodie example AND/OR "blows away ChatGPT" claim is in body; Alibaba PR URL → Accio Work + agent fleets in body; etc.). Body should grow from current ~900 words to ~1,200–1,800 words after the rewrite. If the word count shrinks below 1,000, the enrichment data didn't land — rewrite again.

3. **Skill rule check on `learn-prompt.md`** — confirm the Concept body discipline block is present in the CREATE path section, has both Rule 1 (Subject-purity) and Rule 2 (Enrichment-substance) clearly numbered, and references both `obsidian-claude-integration.md` and the rewritten `accio-2-alibaba-sourcing-agent.md` as tone references.

4. **Daily file check on `daily/2026-05-02.md`** — confirm the "Why this matters as an agentic-pattern exemplar" subsection no longer references Tier-4 or north-star.md. All other H2 metadata, blockquote, Summary, Key Concepts, Code, Quotes, Action Items, Open Questions byte-identical to before.

5. **README cross-reference check** — both Academy README files have the cross-reference lines added without restating the rules (single source of truth = learn-prompt.md).

6. **Memory check** — `MEMORY.md` has the new index line; `feedback_concept-body-discipline.md` exists with both rules + Why + How-to-apply.

7. **Real-world proof: run `/learn` against a fresh test source AFTER the rule lands** and confirm the next concept written passes BOTH checks on first attempt — subject-pure body + enriched-URLs each contributing real body facts. If a fresh capture drifts on either rule, the rule wording is too soft and needs sharpening.
