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
complements: []
tags: [cli, type-hints]
url_docs: https://typer.tiangolo.com/
url_repo: https://github.com/fastapi/typer
---

# Typer

## Pourquoi

Bibliothèque pour construire des **interfaces en ligne de commande** à partir des **annotations de type** Python. On écrit une fonction avec des paramètres typés ; Typer en déduit arguments et options de la CLI, la **validation**, l'**aide** (`--help`) et la **complétion shell** — sans boilerplate. Même auteur que FastAPI (Sebastián Ramírez) et même philosophie : le type hint suffit. Bâti sur **Click** (intégré/vendored depuis la 0.26), dont il hérite la robustesse en simplifiant l'API.

## Quand l'utiliser

- Donner une CLI propre à un script ou un outil Python en quelques lignes.
- Profiter de la complétion automatique et de l'aide générée sans les écrire à la main.
- Projet déjà typé (mypy, Pydantic) : la CLI réutilise les mêmes annotations.

## Quand NE PAS l'utiliser

- Contrôle très fin du parsing ou cas tordus non couverts par l'abstraction → Click directement.
- Dépendance zéro / script jetable → `argparse` de la stdlib.
- Besoin d'une API web, pas d'une CLI → [[FastAPI]].

## Déploiement & coût

- Bibliothèque Python (`uv add typer`). MIT, gratuit.
- Single-node ; rien à héberger.

## Pièges

- Couche au-dessus de Click : pour les besoins avancés, il faut parfois redescendre à l'API Click sous-jacente.
- Le rendu enrichi de l'aide et des erreurs (couleurs, mise en forme) repose sur [[Rich|rich]] : l'installer pour en profiter.
- Commande unique (`typer.run(fn)`) vs application multi-commandes (`app = typer.Typer()` + `@app.command()`) : deux usages distincts, à ne pas mélanger.

## Alternatives

- Click — socle sur lequel Typer est bâti ; API explicite par décorateurs, plus verbeuse mais plus de contrôle. *(Page dédiée non créée.)*
- argparse — parseur de la stdlib, zéro dépendance. *(Page dédiée non créée.)*
- Fire (Google) — CLI générée par introspection, sans annotations. *(Page dédiée non créée.)*

## Liens

- [[Comparatif - Frameworks CLI]] — Typer vs Click / argparse.
- Bâti sur Click ; même auteur que [[FastAPI]] ; rendu terminal via [[Rich|rich]].
- Doc : https://typer.tiangolo.com/
