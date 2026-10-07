---
role: brique
nom: PlantUML
alias: [plantuml, plantuml/plantuml, UML en texte]
pitch: "Outil Java (licences au choix : GPL, LGPL, Apache, EPL ou MIT) qui dessine des diagrammes UML et plus de vingt types — séquence, classes, activité, états, Gantt, carte mentale, JSON, YAML — à partir d'une description textuelle, en ligne de commande, en bibliothèque ou compilé pour le navigateur — mais GitHub ne les rend pas nativement, il faut une extension de navigateur ou un rendu en amont."
categorie: design/diagramme
famille: cli
domaines: [ai-eng]
licence_type: open-source
os: "Linux, macOS, Windows"
langage: Java
maturite: production
alternatives: ["[[Mermaid]]", "[[D2]]"]
complements: ["[[Kroki]]"]
tags: [diagram, diagram-as-code]
url_docs: https://plantuml.com
url_repo: https://github.com/plantuml/plantuml
---

# PlantUML

<!-- AUTO:BANDEAU:START -->
> Outil Java (licences au choix : GPL, LGPL, Apache, EPL ou MIT) qui dessine des diagrammes UML et plus de vingt types — séquence, classes, activité, états, Gantt, carte mentale, JSON, YAML — à partir d'une description textuelle, en ligne de commande, en bibliothèque ou compilé pour le navigateur — mais GitHub ne les rend pas nativement, il faut une extension de navigateur ou un rendu en amont.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Java | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Composant Java qui crée des diagrammes à partir d'un texte. Les diagrammes UML (séquence, cas d'utilisation, classes, objets, activité, composants, déploiement, états, temps) y côtoient des types hors UML : JSON et YAML, EBNF, expressions régulières, réseaux (nwdiag), maquettes d'interface (Salt), ArchiMate, Gantt, cartes mentales, WBS, entité-relation et graphiques. Les liens, les infobulles, le texte riche (Creole) et des jeux d'icônes sont disponibles. Il s'utilise en ligne de commande, comme bibliothèque Java, ou compilé en JavaScript par TeaVM pour tourner dans le navigateur sans serveur.

**Licence, à lire en premier.** Le README propose plusieurs licences, **au choix** : GPL, LGPL, Apache, Eclipse Public License ou MIT, avec une FAQ pour savoir laquelle convient. GitHub détecte la LGPL-3.0 ; pour un usage interne, aucune ne gêne. Le dépôt annonce que PlantUML n'est pas touché par la faille log4j. Version 1.2026.8 du 2026-09-05, dépôt poussé le 2026-10-06. Deux nouveautés du README : une extension de navigateur officielle qui dessine les blocs PlantUML dans GitHub (sans serveur), et un serveur MCP en Node.js (`@plantuml/mcp-js`) pour qu'un assistant rende et vérifie des diagrammes.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Des diagrammes UML précis (séquence, classes, états) dans la documentation d'un projet | Un diagramme rendu nativement par GitHub, GitLab ou Obsidian sans extension : [[Mermaid]] |
| Un large catalogue de types de diagrammes dans un même langage, y compris ArchiMate, Gantt et maquettes | Une syntaxe courte et un rendu soigné : [[D2]] |
| Intégrer le rendu à un serveur de documentation ou à une CI : bibliothèque Java, ou [[Kroki]] | Un poste sans Java : l'outil en suppose un, sauf rendu par le navigateur ou par le serveur MCP Node.js |
| Un langage ancien, avec un guide de référence par type de diagramme sur le site | Un modèle d'architecture aux vues calculées : [[LikeC4]] |

## Mise en œuvre

- Installation — le guide d'installation du site ; un fichier `.jar` se lance avec Java, des paquets existent pour la plupart des systèmes
- Point d'entrée — un fichier texte entre `@startuml` et `@enduml`, rendu par la commande, par l'extension de l'éditeur ou par [[Kroki]]
- Prérequis — Java ; l'extension de navigateur ou le rendu TeaVM n'en demandent pas
- Exécution — sur le poste ou en CI
- Coût — gratuit ; au choix GPL, LGPL, Apache, EPL ou MIT

## Écosystème

### Alternatives

- [[Mermaid]] — Diagram-as-code open-source (MIT, JavaScript) : décrire flowcharts, séquence, ERD, Gantt… en texte type markdown, versionnable et rendu nativement par GitHub et Obsidian. — rendu natif par GitHub ; PlantUML couvre plus de types, mais passe par un rendu.
- [[D2]] — Outil en ligne de commande (MPL-2.0, Go) qui transforme un langage de description de diagrammes en SVG, PNG, PDF, GIF ou PPTX, avec thèmes, plusieurs moteurs de placement, rendu au trait de crayon et animations — mais le langage lui est propre, aucune forge ne le rend nativement, et le moteur TALA est un module à part. — une syntaxe plus courte et un rendu plus soigné, au prix d'un catalogue de types plus étroit.

### Compléments

- [[Kroki]] — Serveur HTTP (MIT, Java) à héberger qui donne une seule API pour rendre une vingtaine de langages de diagrammes — PlantUML, Mermaid, D2, GraphViz, BPMN, Excalidraw, DBML, Vega — en SVG ou PNG, par une URL ou une requête POST — mais les langages tournent dans des conteneurs compagnons, et l'instance publique kroki.io reçoit vos sources si on la préfère à la sienne. — rend PlantUML parmi une vingtaine de langages, sans rien installer chez les clients.

## Ressources

- Documentation — https://plantuml.com
- Dépôt — https://github.com/plantuml/plantuml

## Voir aussi

- [[Diagrammes]] — le hub du dossier
- [[Comparatif - Diagrammes]] — où ces outils se départagent
- [[Design & diagrammes]] — le hub du domaine
