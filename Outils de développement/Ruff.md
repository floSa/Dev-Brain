---
role: brique
nom: Ruff
alias: [ruff]
pitch: "Linter et formateur Python écrit en Rust, 10–100× plus rapide : remplace Flake8, Black, isort, pyupgrade et leurs plugins en un seul outil."
categorie: devtools/qualite
famille: cli
licence_type: open-source
maturite: production
langage: Rust
alternatives: []
complements: []
tags: [linter, formatter]
url_docs: https://docs.astral.sh/ruff/
url_repo: https://github.com/astral-sh/ruff
---

# Ruff

<!-- AUTO:BANDEAU:START -->
> Linter et formateur Python écrit en Rust, 10–100× plus rapide : remplace Flake8, Black, isort, pyupgrade et leurs plugins en un seul outil.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Rust | open-source | en ligne de commande, rien à héberger | production | à jour · 2026-09-03 |
<!-- AUTO:BANDEAU:END -->

## Définition

Linter **et** formateur Python, écrit par Astral — les auteurs de [[uv]]. Plus de 900
règles, ré-implémentations natives des plugins Flake8 populaires, tri des imports façon
isort, réécritures façon pyupgrade, et un formateur compatible Black : le tout dix à cent
fois plus rapide que les outils qu'il remplace. Un seul binaire et une seule configuration,
dans `pyproject.toml`, à la place de l'empilement Flake8 + Black + isort + pydocstyle +
pyupgrade + autoflake. Deux commandes distinctes, et l'une ne fait pas le travail de
l'autre : `ruff check` lint, `ruff format` formate.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Linter et formater un projet Python avec un outil unique et une configuration unique | Vérification statique de types : Ruff n'en fait pas → mypy, ou ty, le vérificateur d'Astral |
| Remplacer une chaîne Flake8 + Black + isort par un binaire nettement plus rapide | Règle très spécifique d'un plugin Flake8 pas encore portée → garder ponctuellement l'outil d'origine |
| Pre-commit et CI : le gain de vitesse est sensible sur un gros dépôt | Catalogue de plus de 900 règles : tout activer produit du bruit, il faut cibler des familles |
| Retour à la frappe dans l'éditeur, par l'extension VS Code officielle | Évolution rapide : épingler la version, une règle nouvelle peut casser la CI du jour au lendemain |

## Mise en œuvre

- Installation — `uv add --dev ruff`, ou binaire autonome
- Point d'entrée — ligne de commande : `ruff check` pour le lint, `ruff format` pour le formatage
- Prérequis — la configuration tient dans `pyproject.toml` ; extension VS Code officielle pour l'éditeur
- Exécution — sur le poste, dans l'éditeur et en CI ; rien à héberger
- Coût — gratuit sous licence MIT

## Ressources

- Documentation — https://docs.astral.sh/ruff/
- Dépôt — https://github.com/astral-sh/ruff

## Voir aussi

- [[Outils de développement]] — le hub du domaine
