---
role: brique
nom: scipy.stats
alias: [SciPy stats]
pitch: "Socle bas niveau des tests statistiques et lois de probabilité en Python — p-values, distributions, corrélations, au sein de SciPy."
categorie: stats/inference
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[statsmodels]]", "[[pingouin]]"]
complements: []
tags: [hypothesis-testing, p-value, confidence-interval, parametric-test, non-parametric]
url_docs: https://docs.scipy.org/doc/scipy/reference/stats.html
url_repo: https://github.com/scipy/scipy
---

# scipy.stats

<!-- AUTO:BANDEAU:START -->
> Socle bas niveau des tests statistiques et lois de probabilité en Python — p-values, distributions, corrélations, au sein de SciPy.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Sous-module statistique de SciPy, présent dans presque tout environnement Python
scientifique : une centaine de lois de probabilité continues et discrètes, les
statistiques descriptives, les corrélations, l'estimation de densité, et la plupart des
tests d'hypothèse classiques. L'API est faite de **fonctions, pas de modèles** — chaque
appel rend une statistique et une p-value, sans objet ajusté, sans état conservé, sans
diagnostic : l'interprétation reste entièrement à la charge du lecteur. C'est le socle bas
niveau sur lequel statsmodels et pingouin sont bâtis.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Calculer vite une p-value ou une statistique de test, sans ajouter de dépendance | Aucun objet modèle, aucun diagnostic : l'interprétation du résultat est à la charge de l'appelant |
| Manipuler des lois de probabilité — `pdf`, `cdf`, `ppf`, tirage, ajustement de paramètres | Conventions subtiles à connaître : `ddof`, `alternative`, bilatéral contre unilatéral, corrections de continuité |
| Bootstrap, tests de permutation, Monte-Carlo — `bootstrap`, `permutation_test`, `monte_carlo_test` | Pas de correction de tests multiples homogène — `false_discovery_control` ne couvre qu'une partie du besoin |
| Classification ascendante hiérarchique par le sous-module voisin `scipy.cluster.hierarchy` (`linkage`, `dendrogram`, `fcluster`) | |

## Mise en œuvre

- Installation — `uv add scipy`
- Point d'entrée — import Python, `from scipy import stats`
- Prérequis — aucun au-delà de NumPy ; noyaux compilés C/Fortran/Cython embarqués dans les wheels
- Exécution — dans le process appelant, CPU, mono-nœud
- Coût — gratuit, BSD-3-Clause, aucune limite d'usage

## Écosystème

### Alternatives

- [[statsmodels]] — Modélisation statistique façon R en Python — GLM, séries temporelles, tests de spécification avec tables de résultats détaillées.
- [[pingouin]] — Tests statistiques simples et lisibles, tailles d'effet incluses — la clarté plutôt que l'exhaustivité, sur pandas.

## Ressources

- Documentation — https://docs.scipy.org/doc/scipy/reference/stats.html
- Dépôt — https://github.com/scipy/scipy

## Voir aussi

- [[Tests d'hypothèse]] · [[Intervalles de confiance]] · [[Test t et ANOVA]] · [[Test du khi-deux]] · [[Tests non paramétriques]] — les notions implémentées
- [[Classification hiérarchique (CAH)|CAH]] — via `scipy.cluster.hierarchy`, le sous-module voisin
- [[Comparatif - Outils stats]] — ce qui départage les outils du dossier
