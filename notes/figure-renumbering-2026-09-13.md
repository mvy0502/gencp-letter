# Figure renumbering, 13 September 2026 (P9 C.3) — enumeration BEFORE the change

Two figures enter ahead of the existing two: the design figure (`fig:design`, Section II-B)
and the sign-replication figure (`fig:signs`, Section III-B). LaTeX numbers by float order,
so the training-time curve (`fig:epochs`) moves from Fig. 1 to Fig. 3 and the panel
comparison (`fig:invention`) from Fig. 2 to Fig. 4. This list was written and committed at
gencp-letter `00c9f9a` before anything was changed; the verification column was filled in
afterwards, against this list.

## gencp-letter

| # | where | text | kind | action | verified after |
|---|---|---|---|---|---|
| L1 | `manuscript/sections/02-methods.tex:110` | `Fig.~2` (the invention measurement) | hard-coded number | replace by `\ref{fig:invention}` (prints 4; a forward reference, as it already was) | |
| L2 | `03-results.tex:1` | `% ... Table I, Fig. 1.` | comment, skeleton-era plan | left; comment, not prose | |
| L3 | `03-results.tex:38` | `% 5. Dose-response, 80 + Fig. 2.` | comment, skeleton-era plan | left | |
| L4 | `03-results.tex:42` | `% 6. Mechanism, 140 + Fig. 1.` | comment, skeleton-era plan | left | |
| L5 | `03-results.tex:184` | `\label{fig:epochs}` | label | no edit; prints 3 after the change | |
| L6 | `03-results.tex:190` | `Fig.~\ref{fig:epochs}` | `\ref` | no edit; prints 3 | |
| L7 | `03-results.tex:223` | `\label{fig:invention}` | label | no edit; prints 4 | |
| L8 | `03-results.tex:227` | `Fig.~\ref{fig:invention}` | `\ref` | no edit; prints 4 | |
| L9 | `03-results.tex:241` | `Fig.~\ref{fig:invention}` | `\ref` | no edit; prints 4 | |
| L10 | `03-results.tex:337` | `Fig.~\ref{fig:invention}a` | `\ref` | no edit; prints 4a | |
| L11 | `04-alternatives.tex:122` | `Fig.~\ref{fig:invention}a` | `\ref` | no edit; prints 4a | |
| L12 | `04-alternatives.tex:153` | `Fig.~\ref{fig:epochs}` | `\ref` | no edit; prints 3 | |
| L13 | `06-data-availability.tex:38` | `the 96 epoch checkpoints behind Fig.~1` | hard-coded number | replace by `\ref{fig:epochs}` (prints 3) | |
| L14 | `figures/README.md:12` | `Fig. 2 (the panel comparison ...)` | record | Fig. 4 | |
| L15 | `figures/README.md:19` | `Fig. 1 (the training-time curve ...)` | record | Fig. 3 | |
| L16 | `figures/README.md` last line | "the curve (III-E) precedes the panels (III-F)" | record | extended with the two new figures | |
| L17 | `EVIDENCE.md:103` | heading `(Fig. 2 as compiled)` | record | Fig. 4 as compiled | |
| L18 | `EVIDENCE.md:113` | heading `(Fig. 1 as compiled)` | record | Fig. 3 as compiled | |
| L19 | `EVIDENCE.md:148` | `II-E and Fig. 2: BT.601 gray` | record | Fig. 4 | |

## gencp-validation (`tubitak/`)

| # | where | text | kind | action | verified after |
|---|---|---|---|---|---|
| V1 | `docs/epoch-curve-registration.md:1` | title: "Fig. 2 as planned; Fig. 1 as compiled" | frozen registration | dated note appended, title untouched | |
| V2 | `docs/epoch-curve-registration.md:69` | "replaces the seed-42 curve as Fig. 2" | frozen registration | same note | |
| V3 | `docs/epoch-curve-results.md:18` | "numbered Fig. 1 in the compiled letter" | results document | dated note appended | |
| V4 | `docs/epoch-curve-results.md:57` | "Fig. 2's terminal point" (skeleton numbering) | results document | same note | |
| V5 | `docs/letter-skeleton.md:88-89` | the 13 Sep numbering note (curve Fig. 1, panels Fig. 2) | plan document | note extended | |
| V6 | `docs/letter-skeleton.md:66, 92, 96, 318, 392, 395` | skeleton-era Fig. 1 / Fig. 2 | plan document | left; covered by the numbering note | |
| V7 | `docs/budget-reconciliation.md:230, 297` | "Fig. 2, the epoch-wise dose-response" (skeleton numbering) | historical costing | left; historical | |
| V8 | `docs/absence-claims-audit-2026-09-13.md:327` | verbatim quote of L14 as it stood | audit quote | left; a quote of that date | |
| V9 | `scripts/seed_eval/epoch_curve_analysis.py:2` | docstring "Fig. 1 as compiled" | script | updated in the grayscale edit (C.4); output file name `fig2_epoch_curve` is a name, left | |
| V10 | `scripts/figures/fig1_invention.py:2` | docstring "Fig. 2 as compiled" | script | dated line added to the docstring; the figure is not regenerated and its README pin stays at the producing commit | |
