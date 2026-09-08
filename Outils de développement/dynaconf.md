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

<!-- AUTO:BANDEAU:START -->
> Gestion de configuration Python multi-format et multi-environnement : couches par environnement (default/dev/prod), surcharge par variables d'environnement et secrets.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-08-05 |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque de gestion de configuration dont la marque est la **fusion de sources** : elle
lit TOML, YAML, JSON, INI et `.py`, depuis des fichiers, l'environnement, un `.env`, des
fichiers de secrets ou des backends comme Vault et Redis, et les superpose selon une
précédence explicite. Par-dessus, un système de **couches par environnement** — `default`,
`development`, `testing`, `production` — dont chacune hérite de la précédente. N'importe
quelle valeur se surcharge par une variable préfixée `DYNACONF_`, et le basculement
d'environnement se pilote par `ENV_FOR_DYNACONF`. Extensions intégrées pour Django et Flask.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Une application qui tourne sur plusieurs environnements, aux réglages distincts mais hérités | Validation typée stricte, modèles et coercition → [[Pydantic Settings]] |
| Configuration éclatée sur plusieurs formats et fichiers, à fusionner avec une précédence prévisible | Composition hiérarchique d'expériences ML, surcharges CLI et balayages → [[hydra]] |
| Secrets externes (Vault) ou surcharge fine par variable d'environnement, sans toucher au code | Simple chargement d'un `.env`, sans couches ni formats multiples → [[python-dotenv]] |
| Projet Django ou Flask cherchant une couche de configuration unifiée | La richesse des sources se paie : la précédence fichiers / environnement / secrets surprend tant qu'elle n'est pas fixée et documentée |

## Mise en œuvre

- Installation — `uv add dynaconf`
- Point d'entrée — import Python : un objet `Dynaconf(...)` déclarant fichiers, environnements et préfixe
- Prérequis — Python ; les backends externes (Vault, Redis) demandent leurs extras
- Exécution — dans le process appelant, en mémoire ; rien à héberger
- Coût — gratuit sous licence MIT

## Écosystème

### Alternatives

- [[hydra]] — Framework de configuration hiérarchique composable (organisation communautaire Hydra Ecosystem, ex-Meta), bâti sur OmegaConf : compositions de configs, surcharge en ligne de commande et balayages multirun — pensé pour les expériences ML.
- [[python-dotenv]] — Charge les paires clé-valeur d'un fichier `.env` dans les variables d'environnement, pour des applications suivant les 12 facteurs.
- [[Pydantic Settings]] — Configuration typée chargée depuis l'environnement, les fichiers .env et les secrets, bâtie sur Pydantic.

## Ressources

- Documentation — https://www.dynaconf.com/
- Dépôt — https://github.com/dynaconf/dynaconf

## Voir aussi

- [[Outils de développement]] — le hub du domaine
