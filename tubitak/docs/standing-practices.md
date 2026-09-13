# Standing practices

Rules of general force, collected where future work will see them. Each carries its origin.

1. **Invariance section in every gate registration** (2026-08-21). Three ill-posed gate
   elements failed the same way — an unstated invariance assumption (same OSM source: false;
   same render path: false; deterministic inference: false). Every gate registration now
   lists explicitly what it assumes identical on both sides: data source, render path, code
   path, determinism. A gate that does not state its invariances does not know what it is
   measuring. Origin: [tool-gate-registration-2.md](tool-gate-registration-2.md) family,
   corrections-log entries 13–15.

2. **K-draw averaging on small subsets** (2026-08-21). Any comparison on roughly n < 60
   chips generates K seeded dropout draws and averages before scoring. Test-time dropout
   noise (~0.1–0.4 px per chip median) is a large relative contributor at small n — it sits
   inside the CI on R, the salt and badlands subsets, and the Cappadocia per-stratum
   numbers. It is removable noise and unaveraged small-n results have been paying it.
   Origin: corrections-log entry 14; Task-3 determinism probe.

3. **No retraining on production-provenance inputs for now** (2026-08-21). The train/serve
   skew is real (training = pre-fix simple-strategy extracts; production = post-fix smart),
   its cost is measured (~0.6 px on forest-heavy chips), and it lands on precisely the class
   the institution intends to mask out — which is fortunate, not designed. Mitigation: the
   reliability layer is weighted against forest; retraining on post-fix inputs is Phase F
   future work, not undertaken now. Origin: phase-c-results Limitations;
   [phase-f-backlog.md](phase-f-backlog.md).

4. **Registrations before numbers; failed gates reported, never adjusted; mis-specified
   gates re-registered with the original preserved** (standing since Phase B, restated here
   for completeness).

5. **Every reported number states its inference path** (2026-08-21). All C-phase and tool
   evaluation numbers were measured on the stochastic (dropout-active) path; the delivered
   tool defaults to the deterministic path (measured agreement |Δ| ≤ 0.05 px at n = 30
   resolution). The invariance rule applied to our own reporting: a reader must see the
   gap, not discover it. Origin: tool-results.md §A; Task 1 decision.

6. **One sign convention, document-wide** (2026-08-21). Δ = candidate − baseline; negative
   = candidate better. "Gain" is defined at point of use as −Δ. Stated at the top of each
   results document. Origin: the regC/+phase-D sign divergence.

7. **Long detached runs checkpoint intermediate results** (2026-08-21). Any run expected to
   outlive a session writes per-item artifacts so a respawn resumes rather than restarts
   (registration B had to be respawned from zero after a session limit). Origin: regB.

8. **Review the open items; do not only append to them** (2026-08-21). At the end of every
   package, [open-items.md](open-items.md) is read from the top; each item is closed or
   explicitly deferred with a written reason. Origin: three headline-deciding findings (the
   cold-D risk, the small-n rule lapse, the unexplained baseline shift) were all items we
   wrote down ourselves and stopped watching. The corrections log records what went wrong;
   nothing before this rule forced revisiting what we flagged as pending.

9. **Registration audits get a fourth leg: does the design support the inference?**
   (2026-08-24). The audit method used on T1, B2/B3 and the phase-C pair has three legs —
   timeline (commit times vs artifact mtimes), recomputation (every reported cell rebuilt from
   raw), and configuration (run configs diffed against the registration text). All three ask
   **whether the numbers are what we say they are**. None asks **what the numbers are evidence
   about**. The fourth leg does: *at what level was the treatment applied, at what level is the
   error bar computed, and are they the same level?* — and, more generally, whether the design
   can support the claim the document draws from it. Origin: the C4/C5 package passed all three
   existing legs on 2026-08-24 and was found the same day, by an adversarial review pass and
   not by us, to rest on a treatment applied once per cell with every standard error computed
   at chip level — 130 chips replicating the evaluation, not the intervention, and an
   interaction term with no run-level error bar at all. The audit that had just cleared it
   would never have caught that, because no leg was pointed at it.
   [seed-replication-registration.md](seed-replication-registration.md) is the correction; this
   practice is so the class is caught next time rather than the instance.

