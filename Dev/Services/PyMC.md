---
role: brique
nom: PyMC
alias: [pymc3, pymc-devs]
pitch: "Programmation probabiliste en Python — modélisation bayésienne et échantillonnage MCMC (NUTS) sur un backend autodiff (PyTensor)."
categorie: stats/bayesien
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Stan]]"]
complements: []
tags: [bayesian, probabilistic-programming, monte-carlo, markov, prior]
url_docs: https://www.pymc.io
url_repo: https://github.com/pymc-devs/pymc
---

# PyMC

## Pourquoi

Framework de **programmation probabiliste** en Python pur. On décrit un modèle génératif (priors, vraisemblance) avec une syntaxe lisible dans un `with pm.Model()`, et PyMC infère l'a posteriori. Le moteur d'échantillonnage par défaut est **NUTS** (variante auto-réglée de Hamiltonian Monte Carlo), porté par un backend de différentiation automatique (PyTensor, successeur de Theano/Aesara). Là où statsmodels estime un modèle figé, PyMC laisse spécifier n'importe quel modèle hiérarchique sur mesure et en quantifie l'incertitude.

## Quand l'utiliser

- Modèle bayésien sur mesure : régression hiérarchique, mélanges, modèles à effets aléatoires, priors informatifs.
- Besoin de la distribution a posteriori complète (incertitude, intervalles de crédibilité), pas seulement d'un point.
- Prototypage rapide en Python pur, sans changer de langage ni compiler.

## Quand NE PAS l'utiliser

- Performance maximale sur gros modèles / grandes données, ou réutilisation d'un modèle hors Python → [[Stan]].
- Simple test d'hypothèse ou GLM fréquentiste → [[statsmodels]], [[scipy.stats]].
- Inspection / diagnostics des chaînes : PyMC les délègue à [[ArviZ]] (renvoie un `InferenceData`).

## Déploiement & coût

- Bibliothèque Python (`uv add pymc`), s'appuie sur PyTensor + NumPy.
- Single-node ; échantillonnage multi-chaînes parallélisé sur les cœurs CPU (GPU possible via backends [[JAX]]/Numba).
- Apache-2.0, gratuit ; sous l'ombrelle NumFOCUS.

## Pièges

- Backend mouvant historiquement (Theano → Aesara → PyTensor) : épingler la version, vérifier la compat des tutoriels anciens (`pymc3` ≠ `pymc`).
- Divergences NUTS sur modèles hiérarchiques : reparamétrer (non-centré) plutôt qu'augmenter `target_accept` à l'aveugle.
- Compilation du graphe au premier `sample` : surcoût de démarrage sensible sur petits modèles.

## Alternatives

- [[Stan]] — Inférence bayésienne haute performance : langage de modélisation dédié compilé en C++, échantillonneur NUTS de référence, piloté depuis Python via CmdStanPy.

## Liens

- Concepts implémentés : [[Inférence bayésienne]], [[MCMC]], [[Estimation MAP]], [[Chaînes de Markov]]
- Diagnostics & viz a posteriori : [[ArviZ]]
- [[Comparatif - Outils stats]] — comparatif des libs statistiques
- Doc : https://www.pymc.io
