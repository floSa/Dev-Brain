---
galaxie: dev
type: service
nom: scipy.stats
alias: [SciPy stats]
pitch: "Socle bas niveau des tests statistiques et lois de probabilité en Python — p-values, distributions, corrélations, au sein de SciPy."
categorie: tooling/stats
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/statsmodels|statsmodels]]", "[[Dev/Services/pingouin|pingouin]]"]
remplace_par: []
status: actif
tags: [hypothesis-testing, p-value, confidence-interval, parametric-test, non-parametric]
url_docs: https://docs.scipy.org/doc/scipy/reference/stats.html
url_repo: https://github.com/scipy/scipy
---

# scipy.stats

## Pourquoi

Sous-module statistique de **SciPy**, présent dans presque tout environnement Python scientifique. Couvre un très large catalogue : ~100 lois de probabilité (continues et discrètes), statistiques descriptives, corrélations, estimation de densité, et la plupart des tests d'hypothèse classiques (t, ANOVA, χ², Mann-Whitney, Wilcoxon, Kruskal-Wallis, Kolmogorov-Smirnov…). Chaque test renvoie une statistique et une p-value ; plusieurs exposent aussi un intervalle de confiance. C'est le **socle bas niveau** sur lequel s'appuient statsmodels et pingouin.

## Quand l'utiliser

- Calculer rapidement une p-value ou une statistique de test sans dépendance supplémentaire (SciPy est presque toujours déjà installé).
- Manipuler des lois de probabilité : `pdf`, `cdf`, `ppf`, tirage, fit de paramètres.
- Bootstrap, tests de permutation, Monte-Carlo via `scipy.stats.bootstrap` / `permutation_test` / `monte_carlo_test`.
- Classification ascendante hiérarchique via le sous-module voisin `scipy.cluster.hierarchy` (`linkage`, `dendrogram`, `fcluster`) → [[Wiki/Concepts/Classification hiérarchique (CAH)|CAH]].

## Quand NE PAS l'utiliser

- Modèles statistiques complets (régression OLS/GLM, séries temporelles, tables de résultats annotées) → [[Dev/Services/statsmodels|statsmodels]].
- API lisible orientée sortie « prête à publier » avec tailles d'effet et tests post-hoc → [[Dev/Services/pingouin|pingouin]].
- Analyse factorielle / réduction de dimension → [[Dev/Services/Prince|Prince]].

## Déploiement & coût

- Bibliothèque liée au process Python (`pip`/`uv add scipy`), aucune infra.
- Single-node ; noyaux compilés (C/Fortran/Cython) pour la performance.
- BSD-3-Clause, gratuit.

## Pièges

- API par fonctions, pas par modèles : peu de mémoire d'état, peu de diagnostics — à toi d'interpréter.
- Conventions parfois subtiles (`ddof`, `alternative`, bilatéral vs unilatéral, corrections de continuité).
- Pas de correction de tests multiples intégrée de façon homogène (voir `scipy.stats.false_discovery_control`, partiel).

## Alternatives

- [[Dev/Services/statsmodels|statsmodels]] — Modélisation statistique façon R en Python — GLM, séries temporelles, tests de spécification avec tables de résultats détaillées.
- [[Dev/Services/pingouin|pingouin]] — Tests statistiques simples et lisibles, tailles d'effet incluses — la clarté plutôt que l'exhaustivité, sur pandas.

## Liens

- Concepts implémentés : [[Wiki/Concepts/Tests d'hypothèse|Tests d'hypothèse]], [[Wiki/Concepts/Intervalles de confiance|Intervalles de confiance]], [[Wiki/Concepts/Test t et ANOVA|Test t et ANOVA]], [[Wiki/Concepts/Test du khi-deux|Test du khi-deux]], [[Wiki/Concepts/Tests non paramétriques|Tests non paramétriques]], [[Wiki/Concepts/Classification hiérarchique (CAH)|CAH]] (via `scipy.cluster.hierarchy`)
- [[Comparatif - Outils stats]] — comparatif des libs statistiques
- Doc : https://docs.scipy.org/doc/scipy/reference/stats.html
