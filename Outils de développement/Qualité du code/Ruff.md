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
complements: ["[[Semgrep]]", "[[pre-commit]]", "[[mypy]]", "[[Pyright]]"]
tags: [linter, formatter]
url_docs: https://docs.astral.sh/ruff/
url_repo: https://github.com/astral-sh/ruff
---

# Ruff

<!-- AUTO:BANDEAU:START -->
> Linter et formateur Python écrit en Rust, 10–100× plus rapide : remplace Flake8, Black, isort, pyupgrade et leurs plugins en un seul outil.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Rust | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Linter **et** formateur Python, écrit par Astral — les auteurs de [[uv]]. Plus de 900
règles, ré-implémentations natives des plugins Flake8 populaires, tri des imports façon
isort, réécritures façon pyupgrade, et un formateur compatible Black : le tout dix à cent
fois plus rapide que les outils qu'il remplace. Un seul binaire et une seule configuration,
dans `pyproject.toml`, à la place de l'empilement Flake8 + Black + isort + pydocstyle +
pyupgrade + autoflake. Deux commandes distinctes, et l'une ne fait pas le travail de
l'autre : `ruff check` lint, `ruff format` formate. Version 0.16.9 du 2026-09-24, environ
49,9 k étoiles le 2026-10-01, licence MIT.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Linter et formater un projet Python avec un outil unique et une configuration unique | Vérification statique de types : Ruff n'en fait pas → [[mypy]] ou [[Pyright]] ; ty, le vérificateur d'Astral, est encore en bêta |
| Remplacer une chaîne Flake8 + Black + isort par un binaire nettement plus rapide | Règle très spécifique d'un plugin Flake8 pas encore portée → garder ponctuellement l'outil d'origine |
| [[pre-commit]] et CI : le gain de vitesse est sensible sur un gros dépôt, et le dépôt `astral-sh/ruff-pre-commit` fournit les hooks `ruff-check` et `ruff-format` | Catalogue de plus de 900 règles : tout activer produit du bruit, il faut cibler des familles |
| Retour à la frappe dans l'éditeur, par l'extension VS Code officielle | Évolution rapide : épingler la version, une règle nouvelle peut casser la CI du jour au lendemain |

## Mise en œuvre

- Installation — `uv add --dev ruff`, ou binaire autonome
- Point d'entrée — ligne de commande : `ruff check` pour le lint, `ruff format` pour le formatage
- Prérequis — la configuration tient dans `pyproject.toml` ; extension VS Code officielle pour l'éditeur
- Exécution — sur le poste, dans l'éditeur et en CI ; rien à héberger
- Coût — gratuit sous licence MIT ; l'éditeur Astral a annoncé le 2026-03-19 qu'il rejoint OpenAI (équipe Codex) avec l'engagement de poursuivre ses outils ouverts — clôture de la transaction non confirmée à cette date

## Écosystème

### Alternatives

- *Aucune alternative déclarée pour ce dossier.*

### Compléments

- [[Semgrep]] — Analyse statique de code par motifs, en édition communautaire (moteur LGPL-2.1, Semgrep Inc.) : règles YAML, plus de 30 langages dont Python, sorties SARIF et JSON, utilisable hors ligne avec des règles locales — mais sans analyse entre fichiers ni entre fonctions, et avec des règles du registre sous une licence d'usage interne qui interdit de les redistribuer. — les règles `S` de Ruff sont un portage de flake8-bandit (documentation de Ruff), un premier filet de motifs simples ; Semgrep le prolonge avec des règles propres et d'autres langages.
- [[pre-commit]] — Gestionnaire de hooks Git multi-langage (MIT) : un fichier .pre-commit-config.yaml épingle des dépôts de hooks, chacun exécuté dans son environnement isolé avant chaque commit — mais sans réseau il faut miroiter à la fois les dépôts de hooks et les paquets qu'ils installent. — dépôt `astral-sh/ruff-pre-commit` (ids `ruff-check` et `ruff-format`, `--fix` avant le formateur) ; le hook télécharge Ruff depuis PyPI, hors ligne un hook local `uv run ruff` évite le clonage.
- [[mypy]] — Vérificateur de types statique de référence pour Python (MIT, dépôt python/mypy) : le plus répandu des outils de typage, avec mode strict, daemon, cache incrémental et plugin Pydantic — mais plus lent que les nouveaux vérificateurs en Rust et sans déduction des types de retour. — Ruff ne vérifie aucun type : mypy prend le relais pour ce que ni le lint ni le formatage ne couvrent.
- [[Pyright]] — Vérificateur de types statique de Microsoft (MIT, écrit en TypeScript), sans plugins : inférence plus poussée que mypy, quatre modes de rigueur, sortie JSON — mais il exige Node, et le paquet PyPI `pyright` est un wrapper communautaire non affilié à Microsoft ; Pylance, son extension VS Code, est propriétaire. — même répartition : Ruff pour le style et les erreurs évidentes, Pyright pour les types.

## Ressources

- Documentation — https://docs.astral.sh/ruff/
- Dépôt — https://github.com/astral-sh/ruff

## Voir aussi

- [[Qualité du code]] — le hub du sous-domaine
- [[Typage statique en Python]] — ce que le typage graduel apporte et ce qu'il ne garantit pas
- [[Outils de développement]] — le hub du domaine
- [[Packaging Python et environnements reproductibles]] — la notion : pyproject.toml, verrouillage, miroir interne, image Docker reproductible
