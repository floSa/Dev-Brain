---
galaxie: wiki
type: concept
nom: Inégalités de concentration
alias: [Concentration inequalities, Hoeffding, Chebyshev, inégalité de Markov]
categorie: concept/stats
domaines: [data-sci]
tags: [probability, concentration]
---

# Inégalités de concentration

## Aperçu

- Bornent la probabilité qu'une variable aléatoire — souvent une moyenne — s'écarte de son espérance, **sans attendre** que $n \to \infty$.
- Version non asymptotique et quantitative de la [[Loi des grands nombres]] : elles disent *à quel point* la moyenne est déjà concentrée à $n$ fini.

## Concepts clés

### Inégalité de Markov
- Pour une variable **positive** : la masse au-delà d'un seuil est bornée par la moyenne sur le seuil.
- Borne la plus brute (n'utilise que l'espérance), point de départ des autres.

### Inégalité de Chebyshev
- Utilise la variance : la probabilité de s'écarter de plus de $k$ écarts-types est au plus $1/k^2$.
- Universelle (aucune hypothèse de loi) donc lâche ; sert à prouver la [[Loi des grands nombres]] faible.

### Inégalité de Hoeffding
- Pour une somme de variables **bornées** indépendantes : borne **exponentielle**, bien plus serrée que Chebyshev.
- Cœur des garanties d'apprentissage et des bornes UCB des [[Multi-armed bandits]].

### Chernoff / Bernstein
- Bornes exponentielles affinées exploitant la variance ou la fonction génératrice des moments.
- Bernstein gagne quand la variance est petite devant l'amplitude.

## Les maths, simplement

- Markov : $P(X \ge a) \le \dfrac{\mathbb{E}[X]}{a}$ pour $X \ge 0$, $a > 0$.
- Chebyshev : $P(|X - \mu| \ge k\sigma) \le \dfrac{1}{k^2}$.
- Hoeffding (moyenne de $X_i \in [a,b]$ i.i.d.) : $P(|\bar{X}_n - \mu| \ge t) \le 2\exp\!\left(-\dfrac{2nt^2}{(b-a)^2}\right)$ — décroissance exponentielle en $n$.

## En pratique

- Garantit une taille d'échantillon : inverser Hoeffding donne le $n$ pour un écart $t$ à confiance fixée.
- Bornes de généralisation en ML (risque empirique vs risque réel), regret des bandits (UCB), tests de qualité de données.
- Tension : plus la borne est serrée (Hoeffding, Bernstein), plus les hypothèses sont fortes (bornes, indépendance).
- À distinguer : l'**inégalité de Markov** (le mathématicien) n'a aucun lien avec les [[Chaînes de Markov]].

## Approches voisines & alternatives

- [[Loi des grands nombres]] — convergence asymptotique sans vitesse ; les concentrations en donnent la version chiffrée.
- [[Théorème central limite]] — asymptotique mais avec loi limite (gaussienne) ; complémentaire des bornes à $n$ fini.
- [[Multi-armed bandits]] — Hoeffding/Chernoff fondent les intervalles de confiance des bras (UCB).
- [[Analyse de puissance]] — autre façon de relier taille d'échantillon et garantie statistique.

## Pour aller plus loin

- McDiarmid (différences bornées), Azuma (martingales), Bernstein ; inégalité de Markov ⇒ Chebyshev ⇒ Chernoff par raffinements successifs.
- Réf : Boucheron, Lugosi, Massart — *Concentration Inequalities*.
