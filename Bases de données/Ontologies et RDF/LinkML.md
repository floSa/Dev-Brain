---
role: brique
nom: LinkML
alias: [linkml, Linked Data Modeling Language]
pitch: "Langage de modélisation en YAML et sa boîte à outils Python (Apache-2.0) — un schéma unique génère JSON Schema, SHACL, OWL, ShEx, Pydantic ou SQL, et valide des données JSON, RDF ou TSV."
categorie: database/rdf
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: ["[[rdflib]]", "[[pySHACL]]"]
tags: [ontology, data-modeling, data-validation]
url_docs: https://linkml.io/linkml/
url_repo: https://github.com/linkml/linkml
---

# LinkML

<!-- AUTO:BANDEAU:START -->
> Langage de modélisation en YAML et sa boîte à outils Python (Apache-2.0) — un schéma unique génère JSON Schema, SHACL, OWL, ShEx, Pydantic ou SQL, et valide des données JSON, RDF ou TSV.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Langage de modélisation de données, et sa boîte à outils Python : le schéma s'écrit en YAML (classes, attributs, énumérations, contraintes), et des **générateurs** le compilent vers d'autres formats : JSON Schema, SHACL, OWL, ShEx, SQL (DDL), Pydantic, classes Python, TypeScript, et de la documentation. La même description sert aussi à valider des données JSON, RDF ou TSV et à les convertir d'une représentation à l'autre. Le méta-modèle de LinkML est lui-même écrit en LinkML. Relevé le 2026-10-19 : version **1.12.1** (2026-10-13), Python 3.10 ou plus, licence Apache-2.0, dépôt actif (dernier push du jour), environ 660 étoiles.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Une seule source de vérité pour le schéma d'un domaine, d'où l'on tire des formes SHACL, un schéma JSON, des modèles Pydantic et une table SQL | Concevoir une ontologie pour raisonner : OWL n'est ici qu'une sortie parmi d'autres, et la documentation lue ne décrit aucun raisonnement ; voir [[Protégé]] |
| Des équipes qui échangent des données dans plusieurs formats (JSON, CSV, RDF) sans réinventer le schéma pour chacun | Un besoin purement RDF avec SHACL à la main : voir [[pySHACL]] |
| Générer une documentation lisible du modèle de données | Un schéma de base relationnelle seul : un outil de migration ([[Alembic]]) suffit |
| Aligner un modèle sur des vocabulaires partagés (cf. [[Données liées et vocabulaires partagés]]) | Une dépendance minimale : la boîte à outils est large |

## Mise en œuvre

- Installation — `uv add linkml`
- Point d'entrée — un fichier de schéma YAML, puis le générateur du format voulu (un par cible, listés dans la documentation) ou la commande de validation
- Prérequis — Python 3.10 ou plus
- Exécution — en bibliothèque et en commande, rien à héberger
- Coût — gratuit, Apache-2.0

## Limites à connaître

- **Un générateur ne vaut que ce que la cible sait dire.** SHACL, OWL et JSON Schema n'expriment pas les mêmes choses ; la documentation lue ne chiffre aucune perte à la traduction. Relire la sortie générée, ne pas la croire équivalente au schéma.
- **Le monde ouvert d'OWL et le monde fermé de SHACL** ne coïncident pas : le même schéma ne donne pas les mêmes réponses dans les deux. Voir [[SHACL]] et [[OWL et raisonnement]].
- **Largeur de l'outil.** Beaucoup de générateurs : épingler les versions et ne garder que ceux dont le projet a besoin.

## Écosystème

### Alternatives

- Aucune alternative déclarée : aucune autre brique du dossier ne décrit un schéma une seule fois pour le compiler vers plusieurs formats.

### Compléments

- [[rdflib]] — Bibliothèque Python pour manipuler du RDF (BSD-3-Clause) — lit et écrit Turtle, JSON-LD et RDF/XML, interroge en SPARQL 1.1 (requêtes et mises à jour), graphe en mémoire ou persistant ; ce n'est pas un serveur. — manipule les données RDF que LinkML décrit, valide ou convertit.
- [[pySHACL]] — Validateur SHACL en Python pur (Apache-2.0), construit sur rdflib — vérifie un graphe RDF contre ses formes, en ligne de commande, en API ou en service HTTP ; peut développer le graphe par RDFS ou OWL-RL avant de valider. — applique les formes SHACL générées depuis le schéma.

## Ressources

- Documentation — https://linkml.io/linkml/
- Dépôt — https://github.com/linkml/linkml

## Voir aussi

- [[Ontologies et RDF]] — le hub du sous-domaine
- [[Comparatif - Outils RDF et OWL en Python]] — ce qui départage les outils Python
- [[Ontologie]] — la notion : décrire les types de choses d'un domaine
- [[SHACL]] — la notion : valider un graphe contre ses formes
