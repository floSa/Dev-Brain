---
galaxie: dev
type: rule
domaine: dependencies
applicable: global
strictness: must
created: 2026-06-11
modified: 2026-06-11
tags: [rule, package-manager, linter, formatter]
---

# Rule — Toolchain Python

## Principe

Un seul gestionnaire d'environnement ([[uv]]) et un seul outil lint+format ([[Ruff]]) sur tout projet Python — pas d'empilement pip + venv + flake8 + isort + black.

## MUST

- Environnement et dépendances via [[uv]] (`uv init`, `uv add`, `uv run`), `uv.lock` commité.
- Lint **et** format via [[Ruff]] (`ruff check`, `ruff format`), configuré dans `pyproject.toml`.
- Pas de `requirements.txt` édité à la main, pas de `pip install` direct dans le projet.

## SHOULD

- Version de Python épinglée par le projet (`uv python pin`).
- `ruff format` remplace black ; `ruff check --select I` remplace isort.

## NICE-TO-HAVE

- `uvx` pour les outils one-shot, sans les ajouter aux dépendances du projet.

## Exemples

### Bon

```bash
uv init && uv add fastapi
uv run ruff check . && uv run ruff format .
```

### Mauvais

```bash
python -m venv .venv && pip install -r requirements.txt
flake8 . ; isort . ; black .
```

## Exceptions

- Repo legacy sous Poetry/pip : migrer quand on y retouche, pas de big-bang.

## Voir aussi

- [[uv]], [[Ruff]]
- [[Rule - Structure de projet]], [[Rule - Qualité stricte]]
