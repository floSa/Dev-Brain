---
role: brique
nom: Excalidraw
alias: [excalidraw]
pitch: "Whiteboard open-source (MIT) au style croquis à main levée : esquisser vite une architecture ou un schéma, collaboration temps réel, export PNG/SVG, s'intègre à Obsidian."
categorie: design/diagramme
famille: application
domaines: []
licence_type: open-source
os: "Web, Windows, macOS, Linux"
langage: TypeScript
alternatives: ["[[draw.io]]", "[[Archify]]"]
complements: []
tags: [diagram, whiteboard]
url_docs: https://docs.excalidraw.com/
url_repo: https://github.com/excalidraw/excalidraw
---

# Excalidraw

<!-- AUTO:BANDEAU:START -->
> Whiteboard open-source (MIT) au style croquis à main levée : esquisser vite une architecture ou un schéma, collaboration temps réel, export PNG/SVG, s'intègre à Obsidian.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Application TypeScript | open-source | Web, Windows, macOS, Linux | — |
<!-- AUTO:BANDEAU:END -->

## Définition

Whiteboard au **style croquis à main levée** : le rendu volontairement dessiné n'est pas
un effet, c'est un message — il signale « schéma conceptuel, pas spécification figée » et
enlève la pression de la perfection. Fait pour esquisser une architecture, un flux ou une
idée en quelques minutes, seul ou à plusieurs en temps réel. Tourne dans le navigateur
sans compte, avec collaboration chiffrée de bout en bout, et existe en plugin Obsidian très
répandu comme en extension VS Code. Le format `.excalidraw` est du JSON versionnable, et
les exports PNG/SVG embarquent la source pour permettre la ré-édition.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Esquisser vite une architecture ou une idée — réunion, atelier, tableau partagé | Le style croquis est **inadapté à un livrable formel** : il signale l'informel, ce qui s'assume ou se refuse |
| Illustration de doc où le style main levée dit « conceptuel, pas figé » | Peu de formes structurées : c'est un whiteboard, pas un éditeur de diagrammes normés |
| Dessiner à côté de ses notes dans Obsidian, via le plugin natif | Les grands tableaux collaboratifs rament côté navigateur |

## Mise en œuvre

- Installation — rien pour excalidraw.com ; apps desktop, plugin Obsidian ou extension VS Code selon le contexte
- Point d'entrée — application graphique ; fichiers `.excalidraw` (JSON), export PNG/SVG avec source embarquée
- Prérequis — un navigateur ; auto-hébergement possible
- Exécution — dans le navigateur ou l'application hôte ; collaboration temps réel chiffrée de bout en bout
- Coût — gratuit, MIT, aucune limite d'usage

## Écosystème

### Alternatives

- [[draw.io]] — Éditeur de diagrammes GUI open-source (Apache-2.0, JavaScript) : flowcharts, UML, réseaux, org-charts, BPMN… ; app web ou desktop, stockage sur ton drive, export multi-format, embarquable.
- [[Archify]] — Skill d'agent IA (MIT, JavaScript) pour diagrammes d'architecture : l'agent produit une IR JSON typée, compilée de façon déterministe en HTML autonome validé, avec exports SVG/PNG/WebM.

## Ressources

- Documentation — https://docs.excalidraw.com/
- Dépôt — https://github.com/excalidraw/excalidraw

## Voir aussi

- [[Diagrammes]] — le hub du dossier
- [[Comparatif - Diagrammes]] — ce qui départage les outils du dossier
