---
role: brique
nom: ArviZ
alias: [arviz, az]
pitch: "Analyse exploratoire et diagnostics des modèles bayésiens, indépendant du moteur — trace plots, R̂, ESS, comparaison LOO/WAIC."
categorie: stats/bayesien
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: ["[[PyMC]]", "[[Stan]]"]
tags: [bayesian, monte-carlo]
url_docs: https://python.arviz.org
url_repo: https://github.com/arviz-devs/arviz
---

# ArviZ

<!-- AUTO:BANDEAU:START -->
> Analyse exploratoire et diagnostics des modèles bayésiens, indépendant du moteur — trace plots, R̂, ESS, comparaison LOO/WAIC.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque d'analyse exploratoire des modèles bayésiens, **indépendante du moteur**
d'échantillonnage : elle n'infère rien elle-même. Elle ingère la sortie de PyMC, Stan,
NumPyro ou Pyro dans un format commun, l'`InferenceData` adossé à xarray, puis rend les
diagnostics de chaînes ($\hat{R}$ de Gelman–Rubin, ESS, énergie BFMI), les visualisations
(trace, rank, posterior, forest, posterior predictive checks) et la comparaison de modèles
par LOO et WAIC. C'est la brique qui standardise l'après-échantillonnage, quel que soit le
sampler qui précède.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Vérifier la convergence d'un run MCMC : $\hat{R}$, ESS, divergences, autocorrélation | N'infère rien : sans moteur d'échantillonnage en amont, il n'y a rien à ingérer |
| Visualiser et comparer des a posteriori, faire des posterior predictive checks | Tout part de l'`InferenceData` : des dims et coords mal nommés en amont brouillent les graphes — laisser le convertisseur natif faire le travail |
| Comparer plusieurs modèles bayésiens sur un même jeu — LOO, WAIC | $\hat{R} \approx 1$ ne suffit pas à conclure : croiser avec ESS et le nombre de divergences |
| | L'écosystème se modularise en `arviz-base`, `arviz-stats` et `arviz-plots` : les imports recommandés dépendent de la version |

## Mise en œuvre

- Installation — `uv add arviz`
- Point d'entrée — import Python, `import arviz as az`, sur un objet `InferenceData`
- Prérequis — xarray, NumPy et matplotlib ; backend Bokeh optionnel
- Exécution — dans le process appelant, CPU, mono-nœud ; travaille sur des échantillons déjà produits
- Coût — gratuit, Apache-2.0, aucune limite d'usage ; sous l'ombrelle NumFOCUS

## Écosystème

### Alternatives

- Aucune dans le brain : ArviZ ne concurrence pas les moteurs d'inférence, il se branche en aval.

### Compléments

- [[PyMC]] — Programmation probabiliste en Python — modélisation bayésienne et échantillonnage MCMC (NUTS) sur un backend autodiff (PyTensor). — `pm.sample` rend directement un `InferenceData`
- [[Stan]] — Inférence bayésienne haute performance : langage de modélisation dédié compilé en C++, échantillonneur NUTS de référence, piloté depuis Python via CmdStanPy. — CmdStanPy expose la même structure

## Ressources

- Documentation — https://python.arviz.org
- Dépôt — https://github.com/arviz-devs/arviz

## Voir aussi

- [[MCMC]] · [[Inférence bayésienne]] — les notions implémentées
- [[Comparatif - Outils stats]] — ce qui départage les outils du dossier
