---
role: brique
nom: Pydantic Settings
alias: [pydantic-settings, pydantic_settings, BaseSettings]
pitch: "Configuration typée chargée depuis l'environnement, les fichiers .env et les secrets, bâtie sur Pydantic."
categorie: devtools/config
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[dynaconf]]", "[[hydra]]", "[[python-dotenv]]"]
complements: ["[[Pydantic]]"]
tags: [config, data-validation]
url_docs: https://docs.pydantic.dev/latest/concepts/pydantic_settings/
url_repo: https://github.com/pydantic/pydantic-settings
---

# Pydantic Settings

<!-- AUTO:BANDEAU:START -->
> Configuration typée chargée depuis l'environnement, les fichiers .env et les secrets, bâtie sur Pydantic.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-08-10 |
<!-- AUTO:BANDEAU:END -->

## Définition

Extension de Pydantic dédiée à la **configuration d'application**. Une classe `BaseSettings`
mappe ses champs sur les variables d'environnement, un fichier `.env` et des fichiers de
secrets montés, selon une précédence fixe — init, puis env, puis `.env`, puis secrets. Tout
passe par la validation typée de Pydantic : une valeur manquante ou mal typée fait échouer
le démarrage, pas le premier appel qui s'en sert. Depuis Pydantic v2 c'est un paquet
séparé, `pydantic-settings`, à installer en plus de `pydantic` ; en v1 c'était
`pydantic.BaseSettings`.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Centraliser la configuration d'un service — API, worker, pipeline — et la valider au démarrage | Configuration hiérarchique d'expériences ML, compositions et surcharges en ligne de commande → [[hydra]] |
| Lire l'environnement et un `.env` en développement, des fichiers de secrets en production | Couches multi-environnements sur des formats variés — TOML, YAML, Vault → [[dynaconf]] |
| Typer la configuration : URLs, ports, enums, valeurs par défaut, coercition | Simple chargement d'un `.env` sans modèle → [[python-dotenv]] |
| | Casse et préfixe des variables (`env_prefix`) à cadrer : un nommage flou fait silencieusement échouer le mapping |

## Mise en œuvre

- Installation — `uv add pydantic-settings`, en plus de `pydantic`
- Point d'entrée — import Python : une classe qui hérite de `BaseSettings`, instanciée au démarrage
- Prérequis — Pydantic v2 ; les sources lues sont l'environnement, un `.env` et des fichiers de secrets montés
- Exécution — dans le process appelant, en mémoire ; rien à héberger
- Coût — gratuit sous licence MIT

## Écosystème

### Alternatives

- [[dynaconf]] — Gestion de configuration Python multi-format et multi-environnement : couches par environnement (default/dev/prod), surcharge par variables d'environnement et secrets.
- [[hydra]] — Framework de configuration hiérarchique composable (organisation communautaire Hydra Ecosystem, ex-Meta), bâti sur OmegaConf : compositions de configs, surcharge en ligne de commande et balayages multirun — pensé pour les expériences ML.
- [[python-dotenv]] — Charge les paires clé-valeur d'un fichier `.env` dans les variables d'environnement, pour des applications suivant les 12 facteurs.

### Compléments

- [[Pydantic]] — Validation de données pilotée par les annotations de type Python, avec un cœur de validation en Rust : parsing, coercition et erreurs claires. — le socle dont `BaseSettings` tire son typage

## Ressources

- Documentation — https://docs.pydantic.dev/latest/concepts/pydantic_settings/
- Dépôt — https://github.com/pydantic/pydantic-settings

## Voir aussi

- [[Outils de développement]] — le hub du domaine
