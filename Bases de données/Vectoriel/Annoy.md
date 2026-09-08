---
role: brique
nom: Annoy
alias: [annoy, approximate-nearest-neighbors-oh-yeah]
pitch: "Bibliothèque ANN de Spotify, index sur disque mmap — simple et stable, désormais en mode maintenance."
categorie: database/vecteur
famille: paquet
licence_type: open-source
maturite: production
langage: C++
alternatives: ["[[hnswlib]]", "[[Faiss]]", "[[ScaNN]]", "[[Chroma]]"]
complements: []
tags: [vector-db, ann, embedded]
url_docs: https://pypi.org/project/annoy/
url_repo: https://github.com/spotify/annoy
---

# Annoy

<!-- AUTO:BANDEAU:START -->
> Bibliothèque ANN de Spotify, index sur disque mmap — simple et stable, désormais en mode maintenance.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie C++ | open-source | en bibliothèque, rien à héberger | production | amont ancien · 2023-06-14 |
<!-- AUTO:BANDEAU:END -->

## Définition

*Approximate Nearest Neighbors Oh Yeah*, de Spotify : une recherche de plus proches voisins
fondée sur des **forêts d'arbres aléatoires**. Sa particularité est le format de l'index —
un fichier **mmap**, partageable entre plusieurs process et chargeable sans tout monter en
RAM. Le nombre d'arbres arbitre la taille contre la précision : trop peu, et le rappel
s'effondre. Annoy a longtemps servi Discover Weekly ; Spotify oriente désormais les nouveaux
usages vers Voyager, fondé sur HNSW.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Index **statique**, construit une fois puis chargé en lecture seule par plusieurs process | Index figé après `build()` : ajouter un vecteur impose de reconstruire l'index entier |
| Empreinte mémoire serrée : le fichier mmap évite de tout charger | Rappel en retrait à temps égal face aux implémentations HNSW plus récentes |
| Besoin simple, dépendances minimales, API très réduite | Projet en maintenance : ce n'est plus un choix par défaut pour du neuf |

## Mise en œuvre

- Installation — `uv add annoy`
- Point d'entrée — import Python, bindings sur la bibliothèque C++
- Prérequis — CPU uniquement, aucune dépendance lourde
- Exécution — dans le process appelant, single-node ; persistance native par le fichier mmap
- Coût — gratuit, licence Apache 2.0

## Écosystème

### Alternatives

- [[hnswlib]] — Implémentation HNSW C++/Python header-only — rapide, minimale, faite pour embarquer l'ANN dans une app.
- [[Faiss]] — Bibliothèque ANN de référence (Meta), index en mémoire CPU/GPU — le moteur derrière beaucoup de vector stores.
- [[ScaNN]] — Bibliothèque ANN de Google à quantification anisotrope — débit/rappel à l'état de l'art sur gros volumes.
- [[Chroma]] — Base vectorielle légère et embarquée, du notebook au serveur — l'option la plus simple pour prototyper un RAG.

## Ressources

- Documentation — https://pypi.org/project/annoy/
- Dépôt — https://github.com/spotify/annoy

## Voir aussi

- [[Bases de données vectorielles]] — la notion du dossier
- [[Comparatif - Bases vectorielles]] — ce qui départage les moteurs du dossier
