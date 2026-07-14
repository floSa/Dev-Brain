---
galaxie: dev
type: service
nom: Neo4j
alias: [neo4j, neo4J, neo 4j]
pitch: "SGBD de graphes natif, leader des données connectées : modèle propriété-graphe et requêtes Cypher."
categorie: database/graph
licence_type: open-core
hosted: both
maturite: production
langage: Java
scaling: single-node
alternatives: ["[[Dev/Services/Nebula Graph|Nebula Graph]]"]
remplace_par: []
status: actif
tags: [graph-db]
url_docs: https://neo4j.com/docs/
url_repo: https://github.com/neo4j/neo4j
---

# Neo4j

## Pourquoi

Base de graphes **native** : les données sont des nœuds reliés par des arêtes typées et orientées, chacun portant des propriétés (modèle *property graph*). Le stockage est pensé pour le graphe — suivre une relation est un saut de pointeur, pas une jointure, donc le parcours de relations profondes reste rapide quand sa profondeur augmente. Le langage **Cypher** exprime ces parcours de façon déclarative et visuelle (`MATCH (a)-[:CONNAIT]->(b)`). C'est la référence historique et la plus mûre du domaine, avec l'écosystème le plus riche (pilotes, GDS pour les algorithmes de graphe, outillage de viz).

## Quand l'utiliser

- Données fortement connectées où la relation est aussi importante que l'entité (réseaux sociaux, fraude, recommandation, généalogie).
- Requêtes de parcours à profondeur variable ou inconnue (chemins, voisinages à N sauts) que SQL exprime mal.
- Détection de motifs et algorithmes de graphe (centralité, communautés, plus courts chemins) via la lib GDS.
- Graphes de connaissances et moteurs de raisonnement, y compris en appui d'un RAG.

## Quand NE PAS l'utiliser

- Données tabulaires peu reliées, transactions classiques → [[Dev/Services/Postgres|Postgres]].
- Graphe dépassant un seul nœud, besoin de partitionnement horizontal massif → [[Dev/Services/Nebula Graph|Nebula Graph]].
- Agrégations analytiques sur de gros volumes → une base colonne/OLAP.

## Déploiement & coût

- Self-host (Community ou Enterprise) ou managé via **Neo4j AuraDB** (offre cloud, free tier).
- Scaling vertical par défaut ; le clustering (réplication, sharding *Fabric*) est réservé à l'édition Enterprise.
- Modèle **open-core** : Community sous GPLv3 (mono-instance, sans clustering ni sauvegarde à chaud) ; Enterprise sous licence commerciale pour la HA et l'exploitation.

## Pièges

- Community est mono-instance : pas de cluster ni de hot backup, ce qui pousse vers Enterprise (payant) ou Aura en production.
- Penser « table » plutôt que « relation » mène à un modèle plat qui perd l'intérêt du graphe.
- Les super-nœuds (un nœud à des millions d'arêtes) dégradent les parcours ; à modéliser autrement.
- La montée en charge se fait surtout en vertical : au-delà d'un nœud, l'architecture distribuée est contrainte.

## Alternatives

- [[Dev/Services/Nebula Graph|Nebula Graph]] — Base de graphes distribuée pour jeux de données massifs.

## Liens

- [[Wiki/Concepts/Bases de données|Bases de données]] — le concept (Wiki)
- [[Comparatif - Bases graphes]] — comparatif des moteurs de graphe
- [[Wiki/Concepts/GraphRAG|GraphRAG]] — retrieval RAG sur graphe de connaissances, souvent stocké ici
- [[Wiki/Concepts/Construction de graphes de connaissances|Construction de graphes de connaissances]] — peupler le graphe par extraction d'entités/relations
- [[Wiki/Concepts/Graph Neural Networks|Graph Neural Networks]] — ML sur graphes, branché sur les données stockées ici
- Doc : https://neo4j.com/docs/
