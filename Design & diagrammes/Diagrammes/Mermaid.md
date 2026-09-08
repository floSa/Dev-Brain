---
role: brique
nom: Mermaid
alias: [mermaid, mermaid.js, mermaidjs]
pitch: "Diagram-as-code open-source (MIT, JavaScript) : décrire flowcharts, séquence, ERD, Gantt… en texte type markdown, versionnable et rendu nativement par GitHub et Obsidian."
categorie: design/diagramme
famille: extension
domaines: []
licence_type: open-source
os: "Web, CLI"
langage: JavaScript
alternatives: ["[[draw.io]]", "[[Archify]]"]
complements: []
tags: [diagram, diagram-as-code]
url_docs: https://mermaid.js.org/
url_repo: https://github.com/mermaid-js/mermaid
---

# Mermaid

<!-- AUTO:BANDEAU:START -->
> Diagram-as-code open-source (MIT, JavaScript) : décrire flowcharts, séquence, ERD, Gantt… en texte type markdown, versionnable et rendu nativement par GitHub et Obsidian.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Extension JavaScript | open-source | dans le moteur hôte, rien à héberger | — | à jour · 2026-08-25 |
<!-- AUTO:BANDEAU:END -->

## Définition

Diagram-as-code : le diagramme est décrit en **texte**, dans une syntaxe inspirée de
markdown, et Mermaid le rend. Vingt et quelques types couverts — flowchart, séquence,
classe, état, ERD, Gantt, pie, git graph. Tout l'intérêt tient dans la nature du livrable :
du texte versionnable, donc diffable, révisable en pull request et générable par script, et
**rendu nativement par GitHub, GitLab et Obsidian** sans image binaire à maintenir à côté du
code. Le prix de ce format est l'auto-layout : le placement des nœuds n'appartient pas à
l'auteur.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Diagramme qui vit dans le dépôt ou la doc et doit rester synchrone avec le code | **Auto-layout subi** : sur un graphe dense, le placement échappe à l'auteur — scinder en plusieurs diagrammes |
| Génération automatique du diagramme par un script, ou revue en pull request | Syntaxe à apprendre, et qui varie d'un type de diagramme à l'autre |
| Contexte markdown : GitHub, Obsidian, MkDocs et Docusaurus le rendent sans plugin lourd | Le rendu diffère légèrement d'une plateforme à l'autre : les versions de Mermaid embarquées ne sont pas les mêmes |

## Mise en œuvre

- Installation — rien à installer là où le rendu est natif ; sinon `npm i mermaid`, ou `mermaid-cli` pour l'export
- Point d'entrée — un bloc de texte dans un markdown, une bibliothèque navigateur, ou la CLI pour produire PNG/SVG
- Prérequis — un moteur de rendu qui embarque Mermaid, ou Node pour la CLI
- Exécution — dans le moteur hôte (navigateur, GitHub, Obsidian), rien à héberger
- Coût — gratuit, MIT, aucune limite d'usage

## Écosystème

### Alternatives

- [[draw.io]] — Éditeur de diagrammes GUI open-source (Apache-2.0, JavaScript) : flowcharts, UML, réseaux, org-charts, BPMN… ; app web ou desktop, stockage sur ton drive, export multi-format, embarquable.
- [[Archify]] — Skill d'agent IA (MIT, JavaScript) pour diagrammes d'architecture : l'agent produit une IR JSON typée, compilée de façon déterministe en HTML autonome validé, avec exports SVG/PNG/WebM.

## Ressources

- Documentation — https://mermaid.js.org/
- Dépôt — https://github.com/mermaid-js/mermaid

## Voir aussi

- [[Diagrammes]] — le hub du dossier
- [[Comparatif - Diagrammes]] — ce qui départage les outils du dossier
