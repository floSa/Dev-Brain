---
role: comparatif
nom: Comparatif - Orchestration de conteneurs
categorie: devops/conteneur
tags: [container]
---

# Comparatif - Orchestration de conteneurs

> On tranche sur : le nombre de machines, qui opère le socle, la haute disponibilité voulue et ce que coûte l'exploitation — la licence ne départage pas, tous les membres sont sous Apache-2.0.

![[Comparatif - Orchestration de conteneurs.base]]

## Ce qui départage

- [[Docker]] — le moteur de référence et l'écosystème le plus large, sur une machine, avec un démon qui tourne en root ; l'Engine est libre, c'est le client de bureau qui est payant au-delà de 250 salariés ou 10 M$ de chiffre d'affaires ; il n'orchestre rien, le mode Swarm intégré n'ayant pas de fiche ici.
- [[Docker Compose]] — la pile d'une machine décrite en un fichier : relance par `restart:`, attente d'un service sain, GPU ; aucune bascule sur une autre machine, et la doc officielle ne dit pas quelles clés `deploy:` sont honorées hors Swarm.
- [[Podman]] — les mêmes images, sans démon et en rootless ; Quadlet confie les redémarrages à systemd, sans orchestrateur ; le compose n'est qu'un aiguillage vers `docker-compose` ou `podman-compose` (GPL-2.0).
- [[k3s]] — Kubernetes avec les choix faits : un binaire, un réseau, un ingress et un stockage local livrés, 2 Go de RAM, un mode hors ligne ; la haute disponibilité demande 3 serveurs avec etcd embarqué ou une base externe, SQLite ne servant qu'un serveur.
- [[Kubernetes]] — l'orchestrateur complet : droits par équipe, quotas, mise à l'échelle, opérateurs ; la haute disponibilité veut 3 nœuds de contrôle et un équilibreur, le support de chaque version dure environ 14 mois, et réseau, ingress, stockage et supervision sont à choisir soi-même. Le coût est du temps d'équipe.

**Ne sont pas des membres** : [[Helm]] et [[Argo CD]] s'installent **sur** Kubernetes, ils n'en sont pas des alternatives ; le premier est dans le même dossier, le second dans `devops/ci`.

**Pas de fiche ici**, faute d'avoir trouvé la place ou la licence qu'il faut :

- HashiCorp Nomad — activement maintenu (v2.0.7, 2026-09-17 ; environ 17 000 étoiles), simple à opérer (un binaire) et capable d'ordonnancer des conteneurs, des binaires et des machines virtuelles. Écarté pour trois raisons : la licence BUSL-1.1 depuis août 2023 (usage interne en production permis, mais interdit d'offrir Nomad à des tiers de façon hébergée ou embarquée pour concurrencer l'offre payante d'IBM, titulaire depuis le rachat de HashiCorp le 2025-02-27 ; chaque version se convertit en MPL 2.0 quatre ans après sa publication) ; aucun fork communautaire notable trouvé ; une part faible dans les données trouvées (3,7 à 3,8 % de la catégorie chez PeerSpot, aucune enquête CNCF ni Stack Overflow chiffrant Nomad). Les fonctions multi-région, quotas, Sentinel et audit sont réservées à Enterprise. Un candidat sérieux pour un petit cluster qui mêle binaires et conteneurs : il n'a pas été fiché parce que le plafond du bloc est de six briques et que Kubernetes, k3s et Helm sont plus éprouvés.
- Docker Swarm — le mode intégré à Docker Engine n'est pas déclaré déprécié, mais le projet autonome « Classic Swarm » n'est plus développé, et le README de Compose précise que Swarm n'a pas adopté la Compose Specification actuelle.
- Kamal — déploiement de conteneurs par SSH (MIT, v2.12.0), impératif, sans réconciliation d'état ; un équilibreur externe est requis en multi-serveurs.
- RKE2, Talos Linux, MicroK8s, OKD — d'autres distributions Kubernetes, décrites dans la fiche de [[Kubernetes]].

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[Conteneurs & orchestration]] — le hub du dossier.
- [[Du Compose à Kubernetes — quand changer d'échelle]] — la notion : ce que Compose ne fait pas, ce que coûte un cluster, le critère de bascule et le GitOps.
