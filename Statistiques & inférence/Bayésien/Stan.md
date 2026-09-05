---
role: brique
nom: Stan
alias: [CmdStanPy, cmdstanpy, Stan language]
pitch: "Inférence bayésienne haute performance : langage de modélisation dédié compilé en C++, échantillonneur NUTS de référence, piloté depuis Python via CmdStanPy."
categorie: stats/bayesien
famille: paquet
licence_type: open-source
maturite: production
langage: C++ / Python
alternatives: ["[[PyMC]]"]
complements: ["[[ArviZ]]"]
tags: [bayesian, probabilistic-programming, monte-carlo, markov]
url_docs: https://mc-stan.org
url_repo: https://github.com/stan-dev/cmdstanpy
---

# Stan

<!-- AUTO:BANDEAU:START -->
> Inférence bayésienne haute performance : langage de modélisation dédié compilé en C++, échantillonneur NUTS de référence, piloté depuis Python via CmdStanPy.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie C++ / Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme de référence pour l'inférence bayésienne. Le modèle s'écrit dans un **langage
dédié** — blocs `data`, `parameters`, `model` —, Stan le **compile en C++**, puis
échantillonne l'a posteriori avec le NUTS qu'il a lui-même popularisé et auquel les autres
frameworks se comparent. Conséquence de ce détour par la compilation : le modèle devient un
artefact `.stan` versionnable et réutilisable hors Python (R, Julia, ligne de commande),
mais chaque modification repaie le coût de compilation. Depuis Python, l'accès passe par
**CmdStanPy**, interface légère qui pilote l'exécutable CmdStan.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Modèle bayésien exigeant en performance ou en taille | Coût de compilation au premier run **et à chaque modification** du `.stan` : mettre en cache le binaire |
| Modèle destiné à être réutilisé hors Python — R, Julia, ligne de commande | Toolchain C++ requise : source classique d'échecs d'installation en CI et sous Windows — conteneur ou CmdStan pré-construit |
| Versionner le modèle comme un artefact indépendant du langage hôte | Langage typé et strict : dimensions et contraintes à déclarer, plus rigide que la syntaxe Python |
| Vouloir l'échantillonneur le plus éprouvé et des diagnostics de convergence soignés | |

## Mise en œuvre

- Installation — `uv add cmdstanpy`, puis `install_cmdstan()` qui télécharge et compile la toolchain
- Point d'entrée — fichier `.stan` compilé, piloté depuis Python par CmdStanPy
- Prérequis — un compilateur C++ sur la machine ; c'est la contrainte structurante
- Exécution — mono-nœud, chaînes parallélisées sur les cœurs ; première exécution lente, binaire réutilisé ensuite
- Coût — gratuit, BSD-3-Clause pour Stan comme pour CmdStanPy

## Écosystème

### Alternatives

- [[PyMC]] — Programmation probabiliste en Python — modélisation bayésienne et échantillonnage MCMC (NUTS) sur un backend autodiff (PyTensor).

### Compléments

- [[ArviZ]] — Analyse exploratoire et diagnostics des modèles bayésiens, indépendant du moteur — trace plots, R̂, ESS, comparaison LOO/WAIC. — CmdStanPy expose un `InferenceData`, et l'exploration des résultats lui est déléguée

## Ressources

- Documentation — https://mc-stan.org
- Dépôt — https://github.com/stan-dev/cmdstanpy

## Voir aussi

- [[Inférence bayésienne]] · [[MCMC]] — les notions implémentées
- [[Comparatif - Outils stats]] — ce qui départage les outils du dossier
