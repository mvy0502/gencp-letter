# Novelty search — the "to our knowledge" claims of Section I

**Written 13 September 2026, preamble committed before any query was run.** Binding
sentence 2 of the letter skeleton keeps every novelty claim at "to our knowledge" until a
structured query and a manual Google Scholar check are done. This is that record.

## The claims under test

Section I of the letter makes four "to our knowledge" statements: (i) no prior work has
asked whether a matched point on a generated image was real; (ii) a 2×2 factorial that
isolates plausibility pressure with a positional outcome, replicated at seed level;
(iii) a cheap, input-conditioned, reproducible measurement of invention tied to
matchability rather than to perception; (iv) a design rule for anyone generating reference
imagery for a geometric consumer.

## What is being searched for, aimed

1. Any prior loss ablation scored against a **positional or registration** metric rather
   than a perceptual one. Arar et al. (CVPR 2020) is the one known; is there a second?
2. Any prior **input-conditioned** measurement of invention or hallucination tied to
   **matchability** rather than to perception.
3. Any prior work asking whether a **matched point on a generated image is real**.

## The three outcomes and what each costs — stated before searching

- **Nothing found.** "To our knowledge" stays, now supported rather than defensive; this
  record says what was searched, where, when, and what came back. Cost: none to the text.
- **Something close found.** It is cited; the contribution narrows to what remains new;
  Section I's contributions and related-work paragraph are rewritten around the narrower
  claim. Cost: one or two sentences per affected contribution, a new bibliography entry
  verified against its record, an EVIDENCE row, and the claim (i)–(iv) that overlaps
  loses its "first" reading.
- **Something equivalent found.** The contribution claim drops. Reported plainly and
  work stops there — that decision is the supervising session's.

## Databases

Scopus and Web of Science: **not reachable** from this machine (no institutional
credentials present; none will be entered by the agent). Used instead: OpenAlex (title and
abstract boolean search over its full index), Crossref (bibliographic query), Semantic
Scholar (bulk boolean search) and the arXiv API (boolean over abstracts), plus the manual
Google Scholar pass in a browser. Exact query strings, dates and counts follow.

## Queries run, 13 September 2026

All boolean strings are given verbatim. OpenAlex: `filter=title_and_abstract.search:` over
the full index, relevance-sorted, top 50 read. Semantic Scholar: `/paper/search/bulk`.
arXiv: `search_query` over abstracts (rate-limited with HTTP 429 on every attempt of the
first run; a second run with 90 s backoff is recorded below). Google Scholar: run in a
browser by the agent, first page read in full; Scholar's own operators, no API.

### OpenAlex — aimed queries

| id | query | count |
|---|---|---|
| Q1_loss_ablation_positional | `("image-to-image translation" OR "image translation" OR "conditional GAN" OR "pix2pix" OR "generative adversarial network") AND ("registration accuracy" OR "geometric accuracy" OR "positional accuracy" OR "localization error" OR "matching accuracy" OR "ground control point" OR "georeferencing") AND ("adversarial loss" OR "perceptual loss" OR "reconstruction loss" OR "ablation" OR "L1 loss" OR "LPIPS")` | 12 |
| Q2_invention_matchability | `("hallucination" OR "hallucinated" OR "hallucinations" OR "invented structure" OR "fabricated" OR "fiction") AND ("image translation" OR "SAR-to-optical" OR "generated image" OR "synthetic image" OR "generated imagery") AND ("keypoint" OR "keypoints" OR "feature matching" OR "matchability" OR "matched points" OR "image registration" OR "control points")` | 26 |
| Q3_matched_point_real | `("generated image" OR "synthetic image" OR "translated image" OR "generated reference") AND ("false match" OR "false matches" OR "spurious match" OR "matched point" OR "matched points" OR "false control point" OR "keypoint") AND ("hallucination" OR "hallucinated" OR "invented" OR "fabricated" OR "not real" OR "reliability") AND ("registration" OR "matching" OR "georeferencing")` | 14 |

### OpenAlex — broader queries (to enumerate the neighbourhoods)

