# Tree cleanup, 18 September 2026 (P16) — enumeration BEFORE any removal

Every Markdown file outside `tubitak/docs/evidence/`, plus the agent-facing configuration and tool-data files, classified into exactly one of: (1) RECORD, keep and do not edit; (2) TOOLING, delete from the tree; (3) DELIVERY COPY, delete from the tree; (4) BOUNDARY, report and hold. The test for (1) is a citation by a record document (the data-availability statement, the corrections log, a registration, a results document, the standing practices, an audit) or the manuscript, not a judgement of importance. Hooks and check scripts are not candidates and stay. Git history is not rewritten; every removed file remains at the commits that carried it, and the pre-move tag `pre-move-2026-09-14` is untouched.

Candidates: 171. Classes: (1) 109, (2) 5, (3) 1, (4) 56.

| path | class | basis |
|---|---|---|
| `EVIDENCE.md` | (1) | cited by the manuscript and the corrections log |
| `README.md` | (1) | the landing page (Part C of P15); to be edited only where it names a removed file |
| `figures/README.md` | (1) | cited by EVIDENCE.md and the manuscript's figure notes |
| `manuscript/drafts/draft-section-II.md` | (1) | the manuscript's Markdown drafts, cited by the section files' comments and the README |
| `manuscript/drafts/draft-section-III.md` | (1) | the manuscript's Markdown drafts, cited by the section files' comments and the README |
| `manuscript/drafts/draft-section-IV.md` | (1) | the manuscript's Markdown drafts, cited by the section files' comments and the README |
| `notes/citations-verified-2026-09-13.md` | (1) | cited by corrections-log entries 39 and 40 |
| `notes/condensation-rule.md` | (1) | cited by standing-practices (P13 cross-reference) |
| `notes/figure-renumbering-2026-09-13.md` | (1) | cited by letter-skeleton.md's numbering note and by figures/README.md |
| `notes/move-2026-09-14.md` | (1) | the move note, named in the brief as record |
| `notes/protected-phrases.txt` | (1) | input of the prose-pass check named in the prose-pass note; tool data, stays with the checks |
| `notes/section-V-recost-2026-09-13.md` | (1) | cited by the absence-claims and presence-claims audits |
| `notes/submission-checklist.md` | (1) | cited by the absence-claims audit; holds the two open items (author line, addressee) |
| `notes/terms.txt` | (1) | input of the term check named in the submission checklist; tool data, stays with the checks |
| `tubitak/README.md` | (1) | the delivery's tubitak README with the P8 dated note; cited by the presence-claims audit |
| `tubitak/docs/B2-B3-audit.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/E3-session-log-excerpt.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/T1-audit.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/T1-benchmark-results.md` | (1) | results document |
| `tubitak/docs/T3-reliability-results.md` | (1) | results document |
| `tubitak/docs/absence-claims-audit-2026-09-13.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/ankara-acquisition.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/arm-common-support-results.md` | (1) | results document |
| `tubitak/docs/budget-reconciliation.md` | (1) | plan-era document, but the absence-claims audit cites it at lines 127 and 130 |
| `tubitak/docs/common-support-registration.md` | (1) | registration |
| `tubitak/docs/common-support-results.md` | (1) | results document |
| `tubitak/docs/confidence-registration-2.md` | (1) | registration |
| `tubitak/docs/confidence-registration-3.md` | (1) | registration |
| `tubitak/docs/confidence-registration.md` | (1) | registration |
| `tubitak/docs/confidence-results.md` | (1) | results document |
| `tubitak/docs/confidence-transfer-results.md` | (1) | results document |
| `tubitak/docs/corrections-entry-35-draft.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/corrections-log.md` | (1) | corrections log |
| `tubitak/docs/data-sources.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/delivery-registrations.md` | (1) | registration |
| `tubitak/docs/epoch-curve-registration.md` | (1) | registration |
| `tubitak/docs/epoch-curve-results.md` | (1) | results document |
| `tubitak/docs/final-report-skeleton.md` | (1) | plan-era document, but seed-block-results.md cites it at line 59 and the absence-claims audit at line 48 |
| `tubitak/docs/gates/seed-block-morning-report.md` | (1) | cited by seed-block-results.md at three places |
| `tubitak/docs/gcp-veto-rule-results.md` | (1) | results document |
| `tubitak/docs/geometry-finding.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/hallucinated-structure.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/hardware-gate-results.md` | (1) | results document |
| `tubitak/docs/headline-registrations.md` | (1) | registration |
| `tubitak/docs/headline-results.md` | (1) | results document |
| `tubitak/docs/informative-mask-registration.md` | (1) | registration |
| `tubitak/docs/informative-mask-results.md` | (1) | results document |
| `tubitak/docs/karios-validation.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/letter-skeleton.md` | (1) | cited by corrections-log entries 31 and 39 and by the manuscript's section comments |
| `tubitak/docs/lr-confound-registration.md` | (1) | registration |
| `tubitak/docs/lr-confound-results.md` | (1) | results document |
| `tubitak/docs/novelty-search-2026-09-13.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/odtu-package-README.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/open-items.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/osm-palette.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/osm-render-baseline-registration.md` | (1) | registration |
| `tubitak/docs/osm-render-baseline-results.md` | (1) | results document |
| `tubitak/docs/packageA-audit.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/packageA-registration.md` | (1) | registration |
| `tubitak/docs/packageA-results.md` | (1) | results document |
| `tubitak/docs/paper-context-addendum.md` | (1) | cited by corrections-log entry 51 and by registrations |
| `tubitak/docs/paper-roadmap.md` | (1) | cited by corrections-log entry 23 and the manuscript |
| `tubitak/docs/phase-c-audit.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/phase-c-config.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/phase-c-europe-registration.md` | (1) | registration |
| `tubitak/docs/phase-c-europe-results.md` | (1) | results document |
| `tubitak/docs/phase-c-lpips-registration.md` | (1) | registration |
| `tubitak/docs/phase-c-lpips-results.md` | (1) | results document |
| `tubitak/docs/phase-c-registration.md` | (1) | registration |
| `tubitak/docs/phase-c-results.md` | (1) | results document |
| `tubitak/docs/phase-c3-results.md` | (1) | results document |
| `tubitak/docs/phase-cd-preparation.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/phase-d-audit.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/phase-d-checks-registration.md` | (1) | registration |
| `tubitak/docs/phase-d-closeout.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/phase-d-ratio-addendum.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/phase-d-regeneration-STOP.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/phase-d-results.md` | (1) | results document |
| `tubitak/docs/phase-f-backlog.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/plugin-field-test.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/plugin-gate-registration-C.md` | (1) | registration |
| `tubitak/docs/plugin-gate-registration-C2.md` | (1) | registration |
| `tubitak/docs/plugin-gate-registrations.md` | (1) | registration |
| `tubitak/docs/plugin-results.md` | (1) | results document |
| `tubitak/docs/positioning-registrations.md` | (1) | registration |
| `tubitak/docs/positioning-results.md` | (1) | results document |
| `tubitak/docs/presence-claims-audit-2026-09-13.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/published-paper-audit.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/related-work.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/renderer-tolerance.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/seam-registration.md` | (1) | registration |
| `tubitak/docs/seam-results.md` | (1) | results document |
| `tubitak/docs/seed-block-results.md` | (1) | results document |
| `tubitak/docs/seed-replication-registration.md` | (1) | registration |
| `tubitak/docs/standing-practices.md` | (1) | standing practices |
| `tubitak/docs/sustained-trend-registration.md` | (1) | registration |
| `tubitak/docs/sustained-trend-results.md` | (1) | results document |
| `tubitak/docs/tool-gate-registration-2.md` | (1) | registration |
| `tubitak/docs/tool-gate-registration.md` | (1) | registration |
| `tubitak/docs/tool-registration-4.md` | (1) | registration |
| `tubitak/docs/tool-registrations-3.md` | (1) | registration |
| `tubitak/docs/tool-results.md` | (1) | results document |
| `tubitak/docs/train-test-scale-mismatch.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/turkey-prediction.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/turkey-results.md` | (1) | results document |
| `tubitak/docs/verifier-degenerate-audit.md` | (1) | audit or record document cited by the corrections log, a registration, a results document or the absence-claims audit |
| `tubitak/docs/warmup-deconfound-registration.md` | (1) | registration |
| `tubitak/docs/warmup-deconfound-results.md` | (1) | results document |
| `tubitak/modal/patches/README.md` | (1) | documents the sorted-image-folder training patch the hardware gate records |
| `.replit` | (2) | IDE/agent run configuration from the upstream fork, uncited |
| `CLAUDE-gencp-validation.md` | (2) | the delivery's agent instruction file, preserved at the P15 merge; lives at gencp-validation and in history (last in this tree at 463f7db); the move note's 'preserved as' sentence stays as written |
| `CLAUDE.md` | (2) | agent instruction file for this repository (named in the P16 brief); the move note's sentence 'rewritten in CLAUDE.md here' will point at commit ac634e9 |
| `MAINTAINERS.md` | (2) | the delivery's maintainer rule for the three repositories, written for maintainers and agents; uncited by any record document; lives at gencp-validation and in history |
| `claude/oturum-devri.md` | (2) | session handover note of 25 August 2026 (Turkish), uncited |
| `README-gencp-validation.md` | (3) | the delivery's root README, preserved at the P15 merge; lives at gencp-validation and in history (last in this tree at 463f7db); the move note's 'preserved as' sentence stays as written |
| `SNAPSHOT.md` | (4) | a handover snapshot by name-class (2), but the absence-claims audit cites it at lines 21 and 66 as the source of two absence claims it checked; the rule does not settle it |
| `docs/README_es.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `docs/datasets.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `docs/docker.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `docs/dogrulama-calismasi.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `docs/overview.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `docs/plugin/QUICKSTART.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `docs/proje1-eklenti.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `docs/proje2-eklenti.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `docs/qa.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `docs/tips.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `notes/number-audit-2026-09-14.md` | (4) | the P10 number audit; cited by README.md and, by description rather than name ('P10 audit (c) 1'), by corrections-log entries 51-53; the rule's citation test is by name |
| `notes/prose-pass-2026-09-14.md` | (4) | the P12 record of the prose pass; cited by nothing (the P13 reconciliation was appended to it and to the number audit) |
| `notes/style-corpus-2026-09-14.md` | (4) | the P12 corpus manifest; cited only by the prose-pass note |
| `tubitak/DEVIR.md` | (4) | the delivery's 504-line handover guide for the institution; cited by tubitak/README.md ('start from the handover guide'); a delivered document rather than a session snapshot, but not cited by any record document |
| `tubitak/demo/DEMO.md` | (4) | the delivery's QGIS demo note; cited only by terimler.md |
| `tubitak/docs/gates/seed-block-wave-launch.md` | (4) | launch record of the six-seed block (task ids, times); cited by nothing, but it is an operational record of a run the letter rests on |
| `tubitak/docs/terimler.md` | (4) | Turkish glossary for the delivery's plugin documents, inside the record directory, cited by nothing |
| `tubitak/makale-context.md` | (4) | 'Paper handoff context: what an agent working on the manuscript needs to know' — an agent instruction file by content, but the absence-claims audit names it in its scope line; the rule does not settle whether a scope listing is a citation |
| `tubitak/qgis_plugin/QUICKSTART.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/qgis_plugin/README.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/rapor2/GenCP_Ilerleme_Raporu_2.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/rapor3/GenCP_Rapor_Sonuc.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/SOURCE.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/00-recon.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/01-wp1.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/02a-reflectance-corpus.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/02b-demo-tik-sirasi.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/02b-plugin.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/03a-corpus-registration.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/03a-wald-corpus.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/03b-registration.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/03b-training.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/04-model-in-plugin.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/05-referans-arac.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/06-wsx4-eklentide.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/07-x4-model.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/07-x4-registration.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/08-eslestirme.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/09-devir.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/09-release-notes-draft.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/10-kurulum.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/11-eox.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/11-zamanlama.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/12-qt5-uyumluluk.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/12-tci-model.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/13-cevrimdisi-kurulum.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/13-tci-model-v2.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/15-kontroller.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/16-checkpoint.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/17-wsx4-hizalama.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/18-depo-tasima.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/19-proje1-fark-olcumu.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/20-komut-satiri.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/gate-s-registration.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |
| `tubitak/sr/docs/sozluk.md` | (4) | the delivery's own documentation at its original path (plugin, Project 2, reports); not a preserved copy, not tooling, not cited by the record; the P15 README says these are carried with the history, so removing them is a separate decision |

## Refined test and rulings, 18 September 2026 (P17)

**The test, refined so the classification is reproducible.** A citation makes a file RECORD when the record depends on the file's content: it is the source of a claim, the evidence for a check, or the target of a line-number reference. A scope line that says "this file was searched" does not. Primary experimental logs in `tubitak/docs/` (launch records, gate tokens, run logs) are record by kind even when nothing cites them; notes and audits are record only by citation.

**Rulings on the 56 boundary files.**

| file(s) | ruling | basis |
|---|---|---|
| `SNAPSHOT.md` | keep, unedited (appended amendment only) | cited by the absence-claims audit at lines 21 and 66 as the source of claims it checked |
| `tubitak/docs/gates/seed-block-wave-launch.md` | keep | launch record of the six-seed block: record by kind |
| `notes/number-audit-2026-09-14.md` | keep | cited by the README; source of corrections entries 51–53 |
| `tubitak/DEVIR.md` | deleted | cited only by the delivery's `tubitak/README.md` (rewritten) and the absence audit's scope line |
| `tubitak/makale-context.md` | deleted | agent instruction file by content; its only mention is the absence audit's scope line |
| `tubitak/docs/terimler.md`, `tubitak/demo/DEMO.md` | deleted | delivery glossary and demo, cited only by each other |
| `notes/prose-pass-2026-09-14.md`, `notes/style-corpus-2026-09-14.md` | deleted | cited by nothing in the record; process scaffolding; last at `fff6c4e` |
| `docs/dogrulama-calismasi.md`, `docs/proje1-eklenti.md`, `docs/proje2-eklenti.md` | deleted | the delivery's front-page documents |
| `docs/README_es.md`, `docs/datasets.md`, `docs/docker.md`, `docs/overview.md`, `docs/qa.md`, `docs/tips.md` | **not deleted** | these six are the upstream pix2pix fork's own documentation, not delivery documentation; the P15 A.6 rule against pruning upstream directories applies, and `train.py`/`test.py` point readers at them |
| `docs/plugin/QUICKSTART.md`, `tubitak/qgis_plugin/QUICKSTART.md` | **not deleted** | `tubitak/docs/plugin-field-test.md` (a results document) says at lines 92 and 290 that user-facing behaviour "is recorded in QUICKSTART.md": a content dependency the P16 enumeration missed |
| `tubitak/qgis_plugin/README.md` | deleted | plugin README; every apparent citation was the substring `README.md` |
| `tubitak/sr/docs/*.md` (32) | deleted | Project 2's delivery documentation; four of them are Project 2 registrations, which belong to the delivery and not to the letter's record; all at `gencp-validation` and in history |
| `tubitak/rapor2/GenCP_Ilerleme_Raporu_2.md`, `tubitak/rapor3/GenCP_Rapor_Sonuc.md` | deleted | the two Turkish reports |
| `tubitak/sr/SOURCE.md`, `tubitak/sr/docs/evidence/*`, `docs/Dockerfile`, `docs/kapak.png`, `docs/plugin/*.png` | not in scope | code provenance, Project 2 evidence, upstream Dockerfile and images: not documentation files of the enumeration; left for a later ruling if one is wanted |

Consequential edits (C): `tubitak/README.md` replaced by a short English README (not record); dated amendments appended, and nothing else changed, to `notes/move-2026-09-14.md`, `SNAPSHOT.md` and `tubitak/docs/presence-claims-audit-2026-09-13.md`, the three record documents whose sentences named a removed file.
