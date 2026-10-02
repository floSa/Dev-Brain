---
role: brique
nom: Seeq
alias: [Seeq Corporation, Seeq Workbench, Seeq Server]
pitch: "Application d'analyse en libre-service de séries temporelles de procédé — se branche sur des historiens dont PI System, sans copier les données ; installable sur site ou en cloud, propriétaire."
categorie: data/bi
famille: application
licence_type: proprietary
hosted: [self, managed]
maturite: production
langage: 
alternatives: []
complements: ["[[AVEVA PI System]]"]
tags: [timeseries, predictive-maintenance, iiot, dashboard]
url_docs: https://support.seeq.com/
url_repo: 
---

# Seeq

<!-- AUTO:BANDEAU:START -->
> Application d'analyse en libre-service de séries temporelles de procédé — se branche sur des historiens dont PI System, sans copier les données ; installable sur site ou en cloud, propriétaire.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application | propriétaire | self-hébergé ou managé | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Application web d'analyse, destinée aux ingénieurs de procédé et de fiabilité plutôt qu'aux
développeurs : la base de connaissances de l'éditeur la décrit comme « a self-service
analytics application ». Elle se connecte aux données là où elles sont — historiens (PI,
Ignition, DeltaV, Ovation, Proficy, PHD, IP.21…), lacs de données, bases SQL — sans les
copier ni les déplacer, d'après la documentation commerciale ; les connecteurs de systèmes
usuels sont inclus dans la licence. L'utilisateur nettoie, rapproche et annote les signaux
dans l'interface, puis publie des analyses. Seeq propose aussi **Data Lab**, un espace de
notebooks Python, et met en avant la surveillance d'état (santé de pompes et de vannes,
détection précoce de dérive de capteurs sur turbines à gaz). L'éditeur se présente comme une
« plateforme d'IA industrielle ». Vendu sur contrat.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Le site a déjà un historien et des ingénieurs de fiabilité qui veulent explorer les signaux sans écrire de code ni monter de copie des données | Un modèle de maintenance entraîné et versionné dans une chaîne de ML : Seeq est un outil d'analyse en libre-service, le cycle de vie du modèle se tient ailleurs → [[Indicateurs de santé]], [[Politique de maintenance et coût]] |
| Analyse sur site : l'installation Seeq Server est documentée sur une machine physique ou virtuelle, avec une base PostgreSQL embarquée | Dimensionnement : le serveur demande de 8 cœurs et 32 Go de RAM pour 1 à 10 utilisateurs jusqu'à 128 cœurs et 1 To pour plus de 800, disques SSD ; Data Lab exige son propre serveur sous Linux (Docker) |
| Prototyper vite des indicateurs d'état avant de les industrialiser | Pas d'offre libre : propriétaire, licence sur contrat (aucun tarif relevé) ; pour une BI générique sur un entrepôt → [[Metabase]], [[Apache Superset]] |
| Garder la donnée à sa source (pas de pipeline de copie) | Aucun historien ni base derrière : l'outil analyse des données qui existent déjà ailleurs → [[InfluxDB]] ou [[TimescaleDB]] à poser d'abord |

## Mise en œuvre

- Installation — Seeq Server sur machine physique ou virtuelle (Ubuntu LTS ou RHEL 64 bits d'après la documentation d'installation) ; ou service cloud de l'éditeur
- Point d'entrée — interface web (Workbench) ; notebooks Python dans Data Lab
- Prérequis — l'accès réseau aux historiens ou bases à relier ; un serveur dédié pour Data Lab, à part de Seeq Server ; Docker pour Data Lab
- Exécution — sur site ou managé ; le serveur embarque Java, PostgreSQL, Nginx, Node.js et Chromium
- Coût — propriétaire, licence sur contrat ; aucun tarif relevé

## Écosystème

### Compléments

- [[AVEVA PI System]] — Historien industriel d'AVEVA — PI Data Archive stocke les séries temporelles de l'atelier, PI Asset Framework les rattache à une hiérarchie d'équipements, PI Vision les affiche ; propriétaire, installé sur site (datasheet : Windows) ; un historien, pas un outil de machine learning.

## Ressources

- Documentation — https://support.seeq.com/

## Voir aussi

- [[Data & pipelines]] — le hub du domaine
- [[Comparatif - BI auto-hébergée]] — ce qui départage les outils de BI du dossier
- [[Données industrielles]] — la chaîne qui amène la donnée d'atelier jusqu'à l'historien
- [[Surveillance conditionnelle et modes de défaillance]] — l'usage dont il fait un argument
- [[Indicateurs de santé]] — ce qu'on y construit par signal
- [[Comparatif - Offres de maintenance prédictive]] — ce qui départage les offres, dont l'auto-hébergement
