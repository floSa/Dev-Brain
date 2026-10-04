---
role: notion
nom: Classification ABC-XYZ
alias: [Classification ABC/XYZ, ABC analysis, analyse ABC, classification ABC, analyse XYZ, matrice ABC-XYZ, Pareto 80/20 (stock), loi de Pareto (stocks)]
categorie: math/recherche-operationnelle
domaines: [data-sci]
tags: [inventory, forecasting]
---

# Classification ABC/XYZ

## Aperçu

- **Segmenter** un catalogue de références (SKU) en quelques classes pour ne pas gérer des milliers de références de la même façon. L'analyse **ABC** classe par **valeur** écoulée (quoi surveiller de près), l'analyse **XYZ** par **régularité** de la demande (quoi est facile ou difficile à servir). Le croisement donne une grille à neuf cases (AX … CZ).
- C'est une **heuristique de priorisation**, pas un modèle : les classes ne calculent ni quantité ni stock de sécurité, elles disent où mettre l'effort et quelle cible de service viser.
- Les **seuils** (80 % de la valeur pour A, CV < 0,5 pour X…) sont des **conventions** d'entreprise. Aucune théorie ne les fixe, et les sources citées plus bas ne s'accordent pas entre elles.
- Distinct de la classification de Syntetos-Boylan ([[Intermittent demand]]) : celle-ci choisit une **méthode de prévision**, la grille ABC-XYZ une **politique de gestion**.

## Concepts clés

### Analyse ABC : cumul de Pareto

1. Pour chaque référence $i$, calculer la **valeur annuelle d'écoulement** $v_i = p_i\,Q_i$ ($p_i$ coût ou prix unitaire, $Q_i$ quantité écoulée sur l'année).
2. Trier par $v_i$ décroissant et calculer la **part cumulée** $F_k = \sum_{j\le k} v_{(j)} \big/ \sum_i v_i$.
3. Couper la courbe en tranches : A en tête, C en queue.

- **Origine** : H. Ford Dickie, de General Electric, « ABC Inventory Analysis Shoots for Dollars, Not Pennies », *Factory Management and Maintenance*, 109(7), p. 92-94, 1951. Référence relevée dans la bibliographie d'une revue de littérature ; l'article lui-même n'a pas été lu. Les sources secondaires le rattachent à la règle des 80/20 de Pareto.
- **Seuils usuels, tous conventionnels** :
  - 80 % / 95 % de la valeur cumulée (A / B / C = 0-80, 80-95, 95-100 %) : retenus « en concertation avec des experts » sur 15 000 références d'un constructeur de machines (Scholz-Reiter et al., 2012). Même découpage « 80-15-5 » dans un glossaire d'éditeur (Tacto).
  - 80 / 15 / 5 % de la valeur pour 20 / 30 / 50 % des références : présenté comme **idéal-typique**, rarement atteint dans la réalité, chaque entreprise fixant ses pourcentages (Wikipédia allemand, « ABC-Analyse »).
  - 70 / 25 / 5 % de la valeur pour 20 / 30 / 50 % des références, ou 66,6 / 23,3 / 10,1 % pour 10 / 20 / 70 % : donnés comme **exemples**, « no fixed standards » (Wikipedia, « ABC analysis »).
- Rien ne justifie ces chiffres en théorie : ils décrivent une forme typique de la courbe de Lorenz des ventes, pas un optimum. Dans la simulation ci-dessous, A regroupe 76 références sur 300 (25 %) pour 80 % de la valeur.
- **Critère de classement** : valeur ou **volume** sont les deux critères les plus courants (Teunter, Babai, Syntetos, 2010). Une référence chère et rare et une référence bon marché très tournante ne se classent pas pareil selon le critère.
- **Convention de coupe** : la référence qui franchit le seuil tombe en A (cumul *avant* la ligne ≤ 80 %) ou en B (cumul *inclus*) selon les outils. Choix à fixer une fois, par écrit.

### Analyse XYZ : variabilité de la demande

