---
galaxie: wiki
type: concept
nom: Jensen-Shannon divergence
alias: [Divergence de Jensen-Shannon, Jensen-Shannon, JSD, JS divergence, divergence JS]
categorie: concept/math
domaines: [data-sci, ml-eng]
tags: [information-theory, kl-divergence]
---

# Jensen-Shannon divergence

## Aperçu

- Version **symétrisée et bornée** de la [[KL divergence|divergence KL]] : moyenne des KL de chaque distribution vers leur mélange. Corrige les deux défauts de la KL — l'asymétrie et l'explosion à $+\infty$.
- Sa racine carrée est une **vraie métrique** (distance de Jensen-Shannon), ce qui la rend utilisable pour comparer ou clusteriser des distributions.

## Concepts clés

### Symétrie et bornes
- $JSD(p,q) = JSD(q,p)$, toujours **finie** et bornée : $0 \le JSD \le \log 2$ (en bits, $\le 1$). Nulle ssi $p = q$, maximale quand les supports sont disjoints.
- Robuste au support : contrairement à la KL, reste définie même si $p$ et $q$ ne se recouvrent pas — la moyenne $m$ couvre les deux.

### Construction par la moyenne
- On forme le mélange $m = \tfrac12(p+q)$, puis on moyenne $D_{KL}(p\,\|\,m)$ et $D_{KL}(q\,\|\,m)$. Chaque KL est finie car $m$ domine $p$ et $q$.

### Interprétation information mutuelle
- $JSD$ égale l'[[Mutual information|information mutuelle]] entre la variable mélangée et l'indicateur de provenance (de $p$ ou de $q$) : « combien observer un échantillon renseigne sur sa source ».

## Les maths, simplement

- $JSD(p\,\|\,q) = \tfrac12 D_{KL}(p\,\|\,m) + \tfrac12 D_{KL}(q\,\|\,m)$, avec $m = \tfrac12(p+q)$.
- Distance métrique : $\sqrt{JSD}$ satisfait l'inégalité triangulaire (contrairement à la KL et à la JSD elle-même).
- Généralisation pondérée à $n$ distributions possible (poids $\pi_i$, mélange $\sum_i \pi_i p_i$).

## En pratique

- **GAN originels** : le discriminateur optimal rend la perte du générateur équivalente à $2\,JSD - \log 4$. Quand les supports ne se recouvrent pas, la JSD sature à $\log 2$ → gradient nul, d'où le passage à la [[Wasserstein distance]] (WGAN).
- **Comparaison de distributions** : similarité de documents (distributions de mots), de clusters, de signatures — la métrique $\sqrt{JSD}$ se branche dans un k-NN ou un clustering.
- Détection de dérive symétrique, là où l'on ne veut pas privilégier un sens (vs la KL dirigée).
- Outils : `scipy.spatial.distance.jensenshannon` ([[Dev/Services/scipy.stats|SciPy]]) renvoie directement $\sqrt{JSD}$.

## Approches voisines & alternatives

- [[KL divergence]] — la brique asymétrique dont la JSD est la symétrisation bornée.
- [[Wasserstein distance]] — préférée quand la JSD sature (supports disjoints) : elle garde un gradient exploitable.
- [[Mutual information]] — la JSD s'interprète comme l'information mutuelle source ↔ échantillon.
- [[Shannon entropy]] — la JSD s'écrit aussi comme l'entropie du mélange moins la moyenne des entropies.

## Pour aller plus loin

- Lin (1991) — *Divergence Measures Based on the Shannon Entropy*.
- Goodfellow et al. (2014) — *Generative Adversarial Nets* (la JSD comme objectif implicite).
