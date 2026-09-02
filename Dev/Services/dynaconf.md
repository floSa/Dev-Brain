---
role: brique
nom: dynaconf
alias: [Dynaconf]
pitch: "Gestion de configuration Python multi-format et multi-environnement : couches par environnement (default/dev/prod), surcharge par variables d'environnement et secrets."
categorie: devtools/config
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[hydra]]", "[[python-dotenv]]", "[[Pydantic Settings]]"]
complements: []
tags: [config]
url_docs: https://www.dynaconf.com/
url_repo: https://github.com/dynaconf/dynaconf
---

# dynaconf

## Pourquoi

Bibliothèque de **gestion de configuration** pour Python. Sa marque : lire les réglages depuis **plusieurs formats** (TOML, YAML, JSON, INI, `.py`) et **plusieurs sources** (fichiers, variables d'environnement, `.env`, secrets, backends comme Vault et Redis), avec une **précédence claire** entre elles. Système de **couches par environnement** (`default`, `development`, `testing`, `production`) qui se superposent. Surcharge de n'importe quelle valeur par variable d'environnement (préfixe `DYNACONF_`). Extensions intégrées pour Django et Flask.

## Quand l'utiliser

- Une application qui doit tourner sur plusieurs environnements avec des réglages distincts mais hérités.
- Configuration éclatée sur plusieurs formats / fichiers, à fusionner avec une précédence prévisible.
- Besoin de secrets externes (Vault) ou de surcharge fine par variable d'environnement sans toucher au code.
- Projet Django ou Flask cherchant une couche de config unifiée.

## Quand NE PAS l'utiliser

- Validation typée stricte de la config (modèles, coercition) → [[Pydantic Settings]].
- Composition hiérarchique d'expériences ML avec overrides CLI et sweeps → [[hydra]].
- Simple chargement d'un `.env` sans couches ni formats multiples → [[python-dotenv]].

## Déploiement & coût

- Bibliothèque Python (`uv add dynaconf`). MIT, gratuit.
- Single-node, en mémoire ; rien à héberger.

## Pièges

- La richesse des sources et la précédence (fichiers ↔ env ↔ secrets) peuvent surprendre : fixer et documenter l'ordre attendu.
- Pas de validation de schéma native aussi forte que Pydantic : combiner avec un modèle typé si la config est critique.
- Le basculement d'environnement repose sur une variable dédiée (`ENV_FOR_DYNACONF`) : bien cadrer son réglage en CI et en prod.

## Alternatives

- [[hydra]] — Framework de configuration hiérarchique composable (organisation communautaire Hydra Ecosystem, ex-Meta), bâti sur OmegaConf : compositions de configs, surcharge en ligne de commande et balayages multirun — pensé pour les expériences ML.
- [[python-dotenv]] — Charge les paires clé-valeur d'un fichier `.env` dans les variables d'environnement, pour des applications suivant les 12 facteurs.
- [[Pydantic Settings]] — Configuration typée chargée depuis l'environnement, les fichiers .env et les secrets, bâtie sur Pydantic.

## Liens

- Doc : https://www.dynaconf.com/
