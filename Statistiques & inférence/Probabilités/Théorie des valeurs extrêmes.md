---
role: notion
nom: Théorie des valeurs extrêmes
alias: [Théorie des valeurs extrêmes, valeurs extrêmes, extreme value theory, EVT, loi des extrêmes, GEV, loi GEV, generalized extreme value, loi de Pareto généralisée, GPD, generalized Pareto, POT, peaks over threshold, dépassements de seuil, block maxima, maxima par blocs, niveau de retour, return level, période de retour, return period, indice de queue, tail index, estimateur de Hill, Fisher-Tippett-Gnedenko, Pickands-Balkema-de Haan, loi de Gumbel, loi de Fréchet, SPOT, DSPOT]
categorie: stats/probabilite
domaines: [data-sci]
tags: [probability, statistical-inference, anomaly-detection, reliability]
---

# Théorie des valeurs extrêmes

## Aperçu

- Branche des probabilités et de la statistique qui modélise **le comportement des valeurs les plus grandes** (ou les plus petites) d'un échantillon : le maximum d'une année, les dépassements d'un seuil élevé.
- Raison d'être : **extrapoler au-delà des données**. Estimer la crue centennale avec trente ans de relevés, la panne qu'aucun historique n'a encore montrée, le seuil au-delà duquel un capteur est anormal.
- Un résultat de convergence joue ici le rôle que le [[Théorème central limite]] joue pour les moyennes : la moyenne tend vers une gaussienne, le maximum tend vers l'une des trois familles ci-dessous.
- Les extrêmes ne se déduisent pas du centre de la distribution. Une loi ajustée sur l'ensemble des données est guidée par la masse centrale et décrit mal la queue ; la théorie des valeurs extrêmes ajuste **la queue seule**.
- Les [[Inégalités de concentration]] donnent des bornes valables pour toute loi dans une classe, souvent lâches. Ici, un modèle paramétrique de la queue, estimé sur les données.

## Concepts clés

### Maxima par blocs et loi GEV

- Découper la série en blocs de même durée (une année, une saison) et retenir le **maximum de chaque bloc**.
- **Théorème de Fisher–Tippett–Gnedenko.** S'il existe des suites $a_n > 0$ et $b_n$ telles que $(\max_i X_i - b_n)/a_n$ converge en loi vers une loi non dégénérée $G$ (variables i.i.d.), alors $G$ est de la famille GEV (formulation reprise de Gardes et Girard).
- Loi **GEV** à trois paramètres (position $\mu$, échelle $\sigma$, forme $\xi$) :
  $$G(z) = \exp\Big\{-\Big[1 + \xi\,\tfrac{z-\mu}{\sigma}\Big]_+^{-1/\xi}\Big\}, \quad \xi \ne 0 ; \qquad G(z) = \exp\{-e^{-(z-\mu)/\sigma}\}, \quad \xi = 0.$$
- Le signe de $\xi$ fixe le type :

  | $\xi$ | Famille | Queue |
  |---|---|---|
  | $> 0$ | Fréchet | lourde, $P(X > x) \sim x^{-1/\xi}$ |
  | $= 0$ | Gumbel | exponentielle |
  | $< 0$ | Weibull « renversée » | **bornée** : borne supérieure $\mu - \sigma/\xi$ |

