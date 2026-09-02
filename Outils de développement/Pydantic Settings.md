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
complements: []
tags: [config, data-validation]
url_docs: https://docs.pydantic.dev/latest/concepts/pydantic_settings/
url_repo: https://github.com/pydantic/pydantic-settings
---

# Pydantic Settings

## Pourquoi

Extension de [[Pydantic]] dédiée à la **configuration d'application**. Une classe `BaseSettings` mappe automatiquement ses champs sur les **variables d'environnement**, les fichiers **`.env`**, les **secrets** (fichiers montés) et d'autres sources, le tout **validé et typé** par Pydantic. C'était `pydantic.BaseSettings` en v1 ; depuis Pydantic **v2**, c'est un paquet séparé (`pydantic-settings`). Source de configuration unique, hiérarchisée (précédence des sources) et fail-fast au démarrage si une valeur manque ou est mal typée.

## Quand l'utiliser

- Centraliser la configuration d'un service (API, worker, pipeline) avec validation au démarrage.
- Charger des réglages depuis l'environnement et un `.env` en dev, des secrets en production.
- Profiter du typage Pydantic pour la config (URLs, ports, enums, valeurs par défaut).

## Quand NE PAS l'utiliser

- Configuration hiérarchique complexe d'expériences ML (compositions, overrides CLI) → [[hydra]].
- Multi-environnements avec couches et formats variés (TOML/YAML/Vault) → [[dynaconf]].
- Simple chargement d'un `.env` sans modèle → [[python-dotenv]].

## Déploiement & coût

- Bibliothèque Python (`uv add pydantic-settings`). MIT, gratuit.
- Single-node, en mémoire ; rien à héberger.

## Pièges

- Paquet **distinct** de Pydantic : installer `pydantic-settings` en plus de `pydantic`.
- Précédence des sources (init > env > `.env` > secrets) à connaître pour éviter les surprises.
- Sensibilité à la casse et au préfixe des variables selon la config (`env_prefix`) : bien cadrer le nommage.

## Alternatives

- [[dynaconf]] — Gestion de configuration Python multi-format et multi-environnement : couches par environnement (default/dev/prod), surcharge par variables d'environnement et secrets.
- [[hydra]] — Framework de configuration hiérarchique composable (organisation communautaire Hydra Ecosystem, ex-Meta), bâti sur OmegaConf : compositions de configs, surcharge en ligne de commande et balayages multirun — pensé pour les expériences ML.
- [[python-dotenv]] — Charge les paires clé-valeur d'un fichier `.env` dans les variables d'environnement, pour des applications suivant les 12 facteurs.

Pydantic Settings se distingue par la **validation typée** Pydantic appliquée aux variables d'environnement et aux `.env`.

## Liens

- Socle de validation : [[Pydantic]].
- Doc : https://docs.pydantic.dev/latest/concepts/pydantic_settings/
