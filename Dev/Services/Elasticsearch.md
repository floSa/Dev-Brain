---
galaxie: dev
type: service
nom: Elasticsearch
alias: [elasticsearch, elastic, es]
pitch: "Moteur de recherche et d'analytique distribué : indexation full-text et logs à grande échelle."
categorie: database/search
licence_type: open-source
hosted: both
maturite: production
langage: Java
scaling: distributed
alternatives: ["[[Dev/Services/Vespa|Vespa]]", "[[Dev/Services/txtai|txtai]]", "[[Dev/Services/Marqo|Marqo]]"]
remplace_par: []
status: actif
tags: [search, distributed]
url_docs: https://www.elastic.co/guide/index.html
url_repo: https://github.com/elastic/elasticsearch
---

# Elasticsearch

## Pourquoi

Moteur de **recherche et d'analytique distribué** bâti sur Apache Lucene. Indexe des documents JSON et offre la recherche **plein texte** avec scoring de pertinence (BM25), des agrégations et un fonctionnement **quasi temps réel**. Cœur de la suite Elastic (avec Kibana pour la visualisation). Distribué par sharding et réplication. Depuis septembre 2024, le code est de nouveau **open-source** sous AGPLv3, en plus des licences SSPL et Elastic License (ELv2).

## Quand l'utiliser

- Recherche plein texte et pertinence (catalogue produit, recherche de site ou d'app).
- Centralisation et exploration de logs, observabilité (stack ELK).
- Agrégations analytiques sur données semi-structurées, dashboards Kibana.
- Recherche quasi temps réel à grande échelle.

## Quand NE PAS l'utiliser

- Source de vérité transactionnelle ACID → [[Dev/Services/Postgres|Postgres]] (Elasticsearch n'est pas une base primaire).
- Analytique SQL pure sur gros volumes colonnes → [[Dev/Services/ClickHouse|ClickHouse]].
- Besoin de recherche simple : l'index plein texte de [[Dev/Services/Postgres|Postgres]] suffit souvent.

## Déploiement & coût

- Self-host (cluster JVM) ou managé (Elastic Cloud).
- Scaling distribué : sharding pour le volume, réplicas pour la disponibilité et la lecture.
- Triple licence AGPLv3 / ELv2 / SSPL ; binaires inchangés. Le coût réel est l'exploitation (JVM, heap, gestion des shards).

## Pièges

- Gourmand en RAM : heap JVM plus cache du système de fichiers.
- Sur-sharding ou mapping mal pensé dégradent perfs et stockage.
- Quasi temps réel (intervalle de refresh) : ce n'est pas une base transactionnelle.
- Retours d'expérience détaillés : `Dev/REX/REX - Elasticsearch.md`.

## Alternatives

- [[Dev/Services/Vespa|Vespa]] — Plateforme de recherche et de serving IA (Apache-2.0) — combine full-text, recherche vectorielle et ranking par modèles ML dans un même moteur distribué, à l'échelle du milliard de documents et sous 100 ms.
- [[Dev/Services/txtai|txtai]] — Base d'embeddings tout-en-un en Python (Apache-2.0, NeuML) — recherche sémantique, SQL et graphe sur un même index, plus orchestration de workflows LLM ; du notebook embarqué à l'API FastAPI.
- [[Dev/Services/Marqo|Marqo]] — Moteur de recherche vectorielle end-to-end (Apache-2.0) qui gère lui-même l'inférence des embeddings texte et image via une seule API — projet open-source déprécié, pivoté vers une plateforme commerciale de recherche e-commerce.

## Liens

- [[Wiki/Concepts/Bases de données|Bases de données]] — le concept (Wiki)
- [[Recherche d'information]] — recherche lexicale (BM25) et, désormais, dense (kNN) et [[Hybrid retrieval|hybride]].
- [[Comparatif - Moteurs de recherche]] — comparatif de la catégorie.
- Doc : https://www.elastic.co/guide/index.html
