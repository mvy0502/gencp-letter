# Section V re-cost against the current limitations list — 13 September 2026

Requested 26 August 2026, never done; done here before any Section V prose is drafted.
Section V is undrafted, so every figure below is an **estimate**, costed per item at the
moment of addition and labelled as such (the Section III lesson: a 100-word estimate for
material that does not yet exist in draft is an estimate). Analogues from the drafted
sections are named where one exists, so each estimate can be checked when the block is
drafted.

Sources are read at gencp-validation `main` 29d2ee1 (13 September 2026), the commit that
moved the drafts here; the record itself is unchanged since 55941c7.

## The allocation being re-costed

Skeleton V, 24 August, 450 words: design rule 60, relation to theory 90, Cramér-Rao 25,
limitations 180, what generalises 80. The reconciled budget carried it at 435, "not
re-costed against current content; likely low, since the limitations list has grown".

## Block-by-block

| block | 24 Aug | re-cost | basis | what changed |
|---|---|---|---|---|
| V.1 Design rule | 60 | **60** | estimated | Wording changes, length does not. The rule is now "do not train it under plausibility pressure" (title change of 26 Aug), not "no adversarial loss, prefer per-pixel". The operational figure is no longer blocked: packageA is audited, verdict QUOTABLE WITH CAVEATS. Two candidate figures exist and one must be chosen before drafting: B2's production-path C2 = 0.593 ± 0.041 px (K = 8, n = 20, POST inputs) or packageA's urban headline C2 = 0.591 px (n = 20, BT.601 KLT, reproduced exact). Neither has an EVIDENCE.md row yet |
| V.2 Relation to theory | 90 | **90** | estimated | Content replaced, not amended. "Substitutability between sources of plausibility pressure" is dead: it was the interaction claim, which failed 5/6 on all three scales and is not made. What the factorial adds instead: both sources carry a penalty independently, each 6/6 at seed level, with no interaction claimed. Same length, different sentence, and the old sentence must not survive in any form |
| V.3 Cramér-Rao | 25 | **25** | estimated | Unchanged |
| V.4 Limitations | 180 | **~415** | estimated, per item below | The list grew from 7 items to 12, and the 5 new ones each carry a measurement or a scope statement, which the old ones mostly did not |
| V.5 What generalises | 80 | **~100** | estimated | Adds the scope-boundary sentence the 05-discussion comment block requires: the 10 m premise fails; sub-metre is where it binds (~20) |
| Repository pointer (from the merged conclusion) | — | **~20** | estimated | Was in the deleted 07-conclusion; never costed in V |
| **Total** | **435–450** | **~710** | | **+260 to +275** |

## V.4 Limitations, item by item

