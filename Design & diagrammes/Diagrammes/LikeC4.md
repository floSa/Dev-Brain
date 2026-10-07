---
role: brique
nom: LikeC4
alias: [likec4, Architecture as code, C4 en code]
pitch: "Outil en ligne de commande (MIT, TypeScript) : décrire une architecture logicielle dans un langage de modélisation inspiré du modèle C4, puis en tirer des vues interactives, un site statique et des exports PNG, Mermaid, D2 ou draw.io."
categorie: design/diagramme
famille: cli
licence_type: open-source
maturite: production
langage: TypeScript
alternatives: ["[[Mermaid]]", "[[draw.io]]"]
complements: []
tags: [diagram, diagram-as-code]
url_docs: https://likec4.dev/
url_repo: https://github.com/likec4/likec4
---

# LikeC4

<!-- AUTO:BANDEAU:START -->
> Outil en ligne de commande (MIT, TypeScript) : décrire une architecture logicielle dans un langage de modélisation inspiré du modèle C4, puis en tirer des vues interactives, un site statique et des exports PNG, Mermaid, D2 ou draw.io.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI TypeScript | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Langage de **modélisation d'architecture** et outils qui en tirent des diagrammes. On décrit le système **une fois**, dans des fichiers texte (`.c4`, `.likec4`) : les éléments, leurs relations, leurs niveaux imbriqués. Puis on définit des **vues** sur ce modèle : le contexte, les conteneurs, un composant et ses voisins. Les diagrammes ne sont pas dessinés, ils sont **calculés** à partir du modèle, ce qui évite qu'un schéma de niveau 2 contredise celui de niveau 1.

Il s'inspire du [[Modèle C4]] et du DSL de Structurizr, avec plus de liberté : la notation, les types d'éléments et le nombre de niveaux se définissent soi-même. C'est la différence avec [[Mermaid]], dont le diagramme C4 est un type de diagramme parmi d'autres (marqué expérimental dans sa documentation, syntaxe compatible avec PlantUML) : chaque diagramme y est écrit séparément, sans modèle commun entre les vues.

Ce que fournit l'outillage (README du paquet `likec4` et documentation, relevés le 2026-10-07) :

- `likec4 start` : prévisualisation dans un serveur local avec mise à jour à chaud ; `likec4 build` : site statique publiable (GitHub Pages, Netlify…).
- **Exports** : PNG, JSON, Mermaid, Dot, D2, draw.io ; **import** de fichiers `.drawio` pour reprendre des schémas existants.
- Extension **VS Code** (validation, coloration, aperçu en direct, renommage sûr), image **Docker**, **GitHub Action**, plugin **Vite** et composants **React** pour intégrer les diagrammes dans une application.
- **IA** : un skill d'agent (`npx skills add https://likec4.dev/`) qui apprend la syntaxe au modèle, et un serveur **MCP** pour interroger le modèle d'architecture.

Version 1.59.4 du 2026-09-21, dernier commit le 2026-10-07, environ 5,8 k étoiles, licence MIT. Prérequis Node : le README du paquet dit « 20+ », mais le champ `engines` de la dernière version publiée exige `>=22.22.3` — se fier au second, et à la version de Node de l'image Docker (22.x) pour une chaîne sans installation locale.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Une architecture à plusieurs niveaux (contexte, conteneurs, composants) qui doit **rester cohérente** entre ses vues | Un diagramme isolé dans un README → [[Mermaid]], rendu nativement par GitHub et Obsidian |
| Le modèle d'architecture versionné dans le dépôt, relu en PR, publié en site statique | Dessin libre où l'on place chaque forme à la main → [[draw.io]] ou [[Excalidraw]] |
| Des vues générées, que l'agent de code peut lire par MCP plutôt que de les redessiner | Chaîne sans Node : l'outil l'exige, y compris pour la construction en CI (l'image Docker le contourne) |
| Une sortie vers Mermaid, D2 ou draw.io pour les besoins de la doc | Schéma à produire une fois, sans suite : le modèle demande un investissement de départ |

## Mise en œuvre

- Installation — `npm install --save-dev likec4`, ou `npx likec4 start` sans installation, ou l'image Docker
- Point d'entrée — un dossier de fichiers `.c4` ; `likec4 start` pour prévisualiser, `likec4 build` pour le site statique
- Prérequis — Node.js (voir plus haut) ; extension VS Code recommandée pour l'édition
- Exécution — sur le poste et en CI ; le site produit est statique
- Coût — gratuit, MIT ; le développement se finance par dons (OpenCollective, GitHub Sponsors)

## Écosystème

### Alternatives

- [[Mermaid]] — Diagram-as-code open-source (MIT, JavaScript) : décrire flowcharts, séquence, ERD, Gantt… en texte type markdown, versionnable et rendu nativement par GitHub et Obsidian.
- [[draw.io]] — Éditeur de diagrammes GUI open-source (Apache-2.0, JavaScript) : flowcharts, UML, réseaux, org-charts, BPMN… ; app web ou desktop, stockage sur ton drive, export multi-format, embarquable.

## Ressources

- Documentation — https://likec4.dev/
- Dépôt — https://github.com/likec4/likec4
- Documentation — https://playground.likec4.dev/ (bac à sable en ligne)

## Voir aussi

- [[Diagrammes]] — le hub du sous-domaine
- [[Modèle C4]] — les quatre niveaux, et quoi montrer à chacun
- [[Comparatif - Diagrammes]] — ce qui départage les outils du dossier
- [[Excalidraw]] et [[GitDiagram]] — le croquis à main levée, et le schéma tiré d'un dépôt par un modèle
- [[Diátaxis et docs-as-code]] — un schéma C4 est une page d'explication, rangée dans le dépôt
