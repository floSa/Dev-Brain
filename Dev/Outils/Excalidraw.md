---
galaxie: dev
type: outil
nom: Excalidraw
alias: [excalidraw]
pitch: "Whiteboard open-source (MIT) au style croquis à main levée : esquisser vite une architecture ou un schéma, collaboration temps réel, export PNG/SVG, s'intègre à Obsidian."
categorie: tooling/diagram
domaines: []
licence_type: open-source
os: "Web, Windows, macOS, Linux"
langage: TypeScript
status: actif
alternatives: ["[[Dev/Outils/draw.io|draw.io]]"]
tags: [diagram, whiteboard]
url_docs: https://docs.excalidraw.com/
url_repo: https://github.com/excalidraw/excalidraw
---

# Excalidraw

## Pourquoi

Whiteboard open-source (MIT) au **style croquis à main levée** : le rendu volontairement « dessiné » enlève la pression de la perfection et convient aux schémas d'idées. Idéal pour esquisser une architecture, un flux ou un concept **en quelques minutes**, seul ou à plusieurs en temps réel. Tourne dans le navigateur (excalidraw.com) sans compte, données chiffrées de bout en bout pour la collaboration ; existe aussi en plugin **Obsidian** très populaire et en extension VS Code.

## Quand l'utiliser

- **Esquisser vite** une archi ou une idée, réunion, atelier, whiteboard partagé.
- Illustrations de doc où le style « main levée » signale « schéma conceptuel, pas spec figée ».
- Dans Obsidian : dessiner à côté de ses notes (plugin natif).

## Quand NE PAS l'utiliser

- Diagramme formel et précis (UML, réseau détaillé) → [[Dev/Outils/draw.io|draw.io]].
- Diagramme versionné en texte dans le repo → [[Dev/Outils/Mermaid|Mermaid]].

## Bases & plateformes

- Open-source MIT, TypeScript. Web, apps desktop, plugin Obsidian, extension VS Code.
- Format `.excalidraw` (JSON) versionnable ; export PNG/SVG (avec la source embarquée pour ré-édition).
- Collaboration temps réel chiffrée de bout en bout ; auto-hébergeable.

## Pièges

- Style « croquis » inadapté à un livrable formel : signale l'informel, à assumer.
- Peu de formes structurées (pas un outil UML) : c'est un whiteboard, pas un éditeur de diagrammes normés.
- Les gros tableaux collaboratifs peuvent ramer côté navigateur.

## Alternatives

- [[Dev/Outils/draw.io|draw.io]] — Éditeur de diagrammes GUI open-source (Apache-2.0, JavaScript) : flowcharts, UML, réseaux, org-charts, BPMN… ; app web ou desktop, stockage sur ton drive, export multi-format, embarquable.

## Liens

- [[Dev/Patterns/Comparatif - Diagrammes|Comparatif - Diagrammes]]
- Docs : https://docs.excalidraw.com/ · Repo : https://github.com/excalidraw/excalidraw
