---
role: hub
nom: Diagrammes
alias: [diagramme, schema, diagram-as-code]
pitch: Expliquer un système par un dessin — à la main sur un canevas, ou en texte versionnable à côté du code.
domaines: [data-eng, ai-eng]
tags: [diagram, diagram-as-code, whiteboard, isometric]
---

# Diagrammes

> Expliquer un système par un dessin — à la main sur un canevas, ou en texte versionnable à côté du code.

## Ce qu'il faut comprendre

- La ligne de fracture du sous-domaine est le **support**, pas le rendu. Un **diagramme-as-code** ([[Mermaid]]) est du texte : il vit dans le dépôt, se relit en diff, se régénère, et le moteur décide du placement. Un **canevas** ([[draw.io]], [[Excalidraw]]) est un dessin : on place à la main, donc on obtient exactement ce qu'on veut, et le fichier ne se relit pas en diff.
- Le corollaire pratique : un schéma qui doit **rester juste dans six mois** gagne à être du code, parce qu'on le corrige en éditant deux lignes. Un schéma qui doit **convaincre à l'écran maintenant** gagne à être dessiné.
- Le placement automatique est la vraie limite du diagramme-as-code : au-delà d'une vingtaine de nœuds, aucun moteur ne produit une mise en page lisible sans indices manuels.
- L'**isométrique** ([[FossFLOW]]) est un cas à part : il ne sert pas à expliquer une logique mais à donner à voir une infrastructure. Joli, peu maintenable.

## Choisir

- Dans un README, une PR, une doc Markdown → [[Mermaid]], rendu nativement par GitHub, GitLab et Obsidian.
- Un schéma d'architecture riche, avec des icônes fournisseur et un contrôle fin du placement → [[draw.io]].
- Un croquis à main levée pour une réunion ou une explication rapide → [[Excalidraw]].
- Une vue isométrique d'infrastructure, pour une présentation → [[FossFLOW]].
- Générer le schéma depuis un dépôt existant plutôt que le dessiner → [[Archify]].

<!-- AUTO:START -->
### Briques
- [[Archify]] — Skill d'agent IA (MIT, JavaScript) pour diagrammes d'architecture : l'agent produit une IR JSON typée, compilée de façon déterministe en HTML autonome validé, avec exports SVG/PNG/WebM.
- [[draw.io]] — Éditeur de diagrammes GUI open-source (Apache-2.0, JavaScript) : flowcharts, UML, réseaux, org-charts, BPMN… ; app web ou desktop, stockage sur ton drive, export multi-format, embarquable.
- [[Excalidraw]] — Whiteboard open-source (MIT) au style croquis à main levée : esquisser vite une architecture ou un schéma, collaboration temps réel, export PNG/SVG, s'intègre à Obsidian.
- [[FossFLOW]] — Application web open-source (Unlicense, bâtie sur Isoflow) pour des diagrammes d'infrastructure isométriques 3D : PWA locale dans le navigateur, icônes AWS/Azure/GCP/K8s, export JSON.
- [[Mermaid]] — Diagram-as-code open-source (MIT, JavaScript) : décrire flowcharts, séquence, ERD, Gantt… en texte type markdown, versionnable et rendu nativement par GitHub et Obsidian.

### Comparatifs
- [[Comparatif - Diagrammes]]
<!-- AUTO:END -->
