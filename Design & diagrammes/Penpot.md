---
role: brique
nom: Penpot
alias: [penpot]
pitch: "Alternative open-source (MPL-2.0) et self-hostable à Figma : design d'interface et prototypage collaboratifs basés sur des standards web (SVG), déployable on-prem — pertinent quand la souveraineté des données compte."
categorie: design/ui
famille: application
domaines: []
licence_type: open-source
os: "Web (self-host Docker)"
langage: Clojure, JavaScript
alternatives: ["[[Figma]]"]
complements: []
tags: [design-tool]
url_docs: https://help.penpot.app/
url_repo: https://github.com/penpot/penpot
---

# Penpot

<!-- AUTO:BANDEAU:START -->
> Alternative open-source (MPL-2.0) et self-hostable à Figma : design d'interface et prototypage collaboratifs basés sur des standards web (SVG), déployable on-prem — pertinent quand la souveraineté des données compte.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application Clojure, JavaScript | open-source | Web (self-host Docker) | — | à jour · 2026-08-27 |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme de design d'interface et de prototypage collaboratif, l'alternative libre à
Figma. Sous licence **MPL-2.0** et **self-hostable** en Docker, ce qui la rend pertinente
dès que la souveraineté des données compte : on-prem, secteurs régulés. Elle est bâtie sur
des **standards web** — SVG, CSS —, si bien que les designs parlent le même langage que le
code et que le passage design → dev n'a pas de format à traverser. Composants, prototypes
interactifs et collaboration temps réel sont là ; l'écart avec Figma se joue sur la
maturité et sur le nombre de plugins.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Concevoir des interfaces sans dépendre d'un cloud propriétaire : self-host, données maîtrisées | Maturité et richesse de plugins **en retrait** : combler l'écart demande parfois des contournements |
| Contexte on-prem ou souverain où le cloud est écarté | Le self-host est une infra de plus à opérer — mises à jour, sauvegardes |
| Vouloir un format ouvert (SVG) aligné sur le web, sans verrouillage ; import de fichiers Figma disponible | Performances historiquement en deçà sur de très gros fichiers, même si elles progressent |
| | Schéma technique — architecture, réseau, UML — plutôt qu'interface → [[draw.io]] ou [[Mermaid]] |
| | Croquis conceptuel rapide → [[Excalidraw]] |

## Mise en œuvre

- Installation — instance hébergée sur penpot.app, ou self-host Docker
- Point d'entrée — application web, édition collaborative temps réel ; formats basés SVG et CSS
- Prérequis — un navigateur pour l'usage ; Docker et une infra à opérer pour le self-host
- Exécution — Web (self-host Docker)
- Coût — gratuit, MPL-2.0 ; en self-host, le coût est celui de l'infrastructure

## Écosystème

### Alternatives

- [[Figma]] — Plateforme de design d'interface et de prototypage collaboratif (propriétaire, freemium) : design temps réel multi-utilisateurs, prototypes interactifs, dev mode ; l'outil de référence du design produit.

## Ressources

- Documentation — https://help.penpot.app/
- Dépôt — https://github.com/penpot/penpot

## Voir aussi

- [[Design & diagrammes]] — le hub du domaine
- [[Comparatif - Design & prototypage]] — ce qui départage les outils du dossier
