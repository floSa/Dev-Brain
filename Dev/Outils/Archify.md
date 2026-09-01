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
alternatives: ["[[Dev/Outils/Mermaid|Mermaid]]", "[[Dev/Outils/draw.io|draw.io]]", "[[Dev/Outils/Excalidraw|Excalidraw]]", "[[Dev/Outils/FossFLOW|FossFLOW]]"]
complements: []
tags: [agent-skill, diagram, diagram-as-code, code-assistant, agents]
url_docs: https://tt-a1i.github.io/archify/
url_repo: https://github.com/tt-a1i/archify
---

# Archify

## Pourquoi

Archify (MIT, JavaScript/Node) est un **skill packagé pour agents de code**, pas une librairie de rendu que l'on appelle soi-même. L'agent ne dessine pas : il remplit une **IR JSON typée**, que la chaîne Archify compile de façon **déterministe** en une page HTML autonome, validée contre un schéma. Cinq types de diagrammes couverts : architecture, workflow, séquence, data-flow, lifecycle. En sortie, la page HTML plus des exports SVG, PNG et WebM, une share card 1200×630, et une vue « Architecture Delta » qui met en regard Before / Delta / After. Validation de schéma, règles de layout et traçage de routes encadrent le rendu — le but est de rendre reproductible ce qu'un agent produirait sinon en texte libre.

Le projet se positionne explicitement comme alternative à [[Dev/Outils/Mermaid|Mermaid]] pour ce périmètre. Il est jeune (créé en avril 2026) et publie vite ; sa popularité sur GitHub est très en avance sur son âge, ce qui ne dit rien de sa stabilité.

## Quand l'utiliser

- Faire produire par un agent IA un schéma d'architecture ou de workflow **reproductible** : même IR, même rendu.
- Livrer un diagramme comme artefact autonome (HTML seul fichier, ou SVG/PNG) plutôt que comme bloc de code dans un markdown.
- Documenter une évolution d'architecture avec un avant / après explicite (Architecture Delta).

## Quand NE PAS l'utiliser

- Diagramme rendu **nativement** dans GitHub, GitLab ou Obsidian sans build → [[Dev/Outils/Mermaid|Mermaid]].
- Édition WYSIWYG à la souris : hors périmètre revendiqué → [[Dev/Outils/draw.io|draw.io]], [[Dev/Outils/Excalidraw|Excalidraw]].
- Conversion d'un corpus Mermaid existant : le parsing Mermaid automatique n'est pas fourni.
- Partage hébergé façon service en ligne : Archify produit des fichiers, pas des URLs.
- Sans agent de code dans la boucle : l'outil suppose un agent qui remplit l'IR.

## Installation & plateformes

- Canal générique : `npx skills add tt-a1i/archify -g`.
- Claude Code : dépôt du skill dans `~/.claude/skills/` (global) ou `.claude/skills/` (projet).
- Codex CLI et opencode : `~/.agents/skills/` ou `.agents/skills/`.
- Cursor : `npx -y skills add tt-a1i/archify --skill archify --agent cursor --global --copy --yes`.
- Claude.ai : upload de `archify.zip` dans Settings → Capabilities → Skills.
- Raven : dézipper dans `~/.raven/workspace/skills`. DeepSeek Harness : `dsh plugin --profile web add @tt-a1i/archify-dsh@0.1.0`.
- Agents confirmés compatibles : Claude Code, Cursor, Codex CLI, opencode, Raven, Claude.ai, DeepSeek Harness. Version courante annoncée v2.16.0 (août 2026).

## Pièges

- **Hors périmètre assumé** : pas de parsing Mermaid, pas d'auto-layout généraliste, pas de partage hébergé, pas d'édition WYSIWYG. Ces quatre absences sont documentées par le projet, pas des oublis.
- Le profil « deployment-ownership » n'infère rien d'un système vivant : les données sont saisies à la main, donc elles périment comme n'importe quelle doc.
- Les prérequis Node ne sont chiffrés que sur le canal DeepSeek ; ailleurs, l'environnement attendu n'est pas documenté — vérifier avant d'industrialiser.
- Multiplicité des canaux d'installation : chaque agent a son chemin, une mise à jour n'est pas propagée aux autres.
- Projet récent, cadence de publication soutenue : verrouiller une version dans un projet qui doit rendre le même schéma dans six mois.

## Alternatives

- [[Dev/Outils/Mermaid|Mermaid]] — Diagram-as-code open-source (MIT, JavaScript) : décrire flowcharts, séquence, ERD, Gantt… en texte type markdown, versionnable et rendu nativement par GitHub et Obsidian.
- [[Dev/Outils/draw.io|draw.io]] — Éditeur de diagrammes GUI open-source (Apache-2.0, JavaScript) : flowcharts, UML, réseaux, org-charts, BPMN… ; app web ou desktop, stockage sur ton drive, export multi-format, embarquable.
- [[Dev/Outils/Excalidraw|Excalidraw]] — Whiteboard open-source (MIT) au style croquis à main levée : esquisser vite une architecture ou un schéma, collaboration temps réel, export PNG/SVG, s'intègre à Obsidian.
- [[Dev/Outils/FossFLOW|FossFLOW]] — Application web open-source (Unlicense, bâtie sur Isoflow) pour des diagrammes d'infrastructure isométriques 3D : PWA locale dans le navigateur, icônes AWS/Azure/GCP/K8s, export JSON.

Voisin de forme mais pas de fonction : [[Dev/Outils/Graphify|Graphify]], autre skill d'agent, qui indexe un dépôt au lieu de produire un schéma.

## Liens

- [[Comparatif - Diagrammes]]
- [[Agent skills]] — concept : compétence packagée installée dans un agent de code
- [[Harnais d'agent]] · [[Context engineering]]
- Docs : https://tt-a1i.github.io/archify/ · Repo : https://github.com/tt-a1i/archify
