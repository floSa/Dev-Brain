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
- Sept familles cohabitent, et chacune répond à une question distincte : les paquets ([[uv]], [[pip]]), la qualité ([[Ruff]]), les tests ([[pytest]], [[testcontainers]]), la validation de données ([[Pydantic]]), la configuration ([[Pydantic Settings]], [[dynaconf]], [[hydra]], [[python-dotenv]]), les CLI ([[Typer]], [[Rich]]), les clients d'API ([[Bruno]], [[Postman]]). Les notebooks ont leur sous-dossier.
- La tendance de fond du domaine est la **consolidation en Rust** : un outil rapide qui en remplace six. [[uv]] absorbe pip, pip-tools, pipx, poetry, pyenv et virtualenv ; [[Ruff]] absorbe Flake8, Black, isort et pyupgrade. Ce n'est pas qu'une question de vitesse : c'est un fichier de config au lieu de six.
- **Validation et configuration ne sont pas le même problème**, même quand la même brique les sert. [[Pydantic]] valide une donnée qui entre (requête, fichier, réponse d'API) ; [[Pydantic Settings]] résout une valeur de réglage depuis plusieurs couches (défauts, `.env`, environnement, secrets). Confondre les deux produit des modèles qui portent des mots de passe.

## Choisir

- Nouveau projet Python → [[uv]] et [[Ruff]], sans hésiter. [[pip]] reste le recours quand l'environnement est imposé (image système, CI ancienne).
- Tests → [[pytest]] par défaut ; ajouter [[testcontainers]] dès qu'un test a besoin d'une vraie base ou d'un vrai broker plutôt que d'un mock.
- Configuration : une poignée de variables → [[python-dotenv]] ; une application typée → [[Pydantic Settings]] ; des expériences ML à balayer en multirun → [[hydra]] ; plusieurs environnements et des secrets → [[dynaconf]].
- Une CLI → [[Typer]] ; l'affichage soigné dans le terminal → [[Rich]] (les deux se combinent).
- Tester une API à la main : [[Bruno]] si les collections doivent vivre dans le dépôt git ; [[Postman]] si l'équipe et la collaboration cloud priment.
- Notebooks → voir [[Notebooks]].

<!-- AUTO:START -->
### Sous-domaines
- [[Notebooks]]

### Briques
- [[Bruno]] — Client d'API git-native et open-source : collections en fichiers texte .bru versionnables, 100 % local, sans compte ni cloud.
- [[dynaconf]] — Gestion de configuration Python multi-format et multi-environnement : couches par environnement (default/dev/prod), surcharge par variables d'environnement et secrets.
- [[hydra]] — Framework de configuration hiérarchique composable (organisation communautaire Hydra Ecosystem, ex-Meta), bâti sur OmegaConf : compositions de configs, surcharge en ligne de commande et balayages multirun — pensé pour les expériences ML.
- [[Obsidian]] — Base de connaissances personnelle (propriétaire, gratuit en usage perso) : notes markdown locales, liens bidirectionnels et vue en graphe, extensible par plugins ; le socle de ce DevBrain.
- [[pip]] — Installeur de paquets historique de Python, recommandé par la PyPA : simple, universel, présent partout.
- [[Postman]] — Plateforme d'API tout-en-un : collections, environnements, tests, mocks et doc — la référence du marché, cloud et collaborative.
- [[Pydantic]] — Validation de données pilotée par les annotations de type Python, avec un cœur de validation en Rust : parsing, coercition et erreurs claires.
- [[Pydantic Settings]] — Configuration typée chargée depuis l'environnement, les fichiers .env et les secrets, bâtie sur Pydantic.
- [[pytest]] — Framework de tests Python de référence : assertions natives, fixtures composables et large écosystème de plugins.
- [[python-dotenv]] — Charge les paires clé-valeur d'un fichier `.env` dans les variables d'environnement, pour des applications suivant les 12 facteurs.
- [[Rich]] — Rendu riche dans le terminal : texte couleur et stylé, tables, barres de progression, Markdown, coloration syntaxique et tracebacks lisibles — en quelques lignes.
- [[Ruff]] — Linter et formateur Python écrit en Rust, 10–100× plus rapide : remplace Flake8, Black, isort, pyupgrade et leurs plugins en un seul outil.
- [[testcontainers]] — Dépendances jetables (bases, brokers, navigateurs…) lancées en conteneurs Docker le temps d'un test, démarrées et nettoyées automatiquement.
- [[Typer]] — Construction de CLI en Python à partir des annotations de type : une fonction typée devient une commande, avec aide, complétion shell et validation générées automatiquement. Bâti sur Click.
- [[uv]] — Gestionnaire de paquets et de projets Python écrit en Rust, extrêmement rapide : un seul outil pour remplacer pip, pip-tools, pipx, poetry, pyenv, virtualenv et twine.

### Comparatifs
- [[Comparatif - Clients d'API]]
- [[Comparatif - Gestionnaires de paquets Python]]
<!-- AUTO:END -->
