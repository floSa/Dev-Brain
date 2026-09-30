---
role: brique
nom: Logstash
alias: [logstash, elastic logstash]
pitch: "Pipeline de collecte et de transformation de données côté serveur (Apache-2.0, x-pack sous Elastic License) — plugins d'entrée, de filtre et de sortie ; alimente Elasticsearch ou tout autre destinataire."
categorie: data/ingestion
famille: plateforme
licence_type: open-core
hosted: [self]
maturite: production
langage: Java
scaling: distributed
alternatives: ["[[Apache NiFi]]"]
complements: ["[[Elasticsearch]]", "[[Beats]]"]
tags: [logging, data-pipeline]
url_docs: https://www.elastic.co/docs/get-started
url_repo: https://github.com/elastic/logstash
---

# Logstash

<!-- AUTO:BANDEAU:START -->
> Pipeline de collecte et de transformation de données côté serveur (Apache-2.0, x-pack sous Elastic License) — plugins d'entrée, de filtre et de sortie ; alimente Elasticsearch ou tout autre destinataire.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Java | open-core | self-hébergé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Pipeline de traitement de données côté serveur : il ingère des sources multiples en parallèle,
les transforme et les envoie vers une destination. L'architecture se compose de plugins
d'entrée, de filtre et de sortie, avec des codecs natifs, et il traite tout type d'événement,
pas seulement des logs. Le cœur est écrit en Java et en Ruby, exécuté sur JRuby. Le code est
sous Apache-2.0 hors du dossier `x-pack`, qui est sous Elastic License ; les binaires `-oss`
n'embarquent que le code Apache-2.0.

Relevé le 2026-09-30 : **9.5.4** du 2026-09-15 (8.19.22 du 2026-09-23 sur la branche 8), environ 14 950
étoiles, dernier commit du jour. Le fichier `LICENSE.txt` du dépôt dit toujours Apache-2.0 hors `x-pack`, Elastic License dans `x-pack`, et
deux jeux de binaires ; les binaires `-oss` existent encore pour la 9.5.4 (vérifié le même jour). L'ajout de l'AGPLv3 d'août 2024
ne touche qu'Elasticsearch et Kibana, pas Logstash d'après la FAQ des licences d'Elastic, lue par résumé.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Normaliser et enrichir des événements hétérogènes avant de les indexer | Simple expédition de fichiers de logs sans transformation : les agents [[Beats]] suffisent |
| Un pipeline déclaratif d'entrées, de filtres et de sorties, avec un large catalogue de plugins | Une JVM par instance : plus lourd qu'un agent de collecte |
| Alimenter [[Elasticsearch]] avec l'API de sortie officielle, ou un autre destinataire | Des fonctions `x-pack` en Elastic License : à qualifier avant usage commercial |

## Mise en œuvre

- Installation — archive, paquet ou image Docker
- Point d'entrée — un fichier de pipeline déclarant les plugins d'entrée, de filtre et de sortie
- Prérequis — une JVM ; les plugins nécessaires installés
- Exécution — auto-hébergé, une instance ou plusieurs
- Coût — gratuit, Apache-2.0 ; les fonctions `x-pack` relèvent de l'Elastic License

## Écosystème

### Alternatives

- [[Apache NiFi]] — Plateforme de flux de données à interface graphique : des centaines de processeurs (fichiers, SFTP, JDBC, MQTT, syslog, Kafka…) reliés par des files avec contre-pression, provenance de chaque donnée et livraison garantie ; Apache-2.0, JVM, sans broker.

### Compléments

- [[Elasticsearch]] — Moteur de recherche et d'analytique distribué : indexation full-text et logs à grande échelle. — la destination de référence, via le plugin de sortie Elasticsearch.
- [[Beats]] — Agents de collecte légers en Go (Apache-2.0, x-pack sous Elastic License) — Filebeat, Metricbeat, Auditbeat… expédient logs et métriques vers Elasticsearch ou Logstash. — les agents en amont, qui lui envoient leurs événements.

## Ressources

- Documentation — https://www.elastic.co/docs/get-started
- Dépôt — https://github.com/elastic/logstash

## Voir aussi

- [[Ingestion de données]] — le hub du dossier
- [[Comparatif - Ingestion de données]] — Logstash y est situé face aux outils d'ingestion généralistes
- [[Kibana]] — l'interface qui visualise ce que Logstash a alimenté dans Elasticsearch
- [[Change Data Capture (CDC)]] — autre façon de produire un flux, depuis une base
