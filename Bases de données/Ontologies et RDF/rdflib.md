---
role: brique
nom: rdflib
alias: [RDFLib, RDFLib Python]
pitch: "Bibliothèque Python pour manipuler du RDF (BSD-3-Clause) — lit et écrit Turtle, JSON-LD et RDF/XML, interroge en SPARQL 1.1 (requêtes et mises à jour), graphe en mémoire ou persistant ; ce n'est pas un serveur."
categorie: database/rdf
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Owlready2]]"]
complements: ["[[pySHACL]]", "[[LinkML]]"]
tags: [rdf, sparql]
url_docs: https://rdflib.readthedocs.io/
url_repo: https://github.com/RDFLib/rdflib
---

# rdflib

<!-- AUTO:BANDEAU:START -->
> Bibliothèque Python pour manipuler du RDF (BSD-3-Clause) — lit et écrit Turtle, JSON-LD et RDF/XML, interroge en SPARQL 1.1 (requêtes et mises à jour), graphe en mémoire ou persistant ; ce n'est pas un serveur.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque Python pour manipuler du RDF : créer et parcourir un graphe de triplets, le lire et l'écrire dans les formats courants (RDF/XML, N3, N-Triples, N-Quads, Turtle, TriG, TriX, JSON-LD, HexTuples, RDFa, Microdata), l'interroger en **SPARQL 1.1**, requêtes et mises à jour. Un graphe vit en mémoire, sur disque (par exemple BerkeleyDB) ou derrière un point d'accès SPARQL distant, seul ou en jeu de données à plusieurs graphes nommés. C'est la brique de base de l'écosystème Python du web sémantique : pySHACL, par exemple, s'appuie dessus. Relevé le 2026-10-19 : version **7.6.0** (2026-02-13) sur PyPI, Python 3.8.1 ou plus, licence BSD-3-Clause, dépôt actif (dernier push du jour), environ 2 500 étoiles.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Lire, écrire, convertir ou fusionner des fichiers RDF (Turtle vers JSON-LD, par exemple) dans un script ou un pipeline Python | Un serveur multi-utilisateurs avec un point d'accès SPARQL : rdflib est une bibliothèque, pas un serveur ; voir [[Apache Jena]] ou [[Oxigraph]] |
| Une petite base de triplets embarquée, ou des requêtes SPARQL sur un fichier ou un point d'accès distant | Un très grand graphe : le graphe en mémoire pèse sur la RAM du processus ; mesurer, puis passer à un moteur dédié |
| Écrire ses tests ou ses vérifications autour d'un graphe, avec les outils qui l'étendent (validation, raisonnement) | Un raisonnement OWL complet : le raisonnement RDFS ou OWL-RL est un module à part (pySHACL dépend d'OWL-RL), et HermiT ou Pellet passent par [[Owlready2]] |
| Une API stable et documentée, en BSD-3-Clause | Du typage fort des instances d'ontologie en objets Python : voir [[Owlready2]] |

## Mise en œuvre

- Installation — `uv add rdflib` (extras optionnels pour des formats ou des stores précis)
- Point d'entrée — `rdflib.Graph()` : `parse()`, `serialize()`, `query()`, `update()`
- Prérequis — Python 3.8.1 ou plus ; le projet tire `isodate` et `pyparsing`
- Exécution — en bibliothèque, rien à héberger
- Coût — gratuit, BSD-3-Clause

## Écosystème

### Alternatives

- [[Owlready2]] — Module Python de programmation orientée ontologie (LGPL-3.0) — charge une ontologie OWL 2 comme des objets Python, raisonne avec HermiT ou Pellet (Java requis), stocke dans un quadstore SQLite ; dépôt hébergé sur Bitbucket.
- [[Oxigraph]] — voisin : son paquet `pyoxigraph` offre un magasin RDF embarqué, quand le graphe en mémoire de rdflib ne suffit plus.

### Compléments

- [[pySHACL]] — Validateur SHACL en Python pur (Apache-2.0), construit sur rdflib — vérifie un graphe RDF contre ses formes, en ligne de commande, en API ou en service HTTP ; peut développer le graphe par RDFS ou OWL-RL avant de valider. — valide un graphe rdflib contre des formes SHACL.
- [[LinkML]] — Langage de modélisation en YAML et sa boîte à outils Python (Apache-2.0) — un schéma unique génère JSON Schema, SHACL, OWL, ShEx, Pydantic ou SQL, et valide des données JSON, RDF ou TSV. — décrit le schéma en YAML et en tire SHACL, OWL ou JSON Schema ; un graphe rdflib se valide ensuite contre les formes SHACL générées.

## Ressources

- Documentation — https://rdflib.readthedocs.io/
- Dépôt — https://github.com/RDFLib/rdflib

## Voir aussi

- [[Ontologies et RDF]] — le hub du sous-domaine
- [[Comparatif - Outils RDF et OWL en Python]] — ce qui départage les outils Python
- [[RDF et triplets]] — la notion : sujet, prédicat, objet, graphes nommés, formats
- [[SPARQL]] — la notion : le langage de requête
