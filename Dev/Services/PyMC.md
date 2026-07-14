---
galaxie: dev
type: service
nom: PyMC
alias: [pymc3, pymc-devs]
pitch: "Programmation probabiliste en Python — modélisation bayésienne et échantillonnage MCMC (NUTS) sur un backend autodiff (PyTensor)."
categorie: tooling/stats
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Stan|Stan]]"]
remplace_par: []
status: actif
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

- Performance maximale sur gros modèles / grandes données, ou réutilisation d'un modèle hors Python → [[Dev/Services/Stan|Stan]].
- Simple test d'hypothèse ou GLM fréquentiste → [[Dev/Services/statsmodels|statsmodels]], [[Dev/Services/scipy.stats|scipy.stats]].
- Inspection / diagnostics des chaînes : PyMC les délègue à [[Dev/Services/ArviZ|ArviZ]] (renvoie un `InferenceData`).

## Déploiement & coût

- Bibliothèque Python (`uv add pymc`), s'appuie sur PyTensor + NumPy.
- Single-node ; échantillonnage multi-chaînes parallélisé sur les cœurs CPU (GPU possible via backends [[Dev/Services/JAX|JAX]]/Numba).
- Apache-2.0, gratuit ; sous l'ombrelle NumFOCUS.

## Pièges

- Backend mouvant historiquement (Theano → Aesara → PyTensor) : épingler la version, vérifier la compat des tutoriels anciens (`pymc3` ≠ `pymc`).
- Divergences NUTS sur modèles hiérarchiques : reparamétrer (non-centré) plutôt qu'augmenter `target_accept` à l'aveugle.
- Compilation du graphe au premier `sample` : surcoût de démarrage sensible sur petits modèles.

## Alternatives

- [[Dev/Services/Stan|Stan]] — Inférence bayésienne haute performance : langage de modélisation dédié compilé en C++, échantillonneur NUTS de référence, piloté depuis Python via CmdStanPy.

## Liens

- Concepts implémentés : [[Wiki/Concepts/Inférence bayésienne|Inférence bayésienne]], [[Wiki/Concepts/MCMC|MCMC]], [[Wiki/Concepts/Estimation MAP|Estimation MAP]], [[Wiki/Concepts/Chaînes de Markov|Chaînes de Markov]]
- Diagnostics & viz a posteriori : [[Dev/Services/ArviZ|ArviZ]]
- [[Comparatif - Outils stats]] — comparatif des libs statistiques
- Doc : https://www.pymc.io
