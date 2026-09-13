# Evidence trail

Every number that appears in the manuscript gets a row here before it is written into
the LaTeX. No row, no number.

**Study repository:** https://github.com/mvy0502/gencp-validation
**Branch:** `main`
**Baseline commit for the rows below:** `284571b` (26 August 2026)

*Re-pinned 2026-08-26. The rows below previously read `612b7f6` on branch `tubitak-tr`,
which is a **GenCP** branch — gencp-validation has no `tubitak-tr`. The SHAs themselves
were never wrong: `612b7f6` is reachable from gencp-validation `main`, because the two
repositories share history and the sync was a merge, not a rewrite. Only the repository
and branch labels were wrong, and they are corrected here.*

Columns: the claim as it will be made, the value, where it comes from in the study repo,
and the commit that value was read at. When a row's source document changes, re-read the
value, update the commit, and note it in the change log at the bottom.

## Leg 1 — scope (E1/E2): the premise fails at 10 m

Two sentences in the introduction, not a section and not a result
(`paper-roadmap.md`:152).

| Claim | Value | Source | Commit |
|---|---|---|---|
| No availability gap | 0/24 extents without a usable scene; median freshness 2 days, max 17 | `tubitak/docs/positioning-results.md` (E1) | `284571b` |
| Scene-per-year counts are lower bounds | archive query capped at 100, every extent hit the cap; censoring does not affect gap rate or freshness | `positioning-results.md` (E1), `open-items.md` item 23 | `284571b` |
| No currency advantage | E2 ABSENT, +0.008 ± 0.031 px | `positioning-results.md` (E2) | `284571b` |

Caveat that must travel with leg 1: E2's null is equally consistent with "currency does
not help" and "OSM had not yet recorded the change" (`open-items.md` item 21).

## Leg 2 — the design rule (no plausibility pressure for a generated reference)

*Renumbered 2026-08-26. The former Leg 2 ("where it binds", sub-metre) moved to the
second paper together with T1 and E3 (`paper-roadmap.md`:158, :178), so the former
Leg 3 is now Leg 2. **T1's C1 row is no longer the primary measurement** — the 2×2
factorial replaces it (`paper-roadmap.md`:180).*

| Claim | Value | Source | Commit |
|---|---|---|---|
| Primary — seed-level sign replication | (fill from `seed-block-results.md` §1 before drafting: C5−C4 negative in all six confirmatory seeds, P = 1/64, direction fixed in advance) | `tubitak/docs/seed-block-results.md` | `284571b` |
| Secondary — LPIPS-alone positional penalty | (fill from `seed-block-results.md` §5(a): C5−C2 positive in all six seeds, P = 1/64; state the thinnest margin) | `seed-block-results.md` | `284571b` |
| B2 production-path ablation | (fill from `headline-results.md` B2 before drafting) | `tubitak/docs/headline-results.md` | `284571b` |
| B3 mechanism measurement (part 1 and part 3 only) | edge-density ratio; carries the §22 non-monotonicity caveat | `headline-results.md` B3, `paper-context-addendum.md` §22 | `284571b` |
| B1 dose-response (support only, not the spine) | post-hoc; registered bands did not cover the observed shape | `headline-results.md` B1 | `284571b` |
| Interaction — registered, tested, NOT claimed | 5/6 on each of three pre-specified scales; pre-committed consequence is no claim | `seed-block-results.md` §4, `paper-context-addendum.md` §24 | `284571b` |
| Seed defence | pre-registered n >= 60 single-draw rule; regA det/stoch bound <= 0.05 px; measured effects 0.38–0.70 px | `positioning-registrations.md`, `tool-results.md`, `headline-results.md` | `284571b` |
| Blur vs restraint (Table II row 3) | six-seed informative-mask edge ratio; C2 reproduces real edge density to within 1.5% where the input asserts structure — selective suppression, not blur | `informative-mask-results.md` | `284571b` |

## Section V.1 — the operational figure (decided 2026-09-13: B2, production path)

| Claim | Value | Source | Commit |
|---|---|---|---|
| Design rule's operational figure | C2 = 0.593 ± 0.041 px, production path (POST inputs), BT.601 KLT, K = 8, n = 20 urban chips; better than pretrained on 20/20 chips (C2 − pretrained −0.777 ± 0.125); C2 − C1 −0.171 ± 0.042 (19/20) | `tubitak/docs/headline-results.md` B2 ("institution-facing sentence"); reproduced from raw in `B2-B3-audit.md`, 384/384 cells | `a415e25` |

