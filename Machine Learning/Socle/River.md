---
role: brique
nom: River
alias: [riverml, river-ml, online-ml]
pitch: "ML en ligne / streaming en Python — apprentissage incrémental échantillon par échantillon (learn_one/predict_one) couvrant classification, régression, clustering, détection d'anomalies et de dérive ; issu de la fusion creme + scikit-multiflow."
categorie: ml/socle
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: []
tags: [streaming, concept-drift]
url_docs: https://riverml.xyz/
url_repo: https://github.com/online-ml/river
---

# River

<!-- AUTO:BANDEAU:START -->
> ML en ligne / streaming en Python — apprentissage incrémental échantillon par échantillon (learn_one/predict_one) couvrant classification, régression, clustering, détection d'anomalies et de dérive ; issu de la fusion creme + scikit-multiflow.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

L'apprentissage **en ligne** en Python : les modèles apprennent **un échantillon à la fois** (`learn_one` / `predict_one`), sans jamais charger tout le jeu de données en mémoire. La bibliothèque couvre classification, régression, clustering, recommandation, détection d'anomalies et détection de dérive, plus les métriques calculées en continu ; elle est née de la fusion de **creme** et **scikit-multiflow**. Le paradigme a deux conséquences qui décident de l'adoption. L'API `_one` — un échantillon est un `dict`, pas une ligne de matrice — est très éloignée du monde batch : le pipeline est à repenser, pas à porter. Et l'évaluation change de forme : on mesure en **progressive validation** (test-then-train), le découpage temporel étant implicite, un train/test classique n'ayant plus de sens. Enfin, sur données stationnaires, un modèle online est souvent moins performant qu'un batch bien réglé — ce qu'on achète ici est l'adaptation, pas l'exactitude brute.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Flux de données continus : arrivée en temps réel, volume au-delà de la RAM, ou séries non stationnaires | Jeu de données **statique** qui tient en mémoire → [[Scikit-Learn]] : plus de modèles, et plus rapide hors ligne |
| Modèles qui s'adaptent à la dérive sans ré-entraînement batch : détecteurs ADWIN, Page-Hinkley, DDM | Deep learning sur GPU → [[PyTorch]] ou [[Keras]] |
| Apprentissage incrémental à faible empreinte mémoire : un seul échantillon à la fois | Entraînement distribué multi-nœuds sur flux → Spark Structured Streaming et MLlib, hors brain |
| Prototyper un pipeline streaming : prétraitement online, métriques progressives (`progressive_val_score`) | |

## Mise en œuvre

- Installation — `uv add river` ; versions 0.x, API encore mouvante d'une mineure à l'autre
- Point d'entrée — import Python : `learn_one` / `predict_one`, et `progressive_val_score` pour évaluer
- Prérequis — aucun ; pur Python, cœurs critiques optimisés
- Exécution — single-node, conçue pour une faible latence par échantillon sur CPU ; s'embarque dans un service d'inférence qui continue d'apprendre en production
- Coût — gratuit, BSD-3-Clause ; rien à héberger

## Écosystème

### Alternatives

- Pas d'équivalent direct dans le brain : scikit-learn en est le pendant **batch**, avec quelques estimateurs à `partial_fit` pour de l'incrémental limité. Hors brain — Vowpal Wabbit (online learning haute performance) et Spark Streaming MLlib (flux distribué).

## Ressources

- Documentation — https://riverml.xyz/
- Dépôt — https://github.com/online-ml/river

## Voir aussi

- [[Socle]] — le hub du domaine
- [[Data drift]] — ce à quoi River répond, par apprentissage incrémental et détecteurs intégrés
