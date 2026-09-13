# Bibliography verification — 13 September 2026

Every entry in `manuscript/refs.bib` was checked by script against its authoritative record: Crossref for DOIs, DataCite for the Zenodo DOI, arXiv and the NeurIPS proceedings pages for the two NeurIPS papers. Nothing was marked verified from memory or from the study repository's own documents.

Trigger: the supervising session found "Chen, Ohayon et al." cited for arXiv:2405.16475, a paper by Cohen, Kligvasser, Rivlin and Freedman (corrections-log entry 39). One of six related-work citations wrong is a base rate that does not permit trusting the other five.

| Key | Status | Record |
|---|---|---|
| `guasch2026gencp` | **VERIFIED** | Crossref 10.3390/rs18142356: Elodie Guasch, Ilyas Yalcin, Sebastien Saunier, Leonardo de Laurentiis, Philippe Goryl, Sultan Kocaman; Remote Sensing 18(14):2356; published 2026-07-15. Matches the supervising session's record verbatim; entry expanded from initials to full names |
| `blau2018perception` | **VERIFIED** | Crossref 10.1109/CVPR.2018.00652: Yochai Blau, Tomer Michaeli; 2018 IEEE/CVF CVPR, pp. 6228–6237 |
| `liu2019classification` | **VERIFIED** | arXiv 1904.08816 and NeurIPS 2019 proceedings (papers.nips.cc, hash 6c29793a…): Dong Liu, Haochen Zhang, Zhiwei Xiong; title casing 'On The Classification-Distortion-Perception Tradeoff' as in both records; booktitle now names the volume |
| `arar2020unsupervised` | **CORRECTED** | Crossref 10.1109/CVPR42600.2020.01342: Moab Arar, Yiftach Ginger, Dov Danon, Amit H. Bermano, Daniel Cohen-Or; 2020 IEEE/CVF CVPR, pp. 13407–13416. Authors and title were right; pages and DOI were missing, added |
| `cohen2024looks (was chen2024looks)` | **CORRECTED** | arXiv 2405.16475 and NeurIPS 2024 proceedings (hash 2847d43f…): Regev Cohen, Idan Kligvasser, Ehud Rivlin, Daniel Freedman; title exact. The entry named 'Chen, Regev Cohen and Ohayon, Guy and others': no such authors. Corrections-log entry 39 |
| `fuentesreyes2019sar` | **CORRECTED** | Crossref 10.3390/rs11172067: Mario Fuentes Reyes, Stefan Auer, Nina Merkle, Corentin Henry, Michael Schmitt; Remote Sensing 11(17):2067, 2019. Title punctuation: the record has an em dash before 'Optimization', not a colon; changed |
| `merkle2018exploring` | **CORRECTED (diacritic)** | Crossref 10.1109/JSTARS.2018.2803212: Nina Merkle, Stefan Auer, Rupert Muller, Peter Reinartz; IEEE JSTARS 11(6):1811–1820, 2018. Crossref strips the umlaut. Second and third sources, 13 Sep: Semantic Scholar's record gives 'Rupert Müller', and the author-deposited open-access PDF (DLR elib 118413, final version) prints 'R. Müller' on its first page. Entry carries Müller |
| `saunier2024karios` | **CORRECTED** | DataCite 10.5281/zenodo.10598329: Saunier Sébastien, Canonicy Patrice, Louis Jérôme, Debaecker Vincent, Albinet Clément; Zenodo, version 1.0, 2024; title 'KARIOS : A fast & efficient open source tool for geometric deformation analysis'. The entry had 'Canonicy, Jérôme', a first name supplied from memory, wrong. Corrections-log entry 40 |
| `pan2013bias` | **VERIFIED** | Crossref 10.1016/j.optlaseng.2013.04.009: Bing Pan; Optics and Lasers in Engineering 51(10):1161–1167, 2013 |
| `isola2017image` | **CORRECTED** | Crossref 10.1109/CVPR.2017.632: Isola, Zhu, Zhou, Efros; 2017 IEEE CVPR, pp. 5967–5976. Pages and DOI added |
| `zhu2017unpaired` | **CORRECTED** | Crossref 10.1109/ICCV.2017.244: Zhu, Park, Isola, Efros; 2017 IEEE ICCV, pp. 2242–2251. Pages and DOI added; title casing matched to the record |
| `zhang2018lpips` | **CORRECTED** | Crossref 10.1109/CVPR.2018.00068: Zhang, Isola, Efros, Shechtman, Wang; 2018 IEEE/CVF CVPR, pp. 586–595. Pages and DOI added |

Summary: 4 verified as written, 8 corrected: 2 wrong author lists (entries 39 and 40), 1 title punctuation, 3 with pages and DOI missing, 1 expanded from initials.

Rule adopted (README working rule 6): no bibliography entry is cited until it has a row here naming the record it was checked against.
