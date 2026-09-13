# Paper repository

This repository holds the manuscript (TeX) and its Markdown drafts only. No code, no
data, no experiments.

Measurements, results and the research record live in `mvy0502/gencp-validation`,
branch `main`, under `tubitak/` — registrations, results, audits, the corrections log,
evidence and standing practices. `EVIDENCE.md` here pins the commit each number was
read at. Read `tubitak/` there for numbers; never re-derive a number here. Every number
that enters the manuscript must cite the gate or registration it came from, and must
state its inference path.

`mvy0502/GenCP` (branch `tubitak-tr`) is the working repository for the pix2pix fork,
the QGIS plugin and the corpus chain. It is not where the paper's numbers are read from.

*Corrected 2026-09-13. The 26 August text of this file said the record lived in GenCP
`tubitak-tr` and that gencp-validation was "a handover snapshot, not the source of
record". That was written at 07:05 that day and was overtaken by the deletion commit
(`b815b46`) the same afternoon, which moved the research record to gencp-validation.
`EVIDENCE.md` had already been re-pinned to gencp-validation `main`; this file had not
caught up.*

## The manuscript lives here — from 13 September 2026

The Markdown drafts of Sections II, III and IV were moved here from
`gencp-validation/tubitak/docs/` into `manuscript/drafts/` (history stays there). The
reasons, recorded in both repositories' handover files:

1. gencp-validation is a delivered artifact; manuscript churn there blurs what was
   delivered.
2. The paper cites gencp-validation at pinned commits; a citation target should be stable.
3. This repository exists for the manuscript and is private, which is right for
   unpublished work.

Do not write manuscript text into gencp-validation. Do not copy analysis code here.
