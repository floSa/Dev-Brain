---
role: brique
nom: Archify
alias: [archify]
pitch: "Skill d'agent IA (MIT, JavaScript) pour diagrammes d'architecture : l'agent produit une IR JSON typée, compilée de façon déterministe en HTML autonome validé, avec exports SVG/PNG/WebM."
categorie: design/diagramme
famille: extension
domaines: [ai-eng]
licence_type: open-source
os: 
langage: JavaScript
alternatives: ["[[Mermaid]]", "[[draw.io]]", "[[Excalidraw]]", "[[FossFLOW]]"]
complements: []
tags: [agent-skill, diagram, diagram-as-code, code-assistant, agents]
url_docs: https://tt-a1i.github.io/archify/
url_repo: https://github.com/tt-a1i/archify
---

# Archify

<!-- AUTO:BANDEAU:START -->
> Skill d'agent IA (MIT, JavaScript) pour diagrammes d'architecture : l'agent produit une IR JSON typée, compilée de façon déterministe en HTML autonome validé, avec exports SVG/PNG/WebM.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Extension JavaScript | open-source | dans le moteur hôte, rien à héberger | — |
<!-- AUTO:BANDEAU:END -->

## Définition

Archify est un **skill packagé pour agents de code**, pas une bibliothèque de rendu qu'on
appelle soi-même. L'agent ne dessine pas : il remplit une **IR JSON typée**, que la chaîne
Archify compile de façon **déterministe** en une page HTML autonome validée contre un
schéma — même IR, même rendu. Cinq types de diagrammes sont couverts (architecture,
workflow, séquence, data-flow, lifecycle), avec en sortie la page HTML plus des exports
SVG, PNG et WebM, une share card et une vue « Architecture Delta » qui met en regard
Before / Delta / After. Le projet est jeune — créé en avril 2026 — et publie vite.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Faire produire par un agent IA un schéma d'architecture ou de workflow **reproductible** : même IR, même rendu | Sans agent de code dans la boucle : l'outil suppose un agent qui remplit l'IR, il ne s'utilise pas à la main |
| Livrer un diagramme comme artefact autonome — HTML seul fichier, SVG, PNG — plutôt qu'un bloc de code dans un markdown | Quatre absences **documentées par le projet** : pas de parsing Mermaid, pas d'auto-layout généraliste, pas de partage hébergé, pas d'édition WYSIWYG |
| Documenter une évolution d'architecture avec un avant / après explicite (Architecture Delta) | Le profil « deployment-ownership » n'infère rien d'un système vivant : les données sont saisies à la main, donc elles périment comme n'importe quelle doc |
| | Prérequis Node chiffrés sur le seul canal DeepSeek : ailleurs l'environnement attendu n'est pas documenté — à vérifier avant d'industrialiser |
| | Chaque agent a son chemin d'installation, et une mise à jour ne se propage pas aux autres |
| | Projet récent à cadence soutenue : verrouiller une version si le schéma doit être reproductible dans six mois |

## Mise en œuvre

- Installation — canal générique `npx skills add tt-a1i/archify -g` ; Cursor, Codex CLI, opencode, Raven et DeepSeek Harness ont chacun le leur
- Point d'entrée — skill déposé dans le dossier de skills de l'agent : `~/.claude/skills/` ou `.claude/skills/` pour Claude Code, `~/.agents/skills/` pour Codex CLI et opencode ; upload de `archify.zip` sur Claude.ai
- Prérequis — un agent de code compatible (Claude Code, Cursor, Codex CLI, opencode, Raven, Claude.ai, DeepSeek Harness) et Node ; version courante annoncée v2.16.0 (août 2026)
- Exécution — dans l'agent hôte, qui remplit l'IR et lance la compilation ; rien à héberger
- Coût — gratuit, MIT, aucune limite d'usage

## Écosystème

### Alternatives

- [[Mermaid]] — Diagram-as-code open-source (MIT, JavaScript) : décrire flowcharts, séquence, ERD, Gantt… en texte type markdown, versionnable et rendu nativement par GitHub et Obsidian.
- [[draw.io]] — Éditeur de diagrammes GUI open-source (Apache-2.0, JavaScript) : flowcharts, UML, réseaux, org-charts, BPMN… ; app web ou desktop, stockage sur ton drive, export multi-format, embarquable.
- [[Excalidraw]] — Whiteboard open-source (MIT) au style croquis à main levée : esquisser vite une architecture ou un schéma, collaboration temps réel, export PNG/SVG, s'intègre à Obsidian.
- [[FossFLOW]] — Application web open-source (Unlicense, bâtie sur Isoflow) pour des diagrammes d'infrastructure isométriques 3D : PWA locale dans le navigateur, icônes AWS/Azure/GCP/K8s, export JSON.

## Ressources

- Documentation — https://tt-a1i.github.io/archify/
- Dépôt — https://github.com/tt-a1i/archify

## Voir aussi

- [[Agent skills]] — la notion : compétence packagée installée dans un agent de code
- [[Harnais d'agent]] · [[Context engineering]] — le contexte d'exécution du skill
- [[Graphify]] — voisin de forme mais pas de fonction : autre skill d'agent, qui indexe un dépôt au lieu de produire un schéma
- [[Diagrammes]] — le hub du dossier
- [[Comparatif - Diagrammes]] — ce qui départage les outils du dossier
