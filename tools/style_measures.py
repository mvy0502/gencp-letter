#!/usr/bin/env python3
"""Prose-only style measures for the letter and a corpus of PDFs (P12 part B, 14 Sep 2026).

Usage:
  style_measures.py letter SECTIONS_DIR OUT.txt        -> prose of the letter (macros expanded, floats/equations/captions/headings/cites dropped)
  style_measures.py pdf FILE.pdf OUT.txt               -> prose of a paper (front matter, captions, tables, equations, references, acknowledgements dropped)
  style_measures.py measure OUT.txt [...]              -> JSON lines of measures, one per file
Deterministic; no judgement, only counts.
"""
import re, sys, json, subprocess, statistics as st, glob, os
ABBR=["Fig","Figs","Eq","Eqs","et al","e.g","i.e","vs","cf","approx","Sec","Secs","No","Ref","Refs","Tab","Dr","Prof","resp","w.r.t","al","St","Mr","Ms"]
def sentences(par):
    t=par
    for a in ABBR: t=re.sub(r"\b"+re.escape(a)+r"\.", a.replace(".","")+"<DOT>", t)
    t=re.sub(r"(\d)\.(\d)", r"\1<DOT>\2", t)
    parts=re.split(r"(?<=[.!?])\s+(?=[A-Z(\[\"“‘'])", t)
    return [p.replace("<DOT>",".").strip() for p in parts if len(re.findall(r"[A-Za-z]",p))>=2]
def words(s): return re.findall(r"[A-Za-z][A-Za-z'\-]*", s)
# ---------------- letter prose from the .tex sources
def letter_prose(d):
    macros={"\\advLone{}":"adversarial + L1","\\advLPIPS{}":"adversarial + LPIPS","\\Lone{}":"L1-only","\\LPIPSonly{}":"LPIPS-only"}
    out=[]
    for f in ["00-abstract","01-introduction","02-methods","03-results","04-alternatives","05-discussion","06-data-availability"]:
        s=open(os.path.join(d,f+".tex"),encoding="utf-8").read()
        s=re.sub(r"^\s*%.*$","",s,flags=re.M)
        s=re.sub(r"\\begin\{(table\*?|figure\*?|equation|align|subequations)\}.*?\\end\{\1\}","",s,flags=re.S)
        s=re.sub(r"\\(sub)?section\*?\{[^}]*\}","",s)
        s=re.sub(r"\\footnote\{([^{}]*)\}",r" (\1)",s)
        s=re.sub(r"\\cite\{[^}]*\}","",s); s=re.sub(r"\\ref\{[^}]*\}","N",s); s=re.sub(r"\\url\{[^}]*\}","URL",s); s=re.sub(r"\\texttt\{([^}]*)\}",r"\1",s); s=re.sub(r"\\emph\{([^}]*)\}",r"\1",s)
        for k,v in macros.items(): s=s.replace(k,v)
        s=re.sub(r"\$[^$]*\$","M",s)            # inline math -> one token, keeps the sentence
        s=s.replace("---","—").replace("--","–").replace("~"," ").replace("``","“").replace("''","”")
        s=re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?(\{[^}]*\})?","",s); s=re.sub(r"[{}]","",s)
        out.append(s)
    text="\n".join(out)
    pars=[re.sub(r"\s+"," ",p).strip() for p in re.split(r"\n\s*\n",text)]
    return "\n\n".join(p for p in pars if len(words(p))>=8)
# ---------------- paper prose from a PDF
def pdf_prose(pdf):
    raw=subprocess.run(["pdftotext",pdf,"-"],capture_output=True,text=True).stdout
    lines=raw.split("\n")
    # start at the abstract if present; stop at the references
    lo=0
    for i,l in enumerate(lines):
        if re.match(r"^\s*(Abstract|ABSTRACT)\b",l.strip()): lo=i; break
    hi=len(lines)
    for i,l in enumerate(lines):
        if i>lo+50 and (re.match(r"^\s*(References|REFERENCES|R EFERENCES)\s*$",l.strip()) or re.match(r"^\[1\]\s+[A-Z]",l.strip())): hi=i; break
    lines=lines[lo:hi]
    # drop acknowledgement sections, captions, tables, index terms, page furniture, equation-like lines
    keep=[]; skip=False; cap=False
    for l in lines:
        s=l.strip()
        if re.match(r"^(ACKNOWLEDG|Acknowledg)",s): skip=True; continue
        if skip and re.match(r"^([IVX]+\.|\d+\.?)\s+[A-Z]",s): skip=False
        if skip: continue
        if s=="" : cap=False; keep.append(""); continue
        if re.match(r"^(Fig\.|Figure|FIGURE|TABLE|Table)\s*\d",s): cap=True
        if cap: continue
        if re.match(r"^(Index Terms|Keywords|KEYWORDS|Manuscript received|Digital Object|Authorized licensed|arXiv:|IEEE |JOURNAL OF|\[\d+\]\s)",s): continue
        if re.search(r"\bvol\.\s*\d+|\bpp\.\s*\d+",s) and len(s)<200: continue
        if re.match(r"^[\d\s]+$",s): continue
        letters=len(re.findall(r"[A-Za-z]",s)); total=len(s)
        if total>0 and letters/total<0.6: continue        # equations, tables, symbol-heavy lines
        if len(s)<25 and not re.search(r"[.!?]$",s): continue   # headers, running heads, short fragments
        keep.append(s)
    text="\n".join(keep); text=re.sub(r"(\w)-\n(\w)",r"\1\2",text); text=re.sub(r"(?<!\n)\n(?!\n)"," ",text)
    text=re.sub(r"\[\d+(?:[,–-]\s*\d+)*\]","",text)             # numeric citations
    pars=[re.sub(r"\s+"," ",p).strip() for p in re.split(r"\n\s*\n",text)]
    return "\n\n".join(p for p in pars if len(words(p))>=8)
