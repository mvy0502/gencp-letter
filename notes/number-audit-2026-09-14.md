# Number audit, 14 September 2026 (P10 A) — enumeration BEFORE checking

Every numeric token in the seven section files at gencp-letter `09a7aa1`, with spelled-out numerals, captured by script (regex over the sources with comment lines and `\ref`/`\cite`/`\label` arguments removed) and listed with its source line and context. Equation numbers and figure/table numbers produced by LaTeX are not tokens in the source and are not listed; the bibliography is not in the A.1 list and was verified against publisher records in P1 (`citations-verified-2026-09-13.md`). Classification and tracing are appended below this table AFTER this enumeration was committed; nothing in the manuscript is changed by this audit.

**597 tokens.**

| # | where | token | context |
|---|---|---|---|
| 1 | `00-abstract.tex:39` | `2` | …GAN renders a Sentinel-2-like image from OpenStreetMap and land cover. A… |
| 2 | `00-abstract.tex:40` | `$2` | …$2\times2$ factorial crosses an adversarial term with the… |
| 3 | `00-abstract.tex:42` | `2` | …itional error of feature matches against real Sentinel-2 over 130 chips. Removing the… |
| 4 | `00-abstract.tex:42` | `130` | …error of feature matches against real Sentinel-2 over 130 chips. Removing the… |
| 5 | `00-abstract.tex:43` | `six` | …s positional accuracy under the perceptual loss in all six… |
| 6 | `00-abstract.tex:44` | `1/64` | …confirmatory training seeds ($P = 1/64$, direction fixed in advance), and under L1 as well;… |
| 7 | `00-abstract.tex:46` | `six` | …penalty in all six seeds. An input-conditioned measurement supplies the n… |
| 8 | `01-introduction.tex:36` | `2` | …nces were proposed to sidestep that: render a Sentinel-2-like image… |
| 9 | `01-introduction.tex:44` | `2` | …renders a Sentinel-2-like image from OpenStreetMap vectors and a… |
| 10 | `01-introduction.tex:45` | `10` | …land-cover raster. Its published objective for the 10~m model is adversarial +… |
| 11 | `01-introduction.tex:46` | `100` | …$\lambda\cdot$LPIPS  with $\lambda = 100$ and a binary… |
| 12 | `01-introduction.tex:48` | `two` | …prove performance, and gives no comparison between the two and no ablation of the… |
| 13 | `01-introduction.tex:51` | `Two` | …Two sentences of scope. At 10~m the premise for a generate… |
| 14 | `01-introduction.tex:51` | `10` | …Two sentences of scope. At 10~m the premise for a generated reference does not bind:… |
| 15 | `01-introduction.tex:52` | `24` | …24 stratified Turkish extents, none lacked a usable Senti… |
| 16 | `01-introduction.tex:52` | `2` | …atified Turkish extents, none lacked a usable Sentinel-2 scene within a year, and the… |
| 17 | `01-introduction.tex:53` | `two` | …median extent had a cloud-free scene from two days before, the worst from seventeen.\footnote{Scene-… |
| 18 | `01-introduction.tex:53` | `seventeen` | …cloud-free scene from two days before, the worst from seventeen.\footnote{Scene-per-year… |
| 19 | `01-introduction.tex:54` | `100` | …ts are lower bounds, since the archive query capped at 100 and every extent hit the… |
| 20 | `01-introduction.tex:56` | `five` | …Nor does currency help: on a rapidly built-up site, a five-year-old… |
| 21 | `01-introduction.tex:57` | `2026` | …real scene registered a 2026 target as well on the tiles that changed most as on th… |
| 22 | `01-introduction.tex:59` | `+0.008` | …current OpenStreetMap was absent, $+0.008 \pm 0.031$~px.\footnote{This null is equally… |
| 23 | `01-introduction.tex:59` | `0.031` | …current OpenStreetMap was absent, $+0.008 \pm 0.031$~px.\footnote{This null is equally… |
| 24 | `01-introduction.tex:73` | `one` | …semantic one with an error rate, where a hallucinated texture that… |
| 25 | `01-introduction.tex:75` | `Two` | …of something that does not exist. Two prior loss studies are scored against a positional met… |
| 26 | `01-introduction.tex:88` | `2019` | …in 2019 and wrote that no suitable metric existed to evaluate… |
| 27 | `01-introduction.tex:96` | `$2` | …The contributions, each to our knowledge new: (i) a $2\times2$ factorial that isolates… |
| 28 | `02-methods.tex:42` | `10` | …pixels at 10~m ground sampling; lower is better.… |
| 29 | `02-methods.tex:46` | `2` | …e a published conditional GAN  that renders a Sentinel-2-like image from… |
| 30 | `02-methods.tex:47` | `256` | …OpenStreetMap vectors and land-cover raster: a U-Net-256 generator (54.414~M parameters)… |
| 31 | `02-methods.tex:47` | `54.414` | …vectors and land-cover raster: a U-Net-256 generator (54.414~M parameters)… |
| 32 | `02-methods.tex:49` | `5,577` | …Training used 5,577 Turkish image pairs and 20 epochs per arm, under the g… |
| 33 | `02-methods.tex:49` | `20` | …Training used 5,577 Turkish image pairs and 20 epochs per arm, under the generator's own… |
| 34 | `02-methods.tex:50` | `ten` | …linear schedule---ten epochs at the base learning rate followed by ten decay… |
| 35 | `02-methods.tex:50` | `ten` | …ule---ten epochs at the base learning rate followed by ten decaying to zero.… |
| 36 | `02-methods.tex:52` | `six` | …The factorial was trained in full at six independent seeds (45--50) on one platform, one… |
| 37 | `02-methods.tex:52` | `45--50` | …actorial was trained in full at six independent seeds (45--50) on one platform, one… |
| 38 | `02-methods.tex:52` | `one` | …s trained in full at six independent seeds (45--50) on one platform, one… |
| 39 | `02-methods.tex:52` | `one` | …ull at six independent seeds (45--50) on one platform, one… |
| 40 | `02-methods.tex:53` | `0` | …A10G GPU per run; that block is the confirmatory evidence… |
| 41 | `02-methods.tex:54` | `42` | …receded by the run that generated the hypothesis (seed 42) and by a… |
| 42 | `02-methods.tex:55` | `two` | …two-seed block (seeds 43 and 44), both on a different plat… |
| 43 | `02-methods.tex:55` | `43` | …two-seed block (seeds 43 and 44), both on a different platform, one T4 GPU per… |
| 44 | `02-methods.tex:55` | `44` | …two-seed block (seeds 43 and 44), both on a different platform, one T4 GPU per run. Be… |
| 45 | `02-methods.tex:55` | `one` | …block (seeds 43 and 44), both on a different platform, one T4 GPU per run. Before… |
| 46 | `02-methods.tex:56` | `six` | …the six-seed block was launched, seed 43 was re-trained on the… |
| 47 | `02-methods.tex:56` | `43` | …the six-seed block was launched, seed 43 was re-trained on the first platform and the two… |
| 48 | `02-methods.tex:56` | `two` | …, seed 43 was re-trained on the first platform and the two… |
| 49 | `02-methods.tex:58` | `one` | …\emph{not pooled}: one of eleven registered quantities, the edge ratio of the… |
| 50 | `02-methods.tex:58` | `eleven` | …\emph{not pooled}: one of eleven registered quantities, the edge ratio of the adversari… |
| 51 | `02-methods.tex:59` | `two` | …ss platforms by more than its seed-to-seed spread. The two platforms… |
| 52 | `02-methods.tex:61` | `six` | …pooled statistic appears anywhere in this letter. The six-seed block carries the… |
| 53 | `02-methods.tex:62` | `two` | …inference; the two-seed block is reported for consistency only.… |
| 54 | `02-methods.tex:64` | `two` | …The arms carrying an adversarial term also carry a two-epoch warm-up at $2\times10^{-5}$… |
| 55 | `02-methods.tex:64` | `$2\times10^{-5}` | …an adversarial term also carry a two-epoch warm-up at $2\times10^{-5}$… |
| 56 | `02-methods.tex:65` | `eighteen` | …before eighteen main epochs at $10^{-4}$; the arms without one run twe… |
| 57 | `02-methods.tex:65` | `$10^{-4}` | …before eighteen main epochs at $10^{-4}$; the arms without one run twenty main epochs at… |
| 58 | `02-methods.tex:65` | `one` | …re eighteen main epochs at $10^{-4}$; the arms without one run twenty main epochs at… |
| 59 | `02-methods.tex:65` | `twenty` | …een main epochs at $10^{-4}$; the arms without one run twenty main epochs at… |
| 60 | `02-methods.tex:66` | `$10^{-4}` | …$10^{-4}$. Integrated over training this gives the adversarial… |
| 61 | `02-methods.tex:66` | `13.40` | …tegrated over training this gives the adversarial arms 13.40 against… |
| 62 | `02-methods.tex:67` | `15.00` | …15.00 in units of $10^{-4}$ epochs, a 10.67\% deficit, borne… |
| 63 | `02-methods.tex:67` | `$10^{-4}` | …15.00 in units of $10^{-4}$ epochs, a 10.67\% deficit, borne by the arms that sco… |
| 64 | `02-methods.tex:67` | `10.67\%` | …15.00 in units of $10^{-4}$ epochs, a 10.67\% deficit, borne by the arms that score… |
| 65 | `02-methods.tex:74` | `+0.007` | …$+0.007 \pm 0.034$~px, roughly 1\% of the 0.647~px gap the sch… |
| 66 | `02-methods.tex:74` | `0.034` | …$+0.007 \pm 0.034$~px, roughly 1\% of the 0.647~px gap the schedule woul… |
| 67 | `02-methods.tex:74` | `1\%` | …$+0.007 \pm 0.034$~px, roughly 1\% of the 0.647~px gap the schedule would have to explain… |
| 68 | `02-methods.tex:74` | `0.647` | …$+0.007 \pm 0.034$~px, roughly 1\% of the 0.647~px gap the schedule would have to explain… |
| 69 | `02-methods.tex:75` | `one` | …(one seed, chip-level bound). The LPIPS-only versus L1-only… |
| 70 | `02-methods.tex:76` | `twenty` | …it by construction, both arms being un-warmed twenty-epoch arms at identical integrated… |
| 71 | `02-methods.tex:84` | `$2` | …\caption{The $2\times2$ loss factorial and the fifth arm. Rows: the re… |
| 72 | `02-methods.tex:89` | `three` | …three seed-level contrasts of Section~III-B, each drawn from… |
| 73 | `02-methods.tex:95` | `$2` | …A $2\times2$ factorial (Fig.~) crosses an adversarial term… |
| 74 | `02-methods.tex:97` | `four` | …all four cells within each replicate: training data, seed, init… |
| 75 | `02-methods.tex:98` | `six` | …and matcher configuration; the seed varies across the six replicates and… |
| 76 | `02-methods.tex:99` | `one` | …never within one. The learning-rate schedule is an explicit exception t… |
| 77 | `02-methods.tex:106` | `100` | …+ $\lambda\cdot$LPIPS with $\lambda = 100$ and a binary cross-entropy… |
| 78 | `02-methods.tex:116` | `one` | …training setup and we state it as one.… |
| 79 | `02-methods.tex:120` | `2,` | …siduals are KLT feature matches  against real Sentinel-2, at a confidence threshold of… |
| 80 | `02-methods.tex:121` | `0.8` | …0.8, over 130 Ankara chips, each a $228\times228$-pixel wi… |
| 81 | `02-methods.tex:121` | `130` | …0.8, over 130 Ankara chips, each a $228\times228$-pixel window at 10… |
| 82 | `02-methods.tex:121` | `$228` | …0.8, over 130 Ankara chips, each a $228\times228$-pixel window at 10~m, stratified into five… |
| 83 | `02-methods.tex:121` | `28` | …0.8, over 130 Ankara chips, each a $228\times228$-pixel window at 10~m, stratified into five… |
| 84 | `02-methods.tex:121` | `10` | …30 Ankara chips, each a $228\times228$-pixel window at 10~m, stratified into five… |
| 85 | `02-methods.tex:121` | `five` | …a $228\times228$-pixel window at 10~m, stratified into five… |
| 86 | `02-methods.tex:123` | `three` | …als of Table~I and of Section~III-L are KLT run on the three-band warped… |
| 87 | `02-methods.tex:124` | `601` | …; the invention measurement of II-E and Fig.~ use a BT.601 gray conversion; the… |
| 88 | `02-methods.tex:125` | `601` | …production-path figure of Section~V-A is KLT on the BT.601 gray band. Test-time dropout is… |
| 89 | `02-methods.tex:127` | `15` | …measured to be score-neutral within $\pm0.15$~px on 30 chips and the earlier arms; the… |
| 90 | `02-methods.tex:127` | `30` | …measured to be score-neutral within $\pm0.15$~px on 30 chips and the earlier arms; the… |
| 91 | `02-methods.tex:131` | `six` | …y: median surviving points per chip, averaged over the six seeds, are 51 for the… |
| 92 | `02-methods.tex:131` | `51` | …ving points per chip, averaged over the six seeds, are 51 for the… |
| 93 | `02-methods.tex:132` | `62` | …pretrained generator, 62 for adversarial + L1, 60 for adversarial + LPIPS, 75 f… |
| 94 | `02-methods.tex:132` | `60` | …pretrained generator, 62 for adversarial + L1, 60 for adversarial + LPIPS, 75 for L1 alone… |
| 95 | `02-methods.tex:132` | `75` | …, 62 for adversarial + L1, 60 for adversarial + LPIPS, 75 for L1 alone… |
| 96 | `02-methods.tex:133` | `87` | …and 87 for LPIPS alone (Table~I). This is selection… |
| 97 | `02-methods.tex:138` | `38\%` | …that chip; the LPIPS-only arm surrenders 38\% of its points and the adversarial-plus-LPIPS… |
| 98 | `02-methods.tex:139` | `7\%` | …arm 7\%. A minimum-match-count sweep over all four arms jointl… |
| 99 | `02-methods.tex:139` | `four` | …arm 7\%. A minimum-match-count sweep over all four arms jointly is reported alongside it.… |
| 100 | `02-methods.tex:144` | `two` | …rated image, so the arms share no point identity: at a two-pixel tolerance, 69 of 130… |
| 101 | `02-methods.tex:144` | `69` | …rms share no point identity: at a two-pixel tolerance, 69 of 130… |
| 102 | `02-methods.tex:144` | `130` | …are no point identity: at a two-pixel tolerance, 69 of 130… |
| 103 | `02-methods.tex:145` | `one` | …chips have no common points at all (counted at one seed before any contrast was computed), and a toleranc… |
| 104 | `02-methods.tex:146` | `1.4--2.0` | …exceed the 1.4--2.0~px residuals under test and absorb the signal. Equal-c… |
| 105 | `02-methods.tex:152` | `130` | …er its own matches, on chip $i$ in seed $s$, with $N = 130$ chips and $S = 6$… |
| 106 | `02-methods.tex:152` | `6` | …on chip $i$ in seed $s$, with $N = 130$ chips and $S = 6$… |
| 107 | `02-methods.tex:153` | `one` | …seeds. A contrast between arms $a$ and $b$ is one number per seed, the mean of the… |
| 108 | `02-methods.tex:157` | `1` | …\Delta_s &= \frac{1}{N}\sum_{i=1}^{N}\bigl(m_{a,s,i} - m_{b,s,i}\bigr), \\… |
| 109 | `02-methods.tex:158` | `5` | …\mathrm{CI}_{95} &= \bar{\Delta} \pm t_{0.975,\,S-1}\,\frac{\hat{\sigm… |
| 110 | `02-methods.tex:158` | `975,\,` | …\mathrm{CI}_{95} &= \bar{\Delta} \pm t_{0.975,\,S-1}\,\frac{\hat{\sigma}_\Delta}{\sqrt{S}},… |
| 111 | `02-methods.tex:158` | `1` | …\mathrm{CI}_{95} &= \bar{\Delta} \pm t_{0.975,\,S-1}\,\frac{\hat{\sigma}_\Delta}{\sqrt{S}},… |
| 112 | `02-methods.tex:159` | `2` | …\quad \hat{\sigma}_\Delta^2 = \frac{1}{S-1}\sum_{s=1}^{S}\bigl(\Delta_s - \bar{\De… |
| 113 | `02-methods.tex:159` | `1` | …\quad \hat{\sigma}_\Delta^2 = \frac{1}{S-1}\sum_{s=1}^{S}\bigl(\Delta_s - \bar{\Delta}\bigr)^2.… |
| 114 | `02-methods.tex:159` | `1` | …\quad \hat{\sigma}_\Delta^2 = \frac{1}{S-1}\sum_{s=1}^{S}\bigl(\Delta_s - \bar{\Delta}\bigr)^2.… |
| 115 | `02-methods.tex:159` | `2` | …{S-1}\sum_{s=1}^{S}\bigl(\Delta_s - \bar{\Delta}\bigr)^2.… |
| 116 | `02-methods.tex:163` | `2` | …$P = 2^{-S} = 1/64$ under a null of no effect and the directi… |
| 117 | `02-methods.tex:163` | `1/64` | …$P = 2^{-S} = 1/64$ under a null of no effect and the direction fixed in… |
| 118 | `02-methods.tex:165` | `one` | …so a standard error taken across the $N$ chips within one… |
| 119 | `02-methods.tex:166` | `one` | …seed measures how consistently one checkpoint beats another, not how consistently the… |
| 120 | `02-methods.tex:171` | `8` | …input render, warped to the chip grid and converted to 8-bit BT.601 gray,… |
| 121 | `02-methods.tex:171` | `601` | …der, warped to the chip grid and converted to 8-bit BT.601 gray,… |
| 122 | `02-methods.tex:173` | `2` | …$G(X) = \sqrt{S_x^2 + S_y^2}$ the gradient magnitude of $X$ under the $3\t… |
| 123 | `02-methods.tex:173` | `2` | …$G(X) = \sqrt{S_x^2 + S_y^2}$ the gradient magnitude of $X$ under the $3\times3$ S… |
| 124 | `02-methods.tex:173` | `$3` | …_x^2 + S_y^2}$ the gradient magnitude of $X$ under the $3\times3$ Sobel… |
| 125 | `02-methods.tex:175` | `20` | …$\Omega = \{p : G(I)(p) \le \tau\}$ with $\tau = 20$ on the 8-bit scale, and the chip's… |
| 126 | `02-methods.tex:175` | `8` | …ga = \{p : G(I)(p) \le \tau\}$ with $\tau = 20$ on the 8-bit scale, and the chip's… |
| 127 | `02-methods.tex:183` | `130` | …on none of the 130. Table~ reports the mean of $r_a$ over chips, then ove… |
| 128 | `02-methods.tex:192` | `$257` | …Resampling $257\times257$ rasters at 10~m to $256\times256$ while copy… |
| 129 | `02-methods.tex:192` | `57` | …Resampling $257\times257$ rasters at 10~m to $256\times256$ while copying the t… |
| 130 | `02-methods.tex:192` | `10` | …Resampling $257\times257$ rasters at 10~m to $256\times256$ while copying the transform… |
| 131 | `02-methods.tex:192` | `$256` | …Resampling $257\times257$ rasters at 10~m to $256\times256$ while copying the transform… |
| 132 | `02-methods.tex:192` | `56` | …esampling $257\times257$ rasters at 10~m to $256\times256$ while copying the transform… |
| 133 | `02-methods.tex:193` | `10.0390625` | …unchanged gives a true ground sampling distance of 10.0390625~m against a declared 10.0~m,… |
| 134 | `02-methods.tex:193` | `10.0` | …d sampling distance of 10.0390625~m against a declared 10.0~m,… |
| 135 | `02-methods.tex:194` | `$1/256` | …an error of exactly $1/256$, zero at the north-west corner and reaching 14.1~m at… |
| 136 | `02-methods.tex:194` | `14.1` | …ly $1/256$, zero at the north-west corner and reaching 14.1~m at the… |
| 137 | `02-methods.tex:198` | `2.89` | …blished means, but the predicted standard deviation is 2.89~m… |
| 138 | `02-methods.tex:199` | `14.5` | …against an observed 14.5 to 17.3~m, so it accounts for roughly 3.9\% of the rep… |
| 139 | `02-methods.tex:199` | `17.3` | …against an observed 14.5 to 17.3~m, so it accounts for roughly 3.9\% of the reported… |
| 140 | `02-methods.tex:199` | `3.9\%` | …an observed 14.5 to 17.3~m, so it accounts for roughly 3.9\% of the reported… |
| 141 | `02-methods.tex:202` | `18` | …(\texttt{e218f29}).… |
| 142 | `02-methods.tex:202` | `9` | …(\texttt{e218f29}).… |
| 143 | `03-results.tex:73` | `five` | …\caption{The five arms over 130 Ankara chips, averaged over the six conf… |
| 144 | `03-results.tex:73` | `130` | …\caption{The five arms over 130 Ankara chips, averaged over the six confirmatory seeds… |
| 145 | `03-results.tex:73` | `six` | …The five arms over 130 Ankara chips, averaged over the six confirmatory seeds… |
| 146 | `03-results.tex:74` | `45--50` | …(45--50). Residual: per chip, the median KLT positional error… |
| 147 | `03-results.tex:75` | `2` | …arm itself produced against real Sentinel-2; per seed, the mean and the median of the 130… |
| 148 | `03-results.tex:75` | `130` | …l Sentinel-2; per seed, the mean and the median of the 130… |
| 149 | `03-results.tex:86` | `2.563` | …pretrained (adv.\ + LPIPS, European) & 2.563 & 2.588 & 51 & 1.02 \\… |
| 150 | `03-results.tex:86` | `2.588` | …pretrained (adv.\ + LPIPS, European) & 2.563 & 2.588 & 51 & 1.02 \\… |
| 151 | `03-results.tex:86` | `51` | …pretrained (adv.\ + LPIPS, European) & 2.563 & 2.588 & 51 & 1.02 \\… |
| 152 | `03-results.tex:86` | `1.02` | …ained (adv.\ + LPIPS, European) & 2.563 & 2.588 & 51 & 1.02 \\… |
| 153 | `03-results.tex:87` | `2.070` | …adversarial + L1 & 2.070 (0.025) & 1.987 & 62 & 1.09 \\… |
| 154 | `03-results.tex:87` | `0.025` | …adversarial + L1 & 2.070 (0.025) & 1.987 & 62 & 1.09 \\… |
| 155 | `03-results.tex:87` | `1.987` | …adversarial + L1 & 2.070 (0.025) & 1.987 & 62 & 1.09 \\… |
| 156 | `03-results.tex:87` | `62` | …adversarial + L1 & 2.070 (0.025) & 1.987 & 62 & 1.09 \\… |
| 157 | `03-results.tex:87` | `1.09` | …adversarial + L1 & 2.070 (0.025) & 1.987 & 62 & 1.09 \\… |
| 158 | `03-results.tex:88` | `393` | …L1 only & \textbf{1.393} (0.037) & \textbf{0.975} & 75 & \textbf{0.28} \\… |
| 159 | `03-results.tex:88` | `0.037` | …L1 only & \textbf{1.393} (0.037) & \textbf{0.975} & 75 & \textbf{0.28} \\… |
| 160 | `03-results.tex:88` | `975` | …L1 only & \textbf{1.393} (0.037) & \textbf{0.975} & 75 & \textbf{0.28} \\… |
| 161 | `03-results.tex:88` | `75` | …L1 only & \textbf{1.393} (0.037) & \textbf{0.975} & 75 & \textbf{0.28} \\… |
| 162 | `03-results.tex:88` | `28` | …extbf{1.393} (0.037) & \textbf{0.975} & 75 & \textbf{0.28} \\… |
| 163 | `03-results.tex:89` | `2.065` | …adversarial + LPIPS & 2.065 (0.025) & 1.939 & 60 & 1.13 \\… |
| 164 | `03-results.tex:89` | `0.025` | …adversarial + LPIPS & 2.065 (0.025) & 1.939 & 60 & 1.13 \\… |
| 165 | `03-results.tex:89` | `1.939` | …adversarial + LPIPS & 2.065 (0.025) & 1.939 & 60 & 1.13 \\… |
| 166 | `03-results.tex:89` | `60` | …adversarial + LPIPS & 2.065 (0.025) & 1.939 & 60 & 1.13 \\… |
| 167 | `03-results.tex:89` | `1.13` | …adversarial + LPIPS & 2.065 (0.025) & 1.939 & 60 & 1.13 \\… |
| 168 | `03-results.tex:90` | `1.456` | …LPIPS only & 1.456 (0.013) & 1.110 & \textbf{87} & \textbf{1.15} \\… |
| 169 | `03-results.tex:90` | `0.013` | …LPIPS only & 1.456 (0.013) & 1.110 & \textbf{87} & \textbf{1.15} \\… |
| 170 | `03-results.tex:90` | `1.110` | …LPIPS only & 1.456 (0.013) & 1.110 & \textbf{87} & \textbf{1.15} \\… |
| 171 | `03-results.tex:90` | `7` | …LPIPS only & 1.456 (0.013) & 1.110 & \textbf{87} & \textbf{1.15} \\… |
| 172 | `03-results.tex:90` | `15` | …only & 1.456 (0.013) & 1.110 & \textbf{87} & \textbf{1.15} \\… |
| 173 | `03-results.tex:95` | `five` | …Table~ gives all five arms over 130 Ankara chips, averaged across six… |
| 174 | `03-results.tex:95` | `130` | …Table~ gives all five arms over 130 Ankara chips, averaged across six… |
| 175 | `03-results.tex:95` | `six` | …s all five arms over 130 Ankara chips, averaged across six… |
| 176 | `03-results.tex:96` | `two` | …seeds. The ordering is L1-only $<$ LPIPS-only $<$ the two… |
| 177 | `03-results.tex:97` | `1.39` | …adversarial arms $<$ pretrained, from 1.39~px to 2.56~px. Three of those positions hold… |
| 178 | `03-results.tex:97` | `2.56` | …adversarial arms $<$ pretrained, from 1.39~px to 2.56~px. Three of those positions hold… |
| 179 | `03-results.tex:97` | `Three` | …ersarial arms $<$ pretrained, from 1.39~px to 2.56~px. Three of those positions hold… |
| 180 | `03-results.tex:98` | `two` | …in every seed; the two adversarial arms do not order: adversarial+LPIPS score… |
| 181 | `03-results.tex:99` | `three` | …adversarial+L1 in three seeds and above it in three, and their six-seed means… |
| 182 | `03-results.tex:99` | `three` | …adversarial+L1 in three seeds and above it in three, and their six-seed means differ by… |
| 183 | `03-results.tex:99` | `six` | …ial+L1 in three seeds and above it in three, and their six-seed means differ by… |
| 184 | `03-results.tex:100` | `0.005` | …0.005~px. Both adversarial arms sit above both non-adversari… |
| 185 | `03-results.tex:101` | `two` | …two non-adversarial arms are separated by 0.063~px.… |
| 186 | `03-results.tex:101` | `0.063` | …two non-adversarial arms are separated by 0.063~px.… |
| 187 | `03-results.tex:108` | `six` | …\caption{Sign replication across the six confirmatory seeds for the three seed-level… |
| 188 | `03-results.tex:108` | `three` | …replication across the six confirmatory seeds for the three seed-level… |
| 189 | `03-results.tex:109` | `one` | …contrasts of this section, in px; each point is one seed's $\Delta_s$ of… |
| 190 | `03-results.tex:111` | `six` | …all six on one side of zero, $P = 1/64$ with the direction fix… |
| 191 | `03-results.tex:111` | `one` | …all six on one side of zero, $P = 1/64$ with the direction fixed in a… |
| 192 | `03-results.tex:111` | `1/64` | …all six on one side of zero, $P = 1/64$ with the direction fixed in advance. The seed-level… |
| 193 | `03-results.tex:112` | `95\%` | …mean (bar) and its 95\% interval of () (gray band) are reported, not… |
| 194 | `03-results.tex:119` | `six` | …reconstruction loss in all six seeds (Fig.~). Per seed, LPIPS-only minus adversarial+… |
| 195 | `03-results.tex:120` | `-0.615` | …$-0.615$, $-0.646$, $-0.616$, $-0.594$, $-0.605$ and $-0.578$~… |
| 196 | `03-results.tex:120` | `-0.646` | …$-0.615$, $-0.646$, $-0.616$, $-0.594$, $-0.605$ and $-0.578$~px. The di… |
| 197 | `03-results.tex:120` | `-0.616` | …$-0.615$, $-0.646$, $-0.616$, $-0.594$, $-0.605$ and $-0.578$~px. The direction wa… |
| 198 | `03-results.tex:120` | `-0.594` | …$-0.615$, $-0.646$, $-0.616$, $-0.594$, $-0.605$ and $-0.578$~px. The direction was fixed… |
| 199 | `03-results.tex:120` | `-0.605` | …$-0.615$, $-0.646$, $-0.616$, $-0.594$, $-0.605$ and $-0.578$~px. The direction was fixed… |
| 200 | `03-results.tex:120` | `-0.578` | …$-0.615$, $-0.646$, $-0.616$, $-0.594$, $-0.605$ and $-0.578$~px. The direction was fixed… |
| 201 | `03-results.tex:121` | `six` | …vance from an earlier seed and registered before these six were trained, so under a… |
| 202 | `03-results.tex:122` | `six` | …null of no effect the probability of six agreeing signs is 1/64.… |
| 203 | `03-results.tex:122` | `1/64` | …of no effect the probability of six agreeing signs is 1/64.… |
| 204 | `03-results.tex:124` | `-0.609` | …The seed-level mean is $-0.609$~px, with a 95\% interval of $[-0.634, -0.585]$ at fiv… |
| 205 | `03-results.tex:124` | `95\%` | …The seed-level mean is $-0.609$~px, with a 95\% interval of $[-0.634, -0.585]$ at five… |
| 206 | `03-results.tex:124` | `-0.634` | …d-level mean is $-0.609$~px, with a 95\% interval of $[-0.634, -0.585]$ at five… |
| 207 | `03-results.tex:124` | `-0.585` | …mean is $-0.609$~px, with a 95\% interval of $[-0.634, -0.585]$ at five… |
| 208 | `03-results.tex:124` | `five` | …609$~px, with a 95\% interval of $[-0.634, -0.585]$ at five… |
| 209 | `03-results.tex:129` | `six` | …positive in all six seeds, per seed $+0.675$, $+0.587$, $+0.701$, $+0.754$… |
| 210 | `03-results.tex:129` | `+0.675` | …positive in all six seeds, per seed $+0.675$, $+0.587$, $+0.701$, $+0.754$, $+0.702$ and… |
| 211 | `03-results.tex:129` | `+0.587` | …positive in all six seeds, per seed $+0.675$, $+0.587$, $+0.701$, $+0.754$, $+0.702$ and… |
| 212 | `03-results.tex:129` | `+0.701` | …sitive in all six seeds, per seed $+0.675$, $+0.587$, $+0.701$, $+0.754$, $+0.702$ and… |
| 213 | `03-results.tex:129` | `+0.754` | …all six seeds, per seed $+0.675$, $+0.587$, $+0.701$, $+0.754$, $+0.702$ and… |
| 214 | `03-results.tex:129` | `+0.702` | …eds, per seed $+0.675$, $+0.587$, $+0.701$, $+0.754$, $+0.702$ and… |
| 215 | `03-results.tex:130` | `+0.644` | …$+0.644$~px, a reading registered at seed level beside the pri… |
| 216 | `03-results.tex:131` | `+0.677` | …$+0.677$~px with a 95\% interval of $[+0.617, +0.737]$, report… |
| 217 | `03-results.tex:131` | `95\%` | …$+0.677$~px with a 95\% interval of $[+0.617, +0.737]$, reported, not required… |
| 218 | `03-results.tex:131` | `+0.617` | …$+0.677$~px with a 95\% interval of $[+0.617, +0.737]$, reported, not required.… |
| 219 | `03-results.tex:131` | `+0.737` | …$+0.677$~px with a 95\% interval of $[+0.617, +0.737]$, reported, not required.… |
| 220 | `03-results.tex:134` | `one` | …section is one number per seed, with variability taken across seeds.… |
| 221 | `03-results.tex:139` | `two` | …two reconstruction terms---the adversarial penalty under a… |
| 222 | `03-results.tex:142` | `four` | …residual, and a within-chip rank transform across the four arms.… |
| 223 | `03-results.tex:144` | `six` | …Across the six confirmatory seeds the interaction was negative in fiv… |
| 224 | `03-results.tex:144` | `five` | …six confirmatory seeds the interaction was negative in five and… |
| 225 | `03-results.tex:145` | `one` | …positive in one, and the same seed reversed the sign on the log and ra… |
| 226 | `03-results.tex:146` | `five` | …five of six on each of the three registered scales. The reg… |
| 227 | `03-results.tex:146` | `six` | …five of six on each of the three registered scales. The registered… |
| 228 | `03-results.tex:146` | `three` | …five of six on each of the three registered scales. The registered reading therefore… |
| 229 | `03-results.tex:150` | `two` | …An earlier two-seed block, run on different hardware, returned a nega… |
| 230 | `03-results.tex:151` | `three` | …both of its seeds on all three scales. It is reported here for completeness and carri… |
| 231 | `03-results.tex:152` | `six` | …weight against the six-seed result, because the two blocks cannot be pooled a… |
| 232 | `03-results.tex:152` | `two` | …weight against the six-seed result, because the two blocks cannot be pooled and two seeds… |
| 233 | `03-results.tex:152` | `two` | …ed result, because the two blocks cannot be pooled and two seeds… |
| 234 | `03-results.tex:153` | `six` | …do not override six.… |
| 235 | `03-results.tex:155` | `three` | …The seed-level means are negative on all three scales, and the log-scale and rank-scale… |
| 236 | `03-results.tex:163` | `six` | …r present: LPIPS-only minus L1-only is positive in all six seeds, again… |
| 237 | `03-results.tex:164` | `1/64` | …$P = 1/64$, with a seed-level mean of $+0.063$~px and a 95\% int… |
| 238 | `03-results.tex:164` | `+0.063` | …$P = 1/64$, with a seed-level mean of $+0.063$~px and a 95\% interval of… |
| 239 | `03-results.tex:164` | `95\%` | …P = 1/64$, with a seed-level mean of $+0.063$~px and a 95\% interval of… |
| 240 | `03-results.tex:165` | `+0.027` | …$[+0.027, +0.098]$ at five degrees of freedom, reported not req… |
| 241 | `03-results.tex:165` | `+0.098` | …$[+0.027, +0.098]$ at five degrees of freedom, reported not required. T… |
| 242 | `03-results.tex:165` | `five` | …$[+0.027, +0.098]$ at five degrees of freedom, reported not required. The narrowe… |
| 243 | `03-results.tex:166` | `0.007` | …seed clears zero by 0.007~px. This is a consistent small positive effect, six ti… |
| 244 | `03-results.tex:166` | `six` | …0.007~px. This is a consistent small positive effect, six times out… |
| 245 | `03-results.tex:167` | `six` | …of six, and it should be read as consistent rather than as co… |
| 246 | `03-results.tex:169` | `two` | …aller than a tolerance stated in Section~II-D, and the two belong… |
| 247 | `03-results.tex:171` | `15` | …score-neutral within $\pm0.15$~px; the effect that carries the title is $+0.063$~px,… |
| 248 | `03-results.tex:171` | `+0.063` | …in $\pm0.15$~px; the effect that carries the title is $+0.063$~px,… |
| 249 | `03-results.tex:172` | `2.4` | …2.4 times smaller than that tolerance. Four things make it… |
| 250 | `03-results.tex:172` | `Four` | …2.4 times smaller than that tolerance. Four things make it a result anyway. The tolerance… |
| 251 | `03-results.tex:173` | `30` | …n of a \emph{path comparison}---the precision at which 30 chips could… |
| 252 | `03-results.tex:174` | `two` | …tell two inference paths apart, with measured path differences… |
| 253 | `03-results.tex:174` | `0.004` | …ference paths apart, with measured path differences of 0.004 to 0.040~px and… |
| 254 | `03-results.tex:174` | `0.040` | …aths apart, with measured path differences of 0.004 to 0.040~px and… |
| 255 | `03-results.tex:175` | `0.08` | …standard errors near 0.08~px---whereas the effect is a paired within-chip contra… |
| 256 | `03-results.tex:176` | `two` | …between two arms scored on the same path, on 130 chips, so draw-to… |
| 257 | `03-results.tex:176` | `130` | …between two arms scored on the same path, on 130 chips, so draw-to-draw variation enters… |
| 258 | `03-results.tex:177` | `six` | …what the tolerance bounds. The sign replicates in all six… |
| 259 | `03-results.tex:178` | `six` | …n draws, which a draw artefact would have to reproduce six times… |
| 260 | `03-results.tex:181` | `two` | …re-measured for the two LPIPS arms, so it is not a bound on this contrast in e… |
| 261 | `03-results.tex:183` | `one` | …small effect, not a comfortable one.… |
| 262 | `03-results.tex:191` | `six` | …six confirmatory seeds. Penalty: per seed, the chip mean o… |
| 263 | `03-results.tex:191` | `130` | …firmatory seeds. Penalty: per seed, the chip mean over 130 chips of the adversarial… |
| 264 | `03-results.tex:193` | `six` | …rsarial arm is worse; thin lines are seeds, points are six-seed means with the… |
| 265 | `03-results.tex:194` | `20` | …seed-to-seed s.d. Epoch 20 is the block of Table~; epochs 1, 2, 5 and 10… |
| 266 | `03-results.tex:194` | `1,` | …d-to-seed s.d. Epoch 20 is the block of Table~; epochs 1, 2, 5 and 10… |
| 267 | `03-results.tex:194` | `2,` | …o-seed s.d. Epoch 20 is the block of Table~; epochs 1, 2, 5 and 10… |
| 268 | `03-results.tex:194` | `5` | …eed s.d. Epoch 20 is the block of Table~; epochs 1, 2, 5 and 10… |
| 269 | `03-results.tex:194` | `10` | …d. Epoch 20 is the block of Table~; epochs 1, 2, 5 and 10… |
| 270 | `03-results.tex:200` | `1,` | …The adversarial penalty was scored at epochs 1, 2, 5, 10 and 20 for both families at all… |
| 271 | `03-results.tex:200` | `2,` | …The adversarial penalty was scored at epochs 1, 2, 5, 10 and 20 for both families at all… |
| 272 | `03-results.tex:200` | `5,` | …The adversarial penalty was scored at epochs 1, 2, 5, 10 and 20 for both families at all… |
| 273 | `03-results.tex:200` | `10` | …The adversarial penalty was scored at epochs 1, 2, 5, 10 and 20 for both families at all… |
| 274 | `03-results.tex:200` | `20` | …versarial penalty was scored at epochs 1, 2, 5, 10 and 20 for both families at all… |
| 275 | `03-results.tex:201` | `six` | …six seeds, with the reading registered before any cell was… |
| 276 | `03-results.tex:202` | `six` | …scored epoch in every seed. It held in both families, six of six at each of the… |
| 277 | `03-results.tex:202` | `six` | …epoch in every seed. It held in both families, six of six at each of the… |
| 278 | `03-results.tex:203` | `five` | …five epochs (Fig.~). The six-seed means run 0.26, 0.26, 0.5… |
| 279 | `03-results.tex:203` | `six` | …five epochs (Fig.~). The six-seed means run 0.26, 0.26, 0.50, 0.53 and… |
| 280 | `03-results.tex:203` | `0.26` | …five epochs (Fig.~). The six-seed means run 0.26, 0.26, 0.50, 0.53 and… |
| 281 | `03-results.tex:203` | `0.26` | …five epochs (Fig.~). The six-seed means run 0.26, 0.26, 0.50, 0.53 and… |
| 282 | `03-results.tex:203` | `0.50` | …ive epochs (Fig.~). The six-seed means run 0.26, 0.26, 0.50, 0.53 and… |
| 283 | `03-results.tex:203` | `0.53` | …ochs (Fig.~). The six-seed means run 0.26, 0.26, 0.50, 0.53 and… |
| 284 | `03-results.tex:204` | `0.61` | …0.61~px under the perceptual loss and 0.52, 0.47, 0.42, 0.5… |
| 285 | `03-results.tex:204` | `0.52` | …0.61~px under the perceptual loss and 0.52, 0.47, 0.42, 0.58 and 0.68~px under L1.… |
| 286 | `03-results.tex:204` | `0.47` | …0.61~px under the perceptual loss and 0.52, 0.47, 0.42, 0.58 and 0.68~px under L1.… |
| 287 | `03-results.tex:204` | `0.42` | …0.61~px under the perceptual loss and 0.52, 0.47, 0.42, 0.58 and 0.68~px under L1.… |
| 288 | `03-results.tex:204` | `0.58` | ….61~px under the perceptual loss and 0.52, 0.47, 0.42, 0.58 and 0.68~px under L1.… |
| 289 | `03-results.tex:204` | `0.68` | …der the perceptual loss and 0.52, 0.47, 0.42, 0.58 and 0.68~px under L1.… |
| 290 | `03-results.tex:205` | `six` | …Under the perceptual loss the six-seed mean rises from epoch 2 onward; under L1 it falls… |
| 291 | `03-results.tex:205` | `2` | …the perceptual loss the six-seed mean rises from epoch 2 onward; under L1 it falls… |
| 292 | `03-results.tex:206` | `1` | …from epoch 1 to epoch 5 before rising, so the mean gap at epoch 20… |
| 293 | `03-results.tex:206` | `5` | …from epoch 1 to epoch 5 before rising, so the mean gap at epoch 20 exceeds the… |
| 294 | `03-results.tex:206` | `20` | …h 1 to epoch 5 before rising, so the mean gap at epoch 20 exceeds the mean gap at… |
| 295 | `03-results.tex:207` | `1` | …epoch 1 in both families while the path between is not monoton… |
| 296 | `03-results.tex:209` | `0.334` | …ip-then-grow shape read off the single generating run (0.334, 0.254, 0.441, 0.496,… |
| 297 | `03-results.tex:209` | `0.254` | …-grow shape read off the single generating run (0.334, 0.254, 0.441, 0.496,… |
| 298 | `03-results.tex:209` | `0.441` | …hape read off the single generating run (0.334, 0.254, 0.441, 0.496,… |
| 299 | `03-results.tex:209` | `0.496` | …ad off the single generating run (0.334, 0.254, 0.441, 0.496,… |
| 300 | `03-results.tex:210` | `0.487` | …0.487~px under the perceptual loss) was registered as an exp… |
| 301 | `03-results.tex:212` | `three` | …growth appears in three of six seeds under the perceptual loss and five of six… |
| 302 | `03-results.tex:212` | `six` | …growth appears in three of six seeds under the perceptual loss and five of six under… |
| 303 | `03-results.tex:212` | `five` | …rs in three of six seeds under the perceptual loss and five of six under L1.… |
| 304 | `03-results.tex:212` | `six` | …ree of six seeds under the perceptual loss and five of six under L1.… |
| 305 | `03-results.tex:222` | `Two` | …What each arm renders where the input asserts nothing. Two chips from the… |
| 306 | `03-results.tex:223` | `130` | …130-chip Ankara panel, chosen by rule rather than by eye:… |
| 307 | `03-results.tex:225` | `601` | …ion. Columns: the input render as the mask sees it (BT.601 gray, the luminance-weighted… |
| 308 | `03-results.tex:226` | `three` | …conversion of the three-band render to one band; the input-silent region is ev… |
| 309 | `03-results.tex:226` | `one` | …conversion of the three-band render to one band; the input-silent region is everything… |
| 310 | `03-results.tex:228` | `2` | …the real Sentinel-2 chip, and the five arms at seed 45 (the pretrained arm… |
| 311 | `03-results.tex:228` | `five` | …the real Sentinel-2 chip, and the five arms at seed 45 (the pretrained arm is… |
| 312 | `03-results.tex:228` | `45` | …the real Sentinel-2 chip, and the five arms at seed 45 (the pretrained arm is… |
| 313 | `03-results.tex:231` | `0.36` | …nders edges only along the input's own structure ($r = 0.36$) while every other arm… |
| 314 | `03-results.tex:234` | `0.94` | …roughly the real density ($r = 0.94$ to $1.18$): information absent from the input… |
| 315 | `03-results.tex:234` | `$1.18` | …roughly the real density ($r = 0.94$ to $1.18$): information absent from the input… |
| 316 | `03-results.tex:243` | `1.15` | …1.15 against 1.13 for adversarial+LPIPS, 1.09 for… |
| 317 | `03-results.tex:243` | `1.13` | …1.15 against 1.13 for adversarial+LPIPS, 1.09 for… |
| 318 | `03-results.tex:243` | `1.09` | …1.15 against 1.13 for adversarial+LPIPS, 1.09 for… |
| 319 | `03-results.tex:244` | `1.02` | …adversarial+L1 and 1.02 for the pretrained generator. L1-only is the outlier i… |
| 320 | `03-results.tex:245` | `0.28` | …the other direction at 0.28. Every value is a six-seed mean and the ordering holds… |
| 321 | `03-results.tex:245` | `six` | …the other direction at 0.28. Every value is a six-seed mean and the ordering holds… |
| 322 | `03-results.tex:246` | `six` | …in all six.… |
| 323 | `03-results.tex:251` | `one` | …arm that has one.… |
| 324 | `03-results.tex:256` | `0.36` | …silent region at a fraction of the real edge density (0.36 on… |
| 325 | `03-results.tex:258` | `two` | …anywhere---two of the 130 chips fall entirely below the threshold---e… |
| 326 | `03-results.tex:258` | `130` | …anywhere---two of the 130 chips fall entirely below the threshold---every arm, L… |
| 327 | `03-results.tex:259` | `0.94` | …cluded, renders structure at roughly the real density (0.94 to 1.18 on the chip with the… |
| 328 | `03-results.tex:259` | `1.18` | …renders structure at roughly the real density (0.94 to 1.18 on the chip with the… |
| 329 | `03-results.tex:262` | `two` | …where there is something to be restrained by. Those two chips do not move the panel mean… |
| 330 | `03-results.tex:263` | `0.28` | …of 0.28, and they are excluded by rule from the comparison on… |
| 331 | `03-results.tex:270` | `130` | …a trivial trade. The LPIPS-only arm refutes it on the 130-chip Ankara panel of Table~: it… |
| 332 | `03-results.tex:271` | `87` | …produces more surviving matches than L1-only, 87 against 75 at the median, and still… |
| 333 | `03-results.tex:271` | `75` | …oduces more surviving matches than L1-only, 87 against 75 at the median, and still… |
| 334 | `03-results.tex:278` | `38\%` | …LPIPS-only arm surrenders 38\% of its points. Under equalised counts the primary… |
| 335 | `03-results.tex:279` | `1.8\%` | …contrast grows by 1.8\%, the LPIPS-only penalty shrinks by 11\%, and both hold… |
| 336 | `03-results.tex:279` | `11\%` | …rast grows by 1.8\%, the LPIPS-only penalty shrinks by 11\%, and both hold in all six… |
| 337 | `03-results.tex:279` | `six` | …IPS-only penalty shrinks by 11\%, and both hold in all six… |
| 338 | `03-results.tex:281` | `+0.037` | …above $+0.037$~px at a floor of 30 matches---the opposite of what a… |
| 339 | `03-results.tex:281` | `30` | …above $+0.037$~px at a floor of 30 matches---the opposite of what a selection artefact… |
| 340 | `03-results.tex:288` | `two` | …where the input does assert structure---separates the two, because blur suppresses… |
| 341 | `03-results.tex:290` | `1.5\%` | …real image's edge density to within 1.5\% there (0.986) while sitting at 0.277… |
| 342 | `03-results.tex:290` | `0.986` | …real image's edge density to within 1.5\% there (0.986) while sitting at 0.277… |
| 343 | `03-results.tex:290` | `0.277` | …density to within 1.5\% there (0.986) while sitting at 0.277… |
| 344 | `03-results.tex:291` | `3.6` | …where the input says nothing: a factor of 3.6 between the two masks, in all six seeds,… |
| 345 | `03-results.tex:291` | `two` | …re the input says nothing: a factor of 3.6 between the two masks, in all six seeds,… |
| 346 | `03-results.tex:291` | `six` | …nothing: a factor of 3.6 between the two masks, in all six seeds,… |
| 347 | `03-results.tex:297` | `one` | …raction estimate recorded in the study repository from one run (commit… |
| 348 | `03-results.tex:298` | `560` | …\texttt{6560c8b}, 24 August 2026), $-0.212$~px, falls outside… |
| 349 | `03-results.tex:298` | `24` | …\texttt{6560c8b}, 24 August 2026), $-0.212$~px, falls outside… |
| 350 | `03-results.tex:298` | `2026` | …\texttt{6560c8b}, 24 August 2026), $-0.212$~px, falls outside… |
| 351 | `03-results.tex:298` | `-0.212` | …\texttt{6560c8b}, 24 August 2026), $-0.212$~px, falls outside… |
| 352 | `03-results.tex:299` | `six` | …the range spanned by six replicates of the same treatment on the raw scale and… |
| 353 | `03-results.tex:301` | `Six` | …chip-level. Six replicates do not contain it, and its sign flips in on… |
| 354 | `03-results.tex:301` | `one` | …ix replicates do not contain it, and its sign flips in one of them.… |
| 355 | `03-results.tex:303` | `six` | …Falling outside a six-replicate range is not a significance test and no p-va… |
| 356 | `03-results.tex:310` | `six` | …tered before the training logs were read and scored at six seeds. What the… |
| 357 | `03-results.tex:312` | `six` | …than its non-adversarial counterpart---six of six in both families. What it does… |
| 358 | `03-results.tex:312` | `six` | …than its non-adversarial counterpart---six of six in both families. What it does… |
| 359 | `03-results.tex:314` | `six` | …reading holds for adversarial+LPIPS in all six seeds, mean $+1.45$\%, but fails for… |
| 360 | `03-results.tex:314` | `+1.45` | …ng holds for adversarial+LPIPS in all six seeds, mean $+1.45$\%, but fails for… |
| 361 | `03-results.tex:315` | `one` | …adversarial+L1, which falls in one seed and is indistinguishable from flat in another.… |
| 362 | `03-results.tex:318` | `one` | …operative form of the argument is the one that replicates; that rule read the generator's… |
| 363 | `03-results.tex:319` | `two` | …perceptual reconstruction loss rising over the first two main-stage epochs as the sign of… |
| 364 | `03-results.tex:320` | `42,` | …adversarial destabilisation, it fired at seed 42, and it was disclosed rather than acted… |
| 365 | `03-results.tex:322` | `6.33` | …g-rate schedule fixed on both sides and gives a gap of 6.33 points under… |
| 366 | `03-results.tex:323` | `4.00` | …the perceptual loss; the L1-family figure of 4.00 rests on an arm whose sign is not stable… |
| 367 | `03-results.tex:327` | `0` | …it is measured. Within platform and within seed (the A10G platform, seed 43), the… |
| 368 | `03-results.tex:327` | `43` | …thin platform and within seed (the A10G platform, seed 43), the… |
| 369 | `03-results.tex:328` | `5.16\%` | …only arm's reconstruction loss $G_{\mathrm{L1}}$ falls 5.16\% over its main stage… |
| 370 | `03-results.tex:329` | `2.98\%` | …un-warmed against 2.98\% warmed, and the LPIPS-only arm's perceptual loss… |
| 371 | `03-results.tex:330` | `7.98\%` | …$G_{\mathrm{LPIPS}}$ falls 7.98\% against 5.32\%; the controlled gap between adversarial… |
| 372 | `03-results.tex:330` | `5.32\%` | …$G_{\mathrm{LPIPS}}$ falls 7.98\% against 5.32\%; the controlled gap between adversarial and non-advers… |
| 373 | `03-results.tex:330` | `35.3\%` | …between adversarial and non-adversarial arm shrinks by 35.3\% in the… |
| 374 | `03-results.tex:331` | `29.7\%` | …L1 family and 29.7\% in the LPIPS family. The gap is a different quantity f… |
| 375 | `03-results.tex:332` | `6.19` | …arial arm's rise minus the non-adversarial arm's fall, 6.19 to 4.00 points… |
| 376 | `03-results.tex:332` | `4.00` | …m's rise minus the non-adversarial arm's fall, 6.19 to 4.00 points… |
| 377 | `03-results.tex:333` | `9.00` | …under L1 and 9.00 to 6.33 under LPIPS, so the percentages are shrinkages… |
| 378 | `03-results.tex:333` | `6.33` | …under L1 and 9.00 to 6.33 under LPIPS, so the percentages are shrinkages of that… |
| 379 | `03-results.tex:334` | `four` | …warm-up fall itself, and cannot be derived from the four fall figures alone.… |
| 380 | `03-results.tex:335` | `42` | …Measured across platforms instead, against the T4 seed-42 comparators, the same… |
| 381 | `03-results.tex:336` | `54.3\%` | …attenuation reads 54.3\% and 22.1\%: it overstates one family and understates t… |
| 382 | `03-results.tex:336` | `22.1\%` | …attenuation reads 54.3\% and 22.1\%: it overstates one family and understates the other,… |
| 383 | `03-results.tex:336` | `one` | …attenuation reads 54.3\% and 22.1\%: it overstates one family and understates the other,… |
| 384 | `03-results.tex:358` | `one` | …he render is seed-invariant, so the measurement yields one number per chip; every… |
| 385 | `03-results.tex:359` | `123` | …arison here is a paired chip-level difference over the 123 chips on which the render… |
| 386 | `03-results.tex:360` | `one` | …produced at least one match, and no seed-level statement is available or mad… |
| 387 | `03-results.tex:362` | `0.583` | …per-chip median residual is 0.583~px (mean of medians 0.797~px), and the paired chip-lev… |
| 388 | `03-results.tex:362` | `0.797` | …per-chip median residual is 0.583~px (mean of medians 0.797~px), and the paired chip-level difference render minus… |
| 389 | `03-results.tex:362` | `123` | …ired chip-level difference render minus arm over those 123 chips is… |
| 390 | `03-results.tex:363` | `-1.715` | …$-1.715 \pm 0.091$~px against the pretrained generator, betwee… |
| 391 | `03-results.tex:363` | `0.091` | …$-1.715 \pm 0.091$~px against the pretrained generator, between $-1.15$… |
| 392 | `03-results.tex:363` | `-1.15` | …m 0.091$~px against the pretrained generator, between $-1.15$ and $-1.22$~px against adversarial + L1, between $-1.… |
| 393 | `03-results.tex:363` | `-1.22` | …against the pretrained generator, between $-1.15$ and $-1.22$~px against adversarial + L1, between $-1.13$ and $-1.… |
| 394 | `03-results.tex:363` | `-1.13` | ….15$ and $-1.22$~px against adversarial + L1, between $-1.13$ and $-1.22$~px… |
| 395 | `03-results.tex:363` | `-1.22` | ….22$~px against adversarial + L1, between $-1.13$ and $-1.22$~px… |
| 396 | `03-results.tex:364` | `-0.53` | …against adversarial + LPIPS, between $-0.53$ and $-0.57$~px against LPIPS-only and between… |
| 397 | `03-results.tex:364` | `-0.57` | …against adversarial + LPIPS, between $-0.53$ and $-0.57$~px against LPIPS-only and between… |
| 398 | `03-results.tex:365` | `-0.44` | …$-0.44$ and $-0.56$~px against L1-only across the six seeds'… |
| 399 | `03-results.tex:365` | `-0.56` | …$-0.44$ and $-0.56$~px against L1-only across the six seeds' arms, every… |
| 400 | `03-results.tex:365` | `six` | …$-0.44$ and $-0.56$~px against L1-only across the six seeds' arms, every one at six standard errors or more;… |
| 401 | `03-results.tex:365` | `one` | …$~px against L1-only across the six seeds' arms, every one at six standard errors or more; the equal-count trunca… |
| 402 | `03-results.tex:365` | `six` | …ainst L1-only across the six seeds' arms, every one at six standard errors or more; the equal-count truncation of… |
| 403 | `03-results.tex:366` | `0.02` | …leaves each fine-tuned comparison within 0.02~px of its raw value and gives $-1.778 \pm 0.109$~px ag… |
| 404 | `03-results.tex:366` | `-1.778` | …comparison within 0.02~px of its raw value and gives $-1.778 \pm 0.109$~px against the pretrained generator, over t… |
| 405 | `03-results.tex:366` | `0.109` | …within 0.02~px of its raw value and gives $-1.778 \pm 0.109$~px against the pretrained generator, over the same 12… |
| 406 | `03-results.tex:366` | `123` | …09$~px against the pretrained generator, over the same 123 chips.… |
| 407 | `03-results.tex:368` | `1.715` | …generator but grew it, from 1.715 to 1.778~px over the same chips; that is the direction… |
| 408 | `03-results.tex:368` | `1.778` | …generator but grew it, from 1.715 to 1.778~px over the same chips; that is the direction… |
| 409 | `03-results.tex:369` | `two` | …mum-match-count sweep of Section~III-G also moves, and two independent… |
| 410 | `03-results.tex:371` | `two` | …render's advantage, to the extent those two numbers support it. It matches on far fewer points: a… |
| 411 | `03-results.tex:371` | `29.5` | …upport it. It matches on far fewer points: a median of 29.5 surviving matches per chip, taken over… |
| 412 | `03-results.tex:372` | `130` | …all 130 chips with the 7 chips that yield no match at all coun… |
| 413 | `03-results.tex:372` | `7` | …all 130 chips with the 7 chips that yield no match at all counted as zero, agai… |
| 414 | `03-results.tex:372` | `75` | …ps that yield no match at all counted as zero, against 75 for… |
| 415 | `03-results.tex:373` | `87` | …L1-only and 87 for LPIPS-only, each a median over the same 130 chips,… |
| 416 | `03-results.tex:373` | `130` | …nly and 87 for LPIPS-only, each a median over the same 130 chips, on every one of which… |
| 417 | `03-results.tex:373` | `one` | …-only, each a median over the same 130 chips, on every one of which… |
| 418 | `03-results.tex:374` | `six` | …that arm matched, averaged over the six seeds. The registered ``matches well'' reading require… |
| 419 | `03-results.tex:376` | `half` | …not met either. The comparison set bounds the residual half of this finding and is named as such: the… |
| 420 | `03-results.tex:377` | `123` | …123 chips are the ones on which the render matched, and th… |
| 421 | `03-results.tex:380` | `130` | …on all 130. This is the selection objection Section~III-G raises… |
| 422 | `03-results.tex:381` | `half` | …e in the same form. It does not weaken the point-yield half, which counts the… |
| 423 | `03-results.tex:387` | `130` | …beyond these 130 chips.… |
| 424 | `04-alternatives.tex:50` | `Four` | …Four explanations compete with the account above. Three are… |
| 425 | `04-alternatives.tex:50` | `Three` | …Four explanations compete with the account above. Three are tested and refuted; the… |
| 426 | `04-alternatives.tex:54` | `1` | …\caption{Alternative explanations. Row 1 is a six-seed result. Rows 2 and 3 rest on single-seed… |
| 427 | `04-alternatives.tex:54` | `six` | …\caption{Alternative explanations. Row 1 is a six-seed result. Rows 2 and 3 rest on single-seed (seed 42… |
| 428 | `04-alternatives.tex:54` | `2` | …rnative explanations. Row 1 is a six-seed result. Rows 2 and 3 rest on single-seed (seed 42) artifacts:… |
| 429 | `04-alternatives.tex:54` | `3` | …e explanations. Row 1 is a six-seed result. Rows 2 and 3 rest on single-seed (seed 42) artifacts:… |
| 430 | `04-alternatives.tex:54` | `42` | …ix-seed result. Rows 2 and 3 rest on single-seed (seed 42) artifacts:… |
| 431 | `04-alternatives.tex:55` | `2` | …row 2 is a chip-level checkpoint sweep whose standard errors… |
| 432 | `04-alternatives.tex:55` | `3` | …sweep whose standard errors are across chips, and row 3's… |
| 433 | `04-alternatives.tex:56` | `two` | …two registrations were scored on seed 42's generated image… |
| 434 | `04-alternatives.tex:56` | `42` | …two registrations were scored on seed 42's generated images. The corrected-georeferencing candi… |
| 435 | `04-alternatives.tex:61` | `6` | …\begin{tabular}{@{}p{2.6cm}p{4.6cm}p{6.2cm}p{2.9cm}@{}}… |
| 436 | `04-alternatives.tex:61` | `6` | …\begin{tabular}{@{}p{2.6cm}p{4.6cm}p{6.2cm}p{2.9cm}@{}}… |
| 437 | `04-alternatives.tex:61` | `2` | …\begin{tabular}{@{}p{2.6cm}p{4.6cm}p{6.2cm}p{2.9cm}@{}}… |
| 438 | `04-alternatives.tex:61` | `9` | …\begin{tabular}{@{}p{2.6cm}p{4.6cm}p{6.2cm}p{2.9cm}@{}}… |
| 439 | `04-alternatives.tex:67` | `six` | …six seeds; bands 0.80 and 0.50 fixed in advance &… |
| 440 | `04-alternatives.tex:67` | `0.80` | …six seeds; bands 0.80 and 0.50 fixed in advance &… |
| 441 | `04-alternatives.tex:67` | `0.50` | …six seeds; bands 0.80 and 0.50 fixed in advance &… |
| 442 | `04-alternatives.tex:68` | `0.986` | …L1-only 0.986 on the informative mask against 0.277 where the input… |
| 443 | `04-alternatives.tex:68` | `0.277` | …L1-only 0.986 on the informative mask against 0.277 where the input is silent, a factor… |
| 444 | `04-alternatives.tex:69` | `3.6` | …of 3.6, in every seed; the other arms 1.03--1.05 on the infor… |
| 445 | `04-alternatives.tex:69` | `1.03--1.05` | …of 3.6, in every seed; the other arms 1.03--1.05 on the informative mask &… |
| 446 | `04-alternatives.tex:73` | `1,` | …Checkpoint sweep at epochs 1, 2, 5, 10, 20 against the pretrained generator and the… |
| 447 | `04-alternatives.tex:73` | `2,` | …Checkpoint sweep at epochs 1, 2, 5, 10, 20 against the pretrained generator and the… |
| 448 | `04-alternatives.tex:73` | `5,` | …Checkpoint sweep at epochs 1, 2, 5, 10, 20 against the pretrained generator and the… |
| 449 | `04-alternatives.tex:73` | `10,` | …Checkpoint sweep at epochs 1, 2, 5, 10, 20 against the pretrained generator and the… |
| 450 | `04-alternatives.tex:73` | `20` | …Checkpoint sweep at epochs 1, 2, 5, 10, 20 against the pretrained generator and the… |
| 451 | `04-alternatives.tex:75` | `1,` | …versarial + L1 already better than pretrained at epoch 1, $-0.399 \pm 0.064$ (6.3… |
| 452 | `04-alternatives.tex:75` | `-0.399` | …arial + L1 already better than pretrained at epoch 1, $-0.399 \pm 0.064$ (6.3… |
| 453 | `04-alternatives.tex:75` | `0.064` | …already better than pretrained at epoch 1, $-0.399 \pm 0.064$ (6.3… |
| 454 | `04-alternatives.tex:75` | `6.3` | …better than pretrained at epoch 1, $-0.399 \pm 0.064$ (6.3… |
| 455 | `04-alternatives.tex:76` | `+0.546` | …s.e.); its deficit against L1-only $+0.546$ at epoch 1 and $+0.700$ at epoch 20, dipping… |
| 456 | `04-alternatives.tex:76` | `1` | …s.e.); its deficit against L1-only $+0.546$ at epoch 1 and $+0.700$ at epoch 20, dipping… |
| 457 | `04-alternatives.tex:76` | `+0.700` | …; its deficit against L1-only $+0.546$ at epoch 1 and $+0.700$ at epoch 20, dipping… |
| 458 | `04-alternatives.tex:76` | `20,` | …inst L1-only $+0.546$ at epoch 1 and $+0.700$ at epoch 20, dipping… |
| 459 | `04-alternatives.tex:77` | `+0.384` | …to $+0.384$ at epoch 5 &… |
| 460 | `04-alternatives.tex:77` | `5` | …to $+0.384$ at epoch 5 &… |
| 461 | `04-alternatives.tex:82` | `two` | …her family: KLT, NCC template grid, phase correlation, two band conversions, an… |
| 462 | `04-alternatives.tex:83` | `6,510` | …urban subset, 6,510 comparisons &… |
| 463 | `04-alternatives.tex:84` | `-0.613` | …(a) L1-only ahead in every family; ORB $-0.613 \pm 0.135$ ($n = 29$), MI a lower bound;… |
| 464 | `04-alternatives.tex:84` | `0.135` | …(a) L1-only ahead in every family; ORB $-0.613 \pm 0.135$ ($n = 29$), MI a lower bound;… |
| 465 | `04-alternatives.tex:84` | `29` | …ly ahead in every family; ORB $-0.613 \pm 0.135$ ($n = 29$), MI a lower bound;… |
| 466 | `04-alternatives.tex:85` | `two` | …(b) ordering preserved in every cell but two, both far below threshold; the template… |
| 467 | `04-alternatives.tex:86` | `eight` | …matcher widened the margin in all eight combinations &… |
| 468 | `04-alternatives.tex:87` | `two` | …Refuted by two registrations sharing no matcher, chip set or code \\… |
| 469 | `04-alternatives.tex:103` | `two` | …, where the input does assert structure, separates the two explanations… |
| 470 | `04-alternatives.tex:108` | `0.80` | …were fixed in advance at 0.80 and 0.50, reusing the bands already registered for the… |
| 471 | `04-alternatives.tex:108` | `0.50` | …were fixed in advance at 0.80 and 0.50, reusing the bands already registered for the… |
| 472 | `04-alternatives.tex:111` | `six` | …The result. Across six seeds the L1-only arm reproduces the real image's edge… |
| 473 | `04-alternatives.tex:112` | `1.5\%` | …density to within 1.5\% on the informative mask---0.986, range 0.980 to 0.989-… |
| 474 | `04-alternatives.tex:112` | `-0.986` | …density to within 1.5\% on the informative mask---0.986, range 0.980 to 0.989---while… |
| 475 | `04-alternatives.tex:112` | `0.980` | …to within 1.5\% on the informative mask---0.986, range 0.980 to 0.989---while… |
| 476 | `04-alternatives.tex:112` | `0.989` | …1.5\% on the informative mask---0.986, range 0.980 to 0.989---while… |
| 477 | `04-alternatives.tex:113` | `0.277` | …sitting at 0.277 on the input-silent mask. A factor of 3.6 between the… |
| 478 | `04-alternatives.tex:113` | `3.6` | …sitting at 0.277 on the input-silent mask. A factor of 3.6 between the two… |
| 479 | `04-alternatives.tex:113` | `two` | …on the input-silent mask. A factor of 3.6 between the two… |
| 480 | `04-alternatives.tex:115` | `six` | …conditions hold six times out of six. The other three arms sit between 1.0… |
| 481 | `04-alternatives.tex:115` | `six` | …conditions hold six times out of six. The other three arms sit between 1.03 and 1.05 on… |
| 482 | `04-alternatives.tex:115` | `three` | …conditions hold six times out of six. The other three arms sit between 1.03 and 1.05 on… |
| 483 | `04-alternatives.tex:115` | `1.03` | …six times out of six. The other three arms sit between 1.03 and 1.05 on… |
| 484 | `04-alternatives.tex:115` | `1.05` | …out of six. The other three arms sit between 1.03 and 1.05 on… |
| 485 | `04-alternatives.tex:116` | `1.09` | …tive mask, slightly above reality, consistent with the 1.09 to 1.15… |
| 486 | `04-alternatives.tex:116` | `1.15` | …k, slightly above reality, consistent with the 1.09 to 1.15… |
| 487 | `04-alternatives.tex:119` | `one` | …The reading. Every arm except the L1-only one adds edges everywhere. Where the input… |
| 488 | `04-alternatives.tex:134` | `one` | …dversarial arm here begins from a randomly initialised one. Adversarial arms… |
| 489 | `04-alternatives.tex:138` | `1,` | …The test. A checkpoint sweep at epochs 1, 2, 5, 10 and 20, comparing each arm to… |
| 490 | `04-alternatives.tex:138` | `2,` | …The test. A checkpoint sweep at epochs 1, 2, 5, 10 and 20, comparing each arm to… |
| 491 | `04-alternatives.tex:138` | `5,` | …The test. A checkpoint sweep at epochs 1, 2, 5, 10 and 20, comparing each arm to… |
| 492 | `04-alternatives.tex:138` | `10` | …The test. A checkpoint sweep at epochs 1, 2, 5, 10 and 20, comparing each arm to… |
| 493 | `04-alternatives.tex:138` | `20,` | …The test. A checkpoint sweep at epochs 1, 2, 5, 10 and 20, comparing each arm to… |
| 494 | `04-alternatives.tex:141` | `1` | …The result. At epoch 1 the adversarial+L1 arm is already better than… |
| 495 | `04-alternatives.tex:142` | `-0.399` | …pretrained, by $-0.399 \pm 0.064$~px at 6.3 standard errors. That is the wron… |
| 496 | `04-alternatives.tex:142` | `0.064` | …pretrained, by $-0.399 \pm 0.064$~px at 6.3 standard errors. That is the wrong… |
| 497 | `04-alternatives.tex:142` | `6.3` | …pretrained, by $-0.399 \pm 0.064$~px at 6.3 standard errors. That is the wrong… |
| 498 | `04-alternatives.tex:145` | `1` | …non-adversarial arm is present from epoch 1 at $+0.546 \pm 0.048$ and reaches $+0.700$ by… |
| 499 | `04-alternatives.tex:145` | `+0.546` | …non-adversarial arm is present from epoch 1 at $+0.546 \pm 0.048$ and reaches $+0.700$ by… |
| 500 | `04-alternatives.tex:145` | `0.048` | …adversarial arm is present from epoch 1 at $+0.546 \pm 0.048$ and reaches $+0.700$ by… |
| 501 | `04-alternatives.tex:145` | `+0.700` | …resent from epoch 1 at $+0.546 \pm 0.048$ and reaches $+0.700$ by… |
| 502 | `04-alternatives.tex:146` | `20` | …epoch 20.… |
| 503 | `04-alternatives.tex:148` | `1` | …is ours rather than a reviewer's. The path from epoch 1 to… |
| 504 | `04-alternatives.tex:149` | `20` | …epoch 20 is not monotone: it dips to $+0.384$ at epoch 5 before… |
| 505 | `04-alternatives.tex:149` | `+0.384` | …epoch 20 is not monotone: it dips to $+0.384$ at epoch 5 before growing. The… |
| 506 | `04-alternatives.tex:149` | `5` | …epoch 20 is not monotone: it dips to $+0.384$ at epoch 5 before growing. The… |
| 507 | `04-alternatives.tex:153` | `1` | …on the shape---it depends on the epoch-1 magnitude, which is large and correctly signed. The si… |
| 508 | `04-alternatives.tex:153` | `six` | …-1 magnitude, which is large and correctly signed. The six-seed curve of Fig.~ confirms the penalty at every scor… |
| 509 | `04-alternatives.tex:161` | `two` | …The evidence, from two independent registrations. The first varied the… |
| 510 | `04-alternatives.tex:163` | `-0.613` | …+L1 on both the Ankara and European sets, with ORB at $-0.613 \pm 0.135$~px.… |
| 511 | `04-alternatives.tex:163` | `0.135` | …the Ankara and European sets, with ORB at $-0.613 \pm 0.135$~px.… |
| 512 | `04-alternatives.tex:164` | `Two` | …Two caveats travel with these numbers and are stated rathe… |
| 513 | `04-alternatives.tex:165` | `29` | …figure is a paired difference over the 29 chips where both arms matched, not over… |
| 514 | `04-alternatives.tex:166` | `53` | …the 53 chips where the L1-only arm matched at all; the AKAZE… |
| 515 | `04-alternatives.tex:166` | `11` | …L1-only arm matched at all; the AKAZE figure rests on 11 paired… |
| 516 | `04-alternatives.tex:167` | `-1.260` | …chips. And the mutual-information margin of $-1.260 \pm 0.261$ is a lower bound,… |
| 517 | `04-alternatives.tex:167` | `0.261` | …hips. And the mutual-information margin of $-1.260 \pm 0.261$ is a lower bound,… |
| 518 | `04-alternatives.tex:169` | `15.8\%` | …15.8\% of chips at its bound, censoring the worse arms harder… |
| 519 | `04-alternatives.tex:173` | `two` | …NCC template grid, and phase correlation, crossed with two band conversions and an… |
| 520 | `04-alternatives.tex:174` | `6,510` | …urban subset over 6,510 scored comparisons. The arm ordering is preserved in e… |
| 521 | `04-alternatives.tex:175` | `two` | …condition cell except two, both at the European urban subset under phase correla… |
| 522 | `04-alternatives.tex:176` | `one` | …one in each band conversion, and both far below the thresh… |
| 523 | `04-alternatives.tex:179` | `eight` | …arm's margin grew rather than shrank, in all eight set-by-conversion combinations.… |
| 524 | `04-alternatives.tex:181` | `two` | …The reading. The candidate is refuted by two registrations that share no matcher,… |
| 525 | `04-alternatives.tex:183` | `two` | …it is the reason this row is reported as two tests rather than one.… |
| 526 | `04-alternatives.tex:183` | `one` | …e reason this row is reported as two tests rather than one.… |
| 527 | `04-alternatives.tex:191` | `six` | …esign and needs no measurement. None of the registered six-seed positional contrasts compares a fine-tuned arm wi… |
| 528 | `04-alternatives.tex:192` | `four` | …the pretrained generator: all four arms are fine-tuned on identical pairs, so any… |
| 529 | `04-alternatives.tex:193` | `one` | …rencing improvement is common to them and cancels. The one registered contrast… |
| 530 | `04-alternatives.tex:199` | `86\%` | …attributed roughly 86\% of the European gain to scatter reduction rather than… |
| 531 | `04-alternatives.tex:210` | `one` | …peak in the wrong one, and that is true of any matcher that localises by cor… |
| 532 | `05-discussion.tex:44` | `601` | …BT.601 gray band against the standard references, the L1-only… |
| 533 | `05-discussion.tex:45` | `$0.593` | …positional error of $0.593 \pm 0.041$~px on 20 urban Ankara chips, each value the… |
| 534 | `05-discussion.tex:45` | `0.041` | …positional error of $0.593 \pm 0.041$~px on 20 urban Ankara chips, each value the mean of… |
| 535 | `05-discussion.tex:45` | `20` | …positional error of $0.593 \pm 0.041$~px on 20 urban Ankara chips, each value the mean of… |
| 536 | `05-discussion.tex:46` | `eight` | …eight stochastic draws per chip, better than the published g… |
| 537 | `05-discussion.tex:46` | `20` | …draws per chip, better than the published generator on 20 of 20 chips.… |
| 538 | `05-discussion.tex:46` | `20` | …per chip, better than the published generator on 20 of 20 chips.… |
| 539 | `05-discussion.tex:58` | `two` | …of two plausibility pressures, the adversarial term and a per… |
| 540 | `05-discussion.tex:59` | `six` | …is established separately as a positional penalty, at six seeds with the sign fixed in… |
| 541 | `05-discussion.tex:60` | `two` | …advance. Nothing is claimed about how the two combine. The mechanism was predicted: Cohen, Kligvasse… |
| 542 | `05-discussion.tex:73` | `two` | …number here is a proxy; the two matcher-independence registrations bound how much the… |
| 543 | `05-discussion.tex:78` | `1.9` | …ed. The perceptual loss was computed with torchmetrics 1.9.0 against the… |
| 544 | `05-discussion.tex:78` | `0` | …The perceptual loss was computed with torchmetrics 1.9.0 against the… |
| 545 | `05-discussion.tex:79` | `0.11` | …upstream's 0.11.0, and LPIPS implementations drift. Known-displacement… |
| 546 | `05-discussion.tex:79` | `0,` | …upstream's 0.11.0, and LPIPS implementations drift. Known-displacement re… |
| 547 | `05-discussion.tex:81` | `0.6` | …production render path, at a cost of roughly 0.6~px on forest-heavy chips. The harness of… |
| 548 | `05-discussion.tex:82` | `four` | …e descriptor-family matcher test was not preserved, so four of its registered parameters… |
| 549 | `05-discussion.tex:85` | `Five` | …Five limitations arose after the design was fixed. The lear… |
| 550 | `05-discussion.tex:87` | `one` | …chip-level, at one seed, and it tests the schedule on the non-adversarial… |
| 551 | `05-discussion.tex:91` | `six` | …ility statement details; the blur row now rests on the six-seed… |
| 552 | `05-discussion.tex:93` | `two` | …Section~IV-D, and two registered outputs of that package are permanently… |
| 553 | `05-discussion.tex:97` | `130` | …s free of post-treatment conditioning. The factorial's 130 chips are one… |
| 554 | `05-discussion.tex:97` | `one` | …-treatment conditioning. The factorial's 130 chips are one… |
| 555 | `05-discussion.tex:99` | `Three` | …tcher rows, never the registered positional contrasts. Three registrations were… |
| 556 | `05-discussion.tex:102` | `one` | …which one quantity vetoed ten, and a tie rule over four arms imp… |
| 557 | `05-discussion.tex:102` | `ten` | …which one quantity vetoed ten, and a tie rule over four arms implemented over five.… |
| 558 | `05-discussion.tex:102` | `four` | …which one quantity vetoed ten, and a tie rule over four arms implemented over five. In each… |
| 559 | `05-discussion.tex:102` | `five` | …ed ten, and a tie rule over four arms implemented over five. In each… |
| 560 | `05-discussion.tex:104` | `one` | …which way it cuts is indistinguishable from one adjusted to pass, and all three are… |
| 561 | `05-discussion.tex:104` | `three` | …s indistinguishable from one adjusted to pass, and all three are… |
| 562 | `05-discussion.tex:107` | `Two` | …Two caveats travel with results stated elsewhere. The null… |
| 563 | `05-discussion.tex:123` | `One` | …physical-measurement consumer pays for . One scope boundary: at 10~m the premise for a generated re… |
| 564 | `05-discussion.tex:123` | `10` | …measurement consumer pays for . One scope boundary: at 10~m the premise for a generated reference… |
| 565 | `06-data-availability.tex:6` | `502` | …The study repository (\url{https://github.com/mvy0502/gencp-validation}) holds, under \texttt{tubitak/docs/}… |
| 566 | `06-data-availability.tex:12` | `six` | …named: the six-seed block (per-chip residuals, surviving-point counts… |
| 567 | `06-data-availability.tex:13` | `five` | …edge ratios for all five arms at seeds 45--50, Section~III-A to III-D and III-F… |
| 568 | `06-data-availability.tex:13` | `45--50` | …edge ratios for all five arms at seeds 45--50, Section~III-A to III-D and III-F); the two-seed block… |
| 569 | `06-data-availability.tex:13` | `two` | …t seeds 45--50, Section~III-A to III-D and III-F); the two-seed block at seeds 43--44 and the hardware gate, the… |
| 570 | `06-data-availability.tex:13` | `43--44` | …III-A to III-D and III-F); the two-seed block at seeds 43--44 and the hardware gate, the registered poolability… |
| 571 | `06-data-availability.tex:14` | `43` | …comparison of Section~II-A, with its re-run of seed 43 (Section~II-A and III-C); the informative-mask test (S… |
| 572 | `06-data-availability.tex:14` | `43,` | …n~III-G); the warm-up and learning-rate probes at seed 43,… |
| 573 | `06-data-availability.tex:15` | `one` | …one set of runs read under two registrations, with their t… |
| 574 | `06-data-availability.tex:15` | `two` | …one set of runs read under two registrations, with their training-loss logs… |
| 575 | `06-data-availability.tex:16` | `six` | …(Section~II-A and III-J); the six-seed training-loss trend (Section~III-J); the epoch sw… |
| 576 | `06-data-availability.tex:17` | `24` | …behind the training-time curve, 24 cells at epochs 1, 2, 5 and 10 (Section~III-E), with… |
| 577 | `06-data-availability.tex:17` | `1,` | …behind the training-time curve, 24 cells at epochs 1, 2, 5 and 10 (Section~III-E), with… |
| 578 | `06-data-availability.tex:17` | `2,` | …behind the training-time curve, 24 cells at epochs 1, 2, 5 and 10 (Section~III-E), with… |
| 579 | `06-data-availability.tex:17` | `5` | …hind the training-time curve, 24 cells at epochs 1, 2, 5 and 10 (Section~III-E), with… |
| 580 | `06-data-availability.tex:17` | `10` | …he training-time curve, 24 cells at epochs 1, 2, 5 and 10 (Section~III-E), with… |
| 581 | `06-data-availability.tex:18` | `96` | …the 96 generator checkpoints it read held outside the reposit… |
| 582 | `06-data-availability.tex:20` | `260` | …behind Table~II; the 260 seed-independent rasters the edge-ratio measurement re… |
| 583 | `06-data-availability.tex:21` | `130` | …premise check (Section~III-L), 130 chip-level residuals and counts with its registration.… |
| 584 | `06-data-availability.tex:23` | `Three` | …Three things are not available, and are stated here rather t… |
| 585 | `06-data-availability.tex:25` | `six` | …corrected-georeferencing rows of Table~II: six of its seven registered checks and its veto… |
| 586 | `06-data-availability.tex:25` | `seven` | …corrected-georeferencing rows of Table~II: six of its seven registered checks and its veto… |
| 587 | `06-data-availability.tex:28` | `Two` | …cannot be re-run. Two of its registered outputs---a point-floor sensitivity… |
| 588 | `06-data-availability.tex:31` | `86\%` | …whether they ran and went unreported or never ran. The 86\% scatter decomposition cited in… |
| 589 | `06-data-availability.tex:33` | `four` | …e descriptor-family matcher test was not preserved, so four of its… |
| 590 | `06-data-availability.tex:37` | `26` | …ot a reproduction. The generated images produced up to 26 August 2026, the training checkpoints of the… |
| 591 | `06-data-availability.tex:37` | `2026,` | …duction. The generated images produced up to 26 August 2026, the training checkpoints of the… |
| 592 | `06-data-availability.tex:38` | `96` | …generating and confirmatory runs, and the 96 epoch checkpoints behind Fig.~ are held in… |
| 593 | `06-data-availability.tex:40` | `24` | …generated images of the 24 epoch cells scored on 13 September 2026 are not in tha… |
| 594 | `06-data-availability.tex:40` | `13` | …generated images of the 24 epoch cells scored on 13 September 2026 are not in that backup… |
| 595 | `06-data-availability.tex:40` | `2026` | …ed images of the 24 epoch cells scored on 13 September 2026 are not in that backup… |
| 596 | `06-data-availability.tex:41` | `one` | …and exist on one machine; this is stated so that the backup is not read… |
| 597 | `06-data-availability.tex:43` | `130` | …The 130 Ankara evaluation inputs were rendered from live map-A… |
