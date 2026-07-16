---
galaxie: wiki
type: concept
nom: MANOVA et tests multivariés
alias: [MANOVA, tests multivariés, multivariate analysis of variance, Hotelling, Hotelling T2, Wilks lambda, trace de Pillai]
categorie: concept/stats
domaines: [data-sci]
tags: [hypothesis-testing, parametric-test, multivariate, effect-size]
---

# MANOVA et tests multivariés

## Aperçu

- Généralisent le [[Test t et ANOVA|test t / l'ANOVA]] à **plusieurs variables réponses simultanées** : on teste si des groupes diffèrent sur un **vecteur** de moyennes.
- Cœur de l'analyse multivariée comparative (`tag: multivariate`).

## Concepts clés

### Du test t à Hotelling à MANOVA
- **T² de Hotelling** : extension multivariée du test t — deux groupes, $p$ réponses.
- **MANOVA** : extension de l'ANOVA — trois groupes ou plus, $p$ réponses.

### Pourquoi multivarié plutôt que $p$ ANOVA séparées
- Contrôle l'inflation du risque $\alpha$ liée aux tests répétés (cf. [[Correction des tests multiples]]).
- Capte les **corrélations entre réponses** : un effet peut n'apparaître que dans leur combinaison, invisible variable par variable.

### Statistiques de test
- **Wilks' Λ** (la plus courante), **trace de Pillai** (la plus robuste aux violations d'hypothèses), trace de Hotelling-Lawley, plus grande racine de Roy.
- Toutes comparent la covariance **inter-groupes** (hypothèse $H$) à la covariance **intra-groupes** (erreur $E$).

### Hypothèses
- Normalité multivariée (Henze-Zirkler), **homogénéité des matrices de covariance** (test M de Box), indépendance.
- En cas de doute sur les hypothèses → privilégier la trace de Pillai.

### Après une MANOVA significative
- ANOVA univariées par réponse, ou **analyse discriminante** (LDA) pour trouver la combinaison qui sépare le mieux les groupes.

## Les maths, simplement

- Wilks' $\Lambda = \dfrac{\det(E)}{\det(E + H)}$ : $\Lambda$ proche de 0 ⇒ groupes très séparés relativement au bruit interne.
- $T^2$ de Hotelling $= \dfrac{n_1 n_2}{n_1 + n_2}\,(\bar{x}_1 - \bar{x}_2)^\top S^{-1} (\bar{x}_1 - \bar{x}_2)$ — une **distance de Mahalanobis** entre moyennes de groupes ($S$ : covariance commune).

## En pratique

- À utiliser quand plusieurs réponses **corrélées** (ex. plusieurs scores d'un même test).
- Réponses non corrélées → des ANOVA séparées + une [[Correction des tests multiples]] suffisent, plus lisibles.
- Vérifier normalité multivariée et M de Box avant de conclure.
- Taille d'effet : $\eta^2$ multivarié (dérivé de Pillai), $\eta^2$ partiel par réponse.
- Outils : `statsmodels` (`MANOVA`), `pingouin` (`multivariate_normality`, `box_m`).

## Approches voisines & alternatives

- [[Test t et ANOVA]] — le cas **univarié** (une seule réponse) que MANOVA généralise.
- [[Correction des tests multiples]] — l'alternative (ANOVA séparées) qui exige une correction ; MANOVA contrôle nativement.
- [[Tests d'hypothèse]] — le cadre général de décision H0 / H1.
- [[Analyse discriminante]] — le débouché prédictif : là où MANOVA teste si les groupes diffèrent, LDA prédit l'appartenance et projette sur les axes qui séparent.
- [[Réduction de dimension]] — la famille des projections, dont l'analyse discriminante est le membre supervisé.

## Pour aller plus loin

- Johnson & Wichern — *Applied Multivariate Statistical Analysis*.
- Outils : `statsmodels.multivariate.manova`, `pingouin`.
