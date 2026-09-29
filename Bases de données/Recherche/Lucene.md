---
role: brique
nom: Lucene
alias: [lucene, apache lucene]
pitch: "Bibliothèque Java de recherche plein texte (Apache-2.0) — le moteur d'indexation sous Elasticsearch et Solr ; index inversé et HNSW natifs, à embarquer dans une application JVM."
categorie: database/recherche
famille: paquet
licence_type: open-source
maturite: production
langage: Java
alternatives: []
complements: []
tags: [search, ann, embedded]
url_docs: https://lucene.apache.org/core/documentation.html
url_repo: https://github.com/apache/lucene
---

# Lucene

<!-- AUTO:BANDEAU:START -->
> Bibliothèque Java de recherche plein texte (Apache-2.0) — le moteur d'indexation sous Elasticsearch et Solr ; index inversé et HNSW natifs, à embarquer dans une application JVM.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Java | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque Java d'indexation et de recherche, projet Apache sous licence Apache-2.0. Elle
construit et interroge des [[Index inversé|index inversés]], avec analyse et tokenisation du
texte, correction orthographique, surlignage des résultats et classement par pertinence (BM25
par défaut). Elle porte aussi la recherche vectorielle, avec un index HNSW natif : `maxConn` à
16 et `beamWidth` à 100 par défaut, réglables. Ce n'est pas un serveur : [[Elasticsearch]] et
[[Apache Solr]] sont des services qui l'enveloppent, et [[OpenSearch]] la reprend par filiation
d'Elasticsearch. Une version 10.5 est publiée sur le site du projet ; PyLucene expose la
bibliothèque à Python.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Embarquer un index de recherche dans une application JVM, sans serveur à exploiter | Un service de recherche prêt à interroger en HTTP : ce n'est pas une bibliothèque qui l'offre |
| Contrôler finement l'analyse, le scoring et la structure de l'index | Distribution, réplication et bascule à mettre en œuvre soi-même : la bibliothèque ne les fournit pas |
| Comprendre ce qui se passe sous un moteur de la famille Lucene | Une équipe sans compétence JVM : le point d'entrée est du code Java |

## Mise en œuvre

- Installation — dépendance Maven ou Gradle ; PyLucene pour Python
- Point d'entrée — API Java : un `IndexWriter` pour indexer, un `IndexSearcher` pour interroger
- Prérequis — un runtime Java ; la version minimale de Java est celle de la version de Lucene retenue
- Exécution — dans le process appelant, single-node ; la distribution est l'affaire du moteur qui l'enveloppe
- Coût — gratuit, Apache-2.0

## Écosystème

### Alternatives

- [[Elasticsearch]] — voisin : le service distribué qui l'enveloppe, quand la bibliothèque seule ne suffit plus.
- [[Apache Solr]] — voisin : l'autre service qui l'enveloppe, gouverné par la même fondation.
- [[hnswlib]] — voisin : HNSW « nu », hors moteur de recherche, quand seul l'index vectoriel compte.

### Compléments

- *Aucun complément déclaré.*

## Ressources

- Documentation — https://lucene.apache.org/core/documentation.html
- Dépôt — https://github.com/apache/lucene

## Voir aussi

- [[Recherche]] — le hub du dossier
- [[Index inversé]] — la structure centrale qu'elle construit
- [[Recherche vectorielle approximative]] — son index HNSW et ses réglages
- [[Comparatif - Moteurs de recherche]] — ce qui départage les moteurs du dossier
