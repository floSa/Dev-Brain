---
role: hub
nom: Data Engineering
pitch: Amener la donnée d'où elle naît jusqu'où elle sert, de façon répétable, traçable et vérifiable.
---

# Data Engineering

> Amener la donnée d'où elle naît jusqu'où elle sert, de façon répétable, traçable et vérifiable.

## Ce qu'il faut comprendre

- L'objet de cet axe n'est pas la donnée mais le **flux** : d'où elle vient, ce qui la transforme, ce qui garantit qu'un rejeu donne le même résultat. L'idempotence et le contrat de schéma y comptent plus que l'algorithme.
- Il occupe deux branches de l'arbre à part entière — [[Data & pipelines]] et [[Bases de données]] — et en emprunte trois : [[Stockage]] pour la couche objet, [[Calcul distribué]] quand le volume déborde d'une machine, [[Outils de développement]] pour ce qui rend un pipeline testable.
- La frontière avec [[MLOps]] est le **contenu du flux** : ici on déplace de la donnée, là on déplace un modèle et ses métriques. Les outils se recouvrent, les défaillances non.

## Choisir

- Extraire, transformer, planifier → [[Data & pipelines]], sous-dossiers [[Orchestration]], [[Scraping]], [[Parsing]].
- Stocker et interroger → [[Bases de données]] ; [[Relationnel]] par défaut, [[Vectoriel]] pour la recherche sémantique.
- Poser une couche de fichiers durable et adressable → [[Stockage]].
- Franchir la limite d'une machine → [[Calcul distribué]].

<!-- AUTO:START -->
Axe métier **Data Engineering** (`data-eng`) — explorer par sous-domaine, puis descendre via le graphe local.

- [[Bases de données]] — 11 page(s)
- [[Data & pipelines]] — 8 page(s)
- [[Machine Learning]] — 2 page(s)
- [[Outils de développement]] — 2 page(s)
- [[Web & API]] — 1 page(s)
- [[Machine learning (notions)]] — 1 page(s)
<!-- AUTO:END -->
