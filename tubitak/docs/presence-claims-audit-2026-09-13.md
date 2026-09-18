# Presence-claims audit — enumeration first, checks second

**Enumerated 2026-09-13, committed before any check.** The mirror of the absence-claims audit: every claim that evidence is present, tested as a stranger would test it, in a fresh unauthenticated clone by the path the record gives. Checks and outcomes are appended in a later commit.

## 1. Data-availability statement items (14 items, 173 paths)

- **six-seed block per-chip residuals, points, edge ratios, seeds 45-50** — `tubitak/docs/evidence/C45_s45_modal/C45_per_chip.csv`, `tubitak/docs/evidence/C45_s45_modal/C45_edge_ratio.csv`, `tubitak/docs/evidence/C45_s46_modal/C45_per_chip.csv`, `tubitak/docs/evidence/C45_s46_modal/C45_edge_ratio.csv`, `tubitak/docs/evidence/C45_s47_modal/C45_per_chip.csv`, `tubitak/docs/evidence/C45_s47_modal/C45_edge_ratio.csv`, … (12 paths); expected rows per CSV: 130
- **two-seed block seeds 43-44** — `tubitak/docs/evidence/C45_s43/C45_per_chip.csv`, `tubitak/docs/evidence/C45_s43/C45_edge_ratio.csv`, `tubitak/docs/evidence/C45_s44/C45_per_chip.csv`, `tubitak/docs/evidence/C45_s44/C45_edge_ratio.csv`; expected rows per CSV: 130
- **hardware gate re-run of seed 43** — `tubitak/docs/evidence/C45_s43_modal/C45_per_chip.csv`, `tubitak/docs/evidence/C45_s43_modal/C45_edge_ratio.csv`, `tubitak/docs/evidence/C45_s43_modal_unsorted/C45_per_chip.csv`, `tubitak/docs/evidence/C45_s43_modal_unsorted/C45_edge_ratio.csv`, `tubitak/docs/hardware-gate-results.md`; expected rows per CSV: 130
- **informative-mask test** — `tubitak/docs/evidence/informative_mask/s45_informative_per_chip.csv`, `tubitak/docs/evidence/informative_mask/s46_informative_per_chip.csv`, `tubitak/docs/evidence/informative_mask/s47_informative_per_chip.csv`, `tubitak/docs/evidence/informative_mask/s48_informative_per_chip.csv`, `tubitak/docs/evidence/informative_mask/s49_informative_per_chip.csv`, `tubitak/docs/evidence/informative_mask/s50_informative_per_chip.csv`, … (9 paths); expected rows per CSV: 127
- **equal-count truncation and minimum-match-count sweep** — `tubitak/docs/evidence/common_support/common_support.json`, `tubitak/docs/common-support-registration.md`, `tubitak/docs/common-support-results.md`
- **warm-up and learning-rate probes at seed 43, with loss logs** — `tubitak/docs/evidence/C45_s43_modalwarmup/C45_per_chip.csv`, `tubitak/docs/evidence/C45_s43_modalwarmup/C45_edge_ratio.csv`, `tubitak/docs/warmup-deconfound-registration.md`, `tubitak/docs/warmup-deconfound-results.md`, `tubitak/docs/lr-confound-registration.md`, `tubitak/docs/lr-confound-results.md`, … (7 paths)
- **six-seed training-loss trend** — `tubitak/docs/gates/loss_logs/s45-C1-loss_log.txt`, `tubitak/docs/gates/loss_logs/s45-C2-loss_log.txt`, `tubitak/docs/gates/loss_logs/s45-C4-loss_log.txt`, `tubitak/docs/gates/loss_logs/s45-C5-loss_log.txt`, `tubitak/docs/gates/loss_logs/s46-C1-loss_log.txt`, `tubitak/docs/gates/loss_logs/s46-C2-loss_log.txt`, … (26 paths)
- **epoch sweep, 24 cells** — `tubitak/docs/evidence/C45_s45_modal_e1/C45_per_chip.csv`, `tubitak/docs/evidence/C45_s45_modal_e1/C45_edge_ratio.csv`, `tubitak/docs/evidence/C45_s45_modal_e2/C45_per_chip.csv`, `tubitak/docs/evidence/C45_s45_modal_e2/C45_edge_ratio.csv`, `tubitak/docs/evidence/C45_s45_modal_e5/C45_per_chip.csv`, `tubitak/docs/evidence/C45_s45_modal_e5/C45_edge_ratio.csv`, … (53 paths); expected rows per CSV: 130
- **single-seed checkpoint sweep (B1 and the C45 sweep)** — `tubitak/docs/evidence/B1`, `tubitak/docs/evidence/C45`, `tubitak/docs/headline-registrations.md`, `tubitak/docs/headline-results.md`, `tubitak/docs/phase-c-lpips-results.md`
- **descriptor-family (B3) and matcher-family (packageA) registrations** — `tubitak/docs/evidence/B3/B3_scores.csv`, `tubitak/docs/evidence/B3/B3_summary.json`, `tubitak/docs/evidence/pkgA/pkgA_scores.csv`, `tubitak/docs/evidence/pkgA/pkgA_summary.json`, `tubitak/docs/packageA-registration.md`, `tubitak/docs/packageA-results.md`, … (8 paths)
- **260 seed-independent rasters** — `tubitak/docs/evidence/rasters/input_render_warped`, `tubitak/docs/evidence/rasters/real_chip_bt601`, `tubitak/docs/evidence/rasters/README.md`; expected files per directory: 130
- **OSM-render premise check, 130 chip-level residuals and counts** — `tubitak/docs/evidence/osm_render_baseline/render_per_chip.csv`, `tubitak/docs/evidence/osm_render_baseline/render_baseline_summary.json`, `tubitak/docs/osm-render-baseline-registration.md`, `tubitak/docs/osm-render-baseline-results.md`, `tubitak/scripts/osm_render_baseline/render_baseline_run.py`, `tubitak/scripts/osm_render_baseline/render_baseline_analysis.py`; expected rows per CSV: 130
- **corrections log and every registration (DA ¶1: 'every registration, the corrections log')** — `tubitak/docs/corrections-log.md`, `common-support-registration.md`, `confidence-registration-2.md`, `confidence-registration-3.md`, `confidence-registration.md`, `delivery-registrations.md`, … (28 paths)
- **frozen analysis scripts pinned by hash** — `tubitak/scripts/seed_eval/seed_analysis.py`, `tubitak/scripts/seed_eval/seed_eval_run.py`, `tubitak/scripts/c45_eval/c45_edge_ratio.py`, `tubitak/configs/karios_gencp.json`

