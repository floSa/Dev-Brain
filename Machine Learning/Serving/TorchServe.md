---
role: brique
nom: TorchServe
alias: [torchserve, torch-serve]
pitch: "Serveur de modèles PyTorch (handlers Python, frontend Java) — packaging .mar, batching et versionnage ; projet archivé et non maintenu depuis août 2025."
categorie: ml/serving
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: deprecated
langage: Java/Python
scaling: distributed
alternatives: ["[[BentoML]]", "[[NVIDIA Triton]]", "[[KServe]]", "[[Seldon Core]]", "[[TensorFlow Serving]]", "[[Ray Serve]]"]
complements: []
tags: [model-serving, inference, gpu]
url_docs: https://docs.pytorch.org/serve/
url_repo: https://github.com/pytorch/serve
---

# TorchServe

<!-- AUTO:BANDEAU:START -->
> Serveur de modèles PyTorch (handlers Python, frontend Java) — packaging .mar, batching et versionnage ; projet archivé et non maintenu depuis août 2025.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme Java/Python | open-source | self-hébergé · distribué | deprecated |
<!-- AUTO:BANDEAU:END -->

## Définition

Serveur de modèles de l'écosystème PyTorch, créé avec AWS. Un modèle est empaqueté en archive
**`.mar`** avec un **handler** Python de pré/post-traitement ; le serveur — frontend Java,
workers Python — expose des endpoints REST et gRPC, avec batching, versionnage des modèles,
métriques et gestion multi-modèles. Le dépôt a été **archivé le 7 août 2025** : plus de
correctifs, plus de nouvelles fonctionnalités, plus de patchs de sécurité. Il ne se retient
plus pour un nouveau déploiement.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Maintenir un existant déjà bâti sur TorchServe | Tout nouveau déploiement : projet archivé, vulnérabilités non corrigées, risque de conformité en production |
| | Le couple frontend Java / handler Python impose deux runtimes dans l'image et complique le débogage |
| | Écrire un `handler` correct — batch, device, sérialisation — est moins trivial qu'il n'y paraît |

## Mise en œuvre

- Installation — conteneur ou binaire ; plus aucune release depuis l'archivage du dépôt
- Point d'entrée — une archive `.mar` (modèle plus handler Python), servie en REST et gRPC
- Prérequis — un modèle PyTorch, un runtime Java pour le frontend et Python pour les workers
- Exécution — self-hébergé ; réplicas pilotés par l'orchestrateur, souvent KServe par le passé
- Coût — Apache-2.0, dépôt en lecture seule depuis le 7 août 2025 : aucun coût, et aucun support

## Écosystème

### Alternatives

- [[BentoML]] — Framework Python de packaging et de service de modèles — transforme n'importe quel modèle (ML, LLM, pipelines multi-modèles) en API d'inférence, du prototype au déploiement scalable (BentoCloud / Kubernetes).
- [[NVIDIA Triton]] — Serveur d'inférence multi-framework de NVIDIA (TensorRT, PyTorch, ONNX, TensorFlow…) — batching dynamique et exécution concurrente sur GPU/CPU, optimisé débit/latence ; intégré à la plateforme Dynamo.
- [[KServe]] — Plateforme d'inférence standard sur Kubernetes (CNCF) — déploiement déclaratif via la CRD InferenceService, autoscaling serverless jusqu'à zéro (Knative), multi-framework, prédictif et génératif.
- [[Seldon Core]] — Plateforme de serving et d'orchestration d'inférence sur Kubernetes — graphes d'inférence multi-étapes, explicabilité et monitoring ; passée en licence source-available (BSL) depuis 2024.
- [[TensorFlow Serving]] — Serveur d'inférence haute performance pour modèles TensorFlow/Keras — API REST et gRPC, versionnage et batching de modèles, cœur C++ éprouvé ; intégré à TFX.
- [[Ray Serve]] — Bibliothèque de serving scalable bâtie sur Ray : déploiements Python framework-agnostiques, composition multi-modèles (deployment graphs) et autoscaling, du prototype au cluster.

## Ressources

- Documentation — https://docs.pytorch.org/serve/
- Dépôt — https://github.com/pytorch/serve

## Voir aussi

- [[Déploiement de modèles]] — la notion du dossier
- [[Comparatif - Serving de modèles]] — ce qui départage les serveurs du dossier
- [[PyTorch]] — le framework dont il servait les modèles
