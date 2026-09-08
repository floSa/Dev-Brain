---
role: brique
nom: rank-bm25
alias: [rank_bm25, bm25 python, okapi bm25 python]
pitch: "Implémentation Python pure des algorithmes BM25 (Okapi, BM25L, BM25+) pour le classement lexical de documents — minimale, sans index ni dépendance, idéale pour prototyper un retrieval sparse."
categorie: database/recherche
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[bm25s]]"]
complements: []
tags: [information-retrieval, ranking, search]
url_docs: https://github.com/dorianbrown/rank_bm25
url_repo: https://github.com/dorianbrown/rank_bm25
---

# rank-bm25

<!-- AUTO:BANDEAU:START -->
> Implémentation Python pure des algorithmes BM25 (Okapi, BM25L, BM25+) pour le classement lexical de documents — minimale, sans index ni dépendance, idéale pour prototyper un retrieval sparse.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont ancien · 2022-02-16 |
<!-- AUTO:BANDEAU:END -->

## Définition

Implémentation **Python pure** des variantes de BM25 : Okapi BM25, BM25L, BM25+. Pas d'index,
pas de serveur, pas de dépendance lourde — on passe un corpus déjà tokenisé, on requête, on
récupère des scores. Tout vit en mémoire et se recalcule à chaque session. C'est l'outil le
plus court pour ajouter une recherche lexicale à un prototype ou à un pipeline de retrieval, et
son périmètre s'arrête là.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Étage lexical / sparse d'un retrieval hybride à petite ou moyenne échelle | Dormant : dernière release en 2022, périmètre minimal — aucune évolution à en attendre |
| Prototyper de la recherche d'information sans monter un moteur | Tout en mémoire, sans index persistant ni mise à jour incrémentale : inadapté aux gros volumes |
| Baseline BM25 pour jauger un retrieval dense | La tokenisation est entièrement à fournir (découpage, minuscules, stop-words) — rien n'est fait automatiquement |
| | Passage à l'échelle : gros corpus, latence, persistance, mises à jour → [[Elasticsearch]] |
| | Recherche sémantique (synonymes, paraphrases) → [[sentence-transformers]] et un index vectoriel |

## Mise en œuvre

- Installation — `uv add rank-bm25` ; aucune dépendance lourde
- Point d'entrée — import Python : `BM25Okapi(corpus_tokenise)`, puis `get_scores(requete)`
- Prérequis — la tokenisation, à écrire soi-même en amont
- Exécution — mono-nœud, tout en mémoire ; le corpus est rechargé et recalculé à chaque session
- Coût — gratuit, licence Apache-2.0

## Écosystème

### Alternatives

- [[bm25s]] — Implémentation BM25 ultra-rapide en Python (matrices creuses SciPy) — scores pré-calculés à l'indexation, requêtes en millisecondes, des ordres de grandeur plus vite que rank-bm25, avec index sauvegardable et rechargeable en mémoire-mappée.

## Ressources

- Dépôt — https://github.com/dorianbrown/rank_bm25 — il tient lieu de documentation

## Voir aussi

- [[BM25]] — l'algorithme qu'il implémente
- [[Recherche d'information]] — le cadre général
- [[Hybrid retrieval]] — l'usage typique, en étage lexical
- [[Comparatif - Moteurs de recherche]] — ce qui départage les moteurs du dossier
- [[Comparatif - NLP|Comparatif — NLP]] — la brique vue depuis le versant NLP
