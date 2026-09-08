---
role: brique
nom: Docker
alias: [docker]
pitch: "Conteneurisation standard : packaging d'applications en images OCI reproductibles, isolées et portables d'un environnement à l'autre."
categorie: devops/conteneur
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Go
scaling: single-node
alternatives: []
complements: ["[[GitHub Actions]]"]
tags: [container]
url_docs: https://docs.docker.com/
url_repo: https://github.com/moby/moby
---

# Docker

<!-- AUTO:BANDEAU:START -->
> Conteneurisation standard : packaging d'applications en images OCI reproductibles, isolées et portables d'un environnement à l'autre.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé · mono-nœud | production | à jour · 2026-09-03 |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil de conteneurisation de référence. Une application et ses dépendances sont figées
dans une **image** au format OCI, construite depuis un `Dockerfile`, puis exécutée comme
**conteneur** isolé par les primitives du noyau Linux — namespaces, cgroups. L'image est
reproductible et portable : la même tourne du poste de dev à la CI puis en production.
C'est le socle du packaging moderne — un service, un modèle, une base éphémère de test se
livrent en conteneur. Deux faits qui ne sont pas des nuances. Un conteneur n'est **pas**
une machine virtuelle : le noyau est partagé avec l'hôte, et l'isolation s'arrête là. Et
le **moteur** (Docker Engine, issu du projet Moby) et l'**application de bureau** (Docker
Desktop) ne relèvent pas du même régime contractuel — la confusion entre les deux est
l'erreur la plus coûteuse du sujet.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Packager une application ou un service avec ses dépendances, pour un déploiement reproductible | Isolation plus forte que le partage de noyau, multi-tenant hostile : il faut une VM ou une micro-VM (Firecracker, hors brain) |
| Lancer des dépendances jetables en local et en CI — Postgres, MinIO, Redis — sans les installer sur l'hôte | Orchestration multi-nœuds — mise à l'échelle, self-healing, rollout : Docker seul ne suffit pas, c'est Kubernetes ou Swarm (hors brain) |
| Standardiser l'environnement entre dev, CI et production | Poste de travail en entreprise où la licence Docker Desktop est exclue : c'est **Desktop** qui est soumis à abonnement, pas le moteur — sur serveur Linux on installe l'Engine, ou une alternative type Podman (hors brain) |
| Servir de base à une chaîne CI/CD et à un déploiement orchestré : Kubernetes consomme des images OCI | |

## Mise en œuvre

- Installation — Docker Engine par paquet système sur Linux ; Docker Desktop sur macOS et Windows
- Point d'entrée — CLI `docker` et `docker compose` ; un `Dockerfile` par image, un `compose.yaml` par pile locale
- Prérequis — un noyau Linux (namespaces, cgroups) ; sur macOS et Windows, Desktop en fournit un dans une VM. Aucun credential dans un `Dockerfile` ni dans une couche d'image : build secrets, ou variables au runtime
- Exécution — auto-hébergé, mono-nœud ; le multi-nœuds relève d'un orchestrateur. Images minces à soigner — image de base réduite, ordre des couches pensé pour le cache, multi-stage build, sans quoi elles gonflent vite
- Coût — Docker Engine gratuit sous Apache 2.0 ; Docker Desktop impose un abonnement payant pour l'usage commercial au-delà de 250 employés ou 10 M$ de chiffre d'affaires, gratuit en deçà et pour l'usage personnel ; Docker Hub gratuit avec quotas de pull, payant au-delà

## Écosystème

### Alternatives

- *Aucune alternative déclarée : seule page de la catégorie `devops/conteneur`. Podman serait le candidat naturel — compatible OCI, sans démon, rootless — mais il n'est pas encore fiché.*

### Compléments

- [[GitHub Actions]] — CI/CD intégrée à GitHub : workflows YAML déclenchés sur événements du dépôt, runners hébergés ou auto-hébergés, large marketplace d'actions. — la CI qui construit et publie les images

## Ressources

- Documentation — https://docs.docker.com/
- Dépôt — https://github.com/moby/moby

## Voir aussi

- [[DevOps]] — le hub du domaine
