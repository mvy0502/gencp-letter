# The condensation rule — recorded 13 September 2026, before it is needed

The arXiv version is drafted at full length. The IEEE GRSL letter is a condensation of it,
performed in October after the preprint is out. This note exists because the condensation
is where the easiest mistake of the project will be made, under time pressure, by someone
who has read the long version so often that its qualifications feel like repetition.

## The rule

**The condensation may cut evidence and detail. It may never cut a qualification.**

If a claim cannot be made in five pages with its qualifications intact, **the claim
narrows**; the qualification does not drop. A narrower claim with its qualification is a
smaller true statement. A broad claim without its qualification is a false one, and false
in exactly the way this paper says the upstream work is.

What counts as a qualification, so nobody argues it is detail: every sentence that says
what a number is *not* — not pooled, not re-measured for these arms, not a complete
explanation, chip-level at one seed, reported not required, a lower bound, read off the
curve rather than matched to a band, conditional on the input carrying information, one
city. The protected interaction disclosure (five elements, paper-context-addendum.md §24).
The two caveats that travel with the scope sentences. The data-availability absences.

What may go: worked examples; the second of two illustrations; per-seed value lists where
the count and the range suffice; the mechanical note in IV-E; the "what this row is not"
paragraph in IV-A; prose that restates a table.

## Procedure

1. Before cutting, list every qualification in the long version with its section. That
   list is the checklist; the condensed draft is checked against it, not against memory.
2. Cut evidence and detail first. Re-measure. Only then decide whether any claim narrows.
3. A claim that narrows is narrowed in the long version in the same commit, so the two
   versions never say different things about one result.
4. The condensed draft is diffed against the qualification list before it goes anywhere.

## Version bookkeeping

- The arXiv version is the **pre-submission** version: the manuscript as it stood before
  it was submitted to the journal.
- At submission, the IEEE copyright notice goes on the arXiv record.
- At acceptance, the DOI of the published version is added to the arXiv record.
- A number that changes in revision changes through EVIDENCE.md's change log, as always.

## Targets flagged 14 September 2026 (P11 C.12), not cut

- IV-A "The result" restates III-H's 0.986 / 0.277 / 3.6 in near-identical words; Table II row 1 states them a third time. Section III reports and Section IV answers, so three statements are by design, but in the letter one of III-H and IV-A can become a pointer. The verbatim mechanism clause was already replaced by a pointer in IV-A.
- The Fig. 3 caption now cites (1a) instead of restating it; the same can be done wherever a caption re-describes a defined quantity.
