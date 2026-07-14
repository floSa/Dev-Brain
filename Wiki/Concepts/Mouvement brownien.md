---
galaxie: wiki
type: concept
nom: Mouvement brownien
alias: [Brownian motion, processus de Wiener, Wiener process]
categorie: concept/stats
domaines: [data-sci]
tags: [stochastic-process, probability]
---

# Mouvement brownien

## Aperçu

- Processus stochastique à **temps continu** et **trajectoires continues**, dont les incréments sont indépendants, stationnaires et gaussiens.
- Limite d'échelle de la marche aléatoire et brique de base du **calcul stochastique** (finance, physique, modèles génératifs par diffusion).

## Concepts clés

### Définition (processus de Wiener)
- Part de 0 : $W_0 = 0$ ; incréments gaussiens, indépendants et stationnaires ; trajectoire continue.
- Sur une durée $t-s$, l'incrément a pour variance exactement $t-s$.

### Trajectoires
- Continues partout mais dérivables nulle part : infiniment « rugueuses », d'où la nécessité d'un calcul dédié.
- Auto-similarité : un zoom sur la trajectoire ressemble (en loi) à la trajectoire entière.

### Du discret au continu
- Théorème de Donsker : une marche aléatoire renormalisée converge vers le mouvement brownien — un [[Théorème central limite]] « fonctionnel » (sur les trajectoires, pas un seul point).

### Calcul stochastique
- Intégrale et lemme d'Itô permettent de manipuler des fonctions du brownien.
- Équations différentielles stochastiques (EDS) : terme de dérive (tendance) + terme de diffusion piloté par $dW_t$.

## Les maths, simplement

- Incréments : $W_t - W_s \sim \mathcal{N}(0,\ t-s)$, indépendants sur intervalles disjoints, $W_0 = 0$.
- Moments : $\mathbb{E}[W_t] = 0$, $\text{Var}(W_t) = t$ — la dispersion croît comme $\sqrt{t}$.
- EDS générique : $dX_t = \mu(X_t,t)\,dt + \sigma(X_t,t)\,dW_t$ (dérive + diffusion).

## En pratique

- Finance : modèle de Black–Scholes, mouvement brownien géométrique pour les prix d'actifs.
- Physique : diffusion, équation de la chaleur ; ML : modèles génératifs par diffusion (bruitage/débruitage progressif).
- Simulation : discrétisation d'Euler–Maruyama, en sommant des incréments $\sqrt{\Delta t}\,\mathcal{N}(0,1)$.

## Approches voisines & alternatives

- [[Chaînes de Markov]] — le brownien est un processus de Markov à temps et espace continus.
- [[Processus de Poisson]] — l'autre processus canonique : sauts discrets contre trajectoire continue.
- [[Théorème central limite]] — Donsker en est la version fonctionnelle, dont la limite est le brownien.
- Processus d'Ornstein–Uhlenbeck — brownien avec rappel vers la moyenne (stationnaire).

## Pour aller plus loin

- Lemme d'Itô, EDS, ponts browniens ; processus de Lévy (généralisation avec sauts).
- Outils : `numpy` (Euler–Maruyama), `sdeint` ; bibliothèques de modèles de diffusion en ML.
