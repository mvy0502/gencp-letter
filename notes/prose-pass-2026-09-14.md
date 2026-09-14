# Prose pass, 14 September 2026 (P12) — record

Corpus: `style-corpus-2026-09-14.md` (twelve arXiv papers, six written 2017–2022, six from 2024–2025). Measures: `tools/style_measures.py`, prose only. Three independent readers (a naive domain reviewer with the PDF alone; a stylometric analyst with the measurement table and the corpus; an adversary briefed to argue for machine authorship). Checks that the pass changed nothing but prose: `tools/prose_pass_checks.py` with `protected-phrases.txt`, plus `tools/term_first_use.py`.

## Measurements before the pass (letter at 66fee6a)

```
measure                      letter |   corpus min-max        p10-p90 |  older p10-p90  recent p10-p90 | flag
sent_mean                      28.1 |    19.1-27.2       19.2-23.8    |   19.1-20.4       20.1-21.3    | ABOVE
sent_median                    25.0 |      18-27.0       18.0-21.0    |     18-19.0         18-21.0    | ABOVE
sent_sd                        21.5 |     8.9-14.7        9.5-12.7    |    9.9-12.2        8.9-11.6    | ABOVE
sent_p90                         51 |      31-43           31-41      |     31-36           31-36      | ABOVE
sent_max                        242 |      57-96           65-89      |     57-89           65-78      | ABOVE
burstiness                    0.765 |   0.421-0.604     0.466-0.58    |  0.516-0.58      0.421-0.535   | ABOVE
par_sent_mean                  3.67 |    4.12-8.88       4.34-7.75    |   4.12-6.59       5.51-7.67    | BELOW
par_sent_sd                    2.12 |    4.15-6.39       4.59-6.33    |   4.15-5.82       4.59-6.27    | BELOW
par_sent_max                     13 |      14-39           20-35      |     14-35           20-21      | BELOW
semicolons                     9.46 |     0.0-2.59        0.0-2.01    |   0.26-1.97        0.0-0.88    | ABOVE
colons                         7.87 |    0.72-8.41        2.3-7.12    |   0.72-6.97       2.71-4.65    | ABOVE
parentheticals                 6.02 |     2.7-25.48      7.45-24.35   |   8.85-24.35       2.7-11.35   | BELOW
dashes                         4.06 |     0.0-3.95        0.0-1.97    |    0.0-0.19       0.25-0.77    | ABOVE
not_but_per_100_sent            3.1 |     0.0-2.1         0.0-0.5     |    0.0-0.3         0.0-0.3     | ABOVE
tricolon_per_100_sent           6.6 |     0.5-14.5        2.7-11.6    |    0.5-8.5         5.1-11.6    | 
first_person_per_1000          2.95 |    1.86-20.29      2.51-17.42   |   1.86-8.42        5.8-17.42   | 
hedges_per_1000                3.93 |    1.26-6.6        1.86-4.59    |   1.86-4.59       1.26-3.72    | 
nominalisation_per_1000       37.24 |   30.82-85.26     44.03-70.52   |  30.82-62.16     54.38-70.52   | BELOW
opener_variety                0.293 |   0.294-0.566     0.294-0.473   |  0.294-0.424     0.294-0.422   | BELOW
ttr_mattr500                  0.484 |   0.423-0.567     0.436-0.502   |  0.423-0.461     0.441-0.502   | 

letter: words 8137 sentences 290 paragraphs 79 top openers [['the', 113], ['a', 17], ['this', 9], ['it', 9], ['what', 8], ['two', 6], ['every', 6], ['an', 5]]
share of sentences opening with 'the': letter 0.39 ; corpus [('1801.08467', 0.21), ('1808.06194', 0.08), ('1901.08236', 0.18), ('2103.16871', 0.15), ('2202.13347', 0.13), ('2212.02277', 0.08), ('2401.00440', 0.13), ('2407.06095', 0.13), ('2408.05777', 0.11), ('2503.16185', 0.11), ('2507.04397', 0.15), ('2511.00598', 0.12)]
1801.08467 words 3050 sent 112 mean 27.2 burst 0.54 top [['the', 23], ['in', 14], ['this', 5], ['we', 5]]
1808.06194 words 7716 sent 401 mean 19.2 burst 0.539 top [['this', 43], ['in', 39], ['the', 31], ['moreover', 15]]
1901.08236 words 6973 sent 364 mean 19.2 burst 0.516 top [['the', 64], ['it', 21], ['for', 16], ['in', 11]]
2103.16871 words 8623 sent 452 mean 19.1 burst 0.538 top [['the', 69], ['in', 40], ['this', 34], ['citation', 16]]
2202.13347 words 10758 sent 528 mean 20.4 burst 0.58 top [['the', 67], ['in', 41], ['ieee', 21], ['a', 14]]
2212.02277 words 8086 sent 399 mean 20.3 burst 0.604 top [['the', 33], ['in', 21], ['ieee', 17], ['and', 15]]
2401.00440 words 7521 sent 316 mean 23.8 burst 0.535 top [['the', 42], ['this', 39], ['in', 26], ['to', 16]]
2407.06095 words 6507 sent 307 mean 21.2 burst 0.421 top [['the', 41], ['this', 36], ['in', 14], ['to', 11]]
2408.05777 words 2595 sent 129 mean 20.1 burst 0.514 top [['the', 14], ['this', 7], ['in', 5], ['experiments', 5]]
2503.16185 words 8107 sent 380 mean 21.3 burst 0.527 top [['the', 40], ['in', 32], ['this', 24], ['to', 21]]
2507.04397 words 7960 sent 395 mean 20.2 burst 0.574 top [['the', 59], ['in', 19], ['additionally', 16], ['for', 15]]
2511.00598 words 5618 sent 275 mean 20.4 burst 0.466 top [['the', 32], ['in', 14], ['to', 13], ['however', 13]]
```

