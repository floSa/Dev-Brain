---
role: brique
nom: bm25s
alias: [bm25-sparse, bm25 sparse]
pitch: "Implémentation BM25 ultra-rapide en Python (matrices creuses SciPy) — scores pré-calculés à l'indexation, requêtes en millisecondes, des ordres de grandeur plus vite que rank-bm25, avec index sauvegardable et rechargeable en mémoire-mappée."
categorie: database/recherche
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[rank-bm25]]"]
complements: []
tags: [information-retrieval, ranking, search]
url_docs: https://bm25s.github.io/
url_repo: https://github.com/xhluca/bm25s
---

# bm25s

<!-- AUTO:BANDEAU:START -->
> Implémentation BM25 ultra-rapide en Python (matrices creuses SciPy) — scores pré-calculés à l'indexation, requêtes en millisecondes, des ordres de grandeur plus vite que rank-bm25, avec index sauvegardable et rechargeable en mémoire-mappée.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-08-25 |
<!-- AUTO:BANDEAU:END -->

## Définition

Implémentation de BM25 qui **pré-calcule tous les scores à l'indexation** et les range dans des
matrices creuses SciPy. À la requête, scorer le corpus se réduit à une multiplication creuse :
on gagne des ordres de grandeur sur une implémentation Python pure, tout en restant une simple
bibliothèque — aucun serveur, aucun index distant. Les variantes Okapi BM25, BM25L, BM25+,
ATIRE et Lucene sont disponibles, et un tokeniseur est fourni (stop-words, stemming Snowball
optionnel).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Étage lexical / sparse d'un retrieval hybride où la latence compte | Le gros de la dépense est à l'indexation, pas à la requête : sur très gros corpus, c'est elle qu'il faut dimensionner |
| Corpus de quelques milliers à quelques millions de documents tenant sur une machine | Pas de mise à jour incrémentale fine — ajouter des documents revient en pratique à réindexer |
| Baseline BM25 sérieuse pour jauger un retrieval dense, sans monter un moteur | La qualité tient à la tokenisation : stop-words et stemming sont à régler pour la langue cible |
| Index à persister (`save` / `load`) et recharger en mémoire-mappée, pour un démarrage instantané | Passage à l'échelle distribuée, persistance transactionnelle, mises à jour incrémentales → [[Elasticsearch]] |
| | Recherche sémantique (synonymes, paraphrases) → [[sentence-transformers]] et un index vectoriel |

## Mise en œuvre

- Installation — `uv add bm25s` ; stemming optionnel via `PyStemmer`
- Point d'entrée — import Python : indexation du corpus tokenisé, puis `retrieve()` ; tokeniseur fourni ou remplacé par le sien
- Prérequis — NumPy et SciPy ; le corpus tokenisé tient en mémoire le temps de l'indexation
- Exécution — mono-nœud, en process ; l'index creux se sauvegarde sur disque et se recharge en mémoire-mappée
- Coût — gratuit, licence MIT

## Écosystème

### Alternatives

- [[rank-bm25]] — Implémentation Python pure des algorithmes BM25 (Okapi, BM25L, BM25+) pour le classement lexical de documents — minimale, sans index ni dépendance, idéale pour prototyper un retrieval sparse.

## Ressources

- Documentation — https://bm25s.github.io/
- Dépôt — https://github.com/xhluca/bm25s

## Voir aussi

- [[BM25]] — l'algorithme qu'il implémente
- [[Recherche d'information]] — le cadre général
- [[Hybrid retrieval]] — l'usage typique, en étage lexical
- [[Ranking metrics]] — pour mesurer la qualité du classement produit
- [[Comparatif - Moteurs de recherche]] — ce qui départage les moteurs du dossier
- [[Comparatif - NLP|Comparatif — NLP]] — la brique vue depuis le versant NLP
