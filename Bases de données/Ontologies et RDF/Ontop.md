---
role: brique
nom: Ontop
alias: [ontop, Ontop VKG, Virtual Knowledge Graph, OBDA, graphe de connaissances virtuel]
pitch: "Plateforme Java qui expose des bases relationnelles comme un graphe RDF virtuel (Apache-2.0) — requêtes SPARQL traduites en SQL, mappings R2RML, ontologie OWL 2 QL ; les données restent dans la base d'origine."
categorie: database/rdf
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Java
scaling: single-node
alternatives: []
complements: ["[[Protégé]]"]
tags: [rdf, sparql, ontology]
url_docs: https://ontop-vkg.org/guide/
url_repo: https://github.com/ontop/ontop
---

# Ontop

<!-- AUTO:BANDEAU:START -->
> Plateforme Java qui expose des bases relationnelles comme un graphe RDF virtuel (Apache-2.0) — requêtes SPARQL traduites en SQL, mappings R2RML, ontologie OWL 2 QL ; les données restent dans la base d'origine.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Java | open-source | self-hébergé · mono-nœud | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme Java qui expose le contenu de bases relationnelles comme un **graphe de connaissances virtuel**, sans déplacer les données. Une requête SPARQL posée sur le graphe est traduite en SQL et exécutée par la base d'origine. Le lien entre tables et graphe est écrit dans des **mappings** (R2RML, ou le langage de mapping d'Ontop) ; une ontologie légère (RDFS, OWL 2 QL) enrichit les réponses. Elle se pilote en ligne de commande (point d'accès SPARQL, ou matérialisation du graphe virtuel en fichiers RDF) et par un plugin Protégé pour écrire et tester les mappings. Relevé le 2026-10-19 : version **5.5.0** (2026-02-14), Apache-2.0 (documentation en Creative Commons Attribution), dépôt actif (dernier push le 2026-10-15), environ 980 étoiles.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Les données vivent déjà dans PostgreSQL, SQL Server, Oracle, MySQL, DuckDB ou un entrepôt, et une copie RDF serait un second système à synchroniser | Du RDF natif, des écritures SPARQL ou de la validation SHACL : la documentation lue ne décrit ni les mises à jour ni SHACL |
| Une ontologie pour donner un vocabulaire commun à plusieurs bases (capteurs, équipements, ordres de travail) sans migration | Un raisonnement OWL riche : le profil retenu est OWL 2 QL, conçu pour se traduire en requêtes SQL |
| Des requêtes SPARQL avec agrégats et fonctions GeoSPARQL traduites en SQL | Des requêtes qui dépassent ce que la base d'origine sait faire vite : la performance dépend de la base et des mappings |
| Réutiliser des mappings R2RML existants | Un graphe qui n'existe pas encore en tables : voir [[Apache Jena]] ou [[Oxigraph]] |

## Mise en œuvre

- Installation — l'archive en ligne de commande du projet, le plugin Protégé, ou l'image Docker (liée depuis le dépôt)
- Point d'entrée — les mappings et l'ontologie en entrée, puis le point d'accès SPARQL ou la matérialisation en RDF
- Prérequis — une base relationnelle prise en charge (PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, DB2, Snowflake, Databricks, BigQuery, Redshift, DuckDB, DynamoDB, TDengine, d'après la documentation) et un accès à celle-ci ; Java 11 et Maven 3.6 pour compiler
- Exécution — self-hébergé ; mono-nœud (l'ordre de grandeur de la charge dépend de la base d'origine)
- Coût — gratuit, Apache-2.0

## Limites à connaître

- **Le graphe n'existe pas, ses réponses non plus sans la base.** L'indisponibilité de la base rend le graphe indisponible ; la qualité des réponses est celle des mappings.
- **Écriture et SHACL non documentés.** La page de présentation ne décrit ni mise à jour du graphe virtuel, ni validation ; pour valider des données tabulaires, passer par la base ou par un graphe matérialisé et [[pySHACL]].

## Écosystème

### Alternatives

- Aucune alternative déclarée : les autres moteurs RDF de ce dossier stockent leur propre copie du graphe, là où Ontop n'en stocke aucune.
- [[Apache Jena]] — voisin : quand le graphe se matérialise, un magasin RDF reçoit la copie produite par Ontop.

### Compléments

- [[Protégé]] — Éditeur d'ontologies OWL 2 à interface graphique, en Java (BSD-2-Clause) — classes, propriétés, requêtes DL, raisonneur HermiT intégré, plugins ; WebProtégé est sa version collaborative en ligne. — édite l'ontologie et, par le plugin d'Ontop, écrit et teste les mappings.

## Ressources

- Documentation — https://ontop-vkg.org/guide/
- Dépôt — https://github.com/ontop/ontop

## Voir aussi

- [[Ontologies et RDF]] — le hub du sous-domaine
- [[Comparatif - Moteurs RDF]] — ce qui départage les moteurs RDF
- [[Ontologie]] — la notion : décrire les types de choses d'un domaine
- [[SPARQL]] — la notion : le langage de requête
