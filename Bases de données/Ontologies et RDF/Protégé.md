---
role: brique
nom: Protégé
alias: [Protege, Protégé Desktop, WebProtégé]
pitch: "Éditeur d'ontologies OWL 2 à interface graphique, en Java (BSD-2-Clause) — classes, propriétés, requêtes DL, raisonneur HermiT intégré, plugins ; WebProtégé est sa version collaborative en ligne."
categorie: database/rdf
famille: application
licence_type: open-source
hosted: [self]
maturite: production
langage: Java
scaling: single-node
alternatives: []
complements: ["[[Owlready2]]", "[[Ontop]]"]
tags: [ontology]
url_docs: https://protegeproject.github.io/protege/
url_repo: https://github.com/protegeproject/protege
---

# Protégé

<!-- AUTO:BANDEAU:START -->
> Éditeur d'ontologies OWL 2 à interface graphique, en Java (BSD-2-Clause) — classes, propriétés, requêtes DL, raisonneur HermiT intégré, plugins ; WebProtégé est sa version collaborative en ligne.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application Java | open-source | self-hébergé · mono-nœud | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Application de bureau, en Java, pour **concevoir et relire une ontologie OWL 2** : on y crée les classes, les propriétés et les individus, on déclare leurs liens, puis on lance un raisonneur pour vérifier que l'ontologie est cohérente et pour voir ce qu'elle déduit. Elle vient de l'université Stanford, et son architecture à plugins permet d'ajouter des raisonneurs et des vues. Une version collaborative en ligne, **WebProtégé**, existe à côté. Relevé le 2026-10-19 : Protégé Desktop **5.6.9** (2026-03-07), documentation officielle de cette version, dépôt actif (dernier push le 2026-10-01), licence BSD à deux clauses (fichier `license.txt` lu).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Concevoir ou relire une ontologie à la main, avec des vues par classes, propriétés et individus | Automatiser la construction d'ontologies dans un pipeline : voir [[Owlready2]] pour la manipuler en Python |
| Vérifier la cohérence d'une ontologie : le raisonneur HermiT est intégré, Pellet et FaCT++ se téléchargent | Un travail collaboratif sans poste partagé : la version en ligne WebProtégé est un autre produit, dont la licence n'a pas été relevée |
| Poser des requêtes DL sur l'ontologie classée (onglet DL Query) | Interroger des données à grande échelle : Protégé édite des ontologies, il ne sert pas de base ; voir [[Apache Jena]] ou [[RDF4J]] |
| Écrire et tester des mappings Ontop, par le plugin du projet [[Ontop]] | Définir un schéma de données pour plusieurs formats : voir [[LinkML]] |

## Mise en œuvre

- Installation — les téléchargements du site du projet et les versions du dépôt `protege-distribution` ; des guides existent pour Windows, macOS et Linux
- Point d'entrée — l'interface graphique : onglets Active Ontology, Entities, DL Query, OWLViz (qui demande GraphViz)
- Prérequis — Java (version non relevée dans la documentation lue : voir le guide d'installation de la plate-forme)
- Exécution — poste de travail ; un fichier d'ontologie, pas de serveur
- Coût — gratuit, BSD à deux clauses

## Limites à connaître

- **C'est un éditeur, pas un moteur.** Il charge et enregistre des ontologies ; pour des données volumineuses, un magasin RDF prend le relais.
- **Les raisonneurs ne se valent pas.** HermiT est livré ; d'autres (Pellet, FaCT++) s'ajoutent. Le choix pèse sur ce qui se déduit et sur le temps. Voir [[OWL et raisonnement]].
- **GitHub ne détecte pas la licence du dépôt `protege`.** Le fichier `license.txt`, lu en entier, contient bien deux clauses de redistribution et la clause de non-garantie de la BSD à deux clauses (Stanford) ; le dépôt `protege-distribution` la déclare.

## Écosystème

### Alternatives

- Aucune alternative déclarée : aucun autre éditeur d'ontologies n'a de fiche dans le brain.

### Compléments

- [[Owlready2]] — Module Python de programmation orientée ontologie (LGPL-3.0) — charge une ontologie OWL 2 comme des objets Python, raisonne avec HermiT ou Pellet (Java requis), stocke dans un quadstore SQLite ; dépôt hébergé sur Bitbucket. — charge en objets Python l'ontologie conçue dans Protégé.
- [[Ontop]] — Plateforme Java qui expose des bases relationnelles comme un graphe RDF virtuel (Apache-2.0) — requêtes SPARQL traduites en SQL, mappings R2RML, ontologie OWL 2 QL ; les données restent dans la base d'origine. — fournit un plugin Protégé pour écrire et tester les mappings vers le graphe virtuel.

## Ressources

- Documentation — https://protegeproject.github.io/protege/
- Dépôt — https://github.com/protegeproject/protege
- Documentation — le site du projet : https://protege.stanford.edu/

## Voir aussi

- [[Ontologies et RDF]] — le hub du sous-domaine
- [[Ontologie]] — la notion : décrire les types de choses d'un domaine
- [[OWL et raisonnement]] — la notion : déduire des faits non écrits
- [[Ontologies industrielles]] — la notion : SOSA/SSN, ISA-95, coque d'administration d'actif