## 2. MANIFEST.md rows (399 files with sha256 and byte size) and checkpoints_modal_MANIFEST.md rows (96, off-repository by design; the manifest file itself is checked)

Every MANIFEST.md row is verified by path, hash and size in the clone.

## 3. Commit SHAs cited in the manuscript and its evidence trail (19)

| SHA | cited in |
|---|---|
| `284571b` | EVIDENCE.md |
| `29d2ee1` | notes/section-V-recost-2026-09-13.md |
| `36875ba` | EVIDENCE.md |
| `48ced64` | EVIDENCE.md |
| `55941c7` | notes/section-V-recost-2026-09-13.md |
| `59612e7` | EVIDENCE.md |
| `5e32c23` | EVIDENCE.md, figures/README.md |
| `612b7f6` | EVIDENCE.md |
| `6560c8b` | EVIDENCE.md, manuscript/sections/03-results.tex |
| `68b9f83` | figures/README.md |
| `813d2dd` | EVIDENCE.md |
| `a3e1918` | EVIDENCE.md |
| `a415e25` | EVIDENCE.md |
| `a5314b1` | EVIDENCE.md |
| `c263e4c` | EVIDENCE.md |
| `cadad66` | EVIDENCE.md |
| `e218f29` | EVIDENCE.md, manuscript/sections/02-methods.tex |
| `e665bc7` | EVIDENCE.md |
| `f27f710` | EVIDENCE.md |

## 4. Paths cited in the corrections log and the registrations (147 distinct file/path citations)