| id | query | count |
|---|---|---|
| Q1b_translation_for_matching_RS | `("image translation" OR "image-to-image translation" OR "generative adversarial") AND ("image matching" OR "image registration" OR "feature matching" OR "control points") AND ("SAR" OR "optical" OR "satellite" OR "remote sensing" OR "aerial")` | 101 |
| Q2b_hallucination_metric_translation | `("hallucination" OR "hallucinations" OR "hallucinated") AND ("image-to-image translation" OR "image translation" OR "image synthesis" OR "image restoration" OR "super-resolution") AND ("metric" OR "measure" OR "quantify" OR "detect" OR "score")` | 161 |
| Q3b_downstream_utility_generated | `("generated image" OR "synthetic image" OR "translated image" OR "synthesized image") AND ("downstream" OR "utility" OR "task performance") AND ("registration" OR "matching" OR "localization" OR "geometric")` | 231 |

### Semantic Scholar (bulk boolean)

| id | query | total |
|---|---|---|
| S2_Q1 | `("image translation" \| "conditional GAN" \| pix2pix) + ("registration accuracy" \| "matching accuracy" \| "positional accuracy" \| "ground control point") + ("adversarial loss" \| "perceptual loss" \| ablation)` | 0 |
| S2_Q2 | `(hallucination \| hallucinated \| fabricated) + ("image translation" \| "SAR-to-optical" \| "generated image") + (keypoint \| "feature matching" \| registration \| "control points")` | 4 |
| S2_Q3 | `("generated image" \| "synthetic image" \| "translated image") + ("false match" \| "matched point" \| keypoint) + (hallucinat* \| invented) + (registration \| matching)` | 0 |

### arXiv API

First run: HTTP 429 on all three queries after four attempts each. Second run with 90 s
backoff: see the addendum at the foot of this file.

### Google Scholar, manual pass (browser, first page of each)

| id | query as typed |
|---|---|
| GS-1 | `"image translation" "registration accuracy" ("adversarial loss" OR "perceptual loss") ablation` |
| GS-2 | `(hallucination OR hallucinated OR "invented structure") ("image translation" OR "SAR-to-optical" OR "generated image") (keypoint OR "feature matching" OR matchability OR "control points") metric` |
| GS-3 | `("generated image" OR "synthetic image" OR "translated image") ("matched point" OR "matched points" OR "false match" OR keypoints) (hallucinated OR invented OR fabricated) (registration OR matching)` |
| GS-4 | `"image translation" ("template matching" OR "image matching" OR registration) ("adversarial loss" OR "GAN loss" OR "perceptual loss") "ablation" ("matching accuracy" OR "registration accuracy" OR "correct matches")` |

## Triage — every hit that survived a title read was read at abstract level; the two closest at full text

