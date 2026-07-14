---
galaxie: wiki
type: concept
nom: EDA automatisée & profiling
alias: [EDA, analyse exploratoire, exploratory data analysis, data profiling, profiling de données]
categorie: concept/ml
domaines: [data-sci, data-eng]
tags: [eda, feature-engineering, missing-data]
---

# EDA automatisée & profiling

## Aperçu

- Produire automatiquement un **portrait d'un jeu de données** : par variable (type, distribution, valeurs manquantes, cardinalité, extrêmes) et entre variables (corrélations, doublons). En un rapport, là où l'EDA manuelle prend des heures.
- But : comprendre la donnée et repérer les problèmes **avant** de modéliser. Étape charnière entre l'ingestion et l'[[Ingénierie des caractéristiques]].

## Concepts clés

### Profiling par variable (univarié)
- Pour chaque colonne : type inféré, statistiques (min/max, moyenne, quantiles), histogramme, taux de manquants, nombre de valeurs distinctes, valeurs les plus fréquentes.
- Repère d'emblée colonnes constantes, quasi-identifiants, formats incohérents, [[Détection d'outliers univariée|valeurs extrêmes]].

### Relations entre variables (bivarié)
- Matrices de corrélation (Pearson, Spearman, associations catégorielles type Cramér's V), variables fortement liées, [[Détection d'outliers multivariée|anomalies multivariées]].
- Signale les **paires redondantes** (colinéarité) et les corrélations suspectes avec la cible — un drapeau de [[Data leakage|fuite de données]].

### Qualité et valeurs manquantes
- Cartographier les trous et leur structure (manquants corrélés entre colonnes) éclaire le choix de stratégie → [[Mécanismes de données manquantes]], [[Imputation des valeurs manquantes]].
- Doublons exacts et quasi-doublons, cohérence de types, dérives de format.

### Automatisé vs ciblé
- Le rapport automatique est un **point de départ** exhaustif mais générique. Il ne remplace ni les questions métier ni la viz ciblée ; il les oriente.

## En pratique

- Lancer le profiling juste après le chargement, avant tout nettoyage, puis le re-jouer après transformation pour vérifier l'effet.
- Sur gros volumes : échantillonner ou désactiver les calculs coûteux (corrélations $O(p^2)$, interactions), sous peine de rapports interminables.
- Lire le rapport comme une **checklist** : manquants, constantes, cardinalités, corrélation avec la cible (fuite), échelles disparates ([[Mise à l'échelle]]), catégories à encoder ([[Encodage des variables catégorielles]]).
- Outils Python : `ydata-profiling` (ex-`pandas-profiling`), `Sweetviz`, `skimpy`, `D-Tale` ; `pandas.DataFrame.describe()` pour le minimum.
- Piège : sur-interpréter des corrélations automatiques (spurious), ou laisser des observations issues de l'ensemble complet biaiser des choix qui devraient se faire sur le train seul (fuite).

## Approches voisines & alternatives

- [[Dev/Services/ydata-profiling|ydata-profiling]], [[Dev/Services/sweetviz|sweetviz]], [[Dev/Services/missingno|missingno]] — les outils Python qui incarnent cette étape (rapport exhaustif, EDA orientée cible, diagnostic des manquants).
- [[Ingénierie des caractéristiques]] — l'étape que l'EDA prépare et oriente.
- [[Mécanismes de données manquantes]], [[Imputation des valeurs manquantes]] — diagnostic puis traitement des trous repérés.
- [[Détection d'outliers univariée]], [[Détection d'outliers multivariée]] — approfondir les valeurs aberrantes signalées.
- [[Data leakage]] — la corrélation cible trop belle que le profiling fait remonter.
- [[Mise à l'échelle]], [[Encodage des variables catégorielles]] — décisions de préparation éclairées par le profil.
- [[Web scraping]] — profiler un corpus fraîchement collecté.

## Pour aller plus loin

- Tukey (1977) — *Exploratory Data Analysis* (la source).
- Documentation `ydata-profiling` — rapport de profiling pandas / Spark.
