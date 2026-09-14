#!/usr/bin/env python3
"""Where is each term first used in the compiled letter? (P11 part D, 14 September 2026.)

P4 ruling 5.1 required seven terms to be defined at first use; P6 later added a sentence that
used two of them earlier than their definitions, and nothing noticed until P10 read the
document again. This script makes the first-use location visible so the check is a command
and not a memory. It cannot judge whether a definition is present; it reports, for each term
in the terms file, the section heading under which the term first occurs in the compiled
text, and it FAILS if that occurrence precedes the heading the terms file declares as the
defining section.

Usage: term_first_use.py PDF TERMS     (TERMS: one line per term, `term | defining heading`)
Deterministic given the PDF: pdftotext, then heading detection on the IEEE layout
(section lines `I.`..`VI.` and subsection lines `A.`..`L.`).
"""
import re, subprocess, sys
if len(sys.argv) != 3:
    sys.exit("usage: term_first_use.py PDF TERMS")
pdf, terms = sys.argv[1], sys.argv[2]
text = subprocess.run(["pdftotext", pdf, "-"], capture_output=True, text=True, check=True).stdout
lines = text.splitlines()
SEC = re.compile(r"^(VI|IV|V|III|II|I)\.\s+\S")
SUB = re.compile(r"^([A-L])\.\s+[A-Z]")
headings = []   # (line index, label)
sec = "front matter"
ROMAN = ["I", "II", "III", "IV", "V", "VI"]; nxt = 0     # sections must appear in order; a subsection lettered I or V is not a section
for i, l in enumerate(lines):
    s = l.strip()
    if s.startswith("Abstract"): sec = "Abstract"; headings.append((i, sec))
    elif s in ("Data Availability", "Acknowledgment", "Acknowledgments", "References"): sec = s; headings.append((i, sec))
    elif SEC.match(s) and nxt < len(ROMAN) and SEC.match(s).group(1) == ROMAN[nxt]: sec = ROMAN[nxt]; nxt += 1; headings.append((i, sec))
    elif SUB.match(s) and sec not in ("front matter", "Abstract"): headings.append((i, f"{sec}-{SUB.match(s).group(1)}"))
def heading_at(i):
    lab = "front matter"
    for h, l in headings:
        if h <= i: lab = l
    return lab
def heading_index(label):
    for h, l in headings:
        if l == label: return h
    return None
flat = "\n".join(lines).lower()
bad = 0
for row in open(terms, encoding="utf-8"):
    row = row.strip()
    if not row or row.startswith("#"): continue
    term, _, defined = [x.strip() for x in row.partition("|")]
    m = re.search(re.escape(term.lower()).replace(r"\ ", r"\s+"), flat)
    if not m:
        print(f"{term:28} NOT FOUND"); bad += 1; continue
    li = flat[:m.start()].count("\n"); where = heading_at(li)
    verdict = ""
    if defined:
        hi = heading_index(defined)
        if hi is None: verdict = f"  (defining heading '{defined}' not found in the PDF)"; bad += 1
        elif where in ("front matter", "Abstract"):
            # the title and abstract cannot define; report the first BODY use instead
            m2 = re.compile(re.escape(term.lower()).replace(r"\ ", r"\s+")).search(flat, len("\n".join(lines[:headings[1][0]])))
            li2 = flat[:m2.start()].count("\n") if m2 else li
            verdict = f"  (also in the {where}); first body use in {heading_at(li2)}" + ("  FAIL: precedes " + defined if li2 < hi else f", ok (defined in {defined})")
            if li2 < hi: bad += 1
        elif li < hi: verdict = f"  FAIL: first use precedes its defining section {defined}"; bad += 1
        else: verdict = f"  ok (defined in {defined})"
    print(f"{term:28} first use in {where}{verdict}")
sys.exit(1 if bad else 0)