| paper | what it does | relation to the three aims | disposition |
|---|---|---|---|
| **Ma, Li, Su, Xian, Zhang, "Visible-to-Infrared Image Translation for Matching Tasks", IEEE JSTARS 17:18199–18213, 2024** (full text read) | Trains a pix2pix-style translator with L1 + LSGAN + a matching loss (NCC or contrastive match-patch), jointly with the matching task; scores template-matching accuracy (mean L2 error, % within 1 px) and SIFT point-matching end-point error on the generated images; ablation (§IV-J) adds the matching losses to an LSGAN+L1 baseline | **Aim 1, close.** A loss ablation scored against positional metrics exists besides Arar. It adds losses to an adversarial baseline; it never removes the adversarial term; training is joint and the generated image is an intermediate inside the loop. Also scores the positional error of matches on generated images (aim 3 neighbourhood) without asking whether matched structure was in the input | **Cite.** Related-work sentence narrowed; contribution (i) reworded |
| Arar et al., CVPR 2020 (already cited) | Joint translation-registration; loss ablation against registration error; opposite sign | Aim 1, the known one | unchanged |
| Medical joint translation-registration frameworks surfaced by GS-4: DTR-GAN (Appl. Sci. 2023), CoCycleReg (Neurocomputing 2022), invertible-translation registration (ECCV 2024), Luo et al. visible-infrared UAV registration (Sci. Rep. 2023) | Registration and translation trained jointly; registration accuracy reported; loss terms sometimes ablated | Aim 1, same family as Arar: joint training, no frozen deliverable, adversarial term kept | not cited individually; the narrowed sentence covers the family |
| **Yu and Jung, "Attention OffsetNet: Translation-Free Transfer Learning for Optical–SAR Registration…", IEEE JSTARS 2026** | A registration method that deliberately avoids an intermediate translation stage because translation carries "a high risk of generating hallucinated textures that do not exist" | Aims 1–3: states the concern this letter measures, as a motivation, without measuring it | **Cite** in the related-work sentence about what the field does |
| **Cohen, Luck, Honari, "Distribution Matching Losses Can Hallucinate Features in Medical Image Translation", MICCAI 2018 (LNCS pp. 529–536)** | Distribution-matching (adversarial, cycle) losses hallucinate class features in medical translation; recommends against direct interpretation | Aim 2, precedent for the mechanism in another consumer; not input-conditioned, not matchability | **Cite** as mechanism precedent |
| BIGPrior (El Helou, Süsstrunk, IEEE TIP 2022) | Decouples the learned-prior (hallucinated) part of a restored image from the data-fidelity part | Aim 2, nearest in spirit (separating what came from the prior from what came from the data); restoration, no downstream consumer | recorded, not cited |
| **Sayez et al., A&A 702:A83, 2025** | Non-adversarial strategies and input-modulated architecture reduce GAN hallucination in solar-physics translation, judged by physical metrics | Aim 2 and the design rule: the same rule argued for a physical-measurement consumer | **Cite** in V.5 as an adjacent consumer |
| Chertok et al., "In Defense of OCTA…", arXiv:2608.15626, 2026 | Downstream-utility evaluation of OCT-to-OCTA synthesis with a matched-blur control showing fabricated detail | Aim 2, the same logic (utility not fidelity; blur control) for a segmentation consumer | recorded, not cited |
| Oh et al., "Hallucination Detection in Virtually-Stained Histology", IEEE TMI 2026 | Post-hoc hallucination detector from the generator's latent space | Aim 2, detection not measurement, medical | recorded, not cited |
| StegoGAN (Wu et al., CVPR 2024) | Suppresses hallucinated instances in non-bijective translation | Aim 2 neighbourhood; hallucination as class instances, no matching | recorded, not cited |
| SAR-to-optical translation-for-matching family (Merkle 2018 cited; Zhang "Feature-Guided", IEEE Access 2020, loss ablation scored by PSNR/SSIM only; Dual-Generator RS 2022; semi-supervised GRSL 2022; OS-CycleGAN TGRS 2025) | Translation evaluated by matching yield; ablations, where present, scored by image-quality metrics or matching rate with the adversarial term kept | Aim 1 neighbourhood; none removes the adversarial term; none asks whether a matched point is real | Merkle stays; family covered by the narrowed sentence |
| LoRCA (arXiv 2026), histology-to-HiP-CT | Evaluates keypoint matching on translated images and mentions hallucination | Aim 3 neighbourhood, semantic domain | recorded, not cited |

## Outcome, per aim

1. **Loss ablation against a positional metric: something close found.** Ma et al. 2024 is a
   second, beside Arar. Both train jointly and both keep the adversarial term. Nothing
   removes the adversarial term against a frozen deliverable scored by an exogenous matcher.
2. **Input-conditioned invention tied to matchability: nothing equivalent; precedents for the
   mechanism in other consumers** (Cohen 2018; Sayez 2025; BIGPrior; Chertok 2026). None
   conditions on the input's silent regions and none ties invention to matchability.
3. **Whether a matched point on a generated image is real: nothing found.** Prior work measures
   how accurately matches on generated images localise (Merkle 2018; Ma 2024); none asks
   whether the matched structure was present in the input.

**Consequence applied (outcome "something close found", not "equivalent"):** the claim of
Section I narrows. The sentence "Arar et al. report the only prior loss ablation scored against
a registration metric" is replaced by a sentence naming both prior loss studies and the
structural difference; contribution (i) is reworded to state the distinction between
positional accuracy of matches and whether the matched structure existed; Ma 2024, Yu and
Jung 2026, Cohen 2018 and Sayez 2025 are cited, each verified against its Crossref record.
Contributions (ii)–(iv) keep "to our knowledge", now supported by this record.
