---
galaxie: dev
type: service
nom: Docker
alias: [docker]
pitch: "Conteneurisation standard : packaging d'applications en images OCI reproductibles, isolées et portables d'un environnement à l'autre."
categorie: devops/container
licence_type: open-source
hosted: self
maturite: production
langage: Go
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [container]
url_docs: https://docs.docker.com/
url_repo: https://github.com/moby/moby
---

# Docker

## Pourquoi

Outil de **conteneurisation** de référence. Une application et ses dépendances sont figées dans une **image** (format OCI) construite depuis un `Dockerfile`, puis exécutée comme **conteneur** isolé via les primitives du noyau Linux (namespaces, cgroups). L'image est reproductible et portable : la même tourne du poste de dev à la CI à la prod. C'est le socle du packaging moderne — un service, un modèle ML, une base éphémère de test se livrent en conteneur.

## Quand l'utiliser

- Packager une appli/un service avec ses dépendances pour un déploiement reproductible.
- Lancer des dépendances jetables en local et en CI (Postgres, MinIO, Redis…) sans les installer sur l'hôte.
- Standardiser l'environnement entre dev, CI et prod (« ça marche sur ma machine » éliminé).
- Base d'une chaîne CI/CD (build d'image) et d'un déploiement orchestré (Kubernetes consomme des images OCI).

## Quand NE PAS l'utiliser

- Besoin d'isolation plus forte que le partage de noyau (multi-tenant hostile) → VM / micro-VM (Firecracker).
- Orchestration multi-nœuds (scaling, self-healing, rollout) → Docker seul ne suffit pas ; passer à Kubernetes (ou Swarm).
- Contexte interdisant la licence Docker Desktop en entreprise → moteur seul, ou alternative type Podman (hors brain pour l'instant).

## Déploiement & coût

- **Docker Engine** (le démon, via le projet open-source Moby) est sous **licence Apache 2.0**, gratuit, auto-hébergé.
- **Docker Desktop** (l'app poste de travail Mac/Windows) impose un **abonnement payant** pour un usage commercial dans les grandes structures (> 250 employés **ou** > 10 M$ de CA) ; gratuit pour l'usage personnel et les petites entités.
- Docker Hub (registre) : palier gratuit avec quotas de pull, offres payantes au-delà.

## Pièges

- Confusion Engine ↔ Desktop : c'est **Desktop** qui est soumis à licence en entreprise, pas le moteur Apache 2.0 — sur serveur Linux, on installe l'Engine, pas Desktop.
- Images qui gonflent : partir d'images de base minces, soigner l'ordre des couches et utiliser le multi-stage build pour le cache.
- Secrets en clair dans une image ou un `Dockerfile` : ne jamais y mettre de credentials (utiliser build secrets / variables au runtime).
- Conteneur ≠ machine virtuelle : noyau partagé avec l'hôte, l'isolation a ses limites.

## Alternatives

<!-- Pas d'autre outil de conteneurisation en brain (categorie devops/container). Podman serait l'alternative naturelle (compatible OCI, daemonless, rootless) mais n'est pas encore documenté ici. -->

## Liens

- [[Dev/Services/GitHub Actions|GitHub Actions]] — CI qui construit et publie des images Docker
- Doc : https://docs.docker.com/
