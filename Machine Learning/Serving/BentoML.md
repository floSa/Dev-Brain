---
role: brique
nom: BentoML
alias: [bentoml, bento]
pitch: "Framework Python de packaging et de service de modèles — transforme n'importe quel modèle (ML, LLM, pipelines multi-modèles) en API d'inférence, du prototype au déploiement scalable (BentoCloud / Kubernetes)."
categorie: ml/serving
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[NVIDIA Triton]]", "[[KServe]]", "[[Seldon Core]]", "[[TorchServe]]", "[[TensorFlow Serving]]", "[[Ray Serve]]"]
complements: []
tags: [model-serving, inference]
url_docs: https://docs.bentoml.com/
url_repo: https://github.com/bentoml/BentoML
---

# BentoML

<!-- AUTO:BANDEAU:START -->
> Framework Python de packaging et de service de modèles — transforme n'importe quel modèle (ML, LLM, pipelines multi-modèles) en API d'inférence, du prototype au déploiement scalable (BentoCloud / Kubernetes).

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme Python | open-source | self-hébergé ou managé · distribué | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Empaquette un modèle entraîné en service d'inférence. Une classe `Service` déclare les
dépendances, le code de pré/post-traitement et les endpoints ; l'outil en construit un
**Bento**, artefact versionné qui fige modèle, code et environnement, prêt à conteneuriser.
Agnostique au framework (scikit-learn, PyTorch, transformers, ONNX, modèles custom) et pensé
du prototype local au cluster, avec un volet LLM — serving haut débit, files de jobs,
pipelines multi-modèles. Tout s'écrit en Python de bout en bout : c'est ce qui rend la
logique métier autour de l'inférence libre, et ce qui prive le serveur du batching GPU fin.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Exposer un modèle Python comme API d'inférence sans écrire le serveur HTTP à la main | L'image d'un Bento devient lourde — modèle plus dépendances : le `python` et les exclusions sont à soigner |
| Figer modèle, code et dépendances dans un artefact conteneurisable | API remaniée en profondeur en 1.2+ : les tutoriels antérieurs ne s'appliquent plus |
| Pipelines multi-modèles, ou logique métier riche autour de l'inférence | |
| Aller du notebook au déploiement scalable, éventuellement managé | |

## Mise en œuvre

- Installation — `uv add bentoml`
- Point d'entrée — une classe `Service` en Python ; serveur local en une commande, puis build d'un Bento et image OCI
- Prérequis — Python ; Docker pour conteneuriser le Bento
- Exécution — conteneur sur n'importe quel runtime (Docker, Kubernetes) ; réplicas côté orchestrateur, ou BentoCloud
- Coût — Apache-2.0 pour le serveur ; BentoCloud, l'offre managée avec autoscaling et scale-to-zero, est payante

## Écosystème

### Alternatives

- [[NVIDIA Triton]] — Serveur d'inférence multi-framework de NVIDIA (TensorRT, PyTorch, ONNX, TensorFlow…) — batching dynamique et exécution concurrente sur GPU/CPU, optimisé débit/latence ; intégré à la plateforme Dynamo.
- [[KServe]] — Plateforme d'inférence standard sur Kubernetes (CNCF) — déploiement déclaratif via la CRD InferenceService, autoscaling serverless jusqu'à zéro (Knative), multi-framework, prédictif et génératif.
- [[Seldon Core]] — Plateforme de serving et d'orchestration d'inférence sur Kubernetes — graphes d'inférence multi-étapes, explicabilité et monitoring ; passée en licence source-available (BSL) depuis 2024.
- [[TorchServe]] — Serveur de modèles PyTorch (handlers Python, frontend Java) — packaging .mar, batching et versionnage ; projet archivé et non maintenu depuis août 2025.
- [[TensorFlow Serving]] — Serveur d'inférence haute performance pour modèles TensorFlow/Keras — API REST et gRPC, versionnage et batching de modèles, cœur C++ éprouvé ; intégré à TFX.
- [[Ray Serve]] — Bibliothèque de serving scalable bâtie sur Ray : déploiements Python framework-agnostiques, composition multi-modèles (deployment graphs) et autoscaling, du prototype au cluster.

## Ressources

- Documentation — https://docs.bentoml.com/
- Dépôt — https://github.com/bentoml/BentoML

## Voir aussi

- [[Déploiement de modèles]] — la notion du dossier
- [[Comparatif - Serving de modèles]] — ce qui départage les serveurs du dossier
- [[PyTorch]], [[Scikit-Learn]], [[HuggingFace]] — les frameworks dont il empaquette les modèles
