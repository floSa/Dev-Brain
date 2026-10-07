---
role: comparatif
nom: Comparatif - Diagrammes
categorie: design/diagramme
tags: [diagram, diagram-as-code, whiteboard, isometric]
---

# Comparatif - Diagrammes

> On tranche sur : ce que le diagramme est — du texte versionné, un fichier posé à la main, un artefact produit par un agent, ou une lecture de dépôt par un modèle — et donc qui en garde la maîtrise de la mise en page.

![[Comparatif - Diagrammes.base]]

## Ce qui départage

- [[Mermaid]] — le **diagram-as-code** généraliste du lot (avec [[LikeC4]], qui y ajoute un modèle) : le diagramme est du texte, donc diffable, révisable en PR et générable par script, et **GitHub, GitLab et Obsidian le rendent nativement**, sans image binaire à maintenir. La contrepartie est l'**auto-layout subi** — sur un graphe dense, on ne maîtrise pas le placement.
- [[draw.io]] — l'inverse exact : une GUI où l'on **place chaque élément à la main**, avec le plus large catalogue de formes (AWS/Azure/GCP, BPMN, UML) et un stockage libre, disque local compris. Son XML est versionnable mais **illisible en diff** : deux modifications à la souris produisent un diff opaque.
- [[Excalidraw]] — le style **croquis à main levée**, qui est un choix de communication avant d'être un choix d'outil : il signale « schéma conceptuel, pas spec figée ». Whiteboard collaboratif, pas éditeur normé — peu de formes structurées, et les grands tableaux rament côté navigateur.
- [[FossFLOW]] — le seul à faire de l'**isométrique 3D** d'infrastructure, avec les jeux d'icônes cloud standard, en PWA qui tourne entièrement dans le navigateur, hors ligne comprise. Périmètre étroit assumé, et le stockage est celui du navigateur : exporter le JSON ou perdre son travail en changeant de poste.
- [[Archify]] — le seul qui ne s'utilise pas à la main : c'est un **skill pour agent de code**, où l'agent remplit une **IR JSON typée** que la chaîne compile de façon **déterministe** en HTML autonome validé — même IR, même rendu. Quatre absences documentées par le projet lui-même : pas de parsing Mermaid, pas d'auto-layout généraliste, pas de partage hébergé, pas d'édition WYSIWYG.

- [[GitDiagram]] — le seul qui part d'une **URL de dépôt** : rien à dessiner ni à installer, un LLM lit le dépôt et rend un diagramme interactif dont chaque composant renvoie à son fichier sur GitHub, avec la source Mermaid et un serveur MCP en sortie. Ce que [[Archify]] fait avec un agent et une IR reproductible, il le fait sans agent, mais le schéma est **régénéré par un modèle** : le banc d'essai du projet mesure encore 17 % de flèches pleines non étayées par le code, donc à relire avant de le publier. À écarter dès que le code ne doit pas partir chez un fournisseur LLM.
- [[LikeC4]] — le seul qui tient un **modèle** d'architecture : les éléments et leurs relations se décrivent une fois en texte (inspiré du modèle C4 et du DSL de Structurizr), et les vues — contexte, conteneurs, composants — en sont **calculées**, donc cohérentes entre elles. Prévisualisation locale, site statique, exports PNG, Mermaid, D2 et draw.io, et serveur MCP pour les agents. Contrepartie : il exige Node (le champ `engines` de la dernière version demande 22.22.3 ou plus) et un investissement de départ qu'un schéma unique ne justifie pas.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
