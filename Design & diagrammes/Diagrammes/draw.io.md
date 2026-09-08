---
role: brique
nom: draw.io
alias: [diagrams.net, drawio, draw io]
pitch: "Éditeur de diagrammes GUI open-source (Apache-2.0, JavaScript) : flowcharts, UML, réseaux, org-charts, BPMN… ; app web ou desktop, stockage sur ton drive, export multi-format, embarquable."
categorie: design/diagramme
famille: application
domaines: []
licence_type: open-source
os: "Web, Windows, macOS, Linux"
langage: JavaScript
alternatives: ["[[Excalidraw]]", "[[Mermaid]]", "[[FossFLOW]]", "[[Archify]]"]
complements: []
tags: [diagram]
url_docs: https://www.drawio.com/docs/
url_repo: https://github.com/jgraph/drawio
---

# draw.io

<!-- AUTO:BANDEAU:START -->
> Éditeur de diagrammes GUI open-source (Apache-2.0, JavaScript) : flowcharts, UML, réseaux, org-charts, BPMN… ; app web ou desktop, stockage sur ton drive, export multi-format, embarquable.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application JavaScript | open-source | Web, Windows, macOS, Linux | — | à jour · 2026-09-07 |
<!-- AUTO:BANDEAU:END -->

## Définition

Éditeur de diagrammes généraliste à interface graphique, en glisser-déposer, rebaptisé
diagrams.net mais que tout le monde appelle encore draw.io. Il couvre à peu près tout —
flowcharts, UML, schémas réseau, org-charts, BPMN, plans, cartes mentales, circuits — avec
le plus large catalogue de formes du lot, AWS, Azure et GCP compris. Chaque élément est
**placé à la main** : c'est l'inverse exact d'un diagram-as-code, et cela se paie sur le
versionnement, car le `.drawio` est du XML lisible par la machine mais opaque en diff.
Aucun compte n'est obligatoire, et les fichiers restent où on veut.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Diagramme précis où l'on veut placer chaque élément soi-même — architecture, réseau, séquence figée | Le XML est versionnable mais **illisible en diff** : deux modifications à la souris produisent un diff opaque |
| Besoin d'un large catalogue de formes (AWS, Azure, GCP, BPMN, UML) sans écrire de code | Le catalogue invite à sur-décorer, au détriment de la lisibilité du schéma |
| Confidentialité : stockage local possible, aucune donnée envoyée à un service | L'app web hébergée charge et enregistre chez le fournisseur de drive choisi — à vérifier en contexte sensible |

## Mise en œuvre

- Installation — rien pour la version web (app.diagrams.net) ; installeur desktop Windows, macOS, Linux ; ou image auto-hébergeable
- Point d'entrée — application graphique, fichiers `.drawio` (XML) ; plugins Obsidian, Confluence et VS Code
- Prérequis — un navigateur, ou Electron pour la version desktop
- Exécution — sur le poste ou dans le navigateur ; auto-hébergement possible pour la version web
- Coût — gratuit, Apache-2.0, aucune limite d'usage

## Écosystème

### Alternatives

- [[Excalidraw]] — Whiteboard open-source (MIT) au style croquis à main levée : esquisser vite une architecture ou un schéma, collaboration temps réel, export PNG/SVG, s'intègre à Obsidian.
- [[Mermaid]] — Diagram-as-code open-source (MIT, JavaScript) : décrire flowcharts, séquence, ERD, Gantt… en texte type markdown, versionnable et rendu nativement par GitHub et Obsidian.
- [[FossFLOW]] — Application web open-source (Unlicense, bâtie sur Isoflow) pour des diagrammes d'infrastructure isométriques 3D : PWA locale dans le navigateur, icônes AWS/Azure/GCP/K8s, export JSON.
- [[Archify]] — Skill d'agent IA (MIT, JavaScript) pour diagrammes d'architecture : l'agent produit une IR JSON typée, compilée de façon déterministe en HTML autonome validé, avec exports SVG/PNG/WebM.

## Ressources

- Documentation — https://www.drawio.com/docs/
- Dépôt — https://github.com/jgraph/drawio

## Voir aussi

- [[Diagrammes]] — le hub du dossier
- [[Comparatif - Diagrammes]] — ce qui départage les outils du dossier
