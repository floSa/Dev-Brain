---
galaxie: dev
type: service
nom: python-dotenv
alias: [dotenv, python_dotenv]
pitch: "Charge les paires clé-valeur d'un fichier `.env` dans les variables d'environnement, pour des applications suivant les 12 facteurs."
categorie: tooling/package
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/dynaconf|dynaconf]]", "[[Dev/Services/hydra|hydra]]", "[[Dev/Services/Pydantic Settings|Pydantic Settings]]"]
remplace_par: []
status: actif
tags: [config]
url_docs: https://github.com/theskumar/python-dotenv#readme
url_repo: https://github.com/theskumar/python-dotenv
---

# python-dotenv

## Pourquoi

Bibliothèque minimale qui **lit un fichier `.env`** (paires `CLÉ=valeur`) et l'injecte dans les **variables d'environnement** du processus (`load_dotenv()`). Elle matérialise le principe **12-factor** : la config vit dans l'environnement, le `.env` sert le développement local sans être versionné. Fournit aussi une **CLI** (`dotenv get/set/list`) et la lecture d'un `.env` sans polluer l'environnement (`dotenv_values()`). Périmètre volontairement étroit : charger un `.env`, rien de plus.

## Quand l'utiliser

- Développement local : centraliser les secrets et réglages dans un `.env` ignoré par Git.
- Briser le couplage code ↔ config en suivant les 12 facteurs, sans dépendance lourde.
- Socle bas niveau réutilisé par d'autres outils (Pydantic Settings, dynaconf savent lire un `.env`).

## Quand NE PAS l'utiliser

- Validation et typage des valeurs chargées → [[Dev/Services/Pydantic Settings|Pydantic Settings]].
- Couches multi-environnements, formats multiples et secrets externes → [[Dev/Services/dynaconf|dynaconf]].
- Composition hiérarchique d'expériences avec overrides CLI → [[Dev/Services/hydra|hydra]].

## Déploiement & coût

- Bibliothèque Python (`uv add python-dotenv`). BSD-3-Clause, gratuit.
- Single-node ; rien à héberger.

## Pièges

- Charge des **chaînes brutes** : aucune coercition de type ni validation (tout est `str`).
- En production, les variables d'environnement réelles doivent primer ; ne pas livrer le `.env` dans l'image.
- N'apporte ni couches ni précédence d'environnements : pour ça, monter en gamme vers dynaconf ou Pydantic Settings.

## Alternatives

- [[Dev/Services/dynaconf|dynaconf]] — Gestion de configuration Python multi-format et multi-environnement : couches par environnement (default/dev/prod), surcharge par variables d'environnement et secrets.
- [[Dev/Services/hydra|hydra]] — Framework de configuration hiérarchique composable (Meta), bâti sur OmegaConf : compositions de configs, surcharge en ligne de commande et balayages multirun — pensé pour les expériences ML.
- [[Dev/Services/Pydantic Settings|Pydantic Settings]] — Configuration typée chargée depuis l'environnement, les fichiers .env et les secrets, bâtie sur Pydantic.

## Liens

- Doc : https://github.com/theskumar/python-dotenv#readme
