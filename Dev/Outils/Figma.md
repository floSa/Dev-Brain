---
galaxie: dev
type: outil
nom: Figma
alias: [figma]
pitch: "Plateforme de design d'interface et de prototypage collaboratif (propriétaire, freemium) : design temps réel multi-utilisateurs, prototypes interactifs, dev mode ; l'outil de référence du design produit."
categorie: tooling/design
domaines: []
licence_type: proprietary
os: "Web, Windows, macOS"
langage: 
status: actif
alternatives: ["[[Dev/Outils/Penpot|Penpot]]"]
tags: [design-tool]
url_docs: https://help.figma.com/
url_repo: 
---

# Figma

## Pourquoi

Plateforme de **design d'interface (UI/UX) et de prototypage** collaborative, devenue le standard du design produit. Édition **temps réel multi-utilisateurs** dans le navigateur, systèmes de composants et de variables (design system), prototypes interactifs cliquables, et un **dev mode** qui expose mesures, tokens et bouts de code aux développeurs. Écosystème de plugins riche. Propriétaire, freemium (gratuit limité, payant par éditeur au-delà).

## Quand l'utiliser

- Concevoir des **interfaces** et des maquettes haute-fidélité, seul ou en équipe design.
- Maintenir un **design system** partagé (composants, styles, variables).
- Passer le relais aux devs proprement (dev mode : specs, tokens, export).

## Quand NE PAS l'utiliser

- Exigence **open-source / self-host / souveraineté des données** → [[Dev/Outils/Penpot|Penpot]].
- Schéma technique (archi, réseau, UML) plutôt qu'interface → [[Dev/Outils/draw.io|draw.io]] / [[Dev/Outils/Mermaid|Mermaid]].
- Croquis conceptuel rapide → [[Dev/Outils/Excalidraw|Excalidraw]].

## Bases & plateformes

- **Propriétaire**, freemium. Web + apps desktop Windows/macOS + apps mobiles de consultation.
- Données hébergées par Figma (cloud) — point d'attention en contexte on-prem / sensible.
- Nombreux plugins et intégrations (Slack, Jira, tokens…).

## Pièges

- **Cloud propriétaire** : données chez l'éditeur, pas de self-host — rédhibitoire pour certains contextes régulés / souverains.
- Coût par éditeur qui grimpe avec l'équipe.
- Verrouillage : format propriétaire, export/interop limités hors de l'écosystème.

## Alternatives

- [[Dev/Outils/Penpot|Penpot]] — Alternative open-source (MPL-2.0) et self-hostable à Figma : design d'interface et prototypage collaboratifs basés sur des standards web (SVG), déployable on-prem — pertinent quand la souveraineté des données compte.

## Liens

- [[Dev/Patterns/Comparatif - Design & prototypage|Comparatif - Design & prototypage]]
- Docs : https://help.figma.com/
