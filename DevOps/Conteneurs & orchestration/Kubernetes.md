---
role: brique
nom: Kubernetes
alias: [k8s, kube, kubernetes]
pitch: "Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter."
categorie: devops/conteneur
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Go
scaling: distributed
alternatives: ["[[k3s]]", "[[Docker Compose]]"]
complements: ["[[Helm]]", "[[Argo CD]]", "[[KServe]]", "[[Seldon Core]]", "[[Ray Serve]]", "[[BentoML]]"]
tags: [container, kubernetes, self-hosted]
url_docs: https://kubernetes.io/docs/
url_repo: https://github.com/kubernetes/kubernetes
---

# Kubernetes

<!-- AUTO:BANDEAU:START -->
> Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé ou managé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Orchestrateur de conteneurs : on déclare l'état voulu d'une application — combien de copies,
quelle image, quelles ressources — et un **plan de contrôle** s'emploie à le maintenir sur un
parc de machines. Il se compose d'un serveur d'API (`kube-apiserver`), d'une base clé-valeur
(`etcd`), d'un ordonnanceur (`kube-scheduler`) et de contrôleurs ; chaque nœud porte un
`kubelet` et un moteur de conteneurs. La doc officielle liste ce qu'il apporte : découverte de
services et équilibrage de charge, déploiements et retours arrière progressifs, placement
automatique, auto-réparation, gestion des secrets et de la configuration, mise à l'échelle
horizontale. Elle dit aussi ce qu'il n'est **pas** : ni middleware, ni base de données, ni CI/CD,
et il n'impose ni journalisation, ni supervision, ni alerte. Relevé le 2026-09-30 : version
**1.37** (2026-08-26, patch 1.37.1 en septembre), environ 128 100 étoiles, Apache-2.0 ; projet
CNCF diplômé (graduated) le 2018-03-06.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Plusieurs équipes ou plusieurs dizaines de services à déployer, avec des règles d'accès (RBAC), des quotas et des espaces de noms séparés | Personne pour opérer un plan de contrôle : mises à jour mineures obligatoires environ une fois par an, sauvegardes d'etcd, certificats |
| Un service qui doit survivre à la panne d'une machine : replacement automatique, déploiement sans coupure, retour arrière | Une pile qui tient sur une seule machine : le coût d'exploitation dépasse ce que le cluster apporte |
| Une mise à l'échelle selon la charge : `HorizontalPodAutoscaler`, GPU alloués dynamiquement (DRA, disponible depuis la 1.34) | Un besoin de réseau, de stockage persistant, d'ingress et d'équilibreur de charge « clés en main » : rien de cela n'est fourni, tout se choisit (Calico, Cilium, MetalLB, une classe de stockage CSI) |
| Déployer des outils qui n'existent que pour Kubernetes : opérateurs, serving de modèles comme [[KServe]], GitOps avec [[Argo CD]] | Une équipe qui n'a pas de temps pour la courbe d'apprentissage : la CNCF cite la formation (36 %) et la sécurité (36 %) parmi les défis |

## Mise en œuvre

- Installation — `kubeadm`, `kops` ou `kubespray` en on-prem ; distributions prêtes à l'emploi : [[k3s]], RKE2 (Apache-2.0), Talos Linux (MPL-2.0), MicroK8s (Apache-2.0), OKD (Apache-2.0) ; ou service managé chez un fournisseur cloud
- Point d'entrée — `kubectl` et des manifestes YAML ; [[Helm]] pour les paquets ; [[Argo CD]] pour le pilotage par Git
- Prérequis — pour un plan de contrôle en haute disponibilité : au moins **3 nœuds** de contrôle (nombre impair, à cause du consensus Raft d'etcd), et un équilibreur de charge TCP devant `kube-apiserver` (port 6443). L'etcd peut vivre sur ces mêmes nœuds (« empilé ») ou sur trois machines de plus (externe). Un CNI, un ingress, une solution de stockage et, sans cloud, un équilibreur comme MetalLB sont à installer
- Exécution — trois versions par an, trois branches maintenues en parallèle ; environ **14 mois** de correctifs (12 mois, puis 2 mois de maintenance) ; la politique de compatibilité interdit de sauter une version mineure, donc une ou deux montées séquentielles par an. Fin de support : 1.34 le 2026-10-27, 1.37 le 2027-10-28
- Coût — gratuit sous Apache-2.0 ; le coût est le temps d'exploitation, pas la licence. Les éditions commerciales (OpenShift) et les offres managées sont hors périmètre de cette fiche

## Limites à connaître

- **L'ingress historique est en fin de vie.** Le projet Ingress NGINX a annoncé le 2025-11-11 l'arrêt de sa maintenance : effort au mieux jusqu'en mars 2026, puis plus aucune version ni correctif de sécurité, alors que la communauté le disait utilisé par environ la moitié des environnements. L'API `Ingress` est gelée ; **Gateway API** est la voie recommandée, avec l'outil Ingress2Gateway pour migrer. Un nouveau déploiement ne s'appuie plus sur Ingress NGINX.
- **Ce que disent les enquêtes, avec leur biais.** L'enquête annuelle de la CNCF (publiée le 2026-01-20, 628 répondants selon la presse) donne 82 % d'utilisation de Kubernetes en production, contre 66 % en 2023 — mais la base est celle des **utilisateurs de conteneurs**, pas de toutes les organisations. Défis cités : changements culturels côté équipes 47 %, formation 36 %, sécurité 36 %, complexité 34 %. La taille des organisations n'est pas ventilée sur la page lue.
- **Une critique venue de l'usage réel.** Gitpod, après six ans, a quitté Kubernetes pour ses environnements de développement (latence d'ordonnancement, volumes persistants lents, modèle de permissions inadapté) tout en écrivant que Kubernetes reste « un bon choix » pour des charges applicatives. Le retour vaut pour une charge atypique, pas comme verdict général.
- **Aucun seuil officiel d'équipe minimale.** La documentation de production demande de planifier disponibilité, quotas, sauvegardes et RBAC, et propose une offre managée quand l'auto-gestion n'est pas envisageable. Aucune taille d'équipe n'est écrite nulle part dans les pages lues.

