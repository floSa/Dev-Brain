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
complements: ["[[Docker]]", "[[Argo CD]]"]
tags: [ci-cd]
url_docs: https://docs.github.com/actions
url_repo: https://github.com/actions/runner
---

# GitHub Actions

<!-- AUTO:BANDEAU:START -->
> CI/CD intégrée à GitHub : workflows YAML déclenchés sur événements du dépôt, runners hébergés ou auto-hébergés, large marketplace d'actions.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| SaaS | propriétaire | managé · serverless | production | à jour · 2026-08-26 |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme de CI/CD intégrée à GitHub. Des **workflows** décrits en YAML dans
`.github/workflows/` se déclenchent sur des événements du dépôt — `push`,
`pull_request`, `schedule`, `workflow_dispatch` — et s'exécutent sur des **runners**,
machines éphémères hébergées par GitHub ou auto-hébergées. La force du modèle est la
proximité du code : rien à brancher quand le dépôt est déjà sur GitHub, et une marketplace
d'actions réutilisables (`actions/checkout`, `setup-python`, déploiements) évite de tout
réécrire. L'offre **sur site** existe : GitHub Enterprise Server exécute Actions, mais
uniquement sur des runners auto-hébergés. Relevé le 2026-09-30 : runner `actions/runner`
**v2.337.0** (2026-08-26), environ 6 300 étoiles, licence MIT. C'est aussi sa surface d'attaque, et elle est réelle : une action tierce
s'exécute avec les droits du workflow, donc elle s'épingle par **SHA** et non par un tag
mobile, et `GITHUB_TOKEN` se restreint par `permissions:` plutôt que laissé à son défaut.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Le code est déjà sur GitHub : CI/CD sans aucun outil externe à connecter | Code hébergé ailleurs — GitLab, Bitbucket : la CI native de la plateforme est plus naturelle (hors brain) |
| Tests, lint, build d'images et déploiement automatisés sur chaque push ou pull request | Orchestration de pipelines data ou ML avec dépendances et reprises : un orchestrateur dédié (Airflow, Dagster) complète mieux qu'une CI |
| Tâches planifiées (`schedule`) ou déclenchées à la demande (`workflow_dispatch`) | Parc important de runners auto-hébergés : un frais de plateforme de 0,002 $/min a été annoncé le 2025-12-16 pour le 2026-03-01, reporté le lendemain « pour réévaluer l'approche » ; au 2026-09-30, aucune nouvelle date n'est publiée et la doc de facturation dit l'usage gratuit sur ces runners |
| Réutiliser des briques toutes faites de la marketplace plutôt que scripter depuis zéro | Dépôts privés à gros volume : le quota de minutes part vite sur des matrices de builds ou des runners gonflés — cacher les dépendances et borner les matrices |

## Mise en œuvre

- Installation — rien à installer si le dépôt est sur GitHub ; le runner (`actions/runner`) est open-source et s'auto-héberge. Sur GitHub Enterprise Server : Actions activé par l'administrateur, avec un stockage blob externe obligatoire (S3, Azure Blob, GCS, ou un MinIO compatible S3) et un minimum de 8 vCPU et 64 Go de RAM pour 740 runners connectés
- Point d'entrée — fichiers YAML dans `.github/workflows/`, déclenchés par événement de dépôt
- Prérequis — un dépôt GitHub. Les secrets passent par le magasin chiffré du dépôt ou de l'organisation, jamais en clair dans le YAML ; se méfier de `pull_request_target`, qui donne à une PR de fork le contexte du dépôt cible. Épingler les actions tierces par SHA — l'action `tj-actions/changed-files` a été compromise en mars 2025 (CVE-2025-30066, tags réécrits, secrets vidés dans les journaux, plus de 23 000 dépôts) — ; la politique d'actions autorisées d'une organisation peut exiger cet épinglage depuis le 2025-08-15. Restreindre `permissions:` au strict nécessaire
- Exécution — managé, sur des runners éphémères hébergés par GitHub, ou sur des runners auto-hébergés ; sur un cluster Kubernetes, le contrôleur Actions Runner Controller (ARC) les fait vivre. La rétention des journaux, statuts et exécutions passe à 90 jours par défaut au 2026-10-01 (plus de 400 jours auparavant)
- Coût — gratuit sur les dépôts publics ; sur les dépôts privés, minutes incluses par mois : 2 000 (Free), 3 000 (Pro, Team), 50 000 (Enterprise Cloud), puis facturation à la minute — Linux 2 cœurs 0,006 $, Windows 2 cœurs 0,010 $, macOS 0,062 $. Baisse des tarifs des runners hébergés allant jusqu'à 39 % le 2026-01-01. Cache : 10 Go par dépôt, 0,07 $/Go/mois au-delà

## Écosystème

### Alternatives

- *Aucune alternative déclarée : seule page de la catégorie `devops/ci`. GitLab CI, Jenkins et CircleCI seraient les candidats naturels, aucun n'est fiché — le cas du code hébergé ailleurs est pointé dans le tableau ci-dessus.*

### Compléments

- [[Docker]] — Conteneurisation standard : packaging d'applications en images OCI reproductibles, isolées et portables d'un environnement à l'autre. — les images que les workflows construisent et publient
- [[Argo CD]] — Contrôleur GitOps pour Kubernetes : compare en continu un dépôt Git à l'état du cluster et le réconcilie (Apache-2.0, Go, CNCF diplômé). — le CD qui déploie ce que la CI a construit

## Ressources

- Documentation — https://docs.github.com/actions
- Dépôt — https://github.com/actions/runner

## Voir aussi

- [[DevOps]] — le hub du domaine
