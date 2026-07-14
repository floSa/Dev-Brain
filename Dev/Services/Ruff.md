---
galaxie: dev
type: service
nom: Ruff
alias: [ruff]
pitch: "Linter et formateur Python écrit en Rust, 10–100× plus rapide : remplace Flake8, Black, isort, pyupgrade et leurs plugins en un seul outil."
categorie: tooling/lint
licence_type: open-source
hosted: self
maturite: production
langage: Rust
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [linter, formatter]
url_docs: https://docs.astral.sh/ruff/
url_repo: https://github.com/astral-sh/ruff
---

# Ruff

## Pourquoi

Linter **et** formateur Python **écrit en Rust** par Astral (les auteurs de [[Dev/Services/uv|uv]]). Plus de 900 règles, ré-implémentations natives des plugins Flake8 populaires, tri des imports (isort), réécritures (pyupgrade) et un formateur compatible Black — le tout **10–100× plus rapide** que les outils qu'il remplace. Un seul binaire et une seule configuration (`pyproject.toml`) à la place de l'empilement Flake8 + Black + isort + pydocstyle + pyupgrade + autoflake.

## Quand l'utiliser

- Linting et formatage de tout projet Python : `ruff check` + `ruff format`.
- Remplacer une chaîne Flake8 + Black + isort par un outil unique, plus rapide.
- Pre-commit et CI : le gain de vitesse est sensible sur les gros dépôts.
- Intégration éditeur (extension VS Code first-party) pour le feedback à la frappe.

## Quand NE PAS l'utiliser

- Vérification de **types** statique : Ruff ne fait pas d'analyse de types → mypy, ou ty (vérificateur de types d'Astral).
- Règle de lint très spécifique d'un plugin Flake8 pas encore portée → garder ponctuellement l'outil d'origine.

## Déploiement & coût

- Binaire unique (`uv add --dev ruff`, ou via pip). MIT, gratuit.
- Local, éditeur et CI ; rien à héberger.

## Pièges

- Linter et formateur sont deux commandes : `ruff check` ne formate pas, `ruff format` ne lint pas.
- Catalogue de règles vaste : activer des familles ciblées plutôt que tout, pour éviter le bruit.
- Évolution rapide : épingler la version pour éviter qu'une nouvelle règle ne casse la CI.

## Alternatives

- Flake8, Black, isort, pylint — outils historiques, chacun spécialisé ; Ruff les regroupe en un binaire Rust bien plus rapide. *(Pages dédiées non encore créées.)*

## Liens

- Même éditeur (Astral) : [[Dev/Services/uv|uv]].
- Doc : https://docs.astral.sh/ruff/
