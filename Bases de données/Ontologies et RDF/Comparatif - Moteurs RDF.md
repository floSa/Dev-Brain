---
role: comparatif
nom: Comparatif - Moteurs RDF
categorie: database/rdf
tags: [rdf, sparql]
---

# Comparatif - Moteurs RDF

> On tranche sur : le graphe tient-il sur un nœud, faut-il du raisonnement ou de la validation SHACL **dans** le moteur, et sous quelle licence.

![[Comparatif - Moteurs RDF.base]]

## Les critères côte à côte

Relevé le 2026-10-19, à la source (README, documentation, fichier de licence, dépôt). « Non annoncé » veut dire que ni la documentation lue ni le dépôt n'en parlent, pas que la fonction est absente.

| Moteur | Modèle | Requête | Raisonnement | SHACL | Nœuds | Licence | Entretien |
|---|---|---|---|---|---|---|---|
| [[Apache Jena]] | RDF, graphes nommés | SPARQL 1.1 (GeoSPARQL en module) | RDFS et OWL partiels, règles | Core et SPARQL, service Fuseki à activer | un nœud | Apache-2.0 | 6.2.0 le 2026-07-31 |
| [[Oxigraph]] | RDF, graphes nommés | SPARQL 1.1, 1.2 préliminaire | non annoncé | non annoncé (voir [[pySHACL]]) | un nœud | Apache-2.0 ou MIT | 0.5.12 le 2026-10-18 |
| [[RDF4J]] | RDF, graphes nommés | SPARQL, fédération FedX | RDFS (couche dédiée) | Core et SPARQL, à chaque transaction | un nœud | BSD-3-Clause | 6.0.0 le 2026-08-10 |
| [[QLever]] | RDF | SPARQL 1.1 complet, plein texte, spatial | non annoncé | non annoncé | une machine | Apache-2.0 | 0.6.0 le 2026-08-13 |
| [[Virtuoso Open Source]] | relationnel et RDF | SPARQL et SQL | de base (sous-classes, `owl:sameAs`) | non relevé | un nœud (cluster : édition commerciale) | GPL v2 seule | 7.2.17 le 2026-05-07 |
| [[Fluree]] | RDF avec historique | SPARQL, JSON-LD, openCypher | RDFS, OWL 2 QL et RL, Datalog | à la transaction | un nœud ou cluster Raft | BUSL-1.1 | 4.2.4 le 2026-10-14 |
| [[Ontop]] | RDF **virtuel** sur SQL | SPARQL traduit en SQL | RDFS, OWL 2 QL par réécriture | non annoncé | sans stockage propre | Apache-2.0 | 5.5.0 le 2026-02-14 |

## Ce qui départage

- [[Apache Jena]] — raisonneurs RDFS et OWL, SHACL, serveur (Fuseki) et API Java dans un même projet de fondation ; un seul nœud, et des raisonneurs OWL que la documentation dit incomplets.
- [[Oxigraph]] — le plus simple à installer : un binaire Rust, une bibliothèque, un paquet Python ; version 0.x, évaluation de requêtes non optimisée d'après son README, ni raisonnement ni SHACL annoncés.
- [[RDF4J]] — la validation SHACL à chaque transaction et un serveur à déployer dans un conteneur de servlets ; Java 25 exigé depuis la 6.0, magasin natif décrit pour environ 100 millions de triplets.
- [[QLever]] — le moteur des très grands graphes sur une seule machine, avec plein texte et spatial ; il indexe avant de servir, sans raisonnement ni SHACL annoncés.
- [[Virtuoso Open Source]] — le seul à mêler du relationnel et du RDF dans un moteur, avec une inférence de base ; en GPL v2 seule, et cluster, réplication et règles sur mesure réservés à l'édition commerciale.
- [[Fluree]] — le plus riche sur le papier : historique interrogeable, SHACL, OWL 2 RL, cluster Raft ; mais BUSL-1.1 (pas une licence libre) et une version 4 dont la première préversion date d'avril 2026.
- [[Ontop]] — ne stocke rien : un graphe **virtuel** posé sur des bases SQL existantes, interrogé en SPARQL ; la bonne réponse quand les données sont déjà en tables, la mauvaise pour du RDF natif.

**Pas de fiche ici**, faute de licence libre, d'entretien ou de périmètre RDF :

- Blazegraph — GPL-2.0, mais dépôt **archivé** par son propriétaire, dernier push le 2023-04-16 et dernière release de 2020 : abandonné.
- TerminusDB — Apache-2.0 et actif (v12.0.8 le 2026-10-12), une base de graphes de documents JSON avec gestion de versions à la manière de git ; elle s'interroge en WOQL et en GraphQL et la documentation lue ne cite pas SPARQL : hors du périmètre RDF.
- GraphDB (Graphwise, ex-Ontotext) — moteur propriétaire construit sur RDF4J ; depuis la 11.0, l'édition gratuite exige une licence à demander au fournisseur, d'après un article secondaire d'août 2026 non recoupé à la source.
- AllegroGraph (Franz) — licence commerciale ; une édition gratuite plafonnée à 5 millions de triplets, d'après la documentation du fournisseur.
- Stardog et RDFox — produits commerciaux ; les conditions de leurs éditions gratuites n'ont pas été vérifiées à la source.
- Comunica (MIT) — cadre JavaScript pour **interroger** des sources RDF hétérogènes, pas un magasin ; version 5.4.1 du 2026-09-14. À examiner séparément si un besoin de requêtes fédérées côté Node se présente.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[Ontologies et RDF]] — le hub du dossier.
- [[Comparatif - Bases graphes]] — le comparatif voisin, pour le graphe de propriétés (Neo4j, Memgraph, JanusGraph).
- [[Bases graphe — modèles et langages de requête]] — la notion : graphe de propriétés ou RDF, Cypher ou SPARQL, avant de choisir un moteur.
- [[Comparatif - Outils RDF et OWL en Python]] — les bibliothèques et outils autour du moteur.
