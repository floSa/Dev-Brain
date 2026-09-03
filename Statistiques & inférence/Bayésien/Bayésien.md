---
role: hub
nom: Bayésien
alias: [statistique bayésienne, inférence bayésienne (dossier)]
pitch: Traiter le paramètre comme une variable aléatoire — une distribution en sortie plutôt qu'un point, au prix d'un a priori assumé et d'un échantillonnage à faire converger.
domaines: [data-sci]
tags: [bayesian, prior, probabilistic-programming, monte-carlo, markov, point-estimation]
---

# Bayésien

> Traiter le paramètre comme une variable aléatoire — une distribution en sortie plutôt qu'un point, au prix d'un a priori assumé et d'un échantillonnage à faire converger.

## Ce qu'il faut comprendre

- **Le clivage avec [[Tests & estimation]] n'est pas une question de goût, c'est ce que la sortie signifie.** Le fréquentiste répond « les données seraient improbables si H0 était vraie » ; le bayésien répond directement sur l'hypothèse, $P(\theta \mid \text{données})$. C'est ce que la plupart des gens croient lire dans une p-value, et c'est la raison principale de venir ici. [[Inférence bayésienne]] pose le cadre.
- **L'a priori est le prix d'entrée, et il ne se contourne pas.** Il se déclare, se justifie et se teste — un a priori mal choisi déplace la conclusion sans que rien ne le signale. En contrepartie il fait travailler l'information externe, ce qu'aucun test fréquentiste ne sait faire : petits échantillons, données rares, connaissance métier chiffrée.
- **Deux façons d'obtenir l'a posteriori, et une seule est générale.** Les [[A priori conjugués]] le donnent en forme fermée — pas d'intégrale, pas de simulation, mise à jour en ligne triviale — mais seulement pour une poignée de couples classiques. Partout ailleurs, c'est [[MCMC]] : on échantillonne une cible connue à une constante près en construisant une [[Chaînes de Markov|chaîne de Markov]] dont la loi stationnaire est cette cible.
- **Le diagnostic n'est pas optionnel, et c'est le piège du domaine** : une chaîne qui n'a pas convergé produit des chiffres d'apparence parfaitement normale. R̂, ESS, trace plots, divergences — [[ArviZ]] fait ce travail indépendamment du moteur, et se branche aussi bien sur [[PyMC]] que sur [[Stan]]. C'est le complément par défaut des deux, pas un extra.
- **[[Estimation MAP]] est le pont vers le fréquentiste** : c'est le [[Maximum de vraisemblance]] auquel on ajoute un a priori, donc un seul point en sortie. Utile comme initialisation ou comme lecture rapide, mais y réduire un a posteriori revient à jeter ce pour quoi on est venu — l'incertitude et la forme de la distribution.

## Choisir

- Un modèle bayésien à écrire en Python, dans un pipeline Python → [[PyMC]].
- Un modèle difficile, ou une équipe déjà sur le langage Stan → [[Stan]], dont l'échantillonneur NUTS est la référence.
- Diagnostiquer et comparer des a posteriori, quel que soit le moteur → [[ArviZ]].
- Un modèle standard, un gros échantillon, une p-value attendue par l'interlocuteur → [[Tests & estimation]], plus court et plus lisible pour tout le monde.
- L'effet causal d'une intervention datée sur une série → [[CausalImpact]], bayésien lui aussi mais rangé au niveau du domaine avec [[Inférence causale]].

<!-- AUTO:START -->
### Notions
- [[A priori conjugués]] — domaines : data-sci
- [[Estimation MAP]] — domaines : data-sci
- [[Inférence bayésienne]] — domaines : data-sci
- [[MCMC]] — domaines : data-sci

### Briques
- [[ArviZ]] — Analyse exploratoire et diagnostics des modèles bayésiens, indépendant du moteur — trace plots, R̂, ESS, comparaison LOO/WAIC.
- [[PyMC]] — Programmation probabiliste en Python — modélisation bayésienne et échantillonnage MCMC (NUTS) sur un backend autodiff (PyTensor).
- [[Stan]] — Inférence bayésienne haute performance : langage de modélisation dédié compilé en C++, échantillonneur NUTS de référence, piloté depuis Python via CmdStanPy.
<!-- AUTO:END -->