Old items, 24 August list (each a sentence; measured analogue: none drafted, but the
reconciled budget's own reading was "each limitation is a sentence rather than an
argument", ~20–25 words each):

| # | item | est. | note |
|---|---|---|---|
| 1 | Institution's own matcher never measured; every number is a proxy; matcher-independence bounds it | 30 | now rests on two registrations (B3 descriptor families + packageA matcher families), and the sentence gains a clause |
| 2 | Discriminator not published | 15 | II-C carries the full disclosure; V needs one clause |
| 3 | OSM positional accuracy never separated; ceiling unmeasured | 25 | unchanged |
| 4 | torchmetrics 1.9.0 vs upstream 0.11.0; LPIPS drift | 20 | unchanged |
| 5 | Known-displacement recovery not run for C4/C5 | 15 | protocol itself moved to the second paper; one clause stays |
| 6 | Forest under-representation, ~0.6 px on forest-heavy chips | 25 | unchanged |
| 7 | B3's harness not preserved; four matcher parameters as configured, not verified | 25 | entry 22; now the first instance of the class item 9 is the second instance of, and the two can share a sentence |
| | **subtotal, old list** | **~155** | consistent with the 180 allocated |

New items, from the 26 August work and the audits:

| # | item | est. | source | what V must say that II–IV do not |
|---|---|---|---|---|
| 8 | LR schedule asymmetry and its measured bound | 40 | lr-confound-results §3; seed-replication-registration (known asymmetries) | II-A already carries the disclosure and the bound (+0.007 ± 0.034 px, ~1% of the gap). V carries the limitation form: **the bound is chip-level, at one seed** (seed 43, Modal, n = 1, a mechanism probe); and it tests the schedule on the non-adversarial arms only — the reverse manipulation (adversarial arms without warm-up) was not run, so it does not establish that those arms would be unaffected |
| 9 | Phase D evidence loss | 60 | phase-d-audit §C; phase-d-closeout D-2, D-4; standing practice 10; drafted entries 32–34 | Six of seven registered checks and the veto rule have no surviving artifact; the scripts were never committed; the input imagery is gone too (no C2 output survives at any site), so the procedures could not be re-run even with scripts. Two registered items are permanently unrecoverable (check 5's Ankara floor sweep, check 7a's per-stratum gains) and it cannot be determined whether they ran unreported or never ran. IV-D already carries the 86% decomposition's loss; V carries the general statement and the pointer to the data-availability statement |
| 10 | Point-level common support impossible | 30 | common-support-registration §2; II-D | II-D carries the full argument (69/130 chips with zero common points at 2 px; wider tolerance absorbs the signal). V carries the consequence as a limitation: equal-count truncation is the only substitute, it is ranked by a post-treatment score, and **no positional contrast in the letter is free of post-treatment conditioning** |
| 11 | Single-site limit | 30 | confidence-transfer-results ("Ankara is one city") | The factorial's 130 chips are one site. Nothing here establishes transfer to Turkey, still less elsewhere. The European set enters only the matcher rows (B3, packageA), not the registered positional contrasts |
| 12 | Three registration-versus-implementation mismatches | 55 | standing practice 11 | One class, three instances, disclosed and not repaired: the warm-up de-confound's branch text with no determinate referent; the hardware gate's acceptance rule that let one quantity veto ten; AMENDMENT SEED-c (d)'s "four arms" against a harness tie rule over five. In each the reading held either way. Not repaired because a rule rewritten after seeing which way it cuts is indistinguishable from a rule adjusted to pass. They enter the corrections log under one heading when entries 30–34 are applied |
| 13 | Carried caveats the 05-discussion comment block already requires | 40 | open-items 21; paper-context-addendum §22 | E2's null is equally consistent with "currency does not help" and "OSM had not yet recorded the change" (~25). The edge ratio does not order errors within the unrestrained group — III-K carries it in full, V needs a pointer (~15) |
| | **subtotal, new** | **~255** | | |
| | **V.4 total** | **~410–415** | against 180 | **+230 to +235** |

Item 13 is not in the user's list of 13 September; it is in the section's own comment block
from 26 August and is costed so it is not discovered later.

## What this does to the letter total

Re-costed budget of 26 August: 4,601 with V at ~435 (three lines estimated, three measured).
With V at ~710: **~4,875**, five lines of six now costed per item, one (V) still undrafted.
Against the 5-page format's ~3,300 the condensation task is **~1,575 words**, not ~1,300.

The budget-reconciliation's cut candidate "Section V limitations 180 → 140" is no longer
available in that form: 140 words cannot carry 12 items each of which is a disclosure. If the
letter version must shed V.4 words, the candidates are the two items whose full statement
lives elsewhere in the letter (8 and 10, whose limitation form can shrink to pointers) and
item 13's second half — perhaps 60 words, not 275.

## Things that must not enter Section V, recorded so the re-cost is not read as licence

- Any interaction claim, "substitutes", or "the same lever" (dead, 5/6 on three scales).
- E3 in any form.
- "GANs are bad" — the claim is about the consumer.
- The 48-of-49 count or "the single exception" (packageA audit: not reproducible; there are two).
- The chip-level C5−C4 = −0.487 ± 0.053 as a primary or as a replicate.

## Open items surfaced by the re-cost

1. **Choose the V.1 operational figure** (0.593 B2 production-path vs 0.591 packageA urban)
   and give it an EVIDENCE.md row before drafting.
2. **Corrections-log entries 30–34 are still drafted, not applied** (30–31 in
   packageA-audit.md, 32–34 in phase-d-audit.md, plus a drafted addition to entry 26 in the
   warm-up package). The log ends at entry 29. **No document contains a drafted entry 35**;
   if one was intended, it is not written down anywhere in gencp-validation.
3. Item 12's "one heading" grouping in the corrections log depends on item 2.
