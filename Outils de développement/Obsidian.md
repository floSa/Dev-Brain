---
role: brique
nom: Obsidian
alias: [obsidian, obsidian.md]
pitch: "Base de connaissances personnelle (propriétaire, gratuit en usage perso) : notes markdown locales, liens bidirectionnels et vue en graphe, extensible par plugins ; le socle de ce DevBrain."
categorie: skill/knowledge
domaines: []
licence_type: proprietary
os: "Windows, macOS, Linux, iOS, Android"
langage: 
alternatives: []
complements: []
tags: [note-taking, knowledge-graph]
url_docs: https://help.obsidian.md/
url_repo: 
---

![Graphe Obsidian](img/obsidian_graph_optimized.gif)

# Obsidian

<!-- AUTO:BANDEAU:START -->
> Base de connaissances personnelle (propriétaire, gratuit en usage perso) : notes markdown locales, liens bidirectionnels et vue en graphe, extensible par plugins ; le socle de ce DevBrain.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| — | propriétaire | — | — |
<!-- AUTO:BANDEAU:END -->

## Définition

Base de connaissances personnelle dont le format de stockage est le système de fichiers :
un vault est un dossier de fichiers `.md` sur le disque, pas une base ni un espace distant.
Les notes se relient par des **wikilinks bidirectionnels** — chaque page sait qui la cite —
et l'ensemble se parcourt en graphe. L'extensibilité passe par des plugins : Bases, Canvas,
Dataview, Templater. Le cœur du programme est fermé, mais les données ne le sont pas : ce
sont des fichiers markdown ordinaires, lisibles et éditables sans lui. C'est le socle de ce
DevBrain — le vault courant.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Construire une mémoire de connaissances durable et navigable : notes liées, graphe, recherche | Édition collaborative en temps réel à plusieurs auteurs : ce n'est pas sa cible → un wiki d'équipe |
| Garder ses données en local, en markdown pérenne, sans dépendre d'un SaaS | Documentation publique versionnée par une équipe → un générateur de site sur un dépôt git (MkDocs, Docusaurus) |
| Étendre l'outil à ses usages par plugins : bases de notes, canevas, automatisation | Le programme n'est pas ouvert, même si les notes le sont : aucune reprise possible du cœur |
| | Trop de plugins fragilise le vault — dépendances croisées, casse à la mise à jour |

## Mise en œuvre

- Installation — application de bureau Windows, macOS et Linux ; applications mobiles iOS et Android
- Point d'entrée — un vault, c'est-à-dire un dossier de fichiers markdown ouvert par l'application
- Prérequis — aucun service à joindre : les données sont sur le disque
- Exécution — sur le poste et sur mobile ; la synchronisation entre appareils est à choisir — service officiel, git, ou cloud tiers
- Coût — gratuit en usage personnel, licence commerciale au-delà ; la synchronisation officielle est un service payant

## Ressources

- Documentation — https://help.obsidian.md/

## Voir aussi

- [[Outils de développement]] — le hub du domaine
