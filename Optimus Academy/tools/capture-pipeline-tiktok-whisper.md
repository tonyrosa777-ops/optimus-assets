# AI Content Capture Pipeline — Extend `/learn` for Short-Form Video

## Context

Anthony watches TikToks, Reels, Shorts, YouTube, and reads articles on AI daily, taking notes manually and saving sources for later capture. He proposed building a new "second brain" capture system — but the second brain already exists as `/learn` + Optimus Academy. What's missing is the **input layer** for sources without a public transcript API (primarily TikTok and Instagram Reels).

The existing system already covers:
- Daily H2 source captures with full attribution (`Optimus Academy/daily/YYYY-MM-DD.md`)
- Atomic concept synthesis with scan-and-decide dedup (`concepts/`)
- Apply-to-optimus bridges with `not-started → in-progress → applied → verified` lifecycle
- Bidirectional wikilinks across daily / concepts / bridges
- Mandatory Dataview metadata on every capture

This plan adds the missing input pathway and one proactive surface (weekly review) without replacing or duplicating anything.

**User decisions confirmed:**
- Source mix: TikTok/IG/Reels + YouTube + articles + miscellaneous ("Other")
- Input UX: URL-paste with silent download → Whisper transcription. **No microphone capture.**
- Review surface: Dataview-powered `weekly-review.md` listing aging bridges. No autonomous review agent.
- **Topic scope is broad, not AI-only.** Captured content can be sales training, copywriting craft, marketing psychology, finance, productivity tools, design, hiring, ops — anything where the value applies somewhere in the Optimus stack. The bridge layer must route knowledge to *any* relevant destination in the vault, not only the four AI offerings.

---

## Architecture

**Two extensions, one skill.** `/learn` already handles YouTube URLs and pasted transcripts. We add (a) URL-pattern detection for TikTok / IG Reels / IG Posts / YouTube Shorts → route through a new `transcribe-url.py` helper → existing `/learn` pipeline, and (b) broadened bridge-target routing so a sales training video can land a bridge in `knowledge/craft/copywriting/`, a finance video in `Optimus Inc/operations/`, a tool review in `Optimus Academy/tools-tracking/`, and an AI-agent paper in the existing offering hubs. Same skill, broader applicability targets, light tag-taxonomy extension.

```
User: /learn <URL>
        │
        ▼
  ┌─────────────────────────────────┐
  │ /learn skill (learn-prompt.md)  │
  │ - URL pattern detection (NEW)   │
  └─────────────────────────────────┘
        │
        ├─ TikTok/IG/Reels/Shorts URL ──► tools/transcribe-url.py (NEW)
        │                                  - yt-dlp: download audio + metadata
        │                                  - Whisper API: transcribe
        │                                  - return {transcript, publisher, title, url, source-date, duration}
        │
        ├─ YouTube long-form URL ────────► existing transcript fetch (unchanged)
        │
        ├─ Article URL / pasted text ────► existing flow (unchanged)
        │
        └─ "Other" (X posts, podcasts) ──► existing paste-text fallback (unchanged)
                                           │
                                           ▼
                       existing scan-and-decide → daily H2 + concept + bridge
                                           │
                                           ▼
                            bridge `applies-to:` target may be:
                            ├─ Offering hub                   (folder exists)
                            ├─ knowledge/patterns/<slug>.md   (folder exists, populated)
                            ├─ knowledge/craft/<area>/<slug>.md   (folder NEW — lazy-create)
                            ├─ Optimus Inc/<area>/<slug>.md   (verify per-area; lazy-create if absent)
                            └─ tools-tracking/<tool-slug>.md  (folder exists with .gitkeep — first population)
```

### Bridge target taxonomy

Every captured concept has at least one `applies-to:` wikilink. The link points to whichever vault location would actually integrate the knowledge. The five valid target zones:

| Target zone | When it applies | Example source → target |
|---|---|---|
| `Offerings/<offering>/` | Concept changes how a productized offering is built or operated | A new agent eval pattern → `Offerings/02 AI Agents/shared-knowledge/lessons/<slug>.md` |
| `knowledge/patterns/` | Cross-website-build pattern that any client site could reuse | Hero animation technique → `knowledge/patterns/<slug>.md` |
| `knowledge/craft/<area>/` | Cross-cutting craft principle (copywriting, psychology, sales, design) | Anchoring tactic from a sales training video → `knowledge/craft/copywriting/anchoring-pricing.md` |
| `Optimus Inc/<area>/` | Concerns Optimus the company itself, not the offerings | Founder cash-flow heuristic from a finance video → `Optimus Inc/operations/cash-flow-rules.md` |
| `Optimus Academy/tools-tracking/<tool-slug>.md` | Evaluating whether to adopt a tool into Optimus's stack | A new agent framework review → `Optimus Academy/tools-tracking/langgraph-eval.md` (flat file, one per tool) |

A single concept may produce multiple bridges (one per applicable zone). The existing bridge schema (concept link, why-it-applies, how-to-apply, status, updates) works unchanged across all five zones.

### Multi-purpose principle: every captured concept must ladder to a business outcome

Knowledge in this vault is not collected for its own sake. Every concept worth capturing must ladder to at least one of three business outcomes — and **every bridge declares which outcome(s) it serves** so the weekly review can prioritize by leverage, not just age.

The three value vectors:

| Vector | What it means | Examples |
|---|---|---|
| `productivity` | Increases speed or quality of building, shipping, or operating | New animation pattern that cuts hero-build time 30% • Better critic agent prompt that improves first-pass quality • SEO checklist that prevents post-launch rework |
| `overhead` | Reduces manual work, context-switching, duplication, error rates | Folder-creation policy that prevents empty-folder noise • Skill that auto-generates boilerplate • Pattern that prevents a recurring error from build-log.md |
| `revenue` | Directly affects pricing, conversion, retention, offerings, or new tiers | New pricing-page tactic from a sales source • CRO heuristic that lifts quiz-to-booking conversion • New offering or tier idea • Better cold-email sequence |

A single concept frequently serves multiple vectors. A pricing-page anchoring tactic serves both `productivity` (every future build inherits the tactic via content-writer.md, so faster shipping) AND `revenue` (every client site converts better). Multi-valued by default.

