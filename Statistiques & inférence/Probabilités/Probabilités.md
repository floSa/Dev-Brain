---
role: hub
nom: Probabilités
alias: [théorie des probabilités, processus stochastiques]
pitch: Ce qui rend l'inférence possible — les théorèmes qui disent qu'un échantillon converge, et les processus qui modélisent le hasard dans le temps.
domaines: [data-sci]
tags: [probability, convergence, concentration, stochastic-process, markov, monte-carlo]
---

# Probabilités

> Ce qui rend l'inférence possible — les théorèmes qui disent qu'un échantillon converge, et les processus qui modélisent le hasard dans le temps.

## Ce qu'il faut comprendre

- **Ce dossier ne calcule rien sur des données ; il dit pourquoi les calculs des autres dossiers ont le droit d'exister.** [[Loi des grands nombres]] justifie qu'une moyenne empirique estime une espérance, donc l'échantillonnage lui-même. [[Théorème central limite]] justifie les [[Intervalles de confiance]] et les tests paramétriques : c'est lui, et non une propriété du monde, qui explique l'omniprésence de la gaussienne.
- **Ces deux théorèmes sont asymptotiques, et c'est leur limite pratique** : ils disent qu'on converge, pas où on en est à $n = 200$. [[Inégalités de concentration]] répond à cette question — Markov, Chebyshev, Hoeffding, Bernstein bornent l'écart à $n$ **fini**, sans passer à la limite. C'est la version utilisable quand il faut une garantie chiffrée plutôt qu'une promesse.
- **Un processus stochastique modélise le hasard qui se déroule**, là où les théorèmes ci-dessus regardent un tas d'observations. [[Chaînes de Markov]] pour un état qui n'a pas de mémoire du chemin parcouru ; [[Processus de Poisson]] pour des événements indépendants à taux constant, dont les inter-arrivées sont exponentielles ; [[Mouvement brownien]] pour la version à temps et trajectoires continus.
- **Trois de ces pages sont la mécanique d'outils qu'on utilise ailleurs sans le voir.** Les [[Chaînes de Markov]] sont la brique de [[MCMC]] — c'est leur loi stationnaire qu'on échantillonne, et l'ergodicité qui rend l'échantillon valide. Le [[Mouvement brownien]] est le socle des modèles génératifs par diffusion. Le [[Processus de Poisson]] est le modèle par défaut de tout comptage d'événements — trafic, pannes, arrivées.
- **La frontière avec [[Mathématiques]] est assumée et datée.** Ces six pages y auraient aussi leur place, mais les quatre piliers de ce domaine sont l'algèbre linéaire, l'optimisation, la théorie de l'information et la théorie de l'apprentissage. Ces pages-ci se justifient toutes par l'inférence, et c'est pourquoi elles sont rangées avec elle (arbitrage du 2026-09-05, lot 4).

## Choisir

- Comprendre pourquoi un intervalle de confiance est légitime → [[Théorème central limite]].
- Une garantie chiffrée à $n$ fini, pas une promesse asymptotique → [[Inégalités de concentration]].
- Modéliser des transitions entre états → [[Chaînes de Markov]].
- Modéliser des arrivées ou des comptages d'événements → [[Processus de Poisson]].
- Simuler ces lois en Python → [[scipy.stats]], au dossier [[Tests & estimation]].
- Les échantillonner pour approcher un a posteriori → [[MCMC]], au dossier [[Bayésien]].

<!-- AUTO:START -->
### Notions
- [[Chaînes de Markov]] — domaines : data-sci
- [[Inégalités de concentration]] — domaines : data-sci
- [[Loi des grands nombres]] — domaines : data-sci
- [[Mouvement brownien]] — domaines : data-sci
- [[Processus de Poisson]] — domaines : data-sci
- [[Théorème central limite]] — domaines : data-sci
<!-- AUTO:END -->
