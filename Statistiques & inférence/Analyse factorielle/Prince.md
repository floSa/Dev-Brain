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

<!-- AUTO:BANDEAU:START -->
> Analyse factorielle (PCA, CA, MCA, FAMD, MFA, GPA) en API scikit-learn — fit/transform sur DataFrames pandas.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque d'analyse factorielle multivariée dans la tradition Benzécri / FactoMineR,
exposée sous une **API scikit-learn** : `fit` / `transform` directement sur des DataFrames
pandas, avec des sorties indexées et lisibles. Couvre toute la famille — PCA pour le
quantitatif, CA pour la contingence, MCA pour le qualitatif, FAMD pour le mixte, MFA pour
des groupes de variables, plus GPA et PGA. Gère les lignes et colonnes supplémentaires et
les pondérations, et ses sorties sont testées contre scikit-learn et FactoMineR via rpy2.
C'est l'implémentation Python de référence du domaine.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Analyse exploratoire multivariée sur tableaux pandas : plans factoriels, contributions, cos² | L'API a notablement évolué entre versions majeures (sorties, noms de méthodes) — épingler la version |
| Données qualitatives (MCA), de contingence (CA) ou mixtes (FAMD), au-delà de la PCA quantitative | Visualisations bâties sur Altair : le rendu dépend de l'environnement, notebook compris |
| Intégration dans un pipeline scikit-learn — `fit_transform` | La décomposition reste en mémoire sur un seul nœud : pas de très gros tableaux |
| | PCA quantitative pure dans un pipeline déjà scikit-learn : `sklearn.decomposition.PCA` suffit → [[Scikit-Learn]] |

## Mise en œuvre

- Installation — `uv add prince`
- Point d'entrée — import Python, `import prince`, estimateurs `fit` / `transform`
- Prérequis — pandas, scikit-learn et altair
- Exécution — dans le process appelant, CPU, mono-nœud, tout en mémoire
- Coût — gratuit, MIT, aucune limite d'usage

## Écosystème

### Alternatives

- [[Fanalysis]] — Analyses factorielles descriptives (PCA, CA, MCA) avec aides à l'interprétation façon FactoMineR ; dépôt sans commit depuis juin 2018, resté en v0.0.1 — préférer Prince.

## Ressources

- Documentation — https://maxhalford.github.io/prince/
- Dépôt — https://github.com/MaxHalford/prince

## Voir aussi

- [[PCA]] · [[MCA]] · [[CA]] · [[FAMD]] · [[MFA]] — les notions implémentées
- [[Comparatif - Outils stats]] — ce qui départage les outils du dossier
- [[Comparatif - Réduction de dimension]] — analyse factorielle face à la PCA et aux méthodes manifold
