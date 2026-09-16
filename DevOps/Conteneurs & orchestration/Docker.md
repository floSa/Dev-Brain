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
alternatives: ["[[Podman]]"]
complements: ["[[Docker Compose]]", "[[GitHub Actions]]"]
tags: [container]
url_docs: https://docs.docker.com/
url_repo: https://github.com/moby/moby
---

# Docker

<!-- AUTO:BANDEAU:START -->
> Conteneurisation standard : packaging d'applications en images OCI reproductibles, isolées et portables d'un environnement à l'autre.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé · mono-nœud | production | amont non sondé |
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
l'erreur la plus coûteuse du sujet. Relevé le 2026-09-30 : Docker Engine **29.8.1**
(2026-09-15), environ 72 100 étoiles sur `moby/moby`, Apache-2.0 ; Docker Desktop **4.93.0**
(2026-09-28). Docker ne fournit pas de support commercial pour l'Engine, seulement pour Desktop
et les produits payants.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Packager une application ou un service avec ses dépendances, pour un déploiement reproductible | Isolation plus forte que le partage de noyau, multi-tenant hostile : il faut une VM ou une micro-VM (Firecracker, hors brain) |
| Lancer des dépendances jetables en local et en CI — Postgres, MinIO, Redis — sans les installer sur l'hôte | Orchestration multi-nœuds — mise à l'échelle, self-healing, rollout : l'Engine seul n'orchestre rien ; le mode Swarm intégré n'est pas déprécié mais le projet autonome Classic Swarm n'est plus développé (hors brain) |
| Standardiser l'environnement entre dev, CI et production | Poste de travail en entreprise où la licence Docker Desktop est exclue : c'est **Desktop** qui est soumis à abonnement, pas le moteur — sur serveur Linux on installe l'Engine, ou [[Podman]] |
| Servir de base à une chaîne CI/CD et à un déploiement orchestré : Kubernetes consomme des images OCI | |

## Mise en œuvre

- Installation — Docker Engine par paquet système sur Linux ; Docker Desktop sur macOS et Windows
- Point d'entrée — CLI `docker` et `docker compose` ; un `Dockerfile` par image, un `compose.yaml` par pile locale
- Prérequis — un noyau Linux (namespaces, cgroups) ; sur macOS et Windows, Desktop en fournit un dans une VM. Aucun credential dans un `Dockerfile` ni dans une couche d'image : build secrets, ou variables au runtime
- Exécution — auto-hébergé, mono-nœud ; le multi-nœuds relève d'un orchestrateur. Images minces à soigner — image de base réduite, ordre des couches pensé pour le cache, multi-stage build, sans quoi elles gonflent vite
- Coût — Docker Engine gratuit sous Apache-2.0. Docker Desktop, client de bureau sous licence propriétaire : abonnement obligatoire au-delà de 250 salariés **ou** 10 M$ de chiffre d'affaires, et pour les entités gouvernementales ; gratuit en deçà et pour l'usage personnel. Tarifs par utilisateur et par mois, relevés sur la page de prix : Pro 9 $ (annuel), Team 15 $, Business 24 $. Le texte du contrat d'abonnement n'a pas été ouvert : la règle vient de la page de licence de Desktop. Docker Hub — anonyme : 100 pulls par 6 h et par adresse IP ; compte gratuit : 200 pulls par 6 h ; offres payantes : illimité sous usage raisonnable. La page de tarifs dit « 100 pulls/heure » pour le compte gratuit : elle contredit la doc d'usage, retenue ici. Docker Hardened Images — socle d'images durcies gratuit sous Apache-2.0 ; offres Select (à partir de 5 k$ par dépôt) et Enterprise payantes

## Écosystème

### Alternatives

- [[Podman]] — Moteur de conteneurs sans démon et rootless par défaut (Apache-2.0, Go), compatible OCI et API Docker — `podman compose` exécute un `compose.yaml`. — l'alternative sans démon root ni licence de bureau à surveiller.

### Compléments

- [[Docker Compose]] — Décrit une pile multi-conteneurs dans un fichier compose.yaml et la lance d'une commande (Apache-2.0, Go) — sur un seul hôte : ni multi-nœuds, ni autoscaling. — la pile de services décrite dans un fichier, sur une machine
- [[GitHub Actions]] — CI/CD intégrée à GitHub : workflows YAML déclenchés sur événements du dépôt, runners hébergés ou auto-hébergés, large marketplace d'actions. — la CI qui construit et publie les images

## Ressources

- Documentation — https://docs.docker.com/
- Dépôt — https://github.com/moby/moby

## Voir aussi

- [[DevOps]] — le hub du domaine
