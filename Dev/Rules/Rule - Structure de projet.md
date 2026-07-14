---
galaxie: dev
type: rule
domaine: code-style
applicable: global
strictness: should
created: 2026-06-11
modified: 2026-06-11
tags: [rule, reproducibility]
---

# Rule — Structure de projet

## Principe

Un layout standard et prévisible : code sous `src/`, tests sous `tests/`, doc sous `documentation/`, métadonnées dans un seul `pyproject.toml`.

## MUST

- Code applicatif dans `src/<package>/` (src-layout — évite l'import accidentel du paquet depuis le cwd).
- Tests dans `tests/`, miroir de l'arborescence `src/`.
- Un seul `pyproject.toml` à la racine = source unique de vérité (deps, build, config des outils).

## SHOULD

- Documentation dans `documentation/`.
- `README.md` à la racine : quoi, pourquoi, comment lancer.

## NICE-TO-HAVE

- `Makefile` (ou `justfile`) pour les commandes courantes — cf. [[Rule - Packaging démo]].

## Exemples

### Bon

```
mon-projet/
├── pyproject.toml
├── README.md
├── src/mon_projet/__init__.py
├── tests/test_core.py
└── documentation/
```

### Mauvais

```
mon-projet/
├── main.py
├── utils.py
├── test_stuff.py
└── requirements.txt
```

## Exceptions

- Script unique jetable → un seul fichier, pas de cérémonie.

## Voir aussi

- [[Rule - Toolchain Python]], [[Rule - Config typée]], [[Rule - Packaging démo]]
