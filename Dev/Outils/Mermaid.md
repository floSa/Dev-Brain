---
galaxie: dev
type: outil
nom: Mermaid
alias: [mermaid, mermaid.js, mermaidjs]
pitch: "Diagram-as-code open-source (MIT, JavaScript) : décrire flowcharts, séquence, ERD, Gantt… en texte type markdown, versionnable et rendu nativement par GitHub et Obsidian."
categorie: tooling/diagram
domaines: []
licence_type: open-source
os: "Web, CLI"
langage: JavaScript
status: actif
alternatives: ["[[Dev/Outils/draw.io|draw.io]]"]
tags: [diagram, diagram-as-code]
url_docs: https://mermaid.js.org/
url_repo: https://github.com/mermaid-js/mermaid
---

# Mermaid

## Pourquoi

**Diagram-as-code** : on décrit le diagramme en **texte** (syntaxe inspirée de markdown) et Mermaid le rend. 20+ types : flowchart, séquence, classe, état, ERD, Gantt, pie, git graph. Le gros intérêt : le diagramme est **du texte versionnable** (diff lisible, revue en PR, généré automatiquement) et il se rend **nativement dans GitHub, GitLab et Obsidian** — pas d'image binaire à maintenir à côté du code. Écrit en JavaScript (MIT).

## Quand l'utiliser

- Diagramme qui **vit dans le repo / la doc** et doit rester synchro avec le code (archi, séquence, ERD dans un README).
- Génération automatique (un script produit le texte Mermaid) ou revue en pull request.
- Contexte markdown : GitHub, Obsidian, MkDocs, Docusaurus le rendent sans plugin lourd.

## Quand NE PAS l'utiliser

- Placement pixel-perfect ou mise en page très contrôlée → [[Dev/Outils/draw.io|draw.io]] (GUI).
- Schéma libre / croquis de réunion → [[Dev/Outils/Excalidraw|Excalidraw]].
- Diagramme dense où l'auto-layout devient illisible : Mermaid place les nœuds automatiquement, on subit la mise en page.

## Bases & plateformes

- Open-source MIT, JavaScript. Utilisable en lib navigateur, via CLI (`mermaid-cli` → PNG/SVG), ou intégré dans un moteur de doc.
- Rendu natif GitHub/GitLab/Obsidian ; éditeur en ligne (Mermaid Live Editor).

## Pièges

- **Auto-layout subi** : sur un graphe dense, on ne maîtrise pas le placement ; scinder en plusieurs diagrammes.
- Syntaxe à apprendre, et qui varie selon le type de diagramme.
- Le rendu peut différer légèrement entre plateformes (versions de Mermaid embarquées différentes).

## Alternatives

- [[Dev/Outils/draw.io|draw.io]] — Éditeur de diagrammes GUI open-source (Apache-2.0, JavaScript) : flowcharts, UML, réseaux, org-charts, BPMN… ; app web ou desktop, stockage sur ton drive, export multi-format, embarquable.

## Liens

- [[Dev/Patterns/Comparatif - Diagrammes|Comparatif - Diagrammes]]
- Docs : https://mermaid.js.org/ · Repo : https://github.com/mermaid-js/mermaid
