---
type: moc
nom: Statistiques & inférence
galaxie: dev
indexe: stats/*
---

# Statistiques & inférence

<!-- AUTO:START -->
Briques techniques de la catégorie `stats/*`.

- [[Dev/Services/ArviZ|ArviZ]] — Analyse exploratoire et diagnostics des modèles bayésiens, indépendant du moteur — trace plots, R̂, ESS, comparaison LOO/WAIC.
- [[Dev/Services/CausalImpact|CausalImpact]] — Effet causal d'une intervention par séries temporelles structurelles bayésiennes — contrefactuel prédit depuis des séries de contrôle.
- [[Dev/Services/Fanalysis|Fanalysis]] — Analyses factorielles descriptives (PCA, CA, MCA) avec aides à l'interprétation façon FactoMineR ; dépôt sans commit depuis juin 2018, resté en v0.0.1 — préférer Prince.
- [[Dev/Services/lifelines|lifelines]] — Analyse de survie en Python pur — estimateurs non paramétriques (Kaplan-Meier, Nelson-Aalen) et modèles de régression (Cox à risques proportionnels, AFT) pour modéliser le temps jusqu'à un événement avec données censurées.
- [[Dev/Services/pingouin|pingouin]] — Tests statistiques simples et lisibles, tailles d'effet incluses — la clarté plutôt que l'exhaustivité, sur pandas.
- [[Dev/Services/Prince|Prince]] — Analyse factorielle (PCA, CA, MCA, FAMD, MFA, GPA) en API scikit-learn — fit/transform sur DataFrames pandas.
- [[Dev/Services/PyMC|PyMC]] — Programmation probabiliste en Python — modélisation bayésienne et échantillonnage MCMC (NUTS) sur un backend autodiff (PyTensor).
- [[Dev/Services/scipy.stats|scipy.stats]] — Socle bas niveau des tests statistiques et lois de probabilité en Python — p-values, distributions, corrélations, au sein de SciPy.
- [[Dev/Services/Stan|Stan]] — Inférence bayésienne haute performance : langage de modélisation dédié compilé en C++, échantillonneur NUTS de référence, piloté depuis Python via CmdStanPy.
- [[Dev/Services/statsmodels|statsmodels]] — Modélisation statistique façon R en Python — GLM, séries temporelles, tests de spécification avec tables de résultats détaillées.
<!-- AUTO:END -->

## Notes

