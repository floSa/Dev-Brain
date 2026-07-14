---
galaxie: dev
type: service
nom: statsmodels
alias: []
pitch: "Modélisation statistique façon R en Python — GLM, séries temporelles, tests de spécification avec tables de résultats détaillées."
categorie: tooling/stats
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/scipy.stats|scipy.stats]]", "[[Dev/Services/pingouin|pingouin]]"]
remplace_par: []
status: actif
tags: [statistical-inference, hypothesis-testing, parametric-test, p-value]
url_docs: https://www.statsmodels.org/stable/
url_repo: https://github.com/statsmodels/statsmodels
---

# statsmodels

## Pourquoi

Bibliothèque de **modélisation statistique** qui apporte à Python l'esprit de R : on estime un modèle (OLS, GLM, mixtes, ANOVA, ARIMA/SARIMAX, VAR…) puis on lit un **résumé annoté** (coefficients, erreurs-types, p-values, IC, R², AIC/BIC) et toute une batterie de **tests de spécification** (hétéroscédasticité, autocorrélation, normalité des résidus, multicolinéarité). Là où scipy.stats donne une fonction, statsmodels donne un objet modèle avec ses diagnostics.

## Quand l'utiliser

- [[Wiki/Concepts/Régression linéaire|Régression linéaire]] (OLS), logistique et Poisson avec inférence complète (IC, tests sur les coefficients), via l'API formules `statsmodels.formula.api` (`smf`) inspirée de R (`y ~ x1 + x2`, sur patsy).
- Modèles linéaires généralisés [[Wiki/Concepts/GLM|GLM]] (familles binomiale, Poisson, Gamma…) et modèles additifs généralisés [[Wiki/Concepts/GAM|GAM]] via `GLMGam` (splines pénalisées).
- Séries temporelles : ARIMA, SARIMAX, lissage exponentiel, décomposition, tests de stationnarité (ADF, KPSS).
- ANOVA et ANCOVA structurées, tests de spécification et d'adéquation d'un modèle.

## Quand NE PAS l'utiliser

- Un simple test ponctuel ou une distribution → [[Dev/Services/scipy.stats|scipy.stats]] (plus direct, déjà installé).
- Sortie lisible avec tailles d'effet et post-hoc sans construire de modèle → [[Dev/Services/pingouin|pingouin]].
- Prédiction pure / ML supervisé à grande échelle → [[Dev/Services/Scikit-Learn|scikit-learn]].

## Déploiement & coût

- Bibliothèque Python (`uv add statsmodels`), s'appuie sur NumPy/SciPy/pandas/patsy.
- Single-node ; calcul en mémoire.
- BSD-3-Clause, gratuit.

## Pièges

- L'OLS **n'ajoute pas** la constante : penser à `add_constant` (ou la formule).
- API double (classes `sm.OLS` vs formules `smf.ols`) : ne pas mélanger les conventions.
- Orienté inférence, pas pipeline ML : pas d'API `fit/predict` homogène avec scikit-learn.

## Alternatives

- [[Dev/Services/scipy.stats|scipy.stats]] — Socle bas niveau des tests statistiques et lois de probabilité en Python — p-values, distributions, corrélations, au sein de SciPy.
- [[Dev/Services/pingouin|pingouin]] — Tests statistiques simples et lisibles, tailles d'effet incluses — la clarté plutôt que l'exhaustivité, sur pandas.

## Liens

- Concepts implémentés : [[Wiki/Concepts/Régression linéaire|Régression linéaire]], [[Wiki/Concepts/GLM|GLM]], [[Wiki/Concepts/GAM|GAM]], [[Wiki/Concepts/Test t et ANOVA|Test t et ANOVA]], [[Wiki/Concepts/Tests d'hypothèse|Tests d'hypothèse]]
- [[Comparatif - Outils stats]] — comparatif des libs statistiques
- Doc : https://www.statsmodels.org/stable/
