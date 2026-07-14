---
galaxie: dev
type: outil
nom: Penpot
alias: [penpot]
pitch: "Alternative open-source (MPL-2.0) et self-hostable à Figma : design d'interface et prototypage collaboratifs basés sur des standards web (SVG), déployable on-prem — pertinent quand la souveraineté des données compte."
categorie: tooling/design
domaines: []
licence_type: open-source
os: "Web (self-host Docker)"
langage: Clojure, JavaScript
status: actif
alternatives: ["[[Dev/Outils/Figma|Figma]]"]
tags: [design-tool]
url_docs: https://help.penpot.app/
url_repo: https://github.com/penpot/penpot
---

# Penpot

## Pourquoi

Plateforme open-source de **design d'interface et de prototypage** collaboratif — l'alternative libre à Figma. Sous licence **MPL-2.0**, **self-hostable** (Docker), ce qui la rend pertinente dès que la **souveraineté des données** compte (on-prem, secteurs régulés). Bâtie sur des **standards web** (SVG, CSS) : les designs parlent le même langage que le code, ce qui fluidifie le passage design→dev. Composants, prototypes interactifs, collaboration temps réel.

## Quand l'utiliser

- Besoin de design d'interface **sans dépendre d'un cloud propriétaire** : self-host, données maîtrisées.
- Contexte on-prem / souverain où Figma est écarté.
- Volonté d'un format ouvert (SVG) aligné sur le web, sans verrouillage.

## Quand NE PAS l'utiliser

- Équipe déjà outillée Figma sans contrainte de souveraineté : l'écosystème et la maturité de [[Dev/Outils/Figma|Figma]] restent devant.
- Schéma technique plutôt qu'interface → [[Dev/Outils/draw.io|draw.io]] / [[Dev/Outils/Mermaid|Mermaid]].
- Croquis conceptuel rapide → [[Dev/Outils/Excalidraw|Excalidraw]].

## Bases & plateformes

- Open-source **MPL-2.0**, Clojure + JavaScript. Instance hébergée (penpot.app) **ou** self-host Docker.
- Formats basés SVG/web ; import de fichiers Figma.
- Collaboration temps réel, composants, prototypage.

## Pièges

- Maturité et richesse de plugins **en retrait** face à Figma : combler l'écart demande parfois des contournements.
- Le self-host, c'est une infra de plus à opérer (mises à jour, sauvegardes).
- Performances sur très gros fichiers historiquement en deçà de Figma (en progrès).

## Alternatives

- [[Dev/Outils/Figma|Figma]] — Plateforme de design d'interface et de prototypage collaboratif (propriétaire, freemium) : design temps réel multi-utilisateurs, prototypes interactifs, dev mode ; l'outil de référence du design produit.

## Liens

- [[Dev/Patterns/Comparatif - Design & prototypage|Comparatif - Design & prototypage]]
- Docs : https://help.penpot.app/ · Repo : https://github.com/penpot/penpot
