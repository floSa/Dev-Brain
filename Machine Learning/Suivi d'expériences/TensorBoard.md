---
role: brique
nom: TensorBoard
alias: [tensorboard, tb]
pitch: "Boîte à outils de visualisation d'entraînement de TensorFlow — courbes de scalaires, histogrammes, graphe du modèle, images et projecteur d'embeddings depuis des event files locaux ; branché à PyTorch via torch.utils.tensorboard."
categorie: ml/tracking
famille: application
licence_type: open-source
hosted: [self]
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[MLflow]]", "[[Weights & Biases]]"]
complements: []
tags: [experiment-tracking, deep-learning, dataviz]
url_docs: https://www.tensorflow.org/tensorboard
url_repo: https://github.com/tensorflow/tensorboard
---

# TensorBoard

## Pourquoi

Boîte à outils de **visualisation d'entraînement**, issue de [[TensorFlow]] mais devenue framework-agnostique. Le code écrit des **event files** dans un répertoire de logs ; le serveur web `tensorboard --logdir` les lit et affiche des dashboards : courbes de **scalaires** (loss, métriques), **histogrammes** de poids/gradients, **graphe** du modèle, **images/audio**, projecteur d'**embeddings** (PCA/t-SNE) et profilage. C'est l'outil local par défaut pour *voir ce que fait un entraînement* sans envoyer de données à un service tiers. Côté [[PyTorch]], `torch.utils.tensorboard.SummaryWriter` écrit ces logs nativement ; la plupart des trackers (MLflow, W&B) savent aussi importer ou afficher des logs TensorBoard.

## Quand l'utiliser

- **Visualisation rapide et locale** d'un entraînement (scalaires, histogrammes) sans compte ni SaaS.
- Projet [[PyTorch]] / [[TensorFlow]] / `transformers` : `SummaryWriter` ou le callback intégré suffit.
- Inspecter le **graphe** d'un modèle, des **images** générées ou un **projecteur d'embeddings**.
- Profiler l'utilisation GPU/étapes via le plugin Profiler.

## Quand NE PAS l'utiliser

- **Comparer des centaines de runs**, collaborer en équipe, gérer un **registre de modèles** → [[MLflow]] ou [[Weights & Biases]] (TensorBoard reste centré visualisation, pas gestion d'expériences).
- Recherche d'hyperparamètres orchestrée (sweeps) → [[Weights & Biases]], [[Optuna]].
- Suivi ultra-léger de très nombreux runs en self-host → [[Aim]].

## Déploiement & coût

- Open-source (Apache-2.0), gratuit ; `uv add tensorboard`. Serveur web local (`--logdir`), aucun backend à gérer.
- Cœur Python (UI en TypeScript) ; lit des event files sur disque ou stockage objet.
- Single-node : sert des logs ; ne stocke pas d'artefacts ni de métadonnées de run au-delà des events.
- TensorBoard.dev (hébergement public de logs) a été **fermé** : partage = exposer son propre serveur ou exporter.

## Pièges

- Les **event files** grossissent vite (histogrammes, images) ; cadrer la fréquence de log et purger les vieux runs.
- Pas d'authentification : ne pas exposer `tensorboard` brut sur Internet, le placer derrière un reverse-proxy.
- Comparaison de runs **limitée** (pas de tableaux de hyperparamètres riches comme un tracker dédié).
- Recharge incrémentale parfois capricieuse sur de gros logdir : rafraîchir / relancer si les courbes figent.

## Alternatives

- [[MLflow]] — Plateforme open-source de cycle de vie ML (Linux Foundation) — tracking d'expériences, registre de modèles, packaging et déploiement, agnostique au framework et au cloud.
- [[Weights & Biases]] — Plateforme SaaS de suivi d'expériences et de visualisation — dashboards riches, sweeps d'hyperparamètres, artefacts et registre de modèles ; référence en R&D deep learning.

Nuance : TensorBoard **visualise** un entraînement (local, gratuit, sans gestion de runs) ; MLflow et W&B sont des **plateformes de tracking** (comparaison de runs, registre, collaboration) qui peuvent d'ailleurs intégrer ses logs.

## Liens

- [[PyTorch]] — `torch.utils.tensorboard.SummaryWriter` écrit les logs nativement.
- [[TensorFlow]] — projet d'origine ; callback Keras intégré.
- [[HuggingFace]] — le `Trainer` logge vers TensorBoard via `report_to`.
- [[MLflow]] · [[Weights & Biases]] · [[Aim]] — trackers qui en prennent le relais à l'échelle.
- Doc : https://www.tensorflow.org/tensorboard
