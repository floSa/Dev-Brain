---
role: notion
nom: Facteurs de Bayes et tailles d'effet
alias: [Facteurs de Bayes et tailles d'effet, facteur de Bayes, facteurs de Bayes, Bayes factor, BF, BF10, taille d'effet, tailles d'effet, effect size, d de Cohen, Cohen's d, g de Hedges, Hedges' g, eta carré, êta carré, omega carré, f² de Cohen, rapport de cotes, odds ratio, a priori JZS, Cauchy prior, paradoxe de Jeffreys-Lindley, Jeffreys-Lindley paradox, déclaration de l'ASA sur les p-valeurs, significativité statistique, e-values, ROPE]
categorie: stats/inference
domaines: [data-sci]
tags: [effect-size, hypothesis-testing, bayesian, p-value]
---

# Facteurs de Bayes et tailles d'effet

## Aperçu

- Deux réponses à une même limite de la p-valeur : elle dit **si** les données sont peu compatibles avec l'hypothèse nulle, ni **de combien** l'effet s'écarte de zéro, ni **dans quelle mesure** les données soutiennent une hypothèse plutôt qu'une autre.
- La **taille d'effet** mesure l'ampleur : un nombre, exprimé dans une unité ou standardisé, indépendant de la taille de l'échantillon.
- Le **facteur de Bayes** (BF) mesure la preuve relative : un rapport entre ce que deux hypothèses donnaient comme probabilité aux données observées.
- Complémentaires : une taille d'effet sans mesure de preuve ne dit pas si l'écart est réel ; un facteur de Bayes sans taille d'effet ne dit pas s'il est important.
- Ce que cette page ne répète pas : la mécanique d'un test et la p-valeur ([[Tests d'hypothèse]], [[Test t et ANOVA]]), le dimensionnement d'un échantillon ([[Analyse de puissance]]), la multiplicité des tests ([[Correction des tests multiples]]).

## Concepts clés

### Taille d'effet standardisée

- **d de Cohen**, deux groupes indépendants : écart de moyennes divisé par l'écart-type poolé (Lakens 2013, éq. 1) :
  $$d_s = \frac{\bar X_1 - \bar X_2}{\sqrt{\dfrac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}}}, \qquad d_s = t\sqrt{\tfrac1{n_1}+\tfrac1{n_2}}.$$
  La seconde forme permet de le retrouver depuis un $t$ publié ; si seul $N$ est connu, $d_s \approx 2t/\sqrt N$.
- **g de Hedges** : correction du biais de $d$, notable pour $n < 20$ (Lakens ; pingouin) :
  $$g = d\Big(1 - \frac{3}{4(n_1+n_2) - 9}\Big).$$
  Lakens recommande de rapporter $g$.
- **Plans appariés** : le dénominateur change, donc la valeur aussi (Lakens).
  - $d_z = M_{\mathrm{diff}} / S_{\mathrm{diff}} = t/\sqrt n$ ;
  - $d_{rm}$ corrige $d_z$ par la corrélation $r$ entre mesures ;
  - $d_{av}$ divise par la moyenne des écarts-types. Désaccord de formule : Lakens (éq. 10) divise par $(SD_1+SD_2)/2$, alors que le code de pingouin tient cette expression pour erronée et utilise $\sqrt{(s_1^2+s_2^2)/2}$, d'après Cumming (2012).
  - **Conséquence** : « $d = 0{,}5$ » ne désigne pas la même chose selon le plan. Toujours dire quelle variante.