**Two simultaneous concept roles** (these are HOW concepts ladder to business outcomes):

1. **Pedagogical role** — the concept note is the teaching artifact. The 7-section structure (What/When/Mechanics/Examples/Gotchas/Related/Updates) is a lesson, full stop. Anthony reads it as a founder applying ideas to Optimus Inc; a future Optimus University student reads it as someone learning the principle for their own business; a future client reads it as part of a paid course. **Same artifact, different consumers, distinguished only by the `audience:` field.**

2. **Operational role** — the concept's applications to Anthony's specific systems get bridges. A bridge says "this concept changes how `<file>` operates AND serves these value vectors." Bridges are downstream of concepts and describe action, not instruction.

**Therefore (until University ships):** there is no "University" bridge zone, and `/learn` must NOT create one. Optimus University compilation in the substrate-accumulation phase is a Dataview query against `concepts/` — grouped by `domain` + `level` + `audience` — not a separate folder of duplicated lessons. The forward-compat fields (`level`, `prerequisites`, `audience`) on the concept note are the sole University substrate during this phase. Bridges remain operational-only and carry the value-vector tagging.

**When University ships as a real offering** (Tier 5, paid product, decided post-substrate accumulation): University becomes a 5th offering hub at `Offerings/05 University/<course>/<module>.md` and bridges route to it like any other offering. A single concept then commonly produces multiple bridges with different vector profiles:

- Bridge to `Optimus Inc/finance/<slug>.md` → `value-vector: [overhead]` — Anthony's own application
- Bridge to `.claude/agents/build/content-writer.md` → `value-vector: [productivity, revenue]` — propagates to all client copy
- Bridge to `Offerings/05 University/Founder Finance 101/<module>.md` → `value-vector: [revenue, productivity]` — course module is direct revenue (course sales) AND students applying it gain productivity

Same concept, four-plus bridges, vectors compound across them. The weekly review correctly surfaces the highest-leverage application first regardless of which target zone it lives in. **The architecture absorbs the University-as-offering transition with zero schema changes** — only the routing map gains a new row when the offering ships.

**Implication for current build:** capture concepts now with full forward-compat fields (`level`, `prerequisites`, `audience`) so when University ships, the substrate is ready. The University bridge target row will be added to the routing map at that time, not now.

**Required bridge frontmatter addition:**

```yaml
value-vector: [productivity, overhead, revenue]   # MANDATORY, multi-valued, at least one
expected-impact: small | medium | large           # OPTIONAL, populated when source makes magnitude obvious
```

`value-vector` is mandatory on every bridge. If `/learn` cannot identify at least one vector for a concept, it does NOT create a bridge — concept note only. A bridge that serves no value vector is by definition dead weight.

**No-bridge rule (sharpened):** if a concept teaches a principle but `/learn` cannot map it to at least one of the three vectors with concrete reasoning ("this lifts conversion because…", "this cuts build time because…"), the concept goes to `concepts/` only. The weekly review never sees value-vector-less captures because they don't exist as bridges.

**Worked example (revised with multi-purpose framing).** A finance YouTube video on bootstrapped runway rules produces:
- One concept note: `concepts/bootstrapped-runway-rules.md` with `domain: finance`, `level: foundational`, `audience: [founder]`. The teaching artifact — neutral, multi-consumer.
- One operational bridge: `applies-to: [[../../Optimus Inc/finance/runway-rules.md]]`, `value-vector: [overhead, revenue]`, `expected-impact: large`. Reasoning: applying runway rules reduces founder context-switching on cash-flow decisions (overhead) AND constrains pricing decisions toward sustainable revenue (revenue).
- Zero University bridges. When Optimus University compiles a "Founder Finance 101" course later, the Dataview query returns this concept note. Course = query result.

**Worked example (multi-vector copywriting).** A sales-training TikTok on pricing anchors produces:
- One concept note: `concepts/pricing-anchor-tactic.md` with `domain: copywriting`, `level: intermediate`, `audience: [marketer, founder]`.
- Bridge A: `applies-to: [[../../.claude/agents/build/content-writer.md]]`, `value-vector: [productivity, revenue]`, `expected-impact: medium`. Reasoning: every future client site's pricing page inherits the anchor (productivity, applied-once-used-forever) AND lifts conversion (revenue, measured via lift on quiz-to-booking).
- Bridge B: `applies-to: [[../../knowledge/craft/copywriting/anchoring-pricing.md]]`, `value-vector: [productivity]`, `expected-impact: small`. Reasoning: institutional pattern absorbed cross-build, marginal productivity gain on top of the agent update.
- Zero University bridges.

This principle holds for every entry in the routing map below: the **target column lists where the concept ACTS** (operational), and **the value-vector field on each bridge declares the business outcome it serves**.

### Concrete routing map (source topic → existing-file bridge target)

The 5-zone taxonomy above is abstract. This table is the concrete routing decision tree `/learn` uses to pick `applies-to:` targets. Every file named here has been verified to exist in the vault before this plan was written. Lazy-created folders are flagged.

**Insight unlocked here:** the `.claude/agents/*.md` files are the highest-leverage bridge targets in the vault. Each agent is a living institutional pattern that runs in every future build. Updating `content-writer.md` with a new copywriting tactic immediately propagates that tactic to every client site shipped after — far faster than waiting for the pattern to be "remembered" via `knowledge/patterns/` consultation. Treat agent files as primary bridge targets when applicable, with `knowledge/craft/` as secondary substrate for cross-cutting principles.

