---
role: brique
nom: Figma
alias: [figma]
pitch: "Plateforme de design d'interface et de prototypage collaboratif (propriétaire, freemium) : design temps réel multi-utilisateurs, prototypes interactifs, dev mode ; l'outil de référence du design produit."
categorie: design/ui
famille: saas
domaines: []
licence_type: proprietary
os: "Web, Windows, macOS"
langage: 
alternatives: ["[[Penpot]]"]
complements: []
tags: [design-tool]
url_docs: https://help.figma.com/
url_repo: 
---

# Figma

<!-- AUTO:BANDEAU:START -->
> Plateforme de design d'interface et de prototypage collaboratif (propriétaire, freemium) : design temps réel multi-utilisateurs, prototypes interactifs, dev mode ; l'outil de référence du design produit.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| SaaS | propriétaire | — | — | aucun amont fiché |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme de design d'interface et de prototypage collaborative, devenue le standard du
design produit. Édition temps réel multi-utilisateurs dans le navigateur, systèmes de
composants et de variables pour tenir un design system, prototypes interactifs cliquables,
et un **dev mode** qui expose mesures, tokens et bouts de code aux développeurs. L'écosystème
de plugins est le plus riche du domaine. La contrepartie tient en une phrase : le service est
un **cloud fermé, sans self-host**, les fichiers sont chez l'éditeur, et le format
n'est pas ouvert.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Concevoir des interfaces et des maquettes haute-fidélité, seul ou en équipe design | **Cloud propriétaire, aucun self-host** : les données restent chez l'éditeur — rédhibitoire en contexte régulé ou souverain |
| Maintenir un design system partagé — composants, styles, variables | Coût par éditeur, qui grimpe avec la taille de l'équipe |
| Passer le relais aux développeurs proprement : specs, tokens, export via le dev mode | Format propriétaire : export et interopérabilité limités hors de l'écosystème |
| | Schéma technique — architecture, réseau, UML — plutôt qu'interface → [[draw.io]] ou [[Mermaid]] |
| | Croquis conceptuel rapide → [[Excalidraw]] |

## Mise en œuvre

- Installation — rien pour le web ; applications desktop Windows et macOS, apps mobiles de consultation
- Point d'entrée — application web ou desktop, édition collaborative temps réel ; nombreux plugins et intégrations (Slack, Jira, tokens)
- Prérequis — un compte Figma ; les fichiers sont hébergés par l'éditeur, sans option d'auto-hébergement
- Exécution — Web, Windows, macOS
- Coût — **propriétaire**, freemium : gratuit et limité, puis facturé par éditeur

## Écosystème

### Alternatives

- [[Penpot]] — Alternative open-source (MPL-2.0) et self-hostable à Figma : design d'interface et prototypage collaboratifs basés sur des standards web (SVG), déployable on-prem — pertinent quand la souveraineté des données compte.

## Ressources

- Documentation — https://help.figma.com/

## Voir aussi

- [[Design & diagrammes]] — le hub du domaine
- [[Comparatif - Design & prototypage]] — ce qui départage les outils du dossier
