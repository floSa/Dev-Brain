---
galaxie: wiki
type: concept
nom: Théorème central limite
alias: [Central limit theorem, CLT, TCL]
categorie: concept/stats
domaines: [data-sci]
tags: [probability, convergence]
---

# Théorème central limite

## Aperçu

- La somme (ou la moyenne) de variables aléatoires indépendantes et de même loi, recentrée et normalisée, tend vers une loi **normale** — quelle que soit la loi de départ, dès lors que sa variance est finie.
- C'est la raison de l'omniprésence de la gaussienne : il justifie les [[Intervalles de confiance]] et les [[Tests d'hypothèse]] paramétriques pour de grands échantillons.

## Concepts clés

### Énoncé standard
- Pour $X_1,\dots,X_n$ i.i.d. d'espérance $\mu$ et de variance $\sigma^2$ finie, la moyenne $\bar{X}_n$ se comporte comme une normale quand $n$ grandit.
- La [[Loi des grands nombres]] dit *où* $\bar{X}_n$ converge ($\mu$) ; le TCL dit *comment elle fluctue* autour ($\sigma/\sqrt{n}$).

### Universalité
- La loi des $X_i$ n'a pas d'importance (binaire, exponentielle, asymétrique…) : la limite est toujours gaussienne.
- C'est pourquoi tant de mesures agrégées (erreurs, moyennes) sont approximativement normales.

### Vitesse de convergence
- Borne de Berry–Esseen : l'écart à la normale décroît en $1/\sqrt{n}$, dégradé par une forte asymétrie ou des queues lourdes.
- Heuristique $n \ge 30$ : raisonnable pour des lois proches du symétrique, optimiste pour des lois très asymétriques.

### Quand il échoue
- Variance infinie (loi de Cauchy, queues en loi de puissance) → la limite est une loi $\alpha$-stable, pas une normale.
- Forte dépendance entre observations → versions adaptées (Lindeberg, Lyapunov) ou échec.

## Les maths, simplement

- Forme normalisée : $\dfrac{\bar{X}_n - \mu}{\sigma/\sqrt{n}} \xrightarrow{d} \mathcal{N}(0,1)$ ($\xrightarrow{d}$ = convergence en loi).
- De façon équivalente sur la somme : $\dfrac{\sum_i X_i - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} \mathcal{N}(0,1)$.
- L'erreur-type d'une moyenne, $\sigma/\sqrt{n}$, sort directement de là — d'où la largeur des IC.

## En pratique

- Justifie les IC et tests « normaux » dès que $n$ est grand, même sans connaître la loi sous-jacente.
- Pièges : queues lourdes, variance infinie, observations corrélées → la normalité approchée tombe.
- Quand le TCL est douteux (petit $n$, statistique non standard), passer au [[Bootstrap]], qui ne suppose pas la normalité.

## Approches voisines & alternatives

- [[Loi des grands nombres]] — la moyenne converge vers $\mu$ ; le TCL en décrit la fluctuation résiduelle.
- [[Inégalités de concentration]] — bornes non asymptotiques (valables à $n$ fini), là où le TCL n'est qu'asymptotique.
- [[Intervalles de confiance]] — le TCL fournit la forme normale qui les calibre.
- [[Tests d'hypothèse]] — t-test, z-test, ANOVA reposent sur la normalité asymptotique de la moyenne.
- [[Bootstrap]] — alternative par simulation quand l'approximation gaussienne ne tient pas.

## Pour aller plus loin

- Berry–Esseen (vitesse), théorème de Donsker (version fonctionnelle → [[Mouvement brownien]]), lois $\alpha$-stables (variance infinie).
- Outils : `scipy.stats` (lois et tests de normalité), `numpy` pour visualiser la convergence par simulation.