10. **Numerical artifacts that a published number depends on live under `docs/` and are
    tracked** (2026-08-26). `.gitignore` excludes `tubitak/data/*` and `tubitak/outputs/*`
    wholesale, so **no per-chip CSV, summary JSON or analysis script under those paths has
    ever been under version control**. Any such file that a published number rests on is
    committed to `tubitak/docs/evidence/`, with its sha256 recorded in
    [evidence/MANIFEST.md](evidence/MANIFEST.md) and verified against any value already
    published for it. **The scripts that produce those files are committed too** — an output
    without its producer is not reproducible, only re-implementable, and re-implementation
    yields new numbers rather than the published ones. Origin: **Phase D**
    ([phase-d-audit.md](phase-d-audit.md) §C). Six of its seven registered checks and its veto
    rule have no surviving artifact of any kind; `eu_per_chip.csv`,
    `blur_control_per_chip.csv`, `eu_decomposition_per_chip.csv`, `veto_features.csv` and
    `veto_rule.py` do not exist anywhere in the repository; and the sentence that justified not
    committing them — "regenerable end-to-end from committed scripts and registrations" — was
    **false**, because none of those scripts was committed either. Two Table II rows rest on
    numbers nothing in this repository can re-derive. **The rule is not "hash your artifacts".
    A hash proves identity if the file survives; it does not preserve the file.** At the moment
    the Phase D audit was written, the six-seed Modal block — 26 arm-units, one night, $23 of
    GPU — was protected by nothing but sha256 strings in a markdown file. The corrective is
    this practice, and entry 22 (B3's harness deleted, four registered matcher parameters
    permanently unverifiable) is the earlier instance of the same class that this practice
    exists to stop recurring for a third time.

    **Extension, 2026-09-13 — the dual: claims that evidence is absent.** This practice
    governs claims that evidence is present. Its dual is governed here too, because three
    instances in eighteen days (corrections-log entries 35, 42 and 44) made a pattern in the
    most dangerous place a paper has: **a claim about whether evidence exists — present or
    absent, retained or lost, regenerable or not — is itself a claim requiring evidence. It is
    verified by a look at the time it is written, and the method of looking is recorded
    beside it.** The look is not the working tree: it includes the full history of both
    repositories with deleted files, every backup, every run-output directory the claim does
    not mention, and any external record the claim rests on. A claim that names its own search
    is evidence; a claim that does not is an assertion, and the record now distinguishes the
    two by outcome — confirmed absent, found, or genuinely ambiguous — as
    [absence-claims-audit-2026-09-13.md](absence-claims-audit-2026-09-13.md) does for every
    such claim that existed on that date. Placed here rather than minted as a sixteenth
    practice because it states the same class as this practice from the other side, and the
    practice-11 test is met: the class is the claim about existence, not the three instances
    that prompted it.

    **Final clause, added 2026-09-13 by corrections-log entry 35.** After an evidence commit,
    **verify from a fresh clone that the files are actually there.** Not `git status`, which
    is silent about ignored paths, and not `git log`, which reports what was committed rather
    than what was intended: clone the pushed remote into a scratch directory and re-run the
    manifest check against that tree. A file is evidence when a stranger can obtain it, not
    when the committing session believes it was added. If the check cannot be run, the
    artifacts are not committed yet and the manifest rows must not be written. Type rules are
    fixed at the class level: `.gitignore` carries `!tubitak/docs/evidence/**` as its last
    rule. Origin: entry 35 — 260 rasters listed in the manifest with sha256s were never
    tracked, because `*.tif` swallowed them and nobody read the repository state back.

