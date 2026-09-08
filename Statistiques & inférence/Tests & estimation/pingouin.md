---
role: brique
nom: pingouin
alias: []
pitch: "Tests statistiques simples et lisibles, tailles d'effet incluses — la clarté plutôt que l'exhaustivité, sur pandas."
categorie: stats/inference
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[scipy.stats]]", "[[statsmodels]]"]
complements: []
tags: [hypothesis-testing, effect-size, statistical-power, non-parametric, parametric-test]
url_docs: https://pingouin-stats.org/
url_repo: https://github.com/raphaelvallat/pingouin
---

# pingouin

<!-- AUTO:BANDEAU:START -->
> Tests statistiques simples et lisibles, tailles d'effet incluses — la clarté plutôt que l'exhaustivité, sur pandas.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-03-28 |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque de tests statistiques pensée pour la lisibilité de la sortie : chaque appel
rend un DataFrame pandas prêt à publier, portant d'un seul coup la p-value, la **taille
d'effet**, l'**intervalle de confiance** et la **puissance** — ce que scipy.stats laisse à
calculer à part. Couvre les t-tests, les ANOVA y compris à mesures répétées et mixtes avec
post-hoc et corrections de multiplicité, les corrélations robustes et partielles, les tests
non paramétriques, et une famille `power_*` pour le dimensionnement d'échantillon. C'est
une surcouche de SciPy, pensée pour des jeux de taille recherche.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Vouloir p-value, taille d'effet et puissance d'un seul appel, dans un DataFrame lisible | **GPL-3.0**, copyleft — là où scipy et statsmodels sont en BSD : à trancher avant toute intégration dans un produit fermé |
| ANOVA à mesures répétées ou mixtes, avec post-hoc et correction de la multiplicité intégrés | Performances pensées pour des jeux de taille recherche, pas pour du volume |
| Dimensionner une expérience — `power_ttest`, `power_anova` | Surcouche de SciPy : un cas très spécifique redescend de toute façon dans le test sous-jacent |

## Mise en œuvre

- Installation — `uv add pingouin`
- Point d'entrée — import Python, `import pingouin as pg`, entrées et sorties en DataFrames pandas
- Prérequis — pandas, NumPy et SciPy ; rien d'autre
- Exécution — dans le process appelant, CPU, mono-nœud, tout en mémoire
- Coût — gratuit mais **GPL-3.0** : copyleft, contamination de licence à vérifier en distribution

## Écosystème

### Alternatives

- [[scipy.stats]] — Socle bas niveau des tests statistiques et lois de probabilité en Python — p-values, distributions, corrélations, au sein de SciPy.
- [[statsmodels]] — Modélisation statistique façon R en Python — GLM, séries temporelles, tests de spécification avec tables de résultats détaillées.

## Ressources

- Documentation — https://pingouin-stats.org/
- Dépôt — https://github.com/raphaelvallat/pingouin

## Voir aussi

- [[Test t et ANOVA]] · [[Tests non paramétriques]] · [[Analyse de puissance]] — les notions implémentées
- [[Comparatif - Outils stats]] — ce qui départage les outils du dossier
