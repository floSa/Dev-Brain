---
role: brique
nom: Zabbix
alias: [zabbix]
pitch: "Plateforme de supervision distribuée d'entreprise (AGPL-3.0 depuis la 7.0, C, PHP, Go) — serveur, agents actifs ou passifs, collecte sans agent (SNMP, IPMI), modèles, déclencheurs et tableaux de bord sur MySQL, MariaDB ou PostgreSQL ; proxies pour les sites distants."
categorie: observability/supervision
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: "C, PHP, Go"
scaling: distributed
alternatives: ["[[Netdata]]", "[[Prometheus]]"]
complements: []
tags: [observability, metrics, alerting, dashboard, self-hosted]
url_docs: https://www.zabbix.com/documentation/current/en/manual/introduction/about
url_repo: https://github.com/zabbix/zabbix
---

# Zabbix

<!-- AUTO:BANDEAU:START -->
> Plateforme de supervision distribuée d'entreprise (AGPL-3.0 depuis la 7.0, C, PHP, Go) — serveur, agents actifs ou passifs, collecte sans agent (SNMP, IPMI), modèles, déclencheurs et tableaux de bord sur MySQL, MariaDB ou PostgreSQL ; proxies pour les sites distants.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme C, PHP, Go | open-source | self-hébergé ou managé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Solution de supervision distribuée « de classe entreprise » : elle surveille serveurs, machines
virtuelles, applications, services, bases de données, sites web et cloud, avec des notifications, des
rapports et des tableaux de bord intégrés. Un **serveur** en C interroge et reçoit les données, évalue les
déclencheurs et envoie les notifications ; une **base** MySQL, MariaDB ou PostgreSQL les stocke ; un
frontal web en PHP les présente ; des **agents** (l'Agent 2 est écrit en Go) collectent sur les hôtes, en
mode actif ou passif, et des **proxies** relaient les sites distants. Des contrôles **sans agent** — SNMP,
IPMI — évitent d'installer quoi que ce soit sur les équipements réseau. La licence a changé : GPLv2 jusqu'à
la 6.4, AGPLv3 à partir de la 7.0.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un parc hétérogène — serveurs, machines virtuelles, réseau, bases, sites web — sous un seul outil | Une poignée de machines sans exploitant dédié : serveur, base et frontal PHP à opérer, avec un dimensionnement « petit » de 2 cœurs et 8 Gio pour 1 000 métriques dans la documentation 7.4 → [[Beszel]] |
| Surveiller du matériel réseau sans agent, par SNMP ou IPMI | Livrable qui embarque Zabbix : AGPLv3 depuis la 7.0, alors que les versions jusqu'à la 6.4 étaient en GPLv2 ; à requalifier |
| Sites distants ou multi-sites, reliés par des proxies | Séries à labels, requêtes dimensionnelles et instrumentation applicative → [[Prometheus]] |
| Modèles réutilisables, déclencheurs et notifications intégrées, avec support commercial disponible | |

## Mise en œuvre

- Installation — paquets par plateforme ; serveur en C, frontal en PHP 8.0 à 8.5 sur Apache 2.4 ou Nginx 1.20 minimum, agent ou Agent 2 sur les hôtes, version 7.4 courante et 8.0 en développement d'après la documentation
- Point d'entrée — interface web du frontal ; contrôles passifs (le serveur interroge) ou actifs (l'agent pousse) ; SNMP et IPMI sans agent
- Prérequis — une base : MySQL 8.0.30 ou plus, MariaDB 10.5 ou plus, PostgreSQL 13 ou plus, ou TimescaleDB 2.13 ou plus ; SQLite pour les seuls proxies ; Elasticsearch 7 en stockage d'historique expérimental
- Exécution — auto-hébergé, avec des proxies pour les sites distants, ou Zabbix Cloud pour le managé
- Coût — gratuit, AGPL-3.0 depuis la 7.0 ; support technique commercial payant ; Zabbix Cloud en plusieurs paliers de prix

## Écosystème

### Alternatives

- [[Netdata]] — Agent de supervision temps réel (GPLv3+, Go, C, Rust) — métriques à la seconde d'hôtes, conteneurs et applications sans configuration, tableau de bord local sur le port 19999, alertes locales ; interface sous licence propriétaire NCUL1, Netdata Cloud optionnel. — plus simple à démarrer — configuration nulle, métriques à la seconde — sans base à opérer ni serveur central obligatoire.
- [[Prometheus]] — Système de supervision et base de séries temporelles open-source (Apache-2.0, Go) — scrape les métriques exposées en HTTP, modèle de données à labels, requêtes PromQL, règles d'alerte transmises à Alertmanager ; stockage local mono-nœud, sans cluster natif. — la pile ouverte par composants, plutôt qu'un outil qui embarque tout.

### Compléments

- *Aucun complément déclaré.*

## Ressources

- Documentation — https://www.zabbix.com/documentation/current/en/manual/introduction/about
- Dépôt — https://github.com/zabbix/zabbix
- Documentation — https://www.zabbix.com/license

## Voir aussi

- [[Observabilité]] — le hub du domaine
- [[SLO et alerting]] — la notion : un déclencheur Zabbix est une règle d'alerte, à juger sur le symptôme
