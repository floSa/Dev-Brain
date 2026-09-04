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
alternatives: ["[[Vespa]]", "[[txtai]]", "[[Marqo]]"]
complements: []
tags: [search, distributed]
url_docs: https://www.elastic.co/guide/index.html
url_repo: https://github.com/elastic/elasticsearch
---

# Elasticsearch

<!-- AUTO:BANDEAU:START -->
> Moteur de recherche et d'analytique distribué : indexation full-text et logs à grande échelle.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme Java | open-source | self-hébergé ou managé · distribué | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Moteur de recherche et d'analytique bâti sur Apache Lucene. Il indexe des documents JSON et
offre la recherche **plein texte** avec scoring de pertinence BM25, des agrégations sur les
mêmes index, et un fonctionnement **quasi temps réel** — un document devient interrogeable au
prochain refresh, pas à l'`INSERT`. La distribution se fait par sharding pour le volume et
réplication pour la disponibilité. C'est le cœur de la suite Elastic, avec Kibana pour la
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

## Ressources

- Documentation — https://www.elastic.co/guide/index.html
- Dépôt — https://github.com/elastic/elasticsearch

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[Recherche d'information]] — recherche lexicale (BM25) et, désormais, dense (kNN)
- [[Hybrid retrieval]] — combiner BM25 et kNN dans la même requête
- [[Comparatif - Moteurs de recherche]] — ce qui départage les moteurs du dossier
