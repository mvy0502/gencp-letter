# Figures

Figures are **regenerated** from the study repository, never hand-edited and never
copied from a report PDF. Each figure gets a row here recording the command that
produces it and the study-repo commit it was produced at, so a reviewer question can be
answered by re-running one line.

Study repository: https://github.com/mvy0502/gencp-validation

| File | What it shows | Command (run in the study repo) | Commit |
|---|---|---|---|
| `fig_invention.pdf` (+ `.png`) | Fig. 2 (the panel comparison; numbered by order of appearance, III-F): input render with the input-silent outline, real chip, five arms at seed 45, per-chip edge ratios; chips `ank_3_34` (largest silent fraction, 100%) and `ank_18_29` (median, 85%) chosen by rule | `/opt/homebrew/Caskroom/miniforge/base/envs/gencp/bin/python tubitak/scripts/figures/fig1_invention.py --out ../gencp-letter/figures` (reads per-seed warps under `tubitak/data/tool_runs/`, not committed, plus committed rasters and the seed-45 edge-ratio CSV) | gencp-validation `68b9f83` |

Rules:

1. Vector (PDF/EPS) for plots, high-resolution raster only for imagery panels.
2. Panel labels and axis text in English, sized for a two-column IEEE page.
3. No number appears in a caption unless it has a row in [`../EVIDENCE.md`](../EVIDENCE.md).
| `fig_epoch_curve.pdf` (+ `.png`) | Fig. 1 (the training-time curve, III-E): adversarial penalty against epoch, both families, six seeds; registered reading HELD in both | `epoch_sweep_run.py` then `epoch_curve_analysis.py --root <GenCP working repo> --out <dir>` (study repository, `tubitak/scripts/seed_eval/`); reads the 24 epoch cells scored 13 Sep 2026 and the six-seed block | gencp-validation `5e32c23` |

Files are named by content, not by number: LaTeX numbers figures by order of appearance, and the curve (III-E) precedes the panels (III-F).
