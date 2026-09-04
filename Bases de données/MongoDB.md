---
role: brique
nom: MongoDB
alias: [mongo, mongodb]
pitch: "Base NoSQL orientée documents (BSON/JSON) : schéma souple et scale horizontal natif par sharding."
categorie: database/document
famille: plateforme
licence_type: source-available
hosted: [self, managed]
maturite: production
langage: C++
scaling: distributed
alternatives: ["[[Redis]]", "[[Apache Cassandra]]"]
complements: ["[[MongoDB Compass]]"]
tags: [nosql, document-db]
url_docs: https://www.mongodb.com/docs/
url_repo: https://github.com/mongodb/mongo
---

# MongoDB

<!-- AUTO:BANDEAU:START -->
> Base NoSQL orientée documents (BSON/JSON) : schéma souple et scale horizontal natif par sharding.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme C++ | source-available | self-hébergé ou managé · distribué | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Base NoSQL orientée **documents** : chaque enregistrement est un document BSON — du JSON
binaire — à schéma libre, regroupé en collections. On stocke l'objet tel qu'il est manipulé
côté application, sans migration de schéma à chaque évolution du modèle. Requêtes riches,
index secondaires et pipeline d'agrégation ; la mise à l'échelle horizontale est native, par
réplica sets pour la disponibilité et sharding pour le volume. Schéma libre n'est pas absence
de schéma : sans validation JSON Schema, la dérive de modèle s'installe.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Données semi-structurées ou au schéma mouvant : catalogues, profils, contenus, événements | Pas de jointure au sens SQL : `$lookup` existe, mais l'employer souvent trahit un modèle mal découpé |
| Modèle agrégat : l'objet métier se lit et s'écrit d'un bloc, peu de relations transverses | Cohérence par défaut au niveau du document ; les transactions multi-documents existent, mais coûtent |
| Scaler horizontalement en écriture sans réarchitecturer, le sharding étant intégré | Index oubliés = scans de collection, et le working set doit tenir en RAM |
| Prototypage rapide, tant que le schéma n'est pas figé | |

## Mise en œuvre

- Installation — self-host par paquet ou Docker, ou managé sur MongoDB Atlas (AWS, GCP, Azure)
- Point d'entrée — API documents et pipeline d'agrégation, depuis un client ou un pilote
- Prérequis — un réplica set pour la haute disponibilité ; un working set qui tient en RAM
- Exécution — self-hébergé ou managé ; distribué, réplica set pour la disponibilité, sharding pour le volume, lectures distribuables sur les secondaires
- Coût — gratuit en self-host, mais la licence SSPL n'est pas reconnue OSI et contraint l'offre « as a service » : Atlas est la voie du managé sans friction

## Écosystème

### Alternatives

- [[Redis]] — Store clé-valeur en mémoire ultra-rapide : cache, sessions, files et broker pub/sub.
- [[Apache Cassandra]] — Base NoSQL wide-column distribuée, sans maître : écritures massives et haute dispo multi-datacenter.

### Compléments

- [[MongoDB Compass]] — Client graphique officiel de MongoDB : exploration de documents, requêtes visuelles et analyse de schéma. — le client officiel pour explorer et administrer l'instance.

## Ressources

- Documentation — https://www.mongodb.com/docs/
- Dépôt — https://github.com/mongodb/mongo

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[Comparatif - Bases NoSQL]] — ce qui départage les moteurs du dossier
