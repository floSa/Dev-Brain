---
galaxie: wiki
type: concept
nom: Suivi d'objets
alias: [object tracking, MOT, multi-object tracking, suivi multi-cibles, tracking-by-detection, SORT, DeepSORT, ByteTrack, Kalman, MOTA, IDF1, HOTA]
categorie: concept/dl
domaines: [data-sci, ml-eng]
tags: [object-tracking, object-detection, computer-vision, deep-learning]
---

# Suivi d'objets

## Aperçu

- Maintenir l'**identité** d'objets d'une frame à l'autre dans une vidéo : sortie = des **trajectoires** (boîtes + un ID stable dans le temps), pas juste des détections isolées.
- Le cas multi-cibles s'appelle **MOT** (Multi-Object Tracking) : plusieurs objets de même classe, apparitions, disparitions, occlusions.

## Concepts clés

### Tracking-by-detection
- Paradigme dominant : un [[Détection d'objets|détecteur]] tourne **à chaque frame**, puis une étape d'**association** relie les détections aux pistes existantes. La qualité du suivi dépend d'abord de celle du détecteur.

### Les trois briques
- **Modèle de mouvement** : un filtre de **Kalman** prédit où chaque piste va se trouver (souvent vitesse constante).
- **Association** : apparier détections ↔ pistes en minimisant un coût (algorithme **hongrois**), coût = recouvrement spatial ([[Métriques vision|IoU]]) et/ou similarité d'apparence.
- **Cycle de vie** : naissance d'une piste, mort après N frames sans match (max age).

### SORT → DeepSORT → ByteTrack
- **SORT** : Kalman + hongrois sur l'IoU. Très rapide, en ligne, **sans apparence** → beaucoup de changements d'identité (*ID switches*) sur occlusion.
- **DeepSORT** : ajoute une **signature d'apparence** (embedding de [[Metric learning & ré-identification|ré-identification]]) au coût d'association → bien plus robuste aux occlusions.
- **ByteTrack** : associe en deux temps — d'abord les boîtes très confiantes, puis **récupère les boîtes peu confiantes** (le pas *BYTE*) souvent dues à une occlusion partielle. SOTA, simple, sans modèle de ré-id.

## Les maths, simplement

- Association = problème d'affectation : minimiser $\sum_{i,j} C_{ij}\,x_{ij}$ (algorithme hongrois), avec un coût $C_{ij}$ p. ex. $1-\text{IoU}$ (SORT) ou une combinaison distance de Mahalanobis (mouvement) + cosinus (apparence) dans DeepSORT.
- Kalman : alternance **prédiction** (propager l'état) / **mise à jour** (corriger avec la détection observée).

## En pratique

- Défaut pragmatique : **ByteTrack** (excellent rapport simplicité/qualité), **DeepSORT** si beaucoup d'occlusions et qu'on dispose d'un bon modèle de ré-id. Implémentation prête à l'emploi (ByteTrack, annotation, comptage par zones) : [[Dev/Services/supervision|supervision]].
- Métriques MOT : **MOTA** (agrège FP, FN, ID switches), **IDF1** (préservation de l'identité), **HOTA** (équilibre détection et association — la métrique moderne de référence).
- Variantes *joint detection & embedding* (JDE, FairMOT) et transformeurs (TrackFormer, MOTR) fusionnent détection et association en un seul réseau.

## Approches voisines & alternatives

- [[Détection d'objets]] — le moteur par-frame du tracking-by-detection.
- [[Metric learning & ré-identification]] — fournit l'embedding d'apparence qui rend DeepSORT robuste.
- [[Estimation de pose]] — le *pose tracking* applique la même logique d'association aux squelettes.
- [[Vision par ordinateur]] — le cadre d'ensemble.

## Pour aller plus loin

- Bewley et al. (2016) — *SORT* · Wojke et al. (2017) — *DeepSORT*.
- Zhang et al. (2022) — *ByteTrack* (association des boîtes basse confiance).
