---
role: brique
nom: Typer
alias: [typer]
pitch: "Construction de CLI en Python à partir des annotations de type : une fonction typée devient une commande, avec aide, complétion shell et validation générées automatiquement. Bâti sur Click."
categorie: devtools/cli
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: ["[[Rich]]"]
tags: [cli, type-hints]
url_docs: https://typer.tiangolo.com/
url_repo: https://github.com/fastapi/typer
---

# Typer

<!-- AUTO:BANDEAU:START -->
> Construction de CLI en Python à partir des annotations de type : une fonction typée devient une commande, avec aide, complétion shell et validation générées automatiquement. Bâti sur Click.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-08-28 |
<!-- AUTO:BANDEAU:END -->

## Définition

Construit une interface en ligne de commande à partir des **annotations de type**. On écrit
une fonction dont les paramètres sont typés ; Typer en déduit les arguments et les options,
la validation, le texte de `--help` et la complétion shell — sans code de plomberie. Il est
bâti sur **Click**, intégré au paquet depuis la 0.26, dont il hérite la robustesse en
simplifiant l'API. Deux usages coexistent et ne se mélangent pas : `typer.run(fn)` expose
une commande unique, `typer.Typer()` et `@app.command()` construisent une application
multi-commandes. Même auteur que FastAPI, et même parti pris : l'annotation de type suffit.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Donner une CLI propre à un script ou un outil Python en quelques lignes | Contrôle très fin du parsing, ou cas tordu non couvert par l'abstraction → redescendre à l'API Click sous-jacente |
| Obtenir aide générée et complétion shell sans les écrire à la main | Script jetable, zéro dépendance → `argparse` de la bibliothèque standard |
| Projet déjà typé (mypy, [[Pydantic]]) : la CLI réutilise les mêmes annotations | Besoin d'une API web et non d'une CLI → [[FastAPI]] |

## Mise en œuvre

- Installation — `uv add typer`
- Point d'entrée — import Python : `typer.run(fn)` pour une commande, `typer.Typer()` et `@app.command()` pour plusieurs
- Prérequis — Python ; l'aide et les erreurs enrichies passent par Rich, sinon le rendu reste brut
- Exécution — dans le process appelant ; rien à héberger
- Coût — gratuit sous licence MIT

## Écosystème

### Compléments

- [[Rich]] — Rendu riche dans le terminal : texte couleur et stylé, tables, barres de progression, Markdown, coloration syntaxique et tracebacks lisibles — en quelques lignes. — la couche d'affichage de l'aide et des tracebacks

## Ressources

- Documentation — https://typer.tiangolo.com/
- Dépôt — https://github.com/fastapi/typer

## Voir aussi

- [[Outils de développement]] — le hub du domaine
- [[Comparatif - Frameworks CLI]] — ce qui départage les briques CLI du dossier
