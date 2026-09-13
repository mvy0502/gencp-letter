# Evidence trail

Every number that appears in the manuscript gets a row here before it is written into
the LaTeX. No row, no number.

**Study repository:** https://github.com/mvy0502/gencp-validation
**Branch:** `main`
**Baseline commit for the rows below:** `a3e1918` (13 September 2026)

*Re-pinned 2026-09-13 after the Sections II–IV row audit. Every row below was read, or
re-read, at `a3e1918`; the two commits after `59612e7` touched only the corrections log
(entries 39–40) and two related-work notes, so every value is also readable at
`59612e7`. Rows written earlier today carry the commit they were read at.*

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

## The panel figure (Fig. 2 as compiled) — per-chip values in the caption (2026-09-13)

| Claim | Value | Source | Commit |
|---|---|---|---|
| Chip (a), largest input-silent fraction | `ank_3_34`, silent 1.000; r: pretrained 1.12, C1 1.18, C2 0.94, C4 1.18, C5 1.15 | `docs/evidence/C45_s45_modal/C45_edge_ratio.csv` (seed 45) | `a3e1918` |
| Chip (b), median input-silent fraction | `ank_18_29`, silent 0.847 (panel median 0.850); r: pretrained 0.93, C1 0.94, C2 0.36, C4 0.93, C5 0.99 | same | `a3e1918` |

| Fully input-silent chips | 2 of 130 per seed (silent_frac = 1.000), identical across the six seeds | `docs/evidence/C45_s{45..50}_modal/C45_edge_ratio.csv`, counted 2026-09-13 | `a3e1918` |
| Chips excluded from the informative-mask statistic | 3 per seed, identical across seeds (empty mask or zero real-chip edge fraction), by the registered rule | `informative-mask-results.md`:12–13, :52–53 | `a3e1918` |

## The training-time curve (Fig. 1 as compiled) at six seeds (scored 2026-09-13)

Registration `epoch-curve-registration.md` (gencp-validation `36875ba`, before any cell was
scored). Inference path: frozen per-seed runner (commit `48ced64`), shim seed 42, KARIOS
config unchanged; penalty = chip mean over 130 chips of (adversarial − counterpart per-chip
median), one value per seed per epoch; epoch 20 is the six-seed block.

| Claim | Value | Source | Commit |
|---|---|---|---|
| Registered reading, LPIPS family | HELD: positive 6/6 at epochs 1, 2, 5, 10, 20 | `epoch-curve-results.md`; `evidence/epoch_curve/epoch_curve_summary.json` | `5e32c23` |
| Registered reading, L1 family | HELD: positive 6/6 at every epoch | same | `5e32c23` |
| Six-seed means, LPIPS | 0.262, 0.258, 0.499, 0.532, 0.609 px (seed sd 0.044, 0.031, 0.053, 0.061, 0.023) | `evidence/epoch_curve/epoch_curve_per_seed.csv` | `5e32c23` |
| Six-seed means, L1 | 0.521, 0.473, 0.423, 0.575, 0.677 px (sd 0.067, 0.065, 0.085, 0.074, 0.057) | same | `5e32c23` |
| Exploratory dip-then-grow | 3 of 6 seeds (LPIPS), 5 of 6 (L1): not stable, not claimed | `epoch_curve_summary.json` | `5e32c23` |
| Seed-42 LPIPS curve (superseded as the curve figure, quoted as the generating run) | 0.334, 0.254, 0.441, 0.496, 0.487 px | `phase-c-lpips-results.md`:176–180 | `a3e1918` |

## Section III-L — the OSM render as a reference (registered and scored 2026-09-13)

Registration `osm-render-baseline-registration.md` (`a5314b1`, amended `e665bc7`); results
`osm-render-baseline-results.md` (`c263e4c`). Inference path: one number per chip, render
seed-invariant; every comparison a paired chip-level difference over 130 chips, D = render −
arm, SE across chips; fine-tuned arms compared per seed and quoted as the range of the six
chip-level means. Reading: INTERMEDIATE.

