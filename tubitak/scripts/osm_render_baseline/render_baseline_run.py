#!/usr/bin/env python3
"""Premise check: the rasterised OpenStreetMap input render used directly as the reference.

Registration: docs/osm-render-baseline-registration.md. ROUTING ONLY around the Table I
arms' own KARIOS invocation (scripts/c45_eval/c45_karios.py, reused verbatim by the frozen
runner): for each of the 130 Ankara chips, `karios process <warped input render>
<reference warp> --conf karios_gencp.json --no-log-file`. The generated image is replaced
by the warped input render and nothing else changes. Per-chip statistic afterwards is the
c45_score.py formula: median hypot(dx, dy) over the KLT rows, n = rows.

Usage: render_baseline_run.py --root ROOT   (no other arguments; refuses unknown ones)
Outputs: tubitak/data/tool_runs/osm_render_baseline/karios/<stem>/ and render_per_chip.csv
"""
import argparse, csv, glob, hashlib, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import numpy as np, pandas as pd

def sha256(p):
    h=hashlib.sha256()
    with open(p,"rb") as f:
        for b in iter(lambda: f.read(1<<20), b""): h.update(b)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--root", required=True)
    args, unknown = ap.parse_known_args()
    if unknown: sys.exit(f"refusing unknown arguments: {unknown}")
    root=Path(args.root).resolve()
    KARIOS=os.environ.get("KARIOS_BIN","/opt/homebrew/Caskroom/miniforge/base/envs/karios/bin/karios")
    CONF=root/"tubitak/configs/karios_gencp.json"
    REF=root/"tubitak/data/ankara/run/ref"
    INP=root/"tubitak/data/tool_runs/C45_s45_modal/warp/input"   # byte-identical across seeds and to evidence/rasters/input_render_warped
    OUT=root/"tubitak/data/tool_runs/osm_render_baseline"; (OUT/"karios").mkdir(parents=True, exist_ok=True)
    stems=sorted(p.name[:-4] for p in (root/"tubitak/data/ankara/run/inputs").glob("*.png")); assert len(stems)==130
    print("config sha256", sha256(CONF), flush=True)
    ver=subprocess.run([KARIOS,"--version"],capture_output=True,text=True).stdout.strip(); print("karios", ver, flush=True)
    def run(st):
        res=OUT/"karios"/st
        if glob.glob(str(res/"*"/"KLT_matcher_*.csv")): return st,0,"skipped"
        res.mkdir(parents=True, exist_ok=True)
        p=subprocess.run([KARIOS,"process",str(INP/f"{st}.tif"),str(REF/f"{st}_warp.tif"),"--out",str(res),"--conf",str(CONF),"--no-log-file"],capture_output=True,text=True)
        return st,p.returncode,(p.stderr[-200:] if p.returncode else "")
    bad=[]
    with ThreadPoolExecutor(max_workers=8) as ex:
        for i,f in enumerate(as_completed([ex.submit(run,s) for s in stems]),1):
            st,rc,err=f.result()
            if rc: bad.append((st,rc,err))
            if i%20==0: print(f"KARIOS {i}/130", flush=True)
    print("KARIOS complete, failures:", len(bad), bad[:5], flush=True)
    rows=[]
    for st in stems:
        cs=glob.glob(str(OUT/"karios"/st/"*"/"KLT_matcher_*.csv"))
        if not cs: rows.append(dict(stem=st, render_med=np.nan, render_n=0)); continue
        d=pd.read_csv(cs[0], sep=None, engine="python")
        rows.append(dict(stem=st, render_med=(float(np.median(np.hypot(d.dx,d.dy))) if len(d) else np.nan), render_n=int(len(d))))
    pd.DataFrame(rows).to_csv(OUT/"render_per_chip.csv", index=False)
    print("wrote", OUT/"render_per_chip.csv", "input sha256 of first chip", sha256(INP/f"{stems[0]}.tif"), flush=True)

if __name__=="__main__": main()
