---
galaxie: dev
type: service
nom: Weights & Biases
alias: [wandb, W&B]
pitch: "Plateforme SaaS de suivi d'expériences et de visualisation — dashboards riches, sweeps d'hyperparamètres, artefacts et registre de modèles ; référence en R&D deep learning."
categorie: ml/tracking
licence_type: proprietary
hosted: both
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Dev/Services/MLflow|MLflow]]", "[[Dev/Services/Neptune|Neptune]]", "[[Dev/Services/Comet|Comet]]", "[[Dev/Services/ClearML|ClearML]]", "[[Dev/Services/Aim|Aim]]", "[[Dev/Services/TensorBoard|TensorBoard]]"]
remplace_par: []
status: actif
tags: [experiment-tracking, model-registry]
url_docs: https://docs.wandb.ai/
url_repo: https://github.com/wandb/wandb
---

# Weights & Biases

## Pourquoi

Plateforme commerciale de suivi d'expériences devenue un standard de fait en recherche deep learning. Quelques lignes (`wandb.init`, `wandb.log`) suffisent à streamer métriques, courbes, gradients, images et tables vers des **dashboards interactifs** partageables. Au-delà du tracking : **Sweeps** (recherche d'hyperparamètres distribuée), **Artifacts** (versionnage de datasets et modèles), **Model Registry** et **Reports** (rapports collaboratifs). SDK open-source, plateforme propriétaire.

## Quand l'utiliser

- Besoin de **visualisations riches** et de partage/collaboration soignés.
- R&D deep learning : suivi fin (gradients, médias, métriques système GPU).
- Campagnes d'hyperparamètres via **Sweeps** intégrés au tracking.
- Équipe acceptant un SaaS (ou disposant d'une licence self-host entreprise).

## Quand NE PAS l'utiliser

- Tout doit rester **open-source et gratuit** en self-host → [[Dev/Services/MLflow|MLflow]] ou [[Dev/Services/Aim|Aim]].
- MLOps tout-en-un (orchestration, données) → [[Dev/Services/ClearML|ClearML]].
- Budget contraint à grande échelle : la facturation à l'usage peut grimper.

## Déploiement & coût

- SaaS managé (cloud W&B) : gratuit en perso/recherche, payant par siège en équipe.
- Self-host entreprise (**W&B Server**, architecture horizontalement scalable) sous licence commerciale.
- SDK `wandb` open-source ; la plateforme et le serveur restent propriétaires.

## Pièges

- Données envoyées au **cloud** par défaut : vérifier la conformité avant d'y mettre des données sensibles.
- Le mode *online* bloque/retarde si le réseau tombe ; prévoir le mode `offline` puis sync.
- Coût qui croît avec le volume loggé (médias, métriques système) — cadrer ce qu'on journalise.

## Alternatives

- [[Dev/Services/MLflow|MLflow]] — Plateforme open-source de cycle de vie ML (Linux Foundation) — tracking d'expériences, registre de modèles, packaging et déploiement, agnostique au framework et au cloud.
- [[Dev/Services/Neptune|Neptune]] — Tracker d'expériences SaaS spécialisé entraînements longue durée et foundation models — racheté par OpenAI, service hébergé arrêté en mars 2026.
- [[Dev/Services/Comet|Comet]] — Plateforme SaaS de suivi d'expériences ML couplée à l'observabilité LLM (Opik, open-source) — du tracking classique au monitoring d'applications génératives.
- [[Dev/Services/ClearML|ClearML]] — Plateforme MLOps open-source tout-en-un — tracking automatique sans code, plus gestion de données, pipelines, orchestration d'agents et serving.
- [[Dev/Services/Aim|Aim]] — Tracker d'expériences open-source léger et auto-hébergé — UI de comparaison rapide sur des centaines de milliers de runs, sans dépendance à un SaaS.
- [[Dev/Services/TensorBoard|TensorBoard]] — Boîte à outils de visualisation d'entraînement de TensorFlow — courbes de scalaires, histogrammes, graphe du modèle, images et projecteur d'embeddings depuis des event files locaux ; branché à PyTorch via torch.utils.tensorboard.

## Liens

- S'intègre avec : [[Dev/Services/PyTorch|PyTorch]], [[Dev/Services/TensorFlow|TensorFlow]], [[Dev/Services/HuggingFace|HuggingFace]], [[Dev/Services/Optuna|Optuna]].
- Doc : https://docs.wandb.ai/
