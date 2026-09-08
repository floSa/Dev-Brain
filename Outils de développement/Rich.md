---
role: brique
nom: Rich
alias: [rich]
pitch: "Rendu riche dans le terminal : texte couleur et stylé, tables, barres de progression, Markdown, coloration syntaxique et tracebacks lisibles — en quelques lignes."
categorie: devtools/cli
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: ["[[Typer]]"]
tags: [terminal-ui]
url_docs: https://rich.readthedocs.io/
url_repo: https://github.com/Textualize/rich
---

# Rich

<!-- AUTO:BANDEAU:START -->
> Rendu riche dans le terminal : texte couleur et stylé, tables, barres de progression, Markdown, coloration syntaxique et tracebacks lisibles — en quelques lignes.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-04-12 |
<!-- AUTO:BANDEAU:END -->

## Définition

Couche de rendu pour le terminal. Un objet `Console` remplace `print` et compose des
éléments que le terminal ne connaît pas nativement : tables, barres de progression,
arbres, panneaux, Markdown, code coloré, et des tracebacks reformatés qui se lisent. Il
interroge les capacités du terminal et dégrade proprement quand elles manquent. Rich ne
parse aucune commande et ne lit aucune entrée : il écrit, et c'est tout — ce qui explique
qu'il serve de couche d'affichage à d'autres outils, pip et Typer compris. Créé par
Will McGugan, il est aussi le socle du framework TUI Textual ; la société Textualize a
fermé en mai 2025, le projet reste maintenu par Will McGugan et une communauté plus
restreinte.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Rendre lisible la sortie d'un script ou d'une CLI : tables, statuts colorés, barres de progression | Hors d'un TTY — fichier, pipe, CI — les couleurs sont désactivées : forcer par `Console(force_terminal=True)` |
| Améliorer logs et tracebacks en développement (`rich.traceback`, handler `logging`) | Le balisage `[bold red]…[/]` entre en conflit avec du texte contenant des crochets : échapper, ou passer par `Text` |
| Afficher du Markdown ou du code coloré directement dans le terminal | Application interactive plein écran, à widgets et événements clavier → Textual, bâti sur Rich |
| | Simples couleurs ANSI portables sans dépendance → colorama ; saisie interactive et REPL → prompt_toolkit |

## Mise en œuvre

- Installation — `uv add rich`
- Point d'entrée — import Python : `rich.console.Console`, `rich.print`, `rich.traceback.install()`
- Prérequis — Python, aucune dépendance lourde ; un terminal capable de couleur pour en profiter
- Exécution — dans le process appelant ; rien à héberger
- Coût — gratuit sous licence MIT

## Écosystème

### Compléments

- [[Typer]] — Construction de CLI en Python à partir des annotations de type : une fonction typée devient une commande, avec aide, complétion shell et validation générées automatiquement. Bâti sur Click. — c'est Rich qu'il appelle pour son aide et ses erreurs enrichies

## Ressources

- Documentation — https://rich.readthedocs.io/
- Dépôt — https://github.com/Textualize/rich

## Voir aussi

- [[Outils de développement]] — le hub du domaine
- [[Comparatif - Frameworks CLI]] — ce qui départage les briques CLI du dossier