Not chosen, recorded so it is not re-litigated: packageA's urban headline C2 = 0.591 px
(BT.601 KLT, n = 20, off-path) — the same measurement on the earlier input path; the
production path is what makes the figure operational.

## Table I — the five-arm panel, rebuilt from the six-seed block (2026-09-13)

Inference path, stated once for every cell: per chip, the median KLT residual (px) over the
matches that arm itself produced against real Sentinel-2, 130 Ankara chips; per seed, the
mean (or median) of those 130 per-chip medians; the table entry is the mean over the six
confirmatory seeds 45–50 (Modal A10G block). The pretrained arm's images were generated once
and scored in every seed's evaluation, so its row is seed-invariant. Points = per-chip median
of surviving matches, averaged over seeds. Edge ratio = per-arm mean of the 130 per-chip
input-silent ratios, averaged over seeds. Computed by
`tubitak/scripts/seed_eval/table1_six_seed.py` from `docs/evidence/C45_s{45..50}_modal/`;
the per-seed contrasts it reproduces match `seed-block-results.md` §1 to four decimals.

| Arm | Mean px | Seed sd | Median px | Points | Edge ratio | Commit |
|---|---|---|---|---|---|---|
| pretrained | 2.563 | — | 2.588 | 51 | 1.02 | `a415e25` |
| adversarial + L1 (C1) | 2.070 | 0.025 | 1.987 | 62 | 1.09 | `a415e25` |
| L1 (C2) | 1.393 | 0.037 | 0.975 | 75 | 0.28 | `a415e25` |
| adversarial + LPIPS (C4) | 2.065 | 0.025 | 1.939 | 60 | 1.13 | `a415e25` |
| LPIPS (C5) | 1.456 | 0.013 | 1.110 | 87 | 1.15 | `a415e25` |

Ordering: C2 < C5 < {C1, C4} < pretrained in every seed. **The two adversarial arms are not
ordered across seeds**: C4 below C1 in seeds 47, 48 and 50, above it in 45, 46 and 49; the
six-seed means differ by 0.005 px. The draft's "same ordering in every seed" was true of
seed 42 and is false of the block; corrected in III-A on 2026-09-13.

## Data-availability statement

| Claim | Value | Source | Commit |
|---|---|---|---|
| Phase D: six of seven checks and the veto rule have no artifact; scripts never committed; input imagery gone | as stated | `phase-d-audit.md` §C, `phase-d-closeout.md` D-2 | `a415e25` |
| Two registered Phase D outputs permanently unrecoverable | check 5's Ankara floor sweep; check 7a's per-stratum gains | `phase-d-closeout.md` D-4; corrections-log entry 33 | `a415e25` |
| B3 harness not preserved; four matcher parameters as configured | as stated | corrections-log entry 22 | `a415e25` |
| Per-seed arm images not committed (650 files × 6 seeds); re-inference is stochastic | as stated | `evidence/rasters/README.md` | `a415e25` |
| 260 seed-independent rasters committed | 130 + 130, 26.4 MB | `evidence/rasters/README.md`, `MANIFEST.md`; entry 35 | `a415e25` |
| Private backup holds checkpoints, generated images, the 130 unregenerable Ankara inputs | Kaggle `gencp-evidence-backup`, `-2` | `evidence/BACKUP.md`, `paper-context-addendum.md` §13 | `a415e25` |

## Sections I and V — rows added 2026-09-13 when the sections were drafted

| Claim | Value | Source | Commit |
|---|---|---|---|
| Upstream objective | adversarial + λ·LPIPS, λ = 100, BCE discriminator; LPIPS backbone not named in the text, VGG in the code; L1→LPIPS substitution stated without comparison or ablation | `paper-context-addendum.md` §16 (69–82), `related-work.md` §6 | `59612e7` |
| Forest under-representation | train/serve skew ≈ 0.6 px on forest-heavy chips | `open-items.md` item 10 (phase-c-results limitations) | `59612e7` |
| LPIPS implementation versions | torchmetrics 1.9.0 (ours) vs 0.11.0 (upstream) | `phase-c-lpips-results.md`:217, `phase-c-audit.md`:286 | `59612e7` |
| E2 headline for the scope sentence | five-year-old real scene (2021) 0.057 px vs GenCP C2 0.120 px mean recovery error; interaction +0.008 ± 0.031 px, ABSENT | `positioning-results.md` E2 | `59612e7` |
| Common-support count | 69 of 130 chips with zero common points at 2 px, seed 45 | `common-support-registration.md` §2 | `59612e7` |
| LR-schedule bound (Section II-A) | +0.007 ± 0.034 px, one seed (43, Modal), chip-level; non-adversarial arms only; reverse manipulation not run | `lr-confound-results.md` §3 | `59612e7` |
| Deterministic-mode bound (Section II-D) | registered ≤ 0.05 px band met on 30 chips, four earlier arms; resolution ≈ 0.15 px | `tool-results.md` Registration A | `59612e7` |

