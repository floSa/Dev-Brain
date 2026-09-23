---
role: brique
nom: Woodpecker CI
alias: [woodpecker, woodpecker-ci]
pitch: "CI légère pilotée par une forge (Apache-2.0, Go, fork de Drone 0.8) : chaque étape tourne dans un conteneur, environ 100 Mo de RAM pour le serveur, Forgejo, Gitea, GitLab, GitHub et Bitbucket comme forges — pas d'authentification propre, les comptes viennent de la forge."
categorie: devops/ci
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Go
scaling: distributed
alternatives: ["[[GitHub Actions]]", "[[GitLab CE]]", "[[Jenkins]]"]
complements: ["[[Forgejo]]", "[[Docker]]", "[[Kubernetes]]"]
tags: [ci-cd, self-hosted, container]
url_docs: https://woodpecker-ci.org/docs/intro
url_repo: https://github.com/woodpecker-ci/woodpecker
---

# Woodpecker CI

<!-- AUTO:BANDEAU:START -->
> CI légère pilotée par une forge (Apache-2.0, Go, fork de Drone 0.8) : chaque étape tourne dans un conteneur, environ 100 Mo de RAM pour le serveur, Forgejo, Gitea, GitLab, GitHub et Bitbucket comme forges — pas d'authentification propre, les comptes viennent de la forge.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Moteur de CI/CD communautaire : un **serveur** reçoit les événements de la forge, des **agents** exécutent les pipelines, et **chaque étape tourne dans son propre conteneur**. Il ne fournit pas de dépôts : il s'appuie sur une forge. Relevé le 2026-09-30 : **v3.18.1** (2026-09-08), environ 7 900 étoiles, licence **Apache-2.0**, dernier push le 2026-09-30.

**Filiation avec Drone.** Woodpecker est un fork de Drone 0.8 (2019), avec une gouvernance communautaire et aucun éditeur derrière. Drone, lui, appartient à Harness : le fichier `LICENSE` de la branche `drone` place la *Community Edition* sous Apache-2.0 et l'*Enterprise Edition* sous la *Drone Non-Commercial License* (propriétaire : l'usage commercial est limité à un essai de 32 jours, avec des dérogations sous 5 M$ de revenus ou 5 000 pipelines par an). La licence de Drone dépend donc de l'édition et de la branche ; le dépôt `harness/harness` (Apache-2.0, 38 500 étoiles) porte le produit successeur de Harness, une plateforme plus vaste. Drone n'a pas de fiche.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Une CI très légère à côté de [[Forgejo]] ou Gitea, sur une petite machine | La forge n'est pas dans la liste (Forgejo, Gitea, GitHub, GitLab, Bitbucket) |
| Des étapes isolées par conteneur, sans configurer d'agents à la main | Des builds qui sortent du conteneur (autre système, matériel) : le moteur local existe, mais le Docker est le plus mûr |
| Une équipe qui connaît Docker et veut des plugins sous forme d'images | Un SSO propre à la CI : il n'y en a pas, les comptes viennent de la forge par OAuth2 |
| Un outil open source sans partie payante | Un support contractuel : aucun éditeur, la gouvernance est communautaire |

## Mise en œuvre

- Installation — binaires ou images Docker pour le serveur et l'agent ; base SQLite par défaut, [[Postgres]] 11 ou plus, MySQL ou MariaDB
- Point d'entrée — dossier `.woodpecker/` du dépôt, un fichier `.yaml` par workflow ; chaque étape porte `name`, `image` et `commands` ; `when` filtre par événement ou branche ; `services` lance des conteneurs annexes ; un plugin se configure par `image` et `settings`
- Prérequis — une forge avec OAuth2 configuré ; l'accès est contrôlé par `WOODPECKER_ADMIN`, `WOODPECKER_ORGS` ou l'inscription fermée. Les secrets s'appellent par `from_secret` et se définissent dans l'interface
- Exécution — serveur et agents ; une étape précédée d'un `clone` automatique, l'espace de travail partagé entre étapes. Environ 100 Mo de RAM au repos pour le serveur et 30 Mo par agent (README). Les moteurs : Docker (par défaut, le plus mûr), Kubernetes, local ; l'agent ne nettoie pas les images sur l'hôte ; Podman n'est pas officiellement supporté
- Coût — gratuit ; le coût est l'exploitation du serveur, des agents et de l'accès Docker