- Moments (d'après Wikipédia, source secondaire) : la moyenne est finie si $\xi < 1$, la variance si $\xi < 1/2$.
- Fisher et Tippett (1928) relèvent déjà, dans leur résumé, que la convergence vers la forme limite est **très lente** pour la loi normale ; l'ajustement d'une GEV à des blocs trop courts en hérite.

### Dépassements de seuil et loi de Pareto généralisée

- Retenir **tous les dépassements** d'un seuil élevé $u$, non plus un seul point par bloc : plus de données utilisées, et un seuil à choisir.
- **Théorème de Pickands–Balkema–de Haan.** Sous des conditions faibles, la loi des excès $Y - u$ sachant $Y > u$, mise à l'échelle, tend vers une **loi de Pareto généralisée** (GPD) quand $u$ approche le point terminal de la loi. Pickands (1975) et Balkema et de Haan (1974) l'ont établi ; Siffer et al. l'énoncent comme équivalent à l'appartenance au domaine d'attraction de la GEV.
- Loi GPD des excès, $\xi$ **identique** à celui de la GEV :
  $$H(x) = 1 - \Big[1 + \xi\,\tfrac{x-u}{\sigma_u}\Big]_+^{-1/\xi}, \qquad \xi = 0 : \ 1 - e^{-(x-u)/\sigma_u}.$$
  Le lien avec la GEV : $\sigma_u = \sigma + \xi(u - \mu)$ (extRemes 2.0).
- **Stabilité par changement de seuil** (Scarrott et MacDonald) : pour $v > u$, $\sigma_v = \sigma_u + \xi(v - u)$, et $\xi$ ne change pas. C'est ce qui permet de **choisir** le seuil : la forme doit rester stable au-dessus du bon seuil.
- Probabilité de dépassement d'un niveau $x > u$ : $\Pr(X > x) = \zeta_u\,[1 - H(x)]$, avec $\zeta_u = \Pr(X > u)$ (représentation « Poisson–GPD »).

### Indice de queue

- $\xi$ est l'**indice de queue** (ou indice des valeurs extrêmes). Sa valeur décide de tout : queue bornée, exponentielle, ou en loi de puissance.
- **Estimateur de Hill** (pour $\xi > 0$), sur les $k$ plus grandes statistiques d'ordre $X_{n-k+1,n} \le \dots \le X_{n,n}$ :
  $$\hat\xi^{H}_{k,n} = \frac1k \sum_{i=1}^{k} \ln X_{n-i+1,n} - \ln X_{n-k,n}.$$
  Convergent si $k \to \infty$ et $k/n \to 0$ ; Hill (1975) le présente pour des queues de type Zipf.
- **Estimateur de Pickands**, valable pour tout $\xi \in \mathbb R$ et invariant par changement d'échelle et de position :
  $$\hat\xi^{P}_{k,n} = \frac{1}{\ln 2}\,\ln \frac{X_{n-k+1,n} - X_{n-2k+1,n}}{X_{n-2k+1,n} - X_{n-4k+1,n}}, \qquad k \le n/4.$$
- Estimateur des **moments** (Dekkers, Einmahl, de Haan, 1989) : valable dans les trois domaines ; formule non vérifiée à la source.
- Tous dépendent d'un nombre $k$ de points de queue à choisir, et c'est le même problème que le seuil (voir *Pièges*).

### Niveaux et périodes de retour

- Le **niveau de retour** $z_p$ est le niveau dépassé en moyenne une fois toutes les $1/p$ périodes. Sur les maxima annuels, c'est la valeur qu'un maximum annuel dépasse avec probabilité $p$ chaque année.
- Par blocs (extRemes, éq. 4), avec $y_p = -1/\ln(1-p)$ :
  $$z_p = \mu + \tfrac{\sigma}{\xi}\big(y_p^{\xi} - 1\big) \quad (\xi \ne 0) ; \qquad \mu + \sigma \ln y_p \quad (\xi = 0).$$
- Par dépassements (extRemes, éq. 7), valeur dépassée en moyenne une fois toutes les $m$ observations :
  $$x_m = u + \tfrac{\sigma_u}{\xi}\big[(m\,\zeta_u)^{\xi} - 1\big] \quad (\xi \ne 0) ; \qquad u + \sigma_u \ln(m\,\zeta_u) \quad (\xi = 0).$$
- Pour $\xi > 0$, le quantile extrême de Weissman (Belzile et Davison) : $\hat Q(1-p) = Y_{(n-n_u)}\,\{n_u/(pn)\}^{\hat\xi}$.
- **« Période de retour de cent ans » n'est pas « une fois par siècle ».** Probabilité d'au moins un dépassement en $n$ années pour une période $T$ : $1 - (1 - 1/T)^n$ ; pour $n = T$, environ 63 %. La documentation de pyextremes cite 39,5 % pour un événement centennal sur 50 ans.
- **Intervalles** (extRemes 2.0) : approximation normale (méthode delta), **vraisemblance profilée**, bootstrap paramétrique. L'intervalle profilé est asymétrique : sur l'exemple du texte, il est décalé de quelques degrés vers le haut par rapport à l'approximation normale, parce que la variance d'un niveau de retour croît vite avec $\xi$.

### Usages

- **Hydrologie** : l'application d'origine. Siffer et al. rappellent la tempête de 1953 en mer du Nord (plus de 1800 morts aux Pays-Bas) comme motivation du dimensionnement des digues.
- **Fiabilité et pannes** : durées de vie extrêmes, charges maximales. Aucune source dédiée n'a été ouverte pour cette page ; voir [[Analyse de survie]] pour le cadre voisin, et la section *Introuvable*.
- **Finance et risque** : McNeil et Frey (2000) combinent un filtre GARCH et la queue GPD des innovations pour estimer VaR et *expected shortfall* conditionnels (résumé seul lu).
- **Détection d'anomalies industrielles** : fixer **automatiquement** un seuil d'alerte sans supposer de loi pour le corps de la distribution. Siffer, Fouque, Termier et Largouët (KDD 2017) en font **SPOT** pour un flux de mesures :
  - calibrer sur les $n \ge 1000$ premières valeurs : seuil initial $t$ égal au quantile empirique à 98 %, ajustement d'une GPD sur les excès par maximum de vraisemblance ;
  - fixer un **risque** $q$, seul paramètre principal, et en tirer le seuil d'alerte $z_q$ ;
  - un point au-dessus de $z_q$ est une anomalie et n'entre pas dans le modèle ; un point entre $t$ et $z_q$ s'ajoute aux pics et met à jour $z_q$ ;
  - **DSPOT** : applique SPOT aux écarts à une moyenne glissante, pour une série dont le niveau dérive.
  - Les auteurs supposent des observations i.i.d. et citent le cas dépendant et le cas multivarié comme perspectives. Ils jugent le seuil choisi par graphe d'excès moyen moins stable.
- Pour le cadre général de la détection sur séries, voir [[Time series anomaly detection]].

### Pièges

- **Choix du seuil** : un seuil trop haut laisse peu de dépassements et une grande variance ; trop bas, l'approximation asymptotique est fausse et le biais s'installe (Scarrott et MacDonald). Exemple relevé dans leur revue : deux seuils tous deux « admissibles » donnent $\hat\xi = 0{,}21$ et $0{,}003$. Le même problème touche le $k$ de Hill.
  - Diagnostics usuels : graphe de l'**excès moyen** $E[X - u \mid X > u] = \sigma_u/(1-\xi)$, linéaire en $u$ de pente $\xi/(1-\xi)$ (pour $\xi < 1$) ; stabilité des paramètres en fonction du seuil. Coles reconnaît leur lecture délicate.
  - Belzile et Davison (arXiv 2606.28540, juin 2026) passent en revue **plus de quarante procédures** de sélection du seuil et en classent par simulation les plus prometteuses : l'existence d'un tel catalogue dit que la question n'est pas réglée.
- **Dépendance sérielle** : les dépassements arrivent en grappes. L'hypothèse i.i.d. est plausible pour de grands blocs, rarement pour des dépassements. Parades : **déclustering** (par blocs de silence ou par intervalles), et **indice extrémal** $\theta \in (0,1]$, inverse de la taille moyenne limite des grappes (extRemes cite $\theta \approx 0{,}40$ sur un exemple de températures à Phoenix).
- **Séries courtes** : peu de blocs, donc un $\hat\xi$ très variable et des niveaux de retour très incertains. Martins et Stedinger (2000) notent l'instabilité des estimateurs du maximum de vraisemblance de la GEV en petit échantillon et proposent une version pénalisée par un a priori sur la forme. Je n'ai pas lu de chiffre quantitatif sur cette variance dans une source ouverte.
- **Non-stationnarité** : la tendance du climat rend suspecte une GEV à paramètres constants (Milly et al., 2008, résumé seul). Les paramètres peuvent dépendre du temps ou de covariables ; extrapoler une tendance hors des données est jugé risqué par les auteurs d'extRemes.
- **Queues lourdes** : si $\xi \ge 1/2$, la variance est infinie ; si $\xi \ge 1$, la moyenne l'est aussi. Un modèle qui compte sur ces moments casse.
- **Données manquantes** : les ignorer biaise les paramètres et **sous-estime** les niveaux de retour (Simpson et Northrop, 2025).
- **Blocs ou dépassements** : la sagesse reçue veut que les dépassements soient plus efficaces. Bücher et Zhou (2018) la nuancent : selon le processus générateur l'une ou l'autre peut gagner, et avec dépendance sérielle les dépassements conviennent mieux aux quantiles, les blocs aux niveaux de retour. Je n'ai lu que leur résumé.

## Les maths, simplement

- $\xi$ est l'unique paramètre de **forme**, et la **seule** quantité qui pilote l'extrapolation : un niveau de retour croît comme $T^{\xi}$ quand $\xi > 0$ (déduit des formules ci-dessus), se stabilise sous une borne quand $\xi < 0$.
- Pourquoi ces trois familles : le maximum de $n$ variables a pour fonction de répartition $F^n$ ; chercher une loi limite après normalisation $(a_n, b_n)$ ne laisse que Gumbel, Fréchet, Weibull, réunies par un seul paramètre $\xi$ (théorème de Fisher–Tippett–Gnedenko).
- Les deux approches sont deux visages du même objet : blocs → GEV, dépassements → GPD, avec le même $\xi$.
- **Paramétrage dans scipy.stats** (vérifié par calcul : les fonctions de répartition coïncident aux décimales) :
  - `genextreme` utilise $c = -\xi$. Un `c > 0` désigne donc une queue **bornée** (Weibull), un `c < 0` une queue lourde (Fréchet). La documentation signale que d'autres logiciels adoptent la convention opposée.
  - `genpareto` utilise $c = \xi$, **même signe**. C'est `genextreme` qui est inversé, pas `genpareto`.

## En pratique

- **Démarche** : tracer la série et regarder la dépendance → choisir blocs (données périodiques, séries longues) ou dépassements (séries plus courtes) → choisir le seuil par les graphes de stabilité → ajuster par maximum de vraisemblance → vérifier l'ajustement (QQ-plot, graphe de niveaux de retour) → calculer les niveaux de retour **avec intervalle**.
- **Toujours** donner l'intervalle d'un niveau de retour, et préférer la vraisemblance profilée à l'approximation normale.
- **Contrôler le résultat contre un modèle ajusté autrement** : blocs et dépassements doivent donner des $\hat\xi$ voisins ; la documentation de pyextremes recommande de recouper le résultat par POT avec une GEV sur maxima par blocs.
- **Ne pas extrapoler trop loin** : un niveau de retour de 1000 ans estimé sur 30 ans repose entièrement sur $\hat\xi$.

### En Python

- **scipy.stats** (1.18.1, 2026-08-21, relevé sur PyPI) : [[scipy.stats]] fournit `genextreme` et `genpareto` avec `fit`, `ppf`, `cdf`, `sf` ; voir le paramétrage ci-dessus. Aucune aide au choix du seuil ni au déclustering.
- **pyextremes** (2.5.0, 2026-02-19, MIT, Python ≥ 3.9, relevé sur PyPI) : classe `EVA` ; `get_extremes('BM' ou 'POT', …)`, `fit_model` (MLE, Emcee, L-moments, MOM), `get_return_value` qui renvoie la valeur et un intervalle par bootstrap, graphes `plot_mean_residual_life`, `plot_parameter_stability`, `plot_threshold_stability`. Les distributions sont celles de scipy : les paramètres de `genextreme` gardent donc $c = -\xi$. La documentation n'a pas pu être lue en entier (certaines pages en erreur).
- **R**, à titre de référence : `extRemes` (`fevd`, `decluster`, `extremalindex`) est décrit dans Gilleland et Katz (2016) ; `evd` et `ismev` n'ont pas été ouverts.
- **SPOT** : le dépôt des auteurs est cité dans l'article ; son état n'a pas été vérifié. `ads-evt` sur PyPI est une réimplémentation tierce, non officielle (version 0.0.4, 2022).

### Travaux récents

Prépublications des 12 derniers mois, lues au niveau du résumé :

- Belzile et Davison — *Choosing the threshold in extreme value analysis* (arXiv 2606.28540, juin 2026) : revue de plus de quarante méthodes de sélection du seuil, simulations, exemple de pluies à Padoue.
- Neves et Xu — *A hybrid-Hill estimator enabled by heavy-tailed block maxima* (arXiv 2512.19338, décembre 2025) : estimateur de type Hill à partir de maxima par blocs ; une variante à biais réduit est annoncée meilleure que le maximum de vraisemblance sur maxima par blocs.
- Simpson et Northrop — *Accounting for missing data when modelling block maxima* (arXiv 2512.15429, décembre 2025 ; *Environmetrics* 2026) : vraisemblance tenant compte de la part de données manquantes par bloc.
- Engelke, Gnecco, Sabourin — *Extrapolation in Statistical Learning with Extreme Value Theory* (arXiv 2605.01909, mai 2026) : revue du lien entre apprentissage statistique et valeurs extrêmes, détection d'anomalies comprise.

D'autres résumés (régression GEV bayésienne non stationnaire sur températures CMIP6, génération profonde d'événements de queue multivariés) ont été retrouvés mais ne sont pas repris ici.