After the pass (f7ec4c4): sentence mean 27.1, sd 16.3, max 97, burstiness 0.601, semicolons 8.59, colons 7.22, 'not X but Y' 1.7 per 100 sentences, 'The' opens 116 of 297 sentences (39 %). Every other measure moved by less than its rounding.

## The readers, in summary

- **Reader 1 (naive):** overall verdict that the letter does not read as a person's, on the grounds of a small set of devices used at every paragraph boundary: 'X, not Y' antitheses, the 'reported, not required' refrain, 'what ... is' clefts, count-then-list openers, aphoristic closers, narrated candour ('we state it as one'), the 'travels with / carries' metaphor, two very long inventory sentences. It named four passages that do read as a person's: the footnotes, the geometry paragraph, the Fig. 2 caption, the V-C admissions.
- **Reader 2 (measures):** of thirteen flags, eight fire in the direction away from the machine signature (long, highly variable sentences; dense semicolons; corrective rather than additive contrast; subject-first rather than connective openers; low nominalisation; sparse first person), one is ambiguous (dashes), four are extraction artefacts (paragraph length, parentheticals). The recent corpus half is flatter than the older half on exactly the measures where model assistance would show.
- **Reader 3 (adversary):** the same device list as Reader 1 with counts (32 'rather than', 31 ', not', 10 'what' clefts, 10 count announcements, 11 objection/test/result/reading labels), plus two items discounted in triangulation: over-consistent cross-referencing, and a voice match with the project's own instruction file, which is the discipline the letter was written under and not evidence about who typed it.

## Triangulation and the ranked list (two readers = tell; one reader = candidate judged against the voice/tell distinction)

1. 'X, not Y' / 'rather than' used as a connector rather than as a qualification (R1, R3; measured above band) — thinned where it carried no qualification.
2. Narrated candour: 'we state it as one', 'we name it as such', 'is named as such', 'We state it that way because ...', 'stated here rather than in a footnote', 'this is stated so that ...' (R1, R3) — removed; the disclosures themselves stay.
3. 'What ... is' clefts (R1, R3) — four of seven rewritten; headings untouched.
4. Count-then-list fragments: 'Two sentences of scope.', 'Not "GANs are bad".' (R1, R3) — rewritten as sentences; the ordinary count sentences ('Five limitations arose ...') left.
5. The 242-word data-availability inventory and the 136-word III-L sentence (R1, R3; R2 called them human but breakable) — split.
6. 'reported, not required' verbatim four times (R1, R3) — the second III-B instance reworded with the same substance; the others stay (a binding qualification).
7. Aphoristic closers with polyptoton or chiasmus: 'conditional means there is a condition', 'restrained by', the IV-E epigram, the introduction's control-point line (R1, R3) — plainer.
8. The 'travels with' metaphor three times, 'carries' five (R1, R3) — two 'travels' replaced; 'carries' left.
9. Three consecutive meta-sentences in III-E (R1; R3 lists the closers) — merged to two.
10. 'consistent rather than comfortable' twice within ten lines (R1) — second instance removed, first kept.
11. Body sentence duplicating the Fig. 4 caption's line (R1) — body varied.
12. Trailing-adverb tags: 'which is our mechanism, predicted', 'deliberately' (R3; R1 in passing) — rewritten.
13. The reviewer wink 'and it is ours rather than a reviewer's' (R1, R3) — 'which we raise ourselves'.
14. Colon-fronted announcement 'The claim of this letter:' (R1, R3) — a sentence; the abstract's 'The design rule:' is protected and stays.
15. Triple-qualified II-D sentence (R1) — split.
16. 'The' opening 39 % of sentences (R2; twice the corpus maximum) — the openers this pass itself introduced were varied; the pre-existing pattern was left, as Reader 2 read it as a human monotony and forcing variety is forbidden by the brief. It remains the one measured outlier.
17. Discounted: Section IV's labels, the verdict titles, 'to our knowledge' three times on page 1 (binding sentence 2), the V-C limitations paragraph's flatness, the cross-reference density, the instruction-file voice match.

