---
galaxie: wiki
type: concept
nom: Optimal transport
alias: [Transport optimal, OT, Plan de transport, Monge-Kantorovich, Sinkhorn, Earth mover's distance problem]
categorie: concept/math
domaines: [data-sci, ml-eng]
tags: [optimization, optimal-transport]
---

# Optimal transport

## Aperçu

- Cherche le **plan de transport** le moins coûteux pour déplacer une distribution de masse vers une autre — un problème d'optimisation linéaire sur des couplages de probabilités.
- Fournit une géométrie sur l'espace des distributions : sa valeur optimale est la [[Wasserstein distance]], métrique qui tient compte de la distance entre les points (contrairement aux divergences point par point).

## Concepts clés

### Monge vs Kantorovich
- **Monge** (1781) : trouver une application $T$ qui envoie chaque point source sur une cible en minimisant $\int c(x, T(x))$ — formulation rigide (pas toujours de solution).
- **Kantorovich** (1942) : relaxe en cherchant un **plan** $\gamma$ (couplage joint) plutôt qu'une application → problème **linéaire**, toujours soluble, base de la théorie moderne.

### Plan de transport
- $\gamma \in \Pi(p,q)$ : loi jointe de marges $p$ et $q$ ; $\gamma(x,y)$ = masse déplacée de $x$ vers $y$. Minimiser $\int c(x,y)\,d\gamma$ sur tous les plans admissibles.
- En discret, c'est un **problème de transport**, cas particulier de [[Programmation linéaire en nombres entiers (MIP)|programmation linéaire]], résoluble par le simplexe réseau.

### Régularisation entropique (Sinkhorn)
- Ajouter $-\varepsilon H(\gamma)$ rend le problème **fortement convexe** et résoluble par l'algorithme de **Sinkhorn** (mises à l'échelle alternées de lignes/colonnes) — rapide et différentiable, d'où son usage en deep learning.

## Les maths, simplement

- $\mathrm{OT}(p,q) = \inf_{\gamma \in \Pi(p,q)} \int c(x,y)\, d\gamma(x,y)$ — coût minimal du déplacement, sous les contraintes de marges $\sum_y \gamma = p$ et $\sum_x \gamma = q$.
- Programme linéaire en $\gamma$ (objectif et contraintes linéaires) ; sa **dualité** de Kantorovich donne la forme duale de $W_1$ sur les fonctions 1-lipschitziennes.
- Coût $c(x,y) = \lVert x-y \rVert^p$ → la valeur optimale vaut $W_p^p$ (cf. [[Wasserstein distance]]).

## En pratique

- Comparer des distributions (histogrammes, nuages de points, embeddings) en respectant la géométrie : alignement de domaines, color transfer, comparaison de formes.
- WGAN : entraîner un générateur contre une distance $W_1$ ; FID : $W_2$ entre gaussiennes d'activations.
- Coût élevé en grande dimension → **Sinkhorn**, sliced-Wasserstein. Outils : POT (Python Optimal Transport), `geomloss`, `scipy.stats.wasserstein_distance` (cas 1D).

## Approches voisines & alternatives

- [[Wasserstein distance]] — la valeur optimale du transport, vue comme métrique entre distributions.
- [[KL divergence]] — compare point par point, diverge sans support commun ; le transport reste informatif.
- [[Convexity]] — le problème de Kantorovich est un programme linéaire (convexe) ; Sinkhorn le rend fortement convexe.
- [[Programmation linéaire en nombres entiers (MIP)|Programmation linéaire]] — le transport discret en est un cas particulier.

## Pour aller plus loin

- Peyré & Cuturi (2019) — *Computational Optimal Transport*.
- Villani — *Optimal Transport: Old and New*.
