---
galaxie: dev
type: service
nom: rank-bm25
alias: [rank_bm25, bm25 python, okapi bm25 python]
pitch: "Implémentation Python pure des algorithmes BM25 (Okapi, BM25L, BM25+) pour le classement lexical de documents — minimale, sans index ni dépendance, idéale pour prototyper un retrieval sparse."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/bm25s|bm25s]]"]
remplace_par: []
status: actif
tags: [information-retrieval, ranking, search]
url_docs: https://github.com/dorianbrown/rank_bm25
url_repo: https://github.com/dorianbrown/rank_bm25
---

# rank-bm25

## Pourquoi

Implémentation **Python pure** des variantes de [[BM25]] (Okapi BM25, BM25L, BM25+). Pas d'index, pas de serveur, pas de dépendance lourde : on passe un corpus tokenisé, on requête, on récupère des scores. L'outil le plus simple pour ajouter une recherche **lexicale** à un prototype ou un pipeline [[RAG]].

## Quand l'utiliser

- Étage **lexical / sparse** d'un [[Hybrid retrieval|retrieval hybride]] à petite/moyenne échelle.
- Prototyper de la [[Recherche d'information]] sans monter un moteur.
- Baseline BM25 pour jauger un retrieval dense.

## Quand NE PAS l'utiliser

- **Passage à l'échelle** (gros corpus, latence, persistance, mises à jour) → un vrai moteur : [[Dev/Services/Elasticsearch|Elasticsearch]] / OpenSearch.
- Besoin de **vitesse** → [[Dev/Services/bm25s|bm25s]] (scores pré-calculés, matrices creuses) est nettement plus rapide.
- Recherche **sémantique** (synonymes, paraphrases) → [[Dev/Services/sentence-transformers|sentence-transformers]] + index vectoriel.

## Déploiement & coût

- Bibliothèque open-source (Apache-2.0), gratuite ; `uv add rank-bm25`.
- **Single-node, en mémoire** ; tout le corpus tient en RAM, recalcul à chaque session.
- Tokenisation **à fournir soi-même** (split, minuscules, stop-words).

## Pièges

- **Dormant** : dernière release en 2022, périmètre minimal — ne pas en attendre d'évolutions.
- Tout **en mémoire**, sans index persistant ni mise à jour incrémentale : inadapté aux gros volumes.
- Qualité = qualité de la **tokenisation** fournie ; rien n'est fait automatiquement.

## Alternatives

- [[Dev/Services/bm25s|bm25s]] — Implémentation BM25 ultra-rapide en Python (matrices creuses SciPy) — scores pré-calculés à l'indexation, requêtes en millisecondes, des ordres de grandeur plus vite que rank-bm25, avec index sauvegardable et rechargeable en mémoire-mappée.

À l'échelle, lui préférer un moteur lexical ([[Dev/Services/Elasticsearch|Elasticsearch]], cf. *Liens*).

## Liens

- [[BM25]] — l'algorithme qu'il implémente.
- [[Recherche d'information]] · [[Hybrid retrieval]] — ses usages.
- [[Dev/Services/Elasticsearch|Elasticsearch]] — BM25 indexé et distribué, pour la production.
- [[Dev/Patterns/Comparatif - NLP|Comparatif — NLP]]
- Repo : https://github.com/dorianbrown/rank_bm25
