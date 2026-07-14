---
galaxie: wiki
type: concept
nom: Offline RL
alias: [offline RL, RL hors ligne, batch RL, offline reinforcement learning, RL hors interaction, batch reinforcement learning]
categorie: concept/rl
domaines: [ml-eng]
tags: [reinforcement-learning, offline-rl, value-function]
---

# Offline RL

## Aperçu

- Apprendre une politique **à partir d'un dataset fixe** de transitions $(s,a,r,s')$ déjà collectées, **sans aucune interaction** nouvelle avec l'environnement. On parle aussi de *batch RL*.
- Motivation : dans beaucoup de domaines (santé, robotique, conduite, recommandation), interagir en ligne est **cher, lent ou dangereux**. On dispose en revanche de logs historiques. L'enjeu est d'en extraire la meilleure politique possible — sans pouvoir tester ses idées.

## Concepts clés

### Le problème central : le distribution shift
- En RL classique ([[Q-learning and DQN]]), l'agent corrige ses erreurs en **revisitant** les états qu'il croit bons. Hors ligne, c'est impossible : aucune nouvelle donnée.
- Conséquence : la cible de Bellman interroge $Q(s', a')$ pour des actions $a'$ **absentes du dataset** (out-of-distribution). Le réseau y produit des valeurs **fausses et surestimées**, que rien ne vient corriger → la politique apprise vise des actions jamais observées et s'effondre.
- C'est l'**erreur d'extrapolation** : le talon d'Achille de l'offline RL.

### Le remède : le pessimisme
- Idée commune à presque tous les algorithmes : **rester proche du support des données** et **pénaliser** les actions mal couvertes.
- **Contrainte de politique** (BCQ, TD3+BC) : forcer la politique à ressembler à celle qui a généré les données (la *behavior policy*).
- **Régularisation de valeur** (CQL — *Conservative Q-Learning*) : abaisser volontairement le $Q$ des actions out-of-distribution, pour ne pas se faire piéger par une surestimation.
- **Sans requêter d'action hors support** (IQL — *Implicit Q-Learning*) : n'évaluer $Q$ que sur des actions présentes dans le dataset, via une régression de quantile sur la valeur.

### Qualité des données
- Un dataset **diversifié** (collecté par plusieurs politiques, même médiocres) permet souvent une meilleure politique qu'un dataset **étroit** d'experts : il couvre plus d'états-actions, donc moins de zones aveugles.
- On ne peut pas dépasser ce que les données **permettent d'inférer** : si une bonne action n'est jamais montrée ni déductible, elle reste hors d'atteinte.

## Les maths, simplement

- Cible de Bellman standard : $y = r + \gamma\,\max_{a'} Q(s', a')$ (cf. [[Bellman equations]]). Le $\max$ sur des $a'$ hors support est précisément ce qui diverge hors ligne.
- CQL ajoute à la perte un terme qui **minimise** $Q$ sur la politique apprise et le **maximise** sur les actions du dataset : $\min_Q\;\alpha\big(\mathbb{E}_{a\sim\pi}[Q(s,a)] - \mathbb{E}_{a\sim\mathcal{D}}[Q(s,a)]\big) + \mathcal{L}_{\text{Bellman}}$ — un $Q$ **borné par le bas**, donc conservateur.

## En pratique

- Pertinent dès qu'on a **des logs mais pas de simulateur** sûr : essais cliniques, contrôle industriel, politiques de recommandation apprises sur l'historique.
- Évaluer une politique hors ligne est **un problème en soi** (*off-policy evaluation*, OPE) : sans interaction, mesurer sa vraie performance est difficile et biaisé. Souvent on valide quand même par un déploiement contrôlé en fin de course.
- Pièges : surestimation silencieuse sur les actions OOD, dataset trop étroit, $\alpha$ de conservatisme mal réglé (trop → politique timide collée au dataset ; trop peu → divergence).
- Lien LLM : **DPO** optimise une politique à partir d'un dataset fixe de préférences, sans boucle d'interaction — c'est de l'alignement *offline* (cf. [[RLHF and DPO]]).

## Approches voisines & alternatives

- [[Reinforcement learning]] — le cadre général ; l'offline RL en est la variante « sans interaction ».
- [[Q-learning and DQN]] — la brique value-based dont l'offline RL hérite la surestimation, en pire (pas de correction par revisite).
- [[Imitation learning]] — autre façon d'apprendre sans récompense en ligne ; le behavioral cloning est le cas dégénéré « copier les données » sans raisonner sur la valeur.
- [[Model-based RL]] — apprendre un modèle du dataset puis planifier dessus est une voie offline (MOReL, MOPO), avec le risque d'exploitation du modèle.
- [[RLHF and DPO]] — DPO est, de fait, du RL de préférences **offline** pour les LLM.

## Pour aller plus loin

- Levine et al. (2020) — *Offline Reinforcement Learning: Tutorial, Review, and Perspectives* (la synthèse de référence).
- Fujimoto et al. (2019) — *BCQ* (mise en évidence de l'erreur d'extrapolation).
- Kumar et al. (2020) — *Conservative Q-Learning (CQL)* ; Kostrikov et al. (2021) — *Implicit Q-Learning (IQL)*.
- Sutton & Barto — *Reinforcement Learning*, ch. 11 (off-policy methods, deadly triad).
