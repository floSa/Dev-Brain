---
role: brique
nom: RDF4J
alias: [rdf4j, Eclipse RDF4J, Sesame, RDF4J Server, RDF4J Workbench]
pitch: "Framework Java pour RDF et SPARQL (BSD-3-Clause, Eclipse) — magasins mémoire et natif, serveur et Workbench à déployer dans Tomcat ou Jetty, validation SHACL à chaque transaction ; mono-nœud."
categorie: database/rdf
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Java
scaling: single-node
alternatives: ["[[Apache Jena]]", "[[Oxigraph]]"]
complements: []
tags: [rdf, sparql, knowledge-graph]
url_docs: https://rdf4j.org/
url_repo: https://github.com/eclipse-rdf4j/rdf4j
---

# RDF4J

<!-- AUTO:BANDEAU:START -->
> Framework Java pour RDF et SPARQL (BSD-3-Clause, Eclipse) — magasins mémoire et natif, serveur et Workbench à déployer dans Tomcat ou Jetty, validation SHACL à chaque transaction ; mono-nœud.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Java | open-source | self-hébergé · mono-nœud | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework Java de la fondation Eclipse pour créer, lire, stocker, raisonner et interroger du RDF, avec un serveur HTTP et une interface web de gestion. La bibliothèque propose des **magasins** (« Sail ») empilables : mémoire, natif sur disque, et des couches qui ajoutent de l'inférence RDFS ou la validation SHACL ; un dépôt peut aussi servir de proxy vers un point d'accès SPARQL distant ou fédérer plusieurs magasins (FedX). **RDF4J Server** expose les dépôts en HTTP (extension du protocole SPARQL) et **RDF4J Workbench** est l'interface web pour gérer dépôts et requêtes. Relevé le 2026-10-19 : licence BSD-3-Clause, dépôt actif (dernier push du jour) ; la page des releases du dépôt s'arrête à la **6.0.0** (2026-08-10), tandis que le site annonce une 6.1.0 du 2026-09-12 corrigeant des bogues avec un changement d'API — à recouper avant de figer une version.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Une application Java qui doit embarquer un magasin RDF, avec une API de dépôts et de transactions propre | Un binaire sans machine Java : la 6.0.0 passe le projet à Java 25, et le serveur exige Java 25 ou plus |
| Valider du RDF **à chaque transaction** par SHACL : la couche SHACL refuse un commit qui viole les formes | Un graphe de plusieurs centaines de millions de triplets : la documentation décrit le magasin natif comme adapté jusqu'à environ 100 millions de triplets |
| Un serveur et une interface web prêts à déployer dans Tomcat ou Jetty (WAR), avec des rôles par motif d'URL | Un cluster ou une réplication : pas décrits ; la fédération (FedX) interroge plusieurs sources, elle ne réplique pas |
| Fédérer des requêtes sur plusieurs magasins ou points d'accès SPARQL | Une inférence OWL riche : la couche prévue est RDFS, plus un raisonnement simple de sous-classes dans la couche SHACL |
| Un projet sous gouvernance de fondation, en BSD-3-Clause | Une mise en route de dix minutes sans conteneur de servlets : voir [[Oxigraph]] |

## Mise en œuvre

- Installation — dépendances Maven pour la bibliothèque ; pour le serveur et le Workbench, les WAR du SDK dans Tomcat 9 ou Jetty 9.4 (recommandés par la documentation) ou l'image construite par le script du dossier `docker/`
- Point d'entrée — l'API Java (`Repository`, `RepositoryConnection`) ou le point d'accès HTTP du Server ; `/rdf4j-workbench` pour l'interface
- Prérequis — Java 25 ou plus et un conteneur de servlets (API Servlet 3.1, JSP 2.2) pour le serveur, d'après la documentation de la 6.x
- Exécution — self-hébergé ; mono-nœud
- Coût — gratuit, BSD-3-Clause

## Limites à connaître

- **Le dimensionnement annoncé est modeste.** Le magasin mémoire est « conçu pour moins de 100 000 triplets », le natif pour « jusqu'à 100 millions » ; le magasin Elasticsearch est « expérimental » et ses versions futures peuvent être incompatibles.
- **SHACL : le cœur, SPARQL et des extensions expérimentales.** Les formes se chargent par une connexion normale (la mise à jour par SPARQL n'est pas prise en charge) ; `sh:entailment` n'est pas géré ; les extensions DASH et RSX sont à activer explicitement. Les gros chargements basculent en validation « en bloc » au-delà d'un seuil de 500 000 énoncés par défaut.
- **Des transactions concurrentes peuvent, ensemble, violer les formes** alors que chacune est valide seule : sous l'isolation SNAPSHOT la couche SHACL sérialise les validations au commit, ce que la documentation chiffre à deux à quatre fois plus rapide que SERIALIZABLE.
- **Version à recouper.** Le dépôt et le site ne donnent pas la même dernière release (6.0.0 contre 6.1.0).

## Écosystème

### Alternatives

- [[Apache Jena]] — Framework Java pour le web sémantique et serveur SPARQL Fuseki (Apache-2.0) — base RDF transactionnelle TDB2 sur une machine, raisonneurs RDFS et OWL partiels, validation SHACL ; pas de cluster décrit.
- [[Oxigraph]] — Base RDF et SPARQL en Rust sur RocksDB (Apache-2.0 ou MIT) — serveur en un binaire, bibliothèque Rust et paquet Python ; mono-nœud, sans SHACL ni raisonnement annoncés.

## Ressources

- Documentation — https://rdf4j.org/
- Dépôt — https://github.com/eclipse-rdf4j/rdf4j
- Documentation — serveur et Workbench : https://rdf4j.org/documentation/tools/server-workbench/
- Documentation — SHACL : https://rdf4j.org/documentation/programming/shacl/

## Voir aussi

- [[Ontologies et RDF]] — le hub du sous-domaine
- [[Comparatif - Moteurs RDF]] — ce qui départage les moteurs RDF
- [[SHACL]] — la notion : valider un graphe contre ses formes
- [[SPARQL]] — la notion : le langage de requête
