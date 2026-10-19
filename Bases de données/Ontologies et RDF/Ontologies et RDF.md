---
role: hub
nom: Ontologies et RDF
alias: [ontologies et RDF, web sémantique, semantic web, graphes de connaissances, knowledge graphs, RDF, ontologies, données liées]
pitch: Décrire des choses et leurs relations avec un sens partagé — ontologie, triplets RDF, SPARQL, OWL, SHACL, données liées — et tout ce qui s'y rattache, regroupé pour ne pas se perdre.
domaines: [data-eng, ai-eng]
tags: [knowledge-graph, rdf, ontology, sparql]
---

# Ontologies et RDF

> Décrire des choses et leurs relations avec un sens partagé — ontologie, triplets RDF, SPARQL, OWL, SHACL, données liées — et tout ce qui s'y rattache, regroupé pour ne pas se perdre.

## Ce qu'il faut comprendre

- **Point d'entrée : [[Graphe de connaissances]].** Elle dit ce que c'est, pose les deux modèles (graphe de propriétés, RDF) et porte une carte qui renvoie vers chaque autre page du sujet, y compris celles rangées ailleurs dans le brain. Si le sujet est neuf, commencer par elle.
- **Le sens est écrit, pas deviné.** Une [[Ontologie]] liste les types de choses et leurs relations ; [[RDF et triplets]] est le format qui les porte ; [[SPARQL]] les interroge ; [[OWL et raisonnement]] en déduit des faits non écrits ; [[SHACL]] vérifie que les données respectent les règles.
- **Ouvert contre fermé : la distinction à retenir.** OWL raisonne en monde ouvert (ce qui n'est pas écrit est inconnu), SHACL valide en monde fermé (ce qui manque est une erreur). Les confondre est l'erreur la plus fréquente.
- **Réutiliser avant d'inventer.** [[Données liées et vocabulaires partagés]] recense schema.org, SKOS, PROV-O, Wikidata ; [[Ontologies industrielles]] recense SOSA/SSN, ISA-95, la coque d'administration d'actif et IOF Core, pour l'usine et la maintenance prédictive.
- **Trois pages vivent dans d'autres dossiers, parce qu'elles suivent leur sujet technique** : [[Plongements de graphe et prédiction de liens]] (apprendre sur un graphe, dossier Machine Learning), [[Liage d'entités]] (partir du texte, dossier NLP) et [[Interroger un graphe en langage naturel]] (dossier Text-to-SQL). Toutes sont citées par la page d'entrée.
- **Le graphe de propriétés a son dossier.** [[Bases de graphes]] et [[Bases graphe — modèles et langages de requête]] couvrent Neo4j, Memgraph et leurs langages ; ce dossier-ci couvre le versant RDF et le sens partagé.

## Choisir

- Comprendre le sujet, ou y adresser quelqu'un → [[Graphe de connaissances]].
- Écrire le schéma d'un domaine → [[Ontologie]], après avoir regardé [[Données liées et vocabulaires partagés]] et [[Ontologies industrielles]].
- Vérifier la qualité des données entrantes → [[SHACL]].
- Déduire des faits → [[OWL et raisonnement]], en restant dans un profil (EL, QL ou RL) pour garder un temps prévisible.
- Interroger → [[SPARQL]] sur du RDF ; sur un graphe de propriétés, Cypher dans [[Bases graphe — modèles et langages de requête]].
- Héberger un graphe RDF sur site → [[Comparatif - Moteurs RDF]] : [[Apache Jena]] ou [[RDF4J]] pour le raisonnement et SHACL intégrés, [[Oxigraph]] pour la simplicité, [[QLever]] pour un très grand graphe sur une machine, [[Ontop]] quand les données sont déjà en tables SQL.
- Manipuler, valider ou concevoir en Python → [[Comparatif - Outils RDF et OWL en Python]] : [[rdflib]], [[pySHACL]], [[Owlready2]], [[LinkML]] ; l'éditeur graphique est [[Protégé]].
- Apprendre des plongements sur un graphe → [[PyKEEN]], fiche rangée dans le dossier Machine Learning avec sa notion.
- Pas de besoin de raisonnement ni d'échange entre systèmes → un graphe de propriétés ([[Bases de graphes]]) ou [[Postgres]] suffit souvent.

<!-- AUTO:START -->
### Notions
- [[Données liées et vocabulaires partagés]] — domaines : data-eng, ai-eng
- [[Graphe de connaissances]] — domaines : data-eng, ai-eng
- [[Ontologie]] — domaines : data-eng, ai-eng
- [[Ontologies industrielles]] — domaines : data-eng, ai-eng
- [[OWL et raisonnement]] — domaines : data-eng, ai-eng
- [[RDF et triplets]] — domaines : data-eng, ai-eng
- [[SHACL]] — domaines : data-eng, ai-eng
- [[SPARQL]] — domaines : data-eng, ai-eng

### Briques
- [[Apache Jena]] — Framework Java pour le web sémantique et serveur SPARQL Fuseki (Apache-2.0) — base RDF transactionnelle TDB2 sur une machine, raisonneurs RDFS et OWL partiels, validation SHACL ; pas de cluster décrit.
- [[Fluree]] — Base de graphes RDF en Rust, sous licence BUSL-1.1 — SPARQL, JSON-LD et openCypher, historique interrogeable, SHACL, raisonnement jusqu'à OWL 2 RL ; version 4 récente, et interdit d'en faire un service de base de données.
- [[LinkML]] — Langage de modélisation en YAML et sa boîte à outils Python (Apache-2.0) — un schéma unique génère JSON Schema, SHACL, OWL, ShEx, Pydantic ou SQL, et valide des données JSON, RDF ou TSV.
- [[neosemantics]] — Plugin Neo4j (Apache-2.0, projet Neo4j Labs expérimental) qui importe et exporte du RDF depuis un graphe de propriétés — validation SHACL, import d'ontologies et de taxonomies, inférence de base ; Community et Enterprise auto-hébergés, pas Aura.
- [[Ontop]] — Plateforme Java qui expose des bases relationnelles comme un graphe RDF virtuel (Apache-2.0) — requêtes SPARQL traduites en SQL, mappings R2RML, ontologie OWL 2 QL ; les données restent dans la base d'origine.
- [[Owlready2]] — Module Python de programmation orientée ontologie (LGPL-3.0) — charge une ontologie OWL 2 comme des objets Python, raisonne avec HermiT ou Pellet (Java requis), stocke dans un quadstore SQLite ; dépôt hébergé sur Bitbucket.
- [[Oxigraph]] — Base RDF et SPARQL en Rust sur RocksDB (Apache-2.0 ou MIT) — serveur en un binaire, bibliothèque Rust et paquet Python ; mono-nœud, sans SHACL ni raisonnement annoncés.
- [[Protégé]] — Éditeur d'ontologies OWL 2 à interface graphique, en Java (BSD-2-Clause) — classes, propriétés, requêtes DL, raisonneur HermiT intégré, plugins ; WebProtégé est sa version collaborative en ligne.
- [[pySHACL]] — Validateur SHACL en Python pur (Apache-2.0), construit sur rdflib — vérifie un graphe RDF contre ses formes, en ligne de commande, en API ou en service HTTP ; peut développer le graphe par RDFS ou OWL-RL avant de valider.
- [[QLever]] — Moteur SPARQL en C++ conçu pour de très grands graphes sur une seule machine (Apache-2.0) — SPARQL 1.1 complet, recherche textuelle, requêtes spatiales ; indexation préalable, sans SHACL ni raisonnement annoncés.
- [[RDF4J]] — Framework Java pour RDF et SPARQL (BSD-3-Clause, Eclipse) — magasins mémoire et natif, serveur et Workbench à déployer dans Tomcat ou Jetty, validation SHACL à chaque transaction ; mono-nœud.
- [[rdflib]] — Bibliothèque Python pour manipuler du RDF (BSD-3-Clause) — lit et écrit Turtle, JSON-LD et RDF/XML, interroge en SPARQL 1.1 (requêtes et mises à jour), graphe en mémoire ou persistant ; ce n'est pas un serveur.
- [[Virtuoso Open Source]] — Base multi-modèle (relationnel, graphe RDF, documents) et serveur HTTP en C (GPLv2) — SPARQL et Linked Data, inférence de base (sous-classes, owl:sameAs) ; cluster et réplication réservés à l'édition commerciale.

### Comparatifs
- [[Comparatif - Moteurs RDF]]
- [[Comparatif - Outils RDF et OWL en Python]]
<!-- AUTO:END -->
