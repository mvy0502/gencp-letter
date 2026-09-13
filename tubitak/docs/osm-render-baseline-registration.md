# Registration — the rasterised OpenStreetMap render as a reference candidate (premise check)

**Registered 13 September 2026, committed before any chip was matched.** Opened by the
supervising session on 13 September 2026. Never run before, never registered before, and
absent from the open-items ledger until this entry. Standing practice 4 governs: nothing
below is adjusted after the numbers exist.

## The question

If generated reference imagery invents structure, why not match the real scene against
the rasterised OpenStreetMap render itself and skip the generator? This is the most
obvious question a reviewer can ask the letter, and the record does not answer it.

## (a) The measurement

The warped input render of each of the 130 Ankara chips — the file the arms were rendered
*from*, committed at `evidence/rasters/input_render_warped/` (130 files, sha256 in
`MANIFEST.md`; byte-identical to `tool_runs/C45_s{S}_modal/warp/input/` at every seed) —
is used directly as the reference chip and matched against real Sentinel-2 with **the Table I
arms' own invocation, unchanged**: `karios process <render> <run/ref/<stem>_warp.tif>
--conf tubitak/configs/karios_gencp.json --no-log-file` (config sha256 `8eaa5bd8cdae066d…`;
KLT, confidence threshold 0.8, the 228 × 228 window at 10 m; KARIOS 2.2.0-dev, the binary
every arm was scored with). Per-chip statistic: the median of hypot(dx, dy) over the KLT
rows, n = rows — the `c45_score.py` formula. **Nothing about the matcher is changed to make
the render work better.** If it matches badly, that is the result.

*One correction to the instruction that opened this registration, recorded here so it is
not read as a deviation:* the instruction asked for "the same BT.601 gray conversion". The
Table I arms' KLT path has no BT.601 step — KARIOS received the three-band warped rasters —
so applying one would change the matcher input relative to Table I. The BT.601 conversion
belongs to the edge-ratio measurement and to the production-path headline (B2), not to
Table I. The render follows Table I's actual path.

## (b) The inference path, stated before the number exists

The input render is seed-invariant, so this measurement produces **one number per chip**,
not six. There is no seed-level inference available and none will be manufactured. Every
comparison against an arm is a **paired per-chip difference over 130 chips at the chip
level**, D = render − arm, positive = render worse, standard error across chips, and is
labelled **chip-level** everywhere it appears, including in any table caption. For the four
fine-tuned arms the comparison is made against each confirmatory seed (45–50) separately
and reported as the mean and range of the six chip-level paired means — six chip-level
numbers, not a seed-level inference. Against the pretrained arm, which is seed-invariant,
once.

## (c) The point count

Median surviving matches per chip is reported beside the residual, with the count of chips
that produced no match at all. Equal-count truncation, as in Section III-D of the letter:
per chip, K = min(render's count, arm's count at that seed); both sets truncated to the
best K by KLT `score` descending, never by residual; medians recomputed; the paired
difference reported beside the raw one. Applied against the four fine-tuned arms at each
seed. **Against the pretrained arm the equal-count version is not constructible on this
path** — its per-chip medians in the record come from a summary file and its KLT rows on
the Table I path are not retained — so the pretrained comparison is raw only, and says so.
Section III-G's own argument forbids reading fewer-but-better as a win; it applies to the
render exactly as to the arms.

## (d) Both outcomes, named in advance, with bands fixed now

- **WELL** — the render's chip-level paired difference against the L1-only arm (the best
  fine-tuned arm) is ≤ 0 at ≥ 2 SE in all six seeds under **both** the raw and the
  equal-count comparison, **and** the render's median surviving points are not below the
  L1-only arm's. *If the render matches well, that is evidence against the premise of the
  whole GenCP approach, including against the usefulness of the tool this internship
  delivered. It is reported in full, in the body, with the same prominence, and it is not
  moved to a footnote or to the limitations section.* It earns a subsection of Section III,
  a statement in the abstract, and a revision of Section I's framing and V-D's scope.
- **POORLY** — the render is worse than every fine-tuned arm at ≥ 2 SE in all six seeds
  (raw), or at least 20 % of chips yield no match at all. *That supports the premise that a
  generated reference is needed at all, and it is reported as a premise check, not as a
  result of the factorial.* It earns a short paragraph in Section III, placed at its end.
- **INTERMEDIATE** — anything else. Reported as intermediate with every number, no
  stronger word, at paragraph length in Section III; whether it also touches Section I is
  decided by the supervising session after seeing it, and that decision is recorded.

The length the result earns is not decided before the number is seen; the placement is.

## (e) What will not be claimed either way

No sweep, no threshold variation, no second matcher, no extension beyond the 130 Ankara
chips, no transfer claim to the rest of Turkey or to Europe, and no seed-level statement
about the render.

## Table I

The render row does **not** enter Table I: its inference path (seed-invariant, chip-level)
differs from the four fine-tuned rows (six-seed means) and the caption would have to carry
both. It is reported in prose or in its own small table, labelled chip-level.

## Invariances

Identical to the Table I arms' scoring: the 130 reference chips `run/ref/<stem>_warp.tif`,
the KARIOS config and binary, the per-chip statistic. The only change is the image
matched: the warped input render in place of a generated image.

## Scripts, committed with this registration and not yet run on data

- `scripts/osm_render_baseline/render_baseline_run.py` — routing only around the arms'
  KARIOS invocation; sha256 `82593cf90d2471a0…`.
- `scripts/osm_render_baseline/render_baseline_analysis.py` — the readings above;
  sha256 `ccf13481a0a6b4ea…`. **Known-false test run before this commit:** `--self-test` plants a
  WELL table, a POORLY table, and two near-misses (fewer points; one seed breaking) that
  must read INTERMEDIATE; output at registration time: "self-test passed: WELL, POORLY, and
  two planted near-misses read INTERMEDIATE". Both scripts refuse unknown arguments.

  *Correction, same day, before any chip was matched.* The commit that carried this
  registration (`a5314b1`) stated that output, but the self-test had not produced it: it
  was launched with the system interpreter, which lacks numpy, and printed a traceback
  that the commit step did not stop on. The self-test was then run with the project
  interpreter and produced exactly that line, and both refusal checks passed; this note
  records the slip rather than rewriting the sentence above. Same class as practice 15's
  origin: a check believed to have run.

## Where it is recorded

New registration, not a reproduction of anything. Open-items ledger: a new item, opened
13 September 2026 by the supervising session, closed by the results document.