## Every change, before and after

**1. 01-introduction — colon-fronted announcement**

> before: The claim of this letter: plausibility pressure degrades generated reference imagery for geometric matching.

> after: This letter claims that plausibility pressure degrades generated reference imagery for geometric matching.

**2. 01-introduction — announce-then-deliver fragment**

> before: Two sentences of scope. At 10~m the premise for a generated reference does not bind:

> after: Two facts fix the scope. At 10~m the premise for a generated reference does not bind:

**3. 01-introduction — aphoristic closer with repeated noun**

> before: An invented edge is a false control point, and for georeferencing a false control point is worse than no control point, because it displaces the solution silently.

> after: An invented edge becomes a false control point, and for georeferencing that is worse than having none, because it displaces the solution silently.

**4. 01-introduction — trailing-adverb tag**

> before: false detail, which is our mechanism, predicted.

> after: false detail, which is the mechanism we propose, predicted before we measured it.

**5. 02-methods — rather-than tic, paragraph closer**

> before: discriminator at full learning rate is unstable, so the asymmetry is a property of the design rather than an accident of it.

> after: discriminator at full learning rate is unstable, so the asymmetry is built into the design.

**6. 02-methods — rather-than tic, two paragraphs running**

> before: Its consequence is measured rather than assumed negligible.

> after: We measured its consequence instead of assuming it negligible.

**7. 02-methods — defensive 'not an X' tag**

> before: list, quantified in II-A, not an omission from it.

> after: list, quantified in II-A.

**8. 02-methods — narrated candour**

> before: but it is a deviation from the published training setup and we state it as one.

> after: but it remains a deviation from the published training setup.

**9. 02-methods — narrated candour**

> before: This is selection on a post-treatment variable and we name it as such.

> after: This is selection on a post-treatment variable.

**10. 02-methods — two near-identical closing sentences**

> before: A minimum-match-count sweep over all four arms jointly is reported alongside it. Both are reported in Section III.

> after: A minimum-match-count sweep over all four arms jointly accompanies it; both appear in Section III.

**11. 02-methods — rather-than tic**

> before: Point-level common support is not constructible here, and we report that rather than approximating it.

> after: Point-level common support is not constructible here, and we did not approximate it.

**12. 02-methods — triple-qualified sentence, split**

> before: It is ranked by match score and never by residual, which would be circular; match score is itself post-treatment, so this removes the count asymmetry rather than all conditioning, and no result here is unbiased.

> after: It is ranked by match score and never by residual, which would be circular. Match score is itself post-treatment, so the truncation removes the count asymmetry and leaves the rest of the conditioning in place; no result here is unbiased.

**13. 02-methods — trailing-adverb tag**

> before: The set $\Omega$ is defined by the input, not by the ground truth, deliberately: it separates

> after: We define $\Omega$ by the input and not by the ground truth because that is what separates

**14. 02-methods — 'travels with' metaphor reused**

> before: The qualifier travels with the claim: the systematic component

> after: The claim needs its qualifier: the systematic component

**15. 03-results — verbatim refrain, second instance varied**

> before: its seed-level mean is $+0.677$~px with a 95\% interval of $[+0.617, +0.737]$, reported, not required.

> after: its seed-level mean is $+0.677$~px with a 95\% interval of $[+0.617, +0.737]$; the interval is reported, and it was not a gate either.

**16. 03-results — same antithesis twice within ten lines**

> before: What the comparison does license is the reading already given: a consistent small effect, not a comfortable one.

> after: The comparison licenses the reading already given, and no more.

**17. 03-results — three consecutive meta-sentences**

> before: The shape is therefore reported and not claimed. What the figure supports is the registered reading and nothing finer. This is a training-time curve and is confounded with convergence; it is reported as a curve, not as a dose.

