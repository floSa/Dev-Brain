---
role: brique
nom: Apache Jena
alias: [Jena, Fuseki, Apache Jena Fuseki, Jena Fuseki, TDB2, ARQ]
pitch: "Framework Java pour le web sémantique et serveur SPARQL Fuseki (Apache-2.0) — base RDF transactionnelle TDB2 sur une machine, raisonneurs RDFS et OWL partiels, validation SHACL ; pas de cluster décrit."
categorie: database/rdf
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Java
scaling: single-node
alternatives: ["[[RDF4J]]", "[[Oxigraph]]", "[[QLever]]", "[[Virtuoso Open Source]]", "[[Fluree]]"]
complements: []
tags: [rdf, sparql, knowledge-graph]
url_docs: https://jena.apache.org/
url_repo: https://github.com/apache/jena
---

# Apache Jena

<!-- AUTO:BANDEAU:START -->
> Framework Java pour le web sémantique et serveur SPARQL Fuseki (Apache-2.0) — base RDF transactionnelle TDB2 sur une machine, raisonneurs RDFS et OWL partiels, validation SHACL ; pas de cluster décrit.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Java | open-source | self-hébergé · mono-nœud | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework Java de la fondation Apache pour écrire des applications de web sémantique, avec son serveur **Fuseki** : un point d'accès SPARQL en HTTP devant une base RDF. Les briques : une API RDF (lecture et écriture de graphes), **ARQ** (le moteur de requêtes SPARQL 1.1, avec requêtes fédérées et recherche plein texte), **TDB2** (le magasin de triplets sur disque, transactionnel), une API d'ontologies, des raisonneurs RDFS et OWL, et un module **SHACL**. Fuseki s'utilise seul, en WAR ou en conteneur Docker, ou s'embarque dans une application Java. Relevé le 2026-10-19 : dernière version notée dans `CHANGES.txt`, **6.2.0** (2026-07-31), licence Apache-2.0, dépôt actif (dernier push du jour).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un point d'accès SPARQL 1.1 complet (requêtes, mises à jour, protocole HTTP, graphes nommés) à héberger soi-même, sur un nœud | Un cluster ou une haute disponibilité : la documentation de Fuseki n'en décrit aucune, et TDB2 est présenté comme un magasin d'une seule machine |
| Une pile Java où le framework s'embarque : API RDF, ontologies, raisonneurs, SHACL dans le même jar | Un raisonnement OWL complet : les raisonneurs fournis sont « utiles mais incomplets », et la documentation renvoie vers Pellet, Racer ou FaCT pour OWL DL |
| Valider un graphe en ligne de commande (`shacl validate`) ou par un service SHACL de Fuseki | Un graphe de plusieurs milliards de triplets avec des latences serrées : voir [[QLever]] |
| Une fondation neutre, une licence Apache-2.0 et une documentation fournie | Un binaire unique sans machine Java : voir [[Oxigraph]] |
| Du GeoSPARQL, du plein texte ou un contrôle d'accès aux données (modules du projet) | Des requêtes Cypher ou un modèle de graphe de propriétés : voir [[Bases de graphes]] |

## Mise en œuvre

- Installation — le serveur Fuseki (archive, WAR ou image Docker), ou les dépendances Maven pour embarquer la bibliothèque
- Point d'entrée — le point d'accès SPARQL de Fuseki (`/ds/sparql`, `/ds/update`), l'API Java ou les commandes du projet
- Prérequis — une machine Java ; la version exigée dépend de la release, à lire dans la documentation de celle-ci (non relevée ici)
- Exécution — self-hébergé ; mono-nœud
- Coût — gratuit, Apache-2.0

## Limites à connaître

- **Le raisonnement n'est pas complet.** Les raisonneurs OWL, OWL Mini et OWL Micro sont décrits comme une implémentation « utile mais incomplète » du sous-ensemble OWL Lite : `complementOf` et `oneOf` ne sont pas gérés, `unionOf` l'est partiellement, les cardinalités se limitent à 0 ou 1. Un raisonneur est sûr (ce qu'il déduit est vrai), pas complet (il peut rater des déductions). Cf. [[OWL et raisonnement]].
- **SHACL : le cœur et SHACL-SPARQL.** Le module implémente SHACL Core et les contraintes SPARQL, plus la syntaxe compacte ; le service SHACL de Fuseki n'est pas actif par défaut et se déclare dans la configuration du point d'accès. La documentation lue ne dit rien de SHACL 1.2.
- **TDB2 n'est pas compatible avec TDB1.** Une base ancienne se migre par la procédure du projet, elle ne s'ouvre pas telle quelle.
- **Pas de release GitHub.** Les versions sortent par la fondation Apache ; la liste des releases du dépôt est vide, et le journal des changements est `CHANGES.txt`.

## Écosystème

### Alternatives

- [[RDF4J]] — Framework Java pour RDF et SPARQL (BSD-3-Clause, Eclipse) — magasins mémoire et natif, serveur et Workbench à déployer dans Tomcat ou Jetty, validation SHACL à chaque transaction ; mono-nœud.
- [[Oxigraph]] — Base RDF et SPARQL en Rust sur RocksDB (Apache-2.0 ou MIT) — serveur en un binaire, bibliothèque Rust et paquet Python ; mono-nœud, sans SHACL ni raisonnement annoncés.
- [[QLever]] — Moteur SPARQL en C++ conçu pour de très grands graphes sur une seule machine (Apache-2.0) — SPARQL 1.1 complet, recherche textuelle, requêtes spatiales ; indexation préalable, sans SHACL ni raisonnement annoncés.
- [[Virtuoso Open Source]] — Base multi-modèle (relationnel, graphe RDF, documents) et serveur HTTP en C (GPLv2) — SPARQL et Linked Data, inférence de base (sous-classes, owl:sameAs) ; cluster et réplication réservés à l'édition commerciale.
- [[Fluree]] — Base de graphes RDF en Rust, sous licence BUSL-1.1 — SPARQL, JSON-LD et openCypher, historique interrogeable, SHACL, raisonnement jusqu'à OWL 2 RL ; version 4 récente, et interdit d'en faire un service de base de données.
- [[Neo4j]] — voisin : un graphe de propriétés interrogé en Cypher, quand le besoin est un parcours de graphe sans échange de données entre systèmes ni ontologie partagée.

## Ressources

- Documentation — https://jena.apache.org/
- Dépôt — https://github.com/apache/jena
- Documentation — Fuseki : https://jena.apache.org/documentation/fuseki2/
- Documentation — SHACL : https://jena.apache.org/documentation/shacl/
- Documentation — raisonneurs : https://jena.apache.org/documentation/inference/

## Voir aussi

- [[Ontologies et RDF]] — le hub du sous-domaine
- [[Comparatif - Moteurs RDF]] — ce qui départage les moteurs RDF
- [[SPARQL]] — la notion : le langage que Fuseki sert
- [[SHACL]] — la notion : valider un graphe contre ses formes
- [[OWL et raisonnement]] — la notion : déduire des faits non écrits
