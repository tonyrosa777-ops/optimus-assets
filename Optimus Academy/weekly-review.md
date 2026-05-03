---
title: Weekly Bridge Review
schema-version: 1
tags: [#learning/review]
---

# Weekly Bridge Review

> **Dataview re-runs on open.** Review revenue first, productivity second, overhead third. Promote applied bridges. Abandon anything aged 30+ days with no traction.
>
> **Bridge model (post 2026-05-03 restructure):** one bridge file per concept, multiple `## Applied to <Target>` H2 sections inside per application. Per-application metadata (`applies-to`, `status`, `value-vector`, `expected-impact`) is declared as inline Dataview fields under each H2 — Dataview rolls them up to file-level as arrays. Queries below normalize to arrays so they work for both single-application files (where the field is a scalar) and multi-application files (where the field is an array).
>
> **What to do here:** scan top-down. For each row, click the bridge link to drill into the per-application H2 sections. Decide per H2: bump that H2's `status::` (`not-started` → `in-progress` → `applied` → `verified`), edit the H2 body directly, or remove the H2 (delete just that H2 section if abandoning one application — keep the file alive for any remaining applications).

---

## 🟢 Revenue bridges — work first

Active bridges (any application is `not-started` or `in-progress`) where any application is tagged with `revenue`. Sorted by best `expected-impact` across applications (large → medium → small → unset), then by file `created` ascending (oldest first within impact tier).

```dataviewjs
const toArr = (v) => Array.isArray(v) ? v.flat() : (v != null ? [v] : []);
const impactRank = { large: 0, medium: 1, small: 2 };

const rows = dv.pages('"Optimus Academy/apply-to-optimus"')
  .where(p => {
    const statuses = toArr(p.status);
    const vectors = toArr(p["value-vector"]);
    const hasActive = statuses.some(s => s === "not-started" || s === "in-progress");
    const hasRevenue = vectors.includes("revenue");
    return hasActive && hasRevenue;
  })
  .map(p => {
    const impacts = toArr(p["expected-impact"]);
    const bestImpact = impacts.length ? Math.min(...impacts.map(i => i in impactRank ? impactRank[i] : 3)) : 3;
    const impactDisplay = impacts.length ? impacts.join(", ") : "—";
    const ageDays = p.created ? Math.floor((Date.now() - new Date(p.created).getTime()) / 86400000) : null;
    const targets = toArr(p["applies-to"]);
    const targetCount = targets.length || 1;
    const statusDisplay = toArr(p.status).join(", ") || "—";
    return [p.file.link, p.concept, targetCount, impactDisplay, ageDays === null ? "—" : ageDays + "d", statusDisplay, bestImpact, p.created];
  })
  .sort(row => row[6] * 1e9 + (row[7] ? new Date(row[7]).getTime() / 86400000 : 0));

dv.table(["Bridge", "Concept", "# Apps", "Impact(s)", "Age", "Status(es)"], rows.map(r => r.slice(0, 6)));
```

---

## 🟡 Productivity bridges — work second

Active bridges where any application is tagged with `productivity`. Same sort. Productivity is the force-multiplier vector — every applied productivity bridge compounds across all future builds.

```dataviewjs
const toArr = (v) => Array.isArray(v) ? v.flat() : (v != null ? [v] : []);
const impactRank = { large: 0, medium: 1, small: 2 };

const rows = dv.pages('"Optimus Academy/apply-to-optimus"')
  .where(p => {
    const statuses = toArr(p.status);
    const vectors = toArr(p["value-vector"]);
    const hasActive = statuses.some(s => s === "not-started" || s === "in-progress");
    const hasProductivity = vectors.includes("productivity");
    return hasActive && hasProductivity;
  })
  .map(p => {
    const impacts = toArr(p["expected-impact"]);
    const bestImpact = impacts.length ? Math.min(...impacts.map(i => i in impactRank ? impactRank[i] : 3)) : 3;
    const impactDisplay = impacts.length ? impacts.join(", ") : "—";
    const ageDays = p.created ? Math.floor((Date.now() - new Date(p.created).getTime()) / 86400000) : null;
    const targets = toArr(p["applies-to"]);
    const targetCount = targets.length || 1;
    const statusDisplay = toArr(p.status).join(", ") || "—";
    return [p.file.link, p.concept, targetCount, impactDisplay, ageDays === null ? "—" : ageDays + "d", statusDisplay, bestImpact, p.created];
  })
  .sort(row => row[6] * 1e9 + (row[7] ? new Date(row[7]).getTime() / 86400000 : 0));

dv.table(["Bridge", "Concept", "# Apps", "Impact(s)", "Age", "Status(es)"], rows.map(r => r.slice(0, 6)));
```

---

## 🔵 Overhead bridges — work third

Active bridges where any application is tagged with `overhead`. Same sort. Overhead reduction is real but quieter — reviewed last among active vectors so high-leverage revenue/productivity work gets attention first.

```dataviewjs
const toArr = (v) => Array.isArray(v) ? v.flat() : (v != null ? [v] : []);
const impactRank = { large: 0, medium: 1, small: 2 };

const rows = dv.pages('"Optimus Academy/apply-to-optimus"')
  .where(p => {
    const statuses = toArr(p.status);
    const vectors = toArr(p["value-vector"]);
    const hasActive = statuses.some(s => s === "not-started" || s === "in-progress");
    const hasOverhead = vectors.includes("overhead");
    return hasActive && hasOverhead;
  })
  .map(p => {
    const impacts = toArr(p["expected-impact"]);
    const bestImpact = impacts.length ? Math.min(...impacts.map(i => i in impactRank ? impactRank[i] : 3)) : 3;
    const impactDisplay = impacts.length ? impacts.join(", ") : "—";
    const ageDays = p.created ? Math.floor((Date.now() - new Date(p.created).getTime()) / 86400000) : null;
    const targets = toArr(p["applies-to"]);
    const targetCount = targets.length || 1;
    const statusDisplay = toArr(p.status).join(", ") || "—";
    return [p.file.link, p.concept, targetCount, impactDisplay, ageDays === null ? "—" : ageDays + "d", statusDisplay, bestImpact, p.created];
  })
  .sort(row => row[6] * 1e9 + (row[7] ? new Date(row[7]).getTime() / 86400000 : 0));

dv.table(["Bridge", "Concept", "# Apps", "Impact(s)", "Age", "Status(es)"], rows.map(r => r.slice(0, 6)));
```

---

## 🟣 Applied → awaiting promotion

Bridge files where any application has `status: applied` — the change shipped, now waiting to be verified or promoted. Promote candidates: institutional patterns get moved to `lessons/`, `knowledge/patterns/`, or `knowledge/craft/<area>/` so they become reusable assets across projects, not just one-off applications.

```dataviewjs
const toArr = (v) => Array.isArray(v) ? v.flat() : (v != null ? [v] : []);

const rows = dv.pages('"Optimus Academy/apply-to-optimus"')
  .where(p => toArr(p.status).includes("applied"))
  .map(p => {
    const lastUpdated = p["last-updated"] || p.created;
    const vectors = toArr(p["value-vector"]);
    const targets = toArr(p["applies-to"]);
    const targetCount = targets.length || 1;
    return [p.file.link, targetCount, vectors.length ? [...new Set(vectors)].join(", ") : "—", lastUpdated, lastUpdated ? new Date(lastUpdated).getTime() : 0];
  })
  .sort(row => -row[4]);

dv.table(["Bridge", "# Apps", "Vectors", "Last updated"], rows.map(r => r.slice(0, 4)));
```

---

## ⚫ Abandonment candidates — aged 30+ days, all applications still not started

Bridge files where every application has sat in `not-started` for over 30 days. Decide per row: drill into the file and bump individual application H2s to `in-progress` (commit to do them now), abandon individual applications (delete the H2 section — keep the file alive for any remaining applications), or keep aging if context isn't ready yet. Surfacing aging items keeps the queue honest.

```dataviewjs
const toArr = (v) => Array.isArray(v) ? v.flat() : (v != null ? [v] : []);
const cutoff = Date.now() - 30 * 86400000;

const rows = dv.pages('"Optimus Academy/apply-to-optimus"')
  .where(p => {
    const statuses = toArr(p.status);
    if (!p.created || new Date(p.created).getTime() >= cutoff) return false;
    if (!statuses.length) return false;
    return statuses.every(s => s === "not-started");
  })
  .map(p => {
    const ageDays = Math.floor((Date.now() - new Date(p.created).getTime()) / 86400000);
    const vectors = toArr(p["value-vector"]);
    const vectorDisplay = vectors.length ? [...new Set(vectors)].join(", ") : "—";
    const targets = toArr(p["applies-to"]);
    const targetCount = targets.length || 1;
    return [p.file.link, vectorDisplay, ageDays + "d", targetCount, ageDays];
  })
  .sort(row => -row[4]);

dv.table(["Bridge", "Vectors", "Age", "# Apps"], rows.map(r => r.slice(0, 4)));
```

---

## Notes

- **Empty blocks are normal early on.** When the bridge folder has fewer than ~20 entries, several blocks may show no rows. Keep the file as-is; rows populate as `/learn` accumulates bridges.
- **Multi-vector duplication is intentional.** A bridge file with applications tagged `[productivity, revenue]` appears in BOTH the 🟢 and 🟡 blocks. That duplication is the signal: it's a higher-leverage bridge than a single-vector one.
- **One row per bridge file, not per application.** Each bridge file shows up once in each query block where any application qualifies. The `# Apps` column shows how many applications the file has so you can gauge fan-out at a glance. To see per-application detail, click into the file.
- **No autonomous promotion.** Status bumps are manual decisions, made per application H2. The 🟣 block surfaces files with at least one applied application; you decide which patterns earn institutional-pattern status.
- **The concept layer is separate.** This file reviews bridges only. Browse `concepts/` directly for the teaching-artifact layer (which is also the future Optimus University substrate).
