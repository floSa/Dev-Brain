---
galaxie: dev
type: service
nom: bm25s
alias: [bm25-sparse, bm25 sparse]
pitch: "Implémentation BM25 ultra-rapide en Python (matrices creuses SciPy) — scores pré-calculés à l'indexation, requêtes en millisecondes, des ordres de grandeur plus vite que rank-bm25, avec index sauvegardable et rechargeable en mémoire-mappée."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/rank-bm25|rank-bm25]]"]
remplace_par: []
status: actif
tags: [information-retrieval, ranking, search]
url_docs: https://bm25s.github.io/
url_repo: https://github.com/xhluca/bm25s
---

# bm25s

## Pourquoi

Implémentation de [[BM25]] qui **pré-calcule tous les scores à l'indexation** et les stocke dans des **matrices creuses SciPy**. Au moment de la requête, scorer le corpus revient à une multiplication creuse : on gagne **des ordres de grandeur** sur les implémentations Python pures comme [[Dev/Services/rank-bm25|rank-bm25]], tout en restant une simple bibliothèque (pas de serveur). Variantes Okapi BM25, BM25L, BM25+, ATIRE, Lucene. Tokeniseur intégré (stop-words, stemming Snowball optionnel).

## Quand l'utiliser

- Étage **lexical / sparse** d'un [[Hybrid retrieval|retrieval hybride]] où la **latence compte**.
- Corpus de quelques milliers à quelques millions de documents tenant sur une machine, avec besoin de requêtes rapides.
- Baseline BM25 sérieuse pour jauger un retrieval dense, sans monter un moteur.
- Index à **persister** (`save` / `load`) et recharger en mémoire-mappée pour démarrage instantané.

## Quand NE PAS l'utiliser

- **Passage à l'échelle distribuée**, persistance transactionnelle, mises à jour incrémentales → un vrai moteur : [[Dev/Services/Elasticsearch|Elasticsearch]] / OpenSearch.
- Prototype jetable sans enjeu de vitesse → [[Dev/Services/rank-bm25|rank-bm25]] suffit et a une API encore plus minimale.
- Recherche **sémantique** (synonymes, paraphrases) → [[Dev/Services/sentence-transformers|sentence-transformers]] + index vectoriel.

## Déploiement & coût

- Bibliothèque open-source (MIT), gratuite ; `uv add bm25s`. Dépend de NumPy / SciPy ; stemming optionnel via `PyStemmer`.
- **Single-node, en mémoire** ; l'index creux peut être sauvegardé sur disque et rechargé en mémoire-mappée (faible empreinte au chargement).
- Tokenisation fournie par la lib (configurable) ou à remplacer par la sienne.

## Pièges

- Le gros de la dépense est à l'**indexation** (pré-calcul des scores) ; la requête est quasi gratuite — dimensionner en conséquence sur très gros corpus.
- Pas de mise à jour incrémentale fine : ajouter des documents implique en pratique de réindexer.
- Qualité = qualité de la **tokenisation** ; bien régler stop-words et stemming pour la langue cible.

## Alternatives

- [[Dev/Services/rank-bm25|rank-bm25]] — Implémentation Python pure des algorithmes BM25 (Okapi, BM25L, BM25+) pour le classement lexical de documents — minimale, sans index ni dépendance, idéale pour prototyper un retrieval sparse.

## Liens

- [[BM25]] — l'algorithme qu'il implémente.
- [[Recherche d'information]] · [[Hybrid retrieval]] — ses usages.
- [[Dev/Services/Elasticsearch|Elasticsearch]] — BM25 indexé et distribué, pour la production.
- [[Ranking metrics]] — pour mesurer la qualité du classement produit.
- [[Dev/Patterns/Comparatif - NLP|Comparatif — NLP]]
- Doc : https://bm25s.github.io/ · Repo : https://github.com/xhluca/bm25s
