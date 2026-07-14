---
galaxie: dev
type: service
nom: GitHub Actions
alias: [github actions, gha, github-actions]
pitch: "CI/CD intégrée à GitHub : workflows YAML déclenchés sur événements du dépôt, runners hébergés ou auto-hébergés, large marketplace d'actions."
categorie: devops/ci
licence_type: proprietary
hosted: managed
maturite: production
langage: 
scaling: serverless
alternatives: []
remplace_par: []
status: actif
tags: [ci-cd]
url_docs: https://docs.github.com/actions
url_repo: https://github.com/actions/runner
---

# GitHub Actions

## Pourquoi

Plateforme de **CI/CD intégrée à GitHub**. Des **workflows** décrits en YAML (`.github/workflows/`) se déclenchent sur des événements du dépôt (`push`, `pull_request`, `schedule`, manuel…) et s'exécutent sur des **runners** — machines éphémères hébergées par GitHub ou auto-hébergées. Force du modèle : la proximité du code (rien à brancher quand le dépôt est déjà sur GitHub) et une **marketplace** d'actions réutilisables (`actions/checkout`, `setup-python`, déploiements…) qui évite de tout réécrire.

## Quand l'utiliser

- Le code est sur GitHub : CI/CD sans outil externe à connecter.
- Tests, lint, build d'images et déploiement automatisés sur chaque push/PR.
- Tâches planifiées (`schedule`) ou déclenchées à la demande (`workflow_dispatch`).
- Réutiliser des briques toutes faites de la marketplace plutôt que scripter from scratch.

## Quand NE PAS l'utiliser

- Code hébergé ailleurs (GitLab, Bitbucket) → la CI native de la plateforme (GitLab CI, etc.) est plus naturelle (hors brain pour l'instant).
- Besoins lourds de runners auto-hébergés à grande échelle : surveiller le modèle de facturation qui évolue (voir Déploiement & coût).
- Orchestration de pipelines data/ML complexes avec dépendances et reprises → un orchestrateur dédié (Airflow, Dagster) complète mieux qu'une CI.

## Déploiement & coût

- Service **managé** propriétaire ; le **runner** est open-source (`actions/runner`) et peut être auto-hébergé.
- **Gratuit sur les dépôts publics** (runners hébergés). Sur les dépôts privés, **quota de minutes gratuites** par plan, puis facturation à la minute selon le type de machine.
- Évolutions 2026 : baisse des tarifs des runners hébergés (janvier 2026) ; un projet de frais d'orchestration sur les runners **auto-hébergés** (~0,002 $/min) a été annoncé puis reporté/réévalué — à suivre.

## Pièges

- **Secrets** : utiliser les secrets chiffrés du dépôt/organisation, jamais en clair dans le YAML ; se méfier des workflows déclenchés par des PR de forks (`pull_request_target`).
- Épingler les actions tierces par **SHA** (pas seulement un tag mobile) : une action compromise s'exécute avec les droits du workflow — surface d'attaque supply-chain réelle.
- Minutes privées consommées vite (matrices de builds, runners gonflés) : cacher les dépendances et borner les matrices.
- `GITHUB_TOKEN` parfois trop permissif par défaut : restreindre les `permissions:` au strict nécessaire.

## Alternatives

<!-- Pas d'autre outil de CI/CD en brain (categorie devops/ci). GitLab CI, Jenkins, CircleCI seraient les alternatives mais ne sont pas encore documentés ici. -->

## Liens

- [[Dev/Services/Docker|Docker]] — images construites et publiées depuis les workflows CI
- Doc : https://docs.github.com/actions
