# Plausibility Pressure Degrades Generated Reference Imagery for Geometric Matching

This repository holds the letter, its LaTeX source, and the complete research record
behind every number in it: registrations written before the runs, results documents, the
corrections log, the standing practices, the per-chip evidence files with their hashes, and
the frozen analysis scripts.

**The claim.** A conditional GAN that renders a Sentinel-2-like image from OpenStreetMap
and land cover was proposed as a reference for satellite georeferencing. A 2 × 2 factorial
crosses an adversarial term with the reconstruction loss (L1 against LPIPS) and scores each
arm by the positional error of feature matches against real Sentinel-2. Removing the
adversarial term improves positional accuracy in all six confirmatory seeds, and the
perceptual loss alone, with no discriminator anywhere, carries its own penalty in all six.
The common factor is plausibility pressure: where the conditioning input asserts no
structure, a loss that rewards plausibility makes the generator invent edges, and an
invented edge is a false control point. Matched directly, the rasterised map itself
localises better than every generated arm where it matches, on far fewer points. The design
rule: if you generate a reference image for a geometric consumer, do not train it under
plausibility pressure.

**arXiv:** placeholder until the identifier exists. The manuscript is
[`manuscript/letter.tex`](manuscript/letter.tex); build it with `tectonic letter.tex` in
`manuscript/`.

## Layout

| path | what it holds |
|---|---|
| `manuscript/`, `manuscript/sections/` | the LaTeX source, one file per section; `refs.bib`; the Markdown drafts under `manuscript/drafts/` |
| `EVIDENCE.md` | every number in the letter, the document and commit it was read from, and its inference path |
| `figures/` | the four figures and, in `figures/README.md`, the script and commit that produced each |
| `notes/` | the audits of this repository's own record: number audit, presence and absence audits, the prose pass, the submission checklist |
| `tubitak/docs/` | the research record: registrations (`*-registration.md`), results (`*-results.md`), `corrections-log.md`, `standing-practices.md` |
| `tubitak/docs/evidence/` and `tubitak/docs/evidence/MANIFEST.md` | the per-chip artifacts the numbers derive from, every file pinned by sha256 and size in the manifest |
| `tubitak/docs/gates/` | training-loss logs and run logs |
| `tubitak/scripts/` | the frozen analysis scripts, the figure scripts, the self-test gate and the pre-commit hook |
| `tools/` | this repository's own checks: number enumeration, term first-use, protected-phrase and prose measures |
| `models/`, `data/`, `options/`, `util/`, `scripts/`, `test.py`, `train.py`, `GenCP_HR_demo/`, `GenCP_VHR_demo/`, `imgs/`, `gencp_imgs/`, the notebooks | **upstream GenCP code** (a pix2pix fork by Telespazio), redistributed under its BSD 3-Clause [`LICENSE`](LICENSE); read and imported by the evidence scripts, never edited here |
| `docs/`, `tubitak/sr/`, `tubitak/qgis_plugin/`, `tubitak/gencp_core/` | the internship delivery's plugin documentation and code, carried with the history; see the last section |

## How to verify a number

Take the L1-only arm's mean residual in Table I, 1.393 px.

1. The table caption gives the inference path: per chip, the median KLT positional error
   over the arm's own matches; per seed, the mean of the 130 per-chip medians; the entry is
   the mean over seeds 45–50.
2. The data-availability statement names the evidence: the six-seed block, per-chip
   residuals for all five arms at seeds 45–50. Those are
   `tubitak/docs/evidence/C45_s45_modal/C45_per_chip.csv` through `C45_s50_modal/`.
3. Check each file against its manifest row:

   ```bash
   shasum -a 256 tubitak/docs/evidence/C45_s45_modal/C45_per_chip.csv
   grep 'C45_s45_modal/C45_per_chip.csv' tubitak/docs/evidence/MANIFEST.md
   ```

4. Recompute the table from the six files with the frozen script (standard library only):

   ```bash
   python3 tubitak/scripts/seed_eval/table1_six_seed.py
   ```

   The `C2` row prints 1.393. `EVIDENCE.md` records the same number with the commit it
   was read at, and `notes/number-audit-2026-09-14.md` does this for every number in the
   letter.

The whole manifest can be checked at once: `python3 tubitak/scripts/manifest_paths_check.py`
confirms every row's path resolves in the index, and the presence audit in
`tubitak/docs/presence-claims-audit-2026-09-13.md` records the hash check of every row.

## What is not here, and why

- **The generated images of the fine-tuned arms, the training checkpoints and the 96 epoch
  checkpoints** are held in a private backup, verified by hash, and are available on
  request; the data-availability statement says so and says what the backup does not cover.
  Re-inference is possible from the retained checkpoints but is a replication, not a
  reproduction, because test-time dropout is active by the generator's design.
- **Three things are unavailable**, as the data-availability statement details: the
  alternative-explanations package that originally supported two rows of Table II (its
  per-chip artifacts did not survive and its scripts were never committed), the harness of
  the descriptor-family matcher test (four registered parameters are reported as configured,
  not verified), and the generated images of the fine-tuned arms at each seed. Each is an
  entry in the corrections log.
- **The QGIS plugins and the internship delivery** live at
  [`mvy0502/gencp-validation`](https://github.com/mvy0502/gencp-validation), which also
  hosts their releases.

## Relationship to gencp-validation

`gencp-validation` is the internship delivery as handed over to the institution, and it is
frozen from 14 September 2026. This repository carries its full history (merged without a
prefix, so every path and every commit cited in the letter resolves here), and the research
record continues here.
