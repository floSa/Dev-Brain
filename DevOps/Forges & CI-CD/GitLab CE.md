---
role: brique
nom: GitLab CE
alias: [gitlab, gitlab-ce, gitlab community edition, gitlab ce]
pitch: "Forge Git complète en édition Community (cœur MIT, dossier ee/ propriétaire) : dépôts, revues, CI/CD, registre de conteneurs et de paquets — lourde à exploiter (PostgreSQL, Redis, Gitaly, 8 vCPU et 16 Go conseillés) ; approbations obligatoires et SAST avancé réservés aux éditions payantes."
categorie: devops/ci
famille: plateforme
licence_type: open-core
hosted: [self]
maturite: production
langage: Ruby
scaling: distributed
alternatives: ["[[GitHub Actions]]", "[[Forgejo]]", "[[Jenkins]]", "[[Woodpecker CI]]"]
complements: ["[[Docker]]", "[[Kubernetes]]", "[[Helm]]", "[[Postgres]]", "[[Redis]]", "[[Keycloak]]"]
tags: [ci-cd, version-control, self-hosted]
url_docs: https://docs.gitlab.com/
url_repo: https://gitlab.com/gitlab-org/gitlab
---

# GitLab CE

<!-- AUTO:BANDEAU:START -->
> Forge Git complète en édition Community (cœur MIT, dossier ee/ propriétaire) : dépôts, revues, CI/CD, registre de conteneurs et de paquets — lourde à exploiter (PostgreSQL, Redis, Gitaly, 8 vCPU et 16 Go conseillés) ; approbations obligatoires et SAST avancé réservés aux éditions payantes.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Ruby | open-core | self-hébergé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Forge Git et plateforme de CI/CD dans un seul produit : dépôts, demandes de fusion, tickets, CI/CD décrite dans `.gitlab-ci.yml`, registre de conteneurs, registre de paquets. La **Community Edition** est la version libre, à installer chez soi. Relevé le 2026-09-30 : **v19.4.1** (2026-09-23, correctif critique), environ 24 500 étoiles sur le miroir GitHub `gitlabhq/gitlabhq` (le dépôt d'origine est sur gitlab.com). Langage principal Ruby, avec des composants en Go (Gitaly, Workhorse, Runner). Les versions mineures sortent chaque mois, les correctifs deux fois par mois ; 19.4 reçoit bugs et sécurité, 19.3 et 19.2 seulement la sécurité.

**Licence : à lire avant de promettre quoi que ce soit.** Le fichier `LICENSE` du dépôt place tout sous MIT Expat, sauf `ee/` (licence propriétaire de GitLab, `ee/LICENSE`), `jh/` et `doc/` (CC BY-SA 4.0). Le code `ee/` exige un abonnement dès la production. D'où le classement en **open-core** : le cœur est libre, une partie des fonctions ne l'est pas.

- **Ce que la CE contient** (page de documentation de chaque fonction lue, « Tier: Free ») : le registre de conteneurs, l'authentification SAML d'une instance auto-hébergée, le SAST de base avec des analyseurs libres et le rapport JSON téléchargeable. GitLab Runner est sous licence MIT.
- **Ce qu'elle ne contient pas** : les règles d'approbation de demandes de fusion (Premium, Ultimate) ; le SAST avancé entre fichiers et entre fonctions, les résultats dans la demande de fusion, la gestion des vulnérabilités et la personnalisation des règles (Ultimate) ; les groupes d'auditeurs SAML (Premium, Ultimate).
- **Ce qu'une ESN peut faire.** La licence MIT autorise de déployer la CE chez un client et de l'exploiter pour lui, en conservant les mentions de copyright. Ce qui change la donne est le **paquet** : le paquet `gitlab-ee` installé sans licence n'active que les fonctions gratuites, mais il embarque du code `ee/`, donc sous la licence propriétaire qui demande un abonnement pour la production. Livrer `gitlab-ce` évite la question. La politique de marque GitLab n'a pas été lue : à consulter avant d'afficher le nom dans une offre. Validation juridique à faire, pas un avis.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un seul outil doit porter dépôts, revue, CI/CD et registre de conteneurs, hébergé chez le client | Une équipe d'une personne et quelques dépôts : [[Forgejo]] tient dans un binaire, GitLab demande 8 vCPU et 16 Go de RAM |
| Le client connaît déjà GitLab, ou exige un éditeur avec des versions de sécurité régulières | Le projet exige des approbations obligatoires, du SAST avancé ou un journal d'audit : ces fonctions sont en Premium ou Ultimate, donc un abonnement à signer |
| Des runners à faire tourner sur le cluster du client (exécuteur Kubernetes) ou sur des machines dédiées | Une installation à mettre à jour sans équipe : la cadence est mensuelle et les correctifs de sécurité ne sont rétroportés que sur deux versions |
| Les comptes viennent du SAML ou de l'annuaire du client | Aucun besoin de forge : une CI seule ([[Woodpecker CI]], [[Jenkins]]) se branche sur les dépôts existants |

## Mise en œuvre

- Installation — paquet Linux Omnibus (méthode décrite comme la plus mature), chart [[Helm]], opérateur Kubernetes, image [[Docker]], ou Terraform et Ansible par GitLab Environment Toolkit
- Point d'entrée — l'interface web ; la CI se décrit dans `.gitlab-ci.yml` à la racine de chaque dépôt
- Prérequis — pour un nœud unique : 8 vCPU et 16 Go de RAM (un déploiement minimal tient sur 8 Go si la mémoire est contrainte), swap désactivé ; [[Postgres]] seule base supportée (17.x conseillée pour la 19.x) ; [[Redis]] 7.2 conseillé, ou Valkey ; au moins 200 Mo par processus Sidekiq ; 40 Go de disque sur les nœuds applicatifs plus un volume Gitaly de la taille des dépôts
- Exécution — plusieurs composants (Puma, Sidekiq, Workhorse, Gitaly pour les dépôts Git) ; les jobs CI tournent sur des **GitLab Runner**, séparés du serveur : exécuteurs Kubernetes, Docker, Docker Autoscaler et Instance recommandés ; Shell, SSH, VirtualBox, Parallels et Custom en maintenance, Docker Machine déprécié
- Coût — la CE est gratuite ; le coût est l'exploitation et, si une fonction Premium ou Ultimate devient nécessaire, l'abonnement par utilisateur

## Limites à connaître

- **Des failles critiques fréquentes côté CI.** Le correctif du 2026-09-23 (19.4.1, 19.3.3, 19.2.7) traite 11 failles dont deux de score 9,9 : CVE-2026-89078 et CVE-2026-93577, des erreurs mémoire dans le traitement des expressions régulières qui permettent à un utilisateur authentifié d'exécuter du code via la configuration CI/CD. Celui du 2026-09-10 corrige CVE-2026-85706 (score 10,0, lecture de fichiers arbitraires sans authentification par l'API des commits, versions 18.7 et suivantes). Une instance exposée doit suivre les correctifs mensuels et bihebdomadaires.
- **L'empreinte.** C'est une application Rails avec plusieurs services : une instance sur un petit serveur partagé ralentit vite ; Gitaly demande un disque rapide.
- **Pas de version à long terme.** Seules la version courante et les deux mensuelles précédentes reçoivent les correctifs de sécurité : un client qui ne met pas à jour chaque trimestre sort du support.
- Aucune annonce de changement de licence de la CE n'a été trouvée sur 2024-2026 ; la recherche dans les pages de dépréciation n'a pas été poussée.