## Approches voisines & alternatives

- [[Théorème central limite]] — le résultat jumeau pour les moyennes ; les extrêmes ont leurs propres lois limites.
- [[Inégalités de concentration]] — bornes sur la queue valables sans modèle, plus lâches ; la théorie des extrêmes les remplace par un modèle paramétrique de la queue.
- [[Time series anomaly detection]] — le cadre où SPOT fixe un seuil ; la théorie des extrêmes en est une brique, pas la seule.
- [[Maximum de vraisemblance]] — la méthode d'ajustement par défaut de la GEV et de la GPD ; instable sur peu de blocs.
- [[Intervalles de confiance]] et [[Bootstrap]] — pour l'incertitude d'un niveau de retour ; l'approximation normale y est mauvaise.
- [[Analyse de survie]] — voisin pour les durées de vie et les pannes ; elle modélise le temps jusqu'à l'événement, non l'amplitude extrême.
- [[Loi des grands nombres]] — fonde l'estimation d'un centre, hors sujet pour une queue.
- [[Stationarity]] — l'hypothèse implicite d'une GEV à paramètres constants.
- [[scipy.stats]] — `genextreme` et `genpareto`.

## Pour aller plus loin

- Fisher et Tippett (1928), *Limiting forms of the frequency distribution of the largest or smallest member of a sample*, Math. Proc. Cambridge Philos. Soc. 24(2) : <https://doi.org/10.1017/S0305004100015681> — résumé vu, texte intégral indisponible.
- Gnedenko (1943), *Sur la distribution limite du terme maximum d'une série aléatoire*, Ann. of Math. 44(3) : <https://doi.org/10.2307/1968974> — métadonnées seules.
- Balkema et de Haan (1974), *Residual life time at great age*, Ann. Probab. 2(5), 792–804 : <https://doi.org/10.1214/aop/1176996548> — résumé seul.
- Pickands (1975), *Statistical inference using extreme order statistics*, Ann. Statist. 3(1), 119–131 : <https://doi.org/10.1214/aos/1176343003> — résumé seul.
- Hill (1975), *A simple general approach to inference about the tail of a distribution*, Ann. Statist. 3(5), 1163–1174 : <https://doi.org/10.1214/aos/1176343247> — résumé seul.
- Davison et Smith (1990), *Models for exceedances over high thresholds*, JRSS B 52(3) : <https://doi.org/10.1111/j.2517-6161.1990.tb01796.x> — résumé seul.
- Coles (2001), *An Introduction to Statistical Modeling of Extreme Values*, Springer : <https://doi.org/10.1007/978-1-4471-3675-0> — livre non lu ; table des matières vue (théorie classique, modèles à seuil, séquences dépendantes, non-stationnarité).
- de Haan et Ferreira (2006), *Extreme Value Theory*, Springer : <https://doi.org/10.1007/0-387-34471-3> — livre non lu ; le sous-titre « An Introduction » n'est pas confirmé.
- Siffer, Fouque, Termier, Largouët (2017), *Anomaly Detection in Streams with Extreme Value Theory*, KDD'17 : <https://doi.org/10.1145/3097983.3098144> — lu.
- Scarrott et MacDonald (2012), *A review of extreme value threshold estimation and uncertainty quantification*, REVSTAT 10(1) : <https://www.ine.pt/revstat/pdf/rs120102.pdf> — lu.
- Gilleland et Katz (2016), *extRemes 2.0: An Extreme Value Analysis Package in R*, J. Stat. Softw. 72(8) : <https://doi.org/10.18637/jss.v072.i08> — lu.
- Gardes et Girard, *A Pickands type estimator of the extreme value index* : <https://arxiv.org/abs/math/0403299> — lu (formules de Hill et Pickands).
- Bücher et Zhou (2018), *A horse racing between the block maxima method and the peak-over-threshold approach* : <https://arxiv.org/abs/1807.00282> — résumé seul.
- Documentation : [scipy.stats.genextreme](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.genextreme.html), [scipy.stats.genpareto](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.genpareto.html), [pyextremes](https://github.com/georgebv/pyextremes).
- Connexions brain : [[Théorème central limite]], [[Inégalités de concentration]], [[Time series anomaly detection]], [[scipy.stats]].
