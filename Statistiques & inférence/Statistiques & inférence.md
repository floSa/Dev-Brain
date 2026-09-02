---
role: hub
nom: Statistiques & inférence
alias: [stats, inférence statistique]
pitch: Généraliser d'un échantillon à une population, et mesurer ce que cette généralisation vaut — tests, estimation, inférence causale.
domaines: [data-sci]
tags: [statistical-inference, bayesian, causal-inference, factor-analysis]
---

# Statistiques & inférence

> Généraliser d'un échantillon à une population, et mesurer ce que cette généralisation vaut — tests, estimation, inférence causale.

## Ce qu'il faut comprendre

- Ce domaine n'est pas du machine learning à petite échelle. Le ML prédit et se juge sur des données non vues ; la statistique **estime un paramètre et quantifie son incertitude**, et se juge sur la validité de ses hypothèses. Les deux se recouvrent sur les modèles linéaires et divergent partout ailleurs — c'est pourquoi [[statsmodels]] et [[Scikit-Learn]] ajustent la même régression et n'affichent pas la même chose.
- Deux écoles se partagent le domaine, et le choix de l'outil suit ce clivage plus que le besoin métier. Le **fréquentiste** répond par une p-value et un [[Intervalles de confiance|intervalle de confiance]] ([[scipy.stats]], [[statsmodels]], [[pingouin]]) ; le **bayésien** répond par une distribution a posteriori ([[PyMC]], [[Stan]]), au prix d'un a priori à assumer et d'un échantillonnage à faire converger. Cf. [[Inférence bayésienne]] et [[Tests d'hypothèse]].
- En bayésien, le moteur et le **diagnostic** sont deux briques distinctes, et la seconde n'est pas optionnelle : un [[MCMC]] qui n'a pas convergé produit des chiffres d'apparence normale. [[ArviZ]] est indépendant du moteur et se branche aussi bien sur [[PyMC]] que sur [[Stan]] — c'est le complément par défaut des deux.
- Le troisième clivage est le **niveau d'API**. [[scipy.stats]] donne les lois et les tests bruts, à assembler soi-même. [[statsmodels]] et [[pingouin]] donnent des modèles et des tables de résultats prêtes à lire. Descendre d'un niveau se paie en code, monter d'un niveau se paie en hypothèses implicites.
- L'**analyse factorielle** ([[Prince]]) est une tradition française à part, distincte de la [[Réduction de dimension]] du ML : elle vise l'interprétation des axes, pas la performance d'un modèle en aval. [[PCA]], [[CA]], [[MCA]], [[FAMD]] sont ses variantes selon la nature des variables.
- Deux familles de questions ont leur outil dédié parce que la censure et la confusion ne se traitent pas par un test ordinaire : l'[[Analyse de survie]] ([[lifelines]]) et l'[[Inférence causale]] ([[CausalImpact]]).

## Choisir

- Une loi, un test brut, une brique dans son propre code → [[scipy.stats]].
- Un modèle statistique et sa table de résultats, façon R → [[statsmodels]].
- Quelques tests à lire vite, tailles d'effet incluses → [[pingouin]].
- Un modèle bayésien à écrire en Python, dans un pipeline Python → [[PyMC]].
- Un modèle bayésien difficile, ou une équipe déjà sur le langage Stan → [[Stan]].
- Diagnostiquer et comparer des a posteriori, quel que soit le moteur → [[ArviZ]].
- Un temps jusqu'à un événement, avec des observations censurées → [[lifelines]].
- L'effet d'une intervention datée sur une série, sans groupe témoin randomisé → [[CausalImpact]].
- Des axes latents à interpréter sur des variables mixtes → [[Prince]] (et non [[Fanalysis]], abandonné depuis 2018).
- Prédire plutôt qu'estimer → [[Machine Learning]], pas ce domaine.

<!-- AUTO:START -->
### Briques
- [[ArviZ]] — Analyse exploratoire et diagnostics des modèles bayésiens, indépendant du moteur — trace plots, R̂, ESS, comparaison LOO/WAIC.
- [[CausalImpact]] — Effet causal d'une intervention par séries temporelles structurelles bayésiennes — contrefactuel prédit depuis des séries de contrôle.
- [[Fanalysis]] — Analyses factorielles descriptives (PCA, CA, MCA) avec aides à l'interprétation façon FactoMineR ; dépôt sans commit depuis juin 2018, resté en v0.0.1 — préférer Prince.
- [[lifelines]] — Analyse de survie en Python pur — estimateurs non paramétriques (Kaplan-Meier, Nelson-Aalen) et modèles de régression (Cox à risques proportionnels, AFT) pour modéliser le temps jusqu'à un événement avec données censurées.
- [[pingouin]] — Tests statistiques simples et lisibles, tailles d'effet incluses — la clarté plutôt que l'exhaustivité, sur pandas.
- [[Prince]] — Analyse factorielle (PCA, CA, MCA, FAMD, MFA, GPA) en API scikit-learn — fit/transform sur DataFrames pandas.
- [[PyMC]] — Programmation probabiliste en Python — modélisation bayésienne et échantillonnage MCMC (NUTS) sur un backend autodiff (PyTensor).
- [[scipy.stats]] — Socle bas niveau des tests statistiques et lois de probabilité en Python — p-values, distributions, corrélations, au sein de SciPy.
- [[Stan]] — Inférence bayésienne haute performance : langage de modélisation dédié compilé en C++, échantillonneur NUTS de référence, piloté depuis Python via CmdStanPy.
- [[statsmodels]] — Modélisation statistique façon R en Python — GLM, séries temporelles, tests de spécification avec tables de résultats détaillées.

### Comparatifs
- [[Comparatif - Outils stats]]
<!-- AUTO:END -->