| Claim | Value | Source | Commit |
|---|---|---|---|
| Render alone | median of per-chip medians 0.583 px; mean of medians 0.797 px; median points 29.5; 7 of 130 chips with no match | `evidence/osm_render_baseline/render_baseline_summary.json` | `c263e4c` |
| D vs pretrained (raw; equal-count not constructible) | −1.715 ± 0.091 px, t −18.8, render better on 121/123 | same | `c263e4c` |
| D vs adversarial + L1 | raw −1.148 … −1.224 (mean −1.186); equal-count −1.074 … −1.225 (mean −1.170) | same | `c263e4c` |
| D vs L1-only | raw −0.444 … −0.559 (mean −0.481), min \|t\| 6.0; equal-count −0.389 … −0.516 (mean −0.461) | same | `c263e4c` |
| D vs adversarial + LPIPS | raw −1.129 … −1.217 (mean −1.173); equal-count −1.100 … −1.266 (mean −1.177) | same | `c263e4c` |
| D vs LPIPS-only | raw −0.526 … −0.572 (mean −0.554); equal-count −0.511 … −0.593 (mean −0.557) | same | `c263e4c` |

| D vs pretrained, equal-count (amendment) | −1.778 ± 0.109 px, t −16.3, render better on 121/123; from the retained rows at `ankara/run/results/` (130/130 reproduce `turkey_karios.csv`) | `osm-render-baseline-results.md` amendment | `f27f710` |
| Denominators, III-L | 123 chips (render matched) for every raw and equal-count comparison; the 7 unmatched chips enter only the point-yield criterion | `render_baseline_summary.json` (`n` fields) | `f27f710` |
| Band handling (II-D) | Table I and III-L: KARIOS on three-band warped rasters; II-E and Fig. 2: BT.601 gray; V-A: KLT on BT.601 gray | `c45_karios.py`; `c45_edge_ratio.py`; `headline-registrations.md` B2 | `f27f710` |

## P4 rows, 2026-09-13 — restored, added or qualified text

| Claim | Value | Source (line) | Commit |
|---|---|---|---|
| 1/256 finding (II-F, restored) | true GSD 10.0390625 m vs 10.0; +0.390625 % = 1/256; 0 at NW, 14.1 m at SE corner; predicted sd 2.89 m vs observed 14.5–17.3 m, ≈3.9 % of reported variance; text-versus-data inconsistency; audited upstream commit `e218f29` | `geometry-finding.md`:233–252; `paper-context-addendum.md` §19; draft text cadad66 block F | `813d2dd` |
| Warm-up attenuation, within platform and seed (III-J) | G_L1: C2 −5.16 % un-warmed vs C2_warmup −2.98 %; G_LPIPS: C5 −7.98 % vs C5_warmup −5.32 %; controlled gap 6.19 → 4.00 (35.3 %) and 9.00 → 6.33 (29.7 %); Modal seed 43 | `warmup-deconfound-results.md` §4a (lines 286–288, 316–317) | `813d2dd` |
| Warm-up attenuation, cross-platform (III-J) | 54.3 % (L1) and 22.1 % (LPIPS) against Kaggle seed-42 comparators; kept beside, labelled | `warmup-deconfound-results.md` §4a (lines 340–346) | `813d2dd` |
| L1-family sign replication (III-B) | C1 − C2 positive 6/6: +0.6749, +0.5868, +0.7010, +0.7544, +0.7024, +0.6444 px; mean +0.6773, CI [+0.6172, +0.7374] | `seed-block-results.md` §1, §5(a) | `813d2dd` |
| Single-run interaction, first record | −0.212 ± 0.069 px entered the record at commit `6560c8b` (24 Aug 2026) | `git log -S` on `phase-c-lpips-results.md` | `813d2dd` |
| Production path (V-A) | the delivered tool renders post-fix Geofabrik extracts; the research chips were rendered from a live API; B2 re-measured the headline on that path: 0.593 ± 0.041 px, BT.601-gray KLT, K = 8, n = 20 urban chips | `headline-registrations.md` B2 (:36–51); `headline-results.md` B2; `paper-context-addendum.md` §13 | `813d2dd` |
| Training-stability rule (III-J) | registered coarse rule: G_LPIPS rising over the first two main-stage epochs; fired at seed 42 (54.37 → 54.65 → 55.02) and was not acted on | `phase-c-lpips-results.md`:37 | `813d2dd` |
| Chip (II-D) | 228 × 228 pixels at 10 m on the warped grid | `scripts/c45_eval/c45_warp.py` (GRID_N, PX) | `813d2dd` |
| Match score (II-D) | KLT's per-match `score` column, ranked descending, never by residual | `common-support-registration.md`:73–78 | `813d2dd` |

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

