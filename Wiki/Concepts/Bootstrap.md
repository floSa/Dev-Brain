---
galaxie: wiki
type: concept
nom: Bootstrap
alias: [resampling, rééchantillonnage]
categorie: concept/stats
domaines: [data-sci]
tags: [resampling, confidence-interval, non-parametric]
---

# Bootstrap

## Aperçu

- Estime la distribution d'échantillonnage d'une statistique en rééchantillonnant l'échantillon lui-même, avec remise.
- Donne IC et erreurs standard sans formule analytique ni hypothèse de normalité.

## Concepts clés

### Rééchantillonnage avec remise
- Tirer $n$ observations avec remise dans l'échantillon de taille $n$, $B$ fois.
- Recalculer la statistique sur chaque rééchantillon → distribution empirique.

### IC bootstrap
- Percentile : prendre les quantiles 2,5 % et 97,5 % de la distribution bootstrap.
- BCa : corrige biais et asymétrie, plus fiable.

### Quand ça brille
- Statistiques sans formule simple (médiane, ratio, corrélation, métriques ML).
- Petits échantillons, distributions non normales.

### Limites
- Ne crée pas d'information : un échantillon biaisé reste biaisé.
- Mal adapté aux extrêmes (max, min) et aux très petits $n$.

## Les maths, simplement

- Idée : remplacer la vraie loi $F$ (inconnue) par la loi empirique $\hat{F}$ de l'échantillon, puis simuler.
- Pour $b = 1\dots B$ : tirer $X^{*b}$ avec remise, calculer $\hat{\theta}^{*b}$.
- Erreur standard bootstrap : $\widehat{SE} = \sqrt{\dfrac{1}{B-1}\sum_b (\hat{\theta}^{*b}-\bar{\theta}^{*})^2}$.
- IC percentile 95 % : $[\hat{\theta}^{*}_{(2{,}5\%)},\ \hat{\theta}^{*}_{(97{,}5\%)}]$. Prendre $B \ge 2000$ pour des IC stables.

## En pratique

- Défaut $B \approx 2000$ à $10000$ ; davantage pour des quantiles fins.
- Données dépendantes (séries temporelles) → block bootstrap, pas le tirage i.i.d.
- Test par permutation = cousin pour comparer deux groupes sans hypothèse de loi.
- Reproductibilité : fixer la graine aléatoire.

## Approches voisines & alternatives

- [[Intervalles de confiance]] — le bootstrap en produit sans formule normale.
- [[Tests non paramétriques]] — même esprit distribution-free ; permutation pour tester.
- [[Tests d'hypothèse]] — bootstrap / permutation comme moteur d'inférence.
- [[Analyse de puissance]] — simulation par rééchantillonnage quand aucune formule fermée n'existe.
- [[Théorème central limite]] — l'approche analytique que le bootstrap remplace quand la normalité ne tient pas.
- [[Loi des grands nombres]] — fonde la convergence du bootstrap quand $B$ grandit.
- [[Validation croisée]] — l'autre grande technique de rééchantillonnage : partitionne sans remise pour estimer la généralisation d'un modèle.
- Méthode delta / jackknife — alternatives analytiques ou antérieures au bootstrap.

## Pour aller plus loin

- Outils : `scipy.stats.bootstrap`, `numpy` (rééchantillonnage manuel), `scikit-learn` (`resample`).
