---
galaxie: wiki
type: concept
nom: Counterfactual Regret Minimization
alias: [CFR, counterfactual regret minimization, minimisation du regret contrefactuel, CFR+, regret matching, Deep CFR, MCCFR]
categorie: concept/rl
domaines: [ml-eng, ai-eng]
tags: [game-theory, regret-minimization, self-play]
---

# Counterfactual Regret Minimization

## Aperçu

- Algorithme itératif qui calcule une stratégie d'équilibre dans les **jeux à information imparfaite** (poker) en minimisant, à chaque point de décision, un **regret contrefactuel**.
- Famille de référence derrière les IA qui ont battu les pros au poker (Libratus, Pluribus). Là où [[Monte Carlo Tree Search|MCTS]] et le self-play d'[[AlphaZero and self-play|AlphaZero]] excellent en information parfaite, CFR est l'outil de l'information cachée.

## Concepts clés

### Information set et regret

- Le joueur ne connaît pas l'état exact mais un **information set** : l'ensemble des états indistinguables compte tenu de son information (ses cartes, l'historique public).
- On joue le jeu en self-play sur de nombreuses itérations ; pour chaque action à chaque information set, on accumule le **regret** : « combien aurais-je gagné en plus en jouant toujours cette action ? ».
- **Contrefactuel** : le regret est pondéré par la probabilité d'atteindre cet information set *si le joueur cherchait à l'atteindre*. Cette décomposition transforme le regret global du jeu en regrets locaux, minimisables indépendamment.

### Regret matching et stratégie moyenne

- À chaque itération, la stratégie est tirée proportionnellement au **regret positif cumulé** (regret matching) : les actions qu'on a regretté de ne pas jouer gagnent en probabilité.
- Résultat clé : c'est la **stratégie moyenne** sur toutes les itérations (pas la dernière) qui converge vers l'[[Théorie des jeux|équilibre de Nash]] dans les jeux à somme nulle à deux joueurs.

### Variantes

- **CFR+** : regrets bornés à zéro et moyennage pondéré → nettement plus rapide (a résolu le heads-up limit hold'em).
- **MCCFR** (Monte-Carlo CFR) : n'échantillonne qu'une partie de l'arbre par itération → passe à l'échelle.
- **Deep CFR** : un réseau approxime les regrets → s'affranchit du stockage tabulaire de tous les information sets.

## Les maths, simplement

- Regret cumulé d'une action $a$ à l'information set $I$ : $R^T(I,a) = \sum_{t=1}^{T} \big(v_t(I, a) - v_t(I)\big)$ — écart de valeur contrefactuelle entre « jouer $a$ » et la stratégie suivie.
- Regret matching : $\sigma^{T+1}(I,a) \propto \max\!\big(R^T(I,a),\,0\big)$ — probabilité proportionnelle au regret positif.
- Le regret total est borné en $O(\sqrt{T})$ → le regret **moyen** tend vers 0, et une paire de stratégies sans regret forme un équilibre de Nash (somme nulle).

## En pratique

- Le bon outil quand l'**information est imparfaite face à un adversaire** : poker, négociation, enchères, sécurité (jeux attaquant/défenseur).
- Exige une structure de jeu explicite (arbre d'information sets) ; les variantes Monte-Carlo et deep repoussent la limite de taille.
- Différence avec le RL classique : CFR vise un **équilibre** contre un adversaire qui s'adapte, pas la maximisation d'une récompense contre un environnement fixe (cf. [[Reinforcement learning]]).
- Pièges : converge en stratégie **moyenne** (oublier de moyenner = pas d'équilibre) ; au-delà de deux joueurs ou en somme non nulle, plus de garantie de Nash.
- Côté outils : [[Dev/Services/OpenSpiel|OpenSpiel]] implémente CFR, CFR+, MCCFR et le calcul d'exploitabilité sur 70+ jeux.

## Approches voisines & alternatives

- [[Théorie des jeux]] — CFR est une méthode constructive pour atteindre l'équilibre de Nash en information imparfaite.
- [[AlphaZero and self-play]] — self-play + MCTS, l'approche duale pour l'information **parfaite**.
- [[Monte Carlo Tree Search]] — recherche en information parfaite, mal adaptée aux information sets.
- [[Multi-armed bandits]] — même socle de minimisation du regret, sans structure d'arbre de jeu.
- [[Exploration vs exploitation]] — le regret est la mesure commune à ces approches.

## Pour aller plus loin

- Zinkevich et al. (2007, NeurIPS) — *Regret Minimization in Games with Incomplete Information* (CFR).
- Tammelin (2014) — *Solving Large Imperfect Information Games Using CFR+*.
- Brown & Sandholm (2017, Science) — *Superhuman AI for heads-up no-limit poker: Libratus*.
- Brown et al. (2019) — *Deep Counterfactual Regret Minimization*.