## Methods — the 1/256 scale bug (one paragraph plus repo pointer)

| Claim | Value | Source | Commit |
|---|---|---|---|
| Scale error | +0.390625% = exactly 1/256; true GSD 10.0390625 m vs 10.0 declared | `tubitak/docs/geometry-finding.md` | `284571b` |
| Worst-case displacement | 14.1 m at the SE corner, zero at NW | `geometry-finding.md` | `284571b` |
| Independent confirmation | three independent lines of evidence, plus KARIOS as an independent check (9.9 sigma) | `geometry-finding.md` | `284571b` |
| Correction reduces global shift | 40.3% | `karios-validation.md` | `284571b` |

## Dataset defects (reported to upstream)

| Claim | Value | Source | Commit |
|---|---|---|---|
| Leaked test chips | 9 of 577 | `geometry-finding.md` §12.1 | `284571b` |
| Demo/train overlaps | 25 of 630 | `geometry-finding.md` §12.2 | `284571b` |
| OSM halves not byte-identical | 323 of the 566 verified test chips | `karios-validation.md`, "Dataset note" | `284571b` |

## Do not quote (retracted, superseded, or moved)

Check `corrections-log.md` before adding any row. Known traps:

| Value | Why it must not appear | Source |
|---|---|---|
| ODTÜ/Cappadocia contamination pair (0.008–0.11 px vs 0.54–3.97 px, 20–130x) | **Moved to the second paper.** Not a section, not a table, not a row of this letter | `paper-roadmap.md`:158, :248 |
| T1's C1 row as a primary measurement | **Moved to the second paper** with the rest of T1; superseded as primary by the factorial | `paper-roadmap.md`:158, :180 |
| "mediation 0%" / B3 part 2 | **Void as stated.** The reported conditional is the OLS fitted value at the covariate means, algebraically the raw mean, so it could not have been a mediation result. Does not appear at all | `corrections-log.md` entry 20, `B2-B3-audit.md` |
| "48 of 49" (matcher row) | Struck; not reproducible from the artifact | `letter-skeleton.md` Table II revision |
| C5−C4 = −0.487 ± 0.053 px as the primary | Chip-level and single-seed; superseded by the seed-level six-seed replication. Seed 42's value falls outside the six-seed range and is not one of the replicates | `seed-block-results.md` §5(c) |
| +0.012 ± 0.132 px rasteriser gate | Retired; superseded by the corrected-input re-run: **+0.119 ± 0.138 px, PASS** | `renderer-tolerance.md` §7, `corrections-log.md` entry 15 |
| "3x worse than upstream" | Withdrawn; compared two different quantities | `karios-validation.md`, `corrections-log.md` |
| E3 pass as a registered result | Reclassified exploratory; absent from the letter entirely | `corrections-log.md` entry 16 |

## Change log

| Date | What changed | Rows touched |
|---|---|---|
| 2026-09-13 | Sections I and V drafted; rows for their numbers and for three Section II bounds added at gencp-validation `59612e7` | I, V, II |
| 2026-09-13 | V.1 figure decided (0.593, B2 production path) and given its row; Table I rebuilt from the six-seed block with its inference path; data-availability rows added; rows read at gencp-validation `a415e25` | V.1, Table I, data availability |
| 2026-08-26 | Evidence trail created at study-repo baseline `612b7f6` | all |
| 2026-08-26 | Re-pinned to gencp-validation `main` at `284571b`; repository/branch labels corrected (`612b7f6` was labelled `tubitak-tr`, a GenCP branch). Removed the ODTÜ contamination table, the former Leg 2 (T1/sub-metre) and Leg 3's T1 C1 row — all moved to the second paper. Struck the mediation clause from the B3 row. Former Leg 3 renumbered to Leg 2; primary and secondary rows added as placeholders for the six-seed replication | all |
