---
role: brique
nom: Kubeflow
alias: [kubeflow, kubeflow platform, kubeflow pipelines]
pitch: "Boîte à outils ML open source sur Kubernetes (CNCF, gradué en 2026) — notebooks, pipelines sur Argo Workflows, entraînement distribué, optimisation d'hyperparamètres, registre et serving derrière un tableau de bord multi-utilisateurs ; se déploie composant par composant, l'installation complète est lourde à opérer."
categorie: ml/plateforme
famille: plateforme
domaines: [mlops, ml-eng]
licence_type: open-source
hosted: [self]
maturite: production
langage: Go, Python
scaling: distributed
alternatives: ["[[Flyte]]", "[[Metaflow]]", "[[ZenML]]"]
complements: ["[[Kubernetes]]", "[[KServe]]"]
tags: [ml-platform, ml-pipeline, kubernetes, hyperparameter-tuning, notebook, self-hosted]
url_docs: https://www.kubeflow.org/docs/
url_repo: https://github.com/kubeflow/manifests
---

# Kubeflow

<!-- AUTO:BANDEAU:START -->
> Boîte à outils ML open source sur Kubernetes (CNCF, gradué en 2026) — notebooks, pipelines sur Argo Workflows, entraînement distribué, optimisation d'hyperparamètres, registre et serving derrière un tableau de bord multi-utilisateurs ; se déploie composant par composant, l'installation complète est lourde à opérer.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go, Python | open-source | self-hébergé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Projet de la CNCF qui assemble, sur un cluster [[Kubernetes]], les étapes d'un cycle ML : notebooks,
pipelines, entraînement distribué, optimisation d'hyperparamètres, registre de modèles et serving,
derrière un **tableau de bord central** et des **profils** qui isolent les utilisateurs par
namespace. Ce n'est pas un produit unique mais une **distribution** de composants indépendants
(dépôt `kubeflow/manifests`) que chacun peut aussi installer seul. Le projet est entré à la CNCF
en juillet 2023 et y est devenu **gradué le 2026-07-24** (page projet CNCF). Il se classe parmi
les plateformes parce qu'il porte, à lui seul, calcul, pipelines, serving et droits. Mais,
contrairement à [[Dataiku]] ou à [[Databricks]], il ne se vend pas : on l'assemble, on l'exploite et
on le met à jour soi-même, ou on passe par une distribution tierce.

**Composants constatés le 2026-09-30** (versions lues dans les flux de releases) :

| Composant | Version | État |
|---|---|---|
| Pipelines | 2.17.2 (2026-09-04) | actif ; exécute sur Argo Workflows ; stockage des pipelines en CRD possible sans base externe ; 4 231 étoiles |
| Trainer | v2.3.0 (2026-08-07) | actif ; CRD `TrainJob`, JobSet requis ; successeur du Training Operator |
| Training Operator v1 | v1.9.4 (2026-08-18) | hérité, encore corrigé ; déprécié côté Kueue et OpenShift AI, aucune date de fin de support trouvée |
| Katib | v0.19.0 (2025-10-31) | maintenu à un rythme lent ; la doc d'installation pointe encore v0.17.0 |
| Notebooks | 1.11.0 (2026-06-04) | stable ; la version 2 (Workspaces) est en bêta, notes de release : pas de production |
| Hub (ex-Model Registry) | v0.3.17 (2026-09-21) | actif, avec un catalogue de modèles |
| KServe | v0.21.0 (2026-09-25) | **hors Kubeflow depuis 2022**, projet CNCF ; livré en add-on dans les manifests |

La distribution suit un versionnage calendaire : **26.03.1** est la dernière release (juin 2026),
avec deux versions par an annoncées et un support communautaire « au mieux » d'environ six mois.
Le dépôt `kubeflow/manifests` compte 1 042 étoiles.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Plusieurs équipes partagent **un cluster Kubernetes** déjà opéré et doivent être isolées (profils, namespaces, `AuthorizationPolicy`) sous un même tableau de bord | **Aucune équipe ne sait opérer Kubernetes** : Istio, Knative, cert-manager, Dex et oauth2-proxy font partie de l'installation, et les mises à jour demandent des étapes manuelles décrites dans le README |
| Le besoin couvre **plusieurs étapes** — notebooks, entraînement distribué, HPO, pipelines, serving — sur du matériel qu'on possède | Un pipeline seul suffit : [[Flyte]], [[Metaflow]] ou [[ZenML]] demandent bien moins, et ZenML ou Metaflow peuvent de toute façon s'appuyer sur Kubeflow comme orchestrateur |
| Un seul composant est utile : **Pipelines**, **Trainer** ou **Katib** s'installent seuls (Pipelines standalone, Trainer avec JobSet, Katib avec une `StorageClass`) | Les ressources sont comptées : le README chiffre l'installation complète à environ 4,4 cœurs, 12,3 Gio de RAM et 65 Go de volumes au repos, et recommande 16 Go et 8 cœurs ; Pipelines pèse à lui seul 35 Go de volumes |
| Un SSO d'entreprise à brancher : Dex (LDAP, OIDC, SAML, GitHub…) plus oauth2-proxy, documentés dans le dépôt de la distribution | L'air-gap sans outillage : possible, mais toutes les images sont à miroiter et à remplacer par des overlays kustomize |
| Un cadre neutre et auditable : CNCF gradué, comité de pilotage à cinq sièges individuels, Apache-2.0 | Un **existant v1** : le monorepo `kubeflow/kubeflow` s'est arrêté à la 1.10, le SDK Pipelines v1 est hérité, le stockage d'artefacts est passé de MinIO à SeaweedFS en 1.11 avec une migration manuelle, et la version 26.03 déplace KServe et le tableau de bord avec interruption du plan de contrôle |

