---
role: brique
nom: Virtuoso Open Source
alias: [Virtuoso, VOS, OpenLink Virtuoso, virtuoso-opensource]
pitch: "Base multi-modèle (relationnel, graphe RDF, documents) et serveur HTTP en C (GPLv2) — SPARQL et Linked Data, inférence de base (sous-classes, owl:sameAs) ; cluster et réplication réservés à l'édition commerciale."
categorie: database/rdf
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: C
scaling: single-node
alternatives: ["[[Apache Jena]]", "[[QLever]]"]
complements: []
tags: [rdf, sparql, relational]
url_docs: https://docs.openlinksw.com/virtuoso/
url_repo: https://github.com/openlink/virtuoso-opensource
---

# Virtuoso Open Source

<!-- AUTO:BANDEAU:START -->
> Base multi-modèle (relationnel, graphe RDF, documents) et serveur HTTP en C (GPLv2) — SPARQL et Linked Data, inférence de base (sous-classes, owl:sameAs) ; cluster et réplication réservés à l'édition commerciale.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme C | open-source | self-hébergé · mono-nœud | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Édition libre de Virtuoso, la base de données d'OpenLink Software qui réunit dans un seul moteur des tables relationnelles, un graphe RDF et des documents, avec un serveur d'applications HTTP et des connecteurs ODBC et JDBC. Le versant RDF s'interroge en SPARQL et sert à publier des données liées (Linked Data) ; le droit d'auteur du projet court depuis 1998. Relevé le 2026-10-19 : version **7.2.17** (2026-05-07), branche de développement `develop/7`, dépôt actif (dernier push le 2026-10-12), environ 975 étoiles. Licence : **GPL version 2 seulement** (« la seule version valide est la GPL v2 de 1991 »), avec une exemption qui autorise le lien avec OpenSSL.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un même moteur pour du relationnel (SQL, ODBC, JDBC) et du graphe RDF interrogé en SPARQL | Un cluster ou une réplication : le cluster est réservé à l'édition commerciale, d'après la documentation d'OpenLink |
| Publier des données liées avec un serveur HTTP intégré | Embarquer ou redistribuer le moteur dans un produit fermé : la GPL v2 est copyleft : un produit dérivé redistribué doit l'être sous GPL v2 |
| Une inférence légère sans raisonneur à part : sous-classes, sous-propriétés, `owl:sameAs`, `owl:equivalentClass`, `owl:inverseOf` | Des règles d'inférence sur mesure : elles sont décrites comme un avantage de l'édition commerciale |
| Un moteur ancien, en paquets pour Linux, macOS et Windows ou en Docker | Une validation SHACL : aucune prise en charge n'a été relevée dans les sources lues |
| Un dépôt actif et une licence libre, sous réserve de la lire | Un graphe énorme et seulement RDF, avec un outil plus récent et plus simple : voir [[QLever]] ou [[Oxigraph]] |

## Mise en œuvre

- Installation — paquets précompilés (Linux, macOS, Windows), Docker, Maven ou compilation depuis les sources, d'après le site du projet
- Point d'entrée — le point d'accès SPARQL du serveur HTTP, l'interface web d'administration, ou une connexion SQL (ODBC, JDBC)
- Prérequis — rien de relevé ; la documentation OpenLink détaille le dimensionnement
- Exécution — self-hébergé ; mono-nœud pour l'édition libre
- Coût — gratuit en GPL v2 ; l'édition commerciale d'OpenLink porte le cluster, la réplication et les règles d'inférence sur mesure

## Limites à connaître

- **Deux éditions, une frontière floue.** Le dépôt libre est celui de ce fichier ; le cluster à réplication et les règles d'inférence personnalisées (écrites en SPARQL, avec le vocabulaire SPIN) sont annoncés comme propres à l'édition commerciale. Lire les pages d'OpenLink sur les éditions avant de bâtir une architecture sur une fonction.
- **L'inférence est une liste de cas, pas un raisonneur OWL.** Les règles se déclarent par des directives SPARQL et des jeux de règles rattachés à des graphes nommés ; pour OWL, voir [[OWL et raisonnement]].

## Écosystème

### Alternatives

- [[Apache Jena]] — Framework Java pour le web sémantique et serveur SPARQL Fuseki (Apache-2.0) — base RDF transactionnelle TDB2 sur une machine, raisonneurs RDFS et OWL partiels, validation SHACL ; pas de cluster décrit.
- [[QLever]] — Moteur SPARQL en C++ conçu pour de très grands graphes sur une seule machine (Apache-2.0) — SPARQL 1.1 complet, recherche textuelle, requêtes spatiales ; indexation préalable, sans SHACL ni raisonnement annoncés.
- [[Oxigraph]] — voisin : la base RDF la plus simple à installer, sans le serveur d'applications ni le moteur relationnel.

## Ressources

- Documentation — https://docs.openlinksw.com/virtuoso/
- Dépôt — https://github.com/openlink/virtuoso-opensource
- Documentation — le wiki du projet : https://vos.openlinksw.com/owiki/wiki/VOS

## Voir aussi

- [[Ontologies et RDF]] — le hub du sous-domaine
- [[Comparatif - Moteurs RDF]] — ce qui départage les moteurs RDF
- [[SPARQL]] — la notion : le langage de requête
- [[Données liées et vocabulaires partagés]] — la notion : publier des données liées
