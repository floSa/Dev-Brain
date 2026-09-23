---
role: comparatif
nom: Comparatif - Registres d'images
categorie: devops/conteneur
tags: [container-registry, self-hosted]
---

# Comparatif - Registres d'images

> On tranche sur : le poids d'exploitation (un binaire ou une pile de services), la gestion des droits (projets et quotas, ou politiques par dépôt) et la maturité du projet — la licence ne départage pas, les deux sont en Apache-2.0 sans édition payante.

![[Comparatif - Registres d'images.base]]

## Ce qui départage

- [[Harbor]] — le registre complet : projets avec rôles, comptes robots et quotas de stockage, SSO LDAP et OIDC, réplication, proxy cache, scan Trivy, signatures Cosign et Notation ; en échange, PostgreSQL et un cache à exploiter, 4 Go de RAM au minimum, un installateur hors ligne de 696 Mio, et une mise à niveau qui demande une sauvegarde (la 2.15.2 migre PostgreSQL de 15 à 18). CNCF gradué depuis 2020, 29 478 étoiles.
- [[Zot]] — le registre léger : un binaire (218 Mio avec les extensions, 81 Mio sans), pas de base de données externe, synchronisation et miroir à la demande, scan Trivy embarqué ; la gestion des droits est par dépôt, sans projets documentés, et la haute disponibilité n'est pas clés en main. CNCF sandbox depuis 2022, 2 824 étoiles, cinq mainteneurs.

Comparaison par critère, en une ligne chacun :

- **Poids d'exploitation.** Harbor : plusieurs conteneurs, PostgreSQL, cache, 160 Go de disque recommandés. Zot : un processus, un stockage.
- **Droits.** Harbor : projets, rôles, comptes robots, quotas de stockage par projet. Zot : politiques d'accès par identité, groupe ou dépôt, avec expressions CEL.
- **Miroir et réplication.** Harbor : proxy cache (en pull-through, on ne peut pas y pousser) et réplication push ou pull vers une liste de registres. Zot : `sync` périodique et à la demande, avec filtre sur les images signées.
- **Scan.** Harbor : adaptateur Trivy, base hors ligne à monter à la main (documentation éclatée). Zot : Trivy en bibliothèque, base miroitable par `dbRepository`.
- **Haute disponibilité.** Harbor : chart Helm, PostgreSQL et cache externes. Zot : actif/passif par `sync`, ou scale-out sur S3 et un cache, sans auto-guérison.
- **Licence.** Les deux : Apache-2.0, aucune édition payante relevée.

**Pas de fiche ici**, et pourquoi (relevé le 2026-10-01) :

- **CNCF Distribution** (`registry:2`, puis la version 3) — Apache-2.0, Go, 10 634 étoiles, v3.1.2 du 2026-09-24, loin d'être en maintenance. C'est le moteur sous Harbor, GitLab et d'autres. Écarté : ni interface, ni authentification avancée, ni droits ; c'est la brique, pas le service. Garder pour un cache de tirage minimal.
- **Registre intégré à une forge** — [[GitLab CE]] livre un registre de conteneurs en édition Free (à activer) ; [[Forgejo]] et Gitea ont des registres de paquets qui comprennent l'OCI. Pas de service de plus si la forge est déjà installée ; c'est le bon choix d'une petite équipe qui a déjà une forge, et la raison pour laquelle ces pages ne sont pas des concurrentes ici.
- **Nexus Repository** — l'édition communautaire est plafonnée à 40 000 composants et 100 000 requêtes par jour (page d'aide de Sonatype, relevée ce jour ; la page commerciale de l'offre annonce encore d'autres chiffres, désaccord non tranché). Écarté : édition gratuite plafonnée sous contrat, pas un logiciel libre ; le support de Docker dans cette édition n'a pas été établi ici.
- **JFrog Artifactory / Container Registry** — licence et limites de l'offre gratuite non établies ; écartés faute d'une licence claire.
- **Quay** (Project Quay) — Apache-2.0, environ 2 800 étoiles, v3.16.6 du 2026-09-30, Python et Go. Écarté sauf contexte Red Hat ou OpenShift : plus lourd sur le papier, et ses prérequis n'ont pas été relevés.
- **Docker Hub** — le registre public, pas un registre à héberger. Pertinent ici pour ses limites de tirage : 100 pulls par 6 heures par adresse IPv4 (ou /64 IPv6) sans compte, 200 avec un compte gratuit, illimité pour les offres payantes (documentation Docker, relevée ce jour). Derrière une même adresse de sortie, le quota anonyme s'épuise vite : c'est ce que le proxy cache de Harbor ou le miroir de Zot absorbent.
- **Dragonfly** (projet CNCF) et **Spegel** — de la distribution d'images entre nœuds, pas des registres : ils s'ajoutent à un registre sur un grand cluster.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[Conteneurs & orchestration]] — le hub du sous-domaine.
