# GenCP letter — manuscript workspace

Manuscript workspace for the IEEE GRSL letter (plus the arXiv long version) coming out
of the GenCP validation study. Code, data and experiment records stay in the study
repository; this repository holds only the manuscript, its figures and its evidence
trail.

- **Study repository (evidence):** https://github.com/mvy0502/gencp-validation
- **Venue plan:** arXiv preprint first (citable ID), then IEEE GRSL (5-page letter,
  submission target end of October 2026); IGARSS 2027 for the second slice.
- **Authors:** Mustafa Vedat Yıldırım; co-authorship with the TÜBİTAK UZAY advisor as
  agreed.

## Scope of this letter

One three-leg narrative (from the study's `paper-roadmap.md`, amended 2026-08-24):

1. **Scope** — at 10 m the premise for synthetic references fails: no availability gap
   (E1) and no currency advantage (E2). Scope-setting, not results: two or three
   sentences plus a footnote.
2. **Where it does bind** — sub-metre resolution, where licensing actually constrains
   reference choice. E3 is exploratory only and does not appear in the letter.
3. **Design rule** — if you generate a reference, do not train it with an adversarial
   loss. Three independent 10 m measurements carry this: T1's C1 row, B2's
   production-path ablation, and B3's direct mechanism measurement (B3 leads, B1
   follows as dose-response support and must not be the spine).

Plus one independent methods contribution: the ODTÜ contamination pair (same tool,
same matcher, same distortions; contaminated site 0.008–0.11 px vs clean site
0.54–3.97 px).

Out of scope for the letter: E3 and its follow-ups (second paper), the full
four-alternative-explanations protocol (arXiv long version only).

## Layout

```
gencp-letter/
├── README.md
├── EVIDENCE.md          # every claim -> study repo commit + document + number
├── manuscript/          # LaTeX sources (letter; arXiv variant shares sections/)
│   ├── letter.tex
│   ├── sections/
│   └── refs.bib
├── figures/             # figures used in the manuscript, plus how each is produced
│   └── README.md
└── notes/               # drafting notes, reviewer replies, submission checklists
```

## Working rules

1. **No numbers without provenance.** Every figure, table and quoted value in the
   manuscript must have a row in [EVIDENCE.md](EVIDENCE.md) naming the study-repo
   commit SHA, the document it comes from, and the exact value. If a number changes in
   the study repo, it changes here through that row.
2. **Do not copy analysis code here.** Figures are regenerated from the study
   repository's scripts; `figures/README.md` records the command and the commit.
3. **The manuscript wording rule of the study repo applies here too** — see
   `paper-roadmap.md` in the study repository before drafting claim sentences.
4. **Retracted or superseded numbers never re-enter.** Check the study repo's
   `corrections-log.md` before quoting a value; some figures are explicitly marked as
   not quotable.
5. No emoji in any file in this repository.
