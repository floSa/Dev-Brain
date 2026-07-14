---
galaxie: dev
type: service
nom: Rich
alias: [rich]
pitch: "Rendu riche dans le terminal : texte couleur et stylé, tables, barres de progression, Markdown, coloration syntaxique et tracebacks lisibles — en quelques lignes."
categorie: tooling/package
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [terminal-ui]
url_docs: https://rich.readthedocs.io/
url_repo: https://github.com/Textualize/rich
---

# Rich

## Pourquoi

Bibliothèque de **rendu riche dans le terminal**. Un objet `Console` écrit du texte en couleur et stylé, et compose des éléments avancés : **tables**, **barres de progression**, **Markdown**, **coloration syntaxique**, arbres, panneaux et **tracebacks** reformatés et lisibles. Détecte les capacités du terminal et dégrade proprement. Largement adoptée comme couche d'affichage par d'autres outils (pip, Typer…). Créée par Will McGugan (Textualize), socle du framework TUI **Textual**.

## Quand l'utiliser

- Rendre lisible la sortie d'un script ou d'une CLI : tables, statuts colorés, barres de progression.
- Améliorer les logs et les tracebacks en développement (`rich.traceback`, handler `logging`).
- Afficher du Markdown ou du code coloré directement dans le terminal.

## Quand NE PAS l'utiliser

- Application **interactive plein écran** (widgets, événements clavier/souris) → Textual, bâti sur Rich.
- Simple besoin de couleurs ANSI portables, sans dépendance → colorama.
- Saisie interactive avancée (prompts, complétion en ligne) → prompt_toolkit.

## Déploiement & coût

- Bibliothèque Python (`uv add rich`), sans dépendance lourde. MIT, gratuit.
- Single-node ; rien à héberger.

## Pièges

- Société Textualize fermée en mai 2025 ; Rich et Textual restent **maintenus** en open-source par Will McGugan — projet actif, mais porté par une communauté plus restreinte.
- Le balisage par tags (`[bold red]…[/]`) est pratique mais peut entrer en conflit avec du texte contenant des crochets : échapper ou utiliser `Text` pour le contenu non fiable.
- Une sortie redirigée (fichier, pipe) n'est pas un TTY : Rich désactive les couleurs, ce qui peut surprendre en CI — forcer via `Console(force_terminal=True)` si besoin.

## Alternatives

- colorama — couleurs/styles ANSI portables (Windows inclus), minimaliste. *(Page dédiée non créée.)*
- prompt_toolkit — saisie interactive et REPL avancés en terminal. *(Page dédiée non créée.)*
- Textual — framework d'applications TUI plein écran, bâti sur Rich. *(Page dédiée non créée.)*

## Liens

- Utilisé par [[Dev/Services/Typer|Typer]] pour l'aide et les erreurs enrichies.
- Doc : https://rich.readthedocs.io/
