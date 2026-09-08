---
role: brique
nom: statsmodels
alias: []
pitch: "Modélisation statistique façon R en Python — GLM, séries temporelles, tests de spécification avec tables de résultats détaillées."
categorie: stats/inference
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[scipy.stats]]", "[[pingouin]]"]
complements: []
tags: [statistical-inference, hypothesis-testing, parametric-test, p-value]
url_docs: https://www.statsmodels.org/stable/
url_repo: https://github.com/statsmodels/statsmodels
---

# statsmodels

<!-- AUTO:BANDEAU:START -->
> Modélisation statistique façon R en Python — GLM, séries temporelles, tests de spécification avec tables de résultats détaillées.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-08-30 |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque de modélisation statistique qui apporte à Python l'esprit de R : on estime un
modèle — OLS, GLM, mixtes, ANOVA, ARIMA/SARIMAX, VAR — puis on lit un **résumé annoté**
(coefficients, erreurs-types, p-values, intervalles de confiance, R², AIC/BIC), doublé
d'une batterie de tests de spécification : hétéroscédasticité, autocorrélation, normalité
des résidus, multicolinéarité. Là où scipy.stats donne une fonction, statsmodels donne un
objet modèle avec ses diagnostics. L'API formules à la R (`y ~ x1 + x2`, via patsy)
coexiste avec l'API par classes, et les deux ne se mélangent pas.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Régression linéaire, logistique ou Poisson avec inférence complète — IC et tests sur les coefficients | L'OLS **n'ajoute pas** la constante : `add_constant`, ou passer par la formule, sous peine de modèle faux |
| Modèles linéaires généralisés et additifs — familles binomiale, Poisson, Gamma, `GLMGam` à splines pénalisées | API double, `sm.OLS` contre `smf.ols` : deux conventions qui se mélangent mal |
| Séries temporelles : ARIMA, SARIMAX, lissage exponentiel, décomposition, tests de stationnarité (ADF, KPSS) | Prédiction pure ou ML supervisé à grande échelle → [[Scikit-Learn]] |
| ANOVA et ANCOVA structurées, tests de spécification et d'adéquation d'un modèle | Orienté inférence, pas pipeline : aucun `fit`/`predict` homogène avec scikit-learn |

## Mise en œuvre

- Installation — `uv add statsmodels`
- Point d'entrée — import Python, `import statsmodels.api as sm` ou `statsmodels.formula.api as smf`
- Prérequis — NumPy, SciPy, pandas et patsy ; rien d'autre
- Exécution — dans le process appelant, CPU, mono-nœud, tout en mémoire
- Coût — gratuit, BSD-3-Clause, aucune limite d'usage

## Écosystème

### Alternatives

- [[scipy.stats]] — Socle bas niveau des tests statistiques et lois de probabilité en Python — p-values, distributions, corrélations, au sein de SciPy.
- [[pingouin]] — Tests statistiques simples et lisibles, tailles d'effet incluses — la clarté plutôt que l'exhaustivité, sur pandas.

## Ressources

- Documentation — https://www.statsmodels.org/stable/
- Dépôt — https://github.com/statsmodels/statsmodels

## Voir aussi

- [[Régression linéaire]] · [[GLM]] · [[GAM]] · [[Test t et ANOVA]] · [[Tests d'hypothèse]] — les notions implémentées
- [[Comparatif - Outils stats]] — ce qui départage les outils du dossier
