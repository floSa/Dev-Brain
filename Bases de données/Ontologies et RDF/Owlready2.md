---
role: brique
nom: Owlready2
alias: [owlready2, Owlready, programmation orientée ontologie]
pitch: "Module Python de programmation orientée ontologie (LGPL-3.0) — charge une ontologie OWL 2 comme des objets Python, raisonne avec HermiT ou Pellet (Java requis), stocke dans un quadstore SQLite ; dépôt hébergé sur Bitbucket."
categorie: database/rdf
famille: paquet
licence_type: open-source
maturite: beta
langage: Python
alternatives: ["[[rdflib]]"]
complements: ["[[Protégé]]"]
tags: [ontology, rdf]
url_docs: https://owlready2.readthedocs.io/
url_repo: https://bitbucket.org/jibalamy/owlready2
---

# Owlready2

<!-- AUTO:BANDEAU:START -->
> Module Python de programmation orientée ontologie (LGPL-3.0) — charge une ontologie OWL 2 comme des objets Python, raisonne avec HermiT ou Pellet (Java requis), stocke dans un quadstore SQLite ; dépôt hébergé sur Bitbucket.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Module Python de **programmation orientée ontologie** : il charge une ontologie OWL 2 et en fait des objets Python (les classes de l'ontologie deviennent des classes Python, les individus des instances), qu'on modifie puis sauvegarde. Il sait lancer un raisonneur pour classer les classes et les individus, interroger en SPARQL (avec son propre moteur, ou par rdflib), et stocker le tout dans un quadstore optimisé sur SQLite. Il est écrit par Jean-Baptiste Lamy (LIMICS) ; les auteurs demandent de le citer dans un travail scientifique. Relevé le 2026-10-19 : version **0.51** (2026-06-22) sur PyPI, licence LGPL-3.0 ou plus, dernier commit du dépôt le **2026-08-11**. Le dépôt de référence est sur **Bitbucket** ; une copie GitHub (`pwin/owlready2`) existe mais son dernier push date de janvier 2023.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Manipuler une ontologie OWL 2 depuis du code Python, comme on manipule des objets (créer une classe, ajouter une méthode, classer un individu) | Des graphes RDF de données sans ontologie : voir [[rdflib]] |
| Raisonner dans un script : HermiT (par défaut) ou Pellet classent classes et individus, et les faits déduits se retrouvent dans l'ontologie | Une machine sans Java : « il faut une machine virtuelle Java pour raisonner » avec Owlready2, d'après la documentation |
| Charger des ontologies volumineuses : la documentation indique qu'Owlready2 y est conçu, à la différence de la version 1 | Une licence sans réciprocité : LGPL pour Owlready2 et HermiT, mais le Pellet modifié qui accompagne est en AGPL ; lire la licence avant de redistribuer |
| Un éditeur graphique à côté pour concevoir l'ontologie : [[Protégé]] | Une validation SHACL : Owlready2 ne la porte pas ; voir [[pySHACL]] |

## Mise en œuvre

- Installation — `uv add owlready2`
- Point d'entrée — `get_ontology(...).load()`, puis `sync_reasoner()` (HermiT) ou `sync_reasoner_pellet()`
- Prérequis — Python 3 et, pour raisonner, une machine virtuelle Java
- Exécution — en bibliothèque, quadstore SQLite dans un fichier ou en mémoire
- Coût — gratuit, LGPL-3.0 ou plus

## Limites à connaître

- **Les faits déduits vont dans une ontologie à part par défaut.** Ils atterrissent dans `http://inferrences/` ; pour les conserver, encadrer l'appel au raisonneur par `with onto:` puis sauvegarder.
- **Une copie GitHub périmée circule.** Le dépôt `pwin/owlready2` n'a pas bougé depuis janvier 2023 : le code à suivre est sur Bitbucket et sur PyPI.
- **Un projet porté par un auteur principal**, d'après PyPI. Les trois derniers commits du dépôt Bitbucket datent du 2026-06-22, du 2026-06-24 et du 2026-08-11 : activité réelle mais discrète, à peser pour une dépendance critique.
- **SWRL : seulement la création, l'affichage et la modification manuelle** des règles d'après la page lue ; la prise en charge par chaque raisonneur n'a pas été relevée.

## Écosystème

### Alternatives

- [[rdflib]] — Bibliothèque Python pour manipuler du RDF (BSD-3-Clause) — lit et écrit Turtle, JSON-LD et RDF/XML, interroge en SPARQL 1.1 (requêtes et mises à jour), graphe en mémoire ou persistant ; ce n'est pas un serveur.
- [[Apache Jena]] — voisin : son API d'ontologies et ses raisonneurs, côté Java, quand l'application n'est pas en Python.

### Compléments

- [[Protégé]] — Éditeur d'ontologies OWL 2 à interface graphique, en Java (BSD-2-Clause) — classes, propriétés, requêtes DL, raisonneur HermiT intégré, plugins ; WebProtégé est sa version collaborative en ligne. — édite l'ontologie qu'Owlready2 charge ensuite en objets Python.

## Ressources

- Documentation — https://owlready2.readthedocs.io/
- Dépôt — https://bitbucket.org/jibalamy/owlready2
- Documentation — le raisonnement : https://owlready2.readthedocs.io/en/latest/reasoning.html

## Voir aussi

- [[Ontologies et RDF]] — le hub du sous-domaine
- [[Comparatif - Outils RDF et OWL en Python]] — ce qui départage les outils Python
- [[OWL et raisonnement]] — la notion : déduire des faits non écrits
- [[Ontologie]] — la notion : décrire les types de choses d'un domaine
