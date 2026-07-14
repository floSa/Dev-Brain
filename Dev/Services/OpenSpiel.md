---
galaxie: dev
type: service
nom: OpenSpiel
alias: [openspiel, open_spiel, open spiel, deepmind openspiel]
pitch: "Collection DeepMind d'environnements et d'algorithmes pour les jeux — 70+ jeux (information parfaite/imparfaite, coopératifs, multi-agents) et les algos de référence (CFR, MCTS, fictitious play, exploitabilité) ; cœur C++ avec bindings Python."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Gymnasium|Gymnasium]]"]
remplace_par: []
status: actif
tags: [reinforcement-learning, game-theory]
url_docs: https://openspiel.readthedocs.io/
url_repo: https://github.com/google-deepmind/open_spiel
---

# OpenSpiel

## Pourquoi

Le terrain de jeu de la **théorie des jeux algorithmique** (Google DeepMind) : 70+ jeux — échecs, go, variantes de poker, jeux de cartes, jeux matriciels, coopératifs — couvrant information parfaite **et** imparfaite, somme nulle ou générale, de 1 à n joueurs. Et, à côté des environnements, les **algorithmes de référence** : [[Counterfactual Regret Minimization|CFR]] et ses variantes, [[Monte Carlo Tree Search|MCTS]], minimax, fictitious play, best response et calcul d'**exploitabilité**, plus des agents RL multi-joueurs. Cœur C++ performant, bindings Python ; utilisable aussi comme bibliothèque C++.

## Quand l'utiliser

- Recherche en **jeux à information imparfaite** (poker, négociation) : CFR/MCCFR et la mesure d'exploitabilité sont les outils canoniques.
- **Multi-agents stratégique** : évaluer des politiques l'une contre l'autre, calculer des équilibres, faire du self-play.
- Reproduire ou prototyper des approches type [[AlphaZero and self-play|AlphaZero]] sur des jeux à règles connues.
- Benchmarker un algorithme sur un éventail large de jeux sous une API unique.

## Quand NE PAS l'utiliser

- RL **mono-agent** classique (contrôle, robotique) → [[Dev/Services/Gymnasium|Gymnasium]] + [[Dev/Services/Stable-Baselines3|Stable-Baselines3]].
- Multi-agents généraliste **hors jeux formels** (essaims, simulation) → PettingZoo (hors brain), API multi-agents de la Farama Foundation.
- Développer un **jeu** à destination de joueurs : OpenSpiel est un outil de recherche, pas un moteur de jeu.

## Déploiement & coût

- Bibliothèque open-source (Apache-2.0), gratuite ; `uv add open_spiel` (wheels Linux et macOS ; sous Windows, passer par WSL ou compiler). Rien à héberger.
- **Single-node** : pas d'infrastructure distribuée fournie — le parallélisme éventuel est à la charge de l'utilisateur.
- Maintenance **active** : releases régulières (v1.6.x en 2026), projet vivant porté par DeepMind.

## Pièges

- API **propre à OpenSpiel** (`state`, `information_state`, joueurs simultanés/séquentiels) — pas l'API Gymnasium ; la transposition d'algos mono-agent demande un vrai travail.
- Ajouter un **jeu custom** performant signifie l'écrire en C++ (et recompiler) ; la version pur Python est plus simple mais lente.
- Les algorithmes en Python sont parfois **research-grade** : valider les performances avant de s'y fier à grande échelle.
- CFR tabulaire explose vite avec la taille du jeu — passer aux variantes Monte-Carlo ou aux approximations deep.

## Alternatives

- [[Dev/Services/Gymnasium|Gymnasium]] — Standard d'API pour les environnements de RL à agent unique (successeur d'OpenAI Gym, par la Farama Foundation) — interface reset/step uniforme + environnements de référence (classic control, Box2D, MuJoCo, Atari) ; le contrat commun entre agents et environnements.

Nuance : Gymnasium pour le mono-agent standard, OpenSpiel dès que le problème est un **jeu** (adversaires, équilibres, information imparfaite). En dehors du brain : PettingZoo (multi-agents général), pgx (jeux vectorisés en JAX).

## Liens

- [[Théorie des jeux]] — le cadre conceptuel (équilibres, somme nulle, information imparfaite).
- [[Counterfactual Regret Minimization]] — l'algorithme phare en information imparfaite, implémenté ici.
- [[Monte Carlo Tree Search]] — la recherche arborescente en information parfaite.
- [[AlphaZero and self-play]] — implémentation pédagogique incluse.
- [[Reinforcement learning]] — le socle mono-agent que ces jeux généralisent.
- [[Dev/Services/Gymnasium|Gymnasium]] — l'API standard côté mono-agent.
- [[Comparatif - Reinforcement learning]] — vue d'ensemble des libs RL.
- Doc : https://openspiel.readthedocs.io/