| Source topic | Primary bridge target | Secondary bridge target | Example |
|---|---|---|---|
| **Sales / cold outreach tactics** | `.claude/agents/sales/gap-analyzer.md` (verified, exists) — propagates to discovery calls | `knowledge/craft/sales/<slug>.md` (NEW lazy-create) | A discovery-call question framework from a sales TikTok → update gap-analyzer's discovery script + write the principle |
| **Copywriting craft** (headlines, CTAs, hooks, structure, tone) | `.claude/agents/build/content-writer.md` (verified, exists) — propagates to every client site | `knowledge/craft/copywriting/<slug>.md` (NEW lazy-create) | Anchoring tactic from a sales-training video → update content-writer's pricing-page section + write the principle |
| **Marketing psychology / cognitive bias** | `.claude/agents/build/content-writer.md` (copy uses the bias) AND `.claude/agents/onboarding/design-synthesizer.md` (visual hierarchy uses the bias) | `knowledge/craft/psychology/<slug>.md` (NEW lazy-create) AND/OR `Optimus Inc/brand/<slug>.md` if it changes Optimus's own marketing voice | Loss-aversion in pricing → update both content-writer + design-synthesizer + write the principle |
| **CRO / landing page conversion** | `.claude/agents/build/content-writer.md` AND `.claude/agents/onboarding/design-synthesizer.md` | `knowledge/patterns/<slug>.md` (existing folder) | New pricing-page heuristic → update both agents + write a pattern |
| **Visual design / UI craft** | `.claude/agents/onboarding/design-synthesizer.md` AND `.claude/agents/build/animation-specialist.md` | `knowledge/craft/design/<slug>.md` (NEW lazy-create) AND/OR `frontend-design.md` (verified, exists) | New micro-interaction pattern → update animation-specialist + frontend-design.md |
| **SEO / AEO / discoverability** | `.claude/agents/build/seo-aeo-specialist.md` (verified, exists) | `knowledge/patterns/<slug>.md` (existing folder) | New schema markup tactic → update the agent + write the pattern |
| **Market research / discovery patterns** | `.claude/agents/onboarding/market-researcher.md` (verified, exists) | `knowledge/patterns/<slug>.md` | New competitive-analysis framework → update the agent + write the pattern |
| **QA / launch / pre-deploy checks** | `.claude/agents/launch/pre-launch-auditor.md` (verified, exists) | `knowledge/patterns/<slug>.md` AND/OR `knowledge/errors/<slug>.md` if it's an error to prevent | New mobile-viewport bug class → update auditor + write the error |
| **Finance / runway / pricing strategy for Optimus** | `Optimus Inc/finance/<slug>.md` (folder **NEW** — lazy-create; verified absent at plan time) | `optimus-system-guide.md` if the finance rule changes vault operations (rare) | Bootstrapped runway heuristic → write to `Optimus Inc/finance/runway-rules.md` |
| **Hiring / team / org design** | `Optimus Inc/operations/<slug>.md` (folder **NEW** — lazy-create; verified absent at plan time) | None | First-hire framework → `Optimus Inc/operations/hiring-playbook.md` |
| **Optimus's own marketing / brand voice** | `Optimus Inc/brand/<slug>.md` (folder **EXISTS** with README.md — write directly, no lazy-create) | None | Brand-voice rule from a marketing podcast → `Optimus Inc/brand/voice-rules.md` |
| **Optimus's own website / content strategy** | `Optimus Inc/website/<slug>.md` (folder **EXISTS** with README.md + content-strategy.md — append or write new file) | `.claude/agents/build/content-writer.md` if the lesson generalizes to all client copy | New homepage copy framework → `Optimus Inc/website/<slug>.md` + bridge to content-writer |
| **Competitive intelligence on Optimus's market** | `Optimus Inc/market-intelligence/<slug>.md` (folder **EXISTS** with README.md — write directly) | None | Competitor pricing analysis → write directly into market-intelligence |
| **Social media pipeline / Optimus's own social** | `Optimus Inc/social-pipeline/<slug>.md` (folder **EXISTS** with README.md — write directly) | None | LinkedIn posting cadence → social-pipeline |
| **Optimus's own deployed AI agents** (drink-own-champagne instances) | `Optimus Inc/ai-agents/<tier>/<slug>.md` (folders **EXIST** for chat-assistant, voice-receptionist, marketing-team, autonomous-employee) | Mirror to corresponding `Offerings/02 AI Agents/0X/lessons/` if the lesson generalizes to all client deployments | Voice-receptionist tuning learning → write to `Optimus Inc/ai-agents/voice-receptionist/<slug>.md` + (if generalizable) bridge to offering lessons |
| **Tool reviews / new framework / new SDK** | `Optimus Academy/tools-tracking/<tool-slug>.md` (folder exists with `.gitkeep` — first population) | `optimus-system-guide.md` ONLY if adopting the tool changes vault operations; OR a Tier-3/Tier-4 `lessons/` file if the tool is an agent-framework candidate | LangGraph review → `tools-tracking/langgraph.md` + (if we adopt it) `Offerings/02 AI Agents/shared-knowledge/lessons/langgraph-adoption.md` |
| **Vault operations / Obsidian workflow / capture process** | `optimus-system-guide.md` (verified, exists at vault root — canonical operating manual per memory) | None — system-guide is the single source of truth for vault ops | New `/learn` enhancement pattern → update optimus-system-guide.md |
| **General AI news** (model release, API change, industry trend) | **No bridge — concept note only.** Most AI news is informational, not actionable. | If actionable (e.g., new Claude API feature we should adopt) → `optimus-system-guide.md` AND/OR a relevant `Offerings/02 AI Agents/0X/lessons/` file | Anthropic ships new caching feature → concept note + bridge to system-guide ("evaluate adoption") |
| **Productivity tools for Anthony's own workflow** (not Optimus offerings) | `Optimus Inc/operations/personal-stack.md` (NEW lazy-create — single file, append entries) | None | New keyboard launcher review → append entry to `personal-stack.md` |

**Default behavior when uncertain (two stop conditions):**

1. **No clear target?** → Concept note only. A bridge-without-clear-target is dead weight.
2. **No clear value vector?** → Concept note only, even if a target is plausible. Per the multi-purpose principle, every bridge MUST declare at least one of `productivity` / `overhead` / `revenue` with concrete reasoning. A bridge tagged "vector unclear" pollutes the prioritization layer.

A concept-without-bridge is still queryable via Dataview and feeds future Optimus University. The user can always add a bridge later by editing the concept's `Updates` section once both target AND value vector become clear. Prefer no bridge over a vague bridge in either dimension.

**Verification rule before any bridge writes:** the skill must `Test-Path` the named target file. If the target is an existing agent file or pattern file → the bridge's `## How to apply it` section instructs how to update that target file, but does NOT auto-edit it (human review of agent edits is mandatory per the LEDGER rule). If the target is a new file in a lazy-created folder → the skill creates the folder + writes the bridge file. Never assume target existence.

---

## Files to create / modify