| cited in | path |
|---|---|
| corrections-log.md | `../README.md` |
| corrections-log.md | `renderer-tolerance.md` |
| corrections-log.md | `phase-c-config.md` |
| corrections-log.md | `phase-cd-preparation.md` |
| corrections-log.md | `../kaggle/build_kernels.py` |
| corrections-log.md | `phase-d-checks-registration.md` |
| corrections-log.md | `dem-ruggedness-labels-36SXJ.csv` |
| corrections-log.md | `tool-gate-registration.md` |
| corrections-log.md | `tool-gate-registration-2.md` |
| corrections-log.md | `positioning-results.md` |
| corrections-log.md | `positioning-registrations.md` |
| corrections-log.md | `E3-session-log-excerpt.md` |
| corrections-log.md | `T1-benchmark-results.md` |
| corrections-log.md | `T1-audit.md` |
| corrections-log.md | `paper-roadmap.md` |
| corrections-log.md | `delivery-registrations.md` |
| corrections-log.md | `B2-B3-audit.md` |
| corrections-log.md | `phase-c-lpips-registration.md` |
| corrections-log.md | `phase-c-audit.md` |
| corrections-log.md | `warmup-deconfound-results.md` |
| corrections-log.md | `letter-skeleton.md` |
| corrections-log.md | `standing-practices.md` |
| corrections-log.md | `hardware-gate-results.md` |
| corrections-log.md | `phase-d-closeout.md` |
| corrections-log.md | `paper-context-addendum.md` |
| corrections-log.md | `related-work.md` |
| corrections-log.md | `phase-c-results.md` |
| corrections-log.md | `phase-c-lpips-results.md` |
| corrections-log.md | `phase-c-europe-results.md` |
| corrections-log.md | `gcp-veto-rule-results.md` |
| corrections-log.md | `phase-d-audit.md` |
| corrections-log.md | `karios-validation.md` |
| corrections-log.md | `headline-results.md` |
| corrections-log.md | `seed-replication-registration.md` |
| corrections-log.md | `../kaggle/train_c1_c2.py` |
| corrections-log.md | `../modal/gencp_modal.py` |
| corrections-log.md | `packageA-results.md` |
| corrections-log.md | `packageA-audit.md` |
| corrections-log.md | `phase-d-results.md` |
| corrections-log.md | `evidence/MANIFEST.md` |
| corrections-log.md | `evidence/rasters/README.md` |
| corrections-log.md | `corrections-entry-35-draft.md` |
| corrections-log.md | `osm-render-baseline-registration.md` |
| corrections-log.md | `absence-claims-audit-2026-09-13.md` |
| corrections-log.md | `tool-results.md` |
| corrections-log.md | `tubitak/data/tool_runs/B3/B3_run.py` |
| corrections-log.md | `tubitak/docs/paper-context-addendum.md` |
| corrections-log.md | `tubitak/data/*` |
| corrections-log.md | `tubitak/kaggle/train_c1_c2.py` |
| corrections-log.md | `tubitak/scripts/` |
| corrections-log.md | `tubitak/modal/patches/image_folder_sorted.patch` |
| corrections-log.md | `tubitak/data/ankara/run/results/<stem>/` |
| corrections-log.md | `evidence/pkgA/` |
| common-support-registration.md | `phase-d-checks-registration.md` |
| common-support-registration.md | `tubitak/data/tool_runs/C45_s{45..50}_modal/` |
| common-support-registration.md | `tubitak/docs/evidence/common_support/` |
| confidence-registration-2.md | `confidence-registration.md` |
| confidence-registration-2.md | `tubitak/docs/evidence/regD/regD_per_chip.csv` |
| confidence-registration-2.md | `tubitak/data/ankara/run/inputs/<stem>.png` |
| confidence-registration-3.md | `confidence-registration.md` |
| confidence-registration-3.md | `confidence-registration-2.md` |
| confidence-registration-3.md | `tubitak/docs/evidence/regD/regD_per_chip.csv` |
| confidence-registration-3.md | `tubitak/docs/evidence/confidence/per_chip_onnx_ankara.csv` |
| confidence-registration.md | `tubitak/docs/evidence/regD/regD_per_chip.csv` |
| confidence-registration.md | `tubitak/data/eu_holdout/inputs/<stem>.png` |
| confidence-registration.md | `tubitak/data/eu_holdout/eu_inventory.csv` |
| epoch-curve-registration.md | `docs/evidence/checkpoints_modal_MANIFEST.md` |
| epoch-curve-registration.md | `scripts/seed_eval/seed_eval_run.py` |
| epoch-curve-registration.md | `scripts/seed_eval/epoch_sweep_run.py` |
| epoch-curve-registration.md | `scripts/seed_eval/epoch_curve_analysis.py` |
| informative-mask-registration.md | `phase-d-regeneration-STOP.md` |
| informative-mask-registration.md | `phase-c-lpips-registration.md` |
| informative-mask-registration.md | `tubitak/docs/evidence/` |
| lr-confound-registration.md | `warmup-deconfound-registration.md` |
| lr-confound-registration.md | `warmup-deconfound-results.md` |
| lr-confound-registration.md | `hardware-gate-results.md` |
| lr-confound-registration.md | `packageA-registration.md` |
| lr-confound-registration.md | `seed-replication-registration.md` |
| lr-confound-registration.md | `tubitak/outputs/c{2,5}_checkpoints_s43_modalwarmup/checkpoints/` |
| lr-confound-registration.md | `tubitak/data/tool_runs/C45_s43_modalwarmup/` |
| lr-confound-registration.md | `tubitak/docs/evidence/` |
| osm-render-baseline-registration.md | `evidence/rasters/input_render_warped/` |
| osm-render-baseline-registration.md | `scripts/osm_render_baseline/render_baseline_run.py` |
| osm-render-baseline-registration.md | `scripts/osm_render_baseline/render_baseline_analysis.py` |
| osm-render-baseline-registration.md | `tubitak/data/ankara/run/results/<stem>/*/KLT_matcher_*.csv` |
| packageA-registration.md | `packageA-urban-chips.csv` |
| phase-c-lpips-registration.md | `headline-results.md` |
| phase-c-lpips-registration.md | `phase-c-config.md` |
| phase-c-lpips-registration.md | `../../models/pix2pix_model.py` |
| phase-c-lpips-registration.md | `published-paper-audit.md` |
| phase-c-lpips-registration.md | `phase-c-results.md` |
| phase-c-lpips-registration.md | `phase-c3-results.md` |
| phase-c-lpips-registration.md | `phase-c-lpips-results.md` |
| phase-c-lpips-registration.md | `../kaggle/build_kernels.py` |
| phase-c-lpips-registration.md | `../kaggle/train_c1_c2.py` |
| phase-c-lpips-registration.md | `tubitak/data/paper/gencp_text.txt` |
| plugin-gate-registration-C.md | `tubitak/configs/karios_gencp.json` |
| plugin-gate-registration-C2.md | `common-support-registration.md` |
| plugin-gate-registration-C2.md | `common-support-results.md` |
| plugin-gate-registration-C2.md | `tubitak/scripts/common_support/common_support_rescore.py` |
| plugin-gate-registrations.md | `plugin-results.md` |
| plugin-gate-registrations.md | `standing-practices.md` |
| plugin-gate-registrations.md | `tool-gate-registration-2.md` |
| plugin-gate-registrations.md | `tool-registrations-3.md` |
| plugin-gate-registrations.md | `tool-results.md` |
| plugin-gate-registrations.md | `tubitak/scripts/osm_to_raster.py` |
| plugin-gate-registrations.md | `tubitak/gencp_core/rasterize.py` |
| plugin-gate-registrations.md | `tubitak/data/tool_runs/task4/acc_census.csv` |
| plugin-gate-registrations.md | `tubitak/data/geofabrik/chips/<stem>.osm.pbf` |
| plugin-gate-registrations.md | `tubitak/data/karios/reference/satellite/<stem>.tif` |
| plugin-gate-registrations.md | `tubitak/data/rasteriser/chips/<stem>.tif` |
| plugin-gate-registrations.md | `tubitak/data/rasteriser/chips_clc/` |
| plugin-gate-registrations.md | `tubitak/scripts/osm_to_raster.make_chip` |
| plugin-gate-registrations.md | `tubitak/scripts/tile_pipeline.py` |
| positioning-registrations.md | `positioning-results.md` |
| positioning-registrations.md | `corrections-log.md` |
| seed-replication-registration.md | `phase-c-lpips-registration.md` |
| seed-replication-registration.md | `standing-practices.md` |
| seed-replication-registration.md | `paper-context-addendum.md` |
| seed-replication-registration.md | `phase-c-audit.md` |
| seed-replication-registration.md | `headline-registrations.md` |
| seed-replication-registration.md | `phase-c-config.md` |
| seed-replication-registration.md | `../kaggle/train_c1_c2.py` |
| seed-replication-registration.md | `gates/` |
| seed-replication-registration.md | `hardware-gate-results.md` |
| seed-replication-registration.md | `tubitak/scripts/c45_eval/` |
| seed-replication-registration.md | `tubitak/scripts/seed_eval/seed_analysis.py` |
| seed-replication-registration.md | `tubitak/kaggle/train_c1_c2.py` |
| seed-replication-registration.md | `tubitak/scripts/` |
| seed-replication-registration.md | `tubitak/modal/patches/image_folder_sorted.patch` |
| seed-replication-registration.md | `tubitak/data/tool_runs/C45_s{43,44}/` |
| sustained-trend-registration.md | `warmup-deconfound-results.md` |
| sustained-trend-registration.md | `warmup-deconfound-registration.md` |
| sustained-trend-registration.md | `seed-block-results.md` |
| sustained-trend-registration.md | `docs/gates/` |
| tool-gate-registration-2.md | `tool-gate-registration.md` |
| tool-gate-registration-2.md | `plugin-gate-registrations.md` |
| tool-gate-registration-2.md | `plugin-results.md` |
| tool-gate-registration-2.md | `tubitak/data/rasteriser/chips/` |
| tool-gate-registration-2.md | `tubitak/data/rasteriser/chips_clc/<stem>.tif` |
| tool-gate-registration-2.md | `tubitak/data/karios/reference/satellite/<stem>.tif` |
| tool-gate-registration-2.md | `tubitak/data/tool_runs/task3/` |
| tool-gate-registration-2.md | `tubitak/data/rasteriser/chips/<stem>.tif` |
| tool-gate-registration-2.md | `tubitak/data/rasteriser/chips_clc/` |
| tool-gate-registration.md | `tool-gate-registration-2.md` |
| tool-gate-registration.md | `tubitak/tool/gencp_ref.py` |
| tool-registration-4.md | `tool-results.md` |

