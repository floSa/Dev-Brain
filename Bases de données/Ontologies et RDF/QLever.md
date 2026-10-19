---
role: brique
nom: QLever
alias: [qlever, QLever SPARQL engine]
pitch: "Moteur SPARQL en C++ conçu pour de très grands graphes sur une seule machine (Apache-2.0) — SPARQL 1.1 complet, recherche textuelle, requêtes spatiales ; indexation préalable, sans SHACL ni raisonnement annoncés."
categorie: database/rdf
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: beta
langage: C++
scaling: single-node
alternatives: ["[[Apache Jena]]", "[[Oxigraph]]", "[[Virtuoso Open Source]]"]
complements: []
tags: [rdf, sparql]
url_docs: https://docs.qlever.dev/
url_repo: https://github.com/ad-freiburg/qlever
---

# QLever

<!-- AUTO:BANDEAU:START -->
> Moteur SPARQL en C++ conçu pour de très grands graphes sur une seule machine (Apache-2.0) — SPARQL 1.1 complet, recherche textuelle, requêtes spatiales ; indexation préalable, sans SHACL ni raisonnement annoncés.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme C++ | open-source | self-hébergé · mono-nœud | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Moteur de base de données RDF et SPARQL écrit en C++ (dépôt `ad-freiburg`, groupe de l'université de Fribourg-en-Brisgau), pensé pour interroger de très grands graphes sur **une seule machine**. Il annonce l'implémentation de SPARQL 1.1 en entier (requêtes fédérées, graphes nommés, protocole de stockage de graphes, mises à jour) et ajoute de la recherche plein texte, des requêtes spatiales avec carte, des vues matérialisées et une analyse de requête en direct. Tout se pilote par un outil unique, `qlever`, et un fichier de configuration `Qleverfile` : télécharger les données, **construire l'index**, puis démarrer le serveur. Relevé le 2026-10-19 : version **0.6.0** (2026-08-13), Apache-2.0, dépôt actif (dernier push du jour), environ 900 étoiles.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un très grand graphe (le projet montre plus d'un billion de triplets sur un seul PC) interrogé en lecture surtout | Du raisonnement OWL ou RDFS, ou une validation SHACL : la documentation lue n'en parle pas |
| Du plein texte et des requêtes spatiales dans le même moteur que SPARQL | Un cluster, une réplication ou une haute disponibilité : la description est celle d'une seule machine |
| Une installation par paquet Debian ou Ubuntu, Homebrew (Apple Silicon) ou conteneur, pilotée par une seule commande | Un graphe qui change sans cesse par petites écritures : l'usage décrit est « indexer d'abord, servir ensuite » ; les mises à jour existent mais leur maturité n'a pas été relevée |
| Un point d'accès SPARQL public sur un jeu de données stable (type Wikidata, DBLP) | Une interface de gestion, des rôles et des sauvegardes d'entreprise : voir [[Apache Jena]] |
| Mesurer son propre cas : le projet publie des comparaisons avec Jena et Oxigraph | Un projet qui exige une API figée : le projet se dit « en développement actif et rapide » |

## Mise en œuvre

- Installation — paquet Debian ou Ubuntu (`apt`), Homebrew sur Apple Silicon, sinon `pip`, `pipx` ou `uv` avec exécution dans un conteneur, au prix d'une performance moindre, d'après le guide de démarrage
- Point d'entrée — `qlever setup-config`, `qlever get-data`, `qlever index`, `qlever start`, puis `qlever query` ou `qlever ui`
- Prérequis — de la mémoire et du disque en rapport avec le graphe : le guide ne chiffre rien, à mesurer sur ses données
- Exécution — self-hébergé ; mono-nœud
- Coût — gratuit, Apache-2.0

## Limites à connaître

- **Les chiffres de performance viennent du projet.** Les comparaisons (DBLP, Wikidata Truthy) sont publiées par ses auteurs ; une évaluation de 2023 sur Wikidata, repérée par recherche web et non ouverte, est antérieure aux versions actuelles. À refaire sur ses données.
- **Le wiki est annoncé comme potentiellement périmé**, et la version est en 0.x : lire la documentation du site plutôt que le wiki.
- **Pas de raisonnement ni de SHACL annoncés.** Le travail d'inférence et de validation passe par un autre outil, avant ou après le chargement.

## Écosystème

### Alternatives

- [[Apache Jena]] — Framework Java pour le web sémantique et serveur SPARQL Fuseki (Apache-2.0) — base RDF transactionnelle TDB2 sur une machine, raisonneurs RDFS et OWL partiels, validation SHACL ; pas de cluster décrit.
- [[Oxigraph]] — Base RDF et SPARQL en Rust sur RocksDB (Apache-2.0 ou MIT) — serveur en un binaire, bibliothèque Rust et paquet Python ; mono-nœud, sans SHACL ni raisonnement annoncés.
- [[Virtuoso Open Source]] — Base multi-modèle (relationnel, graphe RDF, documents) et serveur HTTP en C (GPLv2) — SPARQL et Linked Data, inférence de base (sous-classes, owl:sameAs) ; cluster et réplication réservés à l'édition commerciale.

## Ressources

- Documentation — https://docs.qlever.dev/
- Dépôt — https://github.com/ad-freiburg/qlever
- Documentation — démarrage : https://docs.qlever.dev/quickstart/

## Voir aussi

- [[Ontologies et RDF]] — le hub du sous-domaine
- [[Comparatif - Moteurs RDF]] — ce qui départage les moteurs RDF
- [[SPARQL]] — la notion : le langage que QLever implémente
