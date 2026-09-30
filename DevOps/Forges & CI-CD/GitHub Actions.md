---
role: brique
nom: GitHub Actions
alias: [github actions, gha, github-actions]
pitch: "CI/CD intégrée à GitHub : workflows YAML déclenchés sur événements du dépôt, runners hébergés ou auto-hébergés, large marketplace d'actions."
categorie: devops/ci
famille: saas
licence_type: proprietary
hosted: [self, managed]
maturite: production
langage: 
scaling: serverless
alternatives: ["[[GitLab CE]]", "[[Forgejo]]", "[[Jenkins]]", "[[Woodpecker CI]]"]
complements: ["[[Docker]]", "[[Argo CD]]", "[[Trivy]]", "[[Grype]]", "[[Gitleaks]]", "[[Semgrep]]"]
tags: [ci-cd]
url_docs: https://docs.github.com/actions
url_repo: https://github.com/actions/runner
---

# GitHub Actions

<!-- AUTO:BANDEAU:START -->
> CI/CD intégrée à GitHub : workflows YAML déclenchés sur événements du dépôt, runners hébergés ou auto-hébergés, large marketplace d'actions.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| SaaS | propriétaire | self-hébergé ou managé · serverless | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme de CI/CD intégrée à GitHub. Des **workflows** décrits en YAML dans
`.github/workflows/` se déclenchent sur des événements du dépôt — `push`,
`pull_request`, `schedule`, `workflow_dispatch` — et s'exécutent sur des **runners**,
machines éphémères hébergées par GitHub ou auto-hébergées. La force du modèle est la
proximité du code : rien à brancher quand le dépôt est déjà sur GitHub, et une marketplace
d'actions réutilisables (`actions/checkout`, `setup-python`, déploiements) évite de tout
réécrire. L'offre **sur site** existe : GitHub Enterprise Server (version 3.22 dans la documentation
lue le 2026-09-30) exécute Actions, mais uniquement sur des runners auto-hébergés ; le dépôt
`actions/actions-runner-controller` (ARC, Apache-2.0, environ 6 500 étoiles, dernière version
`gha-runner-scale-set-0.14.2` du 2026-05-22) les fait vivre sur Kubernetes. Relevé le 2026-09-30 : runner `actions/runner`
**v2.337.0** (2026-08-26), environ 6 300 étoiles, licence MIT. C'est aussi sa surface d'attaque, et elle est réelle : une action tierce
s'exécute avec les droits du workflow, donc elle s'épingle par **SHA** et non par un tag
mobile, et `GITHUB_TOKEN` se restreint par `permissions:` plutôt que laissé à son défaut.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Le code est déjà sur GitHub : CI/CD sans aucun outil externe à connecter | Code hébergé ailleurs, ou interdit chez GitHub : la CI de la forge interne ([[GitLab CE]], [[Forgejo]] avec [[Woodpecker CI]] ou Forgejo Actions) ou [[Jenkins]] ; le comparatif les départage : [[Comparatif - CI-CD auto-hébergé]] |
| Tests, lint, build d'images et déploiement automatisés sur chaque push ou pull request | Orchestration de pipelines data ou ML avec dépendances et reprises : un orchestrateur dédié (Airflow, Dagster) complète mieux qu'une CI |
| Tâches planifiées (`schedule`) ou déclenchées à la demande (`workflow_dispatch`) | Parc important de runners auto-hébergés : un frais de plateforme de 0,002 $/min a été annoncé le 2025-12-16 pour le 2026-03-01, reporté le lendemain « pour réévaluer l'approche » ; au 2026-09-30, aucune nouvelle date n'est publiée et la doc de facturation dit l'usage gratuit sur ces runners |
| Réutiliser des briques toutes faites de la marketplace plutôt que scripter depuis zéro | Dépôts privés à gros volume : le quota de minutes part vite sur des matrices de builds ou des runners gonflés — cacher les dépendances et borner les matrices |

## Mise en œuvre

- Installation — rien à installer si le dépôt est sur GitHub ; le runner (`actions/runner`) est open-source et s'auto-héberge. Sur GitHub Enterprise Server : Actions activé par l'administrateur, avec un stockage blob externe obligatoire (S3, Azure Blob, GCS, ou un MinIO compatible S3) et un minimum de 8 vCPU et 64 Go de RAM pour 740 runners connectés
- Point d'entrée — fichiers YAML dans `.github/workflows/`, déclenchés par événement de dépôt
- Prérequis — un dépôt GitHub. Les secrets passent par le magasin chiffré du dépôt ou de l'organisation, jamais en clair dans le YAML ; se méfier de `pull_request_target`, qui donne à une PR de fork le contexte du dépôt cible. Épingler les actions tierces par SHA — l'action `tj-actions/changed-files` a été compromise en mars 2025 (CVE-2025-30066, tags réécrits, secrets vidés dans les journaux, plus de 23 000 dépôts) ; un an plus tard, les tags de `aquasecurity/trivy-action` (76 sur 77) et de `setup-trivy` ont été réécrits vers des commits malveillants pendant une douzaine d'heures (2026-03-19, avis GHSA-69fq-xp46-6x23) : un scanner de sécurité est une action tierce comme une autre, exécutée avec les secrets du workflow, et Aqua précise que le badge « release immuable » ne suffit pas à empêcher le déplacement d'un tag — l'épinglage par SHA reste la protection ; la politique d'actions autorisées d'une organisation peut exiger cet épinglage depuis le 2025-08-15. Restreindre `permissions:` au strict nécessaire
- Exécution — managé, sur des runners éphémères hébergés par GitHub, ou sur des runners auto-hébergés ; sur un cluster Kubernetes, le contrôleur Actions Runner Controller (ARC) les fait vivre. La rétention des journaux, statuts et exécutions passe à 90 jours par défaut au 2026-10-01 (plus de 400 jours auparavant)
- Coût — gratuit sur les dépôts publics ; sur les dépôts privés, minutes incluses par mois : 2 000 (Free), 3 000 (Pro, Team), 50 000 (Enterprise Cloud), puis facturation à la minute — Linux 2 cœurs 0,006 $, Windows 2 cœurs 0,010 $, macOS 0,062 $. Baisse des tarifs des runners hébergés allant jusqu'à 39 % le 2026-01-01. Cache : 10 Go par dépôt, 0,07 $/Go/mois au-delà

