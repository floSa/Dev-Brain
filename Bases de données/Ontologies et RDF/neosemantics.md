---
role: brique
nom: neosemantics
alias: [n10s, Neosemantics, neosemantics n10s]
pitch: "Plugin Neo4j (Apache-2.0, projet Neo4j Labs expérimental) qui importe et exporte du RDF depuis un graphe de propriétés — validation SHACL, import d'ontologies et de taxonomies, inférence de base ; Community et Enterprise auto-hébergés, pas Aura."
categorie: database/rdf
famille: extension
licence_type: open-source
maturite: experimental
langage: Java
alternatives: []
complements: []
tags: [rdf, knowledge-graph, graph-db]
url_docs: https://neo4j.com/labs/neosemantics/
url_repo: https://github.com/neo4j-labs/neosemantics
---

# neosemantics

<!-- AUTO:BANDEAU:START -->
> Plugin Neo4j (Apache-2.0, projet Neo4j Labs expérimental) qui importe et exporte du RDF depuis un graphe de propriétés — validation SHACL, import d'ontologies et de taxonomies, inférence de base ; Community et Enterprise auto-hébergés, pas Aura.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Extension Java | open-source | dans le moteur hôte, rien à héberger | experimental | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Plugin pour la base de graphes [[Neo4j]] qui y fait entrer et en fait sortir du **RDF** : un graphe de propriétés peut recevoir des triplets sans perte (ce qui a été importé peut être exporté sans perdre un seul triplet) et exporter ses données sous forme de RDF à la demande. Il lit et écrit Turtle, N-Triples, JSON-LD, RDF/XML, TriG, N-Quads et leurs variantes RDF-star ; il importe des ontologies et des taxonomies (OWL, RDFS, SKOS), met en correspondance un vocabulaire RDF et un modèle de propriétés, **valide le graphe par des formes SHACL** et fait de l'inférence de base. C'est un projet **Neo4j Labs**, hors de la gamme de produits supportés par Neo4j. Relevé le 2026-10-19 : version **2025.06.1** (2026-06-16, correctif d'une faille de la bibliothèque Jackson), licence Apache-2.0 (fichier `license.txt` lu), dépôt actif (dernier push le 2026-10-09), environ 970 étoiles.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Neo4j est déjà la base de graphes en place et il faut échanger du RDF avec d'autres systèmes (import d'un vocabulaire, export vers un magasin RDF) | Un besoin de graphe RDF natif avec SPARQL : voir [[Apache Jena]], [[Oxigraph]] ou [[RDF4J]] |
| Importer une ontologie ou une taxonomie SKOS comme données de référence dans un graphe de propriétés | Neo4j Aura (le service géré) : le plugin n'est pas disponible dessus ; la page du projet renvoie vers le pilote `rdflib-neo4j` |
| Valider un graphe de propriétés par SHACL sans exporter les données | Un outil supporté par un éditeur : le projet est un Labs expérimental, sans engagement de support |
| Un va-et-vient avec des formats RDF (Turtle, JSON-LD) à partir de Cypher | Une version de Neo4j que le plugin ne suit pas : ses numéros de release (5.26.0, puis 2025.06.1) semblent calqués sur ceux de Neo4j ; la table de compatibilité du manuel n'a pas été relevée |

## Mise en œuvre

- Installation — depuis Neo4j Desktop, par le bouton d'installation du plugin (README du projet) ; pour un serveur, suivre le manuel. Le point d'accès HTTP se monte par une ligne de configuration : `server.unmanaged_extension_classes=n10s.endpoint=/rdf`
- Point d'entrée — les procédures `n10s.*` appelées en Cypher, et le point d'accès HTTP `/rdf`
- Prérequis — Neo4j Community ou Enterprise auto-hébergé, dans une version que le plugin suit
- Exécution — en extension de Neo4j, sur le nœud de la base
- Coût — gratuit, Apache-2.0

## Limites à connaître

- **Expérimental par déclaration du projet.** Le README du dépôt (« projet expérimental Neo4j Labs, hors de la gamme de produits supportés ») et le fichier `LABS_DISCLAIMER.txt` le disent.
- **Pas de SPARQL.** On y passe des triplets, on interroge en Cypher : un graphe de propriétés n'est pas un magasin RDF. Voir [[Bases graphe — modèles et langages de requête]].
- **Pas sur Aura.** Le service géré de Neo4j n'accepte pas le plugin, d'après la page du projet.

## Écosystème

### Alternatives

- Aucune alternative déclarée : les moteurs RDF du dossier stockent du RDF natif, là où le plugin ajoute du RDF à un graphe de propriétés.
- [[Neo4j]] — voisin : la base qui héberge le plugin ; Community en GPLv3 et mono-instance.

## Ressources

- Documentation — https://neo4j.com/labs/neosemantics/
- Dépôt — https://github.com/neo4j-labs/neosemantics

## Voir aussi

- [[Ontologies et RDF]] — le hub du sous-domaine
- [[Bases de graphes]] — le hub de la base qui héberge le plugin
- [[Bases graphe — modèles et langages de requête]] — la notion : graphe de propriétés contre RDF
- [[RDF et triplets]] — la notion : sujet, prédicat, objet, graphes nommés
- [[SHACL]] — la notion : valider un graphe contre ses formes
