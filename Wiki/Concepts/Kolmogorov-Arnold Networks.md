---
galaxie: wiki
type: concept
nom: Kolmogorov-Arnold Networks
alias: [KAN, KANs, réseaux de Kolmogorov-Arnold, kolmogorov-arnold network]
categorie: concept/dl
domaines: [ml-eng]
tags: [deep-learning]
---

# Kolmogorov-Arnold Networks

## Aperçu

- Architecture de réseau de neurones proposée en 2024 comme **alternative au perceptron multicouche (MLP)** : au lieu de poids linéaires fixes + activations fixes sur les nœuds, un **KAN** place des **fonctions d'activation apprenables sur les arêtes** et somme sur les nœuds.
- Motivée par le **théorème de représentation de Kolmogorov-Arnold** : toute fonction continue multivariée s'écrit comme une composition de sommes de fonctions **univariées**. Le KAN paramètre ces fonctions univariées et les apprend.

## Concepts clés

### Le renversement vs MLP
- **MLP** : nœuds = activations fixes (ReLU…), arêtes = poids scalaires appris. La non-linéarité est figée, c'est l'échelle qui s'apprend.
- **KAN** : arêtes = fonctions univariées apprises, nœuds = simple somme. Il n'y a **plus de matrice de poids linéaire** : chaque « poids » est une petite fonction.

### Splines apprenables
- Chaque fonction d'arête est typiquement une **B-spline** : définie par un degré $k$ et un nombre d'intervalles $G$ (la grille), dont on apprend les coefficients. On peut **raffiner la grille** (grid extension) pour gagner en précision sans repartir de zéro.
- Forme usuelle résiduelle : $\phi(x) = w_b\, b(x) + w_s\, \text{spline}(x)$, avec $b$ une base type SiLU et $w_b, w_s$ appris.

### Interprétabilité & sparsification
- Les fonctions d'arête sont **visualisables** : on voit ce que chaque connexion calcule. Avec élagage et régularisation, un KAN peut se réduire à une formule **symbolique** lisible — d'où l'intérêt pour le ML scientifique (régression de fonctions, EDP).

## Les maths, simplement

- Théorème de Kolmogorov-Arnold : $f(x_1,\dots,x_n) = \sum_{q=0}^{2n} \Phi_q\!\Big(\sum_{p=1}^{n} \phi_{q,p}(x_p)\Big)$ — toute fonction continue se ramène à des sommes de fonctions **d'une seule variable** ($\phi_{q,p}$ puis $\Phi_q$).
- Un KAN **généralise** cette forme à des largeurs et profondeurs arbitraires : une couche applique une fonction univariée apprise sur chaque arête, puis somme — la non-linéarité vit sur les connexions, pas sur les neurones.
- Promesse : à précision égale, **moins de paramètres** que le MLP sur des cibles structurées, au prix d'un coût par paramètre plus élevé (évaluer des splines).

## En pratique

- Implémentation de référence [[Dev/Services/pykan|pykan]] (sur [[Dev/Services/PyTorch|PyTorch]]) ; variantes plus rapides (efficient-kan, FastKAN) qui remplacent les B-splines par des bases moins coûteuses.
- Points forts observés : **régression de fonctions**, problèmes de physique / EDP, tâches où l'interprétabilité prime.
- Limites : **entraînement plus lent** que le MLP, écosystème immature, gains peu nets sur les grosses tâches de perception (vision, langage) où MLP et transformeur restent devant. Architecture **récente** et mouvante — à manier comme une piste de recherche, pas comme un défaut de production.

## Approches voisines & alternatives

- [[MOC/Concepts/Deep learning|Deep learning]] — la famille d'architectures dont le KAN est une variante ; le MLP qu'il vise à concurrencer en est la brique de base.
- [[Self-attention]] — autre brique structurante du deep learning moderne, orthogonale au KAN (des KAN-Transformers combinent les deux).

## Pour aller plus loin

- Liu et al. (2024) — *KAN: Kolmogorov-Arnold Networks*, arXiv:2404.19756 (et la suite *KAN 2.0*).
- Implémentation officielle : pykan — https://github.com/KindXiaoming/pykan
- Revue *KAT to KANs* (2024) pour le panorama des variantes.
