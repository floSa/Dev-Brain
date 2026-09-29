---
role: brique
nom: Beats
alias: [beats, elastic beats, filebeat, metricbeat]
pitch: "Agents de collecte légers en Go (Apache-2.0, x-pack sous Elastic License) — Filebeat, Metricbeat, Auditbeat… expédient logs et métriques vers Elasticsearch ou Logstash."
categorie: data/ingestion
famille: cli
licence_type: open-core
maturite: production
langage: Go
alternatives: []
complements: ["[[Elasticsearch]]", "[[Logstash]]"]
tags: [logging, data-pipeline]
url_docs: https://www.elastic.co/docs/get-started
url_repo: https://github.com/elastic/beats
---

# Beats

<!-- AUTO:BANDEAU:START -->
> Agents de collecte légers en Go (Apache-2.0, x-pack sous Elastic License) — Filebeat, Metricbeat, Auditbeat… expédient logs et métriques vers Elasticsearch ou Logstash.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Go | open-core | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Famille d'agents de collecte légers, en Go, installés sur les machines sources pour capturer
des données opérationnelles. Sept Beats sont officiels : Filebeat (fichiers de logs et
journaux), Metricbeat (métriques système et de services), Auditbeat (audit Linux et intégrité
de fichiers), Heartbeat (disponibilité de services distants), Packetbeat (trafic réseau),
Winlogbeat (journaux Windows) et Osquerybeat. Ils envoient leurs données à
[[Elasticsearch]] directement, ou via [[Logstash]] pour un traitement intermédiaire. La
bibliothèque libbeat permet d'écrire ses propres Beats. Le code est sous Apache-2.0, le dossier
`x-pack` sous Elastic License.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Expédier logs et métriques depuis des serveurs, avec un agent léger sans JVM | Transformations complexes des événements avant l'indexation : c'est le rôle de [[Logstash]] |
| Alimenter directement [[Elasticsearch]] depuis les machines sources | Une destination autre que la pile Elastic : ces agents sont conçus pour elle |
| Un agent par sujet : fichiers, métriques, réseau, audit, disponibilité | Des fonctions `x-pack` en Elastic License : à qualifier avant usage commercial |

## Mise en œuvre

- Installation — binaire, paquet ou image Docker, sur chaque machine à observer
- Point d'entrée — un binaire par Beat (`filebeat`, `metricbeat`…) configuré par un fichier YAML
- Prérequis — une destination joignable : Elasticsearch, ou Logstash pour un traitement préalable
- Exécution — sur les machines sources, un agent par Beat
- Coût — gratuit, Apache-2.0 ; les fonctions `x-pack` relèvent de l'Elastic License

## Écosystème

### Alternatives

- *Aucune alternative déclarée : aucun autre collecteur n'est fiché dans `data/ingestion`.*

### Compléments

- [[Elasticsearch]] — Moteur de recherche et d'analytique distribué : indexation full-text et logs à grande échelle. — la destination directe des données collectées.
- [[Logstash]] — Pipeline de collecte et de transformation de données côté serveur (Apache-2.0, x-pack sous Elastic License) — plugins d'entrée, de filtre et de sortie ; alimente Elasticsearch ou tout autre destinataire. — l'étage de transformation, quand l'agent seul ne suffit pas.

## Ressources

- Documentation — https://www.elastic.co/docs/get-started
- Dépôt — https://github.com/elastic/beats

## Voir aussi

- [[Data & pipelines]] — le hub du domaine
- [[Kibana]] — l'interface qui visualise les données collectées
- [[Loki]] — voisin côté logs, avec son propre agent de collecte
