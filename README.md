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

*Amended 2026-08-26 from the study's `paper-roadmap.md` (amendment at :150-:187). The
earlier three-leg description in this file is superseded: leg 1 was demoted to
introduction scope, the old leg 2 moved to the second paper, and the old leg 3's first
independent measurement changed hands.*

1. **Scope, two sentences in the introduction** — at 10 m the premise for synthetic
   references fails: no availability gap (E1) and no currency advantage (E2). Not a
   section and not a result.
2. **The design rule** — if you generate a reference for a geometric consumer, do not
   train it under plausibility pressure. The 2x2 factorial is the primary measurement,
   stated at seed level as a six-seed sign replication; B2 is the production-path row;
   B3 parts 1 and 3 are mechanism support carrying the section-22 non-monotonicity
   caveat; B1 follows as dose-response support and must not be the spine.

**The claim is plausibility pressure, not adversarial training.** C5 carries no
discriminator anywhere in its objective and hallucinates hardest of the five arms. The
title changed on 2026-08-26 to match.

**Out of scope for this letter**, and it is a longer list than it was:

- **The ODTU/Cappadocia contamination pair** — moved to the second paper. It is no
  longer "one independent methods contribution" of this letter; there is no
  contamination section, table or row.
- **T1**, including its C1 row, and **E3 and its follow-ups** — second paper.
- **The registered interaction** — tested, failed 5/6 on all three pre-specified
  scales, and by a consequence committed in advance no interaction claim is made. The
  disclosure is mandatory; the words are already budgeted.
- **B3 part 2 (mediation)** — void as stated (corrections-log entry 20); does not
  appear at all.
- **The full four-alternative-explanations protocol** — arXiv long version only. The
  letter's Table II is three rows.

## Layout

```
gencp-letter/
├── README.md
├── EVIDENCE.md          # every claim -> study repo commit + document + number
├── manuscript/          # LaTeX sources (letter; arXiv variant shares sections/)
│   ├── letter.tex
│   ├── sections/        # 00-abstract, 01-introduction, 02-methods,
│   │                    # 03-results, 04-alternatives, 05-discussion
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
