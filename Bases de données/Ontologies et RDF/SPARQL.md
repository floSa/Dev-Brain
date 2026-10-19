---
role: notion
nom: SPARQL
alias: [SPARQL 1.1, langage de requête RDF, SPARQL endpoint, point d'accès SPARQL, chemins de propriétés, property paths, SPARQL Update]
categorie: database/rdf
domaines: [data-eng, ai-eng]
tags: [sparql, rdf, knowledge-graph]
---

# SPARQL

## Aperçu

- **SPARQL** est le langage W3C pour **interroger un graphe RDF**. Une requête décrit un **motif de triplets** avec des variables ; le moteur rend toutes les façons de remplir les variables pour que le motif existe dans le graphe.
- SPARQL 1.1 est une famille de **onze Recommandations**, dont le langage de requête (21 mars 2013), le langage de mise à jour (Update), le protocole HTTP (le « point d'accès » SPARQL, ou *endpoint*), les requêtes fédérées et les formats de résultats (XML, JSON, CSV, TSV).
- C'est à RDF ce que SQL est aux tables et ce que Cypher est au graphe de propriétés : le langage qu'un moteur de [[RDF et triplets]] parle, normalisé, donc **portable entre moteurs**.

## Concepts clés

### Un motif, des variables

```sparql
PREFIX ex: <http://example.org/usine#>

SELECT ?pompe ?capteur
WHERE {
  ?pompe   a ex:Pompe ;
           ex:installéeSur ex:Ligne2 ;
           ex:équipéeDe    ?capteur .
  ?capteur a ex:CapteurVibration .
}
```

- Chaque ligne du `WHERE` est un motif de triplet ; `?pompe` est une variable ; la syntaxe `;` répète le sujet comme en Turtle ([[RDF et triplets]]).
- Il n'y a **pas de jointure écrite** : deux motifs qui partagent une variable (`?capteur`) sont joints d'office.

### Les quatre formes de requête

| Forme | Rend | Usage |
|---|---|---|
| `SELECT` | un tableau de valeurs de variables | cas courant, résultats pour un tableau de bord |
| `CONSTRUCT` | un **nouveau graphe RDF** construit depuis un gabarit | transformer, aligner deux vocabulaires |
| `ASK` | vrai ou faux | tester qu'un motif existe |
| `DESCRIBE` | un graphe qui décrit les ressources trouvées | exploration ; le contenu dépend du moteur (le W3C le marque informatif) |

### Modificateurs usuels

- `OPTIONAL { … }` : ajoute des valeurs **si** le motif existe, sinon garde la ligne (équivalent d'une jointure externe).
- `FILTER (expression)` : garde les solutions où l'expression est vraie (comparaisons, `regex`, `NOT EXISTS`).
- Agrégats : `COUNT`, `SUM`, `MIN`, `MAX`, `AVG`, `GROUP_CONCAT`, `SAMPLE`, avec `GROUP BY` et `HAVING`.
- `SERVICE <endpoint> { … }` : délègue un sous-motif à un **autre** point d'accès (requêtes fédérées).
- **Update** : `INSERT DATA`, `DELETE/INSERT … WHERE` modifient le graphe.

### Chemins de propriétés

Les chemins parcourent des arêtes de longueur variable, sans récursion écrite :

| Opérateur | Sens |
|---|---|
| `p1 / p2` | séquence |
| `p1 \| p2` | alternative |
| `^p` | arête en sens inverse |
| `p*`, `p+`, `p?` | zéro ou plus, un ou plus, zéro ou un |
| `!p` | toute propriété sauf `p` |

```sparql
# tout ce qui est, directement ou non, dans l'atelier A
SELECT ?machine
WHERE { ?machine ex:partieDe+ ex:AtelierA . }
```

### SPARQL, Cypher et SQL

Même question — « les capteurs de vibration des équipements de la ligne 2 » :

```sparql
SELECT ?c WHERE { ?e ex:installéeSur ex:Ligne2 ; ex:équipéeDe ?c . ?c a ex:CapteurVibration }
```

```cypher
MATCH (e)-[:INSTALLEE_SUR]->(:Ligne {id:'Ligne2'}), (e)-[:EQUIPEE_DE]->(c:CapteurVibration) RETURN c
```

```sql
SELECT c.* FROM capteur c JOIN equipement e ON c.equipement_id = e.id
WHERE e.ligne = 'Ligne2' AND c.type = 'vibration';
```

| | SPARQL | Cypher | SQL |
|---|---|---|---|
| Modèle | triplets RDF | graphe de propriétés | tables |
| Norme | W3C, 1.1 en 2013 | openCypher, puis GQL (ISO/IEC 39075, 2024) | ISO |
| Identifiants | IRI globales | internes à la base | clés locales |
| Parcours profond | chemins de propriétés `+`, `*` | `[:R*1..]` | `WITH RECURSIVE` |
| Fédération | `SERVICE`, dans la norme 1.1 | selon le moteur | selon le moteur |
| Raisonnement | régimes d'implication (RDFS, OWL) définis par le W3C | pas dans le langage | pas dans le langage |

Angles et al. (2017) comparent SPARQL, Cypher et Gremlin sur la même base formelle ; le détail des langages de graphe de propriétés est dans [[Bases graphe — modèles et langages de requête]].

### SPARQL 1.2

SPARQL 1.2 est en cours au W3C : le projet de requête était un *Working Draft* daté du 11 octobre 2026 à la lecture. Il ajoute le support des **triple terms** de RDF 1.2 (écriture `<<( s p o )>>`, annotations `{| … |}`), un identifiant de version (`VERSION "1.2"`) et des fonctions de texte avec direction. Ce n'est pas une Recommandation : un moteur qui l'annonce suit un brouillon.

## Les maths, simplement

- Un motif est un ensemble de triplets où certaines positions sont des variables. Une **solution** est une fonction $\mu$ qui associe à chaque variable une valeur du graphe, de sorte que le motif, une fois $\mu$ appliquée, **est contenu** dans le graphe : $\mu(P) \subseteq G$.
- Le résultat d'un `SELECT` est l'**ensemble (ou multi-ensemble) des solutions** $\mu$. Deux motifs qui partagent une variable : on ne garde que les $\mu$ compatibles, c'est la jointure naturelle de l'algèbre relationnelle.
- Un chemin `p+` est la **fermeture transitive** de la relation $p$ : l'ensemble des couples $(a, b)$ reliés par une chaîne de $p$ d'au moins une arête.

## En pratique

- **Un moteur RDF s'interroge par HTTP** : le protocole SPARQL fait de chaque base un service ; on envoie la requête, on reçoit du JSON ou du CSV. Un script Python ou un tableau de bord n'ont besoin d'aucun pilote spécifique.
- **Explorer avant d'écrire** : `SELECT DISTINCT ?type WHERE { ?s a ?type }` liste les types présents ; `SELECT DISTINCT ?p WHERE { ?s ?p ?o }` liste les prédicats.
- **Pièges** : un motif sans variable partagée produit un **produit cartésien** (le moteur ne se plaint pas, la requête explose) ; `OPTIONAL` imbriqué à la légère change le sens ; sous le monde ouvert, l'absence d'un triplet ne prouve pas que le fait est faux ([[OWL et raisonnement]]) ; `NOT EXISTS` teste l'absence dans le graphe tel qu'il est, pas dans le monde.
- **Écrire peu de SPARQL à la main** quand les questions sont des gabarits : paramétrer une requête fixe. Pour des questions libres, voir [[Interroger un graphe en langage naturel]] et ses limites mesurées.

## Approches voisines & alternatives

- [[RDF et triplets]] — ce qu'on interroge.
- [[Bases graphe — modèles et langages de requête]] — Cypher, GQL, Gremlin, SQL/PGQ : les langages du graphe de propriétés.
- [[SHACL]] — peut embarquer du SPARQL pour des contraintes complexes ; [[OWL et raisonnement]] — l'implication change les réponses.
- [[Interroger un graphe en langage naturel]] — produire du SPARQL ou du Cypher à partir d'une phrase.
- [[Graphe de connaissances]] — l'entrée du sujet.
- **Alternative** : `rdflib` en Python, qui offre le même langage en bibliothèque, sans serveur, pour de petits graphes (à examiner à la fiche d'outil).
- **Moteurs et outils** : [[Apache Jena]] (serveur Fuseki), [[RDF4J]], [[Oxigraph]], [[QLever]] et [[Virtuoso Open Source]] servent SPARQL ; [[Ontop]] le traduit en SQL sur des tables existantes ; [[rdflib]] l'offre en bibliothèque Python. Le choix est dans [[Comparatif - Moteurs RDF]].

## Pour aller plus loin

- W3C — SPARQL 1.1 Query Language (Recommendation, 2013-03-21) — https://www.w3.org/TR/sparql11-query/
- W3C — SPARQL 1.1 Overview (les onze documents) — https://www.w3.org/TR/sparql11-overview/
- W3C — SPARQL 1.2 Query Language (Working Draft, 2026-10-11) — https://www.w3.org/TR/sparql12-query/
- Angles et al. (2017) — *Foundations of Modern Query Languages for Graph Databases* — https://arxiv.org/abs/1610.06264
