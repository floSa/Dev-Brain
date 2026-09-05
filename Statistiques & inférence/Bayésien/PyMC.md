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
complements: ["[[ArviZ]]"]
tags: [bayesian, probabilistic-programming, monte-carlo, markov, prior]
url_docs: https://www.pymc.io
url_repo: https://github.com/pymc-devs/pymc
---

# PyMC

<!-- AUTO:BANDEAU:START -->
> Programmation probabiliste en Python — modélisation bayésienne et échantillonnage MCMC (NUTS) sur un backend autodiff (PyTensor).

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework de programmation probabiliste en Python pur : on décrit un modèle génératif —
priors, vraisemblance — dans un `with pm.Model()`, et PyMC infère l'a posteriori.
L'échantillonneur par défaut est **NUTS**, variante auto-réglée du Hamiltonian Monte Carlo,
portée par un backend de différentiation automatique, PyTensor. Là où statsmodels estime un
modèle figé, PyMC laisse spécifier n'importe quel modèle hiérarchique sur mesure et en
quantifie l'incertitude. Le graphe est compilé au premier `sample`, ce qui donne un
surcoût de démarrage sensible sur les petits modèles.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Modèle bayésien sur mesure : régression hiérarchique, mélanges, effets aléatoires, priors informatifs | Backend historiquement mouvant — Theano, puis Aesara, puis PyTensor : épingler la version, et se méfier des tutoriels `pymc3`, qui n'est pas `pymc` |
| Vouloir la distribution a posteriori complète — incertitude, intervalles de crédibilité — pas seulement un point | Divergences NUTS sur modèles hiérarchiques : la réponse est le **reparamétrage non centré**, pas `target_accept` poussé à l'aveugle |
| Prototyper vite en Python pur, sans changer de langage ni compiler | Compilation du graphe au premier `sample` : surcoût de démarrage sensible sur les petits modèles |

## Mise en œuvre

- Installation — `uv add pymc`
- Point d'entrée — import Python, modèle déclaré dans un `with pm.Model()`, inférence par `pm.sample`
- Prérequis — PyTensor et NumPy ; backends [[JAX]] ou Numba en option pour le GPU
- Exécution — dans le process appelant, mono-nœud, chaînes parallélisées sur les cœurs CPU
- Coût — gratuit, Apache-2.0, aucune limite d'usage ; sous l'ombrelle NumFOCUS

## Écosystème

### Alternatives

- [[Stan]] — Inférence bayésienne haute performance : langage de modélisation dédié compilé en C++, échantillonneur NUTS de référence, piloté depuis Python via CmdStanPy.

### Compléments

- [[ArviZ]] — Analyse exploratoire et diagnostics des modèles bayésiens, indépendant du moteur — trace plots, R̂, ESS, comparaison LOO/WAIC. — PyMC lui délègue tout le diagnostic et rend un `InferenceData`

## Ressources

- Documentation — https://www.pymc.io
- Dépôt — https://github.com/pymc-devs/pymc

## Voir aussi

- [[Inférence bayésienne]] · [[MCMC]] · [[Estimation MAP]] · [[Chaînes de Markov]] — les notions implémentées
- [[Comparatif - Outils stats]] — ce qui départage les outils du dossier