## Écosystème

### Alternatives

- [[GitHub Actions]] — CI/CD intégrée à GitHub : workflows YAML déclenchés sur événements du dépôt, runners hébergés ou auto-hébergés, large marketplace d'actions. — l'autre CI/CD intégrée à sa forge ; ici la forge est hébergeable chez soi sans passer par GitHub Enterprise Server.
- [[Forgejo]] — Forge Git légère issue du fork de Gitea (GPL-3.0-or-later depuis la v9, Go, gouvernance liée à l'association Codeberg e.V.) : dépôts, revues, registres de paquets et Forgejo Actions, dont la syntaxe s'inspire de celle de GitHub Actions sans en être une copie. — la forge légère : même périmètre dépôts, revue et CI, sans l'empreinte ni les éditions payantes.
- [[Jenkins]] — Serveur d'automatisation historique (MIT, Java) : pipelines en Jenkinsfile Groovy, agents permanents ou éphémères, plus de 2 000 plugins — mais chaque plugin est du code tiers à patcher, avec un avis de sécurité sur les plugins presque chaque mois. — le serveur d'automatisation sans forge : il se branche sur des dépôts déjà hébergés ailleurs.
- [[Woodpecker CI]] — CI légère pilotée par une forge (Apache-2.0, Go, fork de Drone 0.8) : chaque étape tourne dans un conteneur, environ 100 Mo de RAM pour le serveur, Forgejo, Gitea, GitLab, GitHub et Bitbucket comme forges — pas d'authentification propre, les comptes viennent de la forge. — la CI légère qui s'appuie sur une forge existante.

### Compléments

- [[Docker]] — Conteneurisation standard : packaging d'applications en images OCI reproductibles, isolées et portables d'un environnement à l'autre. — l'image officielle, et l'exécuteur Docker des runners pour les jobs.
- [[Kubernetes]] — Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter. — l'exécuteur Kubernetes des runners, et la cible du chart Helm de GitLab.
- [[Helm]] — Gestionnaire de paquets de Kubernetes : un chart décrit, versionne et installe un ensemble de ressources (Apache-2.0, Go, CNCF diplômé). — le chart officiel de GitLab, l'une des méthodes d'installation décrites.
- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne. — la seule base supportée par GitLab.
- [[Redis]] — Store clé-valeur en mémoire ultra-rapide : cache, sessions, files et broker pub/sub. — le cache et les files de GitLab, en instance autonome.
- [[Keycloak]] — Fournisseur d'identité complet : OIDC, OAuth 2.0 et SAML 2.0, fédération LDAP et Active Directory, courtage vers d'autres fournisseurs, MFA (TOTP, WebAuthn, passkeys) et plusieurs realms (Apache-2.0, Java sur Quarkus, CNCF incubating) — aucune fonction gardée en édition payante, mais une JVM et une base SQL à exploiter. — un fournisseur d'identité pour l'authentification unique, à côté du SAML déclaré en Free.

## Ressources

- Documentation — https://docs.gitlab.com/
- Dépôt — https://gitlab.com/gitlab-org/gitlab
- Dépôt — licence : https://gitlab.com/gitlab-org/gitlab/-/raw/master/LICENSE
- Documentation — prérequis : https://docs.gitlab.com/install/requirements/
- Documentation — politique de maintenance : https://docs.gitlab.com/policy/maintenance/
- Documentation — exécuteurs du runner : https://docs.gitlab.com/runner/executors/

## Voir aussi

- [[DevOps]] — le hub du domaine
- [[Comparatif - CI-CD auto-hébergé]] — le comparatif : forge intégrée ou séparée, format de pipeline, licence.
- [[Pipelines CI-CD on-prem — runners, secrets et artefacts]] — la notion : anatomie d'un pipeline, runners, artefacts, réseau fermé.
