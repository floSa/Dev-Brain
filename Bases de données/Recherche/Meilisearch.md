---
role: brique
nom: Meilisearch
alias: [meilisearch, meili]
pitch: "Moteur de recherche instantané en Rust — full-text tolérant aux fautes de frappe, sémantique et hybride derrière une API REST ; édition communautaire MIT, sharding réservé à l'édition Enterprise."
categorie: database/recherche
famille: plateforme
licence_type: open-core
hosted: [self, managed]
maturite: production
langage: Rust
scaling: single-node
alternatives: ["[[Elasticsearch]]", "[[Typesense]]"]
complements: []
tags: [search, hybrid-search, semantic-search, self-hosted]
url_docs: https://www.meilisearch.com/docs
url_repo: https://github.com/meilisearch/meilisearch
---

# Meilisearch

<!-- AUTO:BANDEAU:START -->
> Moteur de recherche instantané en Rust — full-text tolérant aux fautes de frappe, sémantique et hybride derrière une API REST ; édition communautaire MIT, sharding réservé à l'édition Enterprise.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Rust | open-core | self-hébergé ou managé · mono-nœud | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Moteur de recherche écrit en Rust, pensé pour la recherche par l'utilisateur final : résultats
instantanés au fil de la frappe, tolérance aux fautes, filtres et facettes, sans schéma à
déclarer. Il tient dans un binaire unique avec une API REST, et stocke ses index en fichiers
mappés en mémoire (LMDB). La recherche sémantique et hybride est disponible avec des
embeddings générés automatiquement ou fournis. Le modèle de licence est double : l'édition
communautaire est MIT, l'édition Enterprise (sharding, réplication, snapshots vers S3) exige
un accord commercial en production.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Recherche de site ou d'application, résultats en moins de 50 ms pendant la frappe | Sharding ou réplication indispensables : ils sont réservés à l'édition Enterprise, payante en production |
| Mise en route sans schéma ni cluster : un binaire, une API REST, des SDK dans une dizaine de langages | Analytique sur les mêmes index (agrégations, logs à grande échelle) |
| Hybride et sémantique dans la même API, embeddings générés par le moteur | Corpus qui dépasse un nœud, sans achat de l'édition Enterprise |
| Licence MIT pour le cœur, sans copyleft à qualifier | |

## Mise en œuvre

- Installation — binaire unique, image Docker ou paquet ; Meilisearch Cloud pour l'offre managée
- Point d'entrée — API REST HTTP ; SDK officiels dans une dizaine de langages
- Prérequis — de quoi mapper l'index en mémoire (stockage LMDB) ; aucun schéma à définir
- Exécution — un nœud dans l'édition communautaire ; sharding et réplication dans l'édition Enterprise seulement
- Coût — édition communautaire MIT gratuite ; Enterprise sous licence commerciale (BSL 1.1 hors production) ; Meilisearch Cloud payant après un essai de 14 jours

## Écosystème

### Alternatives

- [[Elasticsearch]] — Moteur de recherche et d'analytique distribué : indexation full-text et logs à grande échelle. — la référence distribuée, quand le corpus dépasse un nœud ou que l'analytique compte.
- [[Typesense]] — Moteur de recherche tolérant aux fautes de frappe (GPL-3.0, C++) — index en mémoire pour du search-as-you-type sous 50 ms, avec recherche vectorielle HNSW et hybride ; alternative ouverte à Algolia. — même cible, licence différente : GPL-3.0 contre MIT pour le cœur.

### Compléments

- *Aucun complément déclaré.*

## Ressources

- Documentation — https://www.meilisearch.com/docs
- Dépôt — https://github.com/meilisearch/meilisearch

## Voir aussi

- [[Recherche]] — le hub du dossier
- [[Index inversé]] — la structure de base de toute recherche plein texte
- [[Recherche sémantique]] — chercher par le sens, ce que fait sa moitié vectorielle
- [[Hybrid retrieval]] — combiner BM25 et kNN dans la même requête
- [[Comparatif - Moteurs de recherche]] — ce qui départage les moteurs du dossier