## 5. The repository URL printed in the manuscript

`https://github.com/mvy0502/gencp-validation` — reachable without credentials?

---

## Checks and outcomes — appended 13 September 2026

**Method.** `git clone https://github.com/mvy0502/gencp-validation.git` into a scratch directory
with `GIT_TERMINAL_PROMPT=0` and an empty credential helper; the clone landed on `main` at
`2adc706` (GitHub's default branch is `main`; the remote also carries `master`, the upstream
fork base of March 2026, and two workspace branches, `tubitak-tool` and `tubitak-tr`). Every
check below ran inside that clone, by the path the record gives, never by search. Hashes are
sha256 of the file in the clone; counts are rows or files in the clone.

### 1. Data-availability items (14 items, 173 paths)

| item | outcome | method and result |
|---|---|---|
| six-seed block, 12 CSVs | **(a)** | all present, 130 rows each |
| two-seed block, 4 CSVs | **(a)** | present, 130 rows each |
| hardware gate, 4 CSVs + results | **(a)** | present, 130 rows each |
| informative-mask test, 6 CSVs + JSON + registration + results | **(a)** | present, 127 rows each as the results document states |
| equal-count truncation and minimum-match-count sweep | **(a)** | `common_support.json`, registration and results present |
| warm-up and LR probes, seed 43, with loss logs | **(a)** | present |
| six-seed training-loss trend, 24 loss logs | **(a)** | all 24 present |
| epoch sweep, 24 cells (48 CSVs) + curve outputs + registration + results + checkpoint manifest | **(a)** | all 53 present, 130 rows per cell CSV; `epoch_curve_per_seed.csv` has 12 rows (two families × six seeds), which is its design, not a shortfall |
| single-seed checkpoint sweep (B1, C45) | **(a)** | present |
| B3 and packageA registrations and evidence | **(a)** | present |
| 260 rasters | **(b) → corrected** | 130 + 130 files present under `rasters/`, every hash and size matching — but the manifest rows named them without the `rasters/` prefix (entry 48) |
| OSM-render premise check | **(a) files; (b) one number** | CSV present with 130 rows; JSON present and its values match the results document except the surviving-point median, 29.5 in the JSON and printed as 30 (entry 49) |
| corrections log and every registration | **(a)** | 27 registration files and the log present under `tubitak/docs/` (the enumeration listed them without the prefix; the check with the prefix passes) |
| frozen analysis scripts and the KARIOS config | **(a)** | present |

