#!/usr/bin/env python3
"""Table I of the letter, rebuilt from the six-seed Modal block.

Reads docs/evidence/C45_s{45..50}_modal/C45_per_chip.csv and C45_edge_ratio.csv (committed,
sha256 in docs/evidence/MANIFEST.md) and prints the five-arm panel. Inference path: per chip,
the median KLT residual over the arm's own matches; per seed, the mean and the median of
the 130 per-chip medians and the median surviving-point count; the table entry is the mean
over seeds 45-50. The pretrained row is seed-invariant (asserted below). As a check the
per-seed contrasts C5-C4, C5-C2 and C1-C2 are printed; they must match
docs/seed-block-results.md section 1 to four decimals.

Written 2026-09-13. Takes no arguments (tubitak/tests/_guard.py convention: refuses any).
"""
import csv, hashlib, statistics as st, sys
from pathlib import Path

if len(sys.argv) > 1:
    sys.exit("table1_six_seed.py takes no arguments")
ROOT = Path(__file__).resolve().parents[2] / "docs" / "evidence"
SEEDS = [45, 46, 47, 48, 49, 50]
ARMS = ["pre", "C1", "C2", "C4", "C5"]
EDGE = {"pre": "pretrained", "C1": "C1", "C2": "C2", "C4": "C4", "C5": "C5"}

def load(p):
    with open(p) as f:
        return list(csv.DictReader(f))

per = {a: {"mean": [], "median": [], "npts": []} for a in ARMS}
edge = {a: [] for a in ARMS}
contr = {"C5-C4": [], "C5-C2": [], "C1-C2": []}
pre_sig = set()
for s in SEEDS:
    rows = load(ROOT / f"C45_s{s}_modal" / "C45_per_chip.csv")
    er = load(ROOT / f"C45_s{s}_modal" / "C45_edge_ratio.csv")
    assert len(rows) == 130 and len(er) == 130, s
    pre_sig.add(hashlib.sha256("".join(r["pre_med"] for r in rows).encode()).hexdigest())
    for a in ARMS:
        med = [float(r[f"{a}_med"]) for r in rows]
        per[a]["mean"].append(st.mean(med))
        per[a]["median"].append(st.median(med))
        per[a]["npts"].append(st.median(int(r[f"{a}_n"]) for r in rows))
        edge[a].append(st.mean(float(r[EDGE[a]]) for r in er))
    for c in contr:
        x, y = c.split("-")
        contr[c].append(st.mean(float(r[f"{x}_med"]) - float(r[f"{y}_med"]) for r in rows))
assert len(pre_sig) == 1, "pretrained row is not seed-invariant"

print("check: per-seed contrasts (must match seed-block-results.md section 1)")
for c, v in contr.items():
    print(f"  {c}: " + ", ".join(f"{x:+.4f}" for x in v) + f"   mean {st.mean(v):+.4f}")
print("\nTable I, six-seed means (pretrained seed-invariant)")
print(f"{'arm':>4} {'mean px':>8} {'seed sd':>8} {'median px':>10} {'points':>7} {'edge':>6}")
for a in ARMS:
    sd = st.stdev(per[a]["mean"]) if a != "pre" else float("nan")
    print(f"{a:>4} {st.mean(per[a]['mean']):8.3f} {sd:8.3f} {st.mean(per[a]['median']):10.3f} "
          f"{st.mean(per[a]['npts']):7.1f} {st.mean(edge[a]):6.2f}")
print("\nordering per seed:")
for i, s in enumerate(SEEDS):
    m = {a: per[a]["mean"][i] for a in ARMS}
    print(f"  {s}: " + " < ".join(sorted(m, key=m.get)))
