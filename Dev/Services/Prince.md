---
role: brique
nom: Prince
alias: [prince]
pitch: "Analyse factorielle (PCA, CA, MCA, FAMD, MFA, GPA) en API scikit-learn — fit/transform sur DataFrames pandas."
categorie: stats/exploratoire
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Fanalysis]]"]
complements: []
tags: [dimensionality-reduction, factor-analysis, unsupervised]
url_docs: https://maxhalford.github.io/prince/
url_repo: https://github.com/MaxHalford/prince
---

# Prince

## Pourquoi

Bibliothèque d'**analyse factorielle multivariée** (tradition Benzécri / FactoMineR) avec une **API scikit-learn** : `fit` / `transform`, qui travaille directement sur des DataFrames pandas et renvoie des sorties indexées. Couvre toute la famille — PCA (quantitatif), CA (contingence), MCA (qualitatif), FAMD (mixte), MFA (groupes de variables), GPA et PGA. Gère lignes/colonnes supplémentaires et pondérations, et est testée contre scikit-learn et FactoMineR (via rpy2). C'est l'implémentation Python de référence, activement maintenue.

## Quand l'utiliser

- Analyse exploratoire multivariée sur tableaux pandas : plans factoriels, contributions, cos².
- Données qualitatives (MCA), de contingence (CA) ou mixtes (FAMD) — au-delà de la seule PCA quantitative de scikit-learn.
- Intégration dans un pipeline scikit-learn (`fit_transform`).

## Quand NE PAS l'utiliser

- Aides à l'interprétation textuelles « façon FactoMineR » sur PCA/CA/MCA seules → [[Fanalysis]].
- PCA quantitative pure dans un pipeline ML déjà sklearn → [[Scikit-Learn|sklearn.decomposition.PCA]].
- Tests d'hypothèse / modèles statistiques → [[scipy.stats]], [[statsmodels]].

## Déploiement & coût

- Bibliothèque Python (`uv add prince`), au-dessus de pandas/scikit-learn/altair.
- Single-node ; calcul en mémoire.
- MIT, gratuit.

## Pièges

- L'API a notablement évolué entre versions majeures (sorties, noms de méthodes) — épingler la version.
- Visualisations basées sur Altair : rendu dépendant de l'environnement (notebook).
- Sur de très gros tableaux, la décomposition reste en mémoire (single-node).

## Alternatives

- [[Fanalysis]] — Analyses factorielles descriptives (PCA, CA, MCA) avec aides à l'interprétation façon FactoMineR ; dépôt sans commit depuis juin 2018, resté en v0.0.1 — préférer Prince.

## Liens

- Concepts implémentés : [[PCA]], [[MCA]], [[CA]], [[FAMD]], [[MFA]]
- [[Comparatif - Outils stats]] — comparatif des libs statistiques
- [[Comparatif - Réduction de dimension]] — analyse factorielle vs PCA / manifold.
- Doc : https://maxhalford.github.io/prince/
