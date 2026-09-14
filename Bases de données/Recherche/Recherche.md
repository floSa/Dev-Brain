---
role: hub
nom: Recherche
pitch: Indexer des documents pour la recherche plein texte, lexicale ou hybride, avec un classement par pertinence.
domaines: [data-eng, ai-eng]
---

# Recherche

> Indexer des documents pour la recherche plein texte, lexicale ou hybride, avec un classement par pertinence.

## Ce qu'il faut comprendre

- La recherche plein texte classe par **pertinence**, pas par égalité. L'algorithme de référence reste **BM25** : une pondération terme-fréquence / rareté du terme, toujours compétitive face au dense sur les requêtes précises.
- Trois échelles ici, et elles ne s'échangent pas. Une **fonction de classement** ([[rank-bm25]], [[bm25s]]) tient dans un import. Une **bibliothèque d'index** ([[Lucene]], [[txtai]]) porte l'index, et pour txtai l'embedding et la persistance. Un **moteur** ([[Elasticsearch]], [[OpenSearch]], [[Apache Solr]], [[Vespa]], [[Marqo]], et côté recherche instantanée [[Meilisearch]] et [[Typesense]]) est un service à exploiter.
- Presque tous ces moteurs reposent sur le même objet, l'[[Index inversé]] : un dictionnaire de termes et, pour chacun, la liste des documents qui le contiennent. La moitié vectorielle est une [[Recherche vectorielle approximative]], et l'usage qu'on en fait, la [[Recherche sémantique]].
- L'**hybride** — BM25 plus recherche vectorielle, fusionnés au classement — bat en général chacune des deux seule. C'est ce qui rapproche ce sous-domaine du [[Vectoriel]].

## Choisir

- Prototyper un retrieval sparse, quelques milliers de documents → [[rank-bm25]] ; les mêmes algorithmes en rapide → [[bm25s]].
- Recherche sémantique, SQL et graphe sur un même index, du notebook à l'API → [[txtai]].
- Full-text et logs à grande échelle, écosystème mûr → [[Elasticsearch]].
- Le même modèle, sous licence Apache-2.0 sans copyleft réseau → [[OpenSearch]] ; ou [[Apache Solr]], moteur distribué de fondation Apache.
- Recherche de site ou d'application, résultats pendant la frappe, sans cluster → [[Meilisearch]] (MIT pour le cœur, sharding payant) ou [[Typesense]] (GPL-3.0, index en RAM).
- Construire son propre moteur ou embarquer un index dans une application JVM → [[Lucene]].
- Visualiser et alimenter Elasticsearch → [[Kibana]] (voir [[Observabilité]]), [[Logstash]] et [[Beats]] (voir [[Data & pipelines]]) : hors de ce dossier, parce qu'aucun ne stocke.
- Classement par modèle ML dans le moteur, milliard de documents sous 100 ms → [[Vespa]].
- Attention : [[Marqo]] est déprécié côté open-source — vérifier avant de l'engager.

<!-- AUTO:START -->
### Notions
- [[Index inversé]] — domaines : data-eng, ai-eng
- [[Recherche sémantique]] — domaines : data-eng, ai-eng
- [[Recherche vectorielle approximative]] — domaines : data-eng, ai-eng

### Briques
- [[Apache Solr]] — Plateforme de recherche Apache (Apache-2.0) bâtie sur Lucene — full-text, vectoriel et géospatial, distribuée par SolrCloud (réplication, bascule automatique).
- [[bm25s]] — Implémentation BM25 ultra-rapide en Python (matrices creuses SciPy) — scores pré-calculés à l'indexation, requêtes en millisecondes, des ordres de grandeur plus vite que rank-bm25, avec index sauvegardable et rechargeable en mémoire-mappée.
- [[Elasticsearch]] — Moteur de recherche et d'analytique distribué : indexation full-text et logs à grande échelle.
- [[Lucene]] — Bibliothèque Java de recherche plein texte (Apache-2.0) — le moteur d'indexation sous Elasticsearch et Solr ; index inversé et HNSW natifs, à embarquer dans une application JVM.
- [[Marqo]] — Moteur de recherche vectorielle end-to-end (Apache-2.0) qui gère lui-même l'inférence des embeddings texte et image via une seule API — projet open-source déprécié, pivoté vers une plateforme commerciale de recherche e-commerce.
- [[Meilisearch]] — Moteur de recherche instantané en Rust — full-text tolérant aux fautes de frappe, sémantique et hybride derrière une API REST ; édition communautaire MIT, sharding réservé à l'édition Enterprise.
- [[OpenSearch]] — Moteur de recherche et d'analytique distribué (Apache-2.0) — fork d'Elasticsearch 7.10.2 : full-text, k-NN et recherche hybride, visualisé dans OpenSearch Dashboards.
- [[rank-bm25]] — Implémentation Python pure des algorithmes BM25 (Okapi, BM25L, BM25+) pour le classement lexical de documents — minimale, sans index ni dépendance, idéale pour prototyper un retrieval sparse.
- [[txtai]] — Base d'embeddings tout-en-un en Python (Apache-2.0, NeuML) — recherche sémantique, SQL et graphe sur un même index, plus orchestration de workflows LLM ; du notebook embarqué à l'API FastAPI.
- [[Typesense]] — Moteur de recherche tolérant aux fautes de frappe (GPL-3.0, C++) — index en mémoire pour du search-as-you-type sous 50 ms, avec recherche vectorielle HNSW et hybride ; alternative ouverte à Algolia.
- [[Vespa]] — Plateforme de recherche et de serving IA (Apache-2.0) — combine full-text, recherche vectorielle et ranking par modèles ML dans un même moteur distribué, à l'échelle du milliard de documents et sous 100 ms.

### Comparatifs
- [[Comparatif - Moteurs de recherche]]
<!-- AUTO:END -->
