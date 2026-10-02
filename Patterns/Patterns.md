---
role: hub
nom: Patterns
pitch: Des combinaisons de briques déjà éprouvées — ce qui marche ensemble, et pourquoi ces briques-là.
---

# Patterns

> Des combinaisons de briques déjà éprouvées — ce qui marche ensemble, et pourquoi ces briques-là.

## Ce qu'il faut comprendre

- Un pattern n'est pas une brique de plus : c'est un **assemblage**, avec le contexte qui le rend valable et les décisions qui l'ont fixé. Il répond à « par quoi je commence », là où une fiche de brique répond à « est-ce le bon outil ».
- Aucune `categorie:` ne les range, et c'est voulu : un pattern enjambe plusieurs domaines par construction — c'est même sa raison d'être. C'est `role: pattern` qui les groupe, donc ce dossier.
- Le vault en porte huit, ce qui est peu. Les cinq premiers sont issus de projets réels ; aucun n'a été écrit pour combler une case. Les trois derniers (maintenance prédictive on-prem, inspection visuelle, anomalies en deux étages) assemblent des briques du vault et n'ont pas encore de projet appliqué : `projets_appliques:` y est vide.

## Choisir

- Partir d'un archétype de projet plutôt que d'une brique → lire le `contexte:` de chaque pattern, c'est le seul critère d'entrée.
- Surveiller des machines d'atelier sur site, de la lecture OPC UA à l'alerte → [[Pattern - Pipeline de maintenance prédictive on-prem]] ; contrôler des pièces par caméra en cadence → [[Pattern - Inspection visuelle en ligne de production]] ; poser des règles et des cartes de contrôle avant tout modèle appris → [[Pattern - Détection d'anomalies en deux étages]].
- Chercher plutôt ce qui départage deux briques comparables → les comparatifs, dans le dossier du domaine concerné.
- Chercher une contrainte à respecter quel que soit le projet → [[Rules]].

<!-- AUTO:START -->
### Patterns
- [[Pattern - Agent sur LLM auto-hébergé]]
- [[Pattern - Moteur de jeu pur + IA séparée]]
- [[Pattern - Pipeline scraping → matching → optimisation]]
- [[Pattern - RAG structuré graphe + human-in-the-loop]]
- [[Pattern - Stack démo ML locale multi-services]]
<!-- AUTO:END -->
