---
galaxie: dev
type: service
nom: Ray Tune
alias: [ray tune, ray.tune, raytune]
pitch: "Optimisation d'hyperparamètres distribuée sur Ray : schedulers à arrêt précoce (ASHA, PBT, HyperBand) et intégration des moteurs de recherche (Optuna, Hyperopt) à l'échelle du cluster."
categorie: ml/hyperopt
licence_type: open-source
hosted: both
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Dev/Services/Optuna|Optuna]]", "[[Dev/Services/Hyperopt|Hyperopt]]"]
remplace_par: []
status: actif
tags: [hyperparameter-tuning, distributed, bayesian]
url_docs: https://docs.ray.io/en/latest/tune/
url_repo: https://github.com/ray-project/ray
---

# Ray Tune

## Pourquoi

Bibliothèque d'**optimisation d'hyperparamètres** de l'écosystème [[Dev/Services/Ray|Ray]], pensée pour le **distribué** : elle lance des dizaines/centaines d'essais (trials) en parallèle sur un cluster et les pilote par des **schedulers** qui arrêtent tôt les essais ratés (ASHA, HyperBand, Median) ou réallouent les ressources en cours de route (Population Based Training). Plutôt que de réimplémenter un algorithme de recherche, elle **enveloppe** les moteurs existants — [[Dev/Services/Optuna|Optuna]], [[Dev/Services/Hyperopt|Hyperopt]], BayesOpt, Nevergrad — et leur ajoute l'orchestration, la tolérance aux pannes (checkpoints) et l'intégration ML (PyTorch, Lightning, [[Dev/Services/XGBoost|XGBoost]], HuggingFace).

## Quand l'utiliser

- Campagne HPO **à grande échelle** sur un cluster CPU/GPU, au-delà de ce qu'une machine encaisse.
- Besoin de **schedulers avancés** : ASHA / HyperBand pour couper le budget, PBT pour faire évoluer les configs pendant l'entraînement.
- Déjà sur [[Dev/Services/Ray|Ray]] : régler dans le **même runtime** que l'entraînement distribué (Ray Train).
- Garder son moteur préféré ([[Dev/Services/Optuna|Optuna]]…) mais l'**exécuter en distribué** avec tolérance aux pannes.

## Quand NE PAS l'utiliser

- HPO sur une seule machine sans cluster → [[Dev/Services/Optuna|Optuna]] (define-by-run + pruning, plus léger à mettre en place).
- Petit espace, quelques combinaisons → `GridSearchCV` / `RandomizedSearchCV` de [[Dev/Services/Scikit-Learn|Scikit-Learn]].
- Pas d'infra Ray ni besoin de distribuer → ne pas porter la complexité d'un cluster pour rien.

## Déploiement & coût

- Open-source (Apache-2.0), `uv add "ray[tune]"`. S'exécute partout où Ray tourne.
- **Self-host** : cluster Ray local ou multi-nœuds (Kubernetes via KubeRay, cloud, HPC).
- **Managé** : Anyscale (payant) — clusters Ray opérés.
- Coût = l'infra du cluster mobilisée par les trials parallèles ; le réglage des schedulers conditionne l'économie de budget.

## Pièges

- Indissociable de [[Dev/Services/Ray|Ray]] : on hérite de sa complexité (cluster, ressources, sérialisation).
- Le **checkpointing** des trials est la clé de la tolérance aux pannes et de PBT : mal géré, on perd la reprise.
- Beaucoup de combinaisons (scheduler × search algorithm) : choisir avant de se noyer dans les options.
- API Tune remaniée au fil des versions Ray : épingler la version, beaucoup de tutoriels anciens ne s'appliquent plus.

## Alternatives

- [[Dev/Services/Optuna|Optuna]] — Optimisation d'hyperparamètres define-by-run : recherche bayésienne (TPE, GP) et élagage des essais (Hyperband, median), parallélisable.
- [[Dev/Services/Hyperopt|Hyperopt]] — Optimisation d'hyperparamètres distribuée historique : recherche TPE (Parzen) sur espaces conditionnels, parallélisable via MongoDB/Spark ; mature mais peu maintenu.

## Liens

- Concept implémenté : [[Optimisation d'hyperparamètres]]
- Famille Ray : [[Dev/Services/Ray|Ray]] (cœur distribué), [[Dev/Services/Ray Serve|Ray Serve]] (serving).
- [[Comparatif - Optimisation d'hyperparamètres]] — comparatif de la catégorie
- Enveloppe des moteurs de recherche : [[Dev/Services/Optuna|Optuna]], [[Dev/Services/Hyperopt|Hyperopt]].
- Doc : https://docs.ray.io/en/latest/tune/