## Limites à connaître

- **Un accès au moteur de conteneurs, donc un privilège.** Une étape qui construit des images a besoin du socket Docker ou d'une alternative : un pipeline compromis touche l'hôte. Ne pas ouvrir l'instance à des dépôts de tiers sans avoir décidé qui a le droit de lancer ce genre d'étape.
- **Pas de SSO propre.** L'identité est celle de la forge ; le SSO se règle côté forge, pas dans Woodpecker.
- **Écosystème de plugins restreint** : un registre officiel d'images, plus petit que celui de GitHub Actions. La compatibilité avec la syntaxe GitHub n'existe pas.
- **Support de Bitbucket Data Center non vérifié.**

## Écosystème

### Alternatives

- [[GitHub Actions]] — CI/CD intégrée à GitHub : workflows YAML déclenchés sur événements du dépôt, runners hébergés ou auto-hébergés, large marketplace d'actions. — la CI intégrée à sa forge, à l'écosystème d'actions bien plus large.
- [[GitLab CE]] — Forge Git complète en édition Community (cœur MIT, dossier ee/ propriétaire) : dépôts, revues, CI/CD, registre de conteneurs et de paquets — lourde à exploiter (PostgreSQL, Redis, Gitaly, 8 vCPU et 16 Go conseillés) ; approbations obligatoires et SAST avancé réservés aux éditions payantes. — la forge avec CI intégrée, bien plus lourde mais tout-en-un.
- [[Jenkins]] — Serveur d'automatisation historique (MIT, Java) : pipelines en Jenkinsfile Groovy, agents permanents ou éphémères, plus de 2 000 plugins — mais chaque plugin est du code tiers à patcher, avec un avis de sécurité sur les plugins presque chaque mois. — le serveur d'automatisation le plus riche en plugins, avec la dette qui va avec.

### Compléments

- [[Forgejo]] — Forge Git légère issue du fork de Gitea (GPL-3.0-or-later depuis la v9, Go, gouvernance liée à l'association Codeberg e.V.) : dépôts, revues, registres de paquets et Forgejo Actions, dont la syntaxe s'inspire de celle de GitHub Actions sans en être une copie. — la forge que Woodpecker prend comme source des dépôts et des comptes.
- [[Docker]] — Conteneurisation standard : packaging d'applications en images OCI reproductibles, isolées et portables d'un environnement à l'autre. — le moteur par défaut des étapes.
- [[Kubernetes]] — Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter. — un moteur d'exécution des étapes en pods.

## Ressources

- Documentation — https://woodpecker-ci.org/docs/intro
- Dépôt — https://github.com/woodpecker-ci/woodpecker
- Documentation — forge Forgejo : https://woodpecker-ci.org/docs/administration/configuration/forges/forgejo
- Documentation — configuration du serveur : https://woodpecker-ci.org/docs/administration/configuration/server
- Documentation — moteur Docker : https://woodpecker-ci.org/docs/administration/configuration/backends/docker
- Dépôt — licence de Drone : https://raw.githubusercontent.com/harness/harness/drone/LICENSE

## Voir aussi

- [[DevOps]] — le hub du domaine
- [[Comparatif - CI-CD auto-hébergé]] — le comparatif : forge intégrée ou séparée, format de pipeline, licence.
- [[Pipelines CI-CD on-prem — runners, secrets et artefacts]] — la notion : anatomie d'un pipeline, runners, artefacts, réseau fermé.