Aucune comparaison **neutre** et récente avec les alternatives légères n'a été trouvée : celles qui circulent viennent d'éditeurs concurrents (Union.ai pour Flyte, ZenML). Ce que la documentation permet d'affirmer : Kubeflow s'installe composant par composant, donc la distribution complète n'est pas imposée.

## Mise en œuvre

- Installation — `kustomize build` du dépôt `kubeflow/manifests` dans une boucle avec reprise (le README prévient que le premier `apply` échoue souvent), composant par composant, ou distribution tierce ; des charts Helm existent, expérimentaux pour certains composants. Le mot de passe par défaut est à changer avant toute exposition ; distributions tierces : charmed Kubeflow de Canonical (Apache-2.0, installé par Juju, version 1.11 d'avril 2026, support sous abonnement par nœud) ; deployKF (Apache-2.0) est dormant depuis mai 2024
- Point d'entrée — le tableau de bord central derrière la passerelle Istio ; le SDK Python `kfp` pour Pipelines, la ressource `TrainJob` en YAML pour l'entraînement
- Prérequis — Kubernetes (la version supportée se lit dans les notes de chaque release, aucune matrice minimale n'est publiée pour 26.03.1), une `StorageClass` dynamique, HTTPS dès qu'on quitte `localhost`, Istio CNI (configuration spécifique sous Cilium)
- Exécution — sur le cluster, distribué ; l'accès externe passe par `istio-ingressgateway` exposé par un ingress, le README déconseille NodePort ; authentification : dex comme fournisseur OIDC et oauth2-proxy comme client de la passerelle ; [[Keycloak]] n'a qu'un guide « approximatif » dans le dépôt (Dex en connecteur OIDC vers Keycloak), aucune page sur kubeflow.org
- Coût — Apache-2.0, gratuit ; le coût réel est celui du cluster et du temps d'exploitation. L'enquête utilisateurs de 2023 (90 réponses) citait la documentation (55 %), l'installation et les mises à jour (39 % chacune) comme difficultés, et 45 % des répondants étaient en on-prem

## Écosystème

### Alternatives

- [[Flyte]] — Orchestrateur de workflows ML/data Kubernetes-natif (backend Go, SDK Python flytekit) : tâches fortement typées, conteneurisées et versionnées, isolation des ressources et cache d'exécution ; projet gradué LF AI & Data, édition entreprise Union.ai.
- [[Metaflow]] — Framework ML human-centric de Netflix (Python) : des flows à étapes qui s'exécutent en local puis scalent sans changer le code sur AWS Batch / Step Functions / Kubernetes ; versionnage, artefacts et reprise intégrés. Édition managée via Outerbounds.
- [[ZenML]] — Framework MLOps open-source (Python) qui découple le code des pipelines de l'infrastructure : un même pipeline tourne en local puis sur n'importe quel backend (Kubernetes, Airflow, cloud) via des stacks composables ; orchestre les outils MLOps existants derrière une abstraction unique.

### Compléments

- [[Kubernetes]] — Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter. — l'environnement obligatoire : Kubeflow n'existe pas hors d'un cluster.
- [[KServe]] — Plateforme d'inférence standard sur Kubernetes (CNCF) — déploiement déclaratif via la CRD InferenceService, autoscaling serverless jusqu'à zéro (Knative), multi-framework, prédictif et génératif. — le serving de Kubeflow depuis sa sortie du projet en 2022 : livré en add-on dans les manifests, installable sans Kubeflow.

## Ressources

- Documentation — https://www.kubeflow.org/docs/
- Dépôt — https://github.com/kubeflow/manifests
- Article — annonce de la graduation CNCF : https://www.cncf.io/announcements/2026/08/17/cncf-announces-kubeflows-graduation-solidifying-the-standard-for-cloud-native-ai-operations/
- Article — enquête utilisateurs 2023 : https://blog.kubeflow.org/kubeflow-user-survey-2023/

## Voir aussi

- [[Plateformes data & IA]] — le dossier ; Kubeflow y est l'exception open source, qui s'assemble au lieu de s'acheter
- [[Plateforme data & IA — concept]] — les quatre étages qu'une plateforme intègre
- [[Comparatif - Plateformes data & IA]] — ce qui le départage des huit suites commerciales
- [[Comparatif - Orchestrateurs ML]] — l'alternative légère : un pipeline sans la plateforme
- [[Du Compose à Kubernetes — quand changer d'échelle]] — quand un cluster se justifie avant d'y poser Kubeflow
- [[Model registry & versioning]] — la traçabilité que Kubeflow Hub et [[MLflow]] portent
- [[Déploiement de modèles]] — ce que KServe met en œuvre dans Kubeflow
