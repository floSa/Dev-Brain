---
role: comparatif
nom: Comparatif - Outils RDF et OWL en Python
categorie: database/rdf
tags: [rdf, ontology]
---

# Comparatif - Outils RDF et OWL en Python

> On tranche sur : ce que l'outil fait du graphe (le manipuler, le valider, charger une ontologie, décrire un schéma), ce qu'il demande autour de lui (Java pour raisonner), et sa licence.

![[Comparatif - Outils RDF et OWL en Python.base]]

Le premier onglet de la vue réunit les outils Python. Le second, « Hors Python », complète le tableau avec les deux fiches du dossier qui ne sont pas des paquets Python : l'éditeur d'ontologies [[Protégé]] et le plugin [[neosemantics]] pour Neo4j. Les moteurs RDF ont leur comparatif : [[Comparatif - Moteurs RDF]].

## Les critères côte à côte

Relevé le 2026-10-19, à la source (PyPI, README, documentation, fichier de licence).

| Outil | Rôle | S'appuie sur | Java | Licence | Version |
|---|---|---|---|---|---|
| [[rdflib]] | graphes RDF, formats, SPARQL 1.1 | pyparsing, isodate | non | BSD-3-Clause | 7.6.0 le 2026-02-13 |
| [[pySHACL]] | validation SHACL | rdflib, OWL-RL | non | Apache-2.0 | 0.40.1 le 2026-07-28 |
| [[Owlready2]] | ontologie OWL 2 en objets Python, raisonnement | quadstore SQLite | **oui**, pour raisonner | LGPL-3.0 ou plus (Pellet modifié en AGPL) | 0.51 le 2026-06-22 |
| [[LinkML]] | schéma YAML compilé en SHACL, OWL, JSON Schema, Pydantic… | — | non | Apache-2.0 | 1.12.1 le 2026-10-13 |
| [[Protégé]] | édition graphique d'ontologies OWL 2 | — | application Java | BSD à deux clauses | 5.6.9 le 2026-03-07 |
| [[neosemantics]] | RDF dans Neo4j, SHACL | Neo4j Community ou Enterprise | plugin Java | Apache-2.0 | 2025.06.1 le 2026-06-16 |

## Ce qui départage

- [[rdflib]] — le socle : lire, écrire, interroger un graphe ; la validation et le raisonnement sont des modules à part, et les autres outils s'y branchent.
- [[pySHACL]] — la validation SHACL en Python pur, utilisable en CI ; version 0.x, et le taux de réussite aux tests W3C n'a pas été relevé.
- [[Owlready2]] — la voie Python du dossier pour **raisonner** sur de l'OWL 2 avec un raisonneur (HermiT, Pellet), au prix d'une machine Java ; développé sur Bitbucket par un auteur principal, avec une copie GitHub périmée.
- [[LinkML]] — le seul à partir d'un **schéma** plutôt que d'un graphe ou d'une ontologie : une description, plusieurs sorties (dont SHACL et OWL) ; ce qui ne se traduit pas à l'identique est à relire.
- [[Protégé]] — l'éditeur graphique, pas une bibliothèque : on y conçoit l'ontologie à la main avant de la manipuler dans du code.
- [[neosemantics]] — la passerelle RDF pour un Neo4j déjà en place, expérimentale par déclaration (Neo4j Labs), sans SPARQL.

**Hors de ce comparatif, mais dans le brain** : [[PyKEEN]] (plongements de graphes de connaissances, dossier Machine Learning), qui s'entraîne sur un graphe de triplets.

**Pas de fiche ici** :

- OWL-RL — module du même projet que rdflib qui déduit les conséquences du profil OWL 2 RL ; dépendance de pySHACL, cité ici sans fiche parce que sa licence et son entretien n'ont pas été relevés à la source.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[Ontologies et RDF]] — le hub du dossier.
- [[Comparatif - Moteurs RDF]] — le comparatif voisin, pour les bases et serveurs RDF.
- [[SHACL]] — la notion : valider un graphe contre ses formes.
- [[OWL et raisonnement]] — la notion : déduire des faits non écrits.
