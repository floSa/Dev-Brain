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
<!-- AUTO:END -->