## Écosystème

### Alternatives

- [[GitLab CE]] — Forge Git complète en édition Community (cœur MIT, dossier ee/ propriétaire) : dépôts, revues, CI/CD, registre de conteneurs et de paquets — lourde à exploiter (PostgreSQL, Redis, Gitaly, 8 vCPU et 16 Go conseillés) ; approbations obligatoires et SAST avancé réservés aux éditions payantes. — la forge complète hébergeable chez soi, cœur MIT ; approbations obligatoires et SAST avancé en éditions payantes.
- [[Forgejo]] — Forge Git légère issue du fork de Gitea (GPL-3.0-or-later depuis la v9, Go, gouvernance liée à l'association Codeberg e.V.) : dépôts, revues, registres de paquets et Forgejo Actions, dont la syntaxe s'inspire de celle de GitHub Actions sans en être une copie. — la forge légère dont les Actions reprennent la syntaxe de celles de GitHub, avec une compatibilité partielle.
- [[Jenkins]] — Serveur d'automatisation historique (MIT, Java) : pipelines en Jenkinsfile Groovy, agents permanents ou éphémères, plus de 2 000 plugins — mais chaque plugin est du code tiers à patcher, avec un avis de sécurité sur les plugins presque chaque mois. — le serveur de CI sans forge, plus de 2 000 plugins, à brancher sur des dépôts hébergés ailleurs.
- [[Woodpecker CI]] — CI légère pilotée par une forge (Apache-2.0, Go, fork de Drone 0.8) : chaque étape tourne dans un conteneur, environ 100 Mo de RAM pour le serveur, Forgejo, Gitea, GitLab, GitHub et Bitbucket comme forges — pas d'authentification propre, les comptes viennent de la forge. — la CI légère, une étape par conteneur, qui s'appuie sur une forge existante.

### Compléments

- [[Docker]] — Conteneurisation standard : packaging d'applications en images OCI reproductibles, isolées et portables d'un environnement à l'autre. — les images que les workflows construisent et publient
- [[Argo CD]] — Contrôleur GitOps pour Kubernetes : compare en continu un dépôt Git à l'état du cluster et le réconcilie (Apache-2.0, Go, CNCF diplômé). — le CD qui déploie ce que la CI a construit
- [[Trivy]] — Scanner tout-en-un d'Aqua Security (Apache-2.0, Go) : vulnérabilités, secrets, configurations IaC et licences d'une image, d'un dépôt, d'un système de fichiers ou d'un SBOM, avec génération CycloneDX et SPDX et une base miroitable hors ligne — mais sa release, ses actions GitHub et ses images Docker Hub ont été compromises du 2026-03-19 au 2026-03-23 (versions sûres publiées). — action officielle `aquasecurity/trivy-action`, dont 76 tags sur 77 ont été détournés le 2026-03-19 : à épingler par SHA, en versions sûres (≥ 0.35.0).
- [[Grype]] — Scanner de vulnérabilités d'Anchore (Apache-2.0, Go) pour images, répertoires et SBOM — il lit un SBOM produit par Syft et le compare à une base quotidienne de 18 sources, importable à la main pour un site isolé ; il ne cherche ni secrets ni configurations, et refuse de scanner avec une base de plus de 5 jours. — `anchore/scan-action` (et `anchore/sbom-action` pour le SBOM) ; son README recommande l'épinglage par SHA.
- [[Gitleaks]] — Détecteur de secrets dans un dépôt Git, un répertoire ou un flux (MIT, Go) : 222 règles par défaut en expressions régulières, entropie et mots-clés, hook pre-commit, aucune vérification en ligne — mais l'auteur l'a déclaré « complet », sans nouvelles fonctions, et travaille sur son successeur Betterleaks ; l'action GitHub officielle n'est pas en MIT. — `gitleaks/gitleaks-action` est sous licence à clé gratuite pour les comptes d'organisation ; appeler le binaire dans une étape évite la question.
- [[Semgrep]] — Analyse statique de code par motifs, en édition communautaire (moteur LGPL-2.1, Semgrep Inc.) : règles YAML, plus de 30 langages dont Python, sorties SARIF et JSON, utilisable hors ligne avec des règles locales — mais sans analyse entre fichiers ni entre fonctions, et avec des règles du registre sous une licence d'usage interne qui interdit de les redistribuer. — modèle de job dans un conteneur `semgrep/semgrep`, sans jeton ; l'ancienne `semgrep-action` est archivée.

## Ressources

- Documentation — https://docs.github.com/actions
- Dépôt — https://github.com/actions/runner

## Voir aussi

- [[DevOps]] — le hub du domaine
- [[Comparatif - CI-CD auto-hébergé]] — le comparatif : forge intégrée ou séparée, format de pipeline, licence.
- [[Pipelines CI-CD on-prem — runners, secrets et artefacts]] — la notion : runners éphémères, isolation, artefacts, réseau fermé.
