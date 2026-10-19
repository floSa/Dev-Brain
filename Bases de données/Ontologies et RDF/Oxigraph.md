---
role: brique
nom: Oxigraph
alias: [oxigraph, pyoxigraph, Oxigraph server]
pitch: "Base RDF et SPARQL en Rust sur RocksDB (Apache-2.0 ou MIT) — serveur en un binaire, bibliothèque Rust et paquet Python ; mono-nœud, sans SHACL ni raisonnement annoncés."
categorie: database/rdf
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: beta
langage: Rust
scaling: single-node
alternatives: ["[[Apache Jena]]", "[[RDF4J]]", "[[QLever]]", "[[Fluree]]"]
complements: ["[[pySHACL]]"]
tags: [rdf, sparql, embedded]
url_docs: https://oxigraph.org/
url_repo: https://github.com/oxigraph/oxigraph
---

# Oxigraph

<!-- AUTO:BANDEAU:START -->
> Base RDF et SPARQL en Rust sur RocksDB (Apache-2.0 ou MIT) — serveur en un binaire, bibliothèque Rust et paquet Python ; mono-nœud, sans SHACL ni raisonnement annoncés.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Rust | open-source | self-hébergé · mono-nœud | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Base de données RDF et boîte à outils SPARQL écrite en Rust, bâtie sur le magasin clé-valeur RocksDB. Elle se présente sous quatre formes : une bibliothèque Rust, un binaire en ligne de commande qui lance un serveur HTTP (protocole SPARQL 1.1 et protocole de stockage de graphes), un paquet Python (`pyoxigraph`) et un paquet JavaScript compilé en WebAssembly. Elle lit et écrit Turtle, TriG, N-Triples, N-Quads, RDF/XML et JSON-LD, et implémente SPARQL 1.1 (requêtes, mises à jour, requêtes fédérées), avec un support préliminaire de RDF 1.2 et SPARQL 1.2. Relevé le 2026-10-19 : version **0.5.12** (2026-10-18), double licence Apache-2.0 ou MIT, environ 2 000 étoiles.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Une base RDF légère, installée par un seul binaire ou une image Docker, sans machine Java (binaire en Rust) | Du raisonnement OWL ou RDFS intégré, ou une validation SHACL intégrée : ni le README ni les crates du dépôt n'en annoncent |
| Un magasin RDF embarqué dans un programme Python (`pyoxigraph`), Rust ou Node, à la place d'un graphe en mémoire de rdflib | Un cluster ou une haute disponibilité : un seul nœud, sur RocksDB |
| Un point d'accès SPARQL 1.1 pour un projet de petite ou moyenne taille | Des performances de requête garanties : le README dit que l'évaluation des requêtes « n'a pas encore été optimisée » et que le projet est en plein développement |
| Réutiliser des morceaux seuls : parseur et sérialiseur RDF, évaluateur ou optimiseur SPARQL en crates séparés | Un très grand graphe : voir [[QLever]] |
| Valider avec [[pySHACL]] contre un magasin Oxigraph (extra `oxigraph` de pySHACL) | Une plateforme d'entreprise avec console, droits et sauvegardes gérées : voir [[Apache Jena]] ou [[RDF4J]] |

## Mise en œuvre

- Installation — le binaire en ligne de commande, l'image Docker décrite dans le dépôt, `uv add pyoxigraph` côté Python, ou la bibliothèque Rust
- Point d'entrée — `oxigraph serve` pour un point d'accès SPARQL, ou l'API Python (`pyoxigraph.Store`)
- Prérequis — Docker, ou la chaîne Rust pour compiler le binaire (crate `oxigraph-cli`) ; aucune machine Java
- Exécution — self-hébergé ou embarqué ; mono-nœud
- Coût — gratuit, Apache-2.0 ou MIT au choix

## Limites à connaître

- **Version 0.x, et le README le dit.** « En plein développement », avec une évaluation des requêtes non optimisée ; un projet qui doit figer son moteur sur dix ans choisira une fondation.
- **Ni SHACL ni raisonnement dans le dépôt lu.** La liste des crates (`oxrdf`, `spareval`, `spargebra`, `sparopt`, `spargeo`…) ne contient aucun module de validation ni d'inférence. La validation passe par un outil externe ([[pySHACL]]).
- **GeoSPARQL partiel.** La crate `spargeo` est décrite comme une implémentation partielle.

## Écosystème

### Alternatives

- [[Apache Jena]] — Framework Java pour le web sémantique et serveur SPARQL Fuseki (Apache-2.0) — base RDF transactionnelle TDB2 sur une machine, raisonneurs RDFS et OWL partiels, validation SHACL ; pas de cluster décrit.
- [[RDF4J]] — Framework Java pour RDF et SPARQL (BSD-3-Clause, Eclipse) — magasins mémoire et natif, serveur et Workbench à déployer dans Tomcat ou Jetty, validation SHACL à chaque transaction ; mono-nœud.
- [[QLever]] — Moteur SPARQL en C++ conçu pour de très grands graphes sur une seule machine (Apache-2.0) — SPARQL 1.1 complet, recherche textuelle, requêtes spatiales ; indexation préalable, sans SHACL ni raisonnement annoncés.
- [[Fluree]] — Base de graphes RDF en Rust, sous licence BUSL-1.1 — SPARQL, JSON-LD et openCypher, historique interrogeable, SHACL, raisonnement jusqu'à OWL 2 RL ; version 4 récente, et interdit d'en faire un service de base de données.
- [[rdflib]] — voisin : le graphe RDF en mémoire de Python, quand l'objet est de manipuler un fichier plutôt que d'héberger une base ; il sait aussi lire un point d'accès SPARQL distant.

### Compléments

- [[pySHACL]] — Validateur SHACL en Python pur (Apache-2.0), construit sur rdflib — vérifie un graphe RDF contre ses formes, en ligne de commande, en API ou en service HTTP ; peut développer le graphe par RDFS ou OWL-RL avant de valider. — valide un graphe stocké dans Oxigraph, par l'extra `oxigraph` de pySHACL.

## Ressources

- Documentation — https://oxigraph.org/
- Dépôt — https://github.com/oxigraph/oxigraph
- Documentation — l'architecture interne : https://github.com/oxigraph/oxigraph/wiki/Architecture

## Voir aussi

- [[Ontologies et RDF]] — le hub du sous-domaine
- [[Comparatif - Moteurs RDF]] — ce qui départage les moteurs RDF
- [[RDF et triplets]] — la notion : sujet, prédicat, objet, graphes nommés, formats
- [[SPARQL]] — la notion : le langage que le serveur parle
