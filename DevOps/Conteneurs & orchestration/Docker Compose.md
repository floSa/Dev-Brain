---
role: brique
nom: Docker Compose
alias: [compose, docker-compose, docker compose, compose.yaml]
pitch: "Décrit une pile multi-conteneurs dans un fichier compose.yaml et la lance d'une commande (Apache-2.0, Go) — sur un seul hôte : ni multi-nœuds, ni autoscaling."
categorie: devops/conteneur
famille: cli
licence_type: open-source
maturite: production
langage: Go
alternatives: ["[[k3s]]", "[[Kubernetes]]"]
complements: ["[[Docker]]", "[[Podman]]"]
tags: [container]
url_docs: https://docs.docker.com/compose/
url_repo: https://github.com/docker/compose
---

# Docker Compose

<!-- AUTO:BANDEAU:START -->
> Décrit une pile multi-conteneurs dans un fichier compose.yaml et la lance d'une commande (Apache-2.0, Go) — sur un seul hôte : ni multi-nœuds, ni autoscaling.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Go | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil en ligne de commande qui décrit une application faite de plusieurs conteneurs — services,
réseaux, volumes, secrets — dans un seul fichier YAML, le `compose.yaml`, et la démarre par
`docker compose up`. Le format est la **Compose Specification**, maintenue dans un dépôt
distinct (`compose-spec`) et implémentée aussi par d'autres outils ; Docker Compose en est
l'implémentation de référence. Sur un serveur Linux, c'est un plugin du CLI `docker`, gratuit
et sous Apache-2.0. Relevé le 2026-09-30 : **v5.5.1** (2026-09-03), environ 38 300 étoiles. Le
numéro v5 (2025) a sauté v3 et v4 pour ne pas se confondre avec les versions du *format* de
fichier ; la doc le dit fonctionnellement identique à la v2. Compose v1, en Python, n'est plus
supporté depuis juin 2023.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Déployer une pile de services sur **une machine** : API, base, file de messages, proxy | Plusieurs machines pour une même application : Compose s'arrête à un hôte, la doc le cantonne au développement, aux tests et à la production mono-hôte |
| Reproduire la même pile en local, en CI et sur le serveur, à partir d'un seul fichier versionné | Bascule automatique quand un nœud tombe, mise à l'échelle selon la charge, déploiement sans coupure garanti : rien de cela n'est fourni |
| Enchaîner le démarrage sur l'état réel des services : `healthcheck` puis `depends_on` avec `condition: service_healthy`, `up --wait` | Les objets `deploy:` d'un orchestrateur (placement, répliques, mises à jour progressives) : la doc officielle ne dit pas lesquelles des clés `deploy:` sont honorées hors Swarm — à tester avant de s'y fier |
| Réserver un GPU NVIDIA à un service (`deploy.resources.reservations.devices`, ou `gpus: all`) | Un poste où l'on veut un outil sans démon : le plugin s'appuie sur un moteur qui expose l'API Docker (Docker Engine, ou le socket de Podman) |
| Itérer en développement : `docker compose watch` synchronise ou reconstruit à chaque modification du code | |

## Mise en œuvre

- Installation — paquet `docker-compose-plugin` depuis le dépôt apt ou yum de Docker (à configurer au préalable), ou binaire des releases GitHub posé dans `~/.docker/cli-plugins/` ; inclus dans Docker Desktop
- Point d'entrée — `compose.yaml` à la racine du projet ; `docker compose up -d`, `down`, `logs`, `ps`
- Prérequis — un moteur de conteneurs. Les secrets passent par la clé `secrets:` ou un fichier `.env` hors dépôt, jamais en clair dans le YAML versionné
- Exécution — un seul hôte : `restart: unless-stopped` relance après un crash ou un redémarrage de la machine, rien ne replace un service sur une autre machine. `profiles` sélectionnent des sous-ensembles de services
- Coût — gratuit sous Apache-2.0. Le client de bureau qui l'embarque, Docker Desktop, est soumis à abonnement au-delà de 250 salariés ou 10 M$ de chiffre d'affaires (cf. [[Docker]])

## Limites à connaître

- **Un seul hôte, sans autre mécanisme de reprise que `restart:`.** C'est la frontière que la documentation trace elle-même. Pour aller au-delà, la doc renvoie vers un `DOCKER_HOST` distant ou vers Swarm, dont le mode est intégré à l'Engine ; le README de Compose précise que Swarm n'a pas adopté la Compose Specification actuelle.
- **Nouveautés qui élargissent le périmètre sans changer la frontière.** Un niveau `models:` déclare des modèles d'IA à côté des services (Compose 2.38 et plus, plateforme compatible comme Docker Model Runner requise) ; `provider:` délègue le cycle de vie d'un service à un composant externe ; **Compose Bridge** génère des manifests Kubernetes et un overlay Kustomize depuis un `compose.yaml` — voie de sortie vers un cluster, à évaluer sur la pile réelle avant de la croire équivalente.
- **`watch` a des bornes.** Il ne concerne que les services qui ont une section `build`, ne connaît pas les motifs `glob`, et exige `stat`, `mkdir` et `rmdir` dans l'image.

## Écosystème

### Alternatives

- [[k3s]] — Distribution Kubernetes certifiée en un binaire de moins de 100 Mo (Apache-2.0, Go, SUSE) — Traefik, CoreDNS et stockage local livrés, SQLite ou etcd embarqué, air-gap pris en charge ; le chemin le plus court vers Kubernetes on-prem. — le pas suivant quand une seule machine ne suffit plus.
- [[Kubernetes]] — Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter. — l'orchestrateur complet, pour plusieurs équipes ou plusieurs dizaines de services.

### Compléments

- [[Docker]] — Conteneurisation standard : packaging d'applications en images OCI reproductibles, isolées et portables d'un environnement à l'autre. — le moteur que Compose pilote
- [[Podman]] — Moteur de conteneurs sans démon et rootless par défaut (Apache-2.0, Go), compatible OCI et API Docker — `podman compose` exécute un `compose.yaml`.

## Ressources

- Documentation — https://docs.docker.com/compose/
- Dépôt — https://github.com/docker/compose
- Documentation — la Compose Specification : https://github.com/compose-spec/compose-spec
- Documentation — Compose en production : https://docs.docker.com/compose/how-tos/production/
- Documentation — installer le plugin sous Linux : https://docs.docker.com/compose/install/linux/

## Voir aussi

- [[Conteneurs & orchestration]] — le hub du sous-domaine
- [[Comparatif - Orchestration de conteneurs]] — ce qui départage les moteurs, la pile locale et les orchestrateurs du dossier
- [[Du Compose à Kubernetes — quand changer d'échelle]] — la notion : ce que Compose ne fait pas, ce que coûte un cluster, le critère de bascule et le GitOps
