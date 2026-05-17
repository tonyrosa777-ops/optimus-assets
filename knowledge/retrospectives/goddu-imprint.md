# Goddu Imprint — Project Retrospective
**Type:** B2B promotional products distributor (branded apparel, high-volume pens, executive gifts, marketing production)
**Location:** Salem, NH (serves within 1-hour radius across NH + northern MA)
**Tier:** Pro ($3,000) — closed at end of demo
**Completed:** 2026-05-17 (Phase 1 complete; Phase 2 launch + close pending)
**Build sessions:** ~6 sessions across 2 days (Phase 0 May 16, Phase 1 Stages 1A-1J May 16-17)

---

## What Went Well

- **Phase 1 sweep cleared in single-day session** — Stages 1A through 1J completed on 2026-05-17 after Phase 0 + Stages 1A-1H landed 2026-05-16. 11 commits, 77 prerendered routes, zero console errors at all breakpoints, AEO 100% (9 of 9 blog articles open with direct first-paragraph answers).
- **Stage 1B Absolute-Rule Cross-Check (Pattern #58) caught real violations on first design-synthesizer pass** — 36-testimonial mandate was set to "No (yet)" and Pricing page rows were ambiguous. Second pass fixed both. The cross-check pattern earned its slot.
- **Stage 1A repo-scan finding paid off in Stage 1D** — JCM-Graphics adaptation (Pattern #36 chaos→convergence→explosion) shipped clean with reduced particle count (EMBER 38/20, SAMPLE 200). Zero animation re-iterations.
- **Optimus-only lenses (absolute-rules + design-system) returned 0 findings across all 3 /optimus-review runs** — empirical proof that Stages 1B + 1H + 1I cleaned the Optimus-specific concerns thoroughly.
- **Built `/optimus-review` skill end-to-end during the same session it was first needed** — Stage 1J originally specced `/ultrareview` but the tool was unavailable in VSCode extension and gated at 3 lifetime free runs. Local replacement built in ~4 hours including smoke test, then immediately used to clear Goddu Stage 1J.
- **3-run iterate-to-clean review caught 10 real BUGs** that file-level audit (Stage 1H) and browser audit (Stage 1I) both passed. Run-2 specifically caught 3 NEW BUGs from run-1's fix commit — proof the verification pass works on second-order bugs.

---

## What Didn't

| # | Gap | Fix Applied |
|---|-----|-------------|
| 1 | `/ultrareview` not available in VSCode extension; 3-lifetime-run quota + $5–$20 per run after — bad mission fit for per-client scaling | Built `/optimus-review` local skill replacing the gate (commits `5427c3c` + agents) |
| 2 | Stage 1H pre-launch-auditor SECTION 4 (Forms) checked "route exists + has email send" but did NOT check API security: rate limit, validation, sanitization, Origin allowlist, honeypot. 5 security BUGs in `/api/contact` slipped past 1H and 1I. | Stage 1J `/optimus-review` caught all 5; fixed in commit `ef6ac5a` |
| 3 | `replace_all=true` on GodduCanvas BUG-5 fix silently missed PNG-onload branch (different indentation) — latent bug invariant violation | Caught by `/optimus-review` run-2 verifier; explicit Edit on the missed site in `467ef0b` |
| 4 | First `/api/contact` hardening's `isAllowedOrigin()` accepted empty Origin/Referer (waved non-browser clients through) — half-shipped defense | Caught by `/optimus-review` run-2; tightened to reject empty in `467ef0b` |
| 5 | Honeypot field server-side check shipped without corresponding client-side hidden input — dead code defense | Caught by `/optimus-review` run-2; added client-side hidden input + schema entry + default value in `467ef0b` |
| 6 | BookingPreview static-imported BookingCalendar (+ framer-motion + react-hook-form + zod ≈100KB+ gz) into homepage initial bundle for below-fold section 11 of 12 | Caught by `/optimus-review` run-1 performance specialist; converted to `dynamic({ ssr: false })` with branded loading skeleton in `ef6ac5a` |
| 7 | GodduCanvas rAF rescheduled at 60Hz forever when parent was `hidden lg:block` on mobile — wasted main thread + battery + threatened Lighthouse ≥ 90 | Caught by `/optimus-review` run-1 performance specialist; added `loopActive` invariant + visibility guard in `ef6ac5a` (then completed in `467ef0b`) |
| 8 | Sequential awaits in `/api/contact` coupled owner notification success to auto-reply success — flaky auto-reply would 502 a successful owner notification | Refactored to independent try/catch blocks in `ef6ac5a` |
| 9 | No server-side email format validation in `/api/contact` — silently broke documented Pattern #44 (replyTo discipline) for any malformed email | Subsumed by Zod schema `email: z.string().email().max(254)` in `ef6ac5a` |
| 10 | CRLF injection vector in `/api/contact` — user `name`/`company`/`source` fields interpolated into email subject with only `.trim()` | Added `stripControlChars()` sanitizer applied to every field before interpolation in `ef6ac5a` |
| 11 | Branded-domain phishing relay: `/api/contact` auto-reply sent FROM verified `noreply@godduimprint.com` TO attacker-controlled email with attacker-controlled name in greeting | Added `safeName()` (alphanumeric + apostrophe + hyphen + period only) before interpolation; kept auto-reply but hardened it in `ef6ac5a` |
| 12 | Initial supporting-doc sweep after `/ultrareview` → `/optimus-review` entry-point swap was incomplete — 11 vault files + 7 Goddu files still operatively referenced `/ultrareview` | User asked "is it replaced everywhere it applies?" — honest audit revealed gap; full sweep applied in `73c89ff` (vault) + `1dea5dd` (Goddu) |
| 13 | Stale `project-prime.md` at Goddu repo root — Phase 0 leftover that diverged from the canonical `.claude/commands/prime.md` (62KB stale vs 64KB current) | Deleted in `1dea5dd` |

---

## Tools Introduced This Build

- **`/optimus-review`** — local multi-agent code review skill at `~/.claude/skills/optimus-review/`. 8 parallel Sonnet 4.6 specialists (correctness, security, architecture, tests, performance, style + Optimus-only absolute-rules and design-system) + 1 Opus 4.7 verifier. Replaces `/ultrareview` at Stage 1J. Unlimited reruns, ~$1–4 per run. See [[../../optimus-review-skill.md]] for full architecture.
- **Stage 1J handoff token renamed** — `HANDOFF-TO-ULTRAREVIEW` → `HANDOFF-TO-STAGE-1J` (tool-agnostic) across pre-launch-auditor.md output template + agent's Output schema. Surviving future tool changes.
- **In-memory rate limiter for API routes** — Map<ip, RateRecord>-based, 5/IP/10min window, opportunistic cleanup. First applied to `/api/contact`. Pattern generalizes to every public form route.
- **Honeypot pattern with paired client+server halves** — `website: z.string().max(0).optional()` in schema + visually-hidden input in form + server-side silent-200 if filled. First applied to ContactClient.tsx + `/api/contact`.

---

## Changes Made to Toolkit

- **`project-prime.md` Stage 1J section** rewritten in BOTH the vault master AND Goddu's local `.claude/commands/prime.md` — `/ultrareview` invocation replaced with `/optimus-review`, cost/quota/CLI-availability graceful-degradation blocks removed, fix-owner map preserved (commits `b163f33` vault + `5427c3c` Goddu).
- **Vault sweep** — 8 supporting docs updated to reference `/optimus-review` and the renamed `stage-1j-pre-launch-gate.md` pattern: pre-launch-auditor.md SECTION 12 + HANDOFF templates, build-checklist.md, website-build-template.md, end-to-end-workflow.md, CLAUDE.md, opus-4-7-prompt-tuning.md cross-reference (commit `73c89ff`).
- **`knowledge/patterns/ultrareview-as-pre-launch-gate.md` deleted, replaced with `stage-1j-pre-launch-gate.md`** — tool-agnostic filename. Content rewritten to describe the **gate** (Stage 1J) rather than the **tool** (`/optimus-review`). Surviving future tool changes.
- **Plan file `optimus-review-skill.md`** committed at vault root with EXECUTED status + smoke test results + lessons learned (commit `b163f33`).
- **Goddu repo sweep** — CLAUDE.md, website-build-template.md, pre-launch-audit.md (stale HANDOFF block → resolved state), progress.md (older forecast line), deleted stale Phase 0 `project-prime.md` root copy (commit `1dea5dd`).
- **4 new error entries + 6 new pattern entries** logged to `knowledge/errors/` and `knowledge/patterns/` via /retro this session — see Workflow Improvements Implemented table in build-log.md.

---

## Outstanding for Phase 2

- Calendly URL (BookingCalendar runs in seeded demo until Steve provides — Pattern #69 seeded demo-mode active)
- Brand-partner permissions for logo grid (Carhartt, Nike, North Face, etc.)
- Past-client permissions (Phonak, CenturyLink, JetBlue, Yahoo)
- Steve photoshoot (placeholder on /about + AboutTeaser sections)
- 30+ real testimonials (current 36 drafted in target-persona voice per Stage 1E spec)
- Service-area copy review for 37 cities
- Resend account + DNS + Vercel env vars
- Domain registrar ownership confirmation (godduimprint.com)
- DESIGN-tier hardening from `/optimus-review`: replace in-memory rate limiter with Upstash Ratelimit + KV, add CAPTCHA (Cloudflare Turnstile or hCaptcha), defer test framework decision
