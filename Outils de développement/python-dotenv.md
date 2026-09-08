---
role: brique
nom: python-dotenv
alias: [dotenv, python_dotenv]
pitch: "Charge les paires clé-valeur d'un fichier `.env` dans les variables d'environnement, pour des applications suivant les 12 facteurs."
categorie: devtools/config
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[dynaconf]]", "[[hydra]]", "[[Pydantic Settings]]"]
complements: []
tags: [config]
url_docs: https://github.com/theskumar/python-dotenv#readme
url_repo: https://github.com/theskumar/python-dotenv
---

# python-dotenv

<!-- AUTO:BANDEAU:START -->
> Charge les paires clé-valeur d'un fichier `.env` dans les variables d'environnement, pour des applications suivant les 12 facteurs.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-08-16 |
<!-- AUTO:BANDEAU:END -->

## Définition

Lit un fichier `.env` — des paires `CLÉ=valeur` — et l'injecte dans les variables
d'environnement du processus, par un `load_dotenv()`. C'est la mise en œuvre littérale du
principe **12-factor** : la configuration vit dans l'environnement, le `.env` sert le
développement local et ne se versionne pas. Une CLI (`dotenv get/set/list`) et une lecture
sans pollution (`dotenv_values()`) complètent l'API. Le périmètre est volontairement étroit
— charger un `.env`, rien de plus — et c'est ce qui en fait un socle bas niveau que d'autres
outils de configuration savent lire à leur tour.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Développement local : centraliser réglages et secrets dans un `.env` ignoré par git | Validation et typage des valeurs chargées → [[Pydantic Settings]] |
| Découpler code et configuration en suivant les 12 facteurs, sans dépendance lourde | Couches multi-environnements, formats multiples et secrets externes → [[dynaconf]] |
| Socle bas niveau, réutilisé par d'autres outils de configuration | Composition hiérarchique d'expériences avec surcharges en ligne de commande → [[hydra]] |
| | Tout arrive en chaîne brute : aucune coercition de type, aucune validation |

## Mise en œuvre

- Installation — `uv add python-dotenv`
- Point d'entrée — import Python : `load_dotenv()`, `dotenv_values()` ; CLI `dotenv get/set/list`
- Prérequis — un fichier `.env` non versionné ; en production les variables d'environnement réelles doivent primer, et le `.env` ne pas entrer dans l'image
- Exécution — dans le process appelant ; rien à héberger
- Coût — gratuit sous licence BSD-3-Clause

## Écosystème

### Alternatives

- [[dynaconf]] — Gestion de configuration Python multi-format et multi-environnement : couches par environnement (default/dev/prod), surcharge par variables d'environnement et secrets.
- [[hydra]] — Framework de configuration hiérarchique composable (organisation communautaire Hydra Ecosystem, ex-Meta), bâti sur OmegaConf : compositions de configs, surcharge en ligne de commande et balayages multirun — pensé pour les expériences ML.
- [[Pydantic Settings]] — Configuration typée chargée depuis l'environnement, les fichiers .env et les secrets, bâtie sur Pydantic.

## Ressources

- Documentation — https://github.com/theskumar/python-dotenv#readme
- Dépôt — https://github.com/theskumar/python-dotenv

## Voir aussi

- [[Outils de développement]] — le hub du domaine
