#!/usr/bin/env python3
"""Registered readings for the OSM-render premise check (docs/osm-render-baseline-registration.md).

Inputs: tool_runs/osm_render_baseline/render_per_chip.csv (render, seed-invariant),
tool_runs/C45_s{45..50}_modal/C45_per_chip.csv (arms), and the KLT rows of both for the
equal-count truncation. Every comparison is a paired CHIP-LEVEL difference over 130 chips,
D = render - arm, positive = render worse; SE across chips. Fine-tuned arms: one D per seed,
reported as mean and range over the six seeds. Pretrained: once, raw only (its KLT rows on
this path are not retained). Equal-count: per chip K = min(n_render, n_arm at that seed),
both truncated to the best K by KLT score descending, medians recomputed.

Bands (registered): WELL = D(render - L1-only) <= 0 at >= 2 SE in all six seeds under both
raw and equal-count AND render median points >= L1-only's; POORLY = D(render - arm) > 0 at
>= 2 SE in all six seeds for every fine-tuned arm (raw) OR >= 20% of chips with zero
matches; otherwise INTERMEDIATE.
--self-test plants both branches and must read them correctly. Refuses unknown arguments.
"""
import argparse, csv, glob, json, statistics as st, sys
from pathlib import Path
import numpy as np, pandas as pd
SEEDS=(45,46,47,48,49,50); ARMS=("C1","C2","C4","C5")

def paired(d):
    d=np.asarray(d,float); d=d[~np.isnan(d)]; se=d.std(ddof=1)/np.sqrt(len(d))
    return dict(mean=float(d.mean()), se=float(se), t=float(d.mean()/se), n=int(len(d)), render_better=int((d<0).sum()))

def band(D_raw_C2, D_eq_C2, pts_render, pts_C2, D_raw_all, zero_frac):
    well = all(x["mean"]<=0 and abs(x["t"])>=2 for x in D_raw_C2) and all(x["mean"]<=0 and abs(x["t"])>=2 for x in D_eq_C2) and pts_render>=pts_C2
    poorly = all(all(x["mean"]>0 and abs(x["t"])>=2 for x in D_raw_all[a]) for a in ARMS) or zero_frac>=0.20
    return "WELL" if well else ("POORLY" if poorly else "INTERMEDIATE")

def self_test():
    good=[dict(mean=-0.5,se=0.05,t=-10)]*6; bad=[dict(mean=0.8,se=0.05,t=16)]*6
    assert band(good, good, 90, 75, {a: good for a in ARMS}, 0.0)=="WELL"
    assert band(bad, bad, 40, 75, {a: bad for a in ARMS}, 0.0)=="POORLY"
    assert band(good, good, 60, 75, {a: good for a in ARMS}, 0.0)=="INTERMEDIATE", "fewer points must block WELL"
    assert band([dict(mean=-0.5,se=0.05,t=-10)]*5+[dict(mean=0.1,se=0.05,t=2)], good, 90, 75, {a: good for a in ARMS}, 0.0)=="INTERMEDIATE", "one seed breaking must block WELL"
    assert band(bad, bad, 40, 75, {a: bad for a in ARMS}, 0.25)=="POORLY"
    print("self-test passed: WELL, POORLY, and two planted near-misses read INTERMEDIATE")

def klt_rows(path_glob):
    cs=glob.glob(path_glob)
    if not cs: return None
    d=pd.read_csv(cs[0], sep=None, engine="python"); return d

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--root"); ap.add_argument("--out"); ap.add_argument("--self-test",action="store_true")
    args, unknown = ap.parse_known_args()
    if unknown: sys.exit(f"refusing unknown arguments: {unknown}")
    if args.self_test: return self_test()
    if not (args.root and args.out): sys.exit("usage: --root ROOT --out DIR | --self-test")
    root=Path(args.root); out=Path(args.out); out.mkdir(parents=True, exist_ok=True)
    R=pd.read_csv(root/"tubitak/data/tool_runs/osm_render_baseline/render_per_chip.csv").set_index("stem")
    stems=list(R.index); assert len(stems)==130
    res={"render":{"mean_of_medians":float(R.render_med.mean()), "median_of_medians":float(R.render_med.median()), "points_median":float(R.render_n.median()), "zero_point_chips":int((R.render_n==0).sum())}, "raw":{}, "equal_count":{}}
    arms={s: pd.read_csv(root/f"tubitak/data/tool_runs/C45_s{s}_modal/C45_per_chip.csv").set_index("stem").loc[stems] for s in SEEDS}
    # pretrained, seed-invariant, raw only
    pre=arms[45]["pre_med"]; res["raw"]["pretrained"]=paired(R.render_med-pre)
    for a in ARMS:
        res["raw"][a]=[paired(R.render_med-arms[s][f"{a}_med"]) for s in SEEDS]
    # equal-count per seed per arm
    for a in ARMS:
        per_seed=[]
        for s in SEEDS:
            diffs=[]
            for stt in stems:
                dr=klt_rows(str(root/f"tubitak/data/tool_runs/osm_render_baseline/karios/{stt}/*/KLT_matcher_*.csv"))
                da=klt_rows(str(root/f"tubitak/data/tool_runs/C45_s{s}_modal/karios/{a}/{stt}/*/KLT_matcher_*.csv"))
                if dr is None or da is None or len(dr)==0 or len(da)==0: diffs.append(np.nan); continue
                K=min(len(dr),len(da))
                r=dr.sort_values("score",ascending=False).head(K); m=da.sort_values("score",ascending=False).head(K)
                diffs.append(float(np.median(np.hypot(r.dx,r.dy))-np.median(np.hypot(m.dx,m.dy))))
            per_seed.append(paired(diffs))
        res["equal_count"][a]=per_seed
    pts_C2=st.mean(float(arms[s]["C2_n"].median()) for s in SEEDS)
    zero_frac=res["render"]["zero_point_chips"]/130
    res["band"]=band(res["raw"]["C2"], res["equal_count"]["C2"], res["render"]["points_median"], pts_C2, res["raw"], zero_frac)
    res["points_L1_only_six_seed_median_mean"]=pts_C2
    json.dump(res, open(out/"render_baseline_summary.json","w"), indent=1)
    print(f"render: mean of medians {res['render']['mean_of_medians']:.3f} px, median {res['render']['median_of_medians']:.3f}, points median {res['render']['points_median']:.0f}, zero-point chips {res['render']['zero_point_chips']}")
    p=res["raw"]["pretrained"]; print(f"raw render - pretrained: {p['mean']:+.3f} ± {p['se']:.3f} (t {p['t']:.1f}; render better on {p['render_better']}/{p['n']})")
    for a in ARMS:
        ms=[x["mean"] for x in res["raw"][a]]; es=[x["mean"] for x in res["equal_count"][a]]
        print(f"raw render - {a}: mean over seeds {st.mean(ms):+.3f} (range {min(ms):+.3f}..{max(ms):+.3f}); |t| min {min(abs(x['t']) for x in res['raw'][a]):.1f}; equal-count {st.mean(es):+.3f} (range {min(es):+.3f}..{max(es):+.3f})")
    print("BAND:", res["band"], "| L1-only points median (six-seed mean):", round(pts_C2,1))

if __name__=="__main__": main()
