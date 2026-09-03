---
role: comparatif
nom: Comparatif - Diagrammes
categorie: design/diagramme
tags: [diagram, diagram-as-code, whiteboard, isometric]
---

# Comparatif - Diagrammes

> On tranche sur : ce que le diagramme est — du texte versionné, un fichier posé à la main, ou un artefact produit par un agent — et donc qui en garde la maîtrise de la mise en page.

![[Comparatif - Diagrammes.base]]

## Ce qui départage

- [[Mermaid]] — le seul **diagram-as-code** du lot : le diagramme est du texte, donc diffable, révisable en PR et générable par script, et **GitHub, GitLab et Obsidian le rendent nativement**, sans image binaire à maintenir. La contrepartie est l'**auto-layout subi** — sur un graphe dense, on ne maîtrise pas le placement.
- [[draw.io]] — l'inverse exact : une GUI où l'on **place chaque élément à la main**, avec le plus large catalogue de formes (AWS/Azure/GCP, BPMN, UML) et un stockage libre, disque local compris. Son XML est versionnable mais **illisible en diff** : deux modifications à la souris produisent un diff opaque.
- [[Excalidraw]] — le style **croquis à main levée**, qui est un choix de communication avant d'être un choix d'outil : il signale « schéma conceptuel, pas spec figée ». Whiteboard collaboratif, pas éditeur normé — peu de formes structurées, et les grands tableaux rament côté navigateur.
- [[FossFLOW]] — le seul à faire de l'**isométrique 3D** d'infrastructure, avec les jeux d'icônes cloud standard, en PWA qui tourne entièrement dans le navigateur, hors ligne comprise. Périmètre étroit assumé, et le stockage est celui du navigateur : exporter le JSON ou perdre son travail en changeant de poste.
- [[Archify]] — le seul qui ne s'utilise pas à la main : c'est un **skill pour agent de code**, où l'agent remplit une **IR JSON typée** que la chaîne compile de façon **déterministe** en HTML autonome validé — même IR, même rendu. Quatre absences documentées par le projet lui-même : pas de parsing Mermaid, pas d'auto-layout généraliste, pas de partage hébergé, pas d'édition WYSIWYG.
