---
galaxie: wiki
type: concept
nom: Processus de Poisson
alias: [Poisson process, processus ponctuel de Poisson]
categorie: concept/stats
domaines: [data-sci]
tags: [stochastic-process, probability]
---

# Processus de Poisson

## Aperçu

- Modèle de comptage d'événements qui surviennent **indépendamment**, à **taux constant** $\lambda$, sans coordination entre eux.
- Le nombre d'événements sur un intervalle suit une loi de Poisson ; le temps entre deux événements une loi exponentielle (sans mémoire).

## Concepts clés

### Taux et incréments
- Un seul paramètre, l'intensité $\lambda$ (événements par unité de temps).
- Incréments **indépendants** (intervalles disjoints sans influence) et **stationnaires** (seule la durée compte, pas la position).

### Loi du comptage
- Le nombre d'événements sur une durée $t$ suit une loi de Poisson de moyenne $\lambda t$.
- Propriété marquante : moyenne = variance = $\lambda t$.

### Inter-arrivées exponentielles
- Les temps entre événements consécutifs sont i.i.d. exponentiels de taux $\lambda$.
- Absence de mémoire : le temps déjà écoulé n'informe pas sur l'attente restante → fait le lien avec les [[Chaînes de Markov]] en temps continu.

### Variantes
- Non homogène : $\lambda(t)$ varie dans le temps (pics de trafic).
- Spatial / marqué : événements dans le plan, ou porteurs d'attributs.

## Les maths, simplement

- Comptage : $N(t) \sim \text{Poisson}(\lambda t)$, soit $P(N(t)=k) = e^{-\lambda t}\dfrac{(\lambda t)^k}{k!}$.
- Espérance et variance : $\mathbb{E}[N(t)] = \text{Var}(N(t)) = \lambda t$.
- Inter-arrivées : $T_i \sim \text{Exp}(\lambda)$, d'espérance $1/\lambda$.

## En pratique

- Files d'attente, trafic réseau / requêtes web, arrivées clients, sinistres, désintégrations — toute la modélisation de comptage (régression de Poisson).
- Piège : **surdispersion**. Si la variance observée dépasse la moyenne, l'hypothèse Poisson (Var = moyenne) est violée → passer à la binomiale négative.
- Piège : événements groupés ou corrélés (rafales) → l'indépendance tombe, envisager un processus de Hawkes.

## Approches voisines & alternatives

- [[Chaînes de Markov]] — le processus de Poisson est un processus de Markov à temps continu, à sauts.
- [[Mouvement brownien]] — l'autre processus canonique : trajectoire continue contre sauts discrets.
- Processus de Hawkes — auto-excitation, pour les événements qui en déclenchent d'autres (contagion).

## Pour aller plus loin

- Lien Poisson ↔ exponentielle ↔ gamma ; superposition et amincissement (thinning) de processus.
- Outils : `numpy.random` (simulation), `statsmodels` (régression de Poisson, binomiale négative).
