---
title: Trading Bot — Personal Revenue Project
schema-version: 1
domain: business
created: 2026-05-08
last-updated: 2026-05-08
tags: [#owner/anthony-rosa, #layer/optimus-os, #status/draft]
---

# Trading Bot — Personal Revenue Project

Personal automated trading bot. **Mission-orthogonal to Optimus** — different audience, different skillset, different brand, different regulatory surface (capital loss risk, possible securities/CFTC angles depending on structure). Stays a personal project under Anthony's name until validation gates clear.

## Status

`draft` — concept stage, no live capital deployed. This file exists to scaffold the project and declare the gates so the conviction → validation path is explicit.

## Project goal

> *Stub.* Populate when committing to a specific approach.

Suggested skeleton:
- **What's being traded.** Crypto only? Crypto + futures? Stocks via API? Decision drives regulatory surface significantly.
- **Strategy class.** Trend-following, mean-reversion, statistical arbitrage, sentiment-driven, market-making — pick one, stick to it through validation. Strategy mixing is post-validation.
- **Capital sizing rule.** What % of net worth lives in the bot at any given time. What's the max drawdown that triggers shutdown.
- **AI angle.** What does the AI add — signal generation, position sizing, risk management, regime detection? Specifically NOT "AI picks stocks" magic — the AI augments a defined strategy with a defined edge.

## Mission-orthogonality note (load-bearing)

This project does NOT fit Optimus's mission ("newest tech for SMBs at affordable prices"). Optimus sells productized AI services to small businesses. A trading bot is personal capital deployment in financial markets — different audience, different brand, different liability. **Even if validated, this project may NEVER graduate to an Optimus offering.** Productization is optional, not the goal. The goal is automated personal income.

If it ever DOES productize, the audience is likely HNW individuals or accredited investors, not Optimus's SMB ICP. That's a different business under a different brand. The graduation pattern below acknowledges this — gate 3 is explicitly optional, not the natural endpoint.

## Graduation gates

Per `[[README]]` graduation gates pattern:

- **Gate 1 — Side project → Revenue stream.** Bot runs on real capital (not paper) for 3+ consecutive months AND survives at least one drawdown without manual intervention. Suggested capital floor: small enough that 100% loss doesn't materially affect life; large enough that results are economically meaningful (not toy-position-only). Drawdown survival is non-negotiable — up months don't validate; down months survived do.
- **Gate 2 — Revenue stream → Productizable.** The bot's strategy and stack are documented well enough that a second instance could be deployed (paper-traded) by someone who understands the strategy. Re-deployability proves it's a system, not a happy accident.
- **Gate 3 — Productizable → Standalone product (NOT necessarily Optimus offering).** This gate is OPTIONAL. If pursued, it's likely as a separate brand serving HNW/accredited investors, with appropriate licensing, disclosures, and regulatory structure. Most likely outcome: this project stays personal and never graduates beyond Gate 2. That's fine. The point was automated personal income, not building another product company.

## Risk discipline

- **Drawdown threshold.** Pre-declare the % drawdown that triggers shutdown + post-mortem before any capital goes live. Without a pre-declared threshold, drawdowns rationalize their way into "just one more day" disasters.
- **Capital cap.** Pre-declare the max position size as % of net worth. Don't expand mid-validation just because a few months went well.
- **Regulatory check-in.** Before deploying real capital, confirm the structure (personal LLC? sole prop? Anthony's name?) doesn't accidentally trip securities or CFTC requirements. Cheap to ask in advance, expensive to learn the hard way.

## Updates

> Append-only. Each entry: `### YYYY-MM-DD — <label>`.
