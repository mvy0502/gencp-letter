# Evidence trail

Every number that appears in the manuscript gets a row here before it is written into
the LaTeX. No row, no number.

**Study repository:** https://github.com/mvy0502/gencp-validation
**Baseline commit for the rows below:** `612b7f6` (branch `tubitak-tr`, 26 August 2026)

Columns: the claim as it will be made, the value, where it comes from in the study repo,
and the commit that value was read at. When a row's source document changes, re-read the
value, update the commit, and note it in the change log at the bottom.

## Leg 1 — scope (E1/E2): the premise fails at 10 m

| Claim | Value | Source | Commit |
|---|---|---|---|
| No availability gap | 0/24 extents without a usable scene; median freshness 2 days, max 17 | `tubitak/docs/positioning-results.md` (E1) | `612b7f6` |
| Scene-per-year counts are lower bounds | archive query capped at 100, every extent hit the cap; censoring does not affect gap rate or freshness | `positioning-results.md` (E1), `open-items.md` item 23 | `612b7f6` |
| No currency advantage | E2 ABSENT, +0.008 ± 0.031 px | `positioning-results.md` (E2) | `612b7f6` |

Caveat that must travel with leg 1: E2's null is equally consistent with "currency does
not help" and "OSM had not yet recorded the change" (`open-items.md` item 21).

## Leg 2 — where it binds

| Claim | Value | Source | Commit |
|---|---|---|---|
| Real imagery is the better reference where it exists | T1 verdict, clean site | `tubitak/docs/T1-benchmark-results.md` | `612b7f6` |
| E3 is exploratory only, absent from the letter | — | `corrections-log.md` entry 16 | `612b7f6` |

## Leg 3 — the design rule (no adversarial loss for a generated reference)

| Claim | Value | Source | Commit |
|---|---|---|---|
| T1 C1 row, clean site | C1 1.119 px vs C2 0.541 px at t1; point counts 405/388 | `T1-benchmark-results.md` | `612b7f6` |
| B2 production-path ablation | (fill from `headline-results.md` B2 before drafting) | `tubitak/docs/headline-results.md` | `612b7f6` |
| B3 direct mechanism measurement | edge-density ratio; mediation 0% | `headline-results.md` B3 | `612b7f6` |
| B1 dose-response (support only, not the spine) | post-hoc; registered bands did not cover the observed shape | `headline-results.md` B1 | `612b7f6` |
| Seed defence | pre-registered n >= 60 single-draw rule; regA det/stoch bound <= 0.05 px; measured effects 0.38–0.70 px | `positioning-registrations.md`, `tool-results.md`, `headline-results.md` | `612b7f6` |
| Seed-level replication | seed 43: four arms complete; evaluation pending | `seed-replication-registration.md` (SEED-b) | `612b7f6` |

## Methods contribution — ODTÜ contamination pair

| Claim | Value | Source | Commit |
|---|---|---|---|
| Contaminated site | 0.008–0.11 px | `T1-benchmark-results.md`, `delivery-registrations.md` | `612b7f6` |
| Clean site | 0.54–3.97 px | same | `612b7f6` |
| Ratio | 20–130x | `paper-roadmap.md` | `612b7f6` |

## Methods — the 1/256 scale bug (one paragraph plus repo pointer)

| Claim | Value | Source | Commit |
|---|---|---|---|
| Scale error | +0.390625% = exactly 1/256; true GSD 10.0390625 m vs 10.0 declared | `tubitak/docs/geometry-finding.md` | `612b7f6` |
| Worst-case displacement | 14.1 m at the SE corner, zero at NW | `geometry-finding.md` | `612b7f6` |
| Independent confirmation | three independent lines of evidence, plus KARIOS as an independent check (9.9 sigma) | `geometry-finding.md` | `612b7f6` |
| Correction reduces global shift | 40.3% | `karios-validation.md` | `612b7f6` |

## Dataset defects (reported to upstream)

| Claim | Value | Source | Commit |
|---|---|---|---|
| Leaked test chips | 9 of 577 | `geometry-finding.md` §12.1 | `612b7f6` |
| Demo/train overlaps | 25 of 630 | `geometry-finding.md` §12.2 | `612b7f6` |
| OSM halves not byte-identical | 323 of the 566 verified test chips | `karios-validation.md`, "Dataset note" | `612b7f6` |

## Do not quote (retracted or superseded)

Check `corrections-log.md` before adding any row. Known traps:

| Value | Why it must not appear | Source |
|---|---|---|
| +0.012 ± 0.132 px rasteriser gate | Retired; superseded by the corrected-input re-run: **+0.119 ± 0.138 px, PASS** | `renderer-tolerance.md` §7, `corrections-log.md` entry 15 |
| "3x worse than upstream" | Withdrawn; compared two different quantities | `karios-validation.md`, `corrections-log.md` |
| E3 pass as a registered result | Reclassified exploratory | `corrections-log.md` entry 16 |

## Change log

| Date | What changed | Rows touched |
|---|---|---|
| 2026-08-26 | Evidence trail created at study-repo baseline `612b7f6` | all |
