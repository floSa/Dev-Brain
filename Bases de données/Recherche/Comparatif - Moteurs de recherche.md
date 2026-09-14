---
role: comparatif
nom: Comparatif - Moteurs de recherche
categorie: database/recherche
tags: [search]
---

# Comparatif - Moteurs de recherche

> On tranche sur : bibliothèque ou moteur déployé, lexical ou sémantique, le ranking dans le serving ou après, et la licence — Apache-2.0, MIT ou copyleft réseau.

![[Comparatif - Moteurs de recherche.base]]

## Ce qui départage

- [[Elasticsearch]] — full-text BM25 distribué sur Lucene, quasi temps réel : ce n'est pas une base primaire, et la JVM est gourmande.
- [[OpenSearch]] — le fork Apache-2.0 d'Elasticsearch 7.10.2, avec k-NN et hybride ; il partage la lourdeur JVM et l'absence de garantie transactionnelle de son ancêtre.
- [[Apache Solr]] — l'autre moteur distribué sur Lucene, gouverné par une fondation et sous Apache-2.0 ; SolrCloud distribue et réplique, avec la même exigence de JVM.
- [[Meilisearch]] — recherche instantanée tolérante aux fautes, en un binaire Rust, mais nœud unique : le sharding et la réplication relèvent de l'édition Enterprise, sous licence commerciale en production.
- [[Typesense]] — recherche instantanée à index mémoire-résident, avec vectoriel HNSW et hybride, sous GPL-3.0 ; l'index doit tenir en RAM.
- [[Lucene]] — la bibliothèque sous les moteurs distribués, sans serveur, réplication ni API HTTP : l'index se pilote en Java.
- [[Vespa]] — le seul à exécuter le ranking ML **dans** la couche de serving, texte, vecteurs et tenseurs réunis ; la complexité opérationnelle est réelle.
- [[txtai]] — un index unifié vecteur + SQL + graphe, embarqué en Python ou exposé en API, mais single-node.
- [[bm25s]] — BM25 pré-calculé à l'indexation en matrices creuses : requêtes en millisecondes, sans mise à jour incrémentale.
- [[rank-bm25]] — BM25 en Python pur, sans index ni dépendance ; dormant depuis 2022 et tout en mémoire.
- [[Marqo]] — génère lui-même les embeddings texte et image derrière une seule API, mais le projet open-source est déprécié et sans correctif de sécurité.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
