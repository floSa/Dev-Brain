---
role: brique
nom: Kibana
alias: [kibana, elastic kibana]
pitch: "Interface web de la suite Elastic (triple AGPL / SSPL / ELv2) — explore (Discover), visualise (Lens, dashboards) et alerte sur les données d'Elasticsearch ; ne fonctionne qu'avec lui."
categorie: observability/supervision
famille: application
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: TypeScript
alternatives: ["[[Grafana]]"]
complements: ["[[Elasticsearch]]"]
tags: [observability, logging, dashboard]
url_docs: https://www.elastic.co/docs/get-started
url_repo: https://github.com/elastic/kibana
---

# Kibana

<!-- AUTO:BANDEAU:START -->
> Interface web de la suite Elastic (triple AGPL / SSPL / ELv2) — explore (Discover), visualise (Lens, dashboards) et alerte sur les données d'Elasticsearch ; ne fonctionne qu'avec lui.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application TypeScript | open-source | self-hébergé ou managé | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Interface web de la suite Elastic, en TypeScript. Elle ne stocke aucune donnée : elle interroge
[[Elasticsearch]] et met ses résultats en forme. Discover explore et filtre les documents bruts,
Lens construit des graphiques par glisser-déposer, les dashboards les assemblent, Maps traite le
géospatial et l'alerting notifie sur les événements. C'est aussi la console d'où l'on envoie
des requêtes à l'API d'Elasticsearch. Le code est sous triple licence AGPL-3.0, SSPL et
Elastic License 2.0, le dossier `x-pack` sous Elastic License 2.0 seule.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Explorer et visualiser des logs ou des documents déjà dans Elasticsearch | Aucune instance d'Elasticsearch : Kibana ne fonctionne pas sans lui |
| Console d'administration et de requêtes de la pile Elastic | Le dossier `x-pack` est sous Elastic License 2.0 seule : à qualifier avant tout usage commercial ou redistribution |
| Alerting et exploration ad hoc sur les mêmes index | Tableaux de bord sur des sources hétérogènes : Kibana ne lit qu'Elasticsearch |

## Mise en œuvre

- Installation — archive, paquet ou image Docker ; inclus dans Elastic Cloud
- Point d'entrée — application web sur le port 5601
- Prérequis — une instance d'Elasticsearch, de la même version que Kibana sur toute la pile
- Exécution — auto-hébergé ou managé
- Coût — triple licence AGPL / SSPL / ELv2 ; la dépense réelle est celle d'Elasticsearch derrière

## Écosystème

### Alternatives

- [[Grafana]] — Plateforme open-source de dashboards et d'observabilité (AGPL-3.0) — visualise métriques, logs et traces depuis 150+ sources (Prometheus, Loki, InfluxDB, Postgres…) ; alerting intégré, self-host ou Grafana Cloud. — multi-sources, quand Kibana est limité à Elasticsearch.

### Compléments

- [[Elasticsearch]] — Moteur de recherche et d'analytique distribué : indexation full-text et logs à grande échelle. — le seul magasin de données que Kibana lit.

## Ressources

- Documentation — https://www.elastic.co/docs/get-started
- Dépôt — https://github.com/elastic/kibana

## Voir aussi

- [[Observabilité]] — le hub du domaine
- [[Logstash]] — le pipeline qui alimente Elasticsearch
- [[Beats]] — les agents qui expédient logs et métriques
- [[Loki]] — voisin côté logs, qui n'indexe que des labels
- [[Journalisation structurée et traçabilité]] — la notion : événements structurés, contexte, corrélation avec les traces, ce qu'il ne faut pas journaliser
