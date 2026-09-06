---
role: comparatif
nom: Comparatif - Suivi d'expériences ML
categorie: ml/tracking
tags: [experiment-tracking, model-registry]
---

# Comparatif - Suivi d'expériences ML

> On tranche sur : où partent les données — self-host ou cloud —, et jusqu'où va l'outil au-delà des courbes : registre de modèles, orchestration, ou rien.

![[Comparatif - Suivi d'expériences ML.base]]

## Ce qui départage

- [[MLflow]] — le seul à porter un **registre de modèles** ouvert (stades, promotions) et un format d'échange servi partout, le tout auto-hébergeable et hébergé par la Linux Foundation. Son serveur de tracking par défaut n'a **aucune authentification**, et le `mlruns/` sur disque impose vite un backend SQL + stockage objet.
- [[Aim]] — le tracker **léger** : self-host, Apache-2.0, une UI qui tient des centaines de milliers de runs et un SDK de requêtes sur les métadonnées. Pas de registre de modèles ni de RBAC, et les runs vivent sur le disque du serveur Aim — sauvegarde et rétention à prévoir.
- [[ClearML]] — dépasse le tracking : données versionnées, pipelines, **agents et files d'attente** pour orchestrer un parc de GPU, et une capture **sans modifier le code**. Le prix est un serveur self-host à plusieurs services (ES, Mongo, Redis) et une autocapture qui logge plus que prévu.
- [[Weights & Biases]] — les visualisations DL de référence, plus les **Sweeps** d'hyperparamètres intégrés au tracking et les Reports collaboratifs. SaaS propriétaire : données au cloud par défaut, mode *online* qui bloque si le réseau tombe, et facturation qui croît avec le volume loggé.
- [[Comet]] — le seul à couvrir le tracking ML **et** l'observabilité LLM, via **Opik** (tracing et évaluation de RAG/agents), déployable en Docker/Kubernetes. Attention au périmètre : le cœur Comet est propriétaire, Opik seul est open-source.
- [[TensorBoard]] — pas un tracker mais un **visualiseur** : le code écrit des *event files*, le serveur les lit — graphe du modèle, histogrammes de gradients, projecteur d'embeddings, profilage. Comparaison de runs limitée, aucune authentification, et les event files grossissent vite.
- [[Neptune]] — le critère est de cycle de vie, pas de fonction : racheté par OpenAI en décembre 2025, **service hébergé arrêté le 5 mars 2026**. Plus de nouvel usage — export de données existantes seulement.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
