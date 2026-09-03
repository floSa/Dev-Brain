---
role: comparatif
nom: Comparatif - Moteurs de recherche
categorie: database/recherche
tags: [search]
---

# Comparatif - Moteurs de recherche

> On tranche sur : bibliothèque ou moteur déployé, lexical ou sémantique, et le ranking dans le serving ou après.

![[Comparatif - Moteurs de recherche.base]]

## Ce qui départage

- [[Elasticsearch]] — full-text BM25 distribué sur Lucene, quasi temps réel : ce n'est pas une base primaire, et la JVM est gourmande.
- [[Vespa]] — le seul à exécuter le ranking ML **dans** la couche de serving, texte, vecteurs et tenseurs réunis ; la complexité opérationnelle est réelle.
- [[txtai]] — un index unifié vecteur + SQL + graphe, embarqué en Python ou exposé en API, mais single-node.
- [[bm25s]] — BM25 pré-calculé à l'indexation en matrices creuses : requêtes en millisecondes, sans mise à jour incrémentale.
- [[rank-bm25]] — BM25 en Python pur, sans index ni dépendance ; dormant depuis 2022 et tout en mémoire.
- [[Marqo]] — génère lui-même les embeddings texte et image derrière une seule API, mais le projet open-source est déprécié et sans correctif de sécurité.
