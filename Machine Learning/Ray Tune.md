---
role: brique
nom: Ray Tune
alias: [ray tune, ray.tune, raytune]
pitch: "Optimisation d'hyperparamètres distribuée sur Ray : schedulers à arrêt précoce (ASHA, PBT, HyperBand) et intégration des moteurs de recherche (Optuna, Hyperopt) à l'échelle du cluster."
categorie: ml/hyperopt
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Optuna]]", "[[Hyperopt]]"]
complements: []
tags: [hyperparameter-tuning, distributed, bayesian]
url_docs: https://docs.ray.io/en/latest/tune/
url_repo: https://github.com/ray-project/ray
---

# Ray Tune

<!-- AUTO:BANDEAU:START -->
> Optimisation d'hyperparamètres distribuée sur Ray : schedulers à arrêt précoce (ASHA, PBT, HyperBand) et intégration des moteurs de recherche (Optuna, Hyperopt) à l'échelle du cluster.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-08-23 |
<!-- AUTO:BANDEAU:END -->

## Définition

La bibliothèque d'**optimisation d'hyperparamètres** de l'écosystème [[Ray]], pensée pour le
distribué : elle lance des dizaines ou des centaines d'essais en parallèle sur un cluster et
les pilote par des **schedulers** qui arrêtent tôt les essais ratés (ASHA, HyperBand, Median)
ou réallouent les ressources en cours de route (Population Based Training). Elle
**n'implémente aucun algorithme de recherche** : elle enveloppe les moteurs existants —
[[Optuna]], [[Hyperopt]], BayesOpt, Nevergrad — et leur ajoute l'orchestration, la tolérance
aux pannes par checkpoints et l'intégration ML (PyTorch, Lightning, XGBoost, HuggingFace). Le
checkpointing est donc la pièce maîtresse : mal géré, il n'y a ni reprise ni PBT.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Campagne HPO **à grande échelle** sur un cluster CPU/GPU, au-delà de ce qu'une machine encaisse | Indissociable de [[Ray]] : on hérite de sa complexité — cluster, ressources, sérialisation |
| Schedulers avancés : ASHA et HyperBand pour couper le budget, PBT pour faire évoluer les configs en cours d'entraînement | Le **checkpointing** des trials conditionne la tolérance aux pannes et le PBT : mal géré, la reprise est perdue |
| Déjà sur [[Ray]] : régler dans le même runtime que l'entraînement distribué (Ray Train) | API Tune **remaniée au fil des versions** Ray : épingler la version, beaucoup de tutoriels anciens ne s'appliquent plus |
| Garder son moteur préféré — [[Optuna]] — mais l'exécuter en distribué avec tolérance aux pannes | Beaucoup de combinaisons scheduler × algorithme de recherche : trancher avant de se noyer dans les options |
| | Petit espace, quelques combinaisons : `GridSearchCV` / `RandomizedSearchCV` de [[Scikit-Learn]] |

## Mise en œuvre

- Installation — `uv add "ray[tune]"`
- Point d'entrée — API Python : une fonction d'entraînement rapportant sa métrique, un scheduler, un search algorithm enveloppé
- Prérequis — un cluster [[Ray]] et une stratégie de checkpoint des trials
- Exécution — self-hébergé : cluster Ray local ou multi-nœuds (Kubernetes via KubeRay, cloud, HPC) ; managé via Anyscale
- Coût — gratuit, Apache-2.0 ; le coût réel est l'infra mobilisée par les trials parallèles, et le réglage des schedulers commande l'économie de budget

## Écosystème

### Alternatives

- [[Optuna]] — Optimisation d'hyperparamètres define-by-run : recherche bayésienne (TPE, GP) et élagage des essais (Hyperband, median), parallélisable.
- [[Hyperopt]] — Optimisation d'hyperparamètres distribuée historique : recherche TPE (Parzen) sur espaces conditionnels, parallélisable via MongoDB/Spark ; mature mais peu maintenu.

## Ressources

- Documentation — https://docs.ray.io/en/latest/tune/
- Dépôt — https://github.com/ray-project/ray

## Voir aussi

- [[Optimisation d'hyperparamètres]] — la notion qu'il implémente
- [[Ray]] — le cœur distribué dont il dépend ; [[Ray Serve]] pour le serving de la même famille
- [[Comparatif - Optimisation d'hyperparamètres]] — ce qui départage les moteurs de réglage
