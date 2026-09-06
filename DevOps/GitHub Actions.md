---
role: brique
nom: GitHub Actions
alias: [github actions, gha, github-actions]
pitch: "CI/CD intégrée à GitHub : workflows YAML déclenchés sur événements du dépôt, runners hébergés ou auto-hébergés, large marketplace d'actions."
categorie: devops/ci
famille: saas
licence_type: proprietary
hosted: [managed]
maturite: production
langage: 
scaling: serverless
alternatives: []
complements: ["[[Docker]]"]
tags: [ci-cd]
url_docs: https://docs.github.com/actions
url_repo: https://github.com/actions/runner
---

# GitHub Actions

<!-- AUTO:BANDEAU:START -->
> CI/CD intégrée à GitHub : workflows YAML déclenchés sur événements du dépôt, runners hébergés ou auto-hébergés, large marketplace d'actions.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| SaaS | propriétaire | managé · serverless | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme de CI/CD intégrée à GitHub. Des **workflows** décrits en YAML dans
`.github/workflows/` se déclenchent sur des événements du dépôt — `push`,
`pull_request`, `schedule`, `workflow_dispatch` — et s'exécutent sur des **runners**,
machines éphémères hébergées par GitHub ou auto-hébergées. La force du modèle est la
proximité du code : rien à brancher quand le dépôt est déjà sur GitHub, et une marketplace
d'actions réutilisables (`actions/checkout`, `setup-python`, déploiements) évite de tout
réécrire. C'est aussi sa surface d'attaque, et elle est réelle : une action tierce
s'exécute avec les droits du workflow, donc elle s'épingle par **SHA** et non par un tag
mobile, et `GITHUB_TOKEN` se restreint par `permissions:` plutôt que laissé à son défaut.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Le code est déjà sur GitHub : CI/CD sans aucun outil externe à connecter | Code hébergé ailleurs — GitLab, Bitbucket : la CI native de la plateforme est plus naturelle (hors brain) |
| Tests, lint, build d'images et déploiement automatisés sur chaque push ou pull request | Orchestration de pipelines data ou ML avec dépendances et reprises : un orchestrateur dédié (Airflow, Dagster) complète mieux qu'une CI |
| Tâches planifiées (`schedule`) ou déclenchées à la demande (`workflow_dispatch`) | Parc important de runners auto-hébergés : le modèle de facturation bouge — un frais d'orchestration sur ces runners (~0,002 $/min) a été annoncé, puis reporté ou réévalué |
| Réutiliser des briques toutes faites de la marketplace plutôt que scripter depuis zéro | Dépôts privés à gros volume : le quota de minutes part vite sur des matrices de builds ou des runners gonflés — cacher les dépendances et borner les matrices |

## Mise en œuvre

- Installation — rien à installer si le dépôt est sur GitHub ; le runner (`actions/runner`) est open-source et s'auto-héberge
- Point d'entrée — fichiers YAML dans `.github/workflows/`, déclenchés par événement de dépôt
- Prérequis — un dépôt GitHub. Les secrets passent par le magasin chiffré du dépôt ou de l'organisation, jamais en clair dans le YAML ; se méfier de `pull_request_target`, qui donne à une PR de fork le contexte du dépôt cible. Épingler les actions tierces par SHA, et restreindre `permissions:` au strict nécessaire
- Exécution — managé, sur des runners éphémères hébergés par GitHub, ou sur des runners auto-hébergés
- Coût — gratuit sur les dépôts publics ; sur les dépôts privés, quota de minutes gratuit par plan puis facturation à la minute selon le type de machine. Baisse des tarifs des runners hébergés en janvier 2026

## Écosystème

### Alternatives

- *Aucune alternative déclarée : seule page de la catégorie `devops/ci`. GitLab CI, Jenkins et CircleCI seraient les candidats naturels, aucun n'est fiché — le cas du code hébergé ailleurs est pointé dans le tableau ci-dessus.*

### Compléments

- [[Docker]] — Conteneurisation standard : packaging d'applications en images OCI reproductibles, isolées et portables d'un environnement à l'autre. — les images que les workflows construisent et publient

## Ressources

- Documentation — https://docs.github.com/actions
- Dépôt — https://github.com/actions/runner

## Voir aussi

- [[DevOps]] — le hub du domaine
