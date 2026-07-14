---
galaxie: dev
type: service
nom: MLflow
alias: [mlflow]
pitch: "Plateforme open-source de cycle de vie ML (Linux Foundation) — tracking d'expériences, registre de modèles, packaging et déploiement, agnostique au framework et au cloud."
categorie: ml/tracking
licence_type: open-source
hosted: both
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Weights & Biases|Weights & Biases]]", "[[Dev/Services/Neptune|Neptune]]", "[[Dev/Services/Comet|Comet]]", "[[Dev/Services/ClearML|ClearML]]", "[[Dev/Services/Aim|Aim]]", "[[Dev/Services/TensorBoard|TensorBoard]]"]
remplace_par: []
status: actif
tags: [experiment-tracking, model-registry]
url_docs: https://mlflow.org/docs/latest/
url_repo: https://github.com/mlflow/mlflow
---

# MLflow

## Pourquoi

Standard open-source du cycle de vie ML, hébergé par la Linux Foundation. Quatre briques modulaires : **Tracking** (journalise paramètres, métriques, artefacts et code de chaque run), **Model Registry** (versionnage, stades et promotion des modèles), **Projects** (packaging reproductible) et **Models** (format d'échange + déploiement multi-cibles). Agnostique au framework (scikit-learn, PyTorch, XGBoost, LLM…) et au cloud, avec un *autologging* qui capture l'essentiel sans instrumenter le code. 30M+ de téléchargements/mois.

## Quand l'utiliser

- Brique de tracking **auto-hébergeable et gratuite**, sans dépendance à un SaaS.
- Besoin d'un **registre de modèles** ouvert pour gérer stades et promotions.
- Stack hétérogène : un seul format de modèle pour servir partout.
- Déjà sur Databricks → Managed MLflow intégré (auth, Unity Catalog) sans rien opérer.

## Quand NE PAS l'utiliser

- Dashboards de visualisation très riches et collaboration temps réel → [[Dev/Services/Weights & Biases|Weights & Biases]].
- MLOps tout-en-un (données, pipelines, orchestration) clé en main → [[Dev/Services/ClearML|ClearML]].
- Suivi ultra-léger sans serveur à gérer → [[Dev/Services/Aim|Aim]].

## Déploiement & coût

- Open-source (Apache-2.0), `uv add mlflow`. En local : fichiers + UI via `mlflow ui`.
- En équipe : serveur de tracking (single-node) adossé à une base SQL (Postgres) + un stockage d'artefacts (S3/MinIO).
- Offre managée : Databricks Managed MLflow (payant, intégré à la plateforme).

## Pièges

- Le serveur de tracking par défaut n'a **aucune authentification** : à placer derrière un reverse-proxy / SSO.
- Le `mlruns/` local sur disque grossit vite ; viser tôt un backend SQL + stockage objet.
- L'autologging diffère selon les frameworks : vérifier ce qui est réellement capturé.

## Alternatives

- [[Dev/Services/Weights & Biases|Weights & Biases]] — Plateforme SaaS de suivi d'expériences et de visualisation — dashboards riches, sweeps d'hyperparamètres, artefacts et registre de modèles ; référence en R&D deep learning.
- [[Dev/Services/Neptune|Neptune]] — Tracker d'expériences SaaS spécialisé entraînements longue durée et foundation models — racheté par OpenAI, service hébergé arrêté en mars 2026.
- [[Dev/Services/Comet|Comet]] — Plateforme SaaS de suivi d'expériences ML couplée à l'observabilité LLM (Opik, open-source) — du tracking classique au monitoring d'applications génératives.
- [[Dev/Services/ClearML|ClearML]] — Plateforme MLOps open-source tout-en-un — tracking automatique sans code, plus gestion de données, pipelines, orchestration d'agents et serving.
- [[Dev/Services/Aim|Aim]] — Tracker d'expériences open-source léger et auto-hébergé — UI de comparaison rapide sur des centaines de milliers de runs, sans dépendance à un SaaS.
- [[Dev/Services/TensorBoard|TensorBoard]] — Boîte à outils de visualisation d'entraînement de TensorFlow — courbes de scalaires, histogrammes, graphe du modèle, images et projecteur d'embeddings depuis des event files locaux ; branché à PyTorch via torch.utils.tensorboard.

## Liens

- Concept implémenté : [[Model registry & versioning]] (stades, alias, lignage) ; voisins [[Déploiement de modèles]], [[Monitoring de modèle en production]].
- S'intègre avec : [[Dev/Services/PyTorch|PyTorch]], [[Dev/Services/Scikit-Learn|Scikit-Learn]], [[Dev/Services/XGBoost|XGBoost]], [[Dev/Services/Optuna|Optuna]].
- Doc : https://mlflow.org/docs/latest/
