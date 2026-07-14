---
galaxie: dev
type: outil
nom: draw.io
alias: [diagrams.net, drawio, draw io]
pitch: "Éditeur de diagrammes GUI open-source (Apache-2.0, JavaScript) : flowcharts, UML, réseaux, org-charts, BPMN… ; app web ou desktop, stockage sur ton drive, export multi-format, embarquable."
categorie: tooling/diagram
domaines: []
licence_type: open-source
os: "Web, Windows, macOS, Linux"
langage: JavaScript
status: actif
alternatives: ["[[Dev/Outils/Excalidraw|Excalidraw]]", "[[Dev/Outils/Mermaid|Mermaid]]", "[[Dev/Outils/FossFLOW|FossFLOW]]"]
tags: [diagram]
url_docs: https://www.drawio.com/doc/
url_repo: https://github.com/jgraph/drawio
---

# draw.io

## Pourquoi

Éditeur de diagrammes généraliste **GUI** (glisser-déposer), open-source (Apache-2.0, JavaScript). Couvre presque tout : flowcharts, UML, schémas réseau, org-charts, BPMN, plans, cartes mentales, circuits. Rebaptisé **diagrams.net** mais tout le monde dit encore draw.io. Fonctionne dans le navigateur ou en app desktop (Electron), sans compte obligatoire ; les fichiers restent où on veut (disque local, Google Drive, OneDrive). S'intègre partout : plugin Obsidian, Confluence, VS Code.

## Quand l'utiliser

- Diagramme précis et propre où l'on veut **placer chaque élément à la main** (archi, réseau, séquence figée).
- Besoin d'un large catalogue de formes (AWS/Azure/GCP, BPMN, UML) sans coder.
- Confidentialité : stockage local possible, aucune donnée envoyée à un service.

## Quand NE PAS l'utiliser

- Diagramme à **versionner dans le repo** et régénérer automatiquement → [[Dev/Outils/Mermaid|Mermaid]] (texte).
- Croquis rapide, réunion, brainstorming → [[Dev/Outils/Excalidraw|Excalidraw]].
- Rendu isométrique 3D d'infrastructure → [[Dev/Outils/FossFLOW|FossFLOW]].

## Bases & plateformes

- Open-source Apache-2.0, JavaScript. Web (app.diagrams.net), desktop Windows/macOS/Linux, ou auto-hébergeable.
- Fichiers `.drawio` (XML) — lisibles, mais l'édition reste GUI, pas texte.
- Export PNG, SVG, PDF, HTML ; embarquable dans d'autres apps.

## Pièges

- Le format XML est versionnable mais **illisible en diff** : deux modifs GUI produisent un diff opaque (à l'inverse d'un diagram-as-code).
- Beaucoup de formes = tentation de sur-décorer ; la lisibilité prime.
- L'app web hébergée charge/enregistre chez le fournisseur de drive choisi — vérifier où vont les fichiers en contexte sensible.

## Alternatives

- [[Dev/Outils/Excalidraw|Excalidraw]] — Whiteboard open-source (MIT) au style croquis à main levée : esquisser vite une architecture ou un schéma, collaboration temps réel, export PNG/SVG, s'intègre à Obsidian.
- [[Dev/Outils/Mermaid|Mermaid]] — Diagram-as-code open-source (MIT, JavaScript) : décrire flowcharts, séquence, ERD, Gantt… en texte type markdown, versionnable et rendu nativement par GitHub et Obsidian.
- [[Dev/Outils/FossFLOW|FossFLOW]] — Application web open-source (Unlicense, bâtie sur Isoflow) pour des diagrammes d'infrastructure isométriques 3D : PWA locale dans le navigateur, icônes AWS/Azure/GCP/K8s, export JSON.

## Liens

- [[Dev/Patterns/Comparatif - Diagrammes|Comparatif - Diagrammes]]
- Docs : https://www.drawio.com/doc/ · Repo : https://github.com/jgraph/drawio