11. **A registration that names a set, a threshold or a condition QUOTES the implementing
    code's expression of it** (2026-08-26). **FORWARD-ONLY.** When a registration fixes a
    reading in prose, the line of code that implements it is quoted in the registration
    itself, so prose and implementation sit in one place and can be checked against each
    other by reading rather than by remembering to compare two files. Origin: **three findings
    that looked like unrelated slips and share one cause — a registration written in prose,
    implemented in code, and the two drifting.**

    - **The warm-up de-confound's branch text** said "as C1 and C4 did", presuming both
      adversarial arms rise at the first main-stage transition. True at seed 42, false at
      seed 43, where C4 falls. The branch fired on its antecedent so nothing changed, but the
      clause had no determinate referent
      ([warmup-deconfound-results.md](warmup-deconfound-results.md) §5).
    - **The hardware gate's acceptance rule** was written as a single global verdict while
      scaling each quantity to its own spread, so the most reproducibly-measured quantity
      governed the package and one quantity vetoed ten
      ([hardware-gate-results.md](hardware-gate-results.md)).
    - **AMENDMENT SEED-c (d)** reads "C5's edge mean the highest of **the four arms**", while
      `seed_analysis.py:212` implements the tie rule as `("pre", "C1", "C2", "C4")` —
      **five arms, including pretrained** ([phase-d-closeout.md](phase-d-closeout.md) §C).
      The harness was stricter than the registration, which is the safe direction, and the
      reading held either way.

    **Not applied retroactively.** The existing registrations stand exactly as written, with
    their mismatches disclosed where they were found and not repaired — the same disposal the
    hardware gate's own flaw received, and for the same reason: a rule rewritten after seeing
    which way it cuts is indistinguishable from a rule adjusted to pass. **When
    corrections-log entries 30–34 are applied, these three are grouped under one heading in
    the tiering**, so a reader sees one class with three instances rather than three
    unrelated slips. *Done 2026-09-13: entries 36–38 under one heading in Tier 1.*

12. **A drafted corrections-log entry lives in `corrections-log.md` itself, under a
    "Drafted, not yet applied" heading, from the moment it is drafted — never as a separate
    file** (2026-09-13). The log is the one document every session re-reads and the one no
    housekeeping pass rebuilds from a copy; a separate draft file is read by nothing yet and
    so passes the deletion check ("does anything read it?") by construction. Applying an
    entry moves it to its tier; an entry still under that heading at the end of a work
    package is an open item under practice 8. **Entries under that heading are not part of
    the record.** The manuscript cites "a public corrections log", and a reader arriving from
    that citation must not read a drafted entry as a correction that was made: a drafted
    entry is a claim awaiting review, and only an entry in a tier is a correction. This
    practice is structural rather than exhortative — it makes the failure impossible instead
    of warning against it. Origin: entry 35's draft, deleted by `6750978` the day after it
    was committed and reported seventeen days later as never having existed. Distinct from
    practice 10, which covers "the commit did not take"; this covers "a correct commit was
    undone by housekeeping with no way to know the file mattered".

13. **Every run records its random seed and the versions of the libraries that affect
    numerics** — at minimum torch, numpy, and the ONNX runtime if used — **in its option
    dump** (adopted 2026-09-13 from the GenCP `CLAUDE.md` list, item 9, where it had stood
    since 2026-08-26). Class: the inputs that determine a run's numerics are recorded with
    the run. Origin: Registration A's stochastic arm cannot be reproduced byte-for-byte
    because neither was recorded.

14. **Every verifier is run against a known-true and a known-false case before its verdict
    is trusted, and also against its degenerate invocations**: no arguments, empty input, a
    missing file, a path that does not exist. A tool that reports success when given
    nothing to check is not a check (adopted 2026-09-13 from `CLAUDE.md` item 10). Class:
    a verifier's verdict is trusted only after the cases that would expose a vacuous
    verdict have been run. Origin: an audit of all 23 verifiers under three degenerate
    invocations found 18 that exited 0; verifiers now refuse arguments they do not
    understand.

