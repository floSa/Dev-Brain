---
role: brique
nom: KServe
alias: [kserve, kfserving]
pitch: "Plateforme d'inférence standard sur Kubernetes (CNCF) — déploiement déclaratif via la CRD InferenceService, autoscaling serverless jusqu'à zéro (Knative), multi-framework, prédictif et génératif."
categorie: ml/serving
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Go
scaling: distributed
alternatives: ["[[BentoML]]", "[[NVIDIA Triton]]", "[[Seldon Core]]", "[[TorchServe]]", "[[TensorFlow Serving]]", "[[Ray Serve]]"]
complements: ["[[Kubernetes]]"]
tags: [model-serving, inference, kubernetes]
url_docs: https://kserve.github.io/website/
url_repo: https://github.com/kserve/kserve
---

# KServe

<!-- AUTO:BANDEAU:START -->
> Plateforme d'inférence standard sur Kubernetes (CNCF) — déploiement déclaratif via la CRD InferenceService, autoscaling serverless jusqu'à zéro (Knative), multi-framework, prédictif et génératif.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé · distribué | production | à jour · 2026-08-06 |
<!-- AUTO:BANDEAU:END -->

## Définition

Couche d'inférence native Kubernetes : le déploiement d'un modèle se décrit dans une ressource
déclarative **`InferenceService`**, et l'opérateur gère serveur, routes, autoscaling et
rollout. L'intégration **Knative** apporte l'autoscaling au trafic, le **scale-to-zero** — pas
de coût quand aucune requête n'arrive — et les déploiements canary. Multi-framework
(scikit-learn, PyTorch, TensorFlow, XGBoost, ONNX, Triton), et désormais serving génératif.
Né en 2019 comme KFServing sous Kubeflow, sorti de Kubeflow et renommé KServe en 2022, projet CNCF en incubation
(accepté le 29 septembre 2025, annonce le 11 novembre) — gouvernance neutre. Il reste livré en
add-on dans les manifests de la distribution Kubeflow (v0.20.0 sur la branche master des manifests, Kubeflow devenu projet CNCF gradué en juillet 2026),
mais la doc Kubeflow le classe dans l'écosystème, pas parmi ses sous-projets. Version constatée
le 2026-09-30 : v0.21.0 du 2026-09-25, 6 053 étoiles, Apache-2.0, commits quotidiens.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Déjà sur Kubernetes : les modèles se déploient et se versionnent comme le reste de l'infra (GitOps, CRD) | Knative et une couche réseau (Istio…) sont à opérer en plus : la courbe d'apprentissage est celle de Kubernetes, pas celle de KServe |
| Charge variable ou sporadique : le scale-to-zero ne fait payer le GPU que sous trafic | Le scale-from-zero ajoute une latence de démarrage à froid, critique sur un gros modèle GPU |
| Parc multi-framework à standardiser derrière une abstraction commune | Deux modes de déploiement, Standard et Knative/Serverless dans la terminologie actuelle de la doc (l'ancien nom RawDeployment n'y figure plus dans l'aperçu d'administration), aux comportements différents : à choisir tôt. Le canary par `canaryTrafficPercent` n'est documenté qu'en mode Knative/Serverless |
| Rollouts progressifs en canary, transformers et explainers branchés dans le graphe de service | Détection de dérive par Alibi Detect : l'exemple officiel (CIFAR-10, journalisation de charge vers Knative Eventing) dépend d'une bibliothèque passée sous BSL 1.1 ; pour un service on-prem, préférer un contrôle de dérive à côté du serving ([[Comparatif - Monitoring de modèles]]) |

## Mise en œuvre

- Installation — manifests ou Helm sur un cluster Kubernetes, avec Knative et une gateway (Istio) en mode Serverless
- Point d'entrée — la CRD `InferenceService`, déclarée en YAML
- Prérequis — un cluster Kubernetes déjà opéré ; Knative et sa couche réseau pour le mode Serverless
- Exécution — sur le cluster, autoscaling au trafic et scale-to-zero par Knative ; managé indirectement par les distributions K8s/ML des cloud providers
- Coût — Apache-2.0, aucune offre SaaS propre ; le coût est celui du cluster, et il tombe à zéro hors trafic

## Écosystème

### Alternatives

- [[BentoML]] — Framework Python de packaging et de service de modèles — transforme n'importe quel modèle (ML, LLM, pipelines multi-modèles) en API d'inférence, du prototype au déploiement scalable (BentoCloud / Kubernetes).
- [[NVIDIA Triton]] — Serveur d'inférence multi-framework de NVIDIA (TensorRT, PyTorch, ONNX, TensorFlow…) — batching dynamique et exécution concurrente sur GPU/CPU, optimisé débit/latence ; intégré à la plateforme Dynamo.
- [[Seldon Core]] — Plateforme de serving et d'orchestration d'inférence sur Kubernetes — graphes d'inférence multi-étapes, explicabilité et monitoring ; passée en licence source-available (BSL) depuis 2024.
- [[TorchServe]] — Serveur de modèles PyTorch (handlers Python, frontend Java) — packaging .mar, batching et versionnage ; projet archivé et non maintenu depuis août 2025.
- [[TensorFlow Serving]] — Serveur d'inférence haute performance pour modèles TensorFlow/Keras — API REST et gRPC, versionnage et batching de modèles, cœur C++ éprouvé ; intégré à TFX.
- [[Ray Serve]] — Bibliothèque de serving scalable bâtie sur Ray : déploiements Python framework-agnostiques, composition multi-modèles (deployment graphs) et autoscaling, du prototype au cluster.

### Compléments

- [[Kubernetes]] — Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter. — l'environnement sur lequel il repose : un cluster est obligatoire.

## Ressources

- Documentation — https://kserve.github.io/website/
- Dépôt — https://github.com/kserve/kserve

## Voir aussi

- [[Déploiement de modèles]] — la notion du dossier
- [[Comparatif - Serving de modèles]] — ce qui départage les serveurs du dossier
- [[Docker]] — les images de modèles que le cluster exécute
