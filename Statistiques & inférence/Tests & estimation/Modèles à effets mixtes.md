---
role: notion
nom: Modèles à effets mixtes
alias: [mixed effects models, mixed models, modèles mixtes, modèles linéaires mixtes, LMM, linear mixed model, multilevel model, modèle multiniveau, modèle hiérarchique, random effects, effets aléatoires, random intercept, intercept aléatoire, random slope, pente aléatoire, REML, pseudo-réplication, pseudoreplication, partial pooling, lme4, MixedLM]
categorie: stats/inference
domaines: [data-sci]
tags: [statistical-inference, regression, linear-model]
---

# Modèles à effets mixtes

## Aperçu

- Régression pour des observations **groupées ou répétées** (élèves dans des écoles, mesures répétées sur un patient, capteurs sur des machines) : les lignes d'un même groupe se ressemblent, elles ne sont **pas indépendantes**.
- Principe : à côté des **effets fixes** (coefficients communs à tous), le modèle donne à chaque groupe un écart **tiré d'une loi** — l'effet aléatoire. Le modèle estime la **variance** de ces écarts, pas un coefficient par groupe.
- Ignorer le groupement ne rend pas le modèle faux de manière visible : les coefficients sortent, les erreurs-types sont trop petites. C'est la **pseudo-réplication**.

## Concepts clés

### Effets fixes et effets aléatoires

