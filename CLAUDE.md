# Paper and record repository

From 14 September 2026 this repository holds both the manuscript and the research record.
The record was merged in from `mvy0502/gencp-validation` (`main` at `e26c7fa`, tag
`pre-move-2026-09-14`) with full history and no subtree prefix, so every path under
`tubitak/` and every commit SHA the manuscript cites is the same here as there.

| repository | role from 14 September 2026 |
|---|---|
| `mvy0502/gencp-letter` (this one) | the manuscript (`manuscript/`, `EVIDENCE.md`, `figures/`, `notes/`) and the research record (`tubitak/docs/`, `tubitak/docs/evidence/`, `tubitak/scripts/`); public once the preprint has an identifier |
| `mvy0502/gencp-validation` | the internship delivery as handed over to the institution; frozen, one dated line at the top of its READMEs points here; hosts the plugin releases |
| `mvy0502/GenCP` (`tubitak-tr`) | the working repository for the pix2pix fork, the QGIS plugin and the corpus chain; not where the paper's numbers are read from |

**The merge rule, rewritten with its reason.** The working notes said "no merge in either
direction". That rule existed because merging `tubitak-tr` INTO `gencp-validation` would have
propagated deletions and destroyed the record (263 files). The 14 September merge ran the
other way, `gencp-validation` INTO `gencp-letter`, additively, and deleted nothing. The rule's
letter was broken and its purpose kept; the rule now reads: never merge anything into
`gencp-validation`; the record moves forward only additively and only into this repository.

Rules that continue: every number in the manuscript cites the registration or results
document it came from and states its inference path (`EVIDENCE.md`); no number is re-derived
in the manuscript; research changes to the record are made here and never in
`gencp-validation`; the upstream GenCP directories (`models/`, `data/`, `options/`, `util/`,
root `scripts/`, `test.py`, `train.py`, the two demo directories) are read and imported, never
edited; no emoji in any file. The pre-commit hook (`tubitak/scripts/hooks/pre-commit`) runs
the manifest path check and the practice-15 gate; install it with
`cp tubitak/scripts/hooks/pre-commit .git/hooks/ && chmod +x .git/hooks/pre-commit`.

*History of this file: the 26 August text said the record lived in GenCP `tubitak-tr`; the
13 September correction moved that to gencp-validation; this 14 September text records the
move here. The manuscript's Markdown drafts moved here on 13 September for the reasons
recorded in the repository README of that date (preserved in git history).*
