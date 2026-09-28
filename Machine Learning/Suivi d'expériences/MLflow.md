---
role: brique
nom: MLflow
alias: [mlflow]
pitch: "Plateforme open-source de cycle de vie ML (Linux Foundation) — tracking d'expériences, registre de modèles, packaging et déploiement, agnostique au framework et au cloud."
categorie: ml/tracking
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Weights & Biases]]", "[[Neptune]]", "[[Comet]]", "[[ClearML]]", "[[Aim]]", "[[TensorBoard]]"]
complements: ["[[Evidently]]", "[[Databricks]]", "[[lakeFS]]", "[[DVC]]"]
tags: [experiment-tracking, model-registry]
url_docs: https://mlflow.org/docs/latest/
url_repo: https://github.com/mlflow/mlflow
---

# MLflow

<!-- AUTO:BANDEAU:START -->
> Plateforme open-source de cycle de vie ML (Linux Foundation) — tracking d'expériences, registre de modèles, packaging et déploiement, agnostique au framework et au cloud.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Python | open-source | self-hébergé ou managé · mono-nœud | production | à jour · 2026-09-07 |
<!-- AUTO:BANDEAU:END -->

## Définition

Standard du cycle de vie ML hébergé par la Linux Foundation, en quatre briques modulaires :
*Tracking* journalise paramètres, métriques, artefacts et code de chaque exécution ; *Model
Registry* versionne les modèles et les promeut par **alias** et tags de version (les **stades** Staging / Production / Archived sont dépréciés depuis la 2.9.0) ; *Projects*
empaquette une exécution reproductible ; *Models* définit un format d'échange déployable sur
plusieurs cibles. L'ensemble est agnostique au framework comme au cloud, et l'*autologging*
capture l'essentiel sans instrumenter le code. C'est le seul du dossier à porter un registre
de modèles ouvert.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Tracking auto-hébergeable et gratuit, sans dépendance à un service tiers | Le serveur de tracking par défaut n'a aucune authentification : à placer derrière un reverse-proxy ou un SSO |
| Registre de modèles ouvert, pour gérer alias, tags et promotions (les stades sont dépréciés depuis la 2.9.0, à ne pas adopter pour un nouveau registre) | Le `mlruns/` sur disque grossit vite : viser tôt un backend SQL et un stockage objet |
| Stack hétérogène : un seul format de modèle pour servir partout | L'autologging ne capture pas la même chose selon le framework : vérifier ce qui part réellement |
| Déjà sur Databricks : Managed MLflow intégré (auth, Unity Catalog), rien à opérer | Serveur de tracking mono-nœud : ce n'est pas une plateforme d'orchestration |

## Mise en œuvre

- Installation — `uv add mlflow` ; en local, `mlflow ui` suffit sur des fichiers
- Point d'entrée — API Python (`mlflow.log_*`, `autolog`), CLI et UI web ; serveur de tracking dès qu'on est plusieurs
- Prérequis — en équipe, une base SQL (Postgres) pour les métadonnées et un stockage d'artefacts (S3, [[MinIO]] — projet archivé, voir sa fiche ; [[SeaweedFS]], [[Garage]] ou [[Ceph]] comme alternatives)
- Exécution — serveur mono-nœud auto-hébergé, ou managé chez Databricks
- Coût — gratuit, Apache-2.0 ; Managed MLflow (Databricks) payant, intégré à la plateforme

## Écosystème

### Alternatives

- [[Weights & Biases]] — Plateforme SaaS de suivi d'expériences et de visualisation — dashboards riches, sweeps d'hyperparamètres, artefacts et registre de modèles ; référence en R&D deep learning.
- [[Neptune]] — Tracker d'expériences SaaS spécialisé entraînements longue durée et foundation models — racheté par OpenAI, service hébergé arrêté en mars 2026.
- [[Comet]] — Plateforme SaaS de suivi d'expériences ML couplée à l'observabilité LLM (Opik, open-source) — du tracking classique au monitoring d'applications génératives.
- [[ClearML]] — Plateforme MLOps open-source tout-en-un — tracking automatique sans code, plus gestion de données, pipelines, orchestration d'agents et serving.
- [[Aim]] — Tracker d'expériences open-source léger et auto-hébergé — UI de comparaison rapide sur des centaines de milliers de runs, sans dépendance à un SaaS.
- [[TensorBoard]] — Boîte à outils de visualisation d'entraînement de TensorFlow — courbes de scalaires, histogrammes, graphe du modèle, images et projecteur d'embeddings depuis des event files locaux ; branché à PyTorch via torch.utils.tensorboard.

### Compléments

- [[Evidently]] — Framework open-source d'évaluation et de monitoring ML/LLM en Python — 100+ métriques pour détecter la dérive de données, mesurer qualité et performance et générer rapports et tableaux de bord, de l'expérimentation à la production. — le versant dérive et qualité des données, en aval du run suivi
- [[Databricks]] — Plateforme lakehouse bâtie sur Spark et Delta Lake, managée sur AWS, Azure ou GCP : data engineering, SQL analytique et ML dans un même espace, gouvernés par Unity Catalog ; très technique, et sans auto-hébergement. — la plateforme dont il est né, et qui en propose une édition managée intégrée à l'authentification et au catalogue.
- [[lakeFS]] — Versionnage d'un dépôt d'objets à la manière de Git — branches, commits, merges atomiques, retour en arrière, hooks — au-dessus d'un stockage S3-compatible, sans copier les données ; serveur Go avec PostgreSQL, sous licence BSL 1.1 depuis la v1.87.0 (usage interne non modifié), édition libre limitée à un utilisateur. — intégration officielle de lakeFS : le run journalise un jeu de données dont la source est `s3://dépôt/<commit>/…`, avec une branche par expérience.
- [[DVC]] — Versionnage de données et de modèles en ligne de commande, posé sur Git : des pointeurs `.dvc` dans le dépôt, le contenu dans un cache adressé par le hash et des remotes (S3 compatible, SSH, NAS), plus des pipelines reproductibles par `dvc repro` ; Apache-2.0, projet racheté par lakeFS en novembre 2025. — aucune intégration native : l'identifiant du commit Git ou DVC se journalise comme paramètre du run, et un article d'AWS de 2026 en donne la recette.

## Ressources

- Documentation — https://mlflow.org/docs/latest/
- Documentation — dépréciation des stades de modèles, au profit des alias et des tags de version (depuis la 2.9.0) : https://mlflow.org/docs/latest/ml/model-registry/workflow/
- Dépôt — https://github.com/mlflow/mlflow

## Voir aussi

- [[Model registry & versioning]] — la notion du dossier qu'il implémente : alias, tags de version, lignage (les stades sont dépréciés depuis la 2.9.0)
- [[Déploiement de modèles]] — l'étape aval que son format de modèle sert
- [[Monitoring de modèle en production]] — ce qui prend le relais une fois le modèle servi
- [[PyTorch]] · [[Scikit-Learn]] · [[XGBoost]] · [[Optuna]] — les frameworks que son autologging reconnaît
- [[Comparatif - Suivi d'expériences ML]] — ce qui départage les briques du dossier
