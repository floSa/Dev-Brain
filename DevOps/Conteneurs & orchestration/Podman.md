---
role: brique
nom: Podman
alias: [podman, podman desktop, quadlet]
pitch: "Moteur de conteneurs sans démon et rootless par défaut (Apache-2.0, Go), compatible OCI et API Docker — `podman compose` exécute un `compose.yaml`."
categorie: devops/conteneur
famille: cli
licence_type: open-source
maturite: production
langage: Go
alternatives: ["[[Docker]]"]
complements: ["[[Docker Compose]]", "[[Trivy]]", "[[Grype]]"]
tags: [container, self-hosted]
url_docs: https://podman.io/docs
url_repo: https://github.com/containers/podman
---

# Podman

<!-- AUTO:BANDEAU:START -->
> Moteur de conteneurs sans démon et rootless par défaut (Apache-2.0, Go), compatible OCI et API Docker — `podman compose` exécute un `compose.yaml`.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Go | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Moteur de conteneurs qui exécute des images OCI **sans démon central** : chaque conteneur est
un processus fils de la commande qui l'a lancé, en `fork/exec`, et le mode **rootless** — un
utilisateur ordinaire, sans droits root — est le cas nominal. La CLI reprend celle de Docker
(`podman run`, `podman build`, souvent en alias) et un socket compatible avec l'API Docker
permet de brancher les clients qui la parlent. Il gère aussi des **pods**, à la manière de
Kubernetes, et lit du YAML Kubernetes (`podman kube play`). Sa voie de déploiement on-prem la
plus singulière est **Quadlet** : des fichiers `.container`, `.pod` ou `.kube` que systemd
transforme en services. Relevé le 2026-09-30 : **v6.1.3** (2026-09-29), environ 33 000
étoiles, quatre versions majeures ou mineures par an et un correctif toutes les deux à trois
semaines. Soutenu par Red Hat ; Podman, Buildah et Skopeo forment le projet « Podman Container
Tools », au niveau Sandbox de la CNCF depuis le 2025-01-21.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un serveur Linux RHEL, Fedora ou Debian où faire tourner des services sans démon root : le conteneur s'évanouit avec le compte qui le porte | Un poste macOS ou Windows sans Linux dessous : Podman y fonctionne dans une VM (`podman machine`), comme Docker Desktop — l'avantage du rootless disparaît |
| Des services pilotés par systemd, avec redémarrage, journal et dépendances, sans orchestrateur : Quadlet | Une chaîne d'outils qui suppose un vrai démon Docker : la compatibilité passe par le socket et reste partielle |
| Éviter la licence de Docker Desktop en entreprise : Podman et Podman Desktop sont sous Apache-2.0, sans palier payant affiché | Des fichiers Compose complexes à faire tourner sans surprise : `podman compose` n'est qu'un enrobage, qui délègue à `docker-compose` ou à `podman-compose`, un projet à part |
| Une isolation plus stricte que le démon root de Docker, sans changer d'images ni de Dockerfile | Des volumes sur NFS ou sur un système de fichiers parallèle en rootless : les conflits d'identifiants d'utilisateur les font échouer |

## Mise en œuvre

- Installation — `sudo dnf install podman` (Fedora, RHEL) ou `sudo apt-get install podman` (Debian 11 et plus, Ubuntu 20.10 et plus) ; macOS et Windows via l'installeur officiel puis `podman machine init` et `podman machine start`
- Point d'entrée — la CLI `podman` ; des fichiers Quadlet dans `/etc/containers/systemd/` (root) ou `~/.config/containers/systemd/` (rootless) ; `podman kube play` pour du YAML Kubernetes
- Prérequis — plages `subuid` et `subgid` dans `/etc/subuid` et `/etc/subgid` en rootless ; overlayfs natif demande Linux 5.12 ou plus, sinon `fuse-overlayfs`, plus lent ; les limites de ressources ne s'appliquent pas en cgroups v1
- Exécution — sur une machine, sans démon ; les ports inférieurs à 1024 exigent le paramètre `net.ipv4.ip_unprivileged_port_start` ou une redirection ; le réseau rootless passe par **pasta** depuis la 5.0, et l'adresse source d'un client n'est pas préservée par le proxy de ports
- Coût — gratuit sous Apache-2.0 ; Podman Desktop, aussi Apache-2.0 (environ 8 000 étoiles, v1.29.3), n'affiche pas de restriction d'usage — aucun texte n'écrit toutefois « gratuit en entreprise »

