---
role: brique
nom: Netdata
alias: [netdata, "Netdata Agent"]
pitch: "Agent de supervision temps réel (GPLv3+, Go, C, Rust) — métriques à la seconde d'hôtes, conteneurs et applications sans configuration, tableau de bord local sur le port 19999, alertes locales ; interface sous licence propriétaire NCUL1, Netdata Cloud optionnel."
categorie: observability/supervision
famille: application
licence_type: open-core
hosted: [self, managed]
maturite: production
langage: "Go, C, Rust"
scaling: distributed
alternatives: ["[[Beszel]]", "[[Zabbix]]"]
complements: []
tags: [observability, metrics, alerting, dashboard, self-hosted]
url_docs: https://learn.netdata.cloud/docs/netdata-agent/
url_repo: https://github.com/netdata/netdata
---

# Netdata

<!-- AUTO:BANDEAU:START -->
> Agent de supervision temps réel (GPLv3+, Go, C, Rust) — métriques à la seconde d'hôtes, conteneurs et applications sans configuration, tableau de bord local sur le port 19999, alertes locales ; interface sous licence propriétaire NCUL1, Netdata Cloud optionnel.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application Go, C, Rust | open-core | self-hébergé ou managé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Supervision d'hôtes conçue pour le temps réel et la configuration nulle. Un **Agent** collecte des métriques
à la seconde sur les systèmes, les conteneurs, les applications, les VM et le matériel — plus de 800
applications packagées — et sert son propre tableau de bord, sur le port 19999. L'architecture est dite
*edge* : le code va aux données, pas l'inverse. Un Agent gère ses alertes seul ; des **Parents**
centralisent au besoin, et **Netdata Cloud**, optionnel, unifie l'accès en interrogeant les Agents en temps
réel, sans rapatrier les données. Le point à connaître est la licence, à trois étages : l'Agent est en
GPLv3+, l'interface du tableau de bord en NCUL1 — propriétaire, gratuite à l'usage —, et le Cloud est
fermé, gratuit et payant. Ce mélange fait de l'Agent une brique ouverte dans un ensemble qui ne l'est pas tout entier.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Voir une machine en direct, à la seconde, sans configurer des exporters ni des sources | Licence 100 % libre exigée, de l'interface aux alertes : le tableau de bord est sous licence propriétaire NCUL1 → [[Prometheus]] avec [[Grafana]] |
| Garder les données sur site : chaque Agent stocke chez lui, avec une rétention par paliers à la seconde, à la minute et à l'heure | Contrôle d'accès, gestion d'utilisateurs, RBAC : ces fonctions sont celles de Netdata Cloud, fermé |
| Alertes locales par machine, sans serveur central obligatoire | Supervision d'un parc hétérogène avec modèles réutilisables, déclencheurs et rapports intégrés → [[Zabbix]] |

## Mise en œuvre

- Installation — installation simple et configuration nulle, d'après la documentation
- Point d'entrée — le tableau de bord local de chaque Agent, port 19999
- Prérequis — pour une vue unifiée, des Parents ou Netdata Cloud ; sans eux, un tableau de bord et des alertes par machine, à surveiller séparément ; disque à dimensionner, la rétention suivant l'espace disponible, ou mode RAM sans écriture disque
- Exécution — Agent auto-hébergé, Parents pour centraliser, Cloud optionnel ; Linux, FreeBSD, macOS et Windows avec un support inégal selon la plateforme
- Coût — Agent gratuit, GPLv3+ ; interface sous NCUL1, gratuite ; Netdata Cloud gratuit et payant

## Écosystème

### Alternatives

- [[Beszel]] — Hub de supervision de serveurs léger (Go, MIT) : CPU, mémoire, disque, réseau, température, statistiques des conteneurs Docker, historique et alertes, en architecture hub + agents. — la version minimale : un hub et un agent par hôte, sans pile à configurer.
- [[Zabbix]] — Plateforme de supervision distribuée d'entreprise (AGPL-3.0 depuis la 7.0, C, PHP, Go) — serveur, agents actifs ou passifs, collecte sans agent (SNMP, IPMI), modèles, déclencheurs et tableaux de bord sur MySQL, MariaDB ou PostgreSQL ; proxies pour les sites distants. — l'autre grand outil de supervision d'hôtes, orienté parc d'entreprise, sur serveur et base à opérer.

### Compléments

- *Aucun complément déclaré.*

## Ressources

- Documentation — https://learn.netdata.cloud/docs/netdata-agent/
- Dépôt — https://github.com/netdata/netdata

## Voir aussi

- [[Observabilité]] — le hub du domaine
