---
galaxie: wiki
type: concept
nom: Détection d'outliers multivariée
alias: [outliers multivarié, LOF, Isolation Forest, Elliptic Envelope, ECOD, COPOD, Mahalanobis]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [anomaly-detection, unsupervised]
---

# Détection d'outliers multivariée

## Aperçu

- Repérer des points aberrants dans l'**espace conjoint** de plusieurs variables : un individu normal sur chaque axe peut violer la **structure de corrélation** et n'être détectable qu'en multivarié.
- Tâche **non supervisée** : pas de labels d'anomalie. On modélise le « normal » (densité, distance, isolation) et on score l'écart.

## Concepts clés

### Distance — Elliptic Envelope (Mahalanobis)
- Ajuste une **gaussienne robuste** (covariance par déterminant minimal, MCD) et mesure la distance de **Mahalanobis**, qui tient compte des corrélations.
- Hypothèse forte : données ~ ellipsoïde gaussien unimodal. Échoue sur des structures non convexes ou multimodales.

### Densité — LOF (Local Outlier Factor)
- Compare la densité **locale** d'un point à celle de ses voisins : un point en zone clairsemée près d'un cluster dense est un outlier. $\text{LOF} \gg 1$ → anomalie.
- Capte les anomalies **locales** que les méthodes globales ratent ; sensible au choix de $k$ (nombre de voisins). Parent de [[DBSCAN]] (mêmes notions de densité).

### Isolation — Isolation Forest
- Renverse la logique : au lieu de modéliser le normal, on **isole** l'anormal. Des arbres à coupures aléatoires isolent un outlier en **peu de découpes** (chemin court).
- Rapide, passe à l'échelle, peu d'hypothèses ; le détecteur par défaut sur tabulaire.

### Sans paramètre — ECOD / COPOD
- **ECOD** : fonctions de répartition empiriques par dimension, agrégées en probabilité de queue. **COPOD** : modélise la dépendance par **copule** empirique.
- **Zéro hyperparamètre**, déterministes, rapides — d'excellents baselines (auteurs de [[Dev/Services/PyOD|PyOD]]).

## Les maths, simplement

- Mahalanobis : $d_M(x) = \sqrt{(x-\mu)^\top \Sigma^{-1}(x-\mu)}$ ; sous gaussienne, $d_M^2$ suit un $\chi^2_p$ → seuil par quantile.
- Isolation Forest : score $s(x) = 2^{-\,\mathbb{E}[h(x)]/c(n)}$, où $h(x)$ est la profondeur d'isolation et $c(n)$ la profondeur moyenne d'un BST ; $s \to 1$ = anomalie, $s \to 0{,}5$ = normal.
- LOF : rapport de densité $\text{LOF}_k(x) = \dfrac{1}{|N_k(x)|}\sum_{o\in N_k(x)} \dfrac{\text{lrd}_k(o)}{\text{lrd}_k(x)}$, où $\text{lrd}$ est la densité locale d'atteignabilité.

## En pratique

- [[Dev/Services/PyOD|PyOD]] unifie tous ces détecteurs (et 50+ autres) sous une API scikit-learn : comparer plusieurs méthodes vaut mieux qu'en parier une.
- LOF, IsolationForest et EllipticEnvelope sont aussi **natifs dans scikit-learn**.
- Régler la **contamination** (proportion d'outliers attendue) fixe le seuil de décision ; à défaut, raisonner sur les **scores** continus.
- **Standardiser** les variables ([[Mise à l'échelle]]) avant les méthodes à distance/densité (Mahalanobis le fait implicitement, pas LOF).
- Anomalie **collective** ou dépendante du temps → ce cadre statique ne suffit pas : [[Time series anomaly detection|Détection d'anomalies temporelles]].

## Approches voisines & alternatives

- [[Détection d'outliers univariée]] — seuils par variable, quand les corrélations n'entrent pas en jeu.
- [[Isolation Forest]] — le détecteur par défaut sur tabulaire : linéaire en $n$, sans standardisation.
- [[Time series anomaly detection|Détection d'anomalies temporelles]] — anomalies de forme/dynamique dans une série.
- [[DBSCAN]] — clustering par densité ; les points « bruit » sont de fait des outliers.
- [[Clustering]] — l'éloignement à tout cluster est un signal d'anomalie.
- [[Data drift]] — la détection d'anomalies sert aussi à repérer une dérive de distribution en production.

## Pour aller plus loin

- Breunig et al. (2000) — *LOF: Identifying Density-Based Local Outliers*.
- Liu et al. (2008) — *Isolation Forest*.
- Li et al. (2022/2020) — *ECOD* et *COPOD* (détecteurs sans paramètre).
