---
role: brique
nom: Grafana
alias: [grafana]
pitch: "Plateforme open-source de dashboards et d'observabilité (AGPL-3.0) — visualise métriques, logs et traces depuis 150+ sources (Prometheus, Loki, InfluxDB, Postgres…) ; alerting intégré, self-host ou Grafana Cloud."
categorie: observability/supervision
famille: application
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Go
scaling: distributed
alternatives: []
complements: ["[[Loki]]"]
tags: [observability, metrics, dashboard, dataviz]
url_docs: https://grafana.com/docs/grafana/latest/
url_repo: https://github.com/grafana/grafana
---

# Grafana

<!-- AUTO:BANDEAU:START -->
> Plateforme open-source de dashboards et d'observabilité (AGPL-3.0) — visualise métriques, logs et traces depuis 150+ sources (Prometheus, Loki, InfluxDB, Postgres…) ; alerting intégré, self-host ou Grafana Cloud.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application Go | open-source | self-hébergé ou managé · distribué | production | à jour · 2026-09-02 |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme de dashboards et d'observabilité éditée par Grafana Labs, backend en Go et
front en React/TypeScript. Sa particularité est de **ne rien stocker** : elle se branche
sur plus de 150 sources — Prometheus, Loki, InfluxDB, Elasticsearch, Postgres — et met
métriques, logs et traces sur les mêmes tableaux de bord, avec exploration ad hoc et
alerting intégré. Cette composabilité est aussi sa contrainte : la source de données est
un composant à choisir, à déployer et à exploiter séparément, et Grafana ne dispense
d'aucun de ces trois travaux. Le projet est passé d'Apache 2.0 à AGPL-3.0-only en 2021,
un copyleft **réseau** dont les obligations se déclenchent à l'exposition, pas à la
distribution.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Tableaux de bord unifiés au-dessus de plusieurs sources hétérogènes — métriques, logs, traces | Stocker les métriques : Grafana ne stocke rien, il faut une base derrière (Prometheus, Mimir, [[InfluxDB]]) et l'opérer |
| Visualiser des métriques Prometheus ou des logs LogQL, avec alerting sur les mêmes requêtes | Simple application data interactive en Python — formulaires, démo de modèle → [[Streamlit]], [[Dash]] |
| Corréler une métrique et un log dans le même écran, sans changer d'outil | Intégrer et exposer Grafana dans un produit : l'AGPL-3.0 est un copyleft réseau, à faire qualifier avant de s'engager |
| Centraliser la supervision d'une infra ou d'une stack data sur un outil ouvert et auto-hébergeable | Reporting planifié ou RBAC fin attendus d'emblée : ces fonctions sont réservées à l'édition Enterprise |

## Mise en œuvre

- Installation — binaire Go unique, image Docker ou paquet système ; Grafana Cloud pour l'offre managée
- Point d'entrée — application web sur le port 3000 par défaut ; sources et dashboards provisionnables par fichiers YAML
- Prérequis — au moins une source de données exploitée à part (Prometheus ou Mimir, Loki, InfluxDB) ; base SQLite embarquée, ou Postgres/MySQL partagée dès qu'on veut plusieurs instances
- Exécution — auto-hébergé ou managé ; haute disponibilité par plusieurs instances derrière un répartiteur, sur base partagée
- Coût — cœur AGPL-3.0-only gratuit ; édition Enterprise commerciale (reporting, RBAC fin, plugins sous clé) ; Grafana Cloud facturé à l'usage

## Écosystème

### Alternatives

- *Aucune alternative déclarée : la catégorie `observability/supervision` n'a pas encore de second outil de visualisation fiché.*

### Compléments

- [[Loki]] — Système open-source d'agrégation de logs (AGPLv3) inspiré de Prometheus — indexe des labels plutôt que le contenu, stocke des chunks compressés sur object store ; horizontalement scalable, requêté en LogQL et visualisé dans Grafana. — même éditeur, LogQL exploré depuis les mêmes tableaux de bord que les métriques

## Ressources

- Documentation — https://grafana.com/docs/grafana/latest/
- Dépôt — https://github.com/grafana/grafana

## Voir aussi

- [[Observabilité]] — le hub du domaine
- [[Beszel]] — l'échelon en dessous : l'état des hôtes sans pile à opérer
