#!/usr/bin/env python3
"""Mechanical gate for practice 15: run a script's --self-test under the PROJECT interpreter,
require exit 0, and print a PASS token only on success. A registration that claims a
self-test pastes the token line; the pre-commit hook (scripts/hooks/pre-commit) refuses to
commit a registration that mentions --self-test without a PASS token.

Usage: selftest_gate.py SCRIPT [SCRIPT ...]   (refuses any option; exits 1 if anything fails)
"""
import hashlib, subprocess, sys, datetime
PY_EXE="/opt/homebrew/Caskroom/miniforge/base/envs/gencp/bin/python"
def sha16(p): return hashlib.sha256(open(p,"rb").read()).hexdigest()[:16]
def main():
    args=sys.argv[1:]
    if not args or any(a.startswith("-") for a in args): sys.exit("usage: selftest_gate.py SCRIPT [SCRIPT ...] (no options)")
    ok=True
    chk=subprocess.run([PY_EXE,"-c","import numpy, pandas"],capture_output=True)
    if chk.returncode!=0: sys.exit("GATE FAIL: project interpreter cannot import numpy/pandas")
    for s in args:
        p=subprocess.run([PY_EXE,s,"--self-test"],capture_output=True,text=True)
        out=(p.stdout+p.stderr).strip().splitlines()
        if p.returncode!=0 or not any("self-test passed" in l for l in out):
            ok=False; print(f"GATE FAIL: {s} rc={p.returncode}: {out[-1] if out else '(no output)'}")
        else:
            print(f"self-test gate: PASS {sha16(s)} {s} {PY_EXE} {datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%MZ')}")
    sys.exit(0 if ok else 1)
if __name__=="__main__": main()
