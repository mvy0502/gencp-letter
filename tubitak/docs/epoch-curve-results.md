# The training-time curve at six seeds — results

**Scored 13 September 2026** against [epoch-curve-registration.md](epoch-curve-registration.md)
(committed `36875ba` before any cell was scored). Driver wall clock 15:26–16:44 UTC; 24 cells
(6 seeds × epochs 1, 2, 5, 10; four arms each) through the frozen runner
`scripts/seed_eval/seed_eval_run.py` (commit `48ced64`, sha256 `3df87c807cefce86…`), shim
seed 42, KARIOS config unchanged; epoch 20 is the six-seed block. Per-chip artifacts for
every cell are committed under `evidence/C45_s{S}_modal_e{E}/` and listed in
`evidence/MANIFEST.md`; the analysis outputs under `evidence/epoch_curve/`. Sign: penalty =
adversarial arm − non-adversarial counterpart, chip mean of per-chip medians; positive =
adversarial arm worse. Inference at seed level.

## Registered reading — HELD in both families

Penalty positive at every scored epoch in every seed: **6/6 at each of the five epochs, in
both families.** No cell is negative. The consequence rule for "holds in both families"
applies: the letter's III-E states it at seed level and the six-seed figure replaces the
seed-42 curve as the letter's training-time figure (numbered Fig. 1 in the compiled letter; the skeleton called it Fig. 2).

### LPIPS family, D = mean(C4 − C5), px

| seed | e1 | e2 | e5 | e10 | e20 | dip then grow |
|---|---|---|---|---|---|---|
| 45 | +0.3008 | +0.2433 | +0.4931 | +0.5564 | +0.6153 | yes |
| 46 | +0.2187 | +0.2447 | +0.4254 | +0.5546 | +0.6462 | no |
| 47 | +0.2914 | +0.3144 | +0.5216 | +0.5513 | +0.6162 | no |
| 48 | +0.2904 | +0.2612 | +0.4725 | +0.4096 | +0.5942 | yes |
| 49 | +0.2748 | +0.2584 | +0.4955 | +0.5413 | +0.6054 | yes |
| 50 | +0.1942 | +0.2253 | +0.5858 | +0.5771 | +0.5775 | no |
| **mean** | +0.2617 | +0.2579 | +0.4990 | +0.5317 | +0.6091 | 3/6 |
| sd | 0.0443 | 0.0305 | 0.0533 | 0.0609 | 0.0233 | |

### L1 family, D = mean(C1 − C2), px

| seed | e1 | e2 | e5 | e10 | e20 | dip then grow |
|---|---|---|---|---|---|---|
| 45 | +0.5813 | +0.4793 | +0.4463 | +0.4489 | +0.6749 | yes |
| 46 | +0.4096 | +0.3894 | +0.4022 | +0.6067 | +0.5868 | yes |
| 47 | +0.5083 | +0.4400 | +0.5318 | +0.6452 | +0.7010 | yes |
| 48 | +0.5136 | +0.5631 | +0.4964 | +0.5349 | +0.7544 | no |
| 49 | +0.5169 | +0.4350 | +0.3183 | +0.5798 | +0.7024 | yes |
| 50 | +0.5981 | +0.5293 | +0.3409 | +0.6351 | +0.6444 | yes |
| **mean** | +0.5213 | +0.4727 | +0.4226 | +0.5751 | +0.6773 | 5/6 |
| sd | 0.0667 | 0.0646 | 0.0847 | 0.0736 | 0.0573 | |

## Exploratory reading — not stable across seeds, not claimed

Dip-then-grow (D(2) < D(1) and D(20) > D(2)) appears in **3 of 6** seeds under LPIPS and
**5 of 6** under L1. The registered band was 6/6 = "replicates", anything less = "not
stable across seeds". The shape read off seed 42 (LPIPS 0.334 → 0.254 → 0.441 → 0.496 →
0.487) is therefore reported and not claimed; at six seeds the LPIPS means at epochs 1 and 2
are indistinguishable (0.262, 0.258) and the dip is absent from the mean. No mechanism is
attached to the shape. Nothing beyond the registered reading is claimed from this figure.

## What changed for the letter

- The reserve cut's strongest objection — that Fig. 2's terminal point was seed 42's 0.487,
  outside the six-seed range — no longer applies: the terminal point is the block's own
  0.609 ± 0.023 (seed sd). The other objection stands: a training-time curve is confounded
  with convergence, and the figure is named and captioned accordingly. Support, not spine.
- The seed-42 curves are quoted as the generating run and never pooled (NOT POOLED).

## Provenance

- Checkpoints: `evidence/checkpoints_modal_MANIFEST.md` (96 files pulled 13 Sep from the Modal
  volume; sha256 verified at staging by `epoch_sweep_run.py`).
- Scripts: `epoch_sweep_run.py` and `epoch_curve_analysis.py` at the registration commit; the
  analysis self-test (planted negative → FAILED) was run before registration.
- Per-cell edge ratios were also produced by the runner as a by-product; they are committed,
  unregistered, and not read by anything.

*Numbering note, 2026-09-13 (P9 C.3): from this date the compiled letter numbers the curve Fig. 3 (two figures entered ahead of it); line 18's "Fig. 1" and line 57's skeleton-era "Fig. 2" refer to the same figure. Its encoding is grayscale-safe from this date; the numbers are unchanged.*
