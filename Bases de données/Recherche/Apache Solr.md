---
role: brique
nom: Apache Solr
alias: [solr, apache solr, solrcloud]
pitch: "Plateforme de recherche Apache (Apache-2.0) bâtie sur Lucene — full-text, vectoriel et géospatial, distribuée par SolrCloud (réplication, bascule automatique)."
categorie: database/recherche
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Java
scaling: distributed
alternatives: ["[[Elasticsearch]]", "[[OpenSearch]]"]
complements: []
tags: [search, distributed]
url_docs: https://solr.apache.org/guide/
url_repo: https://github.com/apache/solr
---

# Apache Solr

<!-- AUTO:BANDEAU:START -->
> Plateforme de recherche Apache (Apache-2.0) bâtie sur Lucene — full-text, vectoriel et géospatial, distribuée par SolrCloud (réplication, bascule automatique).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Java | open-source | self-hébergé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme de recherche du projet Apache, bâtie sur [[Lucene]] comme Elasticsearch. Elle offre
la recherche plein texte, la recherche vectorielle et la recherche géospatiale sur le
même index. En mode SolrCloud, l'indexation est distribuée, répliquée et interrogée avec répartition de charge, avec bascule et reprise automatiques et une
configuration centralisée. Le projet est gouverné par la fondation Apache, sous licence
Apache-2.0. La version 10.0.0 est sortie le 2026-03-03.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un moteur distribué sous licence Apache-2.0 et gouvernance de fondation, sans éditeur commercial derrière | Recherche simple sur un corpus modeste : l'index plein texte de [[Postgres]] suffit souvent |
| Un parc Solr existant à faire vivre, avec des schémas et des configurations déjà maîtrisés | Gourmand en RAM : heap JVM plus cache du système de fichiers |
| Full-text, vectoriel et géospatial dans un même moteur | Quasi temps réel, jamais transactionnel : ne convient pas comme source de vérité |
| Distribution et réplication intégrées par SolrCloud | |

## Mise en œuvre

- Installation — archive ou image Docker
- Point d'entrée — API HTTP, interface d'administration web
- Prérequis — une JVM ; en SolrCloud, une configuration centralisée
- Exécution — auto-hébergé, distribué par SolrCloud : réplication, répartition de charge, bascule automatique
- Coût — gratuit, Apache-2.0 ; la dépense réelle est l'exploitation (JVM, heap, gestion des shards)

## Écosystème

### Alternatives

- [[Elasticsearch]] — Moteur de recherche et d'analytique distribué : indexation full-text et logs à grande échelle. — l'autre moteur distribué construit sur Lucene, mais sous triple licence AGPL, SSPL et ELv2.
- [[OpenSearch]] — Moteur de recherche et d'analytique distribué (Apache-2.0) — fork d'Elasticsearch 7.10.2 : full-text, k-NN et recherche hybride, visualisé dans OpenSearch Dashboards. — même licence Apache-2.0, lignée d'Elasticsearch plutôt que celle de Solr.

### Compléments

- *Aucun complément déclaré.*

## Ressources

- Documentation — https://solr.apache.org/guide/
- Dépôt — https://github.com/apache/solr

## Voir aussi

- [[Recherche]] — le hub du dossier
- [[Lucene]] — la bibliothèque d'indexation qu'il embarque
- [[Index inversé]] — la structure sur laquelle repose la recherche plein texte
- [[Comparatif - Moteurs de recherche]] — ce qui départage les moteurs du dossier
