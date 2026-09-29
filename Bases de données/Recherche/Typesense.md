---
role: brique
nom: Typesense
alias: [typesense]
pitch: "Moteur de recherche tolérant aux fautes de frappe (GPL-3.0, C++) — index en mémoire pour du search-as-you-type sous 50 ms, avec recherche vectorielle HNSW et hybride ; alternative ouverte à Algolia."
categorie: database/recherche
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: C++
scaling: distributed
alternatives: ["[[Elasticsearch]]", "[[Meilisearch]]"]
complements: []
tags: [search, hybrid-search, ann, self-hosted]
url_docs: https://typesense.org/docs/
url_repo: https://github.com/typesense/typesense
---

# Typesense

<!-- AUTO:BANDEAU:START -->
> Moteur de recherche tolérant aux fautes de frappe (GPL-3.0, C++) — index en mémoire pour du search-as-you-type sous 50 ms, avec recherche vectorielle HNSW et hybride ; alternative ouverte à Algolia.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme C++ | open-source | self-hébergé ou managé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Moteur de recherche en C++ qui garde son index en mémoire pour répondre en quelques dizaines
de millisecondes, avec tolérance aux fautes de frappe et recherche au fil de la saisie. On lui
pousse ses propres données, il ne les collecte pas. Il indexe aussi des embeddings (index HNSW
intégré, génération par modèle intégré ou API tierce) et fusionne une recherche par mots-clés
et une recherche vectorielle par rank fusion, cf. [[Hybrid retrieval]]. Un cluster Raft assure
la haute disponibilité, et les données sont persistées sur disque.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Recherche instantanée sur un catalogue ou un site, avec facettes et tolérance aux fautes | Analytique et agrégations lourdes sur les mêmes index |
| Une alternative auto-hébergeable à Algolia, ouverte | Corpus dont l'index ne tient pas en RAM : l'index est mémoire-résident |
| Hybride et vectoriel avec embeddings générés par le moteur | Licence GPL-3.0 : à faire qualifier avant d'embarquer le moteur dans un produit distribué |
| Cluster haute disponibilité par consensus Raft | |

## Mise en œuvre

- Installation — Docker, binaires Linux x86_64 et ARM64, paquets DEB et RPM, Homebrew ; Typesense Cloud pour l'offre managée
- Point d'entrée — API REST HTTP sur le port 8108, clé d'API obligatoire pour chaque requête
- Prérequis — de la RAM pour l'index entier ; un répertoire de données pour la persistance
- Exécution — un nœud ou un cluster Raft en haute disponibilité
- Coût — GPL-3.0, gratuit en auto-hébergement ; Typesense Cloud pour l'offre managée

## Écosystème

### Alternatives

- [[Elasticsearch]] — Moteur de recherche et d'analytique distribué : indexation full-text et logs à grande échelle. — le concurrent nommé par le projet lui-même : Typesense se veut plus simple à opérer.
- [[Meilisearch]] — Moteur de recherche instantané en Rust — full-text tolérant aux fautes de frappe, sémantique et hybride derrière une API REST ; édition communautaire MIT, sharding réservé à l'édition Enterprise. — même cible : licence GPL-3.0 ici, MIT pour le cœur là-bas.

### Compléments

- *Aucun complément déclaré.*

## Ressources

- Documentation — https://typesense.org/docs/
- Dépôt — https://github.com/typesense/typesense

## Voir aussi

- [[Recherche]] — le hub du dossier
- [[Index inversé]] — la structure de base de toute recherche plein texte
- [[Recherche vectorielle approximative]] — l'index HNSW intégré et ses réglages `M` et `ef_construction`
- [[Recherche sémantique]] — chercher par le sens
- [[Comparatif - Moteurs de recherche]] — ce qui départage les moteurs du dossier
