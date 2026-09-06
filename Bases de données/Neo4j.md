---
role: brique
nom: Neo4j
alias: [neo4j, neo4J, neo 4j]
pitch: "SGBD de graphes natif, leader des données connectées : modèle propriété-graphe et requêtes Cypher."
categorie: database/graphe
famille: plateforme
licence_type: open-core
hosted: [self, managed]
maturite: production
langage: Java
scaling: single-node
alternatives: ["[[Nebula Graph]]"]
complements: []
tags: [graph-db]
url_docs: https://neo4j.com/docs/
url_repo: https://github.com/neo4j/neo4j
---

# Neo4j

<!-- AUTO:BANDEAU:START -->
> SGBD de graphes natif, leader des données connectées : modèle propriété-graphe et requêtes Cypher.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme Java | open-core | self-hébergé ou managé · mono-nœud | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Base de graphes **native** : les données sont des nœuds reliés par des arêtes typées et
orientées, chacun portant des propriétés — le modèle *property graph*. Le stockage est pensé
pour le graphe : suivre une relation est un saut de pointeur, pas une jointure, donc le
parcours reste rapide quand la profondeur augmente. Le langage **Cypher** exprime ces
parcours de façon déclarative et visuelle (`MATCH (a)-[:CONNAIT]->(b)`). C'est la référence
historique du domaine, et l'écosystème le plus riche : pilotes, bibliothèque GDS pour les
algorithmes de graphe, outillage de visualisation. Penser « table » plutôt que « relation »
produit un modèle plat qui perd tout l'intérêt du graphe.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Données fortement connectées où la relation compte autant que l'entité : réseaux sociaux, fraude, recommandation, généalogie | L'édition Community est mono-instance : ni cluster, ni sauvegarde à chaud |
| Parcours à profondeur variable ou inconnue — chemins, voisinages à N sauts — que SQL exprime mal | La montée en charge se fait en vertical ; réplication et sharding *Fabric* sont réservés à l'édition Enterprise |
| Détection de motifs et algorithmes de graphe (centralité, communautés, plus courts chemins) via la bibliothèque GDS | Les super-nœuds — un nœud à des millions d'arêtes — dégradent les parcours et imposent de remodéliser |
| Graphes de connaissances et moteurs de raisonnement, y compris en appui d'un RAG | Agrégations analytiques sur de gros volumes : ce n'est pas un moteur colonne |
| | Données tabulaires peu reliées, transactions classiques → [[Postgres]] |

## Mise en œuvre

- Installation — self-host en édition Community ou Enterprise, ou managé sur Neo4j AuraDB
- Point d'entrée — Cypher, depuis le navigateur Neo4j ou un pilote
- Prérequis — une JVM pour le self-host, et un modèle pensé en relations, pas en tables
- Exécution — self-hébergé ou managé ; scaling vertical par défaut, le clustering relevant d'Enterprise
- Coût — Community sous GPLv3, gratuite mais mono-instance ; Enterprise sous licence commerciale pour la HA — c'est le modèle open-core ; AuraDB propose un free tier

## Écosystème

### Alternatives

- [[Nebula Graph]] — Base de graphes distribuée pour jeux de données massifs.

## Ressources

- Documentation — https://neo4j.com/docs/
- Dépôt — https://github.com/neo4j/neo4j

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[Comparatif - Bases graphes]] — ce qui départage les moteurs du dossier
- [[GraphRAG]] — le retrieval RAG sur graphe de connaissances, souvent stocké ici
- [[Construction de graphes de connaissances]] — peupler le graphe par extraction d'entités et de relations
- [[Graph Neural Networks]] — le ML sur graphes, branché sur les données stockées ici