## Sections II–IV — row audit, 2026-09-13

Every number the three migrated sections quote, with its source line and inference path.
Values already carried in rows above (Table I, the V.1 figure, Section II bounds, data
availability) are not repeated. Commit for every row: `a3e1918`.

### Section II

| Claim | Value | Source (line) |
|---|---|---|
| Generator size | U-Net-256, 54.414 M parameters, PatchGAN discriminator, map-to-image | `paper-context-addendum.md` §16 (69–73); `phase-c3-results.md`:7 |
| Training pairs | 5,577 | `hardware-gate-results.md`:120 (`EXPECTED_N_FILES = 5577`, captured file-list hash) |
| Epochs and schedule | 20 per arm; linear 10 + 10 at base rate then decaying | `seed-replication-registration.md`:64 |
| Confirmatory block | seeds 45–50, Modal A10G, one platform | `seed-block-results.md` head; `hardware-gate-results.md` title |
| Earlier runs | seed 42 (generating), seeds 43–44 (two-seed block), Kaggle T4, `gpu_ids=[0]` | `seed-replication-registration.md`:78–101, :116–125; `phase-c-config.md`:145 |
| Poolability rule and verdict | NOT POOLED: edge_C1 \|Modal−Kaggle\| 0.0177 vs seed spread 0.0042 (4.2×); ten of eleven pass | `hardware-gate-results.md` "Verdict" |
| Warm-up schedule | adversarial arms: 2 epochs at 2×10⁻⁵ then 18 at 10⁻⁴; others 20 at 10⁻⁴ | `lr-confound-registration.md`; `phase-c-config.md` |
| Integrated LR | 13.40 vs 15.00 (10⁻⁴ epochs), 10.67 % deficit | `lr-confound-results.md` §3 |
| LR bound | Δ = warmed − un-warmed, L1 family +0.0065 ± 0.0335 px (quoted +0.007 ± 0.034), 1.0 % of the 0.6473 px gap; one seed (43, Modal), chip-level | `lr-confound-results.md`:10, :74, :158 |
| Matcher configuration | KLT, confidence threshold 0.8 (upstream README value) | `karios-validation.md`:54 |
| Chip panel | 130 Ankara chips, 26 per land-cover edge-density quintile | `ankara-acquisition.md`:86 |
| Test-time dropout | STOCH path, dropout active, single draw, as seed 42 | `seed-replication-registration.md`:491 |
| Points surrendered by truncation | LPIPS-only 38–39 % (38.2–39.1 across seeds); adversarial + LPIPS 5.6–7.4 % (quoted 7 %) | `common-support-results.md`:26–31 |
| Common-support tolerance argument | residuals ~1.4 px (C2) to ~2.0 px (C1); 2 px tolerance is the size of the effect | `common-support-registration.md` §2 |
| Input-silent definition | canonical Sobel ≤ 20 on the input render; edge fraction Sobel > 20; denominator the real chip on the same pixels | `phase-c-lpips-registration.md`:123–124 |

### Section III

