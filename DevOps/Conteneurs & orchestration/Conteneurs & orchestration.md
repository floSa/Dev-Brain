---
role: hub
nom: Conteneurs & orchestration
alias: [conteneurs, orchestration de conteneurs, containers]
pitch: Exécuter des applications en conteneurs, de la machine unique au cluster — le moteur, la pile locale, l'orchestrateur et l'outil qui installe dessus.
domaines: [mlops, infra-ops]
tags: [container, kubernetes]
---

# Conteneurs & orchestration

> Exécuter des applications en conteneurs, de la machine unique au cluster — le moteur, la pile locale, l'orchestrateur et l'outil qui installe dessus.

## Ce qu'il faut comprendre

- **Quatre niveaux, qu'on confond souvent.** Le **moteur** exécute une image ([[Docker]], [[Podman]]). La **pile d'une machine** assemble plusieurs conteneurs dans un fichier ([[Docker Compose]]). L'**orchestrateur** replace, met à l'échelle et met à jour sur plusieurs machines ([[Kubernetes]], [[k3s]]). L'**installateur** empaquette ce qu'on y déploie ([[Helm]]). Chaque niveau se choisit séparément, et le suivant ne remplace pas le précédent : Kubernetes exécute des images que Docker ou un autre outil a construites.
- **La frontière qui compte est « une machine ou plusieurs ».** Sur une machine, Compose tient un service en vie (`restart:`) et sait attendre qu'un autre soit sain ; il ne replace rien ailleurs quand la machine tombe. Au-delà, un orchestrateur devient la question — et son coût d'exploitation, pas sa licence, en est le prix.
- **k3s est Kubernetes, pas un concurrent de son API.** Même API, mêmes manifestes, mêmes charts ; la différence tient à ce qui est déjà choisi pour soi (réseau, ingress, stockage local, stockage du cluster) et à l'empreinte : un binaire, 2 Go de RAM. En on-prem isolé, c'est le chemin le plus court.
- **La licence à surveiller n'est pas celle du moteur.** Docker Engine et Podman sont en Apache-2.0. C'est **Docker Desktop**, le client de bureau, qui demande un abonnement au-delà de 250 salariés ou 10 M$ de chiffre d'affaires ; Podman Desktop n'affiche pas de restriction.
- **HashiCorp Nomad n'a pas de fiche.** Il est activement maintenu (v2.0.7, 2026-09-17) mais sous licence BSL 1.1, dont le titulaire est IBM depuis le rachat de HashiCorp, sans fork communautaire, et sa place dans les enquêtes est faible. Le motif est développé dans le comparatif du dossier.

## Choisir

- Une pile de services sur un serveur, un poste de développement, une CI → [[Docker Compose]] sur [[Docker]] ou [[Podman]].
- Un serveur Linux où tout doit repartir seul après un redémarrage, sans démon root → [[Podman]] et ses fichiers Quadlet.
- Plusieurs machines, une bascule si l'une tombe, des déploiements sans coupure, peu de monde pour l'opérer → [[k3s]].
- Plusieurs équipes, des dizaines de services, des règles d'accès fines → [[Kubernetes]].
- Installer un logiciel tiers sur un cluster, ou le décliner par environnement → [[Helm]] ; le piloter depuis Git → [[Argo CD]] (dossier parent).
- Servir un modèle sur un cluster → [[KServe]] ou [[Seldon Core]], dans « Machine Learning/Serving ».

<!-- AUTO:START -->
### Briques
- [[Docker]] — Conteneurisation standard : packaging d'applications en images OCI reproductibles, isolées et portables d'un environnement à l'autre.
- [[Docker Compose]] — Décrit une pile multi-conteneurs dans un fichier compose.yaml et la lance d'une commande (Apache-2.0, Go) — sur un seul hôte : ni multi-nœuds, ni autoscaling.
- [[Helm]] — Gestionnaire de paquets de Kubernetes : un chart décrit, versionne et installe un ensemble de ressources (Apache-2.0, Go, CNCF diplômé).
- [[k3s]] — Distribution Kubernetes certifiée en un binaire de moins de 100 Mo (Apache-2.0, Go, SUSE) — Traefik, CoreDNS et stockage local livrés, SQLite ou etcd embarqué, air-gap pris en charge ; le chemin le plus court vers Kubernetes on-prem.
- [[Kubernetes]] — Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter.
- [[Podman]] — Moteur de conteneurs sans démon et rootless par défaut (Apache-2.0, Go), compatible OCI et API Docker — `podman compose` exécute un `compose.yaml`.
<!-- AUTO:END -->
