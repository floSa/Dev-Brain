---
galaxie: dev
type: service
nom: Seldon Core
alias: [seldon, seldon-core]
pitch: "Plateforme de serving et d'orchestration d'inférence sur Kubernetes — graphes d'inférence multi-étapes, explicabilité et monitoring ; passée en licence source-available (BSL) depuis 2024."
categorie: ml/serving
licence_type: source-available
hosted: self
maturite: production
langage: Go
scaling: distributed
alternatives: ["[[Dev/Services/BentoML|BentoML]]", "[[Dev/Services/NVIDIA Triton|NVIDIA Triton]]", "[[Dev/Services/KServe|KServe]]", "[[Dev/Services/TorchServe|TorchServe]]", "[[Dev/Services/TensorFlow Serving|TensorFlow Serving]]", "[[Dev/Services/Ray Serve|Ray Serve]]"]
remplace_par: []
status: actif
tags: [model-serving, inference, kubernetes]
url_docs: https://docs.seldon.ai/
url_repo: https://github.com/SeldonIO/seldon-core
---

# Seldon Core

## Pourquoi

Plateforme de serving et d'**orchestration d'inférence** sur **Kubernetes**. Au-delà d'exposer un modèle, elle compose des **graphes d'inférence** multi-étapes (transformers, routeurs, combiners, détecteurs de drift, explainers) déployés comme un seul service. Multi-framework, avec un serveur d'inférence open-source de bas niveau, **MLServer** (protocole V2, compatible KServe). Brique historique du serving ML K8s, **co-créatrice de KServe**. Point de vigilance majeur : depuis le **22 janvier 2024**, Seldon Core (v1 et v2) est passé d'Apache-2.0 à la **Business Source License (BSL 1.1)** — *source-available*, gratuit hors production, payant en production (conversion en Apache-2.0 quatre ans après chaque release).

## Quand l'utiliser

- **Pipelines d'inférence complexes** : pré/post-traitement, routage A/B, ensembles, explainers en un graphe.
- Besoin d'**explicabilité** (Alibi Explain) et de détection de drift/outliers (Alibi Detect) intégrés au serving.
- Déjà sur Kubernetes, avec une équipe à l'aise pour opérer une plateforme MLOps complète.
- Acceptation des **termes BSL** (usage non-production gratuit, licence commerciale en production).

## Quand NE PAS l'utiliser

- Contrainte stricte **open-source en production** → [[Dev/Services/KServe|KServe]] (Apache-2.0, CNCF) ou MLServer seul (Apache-2.0).
- Serveur Python simple sans Kubernetes → [[Dev/Services/BentoML|BentoML]].
- Latence GPU brute sur un parc multi-framework → [[Dev/Services/NVIDIA Triton|NVIDIA Triton]].

## Déploiement & coût

- **Source-available** (BSL 1.1) depuis 2024 : gratuit en non-production, **licence commerciale requise en production**. MLServer, lui, reste open-source (Apache-2.0).
- Self-host sur Kubernetes (CRD, opérateurs Go) ; offre entreprise commerciale au-dessus.
- Scaling distribué par conception (réplicas K8s, graphes répartis).

## Pièges

- **Changement de licence** : vérifier l'éligibilité BSL avant tout usage en production — c'est le critère décisif vs [[Dev/Services/KServe|KServe]].
- Deux générations (Core v1 vs v2/MLServer) aux architectures différentes : ne pas mélanger la doc.
- Plateforme riche = surface opérationnelle large (K8s, réseau, observabilité à câbler).

## Alternatives

- [[Dev/Services/BentoML|BentoML]] — Framework Python de packaging et de service de modèles — transforme n'importe quel modèle (ML, LLM, pipelines multi-modèles) en API d'inférence, du prototype au déploiement scalable (BentoCloud / Kubernetes).
- [[Dev/Services/NVIDIA Triton|NVIDIA Triton]] — Serveur d'inférence multi-framework de NVIDIA (TensorRT, PyTorch, ONNX, TensorFlow…) — batching dynamique et exécution concurrente sur GPU/CPU, optimisé débit/latence ; intégré à la plateforme Dynamo.
- [[Dev/Services/KServe|KServe]] — Plateforme d'inférence standard sur Kubernetes (CNCF) — déploiement déclaratif via la CRD InferenceService, autoscaling serverless jusqu'à zéro (Knative), multi-framework, prédictif et génératif.
- [[Dev/Services/TorchServe|TorchServe]] — Serveur de modèles PyTorch (handlers Python, frontend Java) — packaging .mar, batching et versionnage ; projet archivé et non maintenu depuis août 2025.
- [[Dev/Services/TensorFlow Serving|TensorFlow Serving]] — Serveur d'inférence haute performance pour modèles TensorFlow/Keras — API REST et gRPC, versionnage et batching de modèles, cœur C++ éprouvé ; intégré à TFX.
- [[Dev/Services/Ray Serve|Ray Serve]] — Bibliothèque de serving scalable bâtie sur Ray : déploiements Python framework-agnostiques, composition multi-modèles (deployment graphs) et autoscaling, du prototype au cluster.

## Liens

- Concurrent direct et co-fondé : [[Dev/Services/KServe|KServe]] (protocole d'inférence V2 partagé).
- Tourne sur Kubernetes ([[Dev/Services/Docker|Docker]] pour les images).
- [[Comparatif - Serving de modèles]] — comparatif de la catégorie
- Doc : https://docs.seldon.ai/