- **Effet fixe** : un coefficient unique, estimé pour toute la population (l'effet d'un traitement, d'une pente de temps).
- **Effet aléatoire** : un écart propre à chaque groupe (ou à chaque individu), supposé tiré d'une loi normale centrée. Seule la variance de cette loi est un paramètre du modèle.
- Les définitions de « fixe » et « aléatoire » **ne sont pas stables** : Gelman (2005) en recense cinq, incompatibles entre elles (constant ou variable, intéressant en soi ou non, échantillon exhaustif ou non, réalisation d'une variable aléatoire, estimé avec ou sans rétrécissement). La dernière — un effet aléatoire est estimé avec **shrinkage** — est celle qui sert en pratique.

### Interceptes et pentes aléatoires

- **Intercept aléatoire** : chaque groupe a son niveau de base. Syntaxe lme4 : `(1 | groupe)`.
- **Pente aléatoire** : l'effet d'une variable varie d'un groupe à l'autre. `(x | groupe)` ajoute intercept et pente, **corrélés** par défaut ; `(x || groupe)` les suppose non corrélés (à réserver aux prédicteurs sur échelle de rapport, selon la doc lme4).
- **Imbriqué** (élèves dans classes dans écoles) : `(1 | ecole/classe)`. **Croisé** (sujets × items) : `(1 | sujet) + (1 | item)`.

### Estimation : ML et REML

- Le maximum de vraisemblance (ML) **sous-estime** les composantes de variance, parce qu'il ignore les degrés de liberté consommés par l'estimation des effets fixes (Laird et Ware 1982, §3.3).
- Le **REML** (vraisemblance restreinte) corrige ce biais : il maximise la vraisemblance de contrastes qui n'impliquent plus les effets fixes. Dans lme4 : $\hat\sigma^2 = r^2/(n-p)$ pour le REML, diviseur $n$ pour le ML.
- Défaut REML dans lme4 (`REML = TRUE`) et dans `statsmodels` (`reml=True`). Pour **comparer deux modèles qui diffèrent par leurs effets fixes**, il faut ajuster en ML : `anova()` de lme4 refait l'ajustement en ML tout seul.

### Retrécissement (partial pooling)

- Trois façons de traiter les groupes : **tout mettre ensemble** (un seul effet commun), **un effet par groupe** (indicatrices, aucune information partagée), ou **partial pooling** — compromis où chaque groupe est tiré vers la moyenne générale.
- Plus un groupe est petit ou bruité, plus son estimation est tirée vers la moyenne ; plus la variance entre groupes est grande, moins elle l'est.
- C'est exactement le comportement d'un modèle **bayésien hiérarchique** à a priori normal sur les écarts : un modèle mixte en est la version fréquentiste, avec les variances estimées plutôt que munies d'un a priori.

## Les maths, simplement

- Forme de Laird et Ware (1982), pour l'unité $i$ : $y_i = X_i\beta + Z_i b_i + \varepsilon_i$, avec $b_i \sim \mathcal N(0, D)$ et $\varepsilon_i \sim \mathcal N(0, R_i)$, indépendants. $X_i$ porte les effets fixes $\beta$, $Z_i$ les effets aléatoires $b_i$.
- Vue marginale : $y_i \sim \mathcal N\big(X_i\beta,\; Z_i D Z_i^\top + R_i\big)$. La corrélation entre mesures d'un même groupe vient du terme $Z_i D Z_i^\top$ : c'est ce que l'indépendance supposée par une régression ordinaire ne voit pas.
- Avec $R_i = \sigma^2 I$ (indépendance conditionnelle), un intercept aléatoire seul donne une corrélation intra-groupe $\rho = \tau^2/(\tau^2 + \sigma^2)$, où $\tau^2$ est la variance des interceptes.
- Les composantes de variance ($D$, $\sigma^2$) s'estiment par REML ; $\beta$ en découle par moindres carrés généralisés.

## En pratique

### Pseudo-réplication

- Hurlbert (1984) la définit comme un **test sur un terme d'erreur inadapté à l'hypothèse** : des mesures répétées sur la même unité traitées comme des unités indépendantes. Ce n'est pas un défaut du plan d'expérience seul, mais d'une combinaison plan + analyse.
- Cas courant en data : 10 000 lignes qui viennent de 12 machines, analysées comme 10 000 observations indépendantes. La taille d'échantillon **effective** est proche de 12, pas de 10 000.

### Effet mixte ou indicatrices ?

- **Effet mixte** quand : beaucoup de groupes, l'intérêt porte sur la **population** de groupes (pas sur chacun), les effectifs sont déséquilibrés (le shrinkage stabilise les petits groupes), ou qu'il faut **prédire pour un groupe nouveau**.
- **Indicatrices (effets fixes)** quand : peu de groupes, les groupes eux-mêmes sont l'objet de l'étude, ou aucune généralisation à d'autres groupes n'est visée.
- Seuil indicatif : la FAQ de Bolker conseille au moins 5 à 6 niveaux pour estimer une variance, avec peu de niveaux les estimations sont imprécises ou la variance tombe à zéro. Ce sont des **heuristiques issues de simulations**, pas un théorème.
- Si seul l'effet moyen compte, la documentation de `statsmodels` signale les **GEE** comme alternative (structure moyenne marginale).

### Quelle structure d'effets aléatoires ?

- **Barr et al. (2013), « Keep it maximal »** : pour un test confirmatoire, inclure tous les effets aléatoires que le plan justifie (une pente aléatoire par facteur intra-unité) ; réduire seulement si le modèle ne converge pas.
- **Matuschek et al. (2017)** : le modèle maximal **perd de la puissance**, même quand il est le vrai modèle ; un modèle sans pentes aléatoires gonfle l'erreur de type I. Ils proposent de retenir la structure que **les données soutiennent**, par sélection descendante au test du rapport de vraisemblance, avec $\alpha_{LRT} = 0{,}2$ plutôt que 0,05.
- **Bates et al. (2015), « Parsimonious mixed models »** : un échec de convergence signale en général un modèle trop complexe pour les données ; outil proposé, une ACP des effets aléatoires (`rePCA`) pour repérer les dimensions dégénérées.
- Désaccord laissé tel quel : le premier réduit sur non-convergence et défend le choix a priori par le plan ; les deux autres réduisent selon ce que les données soutiennent. Le manuel lme4 présente les deux options sans trancher.

### Pièges

- **Ajustement singulier** : variance proche de 0 ou corrélation à ±1. Fréquent avec les petits jeux de données et les structures riches ; lme4 le signale (`isSingular`) mais ne le traite pas comme une erreur.
- **p-values** : lme4 n'en affiche pas pour `lmer`, faute de loi nulle exacte dans les plans déséquilibrés. Les approximations de degrés de liberté (Satterthwaite, Kenward-Roger, via `lmerTest` ou `pbkrtest`) sont des solutions de contournement ; avec moins de 50 groupes, la correction de taille finie compte. `statsmodels` affiche des tests de Wald (z) sans correction.
- **Normalité des effets aléatoires** : supposée par les implémentations lues ; aucune source sur la robustesse à son défaut n'a été lue ici.

### En Python

- `statsmodels.regression.mixed_linear_model.MixedLM` (doc stable : `statsmodels 0.15.0`, 2026-08-27) : interceptes aléatoires (défaut), pentes via `re_formula`, composantes de variance via `vc_formula`.

```python
import statsmodels.formula.api as smf

m = smf.mixedlm("y ~ x", df, groups=df["machine"], re_formula="~x").fit(reml=True)
print(m.summary())
```

- Limite documentée : `MixedLM` traite la plupart des modèles **non croisés** et « quelques » modèles croisés ; pour des effets croisés, il faut traiter tout le jeu de données comme un seul groupe. Les effets aléatoires sont indépendants entre groupes.
- Pas de GLMM fréquentiste dans `statsmodels` : seulement `BinomialBayesMixedGLM` et `PoissonBayesMixedGLM`, par approximation de Laplace ou Bayes variationnel.
- Autres routes : `pymer4` (enveloppe de `lme4` via R, donc R requis), `Bambi` (syntaxe à la lme4, moteur [[PyMC]]), ou le modèle hiérarchique écrit à la main dans [[PyMC]] / [[Stan]].

## Approches voisines & alternatives

- [[GLM]] — réponse binaire ou de comptage ; devient un **GLMM** dès qu'on ajoute des effets aléatoires. Les effets mixtes en sont une extension, pas un concurrent.
- [[Analyse de survie]] — pour un temps jusqu'à un événement avec censure : hors du périmètre d'un modèle linéaire mixte à réponse gaussienne.
- [[Inférence bayésienne]] — le modèle hiérarchique bayésien donne la même structure avec une **distribution** sur les variances et sans approximation de degrés de liberté ; [[PyMC]] et [[Stan]] l'implémentent.
- [[statsmodels]] — `MixedLM` pour le cas linéaire gaussien, avec les limites ci-dessus.
- [[Test t et ANOVA]] — l'ANOVA à mesures répétées est le cas particulier historique ; les mixtes gèrent les données déséquilibrées et manquantes.
- [[Régression linéaire]] — le cas à observations indépendantes, point de départ.
- **GEE** — estime l'effet moyen de population avec des erreurs robustes, sans modéliser les effets de groupe.

## Pour aller plus loin

- Laird & Ware (1982), *Random-effects models for longitudinal data*, Biometrics 38 : <https://www.stat.cmu.edu/~brian/463-663/week06/some%20nice%20papers/laird-ware-biometrics-1982.pdf>
- Bates, Mächler, Bolker, Walker (2015), *Fitting linear mixed-effects models using lme4*, JSS 67(1) ; version arXiv lue : <https://arxiv.org/abs/1406.5823>
- Gelman & Hill (2007), *Data Analysis Using Regression and Multilevel/Hierarchical Models*, Cambridge UP (référence de la lecture hiérarchique ; page éditeur seule consultée, livre non lu).
- Gelman (2005), *Analysis of variance — why it is more important than ever*, Annals of Statistics 33 : <https://arxiv.org/abs/math/0504499>
- Barr, Levy, Scheepers, Tily (2013), *Random effects structure for confirmatory hypothesis testing: Keep it maximal*, J. Memory and Language 68 : <https://www.mit.edu/~rplevy/papers/barr-etal-2013-jml.pdf>
- Matuschek, Kliegl, Vasishth, Baayen, Bates (2017), *Balancing Type I error and power in linear mixed models*, J. Memory and Language 94 ; preprint lu : <https://arxiv.org/abs/1511.01864>
- Bates, Kliegl, Vasishth, Baayen, *Parsimonious mixed models* (preprint) : <https://arxiv.org/abs/1506.04967>
- Hurlbert (1984), *Pseudoreplication and the design of ecological field experiments*, Ecological Monographs 54(2).
- Bolker, *GLMM FAQ* : <https://bbolker.github.io/mixedmodels-misc/glmmFAQ.html>
- Documentation `statsmodels` : <https://www.statsmodels.org/stable/mixed_linear.html>
- Connexions brain : [[GLM]], [[Analyse de survie]], [[statsmodels]], [[PyMC]], [[Stan]].
