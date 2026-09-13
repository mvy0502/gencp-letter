#!/usr/bin/env python3
"""The letter's panel figure (Fig. 2 as compiled; the skeleton called it Fig. 1): what each arm renders where the input asserts nothing.

Two Ankara chips from the six-seed panel, chosen by rule and not by eye:
  (a) the chip with the LARGEST input-silent fraction  -- the ceiling case: almost
      nothing in the input, so everything an arm draws is invented;
  (b) the chip whose input-silent fraction is the MEDIAN of the 130 -- the typical case.
For each: the input render (BT.601 gray, as the mask sees it), the real Sentinel-2 chip,
and the five arms at seed 45 (pretrained is seed-invariant), all BT.601 gray. The
input-silent mask (Sobel <= 20 on the input) is outlined in the input panel. Each arm
panel is labelled with that chip's edge ratio from the committed per-chip CSV.

Sources: tool_runs/C45_s45_modal/warp/{input,C1,C2,C4,C5}/<stem>.tif (per-seed warps,
not committed; BACKUP.md), tool_runs/pkgA/gray/ank130/pretrained/bt601/<stem>.tif,
docs/evidence/rasters/real_chip_bt601/<stem>.tif (committed), and
docs/evidence/C45_s45_modal/C45_edge_ratio.csv (committed). Mask functions copied
verbatim from scripts/c45_eval/c45_edge_ratio.py so the outline is the measurement's.

Usage: fig1_invention.py --out DIR   (writes fig1_invention.pdf and .png). No other args.
"""
import csv, statistics as st, sys
from pathlib import Path
import numpy as np, rasterio
from scipy.ndimage import sobel
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

args = sys.argv[1:]
if len(args) != 2 or args[0] != "--out":
    sys.exit("usage: fig1_invention.py --out DIR")
OUT = Path(args[1]); OUT.mkdir(parents=True, exist_ok=True)
GENCP = Path("/Users/vedat/Documents/GenCP-Generative-Goruntu-Uretimi-OpenStreetMap/tubitak/data/tool_runs")
HERE = Path(__file__).resolve().parents[2]
EVID = HERE / "docs" / "evidence"
SEED = 45
THRESH = 20.0

def grad_mag(g):
    return np.hypot(sobel(g.astype(float), 0), sobel(g.astype(float), 1))
def bt601(rgb):
    return np.round(0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]).astype(np.uint8)
def read1(p):
    with rasterio.open(p) as s:
        a = s.read()
    return a[0] if a.shape[0] == 1 else bt601(a)

rows = list(csv.DictReader(open(EVID / f"C45_s{SEED}_modal" / "C45_edge_ratio.csv")))
assert len(rows) == 130
sil = {r["stem"]: float(r["silent_frac"]) for r in rows}
stem_max = max(sil, key=sil.get)
med = st.median(sil.values())
stem_med = min(sil, key=lambda s: (abs(sil[s] - med), s))
ratio = {r["stem"]: r for r in rows}

ARMS = [("pretrained", lambda s: GENCP / f"pkgA/gray/ank130/pretrained/bt601/{s}.tif", "pretrained"),
        ("C1", lambda s: GENCP / f"C45_s{SEED}_modal/warp/C1/{s}.tif", "adversarial + L1"),
        ("C2", lambda s: GENCP / f"C45_s{SEED}_modal/warp/C2/{s}.tif", "L1 only"),
        ("C4", lambda s: GENCP / f"C45_s{SEED}_modal/warp/C4/{s}.tif", "adversarial + LPIPS"),
        ("C5", lambda s: GENCP / f"C45_s{SEED}_modal/warp/C5/{s}.tif", "LPIPS only")]

fig, axes = plt.subplots(2, 7, figsize=(7.16, 2.35))
for i, (stem, tag) in enumerate([(stem_max, "largest input-silent fraction"), (stem_med, "median input-silent fraction")]):
    inp = read1(GENCP / f"C45_s{SEED}_modal/warp/input/{stem}.tif")
    mask = grad_mag(inp) <= THRESH
    real = read1(EVID / "rasters" / "real_chip_bt601" / f"{stem}.tif")
    panels = [(inp, "input render\n(mask source)"), (real, "real Sentinel-2")]
    for key, pf, label in ARMS:
        panels.append((read1(pf(stem)), f"{label}\nr = {float(ratio[stem][key]):.2f}"))
    for j, (img, label) in enumerate(panels):
        ax = axes[i, j]; ax.imshow(img, cmap="gray", vmin=0, vmax=255, interpolation="nearest")
        if j == 0:
            ax.contour(mask.astype(float), levels=[0.5], colors=["#d62728"], linewidths=0.5)
        ax.set_xticks([]); ax.set_yticks([])
        if i == 0: ax.set_title(label, fontsize=6, pad=2)
        else: ax.set_xlabel(label, fontsize=6, labelpad=1)
    axes[i, 0].set_ylabel(f"({'ab'[i]}) {stem}\nsilent {100*sil[stem]:.0f}%", fontsize=6)
plt.subplots_adjust(left=0.05, right=0.995, top=0.88, bottom=0.14, wspace=0.05, hspace=0.12)
fig.savefig(OUT / "fig1_invention.pdf"); fig.savefig(OUT / "fig1_invention.png", dpi=300)
print("chips:", stem_max, f"silent={sil[stem_max]:.3f}", "|", stem_med, f"silent={sil[stem_med]:.3f} (median {med:.3f})")
for s in (stem_max, stem_med):
    print(s, {k: round(float(ratio[s][k]), 2) for k in ("pretrained", "C1", "C2", "C4", "C5")})
