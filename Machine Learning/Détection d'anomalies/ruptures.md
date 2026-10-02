---
role: brique
nom: ruptures
alias: [deepcharles/ruptures, change point detection python, rpt]
pitch: "Bibliothèque Python de détection de ruptures hors ligne — segmente un signal en régimes avec des algorithmes de recherche (PELT, Binseg, BottomUp, Window, Dynp, KernelCPD) combinables à des fonctions de coût (L2, RBF, normale, rang…) ; elle rend des points de changement, pas des scores d'anomalie."
categorie: ml/anomalie
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Kats]]"]
complements: []
tags: [timeseries, change-point]
url_docs: https://centre-borelli.github.io/ruptures-docs/
url_repo: https://github.com/deepcharles/ruptures
---

# ruptures

<!-- AUTO:BANDEAU:START -->
> Bibliothèque Python de détection de ruptures hors ligne — segmente un signal en régimes avec des algorithmes de recherche (PELT, Binseg, BottomUp, Window, Dynp, KernelCPD) combinables à des fonctions de coût (L2, RBF, normale, rang…) ; elle rend des points de changement, pas des scores d'anomalie.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Découpe un signal (univarié ou multivarié) en segments dont les propriétés statistiques sont
homogènes, et rend les indices où elles changent. La bibliothèque sépare trois choses : une
**fonction de coût** (ce qu'est un segment « homogène » : moyenne constante, variance
constante, forme dans un espace à noyau…), une **méthode de recherche** (comment placer les
ruptures pour minimiser le coût total) et une **contrainte** (nombre de ruptures connu, ou
pénalité). Cette modularité reprend la revue de Truong, Oudre et Vayatis (*Signal Processing*,
2020), que le README demande de citer. Le travail est **hors ligne** : le signal entier doit
être disponible. Auteurs déclarés : Charles Truong, Laurent Oudre et Nicolas Vayatis ;
le copyright du fichier LICENSE est à l'ENS Paris-Saclay et au CNRS.

Ce n'est pas un détecteur d'anomalies au sens d'un score par point. Il répond à « quand le
régime a-t-il changé ? », pas à « ce point est-il aberrant ? » — la distinction est posée dans
la notion [[Détection de ruptures]].

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Segmenter un signal en régimes (état d'une machine, phases d'un procédé, plateaux) après coup | Surveiller un flux en continu : tout est hors ligne, aucune mise à jour incrémentale → [[Détection d'anomalies en ligne]] |
| Comparer plusieurs algorithmes de recherche et plusieurs coûts derrière une interface unique | Repérer des points ou des motifs isolés qui s'écartent du normal : pas de score par point → [[Détection d'outliers univariée]], [[STUMPY]] |
| Nombre de ruptures connu (`Dynp`, `n_bkps`) ou pénalité calibrable (`Pelt`, `pen`) | Aucune idée du nombre de régimes ni de la pénalité : la pénalité n'est pas choisie par l'outil, et c'est elle qui décide du résultat |
| Signaux multivariés : les coûts L2, RBF et normale acceptent plusieurs canaux | Série très longue : `Pelt` annonce une complexité moyenne en O(CKn) **sous conditions favorables** seulement (doc officielle), `Dynp` est une recherche exacte par programmation dynamique ; mesurer sur la longueur réelle, `KernelCPD` est l'implémentation C du coût à noyau |
| Brique de pré-traitement : découper une série avant de modéliser chaque régime | Détecter une dérive de modèle déployé : la tâche est autre → [[Data drift]] |

## Mise en œuvre

- Installation — `uv add ruptures` ; l'extra `display` ajoute matplotlib pour `rpt.display`
- Point d'entrée — API Python : `algo = rpt.Pelt(model="rbf").fit(signal)` puis `algo.predict(pen=10)` ; les autres classes de recherche sont `Binseg`, `BottomUp`, `Window`, `Dynp` et `KernelCPD`
- Prérequis — NumPy et SciPy seulement ; la version 1.1.10 sur PyPI demande Python `>=3.9,<3.14`
- Exécution — CPU mono-machine, en bibliothèque ; critères d'arrêt : `Pelt` veut une pénalité `pen`, `Dynp` un nombre `n_bkps`, `Binseg`, `BottomUp` et `Window` acceptent `n_bkps`, `pen` ou `epsilon`, `KernelCPD` `n_bkps` ou `pen`
- Coût — gratuit, BSD-2-Clause ; aucune infrastructure

Fonctions de coût présentes dans la version 1.1.10 : `CostL1`, `CostL2`, `CostNormal`,
`CostRbf`, `CostLinear`, `CostCLinear`, `CostRank`, `CostAR`, `CostCosine` et `CostMl`.
Une méthode `L1Potts` figure sur la branche principale mais pas dans la 1.1.10.

## Écosystème

### Alternatives

- [[Kats]] — Boîte à outils Python de Meta pour l'analyse de séries temporelles — détection (CUSUM, BOCPD, statistiques robustes, outliers), prévision, extraction de features — mais dernière version publiée en 2022 et paquet PyPI aux dépendances épinglées, classé alpha.

## Ressources

- Documentation — https://centre-borelli.github.io/ruptures-docs/
- Dépôt — https://github.com/deepcharles/ruptures
- Papier — Article de référence : Truong, Oudre, Vayatis, *Selective review of offline change point detection methods*, Signal Processing 167:107299, 2020 : https://doi.org/10.1016/j.sigpro.2019.107299

## Voir aussi

- [[Détection de ruptures]] — la notion qu'il outille : ce qu'est une rupture, et en quoi elle diffère d'une anomalie
- [[Détection d'anomalies]] — le hub du dossier
- [[Comparatif - Détection d'anomalies en séries temporelles]] — ce qui le départage des détecteurs de séries
- [[Time series anomaly detection]] — la notion générale ; la rupture y est un type d'événement parmi d'autres
- [[Stationarity]] — une rupture de moyenne ou de variance est une non-stationnarité par morceaux
- [[aeon]] — son module de segmentation s'appuie sur ruptures pour `BinSeg`
- [[Évaluer une détection d'anomalies]] — métriques par événement, utiles aussi pour juger des ruptures posées
