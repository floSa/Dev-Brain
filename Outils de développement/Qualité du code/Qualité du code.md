---
role: hub
nom: Qualité du code
alias: [qualité de code, code quality, qualité statique]
pitch: Contrôler du code Python sans l'exécuter, ou avant qu'il n'entre dans l'historique — style, types, hooks — par opposition au tester, qui exécute le code.
domaines: [data-sci, data-eng, mlops, ml-eng, ai-eng]
tags: [linter, formatter, type-checker, git-hooks]
---

# Qualité du code

> Contrôler du code Python sans l'exécuter, ou avant qu'il n'entre dans l'historique — style, types, hooks — par opposition au tester, qui exécute le code.

## Ce qu'il faut comprendre

- Trois questions distinctes, trois familles d'outils : le **style et les erreurs évidentes** ([[Ruff]], qui lint et formate), les **types** ([[mypy]], [[Pyright]]) et le **moment du contrôle** ([[pre-commit]] et [[Lefthook]], qui n'analysent rien eux-mêmes mais font tourner les autres avant le commit).
- Un linter et un vérificateur de types ne se remplacent pas. [[Ruff]] ne vérifie aucun type ; mypy et Pyright ne reformatent rien. Les deux se placent dans le même hook et la même CI.
- Le typage statique est un sujet à lui seul, et c'est une notion : ce qu'il garantit, ce qu'il ne garantit pas, et comment l'adopter dans du code data et ML sans le geler — voir [[Typage statique en Python]].
- Le domaine bouge vite. Deux vérificateurs écrits en Rust (Pyrefly, de Meta, stable depuis le 2026-05-12 ; ty, d'Astral, en bêta) sont plusieurs fois plus rapides que mypy et Pyright. Ils sont cités dans le comparatif sans fiche : l'un a cinq mois de recul, l'autre n'a pas de version stable.
- Les tests ne sont pas ici : [[pytest]] et [[Hypothesis]] exécutent le code, ils vivent avec les outils de test du domaine ([[Outils de développement]]).

## Choisir

- Linter et formater un projet Python → [[Ruff]], sans hésiter.
- Un vérificateur de types en CI, avec Pydantic ou un code existant à adopter par étapes → [[mypy]] ; le retour à la frappe dans VS Code, sans plugin → [[Pyright]]. Le détail est dans [[Comparatif - Vérificateurs de types Python]].
- Rejouer ces contrôles avant chaque commit → [[pre-commit]] ; hors ligne, prévoir le miroir des dépôts de hooks et des paquets. Des crochets en parallèle, par un binaire unique, qui lancent les commandes déjà présentes sur le poste (projet non Python compris) → [[Lefthook]].

<!-- AUTO:START -->
### Notions
- [[Typage statique en Python]] — domaines : data-sci, data-eng, ml-eng, ai-eng, mlops

### Briques
- [[mypy]] — Vérificateur de types statique de référence pour Python (MIT, dépôt python/mypy) : le plus répandu des outils de typage, avec mode strict, daemon, cache incrémental et plugin Pydantic — mais plus lent que les nouveaux vérificateurs en Rust et sans déduction des types de retour.
- [[pre-commit]] — Gestionnaire de hooks Git multi-langage (MIT) : un fichier .pre-commit-config.yaml épingle des dépôts de hooks, chacun exécuté dans son environnement isolé avant chaque commit — mais sans réseau il faut miroiter à la fois les dépôts de hooks et les paquets qu'ils installent.
- [[Pyright]] — Vérificateur de types statique de Microsoft (MIT, écrit en TypeScript), sans plugins : inférence plus poussée que mypy, quatre modes de rigueur, sortie JSON — mais il exige Node, et le paquet PyPI `pyright` est un wrapper communautaire non affilié à Microsoft ; Pylance, son extension VS Code, est propriétaire.
- [[Ruff]] — Linter et formateur Python écrit en Rust, 10–100× plus rapide : remplace Flake8, Black, isort, pyupgrade et leurs plugins en un seul outil.

### Comparatifs
- [[Comparatif - Vérificateurs de types Python]]
<!-- AUTO:END -->
