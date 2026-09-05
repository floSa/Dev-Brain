---
role: brique
nom: hydra
alias: [Hydra, hydra-core]
pitch: "Framework de configuration hiérarchique composable (organisation communautaire Hydra Ecosystem, ex-Meta), bâti sur OmegaConf : compositions de configs, surcharge en ligne de commande et balayages multirun — pensé pour les expériences ML."
categorie: devtools/config
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[dynaconf]]", "[[python-dotenv]]", "[[Pydantic Settings]]"]
complements: []
tags: [config]
url_docs: https://hydra.cc/docs/intro/
url_repo: https://github.com/hydra-ecosystem/hydra
---

# hydra

<!-- AUTO:BANDEAU:START -->
> Framework de configuration hiérarchique composable (organisation communautaire Hydra Ecosystem, ex-Meta), bâti sur OmegaConf : compositions de configs, surcharge en ligne de commande et balayages multirun — pensé pour les expériences ML.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework de configuration composable, créé en 2019 par Omry Yadan chez Facebook AI
Research, passé le 13 août 2026 sous l'organisation communautaire **Hydra Ecosystem** —
dépôt migré avec son historique, ses issues et ses PR : ni fork, ni abandon, un simple
passage à une gouvernance indépendante. Sa marque : **composer**
dynamiquement une configuration hiérarchique à partir de groupes de fichiers, puis la
surcharger en ligne de commande. Bâti sur **OmegaConf** pour la fusion, les interpolations
et le typage structuré. Le mode `--multirun` rejoue la même tâche sur un balayage de
paramètres, et des launchers et sweepers s'y branchent — Joblib, Optuna, Ax, soumission à un
cluster. Hydra prend la main sur le répertoire de travail : un dossier de run par exécution.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Expériences ML où modèle, dataset et optimiseur varient par combinaisons de configs | Service web ayant besoin d'une configuration typée et validée → [[Pydantic Settings]] |
| Balayage d'hyperparamètres ou de configurations en une seule commande (`--multirun`) | Multi-environnements applicatifs — default, dev, prod — avec secrets et formats variés → [[dynaconf]] |
| Configuration profondément hiérarchique, surchargée depuis la CLI sans réécrire les fichiers | Charger quelques variables depuis un `.env` → [[python-dotenv]] |
| | Coût d'entrée réel : composition, liste `defaults` et interpolations OmegaConf demandent un temps d'appropriation, et le répertoire de travail détourné surprend en debug |

## Mise en œuvre

- Installation — `uv add hydra-core`
- Point d'entrée — décorateur `@hydra.main(...)` sur la fonction d'entrée, plus un arbre de groupes de configs
- Prérequis — Python et OmegaConf ; les launchers et sweepers (Joblib, Optuna, Ax, submitit) sont des plugins à installer
- Exécution — dans le process appelant ; `--multirun` peut déléguer à un launcher distribué, Hydra lui-même n'héberge rien
- Coût — gratuit sous licence MIT

## Écosystème

### Alternatives

- [[dynaconf]] — Gestion de configuration Python multi-format et multi-environnement : couches par environnement (default/dev/prod), surcharge par variables d'environnement et secrets.
- [[python-dotenv]] — Charge les paires clé-valeur d'un fichier `.env` dans les variables d'environnement, pour des applications suivant les 12 facteurs.
- [[Pydantic Settings]] — Configuration typée chargée depuis l'environnement, les fichiers .env et les secrets, bâtie sur Pydantic.

## Ressources

- Documentation — https://hydra.cc/docs/intro/
- Dépôt — https://github.com/hydra-ecosystem/hydra

## Voir aussi

- [[Outils de développement]] — le hub du domaine
