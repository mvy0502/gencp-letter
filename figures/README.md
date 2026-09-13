# Figures

Figures are **regenerated** from the study repository, never hand-edited and never
copied from a report PDF. Each figure gets a row here recording the command that
produces it and the study-repo commit it was produced at, so a reviewer question can be
answered by re-running one line.

Study repository: https://github.com/mvy0502/gencp-validation

| File | What it shows | Command (run in the study repo) | Commit |
|---|---|---|---|
| `fig_invention.pdf` (+ `.png`) | Fig. 4 (the panel comparison; numbered by order of appearance, III-F; Fig. 2 until 13 Sep 2026): input render with the input-silent outline, real chip, five arms at seed 45, per-chip edge ratios; chips `ank_3_34` (largest silent fraction, 100%) and `ank_18_29` (median, 85%) chosen by rule | `/opt/homebrew/Caskroom/miniforge/base/envs/gencp/bin/python tubitak/scripts/figures/fig1_invention.py --out ../gencp-letter/figures` (reads per-seed warps under `tubitak/data/tool_runs/`, not committed, plus committed rasters and the seed-45 edge-ratio CSV) | gencp-validation `68b9f83` |

Rules:

1. Vector (PDF/EPS) for plots, high-resolution raster only for imagery panels.
2. Panel labels and axis text in English, sized for a two-column IEEE page.
3. No number appears in a caption unless it has a row in [`../EVIDENCE.md`](../EVIDENCE.md).
| `fig_epoch_curve.pdf` (+ `.png`) | Fig. 3 (the training-time curve, III-E; Fig. 1 until 13 Sep 2026): adversarial penalty against epoch, both families, six seeds; registered reading HELD in both. Grayscale-safe encoding since 13 Sep (black solid circles vs gray dashed squares; was blue vs red) | `epoch_curve_analysis.py --root <root> --out <dir>` (study repository, `tubitak/scripts/seed_eval/`), where `<root>/tubitak/data/tool_runs` may be a symlink to the committed `tubitak/docs/evidence/` (the 24 epoch cells and the six-seed block); regenerated that way on 13 Sep with analysis outputs byte-identical to `evidence/epoch_curve/` | gencp-validation `952cb7b` |
| `fig_design.pdf` (+ `.png`) | Fig. 1 (the $2\times2$ design, II-B): arm names, repository arm codes, the fifth arm outside the grid, the three reported contrasts as arrows; reads no data | `/opt/homebrew/Caskroom/miniforge/base/envs/gencp/bin/python tubitak/scripts/figures/fig_design.py --out ../gencp-letter/figures` | gencp-validation `952cb7b` |
| `fig_sign_replication.pdf` (+ `.png`) | Fig. 2 (sign replication, III-B): the three seed-level contrasts, six seeds each as points against zero, mean and 95% interval behind them; reads the six committed `C45_s{45..50}_modal/C45_per_chip.csv` and refuses to draw unless it reproduces the committed means and intervals to four decimals | `/opt/homebrew/Caskroom/miniforge/base/envs/gencp/bin/python tubitak/scripts/figures/fig_sign_replication.py --out ../gencp-letter/figures` | gencp-validation `952cb7b` |

Files are named by content, not by number: LaTeX numbers figures by order of appearance. Since 13 Sep 2026 the order is design (II-B), sign replication (III-B), curve (III-E), panels (III-F); the enumeration behind that renumbering is `../notes/figure-renumbering-2026-09-13.md`.
