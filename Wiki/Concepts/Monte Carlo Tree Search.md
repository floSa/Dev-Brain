---
galaxie: wiki
type: concept
nom: Monte Carlo Tree Search
alias: [MCTS, Monte Carlo Tree Search, recherche arborescente Monte-Carlo, UCT, UCB applied to trees]
categorie: concept/rl
domaines: [ml-eng, ai-eng]
tags: [planning, monte-carlo, model-based-rl]
---

# Monte Carlo Tree Search

## Aperçu

- Algorithme de **planification** qui construit un arbre de recherche incrémental : on simule des parties depuis l'état courant et on concentre l'effort sur les branches prometteuses.
- N'exige ni heuristique de domaine ni fonction de valeur apprise — une politique de simulation, même aléatoire, suffit à estimer la valeur d'une action par moyenne des retours (Monte-Carlo). C'est ce qui l'a rendu dominant au Go avant le deep learning.

## Concepts clés

### Les quatre phases

- **Sélection** : depuis la racine, descendre l'arbre en choisissant à chaque nœud l'enfant qui maximise un critère d'arbitrage exploration/exploitation (cf. [[Exploration vs exploitation]]), jusqu'à un nœud non pleinement développé.
- **Expansion** : ajouter un enfant au nœud atteint.
- **Simulation (rollout)** : jouer jusqu'à un état terminal selon une politique par défaut (souvent aléatoire) et récolter un retour.
- **Rétropropagation** : remonter ce retour le long du chemin parcouru, mettre à jour le compteur de visites $N$ et la valeur moyenne $Q$ de chaque nœud.

### UCT — le critère de sélection

- **UCT** (Upper Confidence bounds applied to Trees) traite chaque choix d'enfant comme un [[Multi-armed bandits|bandit]] : équilibrer la valeur estimée et un bonus d'exploration qui décroît avec le nombre de visites.
- Garantit asymptotiquement la convergence vers l'action optimale : le sous-arbre optimal est visité de plus en plus souvent.

### Anytime et croissance asymétrique

- **Anytime** : on peut s'arrêter à tout moment et renvoyer la meilleure action courante — plus le budget de simulations est grand, meilleure est la décision.
- L'arbre croît **asymétriquement** : profond sur les lignes fortes, court sur les coups faibles — pas l'exploration uniforme en largeur du minimax classique.

## Les maths, simplement

- Score UCT d'un enfant : $\text{UCT} = \underbrace{\tfrac{W_i}{N_i}}_{\text{exploitation}} + c\,\underbrace{\sqrt{\tfrac{\ln N_p}{N_i}}}_{\text{exploration}}$ — $W_i$ somme des retours de l'enfant $i$, $N_i$ ses visites, $N_p$ celles du parent, $c$ règle l'exploration.
- Le terme de gauche favorise les coups à fort taux de victoire, celui de droite les coups peu essayés. Quand $N_i$ grandit, le bonus s'efface.

## En pratique

- Pertinent quand un **modèle/simulateur** de l'environnement est disponible (règles du jeu, moteur physique) : jeux à somme nulle, planification, ordonnancement.
- Couplé à des réseaux profonds dans [[AlphaZero and self-play|AlphaZero]] : un réseau remplace les rollouts aléatoires (évaluation de position) et biaise la sélection (probabilités a priori des coups) — le saut qui a battu les pros au Go.
- Réémerge en AI engineering pour la **recherche au moment du test** des LLM (tree-of-thought, recherche guidée par un vérificateur) — cf. [[RL for LLMs]], [[Chain-of-Thought]].
- Pièges : coût des simulations (un rollout = une partie entière), facteur de branchement élevé, et information imparfaite mal gérée par le MCTS vanille (cf. [[Théorie des jeux]], [[Counterfactual Regret Minimization|CFR]]).
- Côté outils : [[Dev/Services/OpenSpiel|OpenSpiel]] fournit MCTS/UCT (et une implémentation pédagogique d'AlphaZero) sur ses 70+ jeux.

## Approches voisines & alternatives

- [[Model-based RL]] — MCTS est l'archétype de la planification par recherche quand un modèle est disponible.
- [[AlphaZero and self-play]] — marie MCTS et réseaux profonds appris par self-play.
- [[Value functions]] — une valeur apprise peut tronquer les rollouts (évaluer une position sans simuler jusqu'au bout).
- [[Multi-armed bandits]] — UCT applique la borne de confiance supérieure (UCB) à chaque nœud.
- [[Counterfactual Regret Minimization]] — l'approche de référence en information imparfaite, là où MCTS peine.

## Pour aller plus loin

- Coulom (2006) — *Efficient Selectivity and Backup Operators in Monte-Carlo Tree Search* (introduit l'idée).
- Kocsis & Szepesvári (2006) — *Bandit based Monte-Carlo Planning* (UCT).
- Browne et al. (2012) — *A Survey of Monte Carlo Tree Search Methods*.
- Silver et al. (2016) — *Mastering the game of Go with deep neural networks and tree search* (AlphaGo : MCTS + réseaux profonds).
