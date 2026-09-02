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
complements: []
tags: [bayesian, monte-carlo]
url_docs: https://python.arviz.org
url_repo: https://github.com/arviz-devs/arviz
---

# ArviZ

## Pourquoi

Bibliothèque dédiée à l'**analyse exploratoire des modèles bayésiens**, **indépendante du moteur** d'échantillonnage. Elle ingère la sortie de PyMC, Stan (CmdStanPy), NumPyro, Pyro… dans un format commun (`InferenceData`, adossé à xarray) puis fournit les diagnostics de chaînes ($\hat{R}$ de Gelman–Rubin, ESS, énergie BFMI), les visualisations (trace, rank, posterior, forest, PPC) et la **comparaison de modèles** (LOO, WAIC). C'est la brique transverse qui standardise le « après-échantillonnage » quel que soit le sampler.

## Quand l'utiliser

- Vérifier la convergence d'un run MCMC : $\hat{R} \approx 1$, ESS suffisant, divergences, autocorrélation.
- Visualiser et comparer des a posteriori, faire des posterior predictive checks.
- Comparer plusieurs modèles bayésiens (LOO/WAIC) sur un même jeu de données.

## Quand NE PAS l'utiliser

- Construire et échantillonner le modèle : ArviZ ne fait pas d'inférence → [[PyMC]] ou [[Stan]] en amont.
- Diagnostics fréquentistes / tables de régression classiques → [[statsmodels]].

## Déploiement & coût

- Bibliothèque Python (`uv add arviz`), s'appuie sur xarray, NumPy, matplotlib (backend Bokeh optionnel).
- Single-node ; travaille sur des échantillons déjà produits, coût négligeable.
- Apache-2.0, gratuit ; sous l'ombrelle NumFOCUS.

## Pièges

- Tout part de l'`InferenceData` : mal nommer dims/coords en amont brouille les graphes — laisser le convertisseur natif (`pm.sample` renvoie déjà de l'`InferenceData`).
- $\hat{R}$ proche de 1 ne suffit pas : croiser avec ESS et le nombre de divergences avant de conclure à la convergence.
- L'écosystème se modularise (`arviz-base`, `arviz-stats`, `arviz-plots`) : suivre les imports recommandés selon la version.

## Alternatives

- Pas d'alternative directe dans le brain : ArviZ est **complémentaire** des moteurs d'inférence, pas un concurrent. Il se branche en aval de [[PyMC]] et [[Stan]].

## Liens

- Concepts implémentés : [[MCMC]], [[Inférence bayésienne]]
- Moteurs en amont : [[PyMC]], [[Stan]]
- [[Comparatif - Outils stats]] — comparatif des libs statistiques
- Doc : https://python.arviz.org
