---
role: hub
nom: Outils de développement
alias: [devtools, outillage, tooling]
pitch: Fabriquer du logiciel — écrire, valider, tester, configurer, packager — par opposition au déployer, qui est du DevOps.
domaines: [data-sci, data-eng, mlops, ml-eng, ai-eng]
tags: [package-manager, linter, testing, config, cli, api-client, data-validation]
---

# Outils de développement

> Fabriquer du logiciel — écrire, valider, tester, configurer, packager — par opposition au déployer, qui est du DevOps.

## Ce qu'il faut comprendre

- Le domaine couvre la **fabrication** : ce qui tourne sur le poste du développeur et dans la CI. Le **déploiement** est ailleurs ([[DevOps]]), et l'**administration** d'une base aussi ([[Bases de données]]).
- Neuf familles cohabitent, et chacune répond à une question distincte : les paquets ([[uv]], [[pip]]), la qualité du code ([[Qualité du code]] : [[Ruff]], [[mypy]], [[Pyright]], [[pre-commit]]), les tests ([[pytest]], [[testcontainers]], [[Hypothesis]]), la validation de données ([[Pydantic]]), la configuration ([[Pydantic Settings]], [[dynaconf]], [[hydra]], [[python-dotenv]]), les CLI ([[Typer]], [[Rich]]), les clients d'API ([[Bruno]], [[Postman]]), la conduite de projet ([[Gestion de projet]] : méthodes, avec ou sans agent), la documentation ([[Documentation technique]] : [[MkDocs]], [[Sphinx]], [[Docusaurus]], [[Zensical]]). Les notebooks ont leur sous-dossier.
- La tendance de fond du domaine est la **consolidation en Rust** : un outil rapide qui en remplace six. [[uv]] absorbe pip, pip-tools, pipx, poetry, pyenv et virtualenv ; [[Ruff]] absorbe Flake8, Black, isort et pyupgrade. Ce n'est pas qu'une question de vitesse : c'est un fichier de config au lieu de six.
- **Validation et configuration ne sont pas le même problème**, même quand la même brique les sert. [[Pydantic]] valide une donnée qui entre (requête, fichier, réponse d'API) ; [[Pydantic Settings]] résout une valeur de réglage depuis plusieurs couches (défauts, `.env`, environnement, secrets). Confondre les deux produit des modèles qui portent des mots de passe.

## Choisir

- Nouveau projet Python → [[uv]] et [[Ruff]], sans hésiter. [[pip]] reste le recours quand l'environnement est imposé (image système, CI ancienne).
- Tests → [[pytest]] par défaut ; ajouter [[testcontainers]] dès qu'un test a besoin d'une vraie base ou d'un vrai broker plutôt que d'un mock, et [[Hypothesis]] pour une fonction de calcul dont les invariants se formulent en propriétés.
- Types et contrôles avant commit → voir [[Qualité du code]] : [[mypy]] ou [[Pyright]] pour les types ([[Comparatif - Vérificateurs de types Python]]), [[pre-commit]] pour rejouer les contrôles avant chaque commit.
- Configuration : une poignée de variables → [[python-dotenv]] ; une application typée → [[Pydantic Settings]] ; des expériences ML à balayer en multirun → [[hydra]] ; plusieurs environnements et des secrets → [[dynaconf]].
- Une CLI → [[Typer]] ; l'affichage soigné dans le terminal → [[Rich]] (les deux se combinent).
- Tester une API à la main : [[Bruno]] si les collections doivent vivre dans le dépôt git ; [[Postman]] si l'équipe et la collaboration cloud priment.
- Notebooks → voir [[Notebooks]].
- Conduire un projet, avec ou sans agent de code (cycle de vie, spécification, backlog, décisions, contexte, revue, versions, mesure) → [[Gestion de projet]] ; documenter ce projet dans son dépôt → [[Documentation technique]] ([[Diátaxis et docs-as-code]] pour quoi écrire, [[Comparatif - Générateurs de documentation]] pour l'outil).
- Rendre une installation reproductible, y compris sans accès à PyPI (verrou, miroir interne, image Docker) → [[Packaging Python et environnements reproductibles]].
- Installer les bonnes versions de Node.js, de Python ou de Go pour chaque projet, avec ses variables et ses tâches dans un seul `mise.toml` → [[mise]] ; pour un projet purement Python, [[uv]] suffit. Une liste de commandes sans gestion de versions → [[just]], rangé dans [[Gestion de projet]].

<!-- AUTO:START -->
### Sous-domaines
- [[Documentation technique]] · [[Gestion de projet]] · [[Notebooks]] · [[Qualité du code]]

### Notions
- [[Packaging Python et environnements reproductibles]] — domaines : data-sci, data-eng, ml-eng, ai-eng, mlops

### Briques
- [[Bruno]] — Client d'API git-native et open-source : collections en fichiers texte .bru versionnables, 100 % local, sans compte ni cloud.
- [[dynaconf]] — Gestion de configuration Python multi-format et multi-environnement : couches par environnement (default/dev/prod), surcharge par variables d'environnement et secrets.
- [[hydra]] — Framework de configuration hiérarchique composable (organisation communautaire Hydra Ecosystem, ex-Meta), bâti sur OmegaConf : compositions de configs, surcharge en ligne de commande et balayages multirun — pensé pour les expériences ML.
- [[Hypothesis]] — Test par propriétés pour Python : on décrit les entrées valides, la bibliothèque en génère des centaines, cherche un contre-exemple et le réduit au plus petit cas qui échoue.
- [[mise]] — Outil en ligne de commande (MIT, Rust) qui installe les outils de développement d'un projet (Node.js, Python, Go et des centaines d'autres), fixe ses variables d'environnement et lance ses tâches depuis un seul `mise.toml` — mais une version demandée comme « 24 » suit la série : il faut une épingle exacte ou un fichier de verrou pour que toute l'équipe ait la même.
- [[Obsidian]] — Base de connaissances personnelle (propriétaire, gratuit en usage perso) : notes markdown locales, liens bidirectionnels et vue en graphe, extensible par plugins ; le socle de ce DevBrain.
- [[pip]] — Installeur de paquets historique de Python, recommandé par la PyPA : simple, universel, présent partout.
- [[Postman]] — Plateforme d'API tout-en-un : collections, environnements, tests, mocks et doc — la référence du marché, cloud et collaborative.
- [[Pydantic]] — Validation de données pilotée par les annotations de type Python, avec un cœur de validation en Rust : parsing, coercition et erreurs claires.
- [[Pydantic Settings]] — Configuration typée chargée depuis l'environnement, les fichiers .env et les secrets, bâtie sur Pydantic.
- [[pytest]] — Framework de tests Python de référence : assertions natives, fixtures composables et large écosystème de plugins.
- [[python-dotenv]] — Charge les paires clé-valeur d'un fichier `.env` dans les variables d'environnement, pour des applications suivant les 12 facteurs.
- [[Rich]] — Rendu riche dans le terminal : texte couleur et stylé, tables, barres de progression, Markdown, coloration syntaxique et tracebacks lisibles — en quelques lignes.
- [[testcontainers]] — Dépendances jetables (bases, brokers, navigateurs…) lancées en conteneurs Docker le temps d'un test, démarrées et nettoyées automatiquement.
- [[Typer]] — Construction de CLI en Python à partir des annotations de type : une fonction typée devient une commande, avec aide, complétion shell et validation générées automatiquement. Bâti sur Click.
- [[uv]] — Gestionnaire de paquets et de projets Python écrit en Rust, extrêmement rapide : un seul outil pour remplacer pip, pip-tools, pipx, poetry, pyenv, virtualenv et twine.

### Comparatifs
- [[Comparatif - Clients d'API]]
- [[Comparatif - Frameworks CLI]]
- [[Comparatif - Gestionnaires de paquets Python]]
<!-- AUTO:END -->
