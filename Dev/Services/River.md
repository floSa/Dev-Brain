---
galaxie: dev
type: service
nom: River
alias: [riverml, river-ml, online-ml]
pitch: "ML en ligne / streaming en Python — apprentissage incrémental échantillon par échantillon (learn_one/predict_one) couvrant classification, régression, clustering, détection d'anomalies et de dérive ; issu de la fusion creme + scikit-multiflow."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [streaming, concept-drift]
url_docs: https://riverml.xyz/
url_repo: https://github.com/online-ml/river
---

# River

## Pourquoi

River fait de l'**apprentissage en ligne** (online / incrémental) en Python : les modèles apprennent **un échantillon à la fois** (`learn_one` / `predict_one`), sans jamais charger tout le dataset en mémoire. Il couvre classification, régression, clustering, recommandation, détection d'anomalies et **détection de dérive**, plus les métriques calculées en continu. Né de la fusion de **creme** et **scikit-multiflow**, c'est la bibliothèque de référence pour le ML sur flux.

## Quand l'utiliser

- **Flux de données** continus : données qui arrivent en temps réel, trop volumineuses pour la RAM, ou non stationnaires.
- Modèles qui **s'adaptent à la dérive** (cf. [[Data drift]]) sans ré-entraînement batch : détecteurs ADWIN, Page-Hinkley, DDM.
- Apprentissage incrémental à faible empreinte mémoire (un seul échantillon en mémoire à la fois).
- Prototyper un pipeline streaming : prétraitement online, métriques progressives (`progressive_val_score`).

## Quand NE PAS l'utiliser

- Dataset **statique** qui tient en mémoire → [[Dev/Services/Scikit-Learn|Scikit-Learn]] (batch : plus de modèles, plus rapide hors ligne).
- Deep learning sur GPU → [[Dev/Services/PyTorch|PyTorch]] / [[Dev/Services/Keras|Keras]].
- Entraînement **distribué** multi-nœuds sur flux → Spark Structured Streaming + MLlib (hors brain).

## Déploiement & coût

- Open-source (BSD-3-Clause), gratuit ; `uv add river`. Rien à héberger.
- Pur Python (cœurs critiques optimisés), **single-node**, conçu pour une faible latence par échantillon (CPU). S'embarque dans un service d'inférence qui continue d'apprendre en production.

## Pièges

- API **`_one`** (un échantillon = un `dict`) très éloignée du paradigme matrices / batch de scikit-learn — le pipeline est à repenser.
- Évaluer en **progressive validation** (test-then-train), pas en train/test classique : le découpage temporel est implicite.
- Les modèles online sont souvent moins performants qu'un batch bien réglé sur données stationnaires — l'intérêt est l'adaptation, pas l'accuracy brute.
- Versions 0.x : API encore mouvante d'une mineure à l'autre.

## Alternatives

Pas d'équivalent direct dans le brain. [[Dev/Services/Scikit-Learn|Scikit-Learn]] est le pendant **batch** (quelques estimateurs offrent `partial_fit` pour de l'incrémental limité). Hors brain : Vowpal Wabbit (online learning haute performance), Spark Streaming MLlib (flux distribué).

## Liens

- [[Data drift]] — River y répond par apprentissage incrémental et détecteurs de dérive intégrés.
- [[Dev/Services/Scikit-Learn|Scikit-Learn]] — le pendant batch ; River en reprend les conventions d'API, côté flux.
- Doc : https://riverml.xyz/
