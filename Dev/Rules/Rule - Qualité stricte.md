---
galaxie: dev
type: rule
domaine: tests
applicable: global
strictness: should
created: 2026-06-11
modified: 2026-06-11
tags: [rule, linter, type-hints, testing, ci-cd]
---

# Rule — Qualité stricte

## Principe

La qualité est outillée et automatique : lint sélectif, typage strict, hooks avant commit, couverture mesurée.

## MUST

- [[Ruff]] avec un `select` explicite (pas seulement les défauts) : `E, F, I, UP, B`, etc.
- `mypy --strict` sur le code applicatif.
- `pre-commit` installé : `ruff`, `ruff-format` et `mypy` passent avant chaque commit.

## SHOULD

- `pytest-cov` avec un seuil (`--cov-fail-under`), vérifié en CI.
- Mêmes hooks rejoués en CI ([[GitHub Actions]]) — un pre-commit local n'est pas une garantie.

## NICE-TO-HAVE

- `--cov-fail-under` qui monte progressivement plutôt qu'un palier irréaliste d'emblée.

## Exemples

### Bon

```toml
[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B", "SIM"]

[tool.mypy]
strict = true
```

### Mauvais

```toml
# ruff aux défauts seulement, pas de mypy, pas de pre-commit
[tool.ruff]
```

## Exceptions

- `# type: ignore[code]` ponctuel et justifié par un commentaire ; jamais un `ignore` nu et global.

## Voir aussi

- [[Ruff]], [[pytest]], [[GitHub Actions]]
- [[Rule - Toolchain Python]], [[Rule - Config typée]]