### 2. MANIFEST.md, 399 rows — the item entry 35 was about

138 rows verified by path, hash and size. **261 failed on the first pass:** the 260 raster rows
by path (files present under `rasters/`, hashes and sizes all matching), and one stale row for
`render_baseline_summary.json` (entry 50). After the corrections in this commit the manifest
was re-verified in the fresh clone: see the closing line of this file.
`checkpoints_modal_MANIFEST.md` is present; its 96 rows describe off-repository files by
design and were verified from the Kaggle copy on 13 September.

### 3. Commit SHAs (19)

All 19 resolve in the fresh clone, including `e218f29`, the audited upstream commit, which
resolves because this repository is a fork of `telespazio-tim/GenCP` and shares its history;
the GitHub API independently returns it (2025-03-20). **19 of 19.**

### 4. Cited paths (147 distinct citations in the corrections log and the registrations)

116 resolve as written. 31 do not, in three groups: (i) `tubitak/data/...` paths, which name
the working machine's gitignored data and are off-repository by design (`BACKUP.md`) — 20
citations, outcome (a) by design; (ii) placeholder patterns (`<stem>`, `{45..50}`, `*`) — a
notation, not a path; (iii) **paths written relative to `tubitak/` in three registrations**
(`scripts/seed_eval/...`, `docs/evidence/...`, `docs/gates/`) that a stranger typing them from
the repository root or from `docs/` would not find — **(b)**, corrected by dated path notes in
`epoch-curve-registration.md`, `osm-render-baseline-registration.md` and
`sustained-trend-registration.md`. One cited path, `tubitak/data/tool_runs/B3/B3_run.py`, is
entry 22's deleted harness and is expected absent.

