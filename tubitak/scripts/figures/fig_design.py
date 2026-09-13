#!/usr/bin/env python3
"""The letter's design figure (Fig. 1 from P9, 13 Sep 2026): the 2x2 loss factorial with the
letter's arm names and the study repository's arm codes in each cell, the pretrained arm
outside the grid, and the three seed-level contrasts of Section III-B drawn as arrows from
subtrahend to minuend in the direction the letter reports them. No data is read: the
figure is the design, and the arm codes are those of C45_per_chip.csv (pre, C1, C2, C4, C5).
Grayscale by construction (black on white).

Usage: fig_design.py --out DIR   (writes fig_design.pdf and .png). No other args.
"""
import sys
from pathlib import Path
if len(sys.argv) != 3 or sys.argv[1] != "--out":
    sys.exit("usage: fig_design.py --out DIR")
OUT = Path(sys.argv[2]); OUT.mkdir(parents=True, exist_ok=True)
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
plt.rcParams.update({"pdf.fonttype": 42, "ps.fonttype": 42, "font.size": 6.5, "font.family": "sans-serif"})

W, H, GX, GY = 1.55, 0.60, 0.72, 0.46          # cell size and gaps (arrow corridors)
X0, Y0 = 0.98, 0.15                            # grid origin (room for row headers)
COLS = {"absent": X0, "present": X0 + W + GX}
ROWS = {"L1": Y0 + H + GY, "LPIPS": Y0}        # L1 row on top
CELLS = {("L1", "absent"): ("L1 only", "C2"), ("L1", "present"): ("adversarial + L1", "C1"),
         ("LPIPS", "absent"): ("LPIPS only", "C5"), ("LPIPS", "present"): ("adversarial + LPIPS", "C4")}
fig, ax = plt.subplots(figsize=(3.5, 1.85)); ax.set_axis_off()
def centre(row, col): return COLS[col] + W / 2, ROWS[row] + H / 2
for (row, col), (name, code) in CELLS.items():
    x, y = COLS[col], ROWS[row]
    ax.add_patch(FancyBboxPatch((x, y), W, H, boxstyle="round,pad=0,rounding_size=0.04", fc="white", ec="black", lw=0.8))
    ax.text(x + W / 2, y + H / 2 + 0.08, name, ha="center", va="center", fontsize=6.2)
    ax.text(x + W / 2, y + H / 2 - 0.12, f"repository code: {code}", ha="center", va="center", fontsize=4.8, color="0.35")
# headers
ax.text(X0 + W + GX / 2, Y0 + 2 * H + GY + 0.30, "adversarial term", ha="center", va="center", fontsize=6.5, style="italic")
for col, lab in (("absent", "absent"), ("present", "present")):
    ax.text(COLS[col] + W / 2, Y0 + 2 * H + GY + 0.13, lab, ha="center", va="center", fontsize=6.5)
ax.text(X0 - 0.80, Y0 + H + GY / 2, "reconstruction\nloss", ha="center", va="center", fontsize=6.5, style="italic", rotation=90)
for row in ROWS:
    ax.text(X0 - 0.22, ROWS[row] + H / 2, row, ha="center", va="center", fontsize=6.5)
# the fifth arm, outside the grid
PX = COLS["present"] + W + 0.30; PW = 1.55
ax.add_patch(FancyBboxPatch((PX, ROWS["LPIPS"]), PW, H, boxstyle="round,pad=0,rounding_size=0.04", fc="white", ec="black", lw=0.8, ls=(0, (3, 2))))
ax.text(PX + PW / 2, ROWS["LPIPS"] + H / 2 + 0.16, "pretrained", ha="center", va="center", fontsize=6.2)
ax.text(PX + PW / 2, ROWS["LPIPS"] + H / 2 + 0.02, "repository code: pre", ha="center", va="center", fontsize=4.8, color="0.35")
ax.text(PX + PW / 2, ROWS["LPIPS"] + H / 2 - 0.16, "adv. + LPIPS objective;\nEuropean training data", ha="center", va="center", fontsize=4.8)
# contrasts: arrow from subtrahend to minuend, as the letter writes each one
def arrow(frm, to, label, lpos, dx=0.0, dy=0.0):
    (x1, y1), (x2, y2) = centre(*frm), centre(*to)
    if y1 == y2:   # horizontal, between cell edges
        x1 = COLS[frm[1]] + (W if x2 > x1 else 0); x2 = COLS[to[1]] + (0 if x2 > x1 else W)
    else:          # vertical
        y1 = ROWS[frm[0]] + (0 if y2 < y1 else H); y2 = ROWS[to[0]] + (H if y2 < y1 else 0)
    ax.add_patch(FancyArrowPatch((x1 + dx, y1 + dy), (x2 + dx, y2 + dy), arrowstyle="-|>", mutation_scale=7, lw=0.9, color="black", shrinkA=1, shrinkB=1))
    ax.text(*lpos, label, ha="center", va="center", fontsize=5, style="italic")
arrow(("LPIPS", "present"), ("LPIPS", "absent"), "primary", (X0 + W + GX / 2, ROWS["LPIPS"] + H / 2 + 0.11))
arrow(("L1", "absent"), ("L1", "present"), "L1 family", (X0 + W + GX / 2, ROWS["L1"] + H / 2 + 0.11))
arrow(("L1", "absent"), ("LPIPS", "absent"), "secondary", (X0 + 0.50, Y0 + H + GY / 2), dx=-W / 2 + 0.18)
ax.set_xlim(0, PX + PW + 0.06); ax.set_ylim(0, Y0 + 2 * H + GY + 0.44)
fig.subplots_adjust(0, 0, 1, 1)
fig.savefig(OUT / "fig_design.pdf"); fig.savefig(OUT / "fig_design.png", dpi=300)
print("wrote", OUT / "fig_design.pdf")
