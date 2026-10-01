---
role: brique
nom: Pyright
alias: [pyright]
pitch: "Vérificateur de types statique de Microsoft (MIT, écrit en TypeScript), sans plugins : inférence plus poussée que mypy, quatre modes de rigueur, sortie JSON — mais il exige Node, et le paquet PyPI `pyright` est un wrapper communautaire non affilié à Microsoft ; Pylance, son extension VS Code, est propriétaire."
categorie: devtools/qualite
famille: cli
licence_type: open-source
maturite: production
langage: TypeScript
alternatives: ["[[mypy]]"]
complements: ["[[Ruff]]", "[[pre-commit]]"]
tags: [type-checker, type-hints]
url_docs: https://microsoft.github.io/pyright/
url_repo: https://github.com/microsoft/pyright
---

# Pyright

<!-- AUTO:BANDEAU:START -->
> Vérificateur de types statique de Microsoft (MIT, écrit en TypeScript), sans plugins : inférence plus poussée que mypy, quatre modes de rigueur, sortie JSON — mais il exige Node, et le paquet PyPI `pyright` est un wrapper communautaire non affilié à Microsoft ; Pylance, son extension VS Code, est propriétaire.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI TypeScript | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Vérificateur de types statique écrit par Microsoft en TypeScript, distribué sur npm. Il
vérifie par défaut le code non annoté, déduit les types de retour, et tient les quatre
modes `off`, `basic`, `standard` (le défaut) et `strict`. Il n'a **pas de plugins** : la
documentation l'écrit comme un choix, et s'appuie sur les extensions du système de types
(`dataclass_transform`, PEP 681). Version 1.1.414 du 2026-09-09, 15 669 étoiles le
2026-10-01. Pylance, l'extension de VS Code qui le prolonge, est
propriétaire.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un retour rapide dans l'éditeur : VS Code (Pylance ou extension Pyright), serveur de langage standard pour les autres éditeurs | Un poste ou une CI sans Node : le paquet PyPI `pyright` n'est pas édité par Microsoft, c'est le wrapper de Robert Craigie, qui embarque Pyright mais réclame Node (extra `[nodejs]` ou Node dans le `PATH`, sinon `nodeenv` le télécharge) |
| Un code annoté en grande partie : l'inférence plus poussée (types de retour, union plutôt que join, narrowing à l'affectation) trouve plus d'erreurs que mypy sans configuration | Un plugin de bibliothèque : il n'y en a pas, et la documentation en fait un choix de conception ; sont pris en charge ce que `dataclass_transform` et les types natifs permettent (Pydantic, SQLAlchemy 2 avec `Mapped[]`) |
| Une sortie lisible par machine : `--outputjson` et des codes de retour documentés (0 à 4) | La vitesse seule : dans le banc d'essai de Microsoft même, mypy est plus rapide sur 8 projets comparables sur 8, avec 3 à 4 fois moins de mémoire |
| Adopter progressivement avec un fichier de référence : le fork basedpyright ajoute une *baseline* | Un usage hors des produits Microsoft de Pylance, l'extension de VS Code : son code n'est pas ouvert, et ses conditions d'usage lues (sur une copie tierce de 2021, à relire sur la version courante) la limitent aux produits Microsoft |

## Mise en œuvre

- Installation — `uv add --dev pyright[nodejs]` (wrapper PyPI, Node embarqué par `nodejs-wheel-binaries`), ou `npm install pyright` ; le fork `basedpyright` embarque Node d'office
- Point d'entrée — `pyright src/` ; configuration dans `[tool.pyright]` de `pyproject.toml` ou `pyrightconfig.json` ; `typeCheckingMode` choisit la rigueur
- Prérequis — Node 14 ou plus ; le wrapper PyPI inclut Pyright 1.1.414 dans sa roue de 6,2 Mo (dossier `pyright/dist` vérifié), donc aucun `npm install` au premier lancement tant qu'on ne force pas une autre version
- Exécution — sur le poste, en hook ([[pre-commit]], dépôt `RobertCraigie/pyright-python`) et en CI ; hors ligne, éviter `PYRIGHT_PYTHON_FORCE_VERSION`, qui retélécharge
- Coût — gratuit sous licence MIT ; 23 contributeurs actifs depuis le 2026-07-01, surtout l'équipe Pylance de Microsoft ; une release tous les un à deux mois depuis début 2026

## Écosystème

### Alternatives

- [[mypy]] — Vérificateur de types statique de référence pour Python (MIT, dépôt python/mypy) : le plus répandu des outils de typage, avec mode strict, daemon, cache incrémental et plugin Pydantic — mais plus lent que les nouveaux vérificateurs en Rust et sans déduction des types de retour. — il accepte des références circulaires que Pyright ne résout pas, a un système de plugins et ignore le code non annoté par défaut ; sur le banc d'essai de Microsoft il est plus rapide que Pyright.
- *Voisins non fichés : basedpyright (DetachHead, MIT, 1.40.1 du 2026-09-10, fusionne chaque release de Pyright), Pyrefly (Meta, stable depuis 1.0) et ty (Astral, bêta) — voir le comparatif.*

### Compléments

- [[Ruff]] — Linter et formateur Python écrit en Rust, 10–100× plus rapide : remplace Flake8, Black, isort, pyupgrade et leurs plugins en un seul outil. — Ruff ne vérifie aucun type ; les deux outils se complètent.
- [[pre-commit]] — Gestionnaire de hooks Git multi-langage (MIT) : un fichier .pre-commit-config.yaml épingle des dépôts de hooks, chacun exécuté dans son environnement isolé avant chaque commit — mais sans réseau il faut miroiter à la fois les dépôts de hooks et les paquets qu'ils installent. — le hook `pyright` du wrapper s'installe dans un environnement isolé qui ne voit pas les dépendances du projet : les ajouter, ou renseigner `venvPath` et `venv`.
- voisin : [[Pydantic]] — `ModelMetaclass` est décoré de `dataclass_transform` dans le code de Pydantic, ce qui permet à Pyright de déduire la signature des modèles sans plugin.

## Ressources

- Documentation — https://microsoft.github.io/pyright/
- Dépôt — https://github.com/microsoft/pyright

## Voir aussi

- [[Typage statique en Python]] — ce que le typage graduel apporte et ce qu'il ne garantit pas
- [[Comparatif - Vérificateurs de types Python]] — ce qui départage les vérificateurs du dossier
- [[Qualité du code]] — le hub du sous-domaine
- [[Outils de développement]] — le hub du domaine