- **Corrélation** : $r$ ou $r_{pb}$ ; lien avec $d$ : $r_{pb} = d_s / \sqrt{d_s^2 + (N^2-2N)/(n_1 n_2)}$ (Lakens, éq. 3).
- **Rapport de cotes** (*odds ratio*) pour des variables binaires. Conversion approchée (docstring pingouin, d'après Borenstein 2009) : $\mathrm{OR} = \exp(d\pi/\sqrt3)$.
- **Variance expliquée** en ANOVA : $\eta^2_p = \dfrac{F\,df_{\mathrm{eff}}}{F\,df_{\mathrm{eff}} + df_{\mathrm{err}}}$ (Lakens, éq. 13), et $\omega^2$ (éq. 14), moins biaisé. Lakens recommande $\eta^2_G$ ou $\eta^2_p$ et note que $\eta^2_p$ diffère entre plans intra et inter sujets.
- **$f$ et $f^2$** (Cohen) : $f = \sigma_m/\sigma$ pour l'ANOVA ; $f^2 = R^2/(1-R^2)$ pour la régression.

### Les seuils « petit, moyen, grand »

| Indice | Petit | Moyen | Grand |
|---|---|---|---|
| $d$ | 0,20 | 0,50 | 0,80 |
| $r$ | 0,10 | 0,30 | 0,50 |
| $f$ | 0,10 | 0,25 | 0,40 |
| $f^2$ | 0,02 | 0,15 | 0,35 |

(Cohen 1992, *A Power Primer*, table 1, qui reprend les conventions du livre de 1988. Repères pour $\eta^2$ : 0,01 / 0,06 / 0,14, rapportés par Lakens et par Schäfer et Schwarz comme tirés de 1988 ; non vérifiés dans le livre.)

- **Ce que Cohen disait réellement.** Dans l'article de 1992, il explique avoir voulu qu'un effet « moyen » soit visible à l'œil nu d'un observateur attentif ; « petit » nettement plus petit, mais pas trivial ; « grand » aussi loin au-dessus de moyen que petit en dessous. Ces définitions sont, écrit-il, subjectives et inchangées depuis l'édition de 1977. Un écart moyen vaut un demi-écart-type.
- Cohen 1988, p. 25 (rapporté par Schäfer et Schwarz, seconde main) : ces termes sont relatifs au domaine ; il recommandait de tirer ses repères des études antérieures du champ. L'expression « nécessairement un peu arbitraire » vient d'un article de 1962, non de 1988.
- **Lakens** juge ces valeurs arbitraires et à ne pas appliquer rigidement. **Schäfer et Schwarz (2019)** jugent les repères globaux inapplicables en l'état : sur 900 effets issus de publications sans préenregistrement contre 93 avec, la médiane de $r$ est de 0,36 contre 0,16 — une « inflation dramatique » selon eux, imputable au biais de publication.
- Désaccord laissé tel quel : Cohen pose des repères en insistant sur leur relativité ; ses lecteurs les emploient comme des seuils absolus.

### Intervalle de confiance sur la taille d'effet

- Une taille d'effet est une **estimation** ; son incertitude doit être donnée, comme pour tout paramètre ([[Intervalles de confiance]]).
- L'intervalle exact de $d$ passe par la loi $t$ **non centrale** (Lakens y renvoie, sans en donner la formule ; non lu à la source).
- Approximation employée par pingouin (`compute_esci`, d'après Hedges et Olkin 1985, non ouvert) : pour deux groupes indépendants,
  $$SE = \sqrt{\frac{n_x + n_y}{n_x n_y} + \frac{d^2}{2(n_x+n_y)}}, \qquad d \pm t_{\mathrm{crit}}\,SE,$$
  avec $n_x + n_y - 2$ degrés de liberté ; pour une corrélation, transformation de Fisher ($\operatorname{arctanh}$, $SE = 1/\sqrt{n-3}$). Le code précise lui-même que ses résultats diffèrent de ceux de JASP, qui utilise la loi $t$ non centrale.
- Un intervalle de $d$ large pour un échantillon petit est normal : le petit échantillon et l'effet « moyen » sont compatibles avec presque tout.

### Facteur de Bayes

- **Définition** (Kass et Raftery 1995, éq. 1 et 2) : rapport des **vraisemblances marginales** de deux hypothèses,
  $$B_{10} = \frac{p(D \mid H_1)}{p(D \mid H_0)}, \qquad p(D \mid H_k) = \int p(D \mid \theta_k, H_k)\,\pi(\theta_k \mid H_k)\,d\theta_k.$$
  Les paramètres sont **intégrés**, non maximisés : c'est ce qui sépare le BF d'un rapport de vraisemblances ordinaire, et ce qui le rend dépendant de l'a priori.
- **Lecture** : cotes a posteriori = $B_{10}$ × cotes a priori. À a priori égaux ($0{,}5$ chacun), le BF égale les cotes a posteriori. Un BF de 6 ne signifie pas « 6 chances sur 7 » sauf à ce que les deux hypothèses aient été jugées également probables d'avance.
- **Échelles de lecture**, tableau de Kass et Raftery (p. 777) :

  | $B_{10}$ | Libellé (K&R, échelle modifiée) |
  |---|---|
  | 1 à 3 | à peine digne d'être mentionné |
  | 3 à 20 | positif |
  | 20 à 150 | fort |
  | > 150 | très fort |

  L'échelle de Jeffreys, regroupée dans le même article, découpe en 1–3,2 / 3,2–10 / 10–100 / > 100. Kass et Raftery précisent que ces catégories sont une description grossière, pas une calibration. Aucune de ces échelles n'est une loi de la nature.
- **Approximation par le BIC** (Kass et Raftery, éq. 9 ; Wagenmakers 2007) : $\log B_{12} \approx S = \log p(D \mid \hat\theta_1, H_1) - \log p(D \mid \hat\theta_2, H_2) - \tfrac12 (d_1 - d_2) \log n$. L'erreur **relative** sur $\exp(S)$ reste $O(1)$ : l'approximation ne donne pas la valeur exacte, même pour de très grands échantillons. Avec un a priori « d'information unitaire », $\log B$ est approché à $O(n^{-1/2})$. Wagenmakers en tire $BF_{01} \approx \exp(\Delta \mathrm{BIC}_{10}/2)$ ; la formule exacte de l'article n'a pas pu être relue.
- **Calcul** : la vraisemblance marginale est souvent difficile. Cas particuliers analytiques (test $t$, corrélation, binomiale) ; sinon des méthodes de Monte Carlo, voir [[Monte Carlo et inférence variationnelle]]. Robert (2016) note qu'il n'existe pas de méthode universelle pour l'estimer.

### A priori et sensibilité : le JZS

- **Test $t$ bayésien de Rouder et al. (2009)** : taille d'effet $\delta = \mu/\sigma$ ; $H_0 : \delta = 0$ ; sous $H_1$, $\delta \sim \mathrm{Cauchy}$ d'échelle $r$ ; a priori de Jeffreys sur la variance, $p(\sigma^2) \propto 1/\sigma^2$. L'ensemble est dit « JZS ». Le BF se calcule depuis le seul $t$ et $N$.
- **Échelle $r$** : plus elle est grande, plus le BF soutient $H_0$ — l'alternative devient plus diffuse, donc plus « gaspilleuse ». Rouder et al. posent $r=1$ ; le package R **BayesFactor** a depuis adopté $\sqrt2/2 \approx 0{,}707$ par défaut (`"medium"`, contre `"wide"` = 1 et `"ultrawide"` = $\sqrt2$), et pingouin aussi. Désaccord de valeur par défaut laissé tel quel : pour retrouver les chiffres de l'article de 2009 il faut fixer $r=1$.
- Rouder et al. recommandent de fixer $r$ **avant** l'analyse et de s'appuyer sur la connaissance du domaine quand elle existe ; $r \approx 0{,}5$ pour des effets attendus petits.
- **Paradoxe de Jeffreys–Lindley** : quand la variance de l'a priori sur $\delta$ tend vers l'infini, le BF soutient $H_0$ sans borne. Rouder et al. en concluent qu'un a priori arbitrairement diffus est à proscrire.
- **Aller plus loin sur la sensibilité** (résumés lus) :
  - Lovric (arXiv 2511.22152, novembre 2025) : pour tout résultat bilatéral significatif à 5 %, il existe des variances a priori qui font indiquer au BF la preuve pour $H_1$ avec un choix et pour $H_0$ avec un autre, **à des tailles d'échantillon réalistes** — contrairement au paradoxe classique, asymptotique. Soumis à *Biometrika*, non publié à la date de lecture.
  - Bartoš, Wagenmakers, Marsman, van den Bergh (arXiv 2604.21596, avril 2026) : reconstruire toute la courbe de sensibilité d'un BF à partir d'un seul ajustement supplémentaire, par un rapport de densités de Savage–Dickey.
- **Pratique** : rapporter le BF **avec** son échelle $r$ et la courbe de sensibilité, jamais le BF seul.

### Critiques de la significativité statistique

- **Déclaration de l'ASA** (Wasserstein et Lazar, 2016), six principes :
  1. une p-valeur peut indiquer l'incompatibilité des données avec un modèle spécifié ;
  2. elle ne mesure ni la probabilité que l'hypothèse soit vraie, ni celle que les données soient dues au seul hasard ;
  3. les conclusions ne devraient pas reposer sur le seul franchissement d'un seuil ;
  4. une inférence correcte exige rapport complet et transparence ;
  5. une p-valeur ne mesure ni la taille d'un effet ni l'importance d'un résultat ;
  6. seule, elle ne fournit pas une bonne mesure de preuve.
  La section « autres approches » de la déclaration cite intervalles, méthodes bayésiennes, rapports de vraisemblance ou facteurs de Bayes, taux de fausses découvertes, et précise que toutes reposent sur d'autres hypothèses. Elle ne désigne aucun remplaçant.
- **Wasserstein, Schirm, Lazar (2019)**, éditorial d'un numéro spécial de 43 articles : n'a été vu que par ses métadonnées et par des commentaires secondaires. L'abandon de l'expression « statistiquement significatif » y serait recommandé ; non vérifié à la source.
- **Wagenmakers (2007)** : trois problèmes de la p-valeur — elle dépend de données jamais observées, d'intentions subjectives (règle d'arrêt), et ne quantifie pas la preuve. Son remède : une sélection de modèle par BIC.
- **Lakens (2013)** : rapporter les tailles d'effet pour faciliter les méta-analyses et le calcul de puissance, et noter que $d$ varie avec le plan.
- Les remèdes proposés **ne concordent pas** :
  - Wagenmakers : le BIC ;
  - Kruschke et Liddell : l'estimation bayésienne et la **région d'équivalence pratique** (ROPE), dont la décision n'est pas liée à celle par BF ;
  - Tendeiro et Kiers (2019) : les probabilités a posteriori de modèles plutôt que les BF (résumé seul lu) ;
  - Robert (2016) : l'estimation de mélange ;
  - Chugg, Ramdas, Grünwald (arXiv 2603.24421, 2026, *Synthese*) : les **e-values**, qui se combinent entre études et supportent l'arrêt optionnel ;
  - la déclaration de l'ASA : un panorama, sans trancher.

### Critiques des facteurs de Bayes

- **Dépendance à l'a priori** : le BF pèse l'a priori sur les modèles **et** celui sur les paramètres (Robert 2016). Une alternative plus diffuse est pénalisée.
- **Échelle** : le BF n'a pas l'échelle d'une probabilité a posteriori ; son interprétation demande une calibration (Robert).
- **A priori impropres** : problématiques pour un BF, la constante arbitraire ne se simplifie plus (Robert).
- **Cotes a priori** : Kruschke et Liddell notent que le BF seul n'est utile qu'à cotes a priori égales. Exemples cités : une hypothèse de perception extra-sensorielle dont la nulle est quasi certaine, un test diagnostique pour une maladie rare.
- **Seuils d'action** : la littérature en propose de différents — 3 (Dienes), 6 pour l'exploration et 10 pour la confirmation (Schönbrodt et al.), d'après Kruschke et Liddell (seconde main). L'échelle « 3 / 10 / 30 » que ces auteurs attribuent à Jeffreys, Kass et Raftery et Wetzels et al. n'est pas celle de Kass et Raftery (3 / 20 / 150) ; non vérifié à la source.
- Désaccord : Tendeiro et Kiers défendent des critiques de fond du test bayésien d'une nulle ponctuelle ; une réponse (van Ravenzwaaij et Wagenmakers, 2019, *Advantages Masquerading as « Issues »*, PsyArXiv, titre seul vu) les conteste. Laissé tel quel.

## Les maths, simplement

- $d$ : « combien d'écarts-types séparent les deux moyennes ». $d = 0{,}5$ : les moyennes sont distantes d'un demi-écart-type.
- $B_{10}$ : « par combien les données multiplient mes cotes en faveur de $H_1$ ». $B_{10} = 1$ : rien ne bouge.
- Lien entre les deux : le BF de Rouder et al. est calculé pour une loi a priori sur **la taille d'effet standardisée** $\delta$ ; fixer $r$, c'est dire quelle taille d'effet on jugeait plausible avant les données.
- Une p-valeur de 0,05 sur un grand échantillon peut correspondre à un BF proche de 1 : même résultat « significatif », peu de preuve (voir *Travaux récents*, eJAB).

## En pratique

- **Toujours rapporter** : la taille d'effet **avec son intervalle**, le plan (indépendant ou apparié), la variante ($d_s$, $d_z$, $g$), et la p-valeur ou le BF **avec leurs hypothèses** (échelle $r$, a priori choisi).
- **Choisir les seuils d'« important » par le domaine**, pas par Cohen : un $d$ de 0,2 peut être majeur (effet sur des millions d'utilisateurs) ou négligeable.
- **Ne pas annoncer « preuve de l'absence »** avec un BF sans dire pour quel a priori : un BF en faveur de $H_0$ dépend de l'échelle $r$ choisie.
- **Combiner** : BF et ROPE répondent à deux questions différentes (« les données soutiennent-elles $H_1$ plutôt que $H_0$ ? », « l'effet est-il pratiquement nul ? »).
- **Pour planifier**, la puissance se raisonne sur une taille d'effet **plausible**, non sur un seuil de Cohen : voir [[Analyse de puissance]].
- **Avec plusieurs tests**, les corrections de [[Correction des tests multiples]] visent les p-valeurs. Raisonnement propre à cette page, sans source lue : un BF ne contrôle pas le même risque, et la multiplicité des comparaisons se traite par les a priori sur les hypothèses plutôt que par un seuil.

### En Python

- **pingouin** (version 0.7.0, 2026-09-26, licence **GPL-3.0**, Python ≥ 3.11, relevé sur PyPI ; le code lu est celui de la branche `main`, qui peut dépasser cette version) :
  - `compute_effsize(x, y, paired=False, eftype="cohen")` : `cohen`, `cohen_dz`, `hedges`, `r`, `pointbiserialr`, `eta_square`, `odds_ratio`, `AUC`, `CLES` ;
  - `compute_effsize_from_t(tval, nx, ny, N, eftype)` : $d$ depuis un $t$ publié ;
  - `compute_esci(stat, nx, ny, paired, eftype, confidence=0.95)` : intervalle **approché**, pas de $t$ non centrale ;
  - `convert_effsize(ef, input_type, output_type, nx, ny)` : $d \leftrightarrow r_{pb}$, $\eta^2$, OR, AUC (d'après Rosenthal, Cohen, Borenstein, Ruscio) ;
  - `bayesfactor_ttest(t, nx, ny, paired, alternative="two-sided", r=0.707)` : BF10 JZS de Rouder et al. ; **bilatéral seulement** ;
  - `bayesfactor_pearson(r, n, alternative="two-sided", method="ly", kappa=1.0)` et `bayesfactor_binom(k, n, p=0.5, a=1, b=1)`.
  - Les pages HTML de la documentation ont répondu en 404 pendant cette recherche : l'API vient du code et des docstrings.
- **scipy.stats** (1.18.1, BSD-3) : **aucune fonction** de d de Cohen, d'$\eta^2$ ni de facteur de Bayes dans la documentation lue (v1.18.0). Présents : `contingency.odds_ratio` (estimation conditionnelle par défaut, ou `kind='sample'`, avec intervalle de confiance), `contingency.association` (V de Cramér, T de Tschuprow, Pearson), `bayes_mvs` (intervalles de crédibilité sur moyenne, variance et écart-type : **pas** un facteur de Bayes). Une proposition d'ajout de $d$ aux résultats du test $t$ est en discussion (septembre 2025), sans fusion constatée.
- **R** : le package **BayesFactor** (0.9.12-4.8, GPL-2) est la référence pour les BF d'un test $t$, d'une ANOVA et d'une régression ; JASP en est l'interface graphique, et c'est son calcul que pingouin cite comme différent pour l'intervalle de $d$.

### Travaux récents

Prépublications des 12 derniers mois, lues au niveau du résumé :

- Chugg, Ramdas, Grünwald — *E-values as statistical evidence: A comparison to Bayes factors, likelihoods, and p-values* (arXiv 2603.24421, mars 2026 ; *Synthese*) : e-values et e-processes comme mesure de preuve qui se combine entre études et gère l'arrêt optionnel.
- Lovric — *The Bayes Factor Reversal Paradox* (arXiv 2511.22152, novembre 2025) : voir plus haut.
- Bartoš, Wagenmakers, Marsman, van den Bergh — *Efficient Bayes Factor Sensitivity Analysis via Posterior Density Ratios* (arXiv 2604.21596, avril 2026).
- Velidi et al. — eJAB, approximation à une ligne d'un BF objectif de Jeffreys depuis la p-valeur, la taille d'échantillon et la dimension (arXiv 2510.10358, octobre 2025) : sur 71 126 résultats d'essais cliniques, environ 35,5 % des résultats significatifs à 5 % n'offrent une preuve que « anecdotique » selon cette mesure.

Plusieurs autres résumés ont été retrouvés (BF pour méta-analyses, plans séquentiels à BF, estimation du biais de publication) mais ne sont pas repris ici. Aucune source récente n'a été retrouvée sur la dépendance de $d$ au plan expérimental ; Lakens 2013 reste la référence lue.

## Approches voisines & alternatives

- [[Tests d'hypothèse]] — le cadre de la p-valeur dont ces deux outils corrigent les limites ; cette page donne le BF comme alternative.
- [[Test t et ANOVA]] — où $d$, $\eta^2$ et le BF du test $t$ se calculent le plus souvent.
- [[Analyse de puissance]] — raisonne sur une taille d'effet plausible ; le choix de cette taille est le point faible commun.
- [[Correction des tests multiples]] — contrôle l'erreur sur des p-valeurs ; ne s'applique pas telle quelle à des BF.
- [[Intervalles de confiance]] — l'intervalle de la taille d'effet en est un cas ; l'intervalle de crédibilité en est l'analogue bayésien.
- [[Inférence bayésienne]] — le cadre dans lequel le BF est défini ; l'a priori y est un choix déclaré.
- [[A priori conjugués]] — un a priori de forme commode, mais le BF exige de savoir intégrer.
- [[Monte Carlo et inférence variationnelle]] — calculer une vraisemblance marginale quand l'intégrale n'est pas analytique.
- [[pingouin]] — tailles d'effet, intervalles approchés, BF du test $t$, de la corrélation et de la binomiale.
- [[scipy.stats]] — rapport de cotes et mesures d'association ; ni $d$ ni BF.

## Pour aller plus loin

- Cohen (1988), *Statistical Power Analysis for the Behavioral Sciences*, 2e éd., Erlbaum/Routledge — livre non ouvert ; fiche éditeur seule. Les valeurs de $d$, $r$, $f$, $f^2$ ci-dessus viennent de Cohen (1992).
- Cohen (1992), *A Power Primer*, Psychological Bulletin 112(1) : 155–159 — lu (scan).
- Kass et Raftery (1995), *Bayes Factors*, JASA 90(430) : 773–795 : <https://doi.org/10.1080/01621459.1995.10476572> — lu (éq. 1, 2, 9 ; tables p. 777).
- Wasserstein et Lazar (2016), *The ASA's Statement on p-Values: Context, Process, and Purpose*, The American Statistician 70(2) : <https://doi.org/10.1080/00031305.2016.1154108> — lu.
- Wasserstein, Schirm, Lazar (2019), *Moving to a World Beyond « p < 0.05 »*, The American Statistician 73(sup1) : <https://doi.org/10.1080/00031305.2019.1583913> — résumé seul.
- Wagenmakers (2007), *A practical solution to the pervasive problems of p values*, Psychonomic Bulletin & Review 14(5) : <https://doi.org/10.3758/BF03194105> — lu.
- Lakens (2013), *Calculating and reporting effect sizes to facilitate cumulative science: a practical primer for t-tests and ANOVAs*, Frontiers in Psychology 4:863 : <https://doi.org/10.3389/fpsyg.2013.00863> — lu.
- Rouder, Speckman, Sun, Morey, Iverson (2009), *Bayesian t tests for accepting and rejecting the null hypothesis*, Psychonomic Bulletin & Review 16(2) : <https://doi.org/10.3758/PBR.16.2.225> — lu.
- Robert (2016), *The expected demise of the Bayes factor*, Journal of Mathematical Psychology 72 : <https://arxiv.org/abs/1506.08292> — lu (préprint).
- Kruschke et Liddell (2018 ; en ligne en 2017), *The Bayesian New Statistics: Hypothesis testing, estimation, meta-analysis, and power analysis from a Bayesian perspective*, Psychonomic Bulletin & Review 25(1) : <https://doi.org/10.3758/s13423-016-1221-4> — lu (version du 15 novembre 2016).
- Tendeiro et Kiers (2019), *A review of issues about null hypothesis Bayesian testing*, Psychological Methods 24(6) : <https://doi.org/10.1037/met0000221> — résumé seul.
- Morey et Rouder (2011), *Bayes factor approaches for testing interval null hypotheses*, Psychological Methods 16(4) : <https://doi.org/10.1037/a0024377> — métadonnées seules. Gelman et Rubin (1995), *Avoiding Model Selection in Bayesian Social Research*, Sociological Methodology 25 — métadonnées seules.
- Schäfer et Schwarz (2019), *The Meaningfulness of Effect Sizes in Psychological Research: Differences Between Sub-Disciplines and the Impact of Potential Bias*, Frontiers in Psychology 10:813 : <https://doi.org/10.3389/fpsyg.2019.00813> — lu.
- Documentation : le code de [pingouin](https://github.com/raphaelvallat/pingouin) (`effsize.py`, `bayesian.py`), la [référence scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html), le [paquet R BayesFactor](https://cran.r-project.org/web/packages/BayesFactor/BayesFactor.pdf).
- Connexions brain : [[Tests d'hypothèse]], [[Analyse de puissance]], [[Correction des tests multiples]], [[pingouin]], [[scipy.stats]].
