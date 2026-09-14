#!/usr/bin/env python3
"""Prove a prose pass changed nothing but prose (P12 part F, 14 Sep 2026).

  prose_pass_checks.py tokens OUT.json      -> enumerate every numeric token (P10's rule) into OUT.json
  prose_pass_checks.py diff BEFORE.json AFTER.json -> multiset comparison of the tokens; exit 1 on any difference
  prose_pass_checks.py phrases PHRASES.txt  -> every phrase (whitespace-tolerant) must occur at least as often as the count given; exit 1 otherwise
"""
import re, sys, json, glob, os
S="manuscript/sections"
WORDS=r"\b(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|hundred|thousand|half|twice|tenfold|fourfold|threefold)\b"
NUM=r"(?<![A-Za-z\\{])[+\-−$]?\$?\d[\d,]*(?:\.\d+)?(?:\\times10\^\{-?\d+\}|\^\{-?\d+\}|\s*\\%|\\,)?(?:--\d+(?:\.\d+)?)?(?:/\d+)?"
tok=re.compile(NUM+"|"+WORDS, re.I)
def tokens():
    out=[]
    for f in sorted(glob.glob(f"{S}/*.tex")):
        for l in open(f,encoding="utf-8"):
            if l.lstrip().startswith("%"): continue
            l2=re.sub(r"(?<!\\)%.*$","",l); clean=re.sub(r"\\(label|ref|cite|includegraphics|input)\{[^}]*\}","",l2)
            for m in tok.finditer(clean):
                t=m.group(0).strip()
                if re.fullmatch(r"[+\-−$]?\$?",t): continue
                out.append((os.path.basename(f), t.lower()))
    return out
def alltext():
    t=""
    for f in sorted(glob.glob(f"{S}/*.tex")): t+=re.sub(r"^\s*%.*$","",open(f,encoding="utf-8").read(),flags=re.M)+"\n"
    return re.sub(r"\s+"," ",t)
cmd=sys.argv[1]
if cmd=="tokens":
    json.dump(tokens(),open(sys.argv[2],"w")); print(len(tokens()),"tokens")
elif cmd=="diff":
    from collections import Counter
    a=Counter(map(tuple,json.load(open(sys.argv[2])))); b=Counter(map(tuple,json.load(open(sys.argv[3]))))
    gone=a-b; new=b-a
    print(f"before {sum(a.values())} after {sum(b.values())}; missing {sum(gone.values())}; added {sum(new.values())}")
    for k,v in gone.items(): print("  MISSING", k, v)
    for k,v in new.items(): print("  ADDED", k, v)
    sys.exit(1 if gone or new else 0)
elif cmd=="phrases":
    t=alltext().lower(); bad=0
    for row in open(sys.argv[2],encoding="utf-8"):
        row=row.strip()
        if not row or row.startswith("#"): continue
        ph,_,n=row.partition("|"); n=int(n or 1); pat=re.escape(ph.strip().lower()).replace(r"\ ",r"\s+")
        c=len(re.findall(pat,t)); flag="" if c>=n else "  MISSING"; bad+= c<n
        print(f"{c:>3} (need {n}) {ph.strip()}{flag}")
    sys.exit(1 if bad else 0)
