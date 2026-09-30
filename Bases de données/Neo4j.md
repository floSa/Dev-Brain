---
role: brique
nom: Neo4j
alias: [neo4j, neo4J, neo 4j]
pitch: "SGBD de graphes natif, référence du modèle propriété-graphe et de Cypher — Community en GPLv3 et mono-instance, cluster et sauvegarde en ligne réservés à Enterprise (licence commerciale)."
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
> SGBD de graphes natif, référence du modèle propriété-graphe et de Cypher — Community en GPLv3 et mono-instance, cluster et sauvegarde en ligne réservés à Enterprise (licence commerciale).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Java | open-core | self-hébergé ou managé · mono-nœud | production | à jour · 2026-08-25 |
<!-- AUTO:BANDEAU:END -->

## Définition

Base de graphes **native** : les données sont des nœuds reliés par des arêtes typées et
orientées, chacun portant des propriétés — le modèle *property graph*. Le stockage est pensé
pour le graphe : suivre une relation est un saut de pointeur, pas une jointure, donc le
parcours reste rapide quand la profondeur augmente. Le langage **Cypher** exprime ces
parcours de façon déclarative et visuelle (`MATCH (a)-[:CONNAIT]->(b)`). C'est la référence
historique du domaine, et l'écosystème le plus riche : pilotes, bibliothèque GDS pour les
algorithmes de graphe, outillage de visualisation. Penser « table » plutôt que « relation »
produit un modèle plat qui perd tout l'intérêt du graphe. Version relevée le 2026-09-30 :
**2026.09.0** (tag du 2026-09-16), numérotation calendaire, avec la ligne 5.26 encore
maintenue (5.26.31) ; environ 17 300 étoiles. Cypher existe en deux versions (Cypher 5 et
Cypher 25) et suit GQL (ISO/IEC 39075:2024) sans la couvrir entièrement : la gestion de
session et de transaction en langage manque encore.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Données fortement connectées où la relation compte autant que l'entité : réseaux sociaux, fraude, recommandation, généalogie | L'édition Community est mono-instance sous GPLv3 : ni cluster, ni sauvegarde en ligne (dump et restauration hors ligne seulement), ni bases multiples, ni RBAC |
| Parcours à profondeur variable ou inconnue — chemins, voisinages à N sauts — que SQL exprime mal | Clustering, sauvegarde en ligne, bases multiples, RBAC, bases composites et sharding de propriétés : tout cela est Enterprise, sous licence commerciale ; le sharding automatique illimité (Infinigraph) est un palier d'abonnement distinct |
| Détection de motifs et algorithmes de graphe (centralité, communautés, plus courts chemins) via la bibliothèque GDS | Les super-nœuds — un nœud à des millions d'arêtes — dégradent les parcours et imposent de remodéliser |
| Graphes de connaissances et moteurs de raisonnement, y compris en appui d'un RAG, avec un index vectoriel inclus en Community (jusqu'à 4 096 dimensions) | Agrégations analytiques sur de gros volumes : ce n'est pas un moteur colonne |
| | La bibliothèque GDS en Community plafonne à 4 cœurs et 3 modèles au catalogue, et son dépôt porte une licence personnalisée, que GitHub ne reconnaît pas comme libre ; cœurs illimités et cluster demandent Enterprise |
| | Données tabulaires peu reliées, transactions classiques → [[Postgres]] |

## Mise en œuvre

- Installation — self-host en édition Community ou Enterprise, ou managé sur Neo4j AuraDB
- Point d'entrée — Cypher, depuis le navigateur Neo4j ou un pilote
- Prérequis — une JVM pour le self-host, et un modèle pensé en relations, pas en tables
- Exécution — self-hébergé ou managé ; scaling vertical en Community, le clustering et le sharding relevant d'Enterprise
- Coût — Community sous GPLv3 (le dépôt n'ajoute aucune clause), gratuite mais mono-instance ; Enterprise sous licence commerciale, qui porte la haute disponibilité — c'est le modèle open-core ; Infinigraph (sharding automatique) en abonnement à part ; AuraDB propose un palier gratuit

## Écosystème

### Alternatives

- [[Nebula Graph]] — Base de graphes distribuée nativement (Apache-2.0, C++, Raft) pour jeux de données massifs — l'édition Community est figée sur la 3.8.0 de mai 2024, l'évolution passe par l'édition Enterprise, fermée.

## Ressources

- Documentation — https://neo4j.com/docs/
- Dépôt — https://github.com/neo4j/neo4j
- Documentation — les éditions et leurs fonctions : https://neo4j.com/docs/operations-manual/current/introduction/
- Documentation — conformité à GQL : https://neo4j.com/docs/cypher-manual/current/appendix/gql-conformance/

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[Comparatif - Bases graphes]] — ce qui départage les moteurs du dossier
- [[GraphRAG]] — le retrieval RAG sur graphe de connaissances, souvent stocké ici
- [[Construction de graphes de connaissances]] — peupler le graphe par extraction d'entités et de relations
- [[Graph Neural Networks]] — le ML sur graphes, branché sur les données stockées ici
