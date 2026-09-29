---
role: brique
nom: OpenSearch
alias: [opensearch, aws opensearch]
pitch: "Moteur de recherche et d'analytique distribué (Apache-2.0) — fork d'Elasticsearch 7.10.2 : full-text, k-NN et recherche hybride, visualisé dans OpenSearch Dashboards."
categorie: database/recherche
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Java
scaling: distributed
alternatives: ["[[Elasticsearch]]", "[[Apache Solr]]"]
complements: []
tags: [search, distributed, hybrid-search, semantic-search]
url_docs: https://docs.opensearch.org/latest/
url_repo: https://github.com/opensearch-project/OpenSearch
---

# OpenSearch

<!-- AUTO:BANDEAU:START -->
> Moteur de recherche et d'analytique distribué (Apache-2.0) — fork d'Elasticsearch 7.10.2 : full-text, k-NN et recherche hybride, visualisé dans OpenSearch Dashboards.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Java | open-source | self-hébergé ou managé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Moteur de recherche et d'analytique distribué, issu d'un fork d'Elasticsearch 7.10.2 après
l'abandon par Elastic d'une licence open source. Il garde le modèle de son ancêtre : documents
JSON, API REST, [[Index inversé|index inversé]] par shard, agrégations sur les mêmes index. Il
s'y ajoute une couche vectorielle (requêtes k-NN et neuronales, cf.
[[Recherche vectorielle approximative]]) et une recherche hybride. L'interface de visualisation, OpenSearch
Dashboards, est livrée avec.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un moteur distribué de type Elasticsearch, sous une licence Apache-2.0 sans copyleft réseau | Gourmand en RAM : heap JVM plus cache du système de fichiers |
| Recherche plein texte, k-NN et hybride dans un même moteur | Quasi temps réel, jamais transactionnel : ne convient pas comme source de vérité |
| Logs et observabilité avec OpenSearch Dashboards, sans dépendre de l'éditeur Elastic | Le sur-sharding ou un mapping mal pensé dégradent durablement performances et stockage |
| Offre managée (Amazon OpenSearch Service, dont une variante serverless), en plus du self-host | |

## Mise en œuvre

- Installation — archive, paquet ou image Docker ; Amazon OpenSearch Service pour l'offre managée
- Point d'entrée — API REST HTTP sur le port 9200 ; OpenSearch Dashboards pour l'exploration
- Prérequis — une JVM et un heap dimensionné ; le mapping des index se conçoit avant l'indexation
- Exécution — self-hébergé ou managé, distribué : sharding pour le volume, réplicas pour la disponibilité
- Coût — gratuit, Apache-2.0 ; la dépense réelle est l'exploitation (JVM, heap, gestion des shards)

## Écosystème

### Alternatives

- [[Elasticsearch]] — Moteur de recherche et d'analytique distribué : indexation full-text et logs à grande échelle. — son ancêtre : OpenSearch en est le fork, à licence Apache-2.0.
- [[Apache Solr]] — Plateforme de recherche Apache (Apache-2.0) bâtie sur Lucene — full-text, vectoriel et géospatial, distribuée par SolrCloud (réplication, bascule automatique). — l'autre moteur Apache-2.0 distribué du dossier, sur Lucene sans passer par la lignée d'Elasticsearch.

### Compléments

- *Aucun complément déclaré.*

## Ressources

- Documentation — https://docs.opensearch.org/latest/
- Dépôt — https://github.com/opensearch-project/OpenSearch

## Voir aussi

- [[Recherche]] — le hub du dossier
- [[Index inversé]] — la structure sur laquelle tout moteur de ce dossier repose
- [[Recherche vectorielle approximative]] — comment le k-NN s'y exécute
- [[Hybrid retrieval]] — combiner BM25 et kNN dans la même requête
- [[Comparatif - Moteurs de recherche]] — ce qui départage les moteurs du dossier
