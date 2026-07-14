---
galaxie: dev
type: service
nom: hydra
alias: [Hydra, hydra-core]
pitch: "Framework de configuration hiérarchique composable (Meta), bâti sur OmegaConf : compositions de configs, surcharge en ligne de commande et balayages multirun — pensé pour les expériences ML."
categorie: tooling/package
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/dynaconf|dynaconf]]", "[[Dev/Services/python-dotenv|python-dotenv]]", "[[Dev/Services/Pydantic Settings|Pydantic Settings]]"]
remplace_par: []
status: actif
tags: [config]
url_docs: https://hydra.cc/docs/intro/
url_repo: https://github.com/facebookresearch/hydra
---

# hydra

## Pourquoi

Framework de configuration pour applications complexes, développé par **Meta** (Facebook Research). Sa marque : **composer dynamiquement** une configuration hiérarchique à partir de groupes de fichiers (`config groups`), puis la **surcharger en ligne de commande**. Bâti sur **OmegaConf** (résolution d'interpolations, fusion, typage structuré). Le mode **multirun** lance automatiquement une même tâche sur un balayage de paramètres (sweeps), et des launchers/sweepers (Joblib, Optuna, Ax, soumission cluster) s'y branchent. Installation via `hydra-core`.

## Quand l'utiliser

- Expériences ML où l'on veut faire varier modèle, dataset, optimiseur via des combinaisons de configs.
- Lancer des balayages d'hyperparamètres ou de configurations en une commande (`--multirun`).
- Applications à configuration profondément hiérarchique, surchargée depuis la CLI sans réécrire les fichiers.

## Quand NE PAS l'utiliser

- Simple service web ayant besoin d'une config typée et validée → [[Dev/Services/Pydantic Settings|Pydantic Settings]].
- Multi-environnements applicatifs (default/dev/prod) avec secrets et formats variés → [[Dev/Services/dynaconf|dynaconf]].
- Charger quelques variables depuis un `.env` → [[Dev/Services/python-dotenv|python-dotenv]].

## Déploiement & coût

- Bibliothèque Python (`uv add hydra-core`). MIT, gratuit.
- Single-node ; le multirun peut déléguer l'exécution à un launcher distribué, mais Hydra lui-même n'héberge rien.

## Pièges

- Courbe d'apprentissage : composition, `defaults` list et interpolations OmegaConf demandent un temps d'appropriation.
- Hydra prend la main sur le répertoire de travail (un dossier de run par exécution) : surprend en debug et en logging.
- Pensé pour les scripts/expériences ; l'intégrer dans un service applicatif classique est moins naturel que Pydantic Settings ou dynaconf.

## Alternatives

- [[Dev/Services/dynaconf|dynaconf]] — Gestion de configuration Python multi-format et multi-environnement : couches par environnement (default/dev/prod), surcharge par variables d'environnement et secrets.
- [[Dev/Services/python-dotenv|python-dotenv]] — Charge les paires clé-valeur d'un fichier `.env` dans les variables d'environnement, pour des applications suivant les 12 facteurs.
- [[Dev/Services/Pydantic Settings|Pydantic Settings]] — Configuration typée chargée depuis l'environnement, les fichiers .env et les secrets, bâtie sur Pydantic.

## Liens

- Doc : https://hydra.cc/docs/intro/
