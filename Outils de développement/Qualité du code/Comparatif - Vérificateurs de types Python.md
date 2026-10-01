---
role: comparatif
nom: Comparatif - Vérificateurs de types Python
categorie: devtools/qualite
tags: [type-checker, type-hints]
---

# Comparatif - Vérificateurs de types Python

> On tranche sur : la **maturité et les plugins** (mypy) contre l'**éditeur et l'inférence** (Pyright) — et sur la vitesse, qu'aucun des deux ne donne face aux vérificateurs en Rust, qui n'ont pas encore la même maturité.

![[Comparatif - Vérificateurs de types Python.base]]

## Ce qui départage

- [[mypy]] — le plus répandu (58 % des répondants de l'enquête « Typed Python 2025 »), seul des deux à avoir des **plugins** (`pydantic.mypy` ; celui de SQLAlchemy est déprécié). Ignore le code non annoté par défaut et ne déduit pas les types de retour. Roues compilées, aucun Node : l'installation hors ligne se résume à un miroir PyPI et aux `types-*`. Plus rapide que Pyright dans le banc d'essai de Microsoft (pandas : 50,2 s contre 96,8 s), avec trois à quatre fois moins de mémoire.
- [[Pyright]] — l'**éditeur** : le moteur de Pylance dans VS Code, serveur de langage standard ailleurs. Vérifie le code non annoté, déduit les types de retour, `--outputjson` pour la CI. Aucun plugin, par choix ; Pydantic passe par `dataclass_transform`. Réclame **Node** : le paquet PyPI `pyright` est un wrapper non affilié à Microsoft, qui ne règle le problème qu'avec l'extra `[nodejs]`.
- *Non fichés, écartés avec leurs raisons.* **Pyrefly** (Meta, MIT, stable depuis la 1.0 du 2026-05-12) : sérieux candidat, mais cinq mois de recul seulement, un seul éditeur sans engagement écrit, et une politique de version qui admet de **nouvelles erreurs à chaque version mineure** ; Pydantic, Django et attrs sont intégrés, sans plugin. **ty** (Astral, MIT, en bêta, versions 0.0.x) : ruptures de diagnostics possibles entre deux versions, pas de plugins, `TypeVarTuple` et `TypeGuard` encore ouverts, une faille d'exécution corrigée en 0.0.84 ; Astral a annoncé le 2026-03-19 rejoindre OpenAI. **basedpyright** : fork communautaire de Pyright (MIT) qui embarque Node et ajoute une *baseline* pour adopter progressivement.

## Voir aussi

- [[Typage statique en Python]] — ce que le typage graduel apporte, et ce qu'il ne garantit pas
- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
