---
role: brique
nom: mypy
alias: [Mypy]
pitch: "Vérificateur de types statique de référence pour Python (MIT, dépôt python/mypy) : le plus répandu des outils de typage, avec mode strict, daemon, cache incrémental et plugin Pydantic — mais plus lent que les nouveaux vérificateurs en Rust et sans déduction des types de retour."
categorie: devtools/qualite
famille: cli
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Pyright]]"]
complements: ["[[Ruff]]", "[[pre-commit]]", "[[Pydantic]]"]
tags: [type-checker, type-hints]
url_docs: https://mypy.readthedocs.io/
url_repo: https://github.com/python/mypy
---

# mypy

<!-- AUTO:BANDEAU:START -->
> Vérificateur de types statique de référence pour Python (MIT, dépôt python/mypy) : le plus répandu des outils de typage, avec mode strict, daemon, cache incrémental et plugin Pydantic — mais plus lent que les nouveaux vérificateurs en Rust et sans déduction des types de retour.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Python | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Vérificateur de types statique pour Python, issu du dépôt du projet `python` et à l'origine
du typage graduel : il lit les annotations, jamais n'exécute le code, et signale les
incohérences avant l'exécution. Il est lui-même compilé avec mypyc, d'où des roues par
plateforme, et ne réclame ni Node ni binaire externe. Version 2.3.1 du 2026-08-15, 20 653
étoiles le 2026-10-01. Dans l'enquête « Typed Python 2025 » (1 241 réponses),
58 % des répondants disent l'utiliser — c'est le plus répandu, devant des concurrents plus
récents dont l'usage reste à confirmer.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un vérificateur de types en CI : code de retour non nul, `pyproject.toml`, mode `--strict` (13 options activées d'un coup) | Retour d'édition à la frappe dans VS Code : Pylance s'appuie sur Pyright, pas sur mypy → [[Pyright]] |
| Du code Pydantic : le plugin `pydantic.mypy` est maintenu par Pydantic et testé contre la dernière version de mypy | Du code SQLAlchemy 2 : le plugin `sqlalchemy.ext.mypy` est déprécié, le typage natif (`Mapped[]`, `mapped_column()`) le remplace |
| Un gros dépôt : le daemon `dmypy` garde l'état en mémoire, le cache incrémental et `--num-workers` (depuis 2.0) répartissent le travail | Un code non annoté : les fonctions sans annotation sont ignorées par défaut, sauf `--check-untyped-defs` (inclus dans `--strict`) |
| Une chaîne de confiance courte : paquet PyPI officiel, roues compilées, aucun Node | Un dépôt entier à vérifier en quelques secondes : les vérificateurs en Rust (Pyrefly, ty) sont d'un autre ordre de grandeur, au prix d'une maturité moindre |

## Mise en œuvre

- Installation — `uv add --dev mypy` ; stubs tiers par paquets `types-<bibliothèque>` (typeshed)
- Point d'entrée — `mypy src/` ; `dmypy run -- src/` pour le daemon ; configuration dans `[tool.mypy]` de `pyproject.toml` (ou `mypy.ini`)
- Prérequis — Python 3.10 ou plus ; `--python-version` vérifie comme sous une autre version, et `--python-executable` indique l'interpréteur dont lire les paquets typés (PEP 561)
- Exécution — sur le poste, en [[pre-commit]] (dépôt `pre-commit/mirrors-mypy`, dont le hook tourne sans les dépendances du projet : `additional_dependencies` ou hook local) et en CI ; hors ligne, un miroir PyPI interne et les `types-*` installés d'avance, car `--install-types` appelle pip
- Coût — gratuit sous licence MIT ; plusieurs releases par trimestre, 30 contributeurs actifs depuis le 2026-07-01, dernier commit le 2026-09-30

## Écosystème

### Alternatives

- [[Pyright]] — Vérificateur de types statique de Microsoft (MIT, écrit en TypeScript), sans plugins : inférence plus poussée que mypy, quatre modes de rigueur, sortie JSON — mais il exige Node, et le paquet PyPI `pyright` est un wrapper communautaire non affilié à Microsoft ; Pylance, son extension VS Code, est propriétaire. — il vérifie le code non annoté par défaut et déduit les types de retour, là où mypy les laisse `Any` ; mypy accepte des références circulaires que Pyright ne résout pas.
- *Voisins non fichés : Pyrefly (Meta, MIT, stable depuis 1.0 le 2026-05-12) et ty (Astral, MIT, bêta en 0.0.x) — voir le comparatif.*

### Compléments

- [[Ruff]] — Linter et formateur Python écrit en Rust, 10–100× plus rapide : remplace Flake8, Black, isort, pyupgrade et leurs plugins en un seul outil. — Ruff ne vérifie aucun type ; les deux outils se complètent dans le même hook et la même CI.
- [[pre-commit]] — Gestionnaire de hooks Git multi-langage (MIT) : un fichier .pre-commit-config.yaml épingle des dépôts de hooks, chacun exécuté dans son environnement isolé avant chaque commit — mais sans réseau il faut miroiter à la fois les dépôts de hooks et les paquets qu'ils installent. — le hook officiel est un miroir de mypy mis à jour avec lui (v2.3.1) ; le piège est l'environnement isolé qui ne voit pas les dépendances du projet.
- [[Pydantic]] — Validation de données pilotée par les annotations de type Python, avec un cœur de validation en Rust : parsing, coercition et erreurs claires. — plugin `pydantic.mypy`, documenté par Pydantic.
- voisin : [[SQLAlchemy]] — son plugin mypy est déprécié depuis la 2.0 et ne fonctionne que jusqu'à mypy 1.10.1 d'après sa propre documentation ; les modèles déclaratifs `Mapped[]` se vérifient sans plugin.

## Ressources

- Documentation — https://mypy.readthedocs.io/
- Dépôt — https://github.com/python/mypy

## Voir aussi

- [[Typage statique en Python]] — ce que le typage graduel apporte et ce qu'il ne garantit pas
- [[Comparatif - Vérificateurs de types Python]] — ce qui départage les vérificateurs du dossier
- [[Qualité du code]] — le hub du sous-domaine
- [[Outils de développement]] — le hub du domaine
