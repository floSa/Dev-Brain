---
role: hub
nom: Suivi d'expériences
alias: [experiment tracking, tracking ML]
pitch: Enregistrer ce qui a produit quel modèle — paramètres, métriques, données, artefacts — pour pouvoir le comparer et le refaire.
domaines: [mlops, ml-eng]
tags: [experiment-tracking, model-registry, reproducibility, hyperparameter-tuning, ml-pipeline]
---

# Suivi d'expériences

> Enregistrer ce qui a produit quel modèle — paramètres, métriques, données, artefacts — pour pouvoir le comparer et le refaire.

## Ce qu'il faut comprendre

- **Ce dossier ne surveille pas la production, il surveille l'entraînement.** La confusion est fréquente et coûteuse : le tracking répond à « quel run a produit ce modèle, avec quels hyperparamètres, sur quelles données », alors que le monitoring répond à « ce modèle se dégrade-t-il depuis qu'il sert ». Le second est au niveau du domaine — [[Monitoring de modèle en production]], [[Data drift]], [[Evidently]]. L'observabilité d'une application LLM est encore un troisième métier, cf. [[LLM & IA générative]].
- **Ce n'est pas non plus l'orchestration.** Un tracker enregistre ; un orchestrateur exécute. Les deux se recouvrent parce que la plupart des plateformes font un peu des deux, mais le besoin qui déclenche l'adoption est différent — cf. [[Comparatif - Orchestrateurs ML]] au niveau du domaine.
- **Le vrai livrable n'est pas la courbe, c'est la reproductibilité.** Un run utile enregistre le code (commit), la donnée (version ou empreinte), l'environnement, les hyperparamètres, les métriques et l'artefact. S'il manque la version de la donnée, la comparaison entre deux runs ne prouve rien : c'est le manque le plus répandu, et le plus invisible.
- **Le registre est la moitié qui sert au-delà de l'équipe** : [[Model registry & versioning]] fait le lien entre un run et ce qui est effectivement servi par [[Serving]]. Sans lui, « quel modèle tourne en production » n'a pas de réponse fiable.
- **La recherche d'hyperparamètres produit des centaines de runs**, et c'est là que le tracking cesse d'être un confort : [[Optimisation d'hyperparamètres]], outillée au niveau du domaine par [[Optuna]] et [[Ray Tune]].
- **Le premier critère de choix est l'hébergement**, pas l'interface. Un contexte on-prem élimine d'emblée ce qui n'existe qu'en SaaS ; c'est un tri plus rapide et plus durable que la comparaison des tableaux de bord.
- Le second critère est le périmètre : un tracker seul reste léger et remplaçable ; une plateforme tout-en-un apporte pipelines et serving, et pèse d'autant plus lourd le jour où on veut en sortir.

## Choisir

- Un standard neutre, auto-hébergeable, avec registre de modèles → [[MLflow]] ; c'est le défaut raisonnable, surtout en on-prem.
- Le plus léger possible, en local ou sur un serveur, sans SaaS → [[Aim]].
- Une plateforme complète — tracking, données, pipelines, agents, serving → [[ClearML]].
- Des dashboards riches, des sweeps intégrés, un usage R&D deep learning → [[Weights & Biases]], en SaaS.
- Du tracking classique doublé d'observabilité LLM → [[Comet]] et son volet Opik.
- Regarder des courbes d'entraînement en local, sans rien installer de plus → [[TensorBoard]], qui se branche aussi sur PyTorch.
- [[Neptune]] n'est plus un choix pour du neuf : racheté par OpenAI, service hébergé arrêté en mars 2026. Cf. [[Comparatif - Suivi d'expériences ML]].

<!-- AUTO:START -->
### Briques
- [[Aim]] — Tracker d'expériences open-source léger et auto-hébergé — UI de comparaison rapide sur des centaines de milliers de runs, sans dépendance à un SaaS.
- [[ClearML]] — Plateforme MLOps open-source tout-en-un — tracking automatique sans code, plus gestion de données, pipelines, orchestration d'agents et serving.
- [[Comet]] — Plateforme SaaS de suivi d'expériences ML couplée à l'observabilité LLM (Opik, open-source) — du tracking classique au monitoring d'applications génératives.
- [[MLflow]] — Plateforme open-source de cycle de vie ML (Linux Foundation) — tracking d'expériences, registre de modèles, packaging et déploiement, agnostique au framework et au cloud.
- [[Neptune]] — Tracker d'expériences SaaS spécialisé entraînements longue durée et foundation models — racheté par OpenAI, service hébergé arrêté en mars 2026.
- [[TensorBoard]] — Boîte à outils de visualisation d'entraînement de TensorFlow — courbes de scalaires, histogrammes, graphe du modèle, images et projecteur d'embeddings depuis des event files locaux ; branché à PyTorch via torch.utils.tensorboard.
- [[Weights & Biases]] — Plateforme SaaS de suivi d'expériences et de visualisation — dashboards riches, sweeps d'hyperparamètres, artefacts et registre de modèles ; référence en R&D deep learning.

### Comparatifs
- [[Comparatif - Suivi d'expériences ML]]
<!-- AUTO:END -->

## Notes