### 5. The URL

`https://github.com/mvy0502/gencp-validation` returns HTTP 200 without credentials; the
repository is public; `ls-remote` succeeds with no credential helper.

### A.6 — "available on request"

The statement names no addressee; the author line reads "and co-author" and the letter has no
corresponding author or contact address. Recorded in the letter's submission checklist as an
open item tied to the author line, to close when it is filled. Not invented here.

### A.7 — the plain reader path

From the front page a stranger is not led to the paper's evidence. `README.md` is the
institution-facing Turkish front page for the two QGIS plugins; its one link to the study
(`docs/dogrulama-calismasi.md`) reaches `tubitak/docs/` and the corrections log but never names
`evidence/` or `MANIFEST.md`; and `tubitak/README.md` told a reader already inside this
repository that the study had "moved to gencp-validation". The evidence is present and, once
the manifest paths are right, obtainable — but only by exploring. Two things done: a dated
note at the head of `tubitak/README.md` saying where the study's record is, and the letter's
data-availability statement now names `tubitak/docs/` and `tubitak/docs/evidence/MANIFEST.md`
explicitly. Not done, proposed: an English paragraph on the front page pointing readers of the
letter to `tubitak/docs/`, since that page is the institution's and not this session's to
rewrite.

*13 September, later (P9 A.2): the proposal was approved and the paragraph added as a separate English section at the end of the front page, the Turkish content untouched. The manifest is now also a check: see practice 10's mechanism note and `scripts/manifest_paths_check.py` (P9 A.1).*

**Closing line.** The corrections were committed at `359355d` and pushed; the fresh clone was pulled to that commit and the manifest re-verified by path, hash and size: 398 of 398 live rows pass, 0 fail, and the one row marked superseded is skipped by design. The first attempt at this commit was refused by the practice-15 pre-commit hook, because `epoch-curve-registration.md` predates the gate and mentions its self-test without a token; the gate was run on the unchanged script and its line pasted as a dated note before the commit was retried. Recorded 13 September 2026.

*Amendment, 18 September 2026 (P17 C.2).* The front page and the path A.7 describes belong to `gencp-validation` as delivered; in this repository the delivery's `docs/dogrulama-calismasi.md` was removed from the tree in the P17 commit (last at `fff6c4e`), and the root README of 14 September is the reader's door. A.7's description of the 13 September state is unchanged.

*Correction, 18 September 2026, same day.* This amendment was committed at `20534bd` before the removals it describes had landed, because the removal command in that step failed silently; the removals landed in the next commit, and the files it names last exist at `20534bd`, not `fff6c4e`.
