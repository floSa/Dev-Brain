---
role: comparatif
nom: Comparatif - CI-CD auto-hébergé
categorie: devops/ci
tags: [ci-cd, self-hosted]
---

# Comparatif - CI-CD auto-hébergé

> On tranche sur : la forge (intégrée ou séparée), ce qu'on accepte d'exploiter, la licence réelle et ce que l'édition libre ne contient pas — le format de pipeline et le SSO pèsent moins que ces trois-là.

![[Comparatif - CI-CD auto-hébergé.base]]

## Ce qui départage

- [[GitHub Actions]] — la CI intégrée à GitHub : sur site, il faut GitHub Enterprise Server (propriétaire) et des runners auto-hébergés, avec un stockage blob externe ; le runner lui-même est MIT. C'est le seul membre à ne pas être libre côté serveur.
- [[GitLab CE]] — la forge complète, dépôts, revue, CI, registres : cœur MIT, dossier `ee/` propriétaire ; approbations obligatoires (Premium) et SAST avancé (Ultimate) à payer ; la plus lourde (8 vCPU et 16 Go conseillés, PostgreSQL, Redis, Gitaly).
- [[Forgejo]] — la forge légère, un binaire, CI par Forgejo Actions dont la syntaxe ressemble à celle de GitHub Actions mais pas à l'identique ; GPL-3.0-or-later depuis la v9, sans édition payante relevée, gouvernance associative.
- [[Jenkins]] — le serveur de CI sans forge, MIT, plus de 2 000 plugins et un Jenkinsfile Groovy ; le plus souple (agents Windows, matériel) et le plus exposé : un avis de sécurité sur les plugins presque chaque mois.
- [[Woodpecker CI]] — la CI sans forge la plus légère (Apache-2.0, environ 100 Mo de RAM), une étape par conteneur ; l'identité vient de la forge, et Forgejo, Gitea, GitLab, GitHub et Bitbucket sont supportées.

Comparaison par critère, en une ligne chacun :

- **Forge.** Intégrée : GitHub Actions, GitLab CE, Forgejo. Séparée : Jenkins, Woodpecker CI.
- **Format.** `.github/workflows` (YAML) ; `.gitlab-ci.yml` ; Forgejo Actions, YAML proche de GitHub ; `Jenkinsfile` (Groovy, déclaratif ou scripté) ; `.woodpecker/*.yaml`, avec `image` et `commands` par étape.
- **Exécution.** Runners éphémères ou permanents chez GitHub et GitLab (exécuteurs Docker et Kubernetes) ; Forgejo Runner, un binaire qui exécute du code arbitraire ; agents Jenkins, éphémères par pod avec le plugin Kubernetes ; agents Woodpecker, une étape par conteneur.
- **Écosystème.** Marketplace d'actions (GitHub) ; actions résolues depuis `data.forgejo.org` par défaut ; plus de 2 000 plugins (Jenkins) ; registre de plugins sous forme d'images (Woodpecker).
- **SSO.** SAML d'instance en Free sur GitLab CE ; OAuth et LDAP annoncés sur Forgejo ; plugins sur Jenkins ; par la forge seulement sur Woodpecker.

**Pas de fiche ici**, et pourquoi :

- **Gitea** — MIT, environ 58 200 étoiles, v28.0.0 (2026-09-29). Écarté parce que Forgejo en est le fork communautaire et qu'un seul des deux suffit : Gitea Enterprise (CommitGo) garde SAML, audit et scan de dépendances en édition payante. À choisir si le client veut précisément un éditeur derrière.
- **Drone / Harness** — la *Community Edition* de Drone est sous Apache-2.0, l'*Enterprise Edition* sous une licence propriétaire non commerciale ; le dépôt `harness/harness` (Apache-2.0, environ 38 500 étoiles, dernière release v2.28.2 du 2026-04-20) porte une plateforme plus vaste. Écarté : Woodpecker, fork communautaire de Drone, couvre le même besoin sous Apache-2.0.
- **Concourse** (Apache-2.0, v8.3.1 du 2026-09-28, environ 7 900 étoiles) — pipelines déclaratifs en conteneurs, à apprendre ; écarté faute de place (plafond de quatre briques).
- **Tekton** (Apache-2.0, v1.16.0 du 2026-08-31, environ 9 100 étoiles) — un cadre Kubernetes, sans interface ni déclencheur de forge inclus ; pertinent seulement sur un cluster déjà là.
- **Buildbot** (GPL-2.0) — configuration en Python, dépôt actif, mais la dernière release relevée date de mai 2025 : contradiction à vérifier.
- **SourceHut** (builds.sr.ht, AGPL) — lié à son écosystème, écarté.
- **Harbor** — registre d'images, à traiter dans le bloc suivant.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[DevOps]] — le hub du domaine.
- [[Pipelines CI-CD on-prem — runners, secrets et artefacts]] — la notion : anatomie d'un pipeline, runners éphémères ou permanents, isolation, artefacts, réseau fermé.
