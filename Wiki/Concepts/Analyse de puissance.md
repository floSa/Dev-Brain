---
galaxie: wiki
type: concept
nom: Analyse de puissance
alias: [power analysis, statistical power, taille d'échantillon]
categorie: concept/stats
domaines: [data-sci]
tags: [statistical-power, hypothesis-testing, effect-size]
---

# Analyse de puissance

## Aperçu

- Relie quatre quantités d'un test : taille d'effet, taille d'échantillon, seuil α et puissance.
- Sert surtout à calculer le $n$ minimal pour détecter un effet donné avec une probabilité voulue — **avant** de collecter.

## Concepts clés

### Puissance
- Puissance = 1 − β = proba de détecter un effet réel. Cible usuelle : 0,80.

### Les quatre leviers
- Fixer trois → le quatrième se déduit. Typiquement : effet, α, puissance → $n$.

### Taille d'effet
- L'ampleur attendue (Cohen's d, η², w…). Plus l'effet est petit, plus $n$ doit être grand.

### A priori vs post-hoc
- A priori (avant l'étude) = utile. « Puissance observée » a posteriori = peu informative, à éviter.

### Sous- / sur-dimensionnement
- Sous-dimensionné → on rate les vrais effets, et les significatifs sont surévalués.
- Sur-dimensionné → coût inutile, détection d'effets triviaux.

## Les maths, simplement

- Quatre liés : taille d'effet, $n$, $\alpha$, puissance $1-\beta$ — trois fixés ⇒ le 4e déterminé.
- Ordre de grandeur (deux moyennes, effet $d$, puissance 0,8, $\alpha$ 0,05 bilatéral) : $n \approx \dfrac{16}{d^2}$ par groupe.
- $n \propto 1/d^2$ : un effet deux fois plus petit demande ~4× plus de sujets.
- Corriger la multiplicité abaisse l'α effectif → puissance moindre à $n$ fixe.

## En pratique

- Estimer la taille d'effet via la littérature, une étude pilote, ou le plus petit effet jugé important (MCID).
- Faire l'analyse **avant** la collecte ; documenter les hypothèses.
- Intégrer les corrections de tests multiples prévues (cf. [[Correction des tests multiples]]).
- Pas de taille d'effet crédible → simuler (y compris par [[Bootstrap]]) plutôt que deviner.

## Approches voisines & alternatives

- [[Tests d'hypothèse]] — la puissance est l'envers du risque β.
- [[Test t et ANOVA]], [[Test du khi-deux]] — chaque test a sa formule de dimensionnement.
- [[Correction des tests multiples]] — son coût en puissance se planifie ici.
- [[A-B testing|A/B testing]] — c'est ici que se fixent son MDE et sa durée.
- [[Bootstrap]] — simulation quand aucune formule fermée ne s'applique.

## Pour aller plus loin

- Outils : `statsmodels.stats.power`, `pingouin` (`power_*`), G*Power.
