---
role: brique
nom: pre-commit
alias: [pre-commit hooks]
pitch: "Gestionnaire de hooks Git multi-langage (MIT) : un fichier .pre-commit-config.yaml épingle des dépôts de hooks, chacun exécuté dans son environnement isolé avant chaque commit — mais sans réseau il faut miroiter à la fois les dépôts de hooks et les paquets qu'ils installent."
categorie: devtools/qualite
famille: cli
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: ["[[Ruff]]", "[[Gitleaks]]", "[[Semgrep]]"]
tags: [git-hooks]
url_docs: https://pre-commit.com/
url_repo: https://github.com/pre-commit/pre-commit
---

# pre-commit

<!-- AUTO:BANDEAU:START -->
> Gestionnaire de hooks Git multi-langage (MIT) : un fichier .pre-commit-config.yaml épingle des dépôts de hooks, chacun exécuté dans son environnement isolé avant chaque commit — mais sans réseau il faut miroiter à la fois les dépôts de hooks et les paquets qu'ils installent.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Python | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil qui installe dans `.git/hooks` un hook unique et lui fait exécuter la liste de
contrôles déclarée dans `.pre-commit-config.yaml`. Chaque contrôle vient d'un **dépôt de
hooks** épinglé par un `rev:` (tag ou SHA, jamais une branche), cloné dans un cache puis
exécuté dans un environnement isolé propre à son langage (Python, Node, Go, Rust, Docker…).
Un hook qui reformate des fichiers fait échouer le commit : on réindexe puis on recommence.
Version 4.6.2 du 2026-08-10, 15 603 étoiles le 2026-10-01, licence MIT.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Faire tourner les mêmes contrôles sur chaque poste avant le commit : [[Ruff]] (lint et format), détection de secrets avec [[Gitleaks]], motifs avec [[Semgrep]] | Environnement sans accès au réseau : la page principale de pre-commit.com ne décrit aucun mode hors ligne, il faut un miroir git des dépôts de hooks **et** un miroir des paquets (PyPI, npm) |
| Épingler les versions des outils de qualité dans le dépôt, avec `pre-commit autoupdate` pour les faire avancer | Un seul contrôle local suffit : `repo: local` avec `language: system` évite le clonage, mais alors la version de l'outil n'est plus épinglée par pre-commit |
| Un catalogue de hooks prêt à l'emploi : le dépôt `pre-commit-hooks` et les hooks publiés par les éditeurs d'outils | Hooks de vérification de types : le hook tourne dans un environnement isolé qui ne voit pas les dépendances du projet, il faut `additional_dependencies` ou un hook local |
| Les mêmes contrôles en CI sur tout le dépôt, par `pre-commit run --all-files` | Une chaîne sans Python ni Node sur le poste : un binaire unique (prek, lefthook) ou de simples scripts versionnés suffisent |

## Mise en œuvre

- Installation — `uv tool install pre-commit`, puis `pre-commit install` dans le dépôt (type de hook à choisir avec `default_install_hook_types`)
- Point d'entrée — `.pre-commit-config.yaml` à la racine ; `pre-commit run --all-files` à la demande ; `SKIP=<id>` saute un hook, `git commit --no-verify` les saute tous
- Prérequis — Python 3.10 ou plus ; chaque langage de hook réclame son propre exécutable (Node, Go…), sauf pour Python que pre-commit sait amorcer
- Exécution — sur le poste à chaque commit, et en CI interne (GitLab CE, Forgejo, Jenkins, Woodpecker CI) par `pre-commit run --all-files` ; le service pre-commit.ci n'existe que pour GitHub
- Coût — gratuit sous licence MIT ; quatre releases par an en moyenne, avec des trous de quatre mois ; projet porté de fait par un seul mainteneur (Anthony Sottile, 2 263 contributions sur le dépôt)

## Écosystème

### Alternatives

- *Aucune alternative fichée dans le brain. Voisins non fichés : prek (réécriture en Rust, binaire unique, lit le même `.pre-commit-config.yaml` ; 0.5.4 du 2026-09-28, MIT, un seul mainteneur sur un compte personnel, créé en octobre 2024, adopté par CPython, Airflow et FastAPI), lefthook (Go, MIT, sans environnements isolés ni dépôts de hooks) et `core.hooksPath` vers un dossier de scripts versionné, la voie de ce dépôt.*

### Compléments

- [[Ruff]] — Linter et formateur Python écrit en Rust, 10–100× plus rapide : remplace Flake8, Black, isort, pyupgrade et leurs plugins en un seul outil. — dépôt `astral-sh/ruff-pre-commit` (version alignée sur celle de Ruff, ids `ruff-check` et `ruff-format`, `--fix` à placer avant le formateur) ; en alternative, un hook local `uv run ruff` garde une seule version, celle du verrou.
- [[Gitleaks]] — Détecteur de secrets dans un dépôt Git, un répertoire ou un flux (MIT, Go) : 222 règles par défaut en expressions régulières, entropie et mots-clés, hook pre-commit, aucune vérification en ligne — mais l'auteur l'a déclaré « complet », sans nouvelles fonctions, et travaille sur son successeur Betterleaks ; l'action GitHub officielle n'est pas en MIT. — le dépôt publie son propre `.pre-commit-hooks.yaml` ; le hook `gitleaks` compile du Go à l'installation, `gitleaks-system` utilise le binaire déjà présent.
- [[Semgrep]] — Analyse statique de code par motifs, en édition communautaire (moteur LGPL-2.1, Semgrep Inc.) : règles YAML, plus de 30 langages dont Python, sorties SARIF et JSON, utilisable hors ligne avec des règles locales — mais sans analyse entre fichiers ni entre fonctions, et avec des règles du registre sous une licence d'usage interne qui interdit de les redistribuer. — dépôt `semgrep/pre-commit` ; un `--config` pointant vers une URL réclame le réseau, des règles locales non.

## Ressources

- Documentation — https://pre-commit.com/
- Dépôt — https://github.com/pre-commit/pre-commit

## Voir aussi

- [[Outils de développement]] — le hub du domaine
