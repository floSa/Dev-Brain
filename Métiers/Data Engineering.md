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

- [[Données (notions)]] — 12 notion(s)
- [[Machine learning (notions)]] — 2 notion(s)
- [[NLP (notions)]] — 1 notion(s)
<!-- AUTO:END -->
