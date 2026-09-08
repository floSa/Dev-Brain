---
role: brique
nom: Faiss
alias: [faiss, faiss-cpu, faiss-gpu]
pitch: "Bibliothèque ANN de référence (Meta), index en mémoire CPU/GPU — le moteur derrière beaucoup de vector stores."
categorie: database/vecteur
famille: paquet
licence_type: open-source
maturite: production
langage: C++
alternatives: ["[[hnswlib]]", "[[Annoy]]", "[[ScaNN]]", "[[Chroma]]"]
complements: []
tags: [vector-db, ann, embedded, in-memory]
url_docs: https://faiss.ai
url_repo: https://github.com/facebookresearch/faiss
---

# Faiss

<!-- AUTO:BANDEAU:START -->
> Bibliothèque ANN de référence (Meta), index en mémoire CPU/GPU — le moteur derrière beaucoup de vector stores.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie C++ | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-08-03 |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque de Meta FAIR pour la recherche de similarité et le clustering de vecteurs
denses, écrite en C++ et pilotée depuis Python. L'index vit dans la mémoire du process et
s'appelle in-process : il n'y a pas de serveur, pas de réseau, et rien qui tourne entre deux
appels. Tout le compromis se joue sur le type d'index choisi — `IndexFlat` est exact mais
lent, `IVF` est rapide mais exige un `train()` sur un échantillon représentatif avant le
premier ajout, `PQ` compresse la mémoire au prix du rappel. Ce choix n'est pas un réglage
fin : mal posé, il rend le rappel ou la latence catastrophiques.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Recherche ANN à fort volume, rappel et latence à régler finement (IVF, PQ, HNSW, OPQ) | Aucune persistance : sérialiser l'index sur disque et le recharger est à la charge de l'application |
| L'index vit déjà dans le process Python, sans base externe à exploiter | Aucune métadonnée, aucun filtrage : rien pour restreindre une recherche à un sous-ensemble |
| Indexer et chercher des dizaines de millions de vecteurs sur GPU | Suppressions et mises à jour limitées, et la limite dépend du type d'index retenu |
| Brique bas niveau d'un moteur maison, dont on gère soi-même persistance et métadonnées | Ni API ni multi-tenant : Faiss s'appelle dans un process, il ne se déploie pas en service |

## Mise en œuvre

- Installation — `uv add faiss-cpu`, ou `faiss-gpu` pour la variante accélérée
- Point d'entrée — import Python (`import faiss`), bindings sur la bibliothèque C++
- Prérequis — CUDA ou ROCm pour la variante GPU ; rien de particulier côté CPU
- Exécution — dans le process appelant, CPU ou GPU ; pas de serveur, pas de réseau
- Coût — gratuit, licence MIT, aucune limite d'usage

## Écosystème

### Alternatives

- [[hnswlib]] — Implémentation HNSW C++/Python header-only — rapide, minimale, faite pour embarquer l'ANN dans une app.
- [[Annoy]] — Bibliothèque ANN de Spotify, index sur disque mmap — simple et stable, désormais en mode maintenance.
- [[ScaNN]] — Bibliothèque ANN de Google à quantification anisotrope — débit/rappel à l'état de l'art sur gros volumes.
- [[Chroma]] — Base vectorielle légère et embarquée, du notebook au serveur — l'option la plus simple pour prototyper un RAG.

## Ressources

- Documentation — https://faiss.ai
- Dépôt — https://github.com/facebookresearch/faiss

## Voir aussi

- [[Bases de données vectorielles]] — la notion du dossier
- [[Index ANN — internes]] — les familles d'index (HNSW, IVF, PQ) que cette bibliothèque implémente
- [[Comparatif - Bases vectorielles]] — ce qui départage les moteurs du dossier
