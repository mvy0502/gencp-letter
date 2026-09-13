#!/usr/bin/env python3
"""Registered readings and figure for the training-time curve at six seeds (Fig. 3 as compiled from 13 Sep 2026, P9 C.3, when two figures entered ahead of it; Fig. 1 as compiled before that; the skeleton called it Fig. 2).

Registration: docs/epoch-curve-registration.md. Reads, per seed S in 45..50:
  epochs 1, 2, 5, 10 from tool_runs/C45_s{S}_modal_e{E}/C45_per_chip.csv
  epoch 20            from tool_runs/C45_s{S}_modal/C45_per_chip.csv   (the six-seed block)
Statistic per seed and epoch: penalty D = chip mean over 130 chips of (adversarial arm's
per-chip median residual - non-adversarial counterpart's), i.e. D_LPIPS = mean(C4 - C5),
D_L1 = mean(C1 - C2). Positive = the adversarial arm is worse.

REGISTERED reading, per family: D > 0 at every scored epoch in every seed (6/6 at each of
five epochs). EXPLORATORY reading (reported, no claim): dip-then-grow, D(2) < D(1) and
D(20) > D(2), counted per seed.

--self-test runs the reading on two planted tables (one all-positive, one with a single
negative cell) and exits non-zero unless the first reads HELD and the second FAILED.
Usage: epoch_curve_analysis.py --root ROOT --out DIR  |  epoch_curve_analysis.py --self-test
"""
import argparse, csv, json, statistics as st, sys
from pathlib import Path

SEEDS = (45, 46, 47, 48, 49, 50)
EPOCHS = (1, 2, 5, 10, 20)
FAMILIES = {"LPIPS": ("C4", "C5"), "L1": ("C1", "C2")}

def penalty(rows, adv, non):
    return st.mean(float(r[f"{adv}_med"]) - float(r[f"{non}_med"]) for r in rows)

def readings(D):
    """D[family][seed][epoch] -> dict of verdicts."""
    out = {}
    for fam, per_seed in D.items():
        per_epoch = {e: sum(1 for s in per_seed if per_seed[s][e] > 0) for e in EPOCHS}
        held = all(per_epoch[e] == len(per_seed) for e in EPOCHS)
        dip = sum(1 for s in per_seed if per_seed[s][2] < per_seed[s][1] and per_seed[s][20] > per_seed[s][2])
        out[fam] = {"registered_positive_every_epoch_every_seed": "HELD" if held else "FAILED",
                    "positive_count_by_epoch": per_epoch, "n_seeds": len(per_seed),
                    "exploratory_dip_then_grow_seeds": dip,
                    "mean_by_epoch": {e: st.mean(per_seed[s][e] for s in per_seed) for e in EPOCHS},
                    "sd_by_epoch": {e: st.stdev(per_seed[s][e] for s in per_seed) if len(per_seed) > 1 else None for e in EPOCHS}}
    return out

def self_test():
    good = {"LPIPS": {s: {1: .3, 2: .25, 5: .4, 10: .5, 20: .6} for s in SEEDS}}
    bad = {"LPIPS": {s: {1: .3, 2: .25, 5: .4, 10: .5, 20: .6} for s in SEEDS}}
    bad["LPIPS"][47][5] = -0.01
    r1 = readings(good)["LPIPS"]["registered_positive_every_epoch_every_seed"]
    r2 = readings(bad)["LPIPS"]["registered_positive_every_epoch_every_seed"]
    print(f"self-test: all-positive -> {r1}; planted negative at seed 47 epoch 5 -> {r2}")
    if r1 != "HELD" or r2 != "FAILED":
        sys.exit("SELF-TEST FAILED: the reading does not detect the planted case")
    print("self-test passed")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root"); ap.add_argument("--out"); ap.add_argument("--self-test", action="store_true")
    args, unknown = ap.parse_known_args()
    if unknown:
        sys.exit(f"refusing unknown arguments: {unknown}")
    if args.self_test:
        return self_test()
    if not (args.root and args.out):
        sys.exit("usage: --root ROOT --out DIR, or --self-test")
    root, out = Path(args.root), Path(args.out); out.mkdir(parents=True, exist_ok=True)
    runs = root / "tubitak/data/tool_runs"
    D = {fam: {} for fam in FAMILIES}
    for s in SEEDS:
        for e in EPOCHS:
            p = runs / (f"C45_s{s}_modal" if e == 20 else f"C45_s{s}_modal_e{e}") / "C45_per_chip.csv"
            rows = list(csv.DictReader(open(p))); assert len(rows) == 130, p
            for fam, (adv, non) in FAMILIES.items():
                D[fam].setdefault(s, {})[e] = penalty(rows, adv, non)
    R = readings(D)
    with open(out / "epoch_curve_per_seed.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["family", "seed"] + [f"e{e}" for e in EPOCHS])
        for fam in D:
            for s in SEEDS: w.writerow([fam, s] + [f"{D[fam][s][e]:.4f}" for e in EPOCHS])
    json.dump({"readings": R, "per_seed": {f: {str(s): {str(e): v for e, v in d.items()} for s, d in D[f].items()} for f in D}},
              open(out / "epoch_curve_summary.json", "w"), indent=1)
    for fam in R:
        print(fam, R[fam]["registered_positive_every_epoch_every_seed"], R[fam]["positive_count_by_epoch"],
              "dip-then-grow seeds:", R[fam]["exploratory_dip_then_grow_seeds"])
        print("  mean by epoch:", {e: round(v, 4) for e, v in R[fam]["mean_by_epoch"].items()})
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(3.5, 2.4))
    # Grayscale-safe since 13 Sep 2026 (P9 C.4): the two families were blue and red, which print
    # to nearly the same gray (BT.601 luma 100 vs 92); now black solid circles vs mid-gray dashed squares.
    for fam, color, ls, mk, lab in (("LPIPS", "black", "-", "o", "LPIPS family: (adv.+LPIPS) $-$ (LPIPS)"),
                                    ("L1", "0.45", "--", "s", "L1 family: (adv.+L1) $-$ (L1)")):
        for s in SEEDS:
            ax.plot(EPOCHS, [D[fam][s][e] for e in EPOCHS], color=color, ls=ls, alpha=0.3, lw=0.6)
        m = [R[fam]["mean_by_epoch"][e] for e in EPOCHS]; sd = [R[fam]["sd_by_epoch"][e] for e in EPOCHS]
        ax.errorbar(EPOCHS, m, yerr=sd, color=color, ls=ls, lw=1.4, marker=mk, ms=3, capsize=2, label=lab)
    ax.axhline(0, color="k", lw=0.5); ax.set_xscale("log"); ax.set_xticks(EPOCHS); ax.set_xticklabels([str(e) for e in EPOCHS])
    ax.set_xlabel("training epoch (log scale)", fontsize=7); ax.set_ylabel("adversarial penalty, px", fontsize=7)
    ax.tick_params(labelsize=6); ax.legend(fontsize=6, frameon=False, loc="lower right")
    fig.tight_layout(); fig.savefig(out / "fig2_epoch_curve.pdf"); fig.savefig(out / "fig2_epoch_curve.png", dpi=300)
    print("wrote", out)

if __name__ == "__main__":
    main()