### 0. Pre-execution preservation (run BEFORE sections 1-7)

These two steps run first because they establish the institutional record AND the rule that every future plan must follow the same preservation discipline.

**0a. Save the complete plan to the vault.**
- **Source:** the contents of `C:\Users\Anthony\.claude\plans\i-would-like-to-valiant-taco.md` (this file)
- **Destination:** `C:\Projects\Optimus Assets\Optimus Academy\tools\capture-pipeline-tiktok-whisper.md`
- Copy verbatim — full architecture diagram, bridge target taxonomy, multi-purpose principle, routing map, folder creation policy, fail-fast preflight checks, verification steps, and out-of-scope notes. The vault copy is the institutional record; the auto-generated plan in `C:\Users\Anthony\.claude\plans\` is ephemeral working memory.
- Naming convention: kebab-case, descriptive of value delivered (`capture-pipeline-tiktok-whisper.md`), not process (`go-into-plan-mode-graceful-karp.md`).
- The vault copy is committed in the SAME git commit as the implementation changes it describes (sections 1-7) — plan and implementation permanently linked in git history.

**0b. Add the "Plan Preservation Rule" to `CLAUDE.md`.**

Insert as a new top-level section immediately AFTER the existing `## Plan Mode Rule` section (so the two plan-related rules are co-located at the top of the file). The new section reads exactly:

```markdown
## Plan Preservation Rule
Every plan that reaches approval and execution MUST be saved to the vault folder or project folder most relevant to what it changes, BEFORE execution begins. The auto-generated plan at `C:\Users\Anthony\.claude\plans\` is Claude Code's working memory — NOT a substitute for this vault-saved copy.

**Where to save (route by primary impact):**
- Plans touching AI capture or Optimus Academy → `C:\Projects\Optimus Assets\Optimus Academy\tools\<plan-name>.md`
- Plans touching upsell architecture or AI agents → `C:\Projects\Optimus Assets\Offerings\02 AI Agents\<plan-name>.md`
- Plans touching the agent system or CLAUDE.md globally → `C:\Projects\Optimus Assets\<plan-name>.md`
- Plans touching founder vision → `C:\Projects\Optimus Assets\anthony-rosa\plans\<plan-name>.md`
- Plans touching a specific client website build → `C:\Projects\<client-folder>\.claude\plans\<plan-name>.md` (e.g., `C:\Projects\Placed-Right-Fence\.claude\plans\shop-stripe-printful-integration.md`)
- Plans touching multiple client projects or Optimus operations globally → `C:\Projects\Optimus Assets\<plan-name>.md`

**Naming convention: kebab-case, descriptive of value delivered, not process.**
- Good: `capture-pipeline-tiktok-whisper.md`
- Good: `shop-stripe-printful-wiring.md`
- Good: `hero-animation-three-layer-refactor.md`
- Bad: `go-into-plan-mode-graceful-karp.md`
- Bad: `my-opinion-on-joyful-spark.md`

**Commit policy:** the plan file is committed in the SAME git commit as the changes it describes, so plan and implementation are permanently linked in git history. A plan committed without its implementation, or implementation committed without its plan, is a process failure — flag and fix before continuing.
```

After inserting, verify CLAUDE.md still parses cleanly (no broken markdown anchors, no duplicate headings, the existing TOC implicit ordering still makes sense).

### 1. NEW: `Optimus Academy/tools/transcribe-url.py`

Python helper that takes a URL → returns JSON `{transcript, publisher, title, url, source-date, duration}`.