## Écosystème

### Alternatives

- [[k3s]] — Distribution Kubernetes certifiée en un binaire de moins de 100 Mo (Apache-2.0, Go, SUSE) — Traefik, CoreDNS et stockage local livrés, SQLite ou etcd embarqué, air-gap pris en charge ; le chemin le plus court vers Kubernetes on-prem. — c'est Kubernetes, allégé : même API, moins de choix à faire.
- [[Docker Compose]] — Décrit une pile multi-conteneurs dans un fichier compose.yaml et la lance d'une commande (Apache-2.0, Go) — sur un seul hôte : ni multi-nœuds, ni autoscaling. — ce qui reste tant que tout tient sur une machine.

### Compléments

- [[Helm]] — Gestionnaire de paquets de Kubernetes : un chart décrit, versionne et installe un ensemble de ressources (Apache-2.0, Go, CNCF diplômé). — l'installation de l'écosystème, comme le prend chaque outil de cette liste
- [[Argo CD]] — Contrôleur GitOps pour Kubernetes : compare en continu un dépôt Git à l'état du cluster et le réconcilie (Apache-2.0, Go, CNCF diplômé). — le pilotage des déploiements par Git
- [[KServe]] — Plateforme d'inférence standard sur Kubernetes (CNCF) — déploiement déclaratif via la CRD InferenceService, autoscaling serverless jusqu'à zéro (Knative), multi-framework, prédictif et génératif. — nécessite un cluster
- [[Seldon Core]] — Plateforme de serving et d'orchestration d'inférence sur Kubernetes — graphes d'inférence multi-étapes, explicabilité et monitoring ; passée en licence source-available (BSL) depuis 2024. — nécessite un cluster ; licence à lire
- [[Ray Serve]] — Bibliothèque de serving scalable bâtie sur Ray : déploiements Python framework-agnostiques, composition multi-modèles (deployment graphs) et autoscaling, du prototype au cluster. — se déploie sur Kubernetes par KubeRay
- [[BentoML]] — Framework Python de packaging et de service de modèles — transforme n'importe quel modèle (ML, LLM, pipelines multi-modèles) en API d'inférence, du prototype au déploiement scalable (BentoCloud / Kubernetes). — l'image se déploie sur Kubernetes

## Ressources

- Documentation — https://kubernetes.io/docs/
- Dépôt — https://github.com/kubernetes/kubernetes
- Documentation — ce que Kubernetes est et n'est pas : https://kubernetes.io/docs/concepts/overview/
- Documentation — cycle de vie des versions : https://kubernetes.io/releases/
- Documentation — plan de contrôle en haute disponibilité avec kubeadm : https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/high-availability/
- Article — la retraite d'Ingress NGINX : https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/
- Article — l'enquête annuelle 2025 de la CNCF : https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/
- Article — Gitpod quitte Kubernetes : https://ona.com/stories/we-are-leaving-kubernetes

## Voir aussi

- [[Conteneurs & orchestration]] — le hub du sous-domaine
- [[Comparatif - Orchestration de conteneurs]] — ce qui départage les moteurs, la pile locale et les orchestrateurs du dossier
- [[Du Compose à Kubernetes — quand changer d'échelle]] — la notion : ce que Compose ne fait pas, ce que coûte un cluster, le critère de bascule et le GitOps