> after: The shape is therefore reported, not claimed; the figure supports the registered reading and nothing finer. The curve is confounded with convergence, because the arms were trained longer rather than dosed.

**18. 03-results — polyptoton aphorism**

> before: The suppression is conditional, and conditional means there is a condition.

> after: The suppression is conditional, and the condition can be shown.

**19. 03-results — aphorism duplicated in the Fig. 4 caption**

> before: Information absent from the input cannot be recovered, and an arm with nothing to copy fills the frame from its prior; restraint operates only where there is something to be restrained by.

> after: Information absent from the input cannot be recovered; an arm with nothing to copy fills the frame from its prior.

**20. 03-results — 'not about X; it is about Y'**

> before: The harm is not about feature count; it is about features with no grounding in the input.

> after: The harm comes from features with no grounding in the input rather than from their number.

**21. 03-results — 'what makes it X is' cleft**

> before: What makes it reportable is that it happens on the quantity a mechanistic claim was built on,

> after: It is reportable because it happens on the quantity a mechanistic claim was built on,

**22. 03-results — fragment opener plus two 'what' clefts**

> before: Registered before the training logs were read and scored at six seeds. What the data supports: in every seed, each adversarial arm reduces its reconstruction loss less than its non-adversarial counterpart---six of six in both families. What it does not support: that adversarial arms fail to reduce the reconstruction loss.

> after: This trend was registered before the training logs were read and scored at six seeds. The data supports this much: in every seed, each adversarial arm reduces its reconstruction loss less than its non-adversarial counterpart, six of six in both families. It does not support the stronger claim that adversarial arms fail to reduce the reconstruction loss at all.

**23. 03-results — 136-word sentence, split**

> before: Where the render matches, it localises better than every generated arm: the median over chips of its per-chip median residual is 0.583~px (the mean over chips, 0.797~px), and the paired chip-level difference render minus arm over those 123 chips is $-1.715 \pm 0.091$~px against the pretrained generator, between $-1.15$ and $-1.22$~px against \advLone{}, between $-1.13$ and $-1.22$~px against \advLPIPS{}, between $-0.53$ and $-0.57$~px against \LPIPSonly{} and between $-0.44$ and $-0.56$~px against \Lone{} across the six seeds' arms, every one at six standard errors or more; under the equal-count truncation

> after: Where the render matches, it localises better than every generated arm. The median over chips of its per-chip median residual is 0.583~px (the mean over chips, 0.797~px). The paired chip-level difference, render minus arm over those 123 chips, is $-1.715 \pm 0.091$~px against the pretrained generator; across the six seeds' arms it lies between $-1.15$ and $-1.22$~px against \advLone{}, between $-1.13$ and $-1.22$~px against \advLPIPS{}, between $-0.53$ and $-0.57$~px against \LPIPSonly{} and between $-0.44$ and $-0.56$~px against \Lone{}, every one at six standard errors or more. Under the equal-count truncation

**24. 03-results — narrated candour**

> before: The comparison set bounds the residual half of this finding and is named as such: the 123 chips are

> after: The comparison set bounds the residual half of this finding: the 123 chips are

**25. 04-alternatives — wink at the reviewer**

> before: The caveat, and it is ours rather than a reviewer's.

> after: The caveat, which we raise ourselves.

**26. 04-alternatives — narrated candour**

> before: The registered bands for this sweep did not anticipate that shape, and the conclusion is read off the curve rather than matched to a band. We state it that way because presenting it as a clean band hit would misrepresent how it was obtained.

> after: The registered bands for this sweep did not anticipate that shape, and the conclusion is read off the curve rather than matched to a band.

**27. 04-alternatives — 'and it is the reason' tag**

> before: Two matcher families agreeing on the same chips is stronger evidence than either alone, and it is the reason this row is reported as two tests rather than one.

> after: Two matcher families agreeing on the same chips is stronger evidence than either alone, which is why this row reports two tests.

**28. 04-alternatives — 'not a fallback' narration**

> before: The design argument is not a fallback: it is stronger, because it depends on the structure of the experiment rather than on a computation, and nothing can be lost that would make it unverifiable.

> after: The design argument is the stronger of the two: it depends on the structure of the experiment, not on a computation, and nothing can be lost that would make it unverifiable.

**29. 04-alternatives — two-sentence crossed epigram**

> before: A blurred template gives a broad correlation peak; invented structure gives a sharp peak in the wrong place. A broad peak in the right place localises better than a sharp peak in the wrong one, and that is true of any matcher that localises by correlation.