15. **A check is born with a failing case.** Write the known-false input first, watch the
    check report it, and only then trust the check (adopted 2026-09-13 from `CLAUDE.md`
    item 11). Class: the order of construction — failing case before the check — not the
    existence of a test afterwards. Origin: three of four checks added late in one package
    could not have caught anything, each written by someone who believed it worked.

    **Mechanism note, 2026-09-13.** This practice was violated on the day it was minted, by
    the mechanism it exists to prevent: a self-test was reported as passing when the
    interpreter that ran it lacked numpy and the commit step did not stop on the traceback
    (`osm-render-baseline-registration.md`, commits `a5314b1` and `e665bc7`). The supervising
    session ruled that no further practice is minted for it: a practice already violated
    once is evidence that restating it will not help. **The general principle: a practice
    that can be enforced mechanically is enforced mechanically rather than restated.** The
    enforcement: `scripts/selftest_gate.py` runs a script's `--self-test` under the project
    interpreter (never whatever `python` resolves to), checks that interpreter can import
    numpy and pandas, exits non-zero on any failure, and prints a `self-test gate: PASS
    <sha16> <script> <interpreter> <time>` token only on success; `scripts/hooks/pre-commit`
    (installed with `cp tubitak/scripts/hooks/pre-commit .git/hooks/pre-commit`) refuses to
    commit any staged `*registration*.md` that mentions `--self-test` without that token. Both
    were born with a failing case: the gate refuses options, and the hook was shown to refuse
    a planted registration before it was installed for real.

16. **When code assumes a unit, it checks that unit where the assumption is made**
    (adopted 2026-09-13 from `CLAUDE.md` item 12). Class: an assumed unit is enforced at
    the point of assumption, not relied on through every caller. Origin: four bugs that are
    one sentence, *code that assumes metres met a geographic CRS*; see
    `vectors.require_metric`.

---

## Numbering note — 2026-09-13

**This file is the canonical list.** Every "standing practice N" in the study repository
resolves here. Two other lists exist and their numbers differ:

- **paper-context-addendum.md §11** — an eight-item summary written 24 August with its own
  numbering; superseded, with a mapping table at its head.
- **The GenCP working repository's `CLAUDE.md`, "Standing practices"** — twelve items, not
  public with the preprint. Mapping, CLAUDE.md → this file: 1 → 1 (invariance); 2 → 5
  (inference path); 3 → 6 (sign convention); 4 → 4 (registrations before outcomes);
  5 → *none* (registration text names the exact corpus and reference directory);
  6 → 4 (failed gates reported, never adjusted); 7 → 7 (checkpointing and counted
  liveness); 8 → 8 (open items); 9 → 13; 10 → 14; 11 → 15; 12 → 16 (all four adopted 2026-09-13, see above;
  the earlier version of this note said they had no number here). CLAUDE.md 5 remains
  without a canonical number: it failed the class test recorded in corrections-log entry
  43, and may be rewritten and reproposed.

Citations found on 2026-09-13 that resolved to the wrong practice under this file's numbering
carry a dated note at the citation; none was silently renumbered. They are: `BACKUP.md`
(two, "practice 9" meaning CLAUDE.md 9), `confidence-registration.md`,
`confidence-registration-2.md`, `confidence-registration-3.md` (one each, the same),
`MANIFEST.md` ("practice 9" meaning this file's 10), `plugin-gate-registrations.md` and
`plugin-results.md` ("practice 6" meaning CLAUDE.md 6, this file's 4), `plugin-results.md`
("practice 22", which is corrections-log entry 22), `tool-gate-registration-2.md` and
`verifier-degenerate-audit.md` (both already say "in CLAUDE.md"; the note makes the
absence of a canonical number explicit). Origin: the two public documents would otherwise
resolve one citation to two different rules.
