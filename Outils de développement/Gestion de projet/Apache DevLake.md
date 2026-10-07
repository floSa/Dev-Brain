---
role: brique
nom: Apache DevLake
alias: [DevLake, apache/devlake]
pitch: "Plateforme à héberger (Apache-2.0, Go) qui collecte les données dispersées des outils de développement — GitHub, GitLab, Jenkins, Jira, SonarQube — et les rend en tableaux de bord Grafana prêts à l'emploi, dont les mesures DORA, extensibles en SQL — mais elle n'a que des versions bêta, et se déploie avec Docker Compose ou Helm avec ses bases et son Grafana."
categorie: devtools/projet
famille: plateforme
domaines: [ai-eng, mlops]
licence_type: open-source
hosted: [self]
maturite: beta
langage: Go
scaling: single-node
alternatives: []
complements: ["[[ccusage]]"]
tags: [project-management, metrics, self-hosted]
url_docs: https://devlake.apache.org
url_repo: https://github.com/apache/devlake
---

# Apache DevLake

<!-- AUTO:BANDEAU:START -->
> Plateforme à héberger (Apache-2.0, Go) qui collecte les données dispersées des outils de développement — GitHub, GitLab, Jenkins, Jira, SonarQube — et les rend en tableaux de bord Grafana prêts à l'emploi, dont les mesures DORA, extensibles en SQL — mais elle n'a que des versions bêta, et se déploie avec Docker Compose ou Helm avec ses bases et son Grafana.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé · mono-nœud | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme de **données de développement**. Les informations d'un projet logiciel vivent dans des outils séparés (forge, CI, tickets, qualité de code) ; DevLake les **ingère, les relie et les affiche** pour mesurer le cycle de développement : des tableaux de bord prêts à l'emploi pour les mesures **DORA** (fréquence de déploiement, délai de livraison, taux d'échec, temps de rétablissement) et pour des rétrospectives Scrum, par exemple. On interagit surtout par les tableaux de bord **Grafana** intégrés ; deux démonstrations existent, pour responsables d'ingénierie et pour mainteneurs de logiciels libres.

L'usage suit cinq étapes décrites par le README : installer (Docker Compose, Helm, ou l'extension `gh-devlake` pour la CLI GitHub), créer un **blueprint** dans l'interface de configuration (connexions, périmètre, transformation, fréquence de collecte), suivre sa progression, lire les tableaux de bord, puis les adapter en SQL. La liste des sources prises en charge (GitHub, GitLab, Jenkins, Jira, SonarQube et d'autres) est sur le site. Licence Apache-2.0 lue dans le README et le dépôt ; toutes les versions publiées sont des bêtas (la dernière, v1.0.3-beta18, date du 2026-09-27) ; dépôt poussé le 2026-10-05.

**À savoir.** DevLake mesure des **équipes** et des **livraisons** à partir de leurs outils ; il ne lit pas les sessions d'agents. Pour le coût des agents, [[ccusage]] ; pour le temps humain, [[ActivityWatch]]. La notion [[Mesurer un projet - DORA, coût des agents et temps passé]] dit ce que ces chiffres valent et ce qu'ils ne mesurent pas.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Mesurer DORA et les cycles de livraison d'une équipe qui utilise GitHub, GitLab, Jenkins ou Jira | Un solo qui n'a pas d'équipe : les mesures DORA n'ont de sens qu'avec un flux de livraison suivi |
| Rassembler des outils dispersés dans un même entrepôt SQL, avec tableaux de bord Grafana déjà faits | Le coût ou le temps d'une session d'agent : [[ccusage]], [[Claude-Code-Usage-Monitor]] |
| Écrire ses propres mesures en SQL sur les données collectées | Une plateforme stable en version 1.0 : les versions publiées sont des bêtas |
| Un déploiement chez soi, dans un cluster (Helm) ou sur un poste (Compose) | Rien à héberger : un entrepôt, Grafana et des connecteurs sont à tenir |

## Mise en œuvre

- Installation — Docker Compose ou Helm, selon la documentation ; l'extension `gh-devlake` déploie aussi en local avec Docker ou sur Azure
- Point d'entrée — l'interface de configuration, où l'on crée un blueprint ; puis les tableaux de bord Grafana
- Prérequis — Docker ou Kubernetes ; accès aux outils à interroger (jetons, selon la source)
- Exécution — auto-hébergé, mono-nœud par défaut
- Coût — gratuit sous licence Apache-2.0

## Écosystème

### Alternatives

- Aucune alternative déclarée : aucune autre plateforme de mesure de livraison n'a de fiche dans le brain.

### Compléments

- [[ccusage]] — Outil en ligne de commande (MIT) qui lit les journaux locaux de 18 agents de code (Claude Code, Codex, OpenCode, Goose…) et en tire jetons et coût estimé par jour, semaine, mois ou session. — le coût des agents, à côté des mesures de livraison de DevLake.

## Ressources

- Documentation — https://devlake.apache.org
- Dépôt — https://github.com/apache/devlake

## Voir aussi

- [[Gestion de projet]] — le hub du sous-domaine
- [[Mesurer un projet - DORA, coût des agents et temps passé]] — la notion : DORA, coût des agents, temps passé, et les mauvaises mesures
- [[Grafana]] — l'outil qui affiche ses tableaux de bord
- [[Outils de développement]] — le hub du domaine