# ---------------- measures
HEDGES=["may","might","could","roughly","approximately","about","likely","possibly","perhaps","suggest","suggests","appear","appears","seem","seems","to our knowledge","arguably","tend","tends","generally","largely","partly","nearly","close to","at least","up to","consistent with","cannot exclude","not necessarily","in principle","plausibly","typically","often","somewhat","relatively"]
def measures(path):
    text=open(path,encoding="utf-8").read(); pars=[p for p in text.split("\n\n") if p.strip()]
    sents=[]; par_len=[]
    for p in pars:
        ss=sentences(p); sents+=ss; par_len.append(len(ss))
    L=[len(words(s)) for s in sents]; W=[w.lower() for s in sents for w in words(s)]; n=len(W)
    per=lambda c: round(1000*c/n,2)
    openers=[words(s)[0].lower() for s in sents if words(s)]
    from collections import Counter
    oc=Counter(openers)
    notbut=sum(1 for s in sents if re.search(r"\bnot\b[^.;:]{1,60}\bbut\b",s) or re.search(r"\bis not\b[^.;]{1,60};\s*it is\b",s) or re.search(r"\bnot\b[^.;:]{1,60}\brather\b",s))
    tric=sum(1 for s in sents if re.search(r"[^,;]{2,40},\s[^,;]{2,40},\s(and|or)\s[^,;]{2,40}",s))
    fp=sum(1 for w in W if w in ("we","our","us","ours"))
    hed=sum(len(re.findall(r"\b"+re.escape(h)+r"\b",text.lower())) for h in HEDGES)
    nom=sum(1 for w in W if re.search(r"(tion|tions|ment|ments|ness|ity|ities)$",w) and len(w)>6)
    def ttr(ws,win=500):
        if len(ws)<win: return round(len(set(ws))/len(ws),3)
        return round(st.mean(len(set(ws[i:i+win]))/win for i in range(0,len(ws)-win+1,250)),3)
    return dict(file=os.path.basename(path), words=n, sentences=len(sents), paragraphs=len(pars),
        sent_mean=round(st.mean(L),1), sent_median=st.median(L), sent_sd=round(st.pstdev(L),1), sent_p90=sorted(L)[int(0.9*len(L))-1], sent_max=max(L),
        burstiness=round(st.pstdev(L)/st.mean(L),3), par_sent_mean=round(st.mean(par_len),2), par_sent_sd=round(st.pstdev(par_len),2), par_sent_max=max(par_len),
        semicolons=per(text.count(";")), colons=per(len(re.findall(r":(?!\d)",text))), parentheticals=per(text.count("(")), dashes=per(len(re.findall(r"—|–|(?<=\s)-(?=\s)",text))),
        not_but_per_100_sent=round(100*notbut/len(sents),1), tricolon_per_100_sent=round(100*tric/len(sents),1), first_person_per_1000=per(fp), hedges_per_1000=per(hed),
        nominalisation_per_1000=per(nom), opener_variety=round(len(oc)/len(openers),3), top_openers=oc.most_common(8), ttr_mattr500=ttr(W), ttr_raw=round(len(set(W))/n,3))
if __name__=="__main__":
    cmd=sys.argv[1]
    if cmd=="letter": open(sys.argv[3],"w",encoding="utf-8").write(letter_prose(sys.argv[2]))
    elif cmd=="pdf": open(sys.argv[3],"w",encoding="utf-8").write(pdf_prose(sys.argv[2]))
    elif cmd=="measure":
        for p in sys.argv[2:]: print(json.dumps(measures(p)))
