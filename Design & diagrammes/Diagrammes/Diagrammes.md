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

- La ligne de fracture du sous-domaine est le **support**, pas le rendu. Un **diagramme-as-code** ([[Mermaid]], [[D2]], [[PlantUML]], [[LikeC4]]) est du texte : il vit dans le dépôt, se relit en diff, se régénère, et le moteur décide du placement. Un **canevas** ([[draw.io]], [[Excalidraw]]) est un dessin : on place à la main, donc on obtient exactement ce qu'on veut, et le fichier ne se relit pas en diff.
- Le corollaire pratique : un schéma qui doit **rester juste dans six mois** gagne à être du code, parce qu'on le corrige en éditant deux lignes. Un schéma qui doit **convaincre à l'écran maintenant** gagne à être dessiné.
- Le placement automatique est la vraie limite du diagramme-as-code : au-delà d'une vingtaine de nœuds, aucun moteur ne produit une mise en page lisible sans indices manuels.
- Un troisième support est apparu : le diagramme **produit par un modèle** à partir d'un dépôt ([[Archify]] via un agent, [[GitDiagram]] via une URL). Personne n'y place rien, donc personne n'en répond : il se relit comme une hypothèse, pas comme une spécification.
- L'**isométrique** ([[FossFLOW]]) est un cas à part : il ne sert pas à expliquer une logique mais à donner à voir une infrastructure. Joli, peu maintenable.

## Choisir

- Dans un README, une PR, une doc Markdown → [[Mermaid]], rendu nativement par GitHub, GitLab et Obsidian.
- Un diagramme en texte au rendu plus soigné que Mermaid (thèmes, mode croquis, moteurs de placement au choix), à produire en CI → [[D2]] ; le plus large catalogue de types, UML en tête (séquence, classes, états, mais aussi Gantt et ArchiMate) → [[PlantUML]], qui demande Java. Ni l'un ni l'autre n'est rendu par GitHub sans étape de plus. Rendre ces langages, et d'autres, par une seule API hébergée chez soi → [[Kroki]].
- Un schéma d'architecture riche, avec des icônes fournisseur et un contrôle fin du placement → [[draw.io]].
- Un croquis à main levée pour une réunion ou une explication rapide → [[Excalidraw]].
- Une vue isométrique d'infrastructure, pour une présentation → [[FossFLOW]].
- Générer le schéma depuis un dépôt existant plutôt que le dessiner → [[Archify]] si un agent de code est dans la boucle et que le rendu doit être reproductible, [[GitDiagram]] pour un coup d'œil immédiat à partir d'une URL, en acceptant que le code passe par un fournisseur LLM.
- Tenir le **modèle** d'une architecture en texte, et en tirer les vues contexte, conteneurs et composants sans qu'elles se contredisent → [[LikeC4]] (inspiré du [[Modèle C4]]) ; [[Mermaid]] dessine un diagramme à la fois, sans modèle commun.
- Savoir **quoi** dessiner à chaque niveau d'un système (contexte, conteneurs, composants) → [[Modèle C4]], qui dit quoi montrer ; les outils ci-dessus ne disent que comment le tracer.

<!-- AUTO:START -->
### Briques
- [[Archify]] — Skill d'agent IA (MIT, JavaScript) pour diagrammes d'architecture : l'agent produit une IR JSON typée, compilée de façon déterministe en HTML autonome validé, avec exports SVG/PNG/WebM.
- [[D2]] — Outil en ligne de commande (MPL-2.0, Go) qui transforme un langage de description de diagrammes en SVG, PNG, PDF, GIF ou PPTX, avec thèmes, plusieurs moteurs de placement, rendu au trait de crayon et animations — mais le langage lui est propre, aucune forge ne le rend nativement, et le moteur TALA est un module à part.
- [[draw.io]] — Éditeur de diagrammes GUI open-source (Apache-2.0, JavaScript) : flowcharts, UML, réseaux, org-charts, BPMN… ; app web ou desktop, stockage sur ton drive, export multi-format, embarquable.
- [[Excalidraw]] — Whiteboard open-source (MIT) au style croquis à main levée : esquisser vite une architecture ou un schéma, collaboration temps réel, export PNG/SVG, s'intègre à Obsidian.
- [[FossFLOW]] — Application web open-source (Unlicense, bâtie sur Isoflow) pour des diagrammes d'infrastructure isométriques 3D : PWA locale dans le navigateur, icônes AWS/Azure/GCP/K8s, export JSON.
- [[GitDiagram]] — Service web open-source (MIT, TypeScript) qui génère par LLM un diagramme d'architecture interactif d'un dépôt GitHub depuis son URL : composants liés au code, export PNG/Mermaid, serveur MCP pour les agents.
- [[Kroki]] — Serveur HTTP (MIT, Java) à héberger qui donne une seule API pour rendre une vingtaine de langages de diagrammes — PlantUML, Mermaid, D2, GraphViz, BPMN, Excalidraw, DBML, Vega — en SVG ou PNG, par une URL ou une requête POST — mais les langages tournent dans des conteneurs compagnons, et l'instance publique kroki.io reçoit vos sources si on la préfère à la sienne.
- [[LikeC4]] — Outil en ligne de commande (MIT, TypeScript) : décrire une architecture logicielle dans un langage de modélisation inspiré du modèle C4, puis en tirer des vues interactives, un site statique et des exports PNG, Mermaid, D2 ou draw.io.
- [[Mermaid]] — Diagram-as-code open-source (MIT, JavaScript) : décrire flowcharts, séquence, ERD, Gantt… en texte type markdown, versionnable et rendu nativement par GitHub et Obsidian.
- [[PlantUML]] — Outil Java (licences au choix : GPL, LGPL, Apache, EPL ou MIT) qui dessine des diagrammes UML et plus de vingt types — séquence, classes, activité, états, Gantt, carte mentale, JSON, YAML — à partir d'une description textuelle, en ligne de commande, en bibliothèque ou compilé pour le navigateur — mais GitHub ne les rend pas nativement, il faut une extension de navigateur ou un rendu en amont.

### Comparatifs
- [[Comparatif - Diagrammes]]
<!-- AUTO:END -->
