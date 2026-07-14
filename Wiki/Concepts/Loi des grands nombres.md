---
galaxie: wiki
type: concept
nom: Loi des grands nombres
alias: [Law of large numbers, LGN, LLN]
categorie: concept/stats
domaines: [data-sci]
tags: [probability, convergence]
---

# Loi des grands nombres

## Aperçu

- La moyenne empirique d'observations indépendantes et de même loi converge vers l'espérance théorique quand le nombre d'observations grandit.
- Fondement de l'estimation par échantillon et des méthodes de [[MCMC|Monte-Carlo]] : « plus de données → estimation plus juste ».

## Concepts clés

### Faible vs forte
- LGN faible : $\bar{X}_n$ converge en probabilité vers $\mu$ (l'écart devient improbable).
- LGN forte : $\bar{X}_n$ converge presque sûrement vers $\mu$ (une seule trajectoire finit par s'y caler).
- En pratique la distinction est technique ; les deux disent « la moyenne se stabilise ».

### Condition d'existence
- Il suffit que l'espérance $\mu$ soit finie (la LGN forte de Kolmogorov ne demande même pas de variance finie).
- Contre-exemple : la loi de Cauchy n'a pas d'espérance → la moyenne ne converge pas, elle reste aussi dispersée que les données.

### Ce qu'elle ne dit pas
- Elle donne la limite, pas la *vitesse* : à quelle distance de $\mu$ on est à $n$ fixé relève du [[Théorème central limite]] et des [[Inégalités de concentration]].
- Pas de « loi des moyennes » : un déséquilibre passé n'est pas compensé, il est dilué.

## Les maths, simplement

- Faible : $\bar{X}_n \xrightarrow{p} \mu$ ; forte : $\bar{X}_n \xrightarrow{a.s.} \mu$, avec $\bar{X}_n = \frac{1}{n}\sum_i X_i$.
- Preuve élémentaire de la version faible via [[Inégalités de concentration|Chebyshev]] : $P(|\bar{X}_n - \mu| \ge \varepsilon) \le \dfrac{\sigma^2}{n\varepsilon^2} \to 0$.
- L'erreur typique décroît en $1/\sqrt{n}$ — quadrupler les données ne fait que diviser l'erreur par deux.

## En pratique

- Justifie d'estimer une espérance par une moyenne d'échantillon (intégration Monte-Carlo, simulation, [[Bootstrap]]).
- Piège : observations corrélées → la convergence ralentit (taille d'échantillon effective réduite).
- Piège : espérance infinie ou queues très lourdes → la moyenne reste instable, préférer la médiane.

## Approches voisines & alternatives

- [[Théorème central limite]] — au-delà de la convergence, décrit la loi (gaussienne) de la fluctuation résiduelle.
- [[Inégalités de concentration]] — version quantitative et non asymptotique : borne l'écart à $n$ fini.
- [[MCMC]] — l'estimation Monte-Carlo (moyenne d'échantillons) repose directement sur la LGN.
- [[Bootstrap]] — rééchantillonne pour approcher la loi d'échantillonnage, en s'appuyant sur la même logique de moyenne.

## Pour aller plus loin

- LGN forte de Kolmogorov ; ergodicité (extension aux suites dépendantes mais stationnaires).
- Outils : `numpy` / `scipy` pour visualiser la stabilisation d'une moyenne par simulation.
