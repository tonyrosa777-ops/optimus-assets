---
title: Weekly Bridge Review
schema-version: 1
tags: [#learning/review]
---

# Weekly Bridge Review

> **Dataview re-runs on open.** Review revenue first, productivity second, overhead third. Promote applied bridges. Abandon anything aged 30+ days with no traction.
>
> **Multi-purpose principle:** every bridge declares one or more `value-vector` tags. Bridges serving multiple vectors appear in multiple blocks below — that duplication signals higher leverage, not noise.
>
> **What to do here:** scan top-down. For each row, decide: bump status (`not-started` → `in-progress` → `applied` → `verified`), edit the bridge file directly, or abandon (delete the bridge file; the concept note stays).

---

## 🟢 Revenue bridges — work first

Active bridges (`not-started` or `in-progress`) tagged `revenue`. Sorted by `expected-impact` (large → medium → small → unset), then by `created` ascending (oldest first within impact tier).

```dataviewjs
const rows = dv.pages('"Optimus Academy/apply-to-optimus"')
  .where(p => (p.status === "not-started" || p.status === "in-progress")
              && p["value-vector"]
              && p["value-vector"].includes("revenue"))
  .map(p => {
    const impactRank = { large: 0, medium: 1, small: 2 };
    const r = p["expected-impact"] in impactRank ? impactRank[p["expected-impact"]] : 3;
    const ageDays = p.created ? Math.floor((Date.now() - new Date(p.created).getTime()) / 86400000) : null;
    return [p.file.link, p.concept, p["applies-to"], p["expected-impact"] || "—", ageDays === null ? "—" : ageDays + "d", p.status, r, p.created];
  })
  .sort(row => row[6] * 1e9 + (row[7] ? new Date(row[7]).getTime() / 86400000 : 0));

dv.table(["Bridge", "Concept", "Target", "Impact", "Age", "Status"], rows.map(r => r.slice(0, 6)));
```

---

## 🟡 Productivity bridges — work second

Active bridges tagged `productivity`. Same sort. Productivity is the force-multiplier vector — every applied productivity bridge compounds across all future builds.

```dataviewjs
const rows = dv.pages('"Optimus Academy/apply-to-optimus"')
  .where(p => (p.status === "not-started" || p.status === "in-progress")
              && p["value-vector"]
              && p["value-vector"].includes("productivity"))
  .map(p => {
    const impactRank = { large: 0, medium: 1, small: 2 };
    const r = p["expected-impact"] in impactRank ? impactRank[p["expected-impact"]] : 3;
    const ageDays = p.created ? Math.floor((Date.now() - new Date(p.created).getTime()) / 86400000) : null;
    return [p.file.link, p.concept, p["applies-to"], p["expected-impact"] || "—", ageDays === null ? "—" : ageDays + "d", p.status, r, p.created];
  })
  .sort(row => row[6] * 1e9 + (row[7] ? new Date(row[7]).getTime() / 86400000 : 0));

dv.table(["Bridge", "Concept", "Target", "Impact", "Age", "Status"], rows.map(r => r.slice(0, 6)));
```

---

## 🔵 Overhead bridges — work third

Active bridges tagged `overhead`. Same sort. Overhead reduction is real but quieter — reviewed last among active vectors so high-leverage revenue/productivity work gets attention first.

```dataviewjs
const rows = dv.pages('"Optimus Academy/apply-to-optimus"')
  .where(p => (p.status === "not-started" || p.status === "in-progress")
              && p["value-vector"]
              && p["value-vector"].includes("overhead"))
  .map(p => {
    const impactRank = { large: 0, medium: 1, small: 2 };
    const r = p["expected-impact"] in impactRank ? impactRank[p["expected-impact"]] : 3;
    const ageDays = p.created ? Math.floor((Date.now() - new Date(p.created).getTime()) / 86400000) : null;
    return [p.file.link, p.concept, p["applies-to"], p["expected-impact"] || "—", ageDays === null ? "—" : ageDays + "d", p.status, r, p.created];
  })
  .sort(row => row[6] * 1e9 + (row[7] ? new Date(row[7]).getTime() / 86400000 : 0));

dv.table(["Bridge", "Concept", "Target", "Impact", "Age", "Status"], rows.map(r => r.slice(0, 6)));
```

---

## 🟣 Applied → awaiting promotion

Bridges with `status: applied` — the change shipped, now waiting to be verified or promoted. Promote candidates: institutional patterns get moved to `lessons/`, `knowledge/patterns/`, or `knowledge/craft/<area>/` so they become reusable assets across projects, not just one-off applications.

```dataviewjs
const rows = dv.pages('"Optimus Academy/apply-to-optimus"')
  .where(p => p.status === "applied")
  .map(p => {
    const lastUpdated = p["last-updated"] || p.created;
    return [p.file.link, p["applies-to"], p["value-vector"] ? p["value-vector"].join(", ") : "—", lastUpdated, lastUpdated ? new Date(lastUpdated).getTime() : 0];
  })
  .sort(row => -row[4]);

dv.table(["Bridge", "Target", "Vectors", "Last updated"], rows.map(r => r.slice(0, 4)));
```

---

## ⚫ Abandonment candidates — aged 30+ days, still not started

Bridges that have sat in `not-started` for over 30 days. Decide per row: bump to `in-progress` (commit to do it now), abandon (delete the bridge file — the concept note stays), or keep aging if the application context isn't ready yet. Surfacing aging items keeps the queue honest.

```dataviewjs
const cutoff = Date.now() - 30 * 86400000;
const rows = dv.pages('"Optimus Academy/apply-to-optimus"')
  .where(p => p.status === "not-started"
              && p.created
              && new Date(p.created).getTime() < cutoff)
  .map(p => {
    const ageDays = Math.floor((Date.now() - new Date(p.created).getTime()) / 86400000);
    const vectors = p["value-vector"] ? p["value-vector"].join(", ") : "—";
    return [p.file.link, vectors, ageDays + "d", p["applies-to"], ageDays];
  })
  .sort(row => -row[4]);

dv.table(["Bridge", "Vectors", "Age", "Target"], rows.map(r => r.slice(0, 4)));
```

---

## Notes

- **Empty blocks are normal early on.** When the bridge folder has fewer than ~20 entries, several blocks may show no rows. Keep the file as-is; rows populate as `/learn` accumulates bridges.
- **Multi-vector duplication is intentional.** A bridge tagged `[productivity, revenue]` appears in BOTH the 🟢 and 🟡 blocks. That duplication is the signal: it's a higher-leverage bridge than a single-vector one.
- **No autonomous promotion.** Status bumps are manual decisions. The 🟣 block surfaces candidates; you decide which ones earn institutional-pattern status.
- **The concept layer is separate.** This file reviews bridges only. Browse `concepts/` directly for the teaching-artifact layer (which is also the future Optimus University substrate).