## Limites à connaître

- **Le compose de Podman est un aiguillage.** `podman compose` cherche d'abord `docker-compose`, puis `podman-compose`, et un avertissement s'affiche à chaque appel. `podman-compose` est un projet distinct, sous **GPL-2.0** (environ 6 200 étoiles) : licence à lire avant de l'embarquer dans un produit livré.
- **GPU NVIDIA par CDI.** La directive Quadlet `AddDevice=nvidia.com/gpu=all` expose les GPU ; ce n'est pas la syntaxe Compose de Docker.
- **Correctif de sécurité récent à connaître.** La v6.1.3 corrige la CVE-2026-94603 (relevée telle quelle sur la page de la release) : `podman run` sur une *image de checkpoint* pouvait désactiver tout le cloisonnement. Le support de ces images dans `podman run` est retiré.
- **Le statut CNCF est celui d'un lot.** La CNCF liste « Podman Container Tools » (Podman, Buildah, Skopeo) au niveau Sandbox ; le statut propre à Podman Desktop n'a pas été trouvé.

## Écosystème

### Alternatives

- [[Docker]] — Conteneurisation standard : packaging d'applications en images OCI reproductibles, isolées et portables d'un environnement à l'autre. — démon root par défaut, Desktop payant au-delà de 250 salariés, écosystème d'outils le plus large.

### Compléments

- [[Docker Compose]] — Décrit une pile multi-conteneurs dans un fichier compose.yaml et la lance d'une commande (Apache-2.0, Go) — sur un seul hôte : ni multi-nœuds, ni autoscaling. — le format que `podman compose` exécute
- [[Trivy]] — Scanner tout-en-un d'Aqua Security (Apache-2.0, Go) : vulnérabilités, secrets, configurations IaC et licences d'une image, d'un dépôt, d'un système de fichiers ou d'un SBOM, avec génération CycloneDX et SPDX et une base miroitable hors ligne — mais sa release, ses actions GitHub et ses images Docker Hub ont été compromises du 2026-03-19 au 2026-03-23 (versions sûres publiées). — une image Podman locale (≥ 2.0) se scanne directement ; le Podman distant n'est pas pris en charge.
- [[Grype]] — Scanner de vulnérabilités d'Anchore (Apache-2.0, Go) pour images, répertoires et SBOM — il lit un SBOM produit par Syft et le compare à une base quotidienne de 18 sources, importable à la main pour un site isolé ; il ne cherche ni secrets ni configurations, et refuse de scanner avec une base de plus de 5 jours. — `--from podman` lit une image Podman locale.

## Ressources

- Documentation — https://podman.io/docs
- Dépôt — https://github.com/containers/podman
- Documentation — Quadlet et les unités systemd : https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html
- Documentation — les limites du rootless : https://github.com/containers/podman/blob/main/rootless.md
- Documentation — installer Podman : https://podman.io/docs/installation
- Dépôt — Podman Desktop : https://github.com/podman-desktop/podman-desktop

## Voir aussi

- [[Conteneurs & orchestration]] — le hub du sous-domaine
- [[Comparatif - Orchestration de conteneurs]] — ce qui départage les moteurs, la pile locale et les orchestrateurs du dossier
- [[Du Compose à Kubernetes — quand changer d'échelle]] — la notion : ce que Compose ne fait pas, ce que coûte un cluster, le critère de bascule et le GitOps
