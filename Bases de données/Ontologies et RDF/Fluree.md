---
role: brique
nom: Fluree
alias: [fluree, Fluree DB, fluree/db]
pitch: "Base de graphes RDF en Rust, sous licence BUSL-1.1 — SPARQL, JSON-LD et openCypher, historique interrogeable, SHACL, raisonnement jusqu'à OWL 2 RL ; version 4 récente, et interdit d'en faire un service de base de données."
categorie: database/rdf
famille: plateforme
licence_type: source-available
hosted: [self, managed]
maturite: beta
langage: Rust
scaling: distributed
alternatives: ["[[Apache Jena]]", "[[Oxigraph]]"]
complements: []
tags: [rdf, sparql, knowledge-graph, data-versioning]
url_docs: https://github.com/fluree/db/tree/main/docs
url_repo: https://github.com/fluree/db
---

# Fluree

<!-- AUTO:BANDEAU:START -->
> Base de graphes RDF en Rust, sous licence BUSL-1.1 — SPARQL, JSON-LD et openCypher, historique interrogeable, SHACL, raisonnement jusqu'à OWL 2 RL ; version 4 récente, et interdit d'en faire un service de base de données.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Rust | source-available | self-hébergé ou managé · distribué | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Base de données de graphes RDF écrite en Rust, qui garde tout l'historique des écritures et se laisse interroger dans le temps. Elle parle RDF 1.1 et 1.2, SPARQL, JSON-LD et openCypher (les trois langages passent par le même moteur), valide les données par des formes SHACL au moment de la transaction et déduit des faits par RDFS, OWL 2 QL, OWL 2 RL ou des règles Datalog. Elle se déploie en conteneur Docker, par un binaire qui embarque le serveur, ou comme bibliothèque Rust, sur mémoire, fichiers, S3 avec DynamoDB ou IPFS. Relevé le 2026-10-19 : version **4.2.4** (2026-10-14), dont la première préversion, la 4.0.0-alpha.1, date du **2026-04-22** ; licence **BUSL-1.1**, environ 470 étoiles.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un graphe RDF avec SHACL à la transaction, du raisonnement OWL 2 RL intégré et la même base pour SPARQL, JSON-LD et Cypher | Une licence libre au sens de l'OSI : BUSL-1.1 n'en est pas une ; elle se convertit en Apache-2.0 quatre ans après la première diffusion de chaque version |
| Interroger l'état du graphe à une date passée (par numéro de transaction, horodatage ou commit) : audit, traçabilité de la maintenance | Offrir Fluree à des tiers comme base de données hébergée, où ils créent leurs bases ou leurs schémas : c'est le « service de base de données » que l'usage autorisé exclut |
| Un usage interne ou l'embarquement dans son propre produit, où l'on définit seul le schéma | Un moteur éprouvé depuis des années : la version 4 a six mois depuis sa première préversion, et aucun retour d'exploitation n'a été relevé |
| Une haute disponibilité des écritures par Raft, et des lectures qui passent à l'échelle par des pairs de requête | Un contexte où une architecture à stockage partagé (S3 et DynamoDB, ou montage de fichiers commun) est exclue |

## Mise en œuvre

- Installation — `docker run -p 8090:8090 fluree/server:latest`, ou le binaire `fluree` (Homebrew, installeur shell ou PowerShell) qui embarque le serveur (`fluree server run`)
- Point d'entrée — `fluree init`, `fluree create`, `fluree insert`, `fluree query` ; ou le serveur HTTP sur le port 8090
- Prérequis — pour un cluster Raft : un stockage partagé adressé par contenu, une identité stable et une adresse interne stable par nœud, d'après la documentation d'exploitation
- Exécution — self-hébergé (un nœud, ou un cluster Raft pour les écritures et des pairs de requête pour les lectures) ; une offre sans serveur existe chez l'éditeur, à usage limité
- Coût — gratuit sous BUSL-1.1 dans les limites de l'usage autorisé ; licences alternatives auprès de l'éditeur

## Limites à connaître

- **Licence à lire en entier.** L'usage de production est permis, sauf pour offrir Fluree comme base de données à des tiers. Ne sont pas un « service de base de données » : l'usage comme composant de sa propre application, même si des tiers l'interrogent, tant que l'on définit seul le schéma ; l'accès en lecture à des données que l'on maîtrise, y compris par un point d'accès SPARQL qui accepte des requêtes libres. Le texte est à confronter à un juriste avant une offre commerciale.
- **Projet jeune et chiffres du fabricant.** Le README annonce plus de deux millions de faits par seconde à l'import et des comparaisons favorables face à QLever, Virtuoso et d'autres, sur des bancs d'essai que l'éditeur publie lui-même. Rien de tout cela n'a été reproduit ici.
- **Pas d'écritures actives sur plusieurs régions.** La documentation d'exploitation le dit : la résilience entre régions repose sur des lectures distribuées et des données répliquables, pas sur des écritures actives partout.

## Écosystème

### Alternatives

- [[Apache Jena]] — Framework Java pour le web sémantique et serveur SPARQL Fuseki (Apache-2.0) — base RDF transactionnelle TDB2 sur une machine, raisonneurs RDFS et OWL partiels, validation SHACL ; pas de cluster décrit.
- [[Oxigraph]] — Base RDF et SPARQL en Rust sur RocksDB (Apache-2.0 ou MIT) — serveur en un binaire, bibliothèque Rust et paquet Python ; mono-nœud, sans SHACL ni raisonnement annoncés.
- [[Neo4j]] — voisin : un graphe de propriétés interrogé en Cypher ; Fluree sait aussi répondre en openCypher, sur un modèle RDF.

## Ressources

- Documentation — https://github.com/fluree/db/tree/main/docs
- Dépôt — https://github.com/fluree/db
- Documentation — le raisonnement : https://github.com/fluree/db/blob/main/docs/concepts/reasoning.md
- Documentation — les clusters Raft : https://github.com/fluree/db/blob/main/docs/operations/raft-clusters.md

## Voir aussi

- [[Ontologies et RDF]] — le hub du sous-domaine
- [[Comparatif - Moteurs RDF]] — ce qui départage les moteurs RDF
- [[SHACL]] — la notion : valider un graphe contre ses formes
- [[OWL et raisonnement]] — la notion : déduire des faits non écrits
- [[SPARQL]] — la notion : le langage de requête