| Claim | Value | Source (line) |
|---|---|---|
| Primary per seed | −0.6153, −0.6462, −0.6162, −0.5942, −0.6054, −0.5775 px; 6/6; P = 1/64; direction fixed by seed 42 | `seed-block-results.md` §1 |
| Primary interval | mean −0.6091, 95 % CI [−0.6335, −0.5847], df = 5 | `seed-block-results.md` §5(a) |
| Interaction | 5/6 on raw, log and rank; seed 46 breaks each (raw +0.0594) | `seed-block-results.md` §1, §3 |
| Two-seed block | seeds 43–44, interaction negative in both on all three scales; never pooled | `seed-block-results.md` §5(d) |
| Interaction intervals | log [−0.1092, −0.0125] and rank [−0.3036, −0.0041] exclude zero; raw does not | `seed-block-results.md` §5(a) |
| Secondary | C5 − C2 6/6; mean +0.0626, CI [+0.0273, +0.0979]; narrowest +0.0068 (seed 46) | `seed-block-results.md` §1, §5(a) |
| Dose-response under LPIPS | C4 − C5 by epoch 1/2/5/10/20: +0.334, +0.254, +0.441, +0.496, +0.487 px, t = 8.3, 6.4, 11.3, 10.7, 9.2; **seed 42, chip-level, single draw** | `phase-c-lpips-results.md`:176–180 |
| Equal-count result | primary +0.0108 px (1.8 %), secondary −0.0069 px (11 %), both 6/6 | `common-support-results.md`:100–104 |
| Floor sweep | K ≥ 30: every seed ≥ +0.0373 px, 6/6 | `common-support-results.md`:84, :90 |
| Informative-mask ratio | C2 0.986 (mean of 0.9882, 0.9800, 0.9885, 0.9849, 0.9858, 0.9859); silent 0.277; factor 3.56 | `informative-mask-results.md`:17–22 |
| Single-run interaction | −0.212 ± 0.069 (t = −3.07), seed 42; outside the six-seed range on raw and rank | `phase-c-lpips-results.md`:100; `seed-block-results.md` §5(c) |
| Sustained trend, arm-level | C4 rises +1.45 % (six-seed mean, range +0.98 to +2.22); C1 at or below zero in two of six seeds | `sustained-trend-results.md`:101, :137, :88 |
| Sustained trend, gaps | LPIPS family 6.33 points (controlled), L1 family 4.00 | `warmup-deconfound-results.md`:316–317, :436 |
| Route-difference caveat | edge ratio does not order errors within the unrestrained group | `paper-context-addendum.md` §22 |

### Section IV

| Claim | Value | Source (line) |
|---|---|---|
| Informative-mask bands | near unity ≥ 0.80; suppressed ≤ 0.50; reused from the registered measurement | `informative-mask-registration.md`:27–31 |
| Informative-mask per-seed C2 | 0.9800–0.9885 (quoted 0.980 to 0.989); other arms 1.03–1.05 | `informative-mask-results.md`:17–22, :42 |
| Checkpoint sweep | C1 − pre at epoch 1 −0.399 ± 0.064 (6.3 SE); C1 − C2 +0.546 ± 0.048 (e1), +0.384 ± 0.052 (e5), +0.700 ± 0.059 (e20); **seed 42, chip-level** | `headline-results.md` B1 table |
| Descriptor families | ORB −0.6127 ± 0.1354 (n = 29 paired; C2 matched 53/130), AKAZE n = 11, MI −1.2600 ± 0.2613 lower bound, refinement never ran, 15.8 % censored at the bound | `B2-B3-audit.md`:161–166, :96–97, :353, :456 |
| Matcher families | KLT, NCC grid, phase correlation × 2 band conversions × urban subset; 6,510 scored comparisons; ordering preserved except two EU-150 urban phase-correlation cells, both far below 2 SE; template matcher widened C2's margin in all eight set × band combinations | `packageA-audit.md`:59, :183; `packageA-results.md`:20–27; corrections-log entry 30 |
| Scatter decomposition | ~86 % of the European gain is scatter; artifacts lost, not reproducible | `phase-c-europe-results.md`:31; corrections-log entry 32 |

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
| 2026-09-13 | Sections II–IV row audit: 36 rows added with source lines; header re-pinned from `284571b` to `a3e1918` | header, II, III, IV |
| 2026-09-13 | Sections I and V drafted; rows for their numbers and for three Section II bounds added at gencp-validation `59612e7` | I, V, II |
| 2026-09-13 | V.1 figure decided (0.593, B2 production path) and given its row; Table I rebuilt from the six-seed block with its inference path; data-availability rows added; rows read at gencp-validation `a415e25` | V.1, Table I, data availability |
| 2026-08-26 | Evidence trail created at study-repo baseline `612b7f6` | all |
| 2026-08-26 | Re-pinned to gencp-validation `main` at `284571b`; repository/branch labels corrected (`612b7f6` was labelled `tubitak-tr`, a GenCP branch). Removed the ODTÜ contamination table, the former Leg 2 (T1/sub-metre) and Leg 3's T1 C1 row — all moved to the second paper. Struck the mediation clause from the B3 row. Former Leg 3 renumbered to Leg 2; primary and secondary rows added as placeholders for the six-seed replication | all |