> after: A blurred template gives a broad correlation peak in the right place; invented structure gives a sharp peak in the wrong one, and any matcher that localises by correlation prefers the first.

**30. 05-discussion — 'what X adds is not A but B'**

> before: What the factorial adds is not a refinement of the theory but a statement about who pays for movement along its axis:

> after: Instead of refining the theory, the factorial says who pays for movement along its axis:

**31. 05-discussion — 'travel with' metaphor, third use**

> before: Two caveats travel with results stated elsewhere.

> after: Two caveats belong to results stated elsewhere.

**32. 05-discussion — fragment opener**

> before: Not ``GANs are bad''. The claim is about the consumer:

> after: The generalisation is narrower than ``GANs are bad''. It is about the consumer:

**33. 06-data-availability — 242-word inventory sentence, split**

> before: Every separately registered body of evidence is named here rather than covered generically, so that a reader looking for the evidence behind a specific claim finds it named: the six-seed block (per-chip residuals, surviving-point counts and input-silent edge ratios for all five arms at seeds 45--50, Section~III-A to III-D and III-F); the two-seed block at seeds 43--44 and the hardware gate, the registered poolability comparison of Section~II-A, with its re-run of seed 43 (Section~II-A and III-C); the informative-mask test (Section~III-H and Table~II); the equal-count truncation and the minimum-match-count sweep (Section~III-G); the warm-up and learning-rate probes at seed 43, one set of runs read under two registrations, with their training-loss logs (Section~II-A and III-J); the six-seed training-loss trend and the generating run's seed-42 loss logs behind the cross-platform comparison (Section~III-J); the epoch sweep behind the training-time curve, 24 cells at epochs 1, 2, 5 and 10 (Section~III-E), with the 96 generator checkpoints it read held outside the repository and listed by hash; the single-seed checkpoint sweep and the descriptor-family and matcher-family registrations behind Table~II; the 260 seed-independent rasters the edge-ratio measurement reads; the OSM-render premise check (Section~III-L), 130 chip-level residuals and counts with its registration; and, in the only form they were retained, the scope measurements of Section~I (scene availability over 24 extents and the currency test), recorded as tables in the positioning results document with no per-chip artifact, and the two-pixel common-point count of Section~II-D, recorded in the common-support registration's table only.

> after: Every separately registered body of evidence is named here, so that a reader looking for the evidence behind a specific claim finds it. The six-seed block holds per-chip residuals, surviving-point counts and input-silent edge ratios for all five arms at seeds 45--50 (Section~III-A to III-D and III-F). The two-seed block at seeds 43--44 sits beside the hardware gate, the registered poolability comparison of Section~II-A, with its re-run of seed 43 (Section~II-A and III-C). The informative-mask test is under Section~III-H and Table~II; the equal-count truncation and the minimum-match-count sweep under Section~III-G. The warm-up and learning-rate probes at seed 43 are one set of runs read under two registrations, kept with their training-loss logs (Section~II-A and III-J), as are the six-seed training-loss trend and the generating run's seed-42 loss logs behind the cross-platform comparison (Section~III-J). The epoch sweep behind the training-time curve has 24 cells at epochs 1, 2, 5 and 10 (Section~III-E); the 96 generator checkpoints it read are held outside the repository and listed by hash. The single-seed checkpoint sweep and the descriptor-family and matcher-family registrations behind Table~II are there, as are the 260 seed-independent rasters the edge-ratio measurement reads and the OSM-render premise check (Section~III-L), 130 chip-level residuals and counts with its registration. In the only form they were retained, the scope measurements of Section~I (scene availability over 24 extents and the currency test), recorded as tables in the positioning results document with no per-chip artifact, and the two-pixel common-point count of Section~II-D, recorded in the common-support registration's table only, are named here as well.

**34. 06-data-availability — narrated candour**

> before: Three things are not available, and are stated here rather than in a footnote.

> after: Three things are not available.

**35. 06-data-availability — narrated candour**

> before: are not in that backup and exist on one machine; this is stated so that the backup is not read as covering them.

> after: are not in that backup and exist on one machine.

## Part F

F.1 numeric tokens: 634 before, 632 after; every numeric token identical. The differences are three pronoun 'one's removed with the tic clauses ('we state it as one', 'not a comfortable one', 'two tests rather than one') and one 'two' added in 'the stronger of the two'. F.2 term first-use check: 11 of 11 pass. F.3 every protected phrase present at or above its minimum count. F.4 the sixteen binding sentences hold as at P10. F.5 build clean, 12 pages, no overfull boxes; figures on the pages of their first references as before.
