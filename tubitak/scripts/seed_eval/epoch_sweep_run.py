#!/usr/bin/env python3
"""Epoch sweep at six seeds for the letter's training-time curve (Fig. 2).

Registration: docs/epoch-curve-registration.md. ROUTING ONLY: this script stages the
pulled per-epoch generator checkpoints where the frozen runner expects them and invokes
the frozen runner (seed_eval_run.py, commit 48ced64) once per (seed, epoch) with
--variant modal_e{E}. Every numeric step -- inference command, shim seed 42, warp
geometry, KARIOS config, scoring formula -- is the frozen runner's, unchanged.

Staging: tubitak/outputs/{arm}_checkpoints_s{S}_modal_e{E}/checkpoints/{ARM}/latest_net_G.pth
is a symlink to tubitak/data/checkpoints_modal/seed{S}/{ARM}/{E}_net_G.pth, created only
after the file's sha256 matches the pull log (the record of what left the Modal volume).
Outputs: tubitak/data/tool_runs/C45_s{S}_modal_e{E}/ (C45_per_chip.csv, C45_edge_ratio.csv).

Usage: epoch_sweep_run.py --root ROOT --seeds 45,46,47,48,49,50 --epochs 1,2,5,10
No other arguments are accepted.
"""
import argparse, hashlib, os, subprocess, sys, time
from pathlib import Path

ARMS = ("C1", "C2", "C4", "C5")

def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("--root", required=True)
    ap.add_argument("--seeds", required=True)
    ap.add_argument("--epochs", required=True)
    args, unknown = ap.parse_known_args()
    if unknown:
        sys.exit(f"refusing unknown arguments: {unknown}")
    root = Path(args.root).resolve()
    seeds = [int(s) for s in args.seeds.split(",")]
    epochs = [int(e) for e in args.epochs.split(",")]
    ck = root / "tubitak/data/checkpoints_modal"
    log = {}
    for line in (ck / "pull.log").read_text().splitlines():
        if " rc=0 " in line:
            t = line.split()
            log[(int(t[0][4:]), t[1], int(t[2][1:]))] = dict(x.split("=") for x in t[3:])
    runner = root / "tubitak/scripts/seed_eval/seed_eval_run.py"
    gp = os.environ.get("GENCP_PYTHON", "/opt/homebrew/Caskroom/miniforge/base/envs/gencp/bin/python")
    print(f"runner {runner} sha256 {sha256(runner)}", flush=True)
    for s in seeds:
        for e in epochs:
            for a in ARMS:
                src = ck / f"seed{s}/{a}/{e}_net_G.pth"
                rec = log[(s, a, e)]
                h = sha256(src)
                assert h.startswith(rec["sha256"]) and str(src.stat().st_size) == rec["bytes"], \
                    f"{src}: sha256/size do not match the pull log"
                dst = root / f"tubitak/outputs/{a.lower()}_checkpoints_s{s}_modal_e{e}/checkpoints/{a}/latest_net_G.pth"
                dst.parent.mkdir(parents=True, exist_ok=True)
                if dst.is_symlink() or dst.exists():
                    dst.unlink()
                dst.symlink_to(src)
            out = root / f"tubitak/data/tool_runs/C45_s{s}_modal_e{e}"
            if (out / "C45_per_chip.csv").exists():
                print(f"seed {s} epoch {e}: already scored, skipped", flush=True); continue
            t0 = time.time()
            p = subprocess.run([gp, str(runner), "--seed", str(s), "--root", str(root),
                                "--variant", f"modal_e{e}"], cwd=root)
            print(f"seed {s} epoch {e}: rc={p.returncode} {time.time()-t0:.0f}s", flush=True)
            if p.returncode != 0:
                sys.exit(f"runner failed at seed {s} epoch {e}")
    print("sweep complete", flush=True)

if __name__ == "__main__":
    main()
