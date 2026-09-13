# The rasterised OpenStreetMap render as a reference candidate — results

**Scored 13 September 2026, 21:31–21:32 UTC**, against
[osm-render-baseline-registration.md](osm-render-baseline-registration.md) (registered at
`a5314b1`, amended at `e665bc7`, before any chip was matched). 130 KARIOS runs, zero
failures, the Table I arms' invocation unchanged (config sha256 `8eaa5bd8cdae066d…`,
KARIOS 2.2.0-dev). Inputs: the committed warped input renders
(`evidence/rasters/input_render_warped/`, first chip sha256 `a1ec648f716f29cb…`), the
reference chips `run/ref/<stem>_warp.tif`. Per-chip statistic: median hypot(dx, dy) over
the KLT rows. **Inference path: one number per chip; the render is seed-invariant; every
comparison below is a paired chip-level difference over 130 chips, D = render − arm,
positive = render worse, SE across chips. No seed-level statement is made.**

## The render alone

| quantity | value |
|---|---|
| mean of per-chip medians | 0.797 px |
| median of per-chip medians | 0.583 px |
| median surviving matches per chip | 30 |
| chips with no match at all | 7 of 130 (5.4 %) |

For comparison, Table I's arms (six-seed means): L1-only 1.393 px mean / 0.975 median /
75 points; LPIPS-only 1.456 / 1.110 / 87; adversarial + L1 2.070 / 1.987 / 62; adversarial
+ LPIPS 2.065 / 1.939 / 60; pretrained 2.563 / 2.588 / 51.

## Raw paired chip-level differences, D = render − arm (px)

Against the pretrained arm (seed-invariant, once): **-1.715 ± 0.091** (t -18.8),
render better on 121 of 123 chips with a match on both.

Against each fine-tuned arm, one chip-level D per confirmatory seed:

| arm | s45 | s46 | s47 | s48 | s49 | s50 | mean | range | min \|t\| |
|---|---|---|---|---|---|---|---|---|---|
| adversarial + L1 | -1.182 ± 0.099 | -1.148 ± 0.102 | -1.196 ± 0.096 | -1.224 ± 0.099 | -1.178 ± 0.095 | -1.185 ± 0.098 | -1.186 | -1.224 … -1.148 | 11.3 |
| L1 only | -0.486 ± 0.076 | -0.559 ± 0.079 | -0.446 ± 0.069 | -0.446 ± 0.074 | -0.444 ± 0.069 | -0.501 ± 0.083 | -0.481 | -0.559 … -0.444 | 6.0 |
| adversarial + LPIPS | -1.191 ± 0.098 | -1.217 ± 0.096 | -1.158 ± 0.095 | -1.129 ± 0.095 | -1.182 ± 0.100 | -1.164 ± 0.090 | -1.173 | -1.217 … -1.129 | 11.8 |
| LPIPS only | -0.562 ± 0.078 | -0.548 ± 0.078 | -0.526 ± 0.080 | -0.544 ± 0.074 | -0.572 ± 0.076 | -0.570 ± 0.078 | -0.554 | -0.572 … -0.526 | 6.5 |

## Equal-count paired differences (per chip K = min of the two counts, best K by KLT score)

*Amendment, 13 September 2026, after the registration's amendment of the same date:* the
pretrained arm's KLT rows on this path **are** retained (`ankara/run/results/`, 130/130
chips reproducing `turkey_karios.csv`), so the row that the first version of this document
called not constructible is constructed from them:

Against the pretrained arm, equal-count: **-1.778 ± 0.109** (t -16.3), over
123 chips (raw row above: -1.715 ± 0.091 over 123); render better on 121 of 123.
No reversal, no material narrowing: the equal-count difference is slightly larger than the
raw one. The band is unchanged.

**Denominators.** Every paired comparison in this document, raw and equal-count, is over
the **123 chips where the render produced at least one match**; the 7 unmatched chips enter
only the point-yield criterion, which counts them. Stated here because the first version
of this document said "over 130 chips" in the inference-path paragraph.

Against the four fine-tuned arms:

| arm | s45 | s46 | s47 | s48 | s49 | s50 | mean | range | min \|t\| |
|---|---|---|---|---|---|---|---|---|---|
| adversarial + L1 | -1.225 ± 0.108 | -1.074 ± 0.119 | -1.166 ± 0.110 | -1.185 ± 0.112 | -1.187 ± 0.121 | -1.185 ± 0.109 | -1.170 | -1.225 … -1.074 | 9.1 |
| L1 only | -0.465 ± 0.086 | -0.478 ± 0.093 | -0.516 ± 0.090 | -0.460 ± 0.072 | -0.389 ± 0.072 | -0.458 ± 0.105 | -0.461 | -0.516 … -0.389 | 4.4 |
| adversarial + LPIPS | -1.248 ± 0.108 | -1.266 ± 0.113 | -1.100 ± 0.098 | -1.118 ± 0.095 | -1.194 ± 0.114 | -1.134 ± 0.097 | -1.177 | -1.266 … -1.100 | 10.5 |
| LPIPS only | -0.584 ± 0.102 | -0.564 ± 0.089 | -0.515 ± 0.089 | -0.593 ± 0.071 | -0.511 ± 0.084 | -0.575 ± 0.096 | -0.557 | -0.593 … -0.511 | 5.7 |

## Registered reading — INTERMEDIATE

- The residual half of WELL is met: D(render − L1-only) ≤ 0 at ≥ 2 SE in all six seeds,
  raw **and** equal-count (minimum |t| 6.0 raw).
- The point half of WELL is not met: the render's median surviving points, 30,
  is far below the L1-only arm's 75.2; and 7 chips
  yield no match at all (5.4 %, below the 20 % POORLY threshold).
- POORLY is not met on either criterion.

**What this is, in the registration's words: intermediate, reported with every number and no
stronger word.** In plain terms: where the render matches, it localises better than every
generated arm, including at equal point counts; it matches on far fewer points and fails
outright on 7 chips. The generated reference's remaining case is point yield and
coverage, not positional accuracy. Per the registration, this earns paragraph length in
Section III; whether it also touches Section I is the supervising session's decision after
seeing it, and that decision is to be recorded here when taken.

## What is not claimed

No sweep, no threshold variation, no second matcher, no extension beyond the 130 Ankara
chips, no transfer claim, no seed-level statement about the render.

## Evidence

`evidence/osm_render_baseline/render_per_chip.csv` (sha256 `42dd3e6ef30c6d67fe32e84009d45ea88d163fca13072f46f4987e789cd74b7b`),
`evidence/osm_render_baseline/render_baseline_summary.json` (sha256 `d4160055858cd02dca6607c675f85c1f945559e7c31a15ab5903ce43d03c9ae0`).
The 130 KARIOS output trees are under `tool_runs/osm_render_baseline/karios/` (not committed;
regenerable from the committed inputs in about a minute).
