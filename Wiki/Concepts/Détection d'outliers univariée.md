---
galaxie: wiki
type: concept
nom: Détection d'outliers univariée
alias: [outliers univarié, Z-score, IQR, MAD, règle de Tukey, modified Z-score]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [anomaly-detection, unsupervised]
---

# Détection d'outliers univariée

## Aperçu

- Repérer, **variable par variable**, les valeurs qui s'écartent anormalement du reste : seuils statistiques simples sur une seule dimension. Premier réflexe en EDA et en nettoyage de données.
- Trois familles selon la statistique de centre/dispersion utilisée : **moyenne/écart-type** (Z-score), **quartiles** (IQR), **médiane/MAD** (robuste).

## Concepts clés

### Z-score
- Distance à la moyenne en nombre d'écarts-types : seuil usuel $|z| > 3$. Suppose une distribution **à peu près normale**.
- Faiblesse : moyenne et écart-type sont eux-mêmes **tirés par les outliers** (effet de masquage). Inadapté aux distributions asymétriques ou à queues lourdes.

### IQR — règle de Tukey
- Fondée sur les quartiles, donc **robuste** : une valeur est suspecte hors de $[Q_1 - 1{,}5\,\text{IQR},\; Q_3 + 1{,}5\,\text{IQR}]$ (facteur 3 pour les outliers « extrêmes »).
- C'est la règle des **boîtes à moustaches** (boxplot). Sans hypothèse de normalité.

### MAD — déviation absolue médiane
- La plus robuste : centre = **médiane**, dispersion = médiane des écarts absolus à la médiane. Résiste jusqu'à ~50 % de contamination.
- Donne le **Z-score modifié**, comparable au Z-score classique mais insensible aux valeurs extrêmes.

### Limite intrinsèque
- L'approche univariée ignore les **corrélations** : un point peut être normal sur chaque axe pris isolément et aberrant dans l'espace conjoint → [[Détection d'outliers multivariée]].

## Les maths, simplement

- Z-score : $z = \dfrac{x - \mu}{\sigma}$ ; on signale $|z| > 3$.
- Bornes de Tukey : $[\,Q_1 - k\,\text{IQR},\; Q_3 + k\,\text{IQR}\,]$ avec $\text{IQR} = Q_3 - Q_1$ et $k = 1{,}5$ (suspect) ou $3$ (extrême).
- MAD : $\text{MAD} = \text{médiane}\big(|x_i - \tilde{x}|\big)$, et Z-score modifié $z_M = \dfrac{0{,}6745\,(x - \tilde{x})}{\text{MAD}}$, seuil $|z_M| > 3{,}5$. Le facteur $0{,}6745$ aligne la MAD sur $\sigma$ en loi normale.

## En pratique

- Calcul direct en `numpy` / `scipy.stats` (`zscore`, `iqr`) ou `pandas` ; aucune dépendance lourde.
- **Préférer IQR ou MAD** au Z-score dès que la distribution est asymétrique ou contaminée — le Z-score se sabote lui-même.
- Toujours **regarder la distribution** (histogramme, boxplot) avant de seuiller : un mode secondaire légitime n'est pas un outlier.
- Distinguer outlier **erreur** (à corriger/exclure) et outlier **signal** (événement rare à garder) — cf. [[Imbalanced classification]].

## Approches voisines & alternatives

- [[Détection d'outliers multivariée]] — quand l'anomalie n'apparaît que dans la structure conjointe des variables.
- [[Time series anomaly detection|Détection d'anomalies temporelles]] — pour un point aberrant relativement à sa dynamique temporelle, pas à une distribution statique.
- [[Imbalanced classification]] — les outliers « signal » rejoignent le cadre des événements rares.
- [[Mise à l'échelle]] — le prétraitement conditionne ce qui sera vu comme aberrant.

## Pour aller plus loin

- Tukey (1977) — *Exploratory Data Analysis* (règle des 1,5 IQR).
- Leys et al. (2013) — *Detecting outliers: do not use standard deviation around the mean, use absolute deviation around the median*.
