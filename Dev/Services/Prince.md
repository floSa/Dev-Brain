---
galaxie: dev
type: service
nom: Prince
alias: [prince]
pitch: "Analyse factorielle (PCA, CA, MCA, FAMD, MFA, GPA) en API scikit-learn — fit/transform sur DataFrames pandas."
categorie: tooling/stats
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Fanalysis|Fanalysis]]"]
remplace_par: []
status: actif
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

- Aides à l'interprétation textuelles « façon FactoMineR » sur PCA/CA/MCA seules → [[Dev/Services/Fanalysis|Fanalysis]].
- PCA quantitative pure dans un pipeline ML déjà sklearn → [[Dev/Services/Scikit-Learn|sklearn.decomposition.PCA]].
- Tests d'hypothèse / modèles statistiques → [[Dev/Services/scipy.stats|scipy.stats]], [[Dev/Services/statsmodels|statsmodels]].

## Déploiement & coût

- Bibliothèque Python (`uv add prince`), au-dessus de pandas/scikit-learn/altair.
- Single-node ; calcul en mémoire.
- MIT, gratuit.

## Pièges

- L'API a notablement évolué entre versions majeures (sorties, noms de méthodes) — épingler la version.
- Visualisations basées sur Altair : rendu dépendant de l'environnement (notebook).
- Sur de très gros tableaux, la décomposition reste en mémoire (single-node).

## Alternatives

- [[Dev/Services/Fanalysis|Fanalysis]] — Analyses factorielles descriptives (PCA, CA, MCA) avec aides à l'interprétation façon FactoMineR.

## Liens

- Concepts implémentés : [[Wiki/Concepts/PCA|PCA]], [[Wiki/Concepts/MCA|MCA]], [[Wiki/Concepts/CA|CA]], [[Wiki/Concepts/FAMD|FAMD]], [[Wiki/Concepts/MFA|MFA]]
- [[Comparatif - Outils stats]] — comparatif des libs statistiques
- [[Dev/Patterns/Comparatif - Réduction de dimension]] — analyse factorielle vs PCA / manifold.
- Doc : https://maxhalford.github.io/prince/
