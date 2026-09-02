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
- Trois échelles ici, et elles ne s'échangent pas. Une **fonction de classement** ([[rank-bm25]], [[bm25s]]) tient dans un import. Une **bibliothèque d'index** ([[txtai]]) porte l'embedding et la persistance. Un **moteur distribué** ([[Elasticsearch]], [[Vespa]], [[Marqo]]) est un service à exploiter.
- L'**hybride** — BM25 plus recherche vectorielle, fusionnés au classement — bat en général chacune des deux seule. C'est ce qui rapproche ce sous-domaine du [[Vectoriel]].

## Choisir

- Prototyper un retrieval sparse, quelques milliers de documents → [[rank-bm25]] ; les mêmes algorithmes en rapide → [[bm25s]].
- Recherche sémantique, SQL et graphe sur un même index, du notebook à l'API → [[txtai]].
- Full-text et logs à grande échelle, écosystème mûr → [[Elasticsearch]].
- Classement par modèle ML dans le moteur, milliard de documents sous 100 ms → [[Vespa]].
- Attention : [[Marqo]] est déprécié côté open-source — vérifier avant de l'engager.

<!-- AUTO:START -->
### Briques
- [[bm25s]] — Implémentation BM25 ultra-rapide en Python (matrices creuses SciPy) — scores pré-calculés à l'indexation, requêtes en millisecondes, des ordres de grandeur plus vite que rank-bm25, avec index sauvegardable et rechargeable en mémoire-mappée.
- [[Elasticsearch]] — Moteur de recherche et d'analytique distribué : indexation full-text et logs à grande échelle.
- [[Marqo]] — Moteur de recherche vectorielle end-to-end (Apache-2.0) qui gère lui-même l'inférence des embeddings texte et image via une seule API — projet open-source déprécié, pivoté vers une plateforme commerciale de recherche e-commerce.
- [[rank-bm25]] — Implémentation Python pure des algorithmes BM25 (Okapi, BM25L, BM25+) pour le classement lexical de documents — minimale, sans index ni dépendance, idéale pour prototyper un retrieval sparse.
- [[txtai]] — Base d'embeddings tout-en-un en Python (Apache-2.0, NeuML) — recherche sémantique, SQL et graphe sur un même index, plus orchestration de workflows LLM ; du notebook embarqué à l'API FastAPI.
- [[Vespa]] — Plateforme de recherche et de serving IA (Apache-2.0) — combine full-text, recherche vectorielle et ranking par modèles ML dans un même moteur distribué, à l'échelle du milliard de documents et sous 100 ms.

### Comparatifs
- [[Comparatif - Moteurs de recherche]]
<!-- AUTO:END -->
