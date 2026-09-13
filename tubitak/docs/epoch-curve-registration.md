# Registration — the training-time curve at six seeds (letter Fig. 2 as planned; Fig. 1 as compiled, since III-E precedes III-F)

**Registered 13 September 2026, before any cell was scored.** Nothing below has been
computed at the time of this commit; the checkpoints were being pulled from the Modal
volume while it was written. The results document will cite this commit.

## What is measured

For each confirmatory seed S in 45–50 and each epoch E in {1, 2, 5, 10}, the four
fine-tuned arms' epoch-E generator checkpoints (pulled from the Modal volume, sha256 in
`docs/evidence/checkpoints_modal_MANIFEST.md`) are run through the **frozen** per-seed
evaluation runner `scripts/seed_eval/seed_eval_run.py` (commit `48ced64`, sha256
`3df87c807cefce86…`) with `--variant modal_e{E}`: inference on the 130 Ankara inputs
with the dropout shim pinned to seed 42 (AMENDMENT SEED-a), the registered warp geometry,
KARIOS with the unchanged config (sha256 `8eaa5bd8cdae066d…`), per-chip median
residual. Epoch 20 is the six-seed block itself (`C45_s{S}_modal`), not re-run.

Statistic, per seed and epoch: the adversarial penalty D = chip mean over 130 chips of
(adversarial arm's per-chip median − its non-adversarial counterpart's):
D_LPIPS = mean(C4 − C5), D_L1 = mean(C1 − C2). Sign: positive = adversarial arm worse.
Inference at seed level: one D per seed per epoch; variability across seeds.

## Registered reading (one per family)

**D > 0 at every scored epoch in every seed** — 6/6 at each of the five epochs. Under a
null of no effect the six signs at one epoch agree with probability 1/64; the five epochs
are not independent (same runs at later epochs) and no joint probability is claimed.
A single negative cell fails the reading for that family. If it fails, the figure is still
drawn, the failing seed and epoch are named, and the text claims only what held.

## Exploratory reading (reported, no claim)

The shape: D(2) < D(1) and D(20) > D(2) ("dip then grow"), counted per seed per family.
The seed-42 curves showed it in both families (LPIPS: 0.334 → 0.254 → 0.441 → 0.496 →
0.487; L1: 0.546 → 0.402 → 0.384 → 0.552 → 0.700, chip-level, single seed). Band: the
count is reported; 6/6 would be described as "replicates", anything less as "not stable
across seeds". No mechanism is attached to the shape in either case.

## Invariances

Identical across all 120 cells (6 seeds × 5 epochs × 4 arms): the 130 inputs and
references, the warp geometry, the KARIOS config, the inference shim (seed 42), the
frozen runner. The only varying elements are the training seed and the epoch. The
pretrained arm does not enter any D.

## What it is and is not

A training-time curve is confounded with convergence: the arms are trained longer, not
dosed. The figure is named accordingly ("training-time curve", never "dose-response"),
is support for Section IV-B's cold-discriminator row and for III-E, and is not the spine.
The Kaggle seed-42 curves are reported beside it and never pooled with it (hardware gate:
NOT POOLED).

## Scripts (committed with this registration)

- `scripts/seed_eval/epoch_sweep_run.py` — routing only; stages symlinks after verifying
  each checkpoint's sha256 against the pull log, then invokes the frozen runner. sha256
  `c223f9bb95b16347f9381aca33f0d9b65bcd717d0e246437ed23929630436254`.
- `scripts/seed_eval/epoch_curve_analysis.py` — the readings above and the figure.
  sha256 `1e5d8731d0f5830341dd6b123b4904c417de0d878fc6b0814e19fad7c050c807`. **Known-false test run before registration:** `--self-test` plants a
  single negative cell (seed 47, epoch 5) in an otherwise positive table and must report
  FAILED, and reports HELD on the all-positive table; both scripts refuse unknown
  arguments. Output of the run at registration time: "all-positive -> HELD; planted
  negative at seed 47 epoch 5 -> FAILED; self-test passed".

## Consequence rules, committed now

- Registered reading holds in both families: the letter's III-E states it at seed level
  and the figure replaces the seed-42 curve as Fig. 2.
- Fails in one family: that family's curve is shown with the failing cells marked; the
  text says which epochs and seeds; no "at every epoch" sentence for that family.
- The exploratory shape gets no band-hit language either way.

*Path note, 2026-09-13 (presence-claims audit): `scripts/seed_eval/...` and `docs/evidence/checkpoints_modal_MANIFEST.md` above are written relative to `tubitak/`; from the repository root they are `tubitak/scripts/seed_eval/seed_eval_run.py`, `tubitak/scripts/seed_eval/epoch_sweep_run.py`, `tubitak/scripts/seed_eval/epoch_curve_analysis.py` and `tubitak/docs/evidence/checkpoints_modal_MANIFEST.md`. A stranger typing the paths as written would not find the files.*

*Gate note, 2026-09-13: this registration predates the mechanical self-test gate (practice 15, adopted 13 September) and the pre-commit hook refused to accept the path note above without a gate token. The self-test it describes was re-run under the project interpreter through the gate, with no change to the script:*
`self-test gate: PASS 8b26310ff4101714 scripts/seed_eval/epoch_curve_analysis.py /opt/homebrew/Caskroom/miniforge/base/envs/gencp/bin/python 2026-09-13T22:23Z`
