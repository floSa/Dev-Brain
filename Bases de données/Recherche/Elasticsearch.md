---
role: brique
nom: Elasticsearch
alias: [elasticsearch, elastic, es]
pitch: "Moteur de recherche et d'analytique distribué : indexation full-text et logs à grande échelle."
categorie: database/recherche
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Java
scaling: distributed
alternatives: ["[[Vespa]]", "[[txtai]]", "[[Marqo]]", "[[OpenSearch]]", "[[Meilisearch]]", "[[Typesense]]", "[[Apache Solr]]"]
complements: ["[[Kibana]]", "[[Logstash]]", "[[Beats]]", "[[JanusGraph]]", "[[OpenMetadata]]", "[[DataHub]]", "[[RAGFlow]]"]
tags: [search, distributed]
url_docs: https://www.elastic.co/guide/index.html
url_repo: https://github.com/elastic/elasticsearch
---

# Elasticsearch

<!-- AUTO:BANDEAU:START -->
> Moteur de recherche et d'analytique distribué : indexation full-text et logs à grande échelle.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Java | open-source | self-hébergé ou managé · distribué | production | à jour · 2026-09-03 |
<!-- AUTO:BANDEAU:END -->

## Définition

Moteur de recherche et d'analytique bâti sur [[Lucene]]. Il indexe des documents JSON et
offre la recherche **plein texte** avec scoring de pertinence BM25, des agrégations sur les
mêmes index, et un fonctionnement **quasi temps réel** — un document devient interrogeable au
prochain refresh, pas à l'`INSERT`. La distribution se fait par sharding pour le volume et
réplication pour la disponibilité. C'est le cœur de la suite Elastic, avec [[Kibana]] pour la
visualisation.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Recherche plein texte et pertinence (catalogue produit, recherche de site ou d'app) | Gourmand en RAM : heap JVM plus cache du système de fichiers |
| Centralisation et exploration de logs, observabilité (stack ELK) | Le sur-sharding ou un mapping mal pensé dégradent durablement performances et stockage |
| Agrégations analytiques sur données semi-structurées, dashboards Kibana | Quasi temps réel, jamais transactionnel : l'intervalle de refresh interdit d'en faire une source de vérité |
| Recherche quasi temps réel à grande échelle, sur un corpus qui dépasse un nœud | Recherche simple sur un corpus modeste : l'index plein texte de [[Postgres]] suffit souvent |
| | Analytique SQL sur gros volumes en colonnes → [[ClickHouse]] |

## Mise en œuvre

- Installation — archive, paquet ou image Docker ; managé via Elastic Cloud
- Point d'entrée — API REST HTTP sur le port 9200, documents JSON ; Kibana pour l'exploration et les dashboards
- Prérequis — une JVM et un heap dimensionné ; le mapping des index se conçoit avant l'indexation
- Exécution — self-hébergé ou managé, distribué : sharding pour le volume, réplicas pour la disponibilité et la lecture
- Coût — triple licence AGPLv3 / ELv2 / SSPL depuis 2024, binaires identiques ; la dépense réelle est l'exploitation (JVM, heap, gestion des shards)

## Écosystème

### Alternatives

- [[Vespa]] — Plateforme de recherche et de serving IA (Apache-2.0) — combine full-text, recherche vectorielle et ranking par modèles ML dans un même moteur distribué, à l'échelle du milliard de documents et sous 100 ms.
- [[txtai]] — Base d'embeddings tout-en-un en Python (Apache-2.0, NeuML) — recherche sémantique, SQL et graphe sur un même index, plus orchestration de workflows LLM ; du notebook embarqué à l'API FastAPI.
- [[Marqo]] — Moteur de recherche vectorielle end-to-end (Apache-2.0) qui gère lui-même l'inférence des embeddings texte et image via une seule API — projet open-source déprécié, pivoté vers une plateforme commerciale de recherche e-commerce.
- [[OpenSearch]] — Moteur de recherche et d'analytique distribué (Apache-2.0) — fork d'Elasticsearch 7.10.2 : full-text, k-NN et recherche hybride, visualisé dans OpenSearch Dashboards. — le fork Apache-2.0 : même modèle d'API, licence sans copyleft réseau.
- [[Meilisearch]] — Moteur de recherche instantané en Rust — full-text tolérant aux fautes de frappe, sémantique et hybride derrière une API REST ; édition communautaire MIT, sharding réservé à l'édition Enterprise. — pour une recherche de site ou d'application, plus simple à mettre en route qu'un cluster.
- [[Typesense]] — Moteur de recherche tolérant aux fautes de frappe (GPL-3.0, C++) — index en mémoire pour du search-as-you-type sous 50 ms, avec recherche vectorielle HNSW et hybride ; alternative ouverte à Algolia. — même cible que Meilisearch, index en mémoire.
- [[Apache Solr]] — Plateforme de recherche Apache (Apache-2.0) bâtie sur Lucene — full-text, vectoriel et géospatial, distribuée par SolrCloud (réplication, bascule automatique). — l'autre moteur distribué sur Lucene, sous Apache-2.0.

### Compléments

- [[Kibana]] — Interface web de la suite Elastic (triple AGPL / SSPL / ELv2) — explore (Discover), visualise (Lens, dashboards) et alerte sur les données d'Elasticsearch ; ne fonctionne qu'avec lui. — l'interface d'exploration et de dashboards de la pile Elastic.
- [[Logstash]] — Pipeline de collecte et de transformation de données côté serveur (Apache-2.0, x-pack sous Elastic License) — plugins d'entrée, de filtre et de sortie ; alimente Elasticsearch ou tout autre destinataire. — le pipeline qui transforme les événements avant l'indexation.
- [[Beats]] — Agents de collecte légers en Go (Apache-2.0, x-pack sous Elastic License) — Filebeat, Metricbeat, Auditbeat… expédient logs et métriques vers Elasticsearch ou Logstash. — les agents qui expédient logs et métriques depuis les machines sources.
- [[JanusGraph]] — Couche de graphe Java au-dessus de Cassandra, ScyllaDB ou HBase et d'un index Elasticsearch ou Solr (Apache-2.0, Linux Foundation) — Gremlin, milliards de sommets ; trois composants à opérer, et aucune version stable depuis novembre 2024. — la couche de graphe qui s'appuie sur Elasticsearch comme index externe pour la recherche par propriété.
- [[OpenMetadata]] — Catalogue de métadonnées open source : découverte, lignage table et colonne, glossaire, propriétaires, RBAC, tests de qualité et contrats de données sur plus de 130 connecteurs ; un serveur, une base SQL et un moteur de recherche à héberger (Apache-2.0, éditeur commercial Collate). — moteur de recherche obligatoire du serveur, en 9.x.
- [[DataHub]] — Catalogue de métadonnées open source né chez LinkedIn : lignage table et colonne, glossaire, domaines, propriétaires, contrats de données et politiques d'accès, alimenté par recettes d'ingestion ou par événements ; Kafka, une base SQL et un moteur de recherche à héberger (Apache-2.0, offre commerciale DataHub Cloud). — moteur de recherche du serveur, en 8.x ; l'index de graphe s'y appuie aussi.
- [[RAGFlow]] — Moteur RAG clé en main (Apache-2.0, InfiniFlow) — parsing de documents par mise en page (DeepDoc, OCR, tables), chunking par modèles, recherche hybride avec reranking, GraphRAG, agents et serveur MCP ; lourd : un moteur de documents, MySQL, MinIO et un cache.

## Ressources

- Documentation — https://www.elastic.co/guide/index.html
- Dépôt — https://github.com/elastic/elasticsearch

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[Recherche d'information]] — recherche lexicale (BM25) et, désormais, dense (kNN)
- [[Hybrid retrieval]] — combiner BM25 et kNN dans la même requête
- [[Index inversé]] — la structure sur laquelle repose la recherche plein texte
- [[Recherche vectorielle approximative]] — le kNN approximatif dans le moteur
- [[Recherche sémantique]] — chercher par le sens
- [[Comparatif - Moteurs de recherche]] — ce qui départage les moteurs du dossier
