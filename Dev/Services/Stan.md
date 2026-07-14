---
galaxie: dev
type: service
nom: Stan
alias: [CmdStanPy, cmdstanpy, Stan language]
pitch: "Inférence bayésienne haute performance : langage de modélisation dédié compilé en C++, échantillonneur NUTS de référence, piloté depuis Python via CmdStanPy."
categorie: tooling/stats
licence_type: open-source
hosted: self
maturite: production
langage: C++ / Python
scaling: single-node
alternatives: ["[[Dev/Services/PyMC|PyMC]]"]
remplace_par: []
status: actif
tags: [bayesian, probabilistic-programming, monte-carlo, markov]
url_docs: https://mc-stan.org
url_repo: https://github.com/stan-dev/cmdstanpy
---

# Stan

## Pourquoi

Plateforme de référence pour l'inférence bayésienne. On écrit le modèle dans un **langage dédié** (blocs `data`, `parameters`, `model`), Stan le **compile en C++** puis échantillonne l'a posteriori avec un **NUTS** réputé pour sa robustesse et sa vitesse. Stan est l'implémentation qui a popularisé NUTS ; les autres frameworks s'y comparent. Depuis Python, l'accès se fait via **CmdStanPy**, une interface pure-Python légère qui pilote l'exécutable CmdStan (alternatives historiques : PyStan, plus lourde à installer).

## Quand l'utiliser

- Modèle bayésien exigeant en performance / taille, ou destiné à être réutilisé hors Python (R, ligne de commande, Julia).
- Besoin de l'échantillonneur le plus éprouvé et de diagnostics de convergence soignés.
- Modèle stable que l'on veut versionner comme un artefact `.stan` indépendant du langage hôte.

## Quand NE PAS l'utiliser

- Prototypage rapide tout en Python, modèle évoluant souvent → [[Dev/Services/PyMC|PyMC]] (pas de compilation, syntaxe Python).
- Statistique fréquentiste classique (GLM, séries temporelles, tests) → [[Dev/Services/statsmodels|statsmodels]].
- Exploration des résultats : déléguée à [[Dev/Services/ArviZ|ArviZ]] (CmdStanPy expose un `InferenceData`).

## Déploiement & coût

- `uv add cmdstanpy` puis `install_cmdstan()` télécharge et compile la toolchain CmdStan (C++) — prévoir un compilateur.
- Single-node ; chaînes parallélisées sur les cœurs. Première exécution lente (compilation du modèle), puis binaire réutilisé.
- BSD-3-Clause (Stan et CmdStanPy), gratuit.

## Pièges

- Coût de compilation au premier run et à chaque modification du `.stan` : mettre en cache le binaire compilé.
- Toolchain C++ requise : source d'échecs d'install en CI/Windows → privilégier conteneur ou cmdstan pré-construit.
- Le langage Stan est typé et strict (déclarer dimensions et contraintes) : plus rigide que la syntaxe PyMC, mais protège des erreurs.

## Alternatives

- [[Dev/Services/PyMC|PyMC]] — Programmation probabiliste en Python — modélisation bayésienne et échantillonnage MCMC (NUTS) sur un backend autodiff (PyTensor).

## Liens

- Concepts implémentés : [[Wiki/Concepts/Inférence bayésienne|Inférence bayésienne]], [[Wiki/Concepts/MCMC|MCMC]]
- Diagnostics & viz a posteriori : [[Dev/Services/ArviZ|ArviZ]]
- [[Comparatif - Outils stats]] — comparatif des libs statistiques
- Doc : https://mc-stan.org/cmdstanpy
