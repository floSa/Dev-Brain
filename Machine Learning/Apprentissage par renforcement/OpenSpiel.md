---
role: brique
nom: OpenSpiel
alias: [openspiel, open_spiel, open spiel, deepmind openspiel]
pitch: "Collection DeepMind d'environnements et d'algorithmes pour les jeux — 70+ jeux (information parfaite/imparfaite, coopératifs, multi-agents) et les algos de référence (CFR, MCTS, fictitious play, exploitabilité) ; cœur C++ avec bindings Python."
categorie: ml/rl
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Gymnasium]]"]
complements: []
tags: [reinforcement-learning, game-theory]
url_docs: https://openspiel.readthedocs.io/
url_repo: https://github.com/google-deepmind/open_spiel
---

# OpenSpiel

<!-- AUTO:BANDEAU:START -->
> Collection DeepMind d'environnements et d'algorithmes pour les jeux — 70+ jeux (information parfaite/imparfaite, coopératifs, multi-agents) et les algos de référence (CFR, MCTS, fictitious play, exploitabilité) ; cœur C++ avec bindings Python.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Le terrain de jeu de la **théorie des jeux algorithmique**, signé Google DeepMind : 70+ jeux —
échecs, go, variantes de poker, jeux de cartes, jeux matriciels, coopératifs — couvrant
information parfaite **et** imparfaite, somme nulle ou générale, de 1 à n joueurs. À côté des
environnements viennent les **algorithmes de référence** :
[[Counterfactual Regret Minimization|CFR]] et ses variantes,
[[Monte Carlo Tree Search|MCTS]], minimax, fictitious play, best response et calcul
d'**exploitabilité**, plus des agents RL multi-joueurs. Le cœur est en C++, avec bindings
Python ; la bibliothèque s'utilise aussi directement en C++. Son API lui est propre — `state`,
`information_state`, joueurs simultanés ou séquentiels — et ne suit pas celle de Gymnasium.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Recherche en jeux à **information imparfaite** (poker, négociation) : CFR/MCCFR et la mesure d'exploitabilité sont les outils canoniques | RL **mono-agent** classique (contrôle, robotique) : l'API n'est pas celle de [[Gymnasium]], et transposer un algo mono-agent demande un vrai travail |
| Multi-agents stratégique : évaluer des politiques l'une contre l'autre, calculer des équilibres, faire du self-play | Ajouter un **jeu custom performant** signifie l'écrire en C++ et recompiler ; la version pur Python est plus simple mais lente |
| Reproduire ou prototyper des approches type AlphaZero ([[AlphaZero and self-play]]) sur des jeux à règles connues | CFR tabulaire **explose** avec la taille du jeu : passer aux variantes Monte-Carlo ou aux approximations deep |
| Benchmarker un algorithme sur un éventail large de jeux sous une API unique | Développer un jeu **à destination de joueurs** : c'est un outil de recherche, pas un moteur de jeu |
| | Les algorithmes en Python sont parfois **research-grade** : valider les performances avant de s'y fier à grande échelle |

## Mise en œuvre

- Installation — `uv add open_spiel` ; wheels Linux et macOS, sous Windows passer par WSL ou compiler
- Point d'entrée — API Python (`pyspiel`) ou bibliothèque C++ ; API propre au projet, `state` et `information_state`
- Prérequis — chaîne de compilation C++ dès qu'on ajoute un jeu performant
- Exécution — single-node : aucune infrastructure distribuée fournie, le parallélisme est à la charge de l'utilisateur
- Coût — gratuit, Apache-2.0, rien à héberger ; maintenance active, releases régulières (v1.6.x en 2026)

## Écosystème

### Alternatives

- [[Gymnasium]] — Standard d'API pour les environnements de RL à agent unique (successeur d'OpenAI Gym, par la Farama Foundation) — interface reset/step uniforme + environnements de référence (classic control, Box2D, MuJoCo, Atari) ; le contrat commun entre agents et environnements.
- PettingZoo — l'API multi-agents généraliste, hors jeux formels (pas encore en fiche).
- pgx — jeux vectorisés en JAX (pas encore en fiche).

## Ressources

- Documentation — https://openspiel.readthedocs.io/
- Dépôt — https://github.com/google-deepmind/open_spiel

## Voir aussi

- [[Théorie des jeux]] — le cadre conceptuel : équilibres, somme nulle, information imparfaite
- [[Counterfactual Regret Minimization]] — l'algorithme phare en information imparfaite, implémenté ici
- [[Monte Carlo Tree Search]] — la recherche arborescente en information parfaite
- [[AlphaZero and self-play]] — implémentation pédagogique incluse
- [[Reinforcement learning]] — la notion du dossier : le socle mono-agent que ces jeux généralisent
- [[Comparatif - Reinforcement learning]] — ce qui départage les bibliothèques du dossier