- Sur une fenêtre de $T$ périodes (12 mois agrégés par mois dans l'étude de Scholz-Reiter et al.), calculer le **coefficient de variation** de la demande par période :
  $$\mathrm{CV}_i = \frac{\sigma_i}{\mu_i},$$
  où $\mu_i$ est la demande moyenne par période et $\sigma_i$ son écart-type (empirique ; le diviseur $T$ ou $T-1$ est à fixer, les sources ne le précisent pas).
- Seuils, **conventionnels** et **en désaccord** selon les sources :
  - X : $\mathrm{CV} < 0{,}5$ ; Y : $0{,}5 \le \mathrm{CV} \le 1$ ; Z : $\mathrm{CV} > 1$ (Scholz-Reiter et al., 2012 ; Tacto ; valeurs par défaut d'un outil de calcul en ligne, MetricGate, qui conseille de les relever pour les pièces de rechange).
  - X : CV ≤ 10 % ; Y : de 10 à 25 % ; Z : > 25 % (Mecalux, qui les dit « most common », et Lokad à titre d'exemple, en précisant que les seuils sont arbitraires).
  - Les deux jeux diffèrent d'un facteur 4 à 5 : la même référence peut être Z dans un outil et X dans l'autre. Aucune des sources lues ne tranche.
- Lecture décrite par Scholz-Reiter et al. : X, consommation à peu près constante ; Y, fluctuations plus fortes, souvent tendance ou saisonnalité ; Z, consommation tout à fait irrégulière.
- Fenêtre courte : MetricGate recommande au moins 8 à 12 périodes, sinon classe Z par défaut (recommandation d'outil, non argumentée dans la source).

### La matrice à neuf cases

- ABC sert de classement primaire, XYZ le complète (Scholz-Reiter et al., citant la littérature allemande de logistique). Le croisement donne AX, AY, AZ, BX, … CZ.
- **Exemples de pratique relevés** (une seule source par exemple ; aucune des sources lues ne détaille les neuf cases) :
  - AX : suivi fournisseur renforcé et contrôle d'inventaire hebdomadaire ; CZ : pilotage par Kanban automatisé (Tacto).
  - Cible de service de plus de 98 % pour A, 90-95 % pour C (Tacto). Teunter et al. (2010) rapportent que la classe qui doit avoir le meilleur ou le plus mauvais service est **disputée** dans la littérature, et jugent peu économiques les cibles fixes par classe (voir Limites) : les deux lectures coexistent, sans arbitrage ici.
- **Lecture proposée** (raisonnement de cette page, pas une règle sourcée) :

| | X (stable) | Y (variable) | Z (irrégulier) |
|---|---|---|---|
| **A** (valeur forte) | stock cyclique serré, peu de sécurité, révision fréquente | sécurité calculée, révision fréquente | cas dur : la sécurité coûte cher ; réduire les délais, mutualiser, ou produire/commander sur ordre |
| **B** | politique standard | politique standard + sécurité | à examiner au cas par cas |
| **C** (valeur faible) | gros lots, révision rare, Kanban | sécurité généreuse, peu de suivi | stock minimal ou commande sur ordre, selon la criticité |

- Le raisonnement : la sécurité croît avec $\sigma$ (colonne Z) et son coût avec la valeur (ligne A). Voir [[Stock de sécurité et taux de service]].

### Lien avec Syntetos-Boylan (ADI / CV²)

- La classification de [[Intermittent demand]] (Syntetos, Boylan, Croston, 2005) utilise **ADI** (intervalle moyen entre demandes) et **CV²** des **tailles de demande non nulles**, avec les seuils 1,32 et 0,49 (valeurs relevées dans un article de prévision qui les reprend). Elle sert à choisir la **méthode** (lissage simple, Croston, SBA).
- XYZ utilise le CV de la demande **par période, zéros compris**. Il sert à choisir la **politique** (sécurité, service, mode de commande).
- Les deux coïncident mal : si chaque période porte une demande avec probabilité $p = 1/\mathrm{ADI}$, de taille indépendante de CV² $=\mathrm{CV}_z^2$, alors
  $$\mathrm{CV}^2_{\text{XYZ}} = \mathrm{ADI}\,(1 + \mathrm{CV}_z^2) - 1.$$
  Dérivation propre à cette page (Bernoulli × taille indépendante), vérifiée par simulation. Exemple : ADI = 4, CV$_z^2$ = 0,25 donne CV = 2, soit Z, alors que les tailles sont régulières.

## Les maths, simplement

- Pour $T$ périodes, le CV (écart-type de population) est borné par $\sqrt{T-1}$ : atteint quand toute la demande tombe sur une seule période. Sur 12 mois, un CV de 3,3 est un maximum, pas une « extrême variabilité ».
- Avec des zéros, le CV monte mécaniquement : pour une taille fixe $z$ avec probabilité $p$, $\mathrm{CV} = \sqrt{(1-p)/p}$ ; $p = 0{,}1$ donne 3.
- Pour des demandes **indépendantes**, le CV d'un agrégat de $n$ références comparables décroît en $1/\sqrt{n}$ : une famille est plus « X » que ses références.

## En pratique

### Calcul d'exemple

Données simulées (300 références, 12 mois de demande gamma-Poisson, prix log-normal), classes A/B/C à 80 / 95 % et X/Y/Z à 0,5 / 1, exécutées avec numpy et pandas :

```python
import numpy as np, pandas as pd
rng = np.random.default_rng(0); n = 300
mu, k = rng.lognormal(3, 1.2, n), rng.uniform(0.3, 8, n)          # demande moyenne, dispersion
d = pd.DataFrame(rng.poisson(rng.gamma(k[:, None], (mu / k)[:, None], (n, 12))))  # 12 mois
v = d.sum(axis=1) * rng.lognormal(2, 0.8, n)                       # valeur = quantité x prix
abc = pd.cut((v.sort_values(ascending=False).cumsum() - v) / v.sum(), [-1, .80, .95, 1], labels=list("ABC"))
xyz = pd.cut(d.std(axis=1, ddof=0) / d.mean(axis=1), [0, .5, 1, np.inf], labels=list("XYZ"), right=False)
print(pd.crosstab(abc, xyz))
```

Résultat : AX 40, AY 33, AZ 3 ; BX 44, BY 43, BZ 5 ; CX 39, CY 77, CZ 16. La répartition dépend de la simulation et des seuils, pas du métier : l'exercice montre le mécanisme, pas des proportions à attendre.

### Limites

- **Classement statique, donc instable.** Dans l'étude de Scholz-Reiter et al. (15 000 références, un seul industriel) : deux analyses à 12 mois d'écart n'ont classé identiquement que 60 % des références ; décaler ou allonger la fenêtre d'un mois change 4,24 % (allongement) à 6,5 % (décalage) des classes en moyenne ; les auteurs préconisent une mise à jour mensuelle. Le fait vient d'une seule entreprise.
- **Valeur n'est pas criticité.** Une pièce de rechange peu chère mais dont l'absence arrête une ligne est classée C. Flores et Whybark (1986) proposent une matrice à critères multiples ; Teunter et al. (2010) proposent un critère qui peut intégrer la criticité. Le coût d'une panne se traite dans [[Politique de maintenance et coût]].
- **Cibles fixes par classe, loin de l'optimum de coût.** Sur trois jeux réels, classer par valeur ou par volume avec un même niveau de service par classe donne des solutions « far from cost optimal » (Teunter et al., 2010, résumé lu seulement).
- **CV mal défini quand la demande est intermittente.** Beaucoup de zéros gonflent le CV (voir ci-dessus) ; il mélange fréquence et taille, que Croston/SBA séparent. XYZ range alors la plupart des références en Z sans dire pourquoi.
- **Variabilité n'est pas imprévisibilité.** Une série très saisonnière a un CV élevé (donc Y ou Z) et peut pourtant se prévoir finement. XYZ ignore tendance et saisonnalité ; Lokad (éditeur d'un logiciel d'optimisation de stock, qui vend une alternative) critique aussi des classes qui bougent avec l'horizon choisi, et des neuf cases qui manquent la tendance et la saisonnalité. Cadrer l'horizon et le but avant de classer : [[Forecasting framing]].
- **Dépend de la fenêtre et de la période** : mois contre semaine change le CV ; un produit lancé ou arrêté dans la fenêtre fausse A comme X/Y/Z.
- **Pas de lien aux coûts** : ni coût de rupture, ni coût de possession, ni délai fournisseur n'entrent dans les seuils.

## Approches voisines & alternatives

- [[Intermittent demand]] — classe pour choisir la **méthode de prévision** (ADI, CV²) ; XYZ classe pour la **politique**.
- [[Stock de sécurité et taux de service]] — la cible de service par classe s'y traduit en stock de sécurité.
- [[Indicateurs de stock (rotation, couverture, rupture)]] — mesurer ce que la classification a changé, classe par classe.
- [[Hierarchical forecasting]] — agréger les références en familles pour prévoir et réconcilier ; une famille est moins variable que ses références.
- [[Forecasting framing]] — horizon, fréquence et objectif à fixer avant de classer.
- [[Politique de maintenance et coût]] — la criticité d'une pièce de rechange, axe que la valeur ne capture pas.
- **Autres grilles** : ABC-VED (vital, essentiel, désirable) pour la criticité, FSN (rapide, lent, immobile) pour la rotation, HML (prix élevé, moyen, bas) — citées dans une revue de littérature (Praveen et al., 2016).

## Pour aller plus loin

- Dickie, H. F. (1951), *ABC Inventory Analysis Shoots for Dollars, Not Pennies*, Factory Management and Maintenance 109(7), p. 92-94 — référence relevée dans la revue de Praveen, Simha et Venkataram (2016, <https://www.ijraset.com/fileserve.php?FID=5680>), article non lu.
- Scholz-Reiter, Heger, Meinecke, Bergmann (2012), *Integration of demand forecasts in ABC-XYZ analysis: practical investigation at an industrial company*, IJPPM 61(4), p. 445-451 : <https://doi.org/10.1108/17410401211212689> (texte lu).
- Teunter, Babai, Syntetos (2010), *ABC classification: service levels and inventory costs*, Production and Operations Management 19(3), p. 343-352 : <https://doi.org/10.1111/j.1937-5956.2009.01098.x> (seul le résumé a été lu).
- Flores, Whybark (1986), *Multiple Criteria ABC Analysis*, IJOPM 6(3), p. 38-46 : <https://doi.org/10.1108/eb054765> (résumé lu).
- Syntetos, Boylan, Croston (2005), *On the categorization of demand patterns*, JORS 56(5), p. 495-503 : <https://doi.org/10.1057/palgrave.jors.2601841> (métadonnées et résumé lus).
- Pages d'usage, non académiques : Wikipedia, « ABC analysis » (<https://en.wikipedia.org/wiki/ABC_analysis>) ; Wikipédia allemand, « ABC-Analyse » (<https://dewiki.de/Lexikon/ABC-Analyse>, miroir) ; pages d'éditeurs, citées comme sources d'usage et non comme outils : Mecalux (<https://www.mecalux.com/blog/abc-xyz>), Lokad (<https://www.lokad.com/abc-xyz-analysis-inventory>), Tacto (<https://www.tacto.ai/buyer-lexicon/abc-xyz-analysis>) ; MetricGate (<https://metricgate.com/docs/xyz-demand-classification/>).
- Connexions brain : [[Intermittent demand]], [[Stock de sécurité et taux de service]], [[Indicateurs de stock (rotation, couverture, rupture)]], [[Hierarchical forecasting]], [[Forecasting framing]], [[Politique de maintenance et coût]].
