---
role: brique
nom: hnswlib
alias: [hnsw, nmslib-hnswlib]
pitch: "Implémentation HNSW C++/Python header-only — rapide, minimale, faite pour embarquer l'ANN dans une app."
categorie: database/vecteur
famille: paquet
licence_type: open-source
maturite: production
langage: C++
alternatives: ["[[Faiss]]", "[[Annoy]]", "[[ScaNN]]", "[[Chroma]]"]
complements: []
tags: [vector-db, ann, embedded, in-memory]
url_docs: https://pypi.org/project/hnswlib/
url_repo: https://github.com/nmslib/hnswlib
---

# hnswlib

<!-- AUTO:BANDEAU:START -->
> Implémentation HNSW C++/Python header-only — rapide, minimale, faite pour embarquer l'ANN dans une app.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie C++ | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-03-28 |
<!-- AUTO:BANDEAU:END -->

## Définition

Implémentation header-only, en C++, de l'algorithme **HNSW** — le graphe navigable
hiérarchique — issue de nmslib, avec des bindings Python et R. Aucune dépendance hors C++11 :
c'est le HNSW « nu », celui que plusieurs moteurs ont embarqué chez eux. La construction est
incrémentale, la suppression d'éléments possible, l'empreinte mémoire faible pour ce que fait
l'algorithme. Les trois paramètres qui décident de tout — `M`, `ef_construction`, `ef` — sont
exposés directement.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Recherche ANN purement HNSW, rapide à intégrer et sans dépendance lourde | Taille maximale de l'index fixée à l'initialisation (`max_elements`) : au-delà, `resize_index` explicite |
| Index incrémental, avec des ajouts au fil de l'eau directement en mémoire | `ef` à la requête arbitre rappel contre latence, et trop bas le rappel chute sans le signaler |
| Embarquer l'ANN dans une application C++ ou Python sans tirer une bibliothèque massive | Pas de filtrage riche par métadonnées — un filtre par callback seulement — ni de stockage de payload |
| HNSW suffit, et on veut garder la main sur `M`, `ef_construction` et `ef` | Le graphe tient entier en RAM, et il n'y a pas de GPU |

## Mise en œuvre

- Installation — `uv add hnswlib`
- Point d'entrée — en-têtes C++ à inclure, ou import Python
- Prérequis — un compilateur C++11 ; CPU uniquement
- Exécution — dans le process appelant, single-node ; persistance par `save_index` / `load_index`
- Coût — gratuit, licence Apache 2.0

## Écosystème

### Alternatives

- [[Faiss]] — Bibliothèque ANN de référence (Meta), index en mémoire CPU/GPU — le moteur derrière beaucoup de vector stores.
- [[Annoy]] — Bibliothèque ANN de Spotify, index sur disque mmap — simple et stable, désormais en mode maintenance.
- [[ScaNN]] — Bibliothèque ANN de Google à quantification anisotrope — débit/rappel à l'état de l'art sur gros volumes.
- [[Chroma]] — Base vectorielle légère et embarquée, du notebook au serveur — l'option la plus simple pour prototyper un RAG.

## Ressources

- Documentation — https://pypi.org/project/hnswlib/
- Dépôt — https://github.com/nmslib/hnswlib

## Voir aussi

- [[Bases de données vectorielles]] — la notion du dossier
- [[Index ANN — internes]] — les internes de HNSW et le réglage de `M` et `ef`
- [[Comparatif - Bases vectorielles]] — ce qui départage les moteurs du dossier
