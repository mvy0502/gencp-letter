#!/usr/bin/env python3
"""The letter's sign-replication figure (Fig. 2 from P9, 13 Sep 2026): the three seed-level
contrasts of Section III-B, six confirmatory seeds each, every seed as a point against a zero
line; the seed-level mean and its 95% t-interval (df = 5) drawn BEHIND the points in gray,
because in this letter the registered reading is the sign replication (P = 1/64) and the
interval is reported, not required. The render of III-L is deliberately absent: chip-level,
seed-invariant, a different inference path.

Reads docs/evidence/C45_s{45..50}_modal/C45_per_chip.csv (committed; sha256 in MANIFEST.md).
Inference path: per chip, the median KLT residual over the arm's own matches; per seed, the
mean over 130 chips of the paired difference (seed_analysis.py seed_mean); across seeds,
mean, sd (ddof=1), t_{0.975,5} (seed_analysis.py across_seeds). Before drawing, the script
asserts that it reproduces the committed numbers of seed-block-results.md section 1 and
5(a) to four decimals; a figure drawn from numbers that disagree with the record is refused.

Usage: fig_sign_replication.py --out DIR   (writes fig_sign_replication.pdf and .png).
"""
import csv, statistics as st, sys
from math import sqrt
from pathlib import Path
if len(sys.argv) != 3 or sys.argv[1] != "--out":
    sys.exit("usage: fig_sign_replication.py --out DIR")
OUT = Path(sys.argv[2]); OUT.mkdir(parents=True, exist_ok=True)
ROOT = Path(__file__).resolve().parents[2] / "docs" / "evidence"
SEEDS = (45, 46, 47, 48, 49, 50)
T975_5 = 2.570581835636314          # scipy.stats.t.ppf(0.975, 5), the value seed_analysis.py uses
CONTRASTS = [  # (panel title, minuend, subtrahend, committed mean, committed CI)
    ("primary\nLPIPS-only $-$ adv.+LPIPS", "C5", "C4", -0.6091, (-0.6335, -0.5847)),
    ("L1 family\nadv.+L1 $-$ L1-only", "C1", "C2", +0.6773, (+0.6172, +0.7374)),
    ("secondary\nLPIPS-only $-$ L1-only", "C5", "C2", +0.0626, (+0.0273, +0.0979)),
]
def per_seed(a, b):
    out = []
    for s in SEEDS:
        rows = list(csv.DictReader(open(ROOT / f"C45_s{s}_modal" / "C45_per_chip.csv")))
        assert len(rows) == 130, s
        out.append(st.mean(float(r[f"{a}_med"]) - float(r[f"{b}_med"]) for r in rows))
    return out
def across(v):
    m, sd = st.mean(v), st.stdev(v); se = sd / sqrt(len(v))
    return m, (m - T975_5 * se, m + T975_5 * se)
data = []
for title, a, b, m_ref, ci_ref in CONTRASTS:
    v = per_seed(a, b); m, ci = across(v)
    assert round(m, 4) == m_ref and round(ci[0], 4) == ci_ref[0] and round(ci[1], 4) == ci_ref[1], (title, m, ci)
    data.append((title, v, m, ci))
    print(f"{title.splitlines()[0]:<10} " + " ".join(f"{x:+.4f}" for x in v) + f"  mean {m:+.4f} CI [{ci[0]:+.4f}, {ci[1]:+.4f}]  "
          f"{sum(x < 0 for x in v)}/6 below zero")
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"pdf.fonttype": 42, "ps.fonttype": 42, "font.family": "sans-serif"})
fig, axes = plt.subplots(1, 3, figsize=(3.5, 1.9))
for ax, (title, v, m, ci) in zip(axes, data):
    ax.axhspan(ci[0], ci[1], color="0.85", lw=0, zorder=1)                 # interval: behind, light
    ax.hlines(m, 0.55, 1.45, color="0.45", lw=1.0, zorder=2)              # mean: behind, mid-gray
    ax.axhline(0, color="black", lw=0.7, zorder=3)                         # zero line
    xs = [0.7 + 0.12 * i for i in range(6)]
    ax.scatter(xs, v, s=14, color="black", zorder=4)                        # the six seeds: foreground
    for x, y, s in zip(xs, v, SEEDS):
        ax.annotate(str(s), (x, y), xytext=(0, 3.5), textcoords="offset points", ha="center", fontsize=4, color="0.3")
    n = sum(x < 0 for x in v) if m < 0 else sum(x > 0 for x in v)
    ax.text(0.5, 0.04 if m > 0 else 0.90, f"{n}/6 {'below' if m < 0 else 'above'} 0", transform=ax.transAxes, ha="center", fontsize=6, weight="bold")
    lo, hi = min(min(v), 0), max(max(v), 0); pad = 0.18 * (hi - lo)
    ax.set_ylim(lo - pad, hi + pad); ax.set_xlim(0.5, 1.5); ax.set_xticks([])
    ax.set_title(title, fontsize=6, pad=3); ax.tick_params(axis="y", labelsize=5.5)
    for sp in ("top", "right", "bottom"): ax.spines[sp].set_visible(False)
axes[0].set_ylabel("seed-level contrast $\\Delta_s$, px", fontsize=6)
fig.tight_layout(w_pad=0.6)
fig.savefig(OUT / "fig_sign_replication.pdf"); fig.savefig(OUT / "fig_sign_replication.png", dpi=300)
print("wrote", OUT / "fig_sign_replication.pdf")