**Stack (all confirmed installed at plan time):**
- Python **3.11.9** via `py -3.11` launcher (Python 3.14 is broken on this machine and sits ahead of 3.11 on PATH — every Python invocation MUST use `py -3.11` explicitly, never `python` or `python3`)
- `openai-whisper` 20250625 (LOCAL transcription — no API, no key)
- `yt-dlp` 2026.3.17 (imported as Python module via `import yt_dlp`, NOT subprocessed via `yt-dlp.exe` shim)
- `ffmpeg` 8.1 (binary on PATH — yt-dlp's audio extraction depends on it)
- Whisper `base` model (already downloaded and loaded — confirmed working)

**No second API key.** The Anthropic SDK key already in the environment is the only key this system needs. Local Whisper means transcription is offline, free, and private.

**Implementation pattern:**
- Use `import yt_dlp` and `import whisper` directly — no subprocess calls. The script runs entirely in the Python 3.11 process invoked by the caller.
- yt-dlp configured with `format="bestaudio"`, audio postprocessor to extract WAV/MP3, output template to a `tempfile.mkdtemp()` directory.
- `whisper.load_model("base")` as the default — fast enough for short-form video, accurate enough for clear speech.
- `try/finally` around the temp dir so failures don't leak audio files.
- Output JSON to stdout for `/learn` to consume.

**Caller invocation (from `/learn` and from manual testing):**
```
py -3.11 "Optimus Academy/tools/transcribe-url.py" <URL>
```
Never `python transcribe-url.py`, never `python3 transcribe-url.py`, never the `yt-dlp.exe` shim. The `learn-prompt.md` skill spec must spell out the `py -3.11` invocation explicitly so a future Claude run doesn't fall back to bare `python` and hit the broken Python 3.14.

**Fail-fast preflight checks (mandatory, run BEFORE any work):**

First executable code after imports — before URL parsing, before yt-dlp invocation, before model load. Any failure prints a single clear error line to stderr and exits with a distinct non-zero code so `/learn` can route the failure cleanly:

```python
import os, sys, shutil, json, tempfile

# Preflight 1: ffmpeg must be on PATH (yt-dlp's audio extraction depends on it)
if shutil.which("ffmpeg") is None:
    print("ERROR: ffmpeg not on PATH. Install ffmpeg and ensure it's in your PATH. "
          "Windows: scoop install ffmpeg or choco install ffmpeg.", file=sys.stderr)
    sys.exit(4)  # exit code 4 = missing system binary

# Preflight 2: yt-dlp must be importable as a Python module (NOT the .exe shim)
try:
    import yt_dlp
except ImportError:
    print("ERROR: yt-dlp Python module not installed for the active Python. "
          "Run: py -3.11 -m pip install yt-dlp", file=sys.stderr)
    sys.exit(3)

# Preflight 3: openai-whisper must be importable
try:
    import whisper
except ImportError:
    print("ERROR: openai-whisper Python module not installed for the active Python. "
          "Run: py -3.11 -m pip install openai-whisper", file=sys.stderr)
    sys.exit(5)  # exit code 5 = missing whisper

# Preflight 4: Python version sanity (defensive — should already be 3.11 if invoked correctly)
if sys.version_info[:2] != (3, 11):
    print(f"ERROR: this script requires Python 3.11. Active interpreter is {sys.version_info[:2]}. "
          "Invoke via: py -3.11 \"Optimus Academy/tools/transcribe-url.py\" <URL>", file=sys.stderr)
    sys.exit(6)  # exit code 6 = wrong Python version
```

**Exit code semantics** (`/learn` skill must handle these explicitly):
- `0` — success; stdout has valid JSON `{transcript, publisher, title, url, source-date, duration}`
- `1` — runtime error during download/transcription (network failure, unsupported URL, audio extraction failed); stderr has details
- `3` — `yt-dlp` Python module missing for active Python → `/learn` tells the user: "Run `py -3.11 -m pip install yt-dlp` then re-run."
- `4` — `ffmpeg` missing → `/learn` tells the user: "Install ffmpeg (Windows: `scoop install ffmpeg` or `choco install ffmpeg`) then re-run."
- `5` — `openai-whisper` missing → `/learn` tells the user: "Run `py -3.11 -m pip install openai-whisper` then re-run."
- `6` — wrong Python version → `/learn` tells the user: "Invoke via `py -3.11`, not bare `python`."

Note: exit code `2` (used for `OPENAI_API_KEY` missing in earlier draft) is intentionally retired. No API key check exists because no API is used.

**Default model selection:** `whisper.load_model("base")`. Reasons:
- Fast enough for short-form video (TikToks, Reels, Shorts are 15-60s; base model transcribes in ~real-time on CPU, faster on GPU)
- Accurate enough for clear, conversational speech (the dominant content type Anthony captures)
- Confirmed already downloaded and working on this machine

**Upgrade path documented in script docstring (do NOT build now):** if base model accuracy is insufficient for noisy audio, technical jargon, or non-native speakers, swap to `whisper.load_model("large")` — slower (5-10× transcription time), much more accurate, requires the large model to be pre-downloaded (~3 GB). Make the model name a constant at the top of the script (`WHISPER_MODEL = "base"`) so the swap is one-line.

**Performance & cost notes:**
- Cost: $0 per transcription (local). Anthropic API key for `/learn` itself is the only paid call in the loop, and it's already in env.
- Privacy: audio never leaves the machine. Sources Anthony might not want hitting third-party APIs (private content, paywalled material) transcribe locally without exposure.
- First-run model load: ~140 MB base model held in memory after first call. Subsequent calls in the same process (none — script is one-shot) would be instant. Cold-start per-script-run is acceptable for the daily-capture cadence (1-5 sources/day).

### 2. MODIFY: `c:\Projects\Optimus Assets\learn-prompt.md`

Two additions before the existing transcript-processing flow:

**(a) URL Pattern Detection**
- Regex for tiktok.com, instagram.com/reel/, instagram.com/p/, youtube.com/shorts/, x.com/.../status/.../video, vm.tiktok.com
- **Routing rule:**
  - Match short-form video pattern → invoke `python "Optimus Academy/tools/transcribe-url.py" <URL>` → parse JSON → seed publisher/title/url/source-date/duration into the daily H2 metadata block, transcript into the body
  - Match `youtube.com/watch` → existing transcript fetch (unchanged)
  - No URL match → existing paste-text flow (unchanged)
- One worked example showing TikTok URL → daily H2 with all 7 H3 sections populated

**X (Twitter) handling rule** (one paragraph in `learn-prompt.md`):
- **Single posts:** skip. Too short to earn a concept note. If a single tweet sparks a real thought, capture the *thought* via paste-text, citing the tweet as inspiration in the source blockquote — do not capture the tweet itself.
- **Threads:** worth capturing. Use the paste-text fallback. Copy the full thread (top to bottom), paste into `/learn`, set `publisher = @handle`, `url = link to first tweet`, `source-type = thread`, `source-date = first tweet date`.
- **Embedded videos:** the URL pattern detection above already routes `x.com/.../status/.../video` through yt-dlp + Whisper. No special handling.
- This rule prevents the most common failure mode for social-media capture: fragmenting `concepts/` with single-tweet one-liners that don't deserve their own atomic note.

**(b) Bridge target classification (broaden, do not narrow)**
- Replace any phrasing in the current `learn-prompt.md` that implies bridges only target the four offerings.
- Add a "Bridge Target Selection" rule: after extracting a concept, the skill must consider all five target zones (Offerings, knowledge/patterns, knowledge/craft, Optimus Inc, tools-tracking) and create a bridge for *every* zone where the concept has concrete, actionable application — not just the first match.
- Reference the bridge target taxonomy table in this plan for examples.
- Worked examples to include directly in `learn-prompt.md`:
  1. **Sales-training TikTok** — concept: pricing anchor tactic → bridge to `knowledge/craft/copywriting/<slug>.md` AND `Offerings/01 Website Development/lessons/<slug>.md` (because every client site's pricing page benefits)
  2. **Finance YouTube** — concept: bootstrapped runway rule → bridge to `Optimus Inc/operations/<slug>.md` only
  3. **AI tool review** — concept: new agent framework features → bridge to `Optimus Academy/tools-tracking/<slug>.md` AND (if framework is a Tier-3/Tier-4 candidate) `Offerings/02 AI Agents/shared-knowledge/lessons/<slug>.md`
  4. **Marketing psychology article** — concept: cognitive bias used in CRO → bridge to `knowledge/craft/psychology/<slug>.md` AND `Offerings/01 Website Development/lessons/<slug>.md`

**(c) Forward-compat fields for future Optimus University compilation**
Extend the concept-note frontmatter template (in `learn-prompt.md`, the section that defines the mandatory 8 frontmatter fields for `concepts/<slug>.md`) with three OPTIONAL fields. Optional means: `/learn` populates them when the source makes the answer obvious; leaves them blank or omits them otherwise. Existing concepts (the 1 file currently in `concepts/`) remain valid without the fields.

```yaml
level: foundational | intermediate | advanced   # optional — pedagogical difficulty
prerequisites: ["[[../concepts/<slug>]]", ...]  # optional — concepts the learner needs first
audience: [founder, developer, marketer, client, optimus-internal]  # optional, multi-valued
```

**(d) Enrichment via web search (Step 1.5 in learn-prompt.md)** — added during execution after user feedback (DialogueDB scenario): a 15-second TikTok mentioning a tool is real signal but the source itself can't fill out Mechanics / Examples / Gotchas. Auto-trigger conditions: source duration < 60s OR transcript word count < 200 OR source mentions a named tool/framework not yet in `concepts/` OR borderline scan-and-decide case. Auto-skip for: long-form sources (YouTube > 5 min, articles > 1000 words), HIGH-MATCH existing concepts, or `--no-enrich` flag. Procedure: 2-3 WebSearch queries (`<topic> documentation`, `<topic> review`, `<topic> when to use`), top 3-5 WebFetch results, synthesize into Mechanics/Examples/Gotchas. **Source attribution split is non-negotiable**: daily file's H2 credits ONLY the original source (the TikTok); concept's frontmatter gets a NEW `enriched-from:` field listing enrichment URLs. Concept gets `#learning/enriched` tag in addition to `#learning/synthesized`. This keeps "show me everything I learned from creator X" queries clean while still augmenting concept depth.

**(e) Within-concept dedup at append time** — added during execution after user feedback (variations are NEW info, not duplicates): the APPEND path now includes an information-delta check that ONLY blocks identical/near-verbatim repetition. Variations always pass (new angle on a known principle, new example, new gotcha, new mechanism, contradictory data). Block only when the new source says the same thing already in the concept with merely different wording. When in doubt, append — false-restate is recoverable, false-suppress loses information permanently. The `source-references:` list always grows with the new daily-anchor (concept tracks every source that taught it), independent of whether the body gets a new `## Updates` block. Same dedup rule applies to bridge APPEND.

**(f) Bridge value-vector field — MANDATORY** (per multi-purpose principle): every bridge declares `value-vector: [productivity | overhead | revenue]` (multi-valued, at least one) plus optional `expected-impact: small | medium | large`. Every bridge also gains a new mandatory `## Value vector reasoning` section showing concrete mechanism per tagged vector. Value-vector merge rule on APPEND: a new source can ADD vectors to an existing bridge (`[productivity]` → `[productivity, revenue]` if a later source reveals a revenue mechanism); never remove vectors during APPEND.

**Rationale (kept short in `learn-prompt.md` to avoid bloat):** these fields turn the concepts library into a Dataview-queryable course substrate. Future Optimus University compilation becomes a query (`"foundational copywriting concepts targeting founder audience, ordered by prerequisite depth"`) rather than a re-tagging exercise across hundreds of files. Adding the fields after the substrate accumulates is 10× the cost of adding them at capture time.

Decision rule for `/learn` when populating these fields:
- `level`: if the source explicitly teaches a primitive ("what is anchoring") → `foundational`. If it builds on assumed primitives ("how anchoring interacts with loss aversion in 3-tier pricing") → `advanced`. Default `intermediate` when ambiguous.
- `prerequisites`: only fill when the source explicitly references another concept that already exists in `concepts/`. Do NOT invent prerequisites the source doesn't reference.
- `audience`: multi-valued. If a copywriting tactic is universally useful → `[founder, marketer]`. If it's a developer-only Next.js pattern → `[developer]`. If unsure → omit. Better blank than wrong.

Keep all existing sections intact. The 7-H3 daily-file structure, the scan-and-decide concept dedup, the status lifecycle, and the dedup heuristics do not change. The 8 mandatory frontmatter fields stay mandatory; these three are *additional* and optional.

### 3. NEW: `Optimus Academy/weekly-review.md`

A single file (not dated; rolling). Built around the multi-purpose principle: prioritization is **value-vector-first, age-second** — not the reverse. Anthony's review time is finite and should be spent on the highest-leverage bridges, not the oldest.

Five stacked Dataview blocks, in this order:

1. **🟢 Revenue bridges** (top of file) — every bridge with `status` in `[not-started, in-progress]` AND `value-vector` contains `revenue`, sorted by `expected-impact: large → medium → small → unset`, then by `created` ascending. Columns: bridge title, concept, target file, expected-impact, age, status. Revenue is the highest-leverage vector; it goes first.
2. **🟡 Productivity bridges** — same filter, `value-vector` contains `productivity`. Same sort. Productivity is force-multiplier — every applied productivity bridge compounds across future builds.
3. **🔵 Overhead bridges** — same filter, `value-vector` contains `overhead`. Same sort. Overhead reduction is real but quieter; reviewed last among active vectors.
4. **🟣 Applied → awaiting promotion** — bridges with `status: applied`, sorted by `last-updated` descending. These are candidates to promote to `lessons/`, `knowledge/patterns/`, or `knowledge/craft/`. Columns: bridge title, target zone, value-vector, last-updated.
5. **⚫ Abandonment candidates** — bridges with `status: not-started` AND `created > 30 days ago`. Anthony decides per row: bump to in-progress, abandon, or keep aging. Columns: bridge title, value-vector, age, why-it-applies (first sentence). Surfacing aging items keeps the queue honest.

Bridges tagged with multiple vectors appear in each relevant block (deliberate duplication — a bridge serving both `revenue` and `productivity` is reviewed twice, which is correct because it's higher-leverage than single-vector bridges).

Brief instruction header at top of file: "Dataview re-runs on open. Review revenue first, productivity second, overhead third. Promote applied bridges. Abandon anything aged 30+ days with no traction."

Why a single rolling file: matches the existing pattern (one `weekly-review.md`, regenerated by Dataview on open). No script needed; Obsidian re-runs the query every time the file opens. Anthony reviews when he wants; nothing auto-promotes; the prioritization is built into the block ordering.

### 4. MODIFY: `Optimus Academy/README.md` AND `Optimus Academy/apply-to-optimus/README.md`

**Academy README:** Add one section: "Input Pathways" — documents that `/learn` accepts: TikTok/IG/Reels/Shorts URLs (via yt-dlp + LOCAL whisper, no API), YouTube long-form URLs (existing), article URLs or text (existing), "Other" via direct paste with manual metadata. Link to `tools/transcribe-url.py` and `weekly-review.md`. Document that the script must be invoked via `py -3.11`, never bare `python` (Python 3.14 is broken on this machine and sits ahead on PATH).

**Apply-to-optimus README:** Replace the implicit four-offering scoping with the explicit five-zone bridge-target taxonomy from this plan's Architecture section. Show one worked example bridge per zone (Offerings, knowledge/patterns, knowledge/craft, Optimus Inc, tools-tracking) with the concrete frontmatter and target wikilink, so future runs of `/learn` (and humans editing bridges manually) have a copy-paste reference.

### 5. MODIFY: `c:\Projects\Optimus Assets\CLAUDE.md`

Under **Vault Organization → Optimus Academy** section, add two bullets:
- "**Input pathways:** `/learn` accepts TikTok/IG/Reels URLs (auto-downloads via yt-dlp + transcribes via LOCAL openai-whisper — no API key, no cost), YouTube URLs, article URLs/text, and pasted text. The transcribe script MUST be invoked via `py -3.11` (Python 3.14 is broken; bare `python` will fail). No `OPENAI_API_KEY` required."
- "**Topic scope is broad, not AI-only.** `/learn` captures any source whose value applies somewhere — sales training, copywriting, marketing psychology, finance, design, productivity tools. Bridges route to one of five zones per the bridge-target taxonomy in `Optimus Academy/apply-to-optimus/README.md`."

No changes to any other CLAUDE.md rules. The Pre-Read Protocol, the Knowledge Base Rule, the Memory Search Protocol all keep working.

### 6. MODIFY: `00 — Empire Index/tag-schema.md`

The current `#applies-to/*` family covers website-dev and AI offerings only. The current `domain:` vocab is heavily AI-skewed. Both need extension to absorb the broader topic scope (sales, copywriting, psychology, finance, design, productivity tools).

**Extend `#applies-to/*` family** (additive — existing tags unchanged):
- Existing: `#applies-to/website-dev`, `#applies-to/ai-agents`, `#applies-to/ai-agents/{chat,voice,marketing}`
- Add:
  - `#applies-to/craft/copywriting`
  - `#applies-to/craft/psychology`
  - `#applies-to/craft/sales`
  - `#applies-to/craft/design`
  - `#applies-to/optimus-inc/finance`
  - `#applies-to/optimus-inc/marketing` (Optimus's own marketing, distinct from Marketing-Team offering)
  - `#applies-to/optimus-inc/operations`
  - `#applies-to/optimus-inc/brand`
  - `#applies-to/tools/<tool-slug>` (tool-evaluation captures)

**Extend `domain:` vocabulary** (additive):
- Existing: claude-api, agents, prompt-engineering, obsidian, evals, tooling, voice, marketing, web-dev, automation, business
- Add: copywriting, sales, psychology, finance, design, productivity, hiring, brand

The `source-type::` Dataview field already supports `video / article / podcast / course / book / paper` — no change needed there.

### 7. Folder creation policy (per-zone, explicit)

Three different states across the five target zones — the `/learn` skill must check before writing:

| Target zone | Current folder state | Skill behavior on first bridge |
|---|---|---|
| `Offerings/<offering>/` and its `lessons/`, `shared-knowledge/lessons/` | All exist | Write file directly |
| `knowledge/patterns/` | Exists, populated | Write file directly |
| `knowledge/craft/<area>/` | **Does NOT exist** for any `<area>` | `mkdir -p` then write file. No `.gitkeep` needed once a real file lands |
| `Optimus Inc/<area>/` | **Verify per-area** at write time. Some Optimus Inc subfolders exist (marketing, brand, market-intelligence per CLAUDE.md), `operations/` and `finance/` likely do not | If folder missing → `mkdir -p` then write file. If present → write directly |
| `Optimus Academy/tools-tracking/` | **Folder exists with `.gitkeep`** — populated for the first time | Write `<tool-slug>.md` directly into the existing folder. After first real file lands, the `.gitkeep` may be deleted in the same commit (optional cleanup, not required) |

**Implementation rule for `learn-prompt.md`:** before writing any bridge file, the skill calls (or instructs Claude to use Bash to call) `Test-Path <target-folder>` (PowerShell) or equivalent. If the parent folder is missing → create it via `mkdir -p` (or `New-Item -ItemType Directory -Force`). Never assume existence. Never scaffold empty folders preemptively.

Add a one-line note in `Optimus Academy/README.md` linking to this folder creation policy, so anyone (human or agent) running `/learn` knows the rule.

---

## Reused, unchanged

- `/learn` skill's existing transcript-processing flow (440 lines — keep intact)
- Daily file 7-H3 structure, scan-and-decide dedup, bridge lifecycle
- Tag schema, domain vocab, source-type field
- All git-commit-and-push behavior at end of `/learn`
- Apply-to-optimus README and bridge schema

---

## Verification

End-to-end test before declaring complete. The test scenarios below mirror the worked examples added to `learn-prompt.md` so verification proves the broadened bridge routing actually works in practice — not just on paper.

**0. Plan preservation verification (precedes all functional tests).**
- `Test-Path "C:\Projects\Optimus Assets\Optimus Academy\tools\capture-pipeline-tiktok-whisper.md"` returns `True`.
- File size > 10 KB (full plan content, not truncated).
- `Select-String -Path "C:\Projects\Optimus Assets\CLAUDE.md" -Pattern "## Plan Preservation Rule"` returns one match positioned AFTER the existing `## Plan Mode Rule` section.
- `git status` shows both files staged together with the implementation changes (sections 1-7) — single atomic commit, plan and implementation linked permanently in git history.

1. **TikTok happy path (sales-training source)** — Run `/learn` against a real sales-training TikTok. Verify:
   - Audio downloaded silently (no terminal noise leaking the source)
   - Transcript JSON returned with all 6 fields populated
   - Daily H2 section appears in today's daily file with all 7 H3 sections (Summary, Key Concepts Extracted, Detailed Notes, Code & Examples, Notable Quotes, Action Items, Open Questions) populated
   - Inline Dataview metadata (`publisher::`, `source-type::`, `url::`, `source-date::`, `captured::`, `duration::`, `domain::` set to `sales` or `copywriting`) all present and correct
   - Concept created or updated via scan-and-decide
   - **Bridge target verification:** at least one bridge created with `applies-to:` pointing to `knowledge/craft/copywriting/<slug>.md` (lazy-folder-create works) or `Offerings/01 Website Development/lessons/<slug>.md`. NOT defaulted to an AI-agent offering.

2. **YouTube regression (finance source)** — Run `/learn https://www.youtube.com/watch?v=<id>` against a real finance/business video. Verify the existing transcript-fetch path is unbroken AND the bridge lands in `Optimus Inc/operations/` or `Optimus Inc/finance/`, NOT in any offering folder.

3. **Pasted-text fallback (psychology article)** — Run `/learn` with a copy-pasted marketing-psychology article body. Verify the no-URL path still works AND the bridge lands in `knowledge/craft/psychology/<slug>.md`. Bonus check: a second bridge to `Offerings/01 Website Development/lessons/` if the principle clearly applies to client-site CRO.

3a. **Tool-review source** — Run `/learn` against a TikTok or article reviewing a new AI agent framework. Verify the bridge lands as `Optimus Academy/tools-tracking/<tool-slug>.md` written into the **already-existing folder** (no `mkdir` should fire — folder is present with `.gitkeep`). After the first real file lands, optionally delete `tools-tracking/.gitkeep` in the same commit. This scenario tests "write directly into existing-but-empty folder," distinct from the lazy-create scenarios in tests 1 and 3.

3b. **Lazy-create scenario (separate from 3a)** — One of tests 1 or 3 must hit a previously-nonexistent folder (`knowledge/craft/copywriting/` or `knowledge/craft/psychology/`). Verify `/learn` (or the orchestrator) created the folder via `mkdir -p` before writing the bridge file, and that no empty `.gitkeep` was added (a real bridge file makes a placeholder unnecessary).

4. **Weekly review render** — Open `Optimus Academy/weekly-review.md` in Obsidian. Verify both Dataview blocks render. Manually create a dummy bridge with `status: not-started` to confirm it appears in the list.

5. **Audit:** grep `Optimus Academy/` for any orphaned audio temp files (`.mp3`, `.m4a`, `.webm`). The transcribe script must clean up after itself.

6. **Cost check:** N/A — local Whisper, zero per-transcription cost. The only spend is on `/learn`'s own Anthropic API call (existing, unchanged). Verify no `OPENAI_API_KEY` reads in the codebase: `grep -r "OPENAI_API_KEY" "Optimus Academy/" learn-prompt.md` should return zero hits.

7. **Git push verification** — confirm the daily-file commit lands on remote per the existing `/learn` push behavior. Do not skip; this is part of how Anthony's workflow stays auditable.

---

## Out of scope (intentionally deferred)

- **Microphone capture** — User explicitly chose URL-paste. If a podcast or livestream surfaces a need, revisit then.
- **Autonomous review agent** — User chose the manual Dataview surface. The bridge is a candidate for a Tier-3 Marketing Team capability (autonomous note synthesis + recommendation) once that offering ships.
- **Larger Whisper model upgrade** — Local `base` model is the default and ships now. If accuracy proves insufficient for noisy audio, technical jargon, or non-native speakers, swap `WHISPER_MODEL = "base"` → `"large"` (one-line change). Pre-download required (~3 GB). Move only if base produces transcripts requiring manual cleanup more than once per week.
- **TikTok/IG paywalled or private content** — yt-dlp may need cookies for some sources. Document cookie-export instructions in the helper script's docstring; do not build a credential manager.
- **`apply-to-optimus` autopilot promotion** — Verified bridges stay manually promoted to `lessons/` or `knowledge/patterns/`. The bar to automate this is `verified` status reliably mapping to a quantified improvement metric, which doesn't exist yet.
- **Optimus University course compilation** — The concept library is a course substrate, not a course. The three forward-compat frontmatter fields (`level`, `prerequisites`, `audience`) are added at capture time so future-University doesn't need a retroactive tagging pass. Course design itself (modules, assessments, retention loops, learner persona modeling, decision on whether University is a paid product / outbound marketing / internal training) is a separate phase. Build the substrate first, run `/learn` for ~6 months until critical mass, then commit to one University strategy with substrate to test against.

---

## Critical files reference

| Path | Why |
|------|-----|
| `c:\Projects\Optimus Assets\Optimus Academy\tools\capture-pipeline-tiktok-whisper.md` | **NEW (Section 0a)** — vault-preserved copy of this plan, committed with the implementation |
| `c:\Projects\Optimus Assets\CLAUDE.md` | **MODIFY (Section 0b)** — insert Plan Preservation Rule after Plan Mode Rule, plus the two existing bullets under Vault Organization (Section 5) |
| `c:\Projects\Optimus Assets\learn-prompt.md` | **MODIFY** — URL detection + bridge target classification |
| `c:\Projects\Optimus Assets\Optimus Academy\tools\transcribe-url.py` | **NEW** — yt-dlp + local Whisper pipeline (py -3.11) |
| `c:\Projects\Optimus Assets\Optimus Academy\weekly-review.md` | **NEW** — Dataview-powered review surface |
| `c:\Projects\Optimus Assets\Optimus Academy\README.md` | **MODIFY** — Input pathways section |
| `c:\Projects\Optimus Assets\Optimus Academy\apply-to-optimus\README.md` | **MODIFY** — Five-zone bridge target taxonomy + worked examples |
| `c:\Projects\Optimus Assets\00 — Empire Index\tag-schema.md` | **MODIFY** — Extend `#applies-to/*` family + `domain:` vocab |
| `c:\Projects\Optimus Assets\CLAUDE.md` | **MODIFY** — Two bullets under Vault Organization → Optimus Academy |
| `c:\Projects\Optimus Assets\Optimus Academy\daily\YYYY-MM-DD.md` | Output target — H2 schema fixed, do not change |
| `c:\Projects\Optimus Assets\Optimus Academy\concepts\<slug>.md` | Output target — dedup logic stays in `learn-prompt.md`, do not duplicate |
| `knowledge/craft/<area>/`, `Optimus Inc/<area>/` | **LAZY-CREATE** — folders materialize on first bridge target |
