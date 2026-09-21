---
role: notion
nom: CI-CD pour le ML
alias: [CI/CD pour le ML, CI/CD ML, CD4ML, intégration continue ML, livraison continue ML, entraînement continu, continuous training]
categorie: ml/orchestration
domaines: [mlops]
tags: [ci-cd, ml-pipeline, deployment-strategy, reproducibility, model-registry]
---

# CI-CD pour le ML

## Aperçu

- Étendre la livraison continue du logiciel à ce qui change dans un système ML : **le code, les données et le modèle**. Un modèle se dégrade sans qu'une ligne de code ne bouge, donc un pipeline qui ne teste que le code laisse passer la panne la plus fréquente.
- Le sigle cache trois métiers : la **CI** teste code, composants, schémas de données et modèles ; la **CD** livre le système entier (pipeline et service), pas seulement un fichier de modèle ; le **CT** (*continuous training*) réentraîne automatiquement. Cette notion pose ce qui diffère, pas les mécanismes qui ont leur page.

## Concepts clés

### Ce qui diffère du CI/CD logiciel
- **Trois artefacts versionnés au lieu d'un.** Sato, Wider et Windheuser (Thoughtworks, 2019) définissent le CD4ML sur trois axes de changement, code, modèle et données, qui ont chacun leurs outils. Le modèle lui-même peut être non déterministe ; ce qui doit rester fiable et reproductible, c'est le processus de livraison.
- **L'entraînement est une compilation dont la source est le code plus les données.** Breck et al. (Google, 2017) en tirent la règle : les données se testent comme du code, et le modèle entraîné demande des pratiques de binaire — débogage, retour arrière, monitoring.
- **On livre un pipeline, pas un modèle.** Au niveau d'automatisation le plus élevé du guide de Google Cloud, ce qui part en production est un pipeline capable de réentraîner et de déployer.
- **CACE, « changer une chose change tout ».** Sculley et al. (NeurIPS 2015) : aucune entrée n'est indépendante, y compris les hyperparamètres, le seuil de convergence ou la sélection des données. Les seuils de décision posés à la main deviennent faux à la mise à jour du modèle.

### Trois niveaux d'automatisation (Google Cloud)
- **Niveau 0, tout manuel** : notebooks, déploiement rare, pas de CI, seul le modèle est livré, pas de monitoring actif.
- **Niveau 1, l'entraînement est un pipeline** : orchestré, conteneurisé, identique en préproduction et en production ; il ajoute la validation des données (schéma, dérive) avant l'entraînement, la validation du modèle après (contre un modèle de référence, par tranches), un feature store et un métastore.
- **Niveau 2, le pipeline est lui-même livré par CI/CD** : expérimentation, CI du pipeline, CD du pipeline, déclenchement automatique, CD du modèle, monitoring.

### Tester un modèle avant de le livrer
- **Le ML Test Score** (Breck et al., IEEE Big Data 2017) range 28 tests en quatre catégories de sept : données, développement du modèle, infrastructure ML, monitoring. Côté infrastructure : entraînement reproductible, qualité validée avant le service, canary avant le service, retour arrière possible.
- **Tester par tranches.** Une métrique globale masque une chute locale : les auteurs citent une précision qui gagne 1 % en moyenne tout en perdant 50 % pour un pays.
- **Tester des comportements, pas seulement une précision.** CheckList (Ribeiro et al., ACL 2020) propose trois familles : tests de capacité avec étiquettes, tests d'invariance (la sortie ne doit pas changer sous une perturbation) et tests directionnels (elle doit changer dans un sens attendu). Le papier vise le NLP ; l'idée d'invariance et de direction se transpose, pas les gabarits linguistiques.
- **Faire échouer le build.** Les suites pass/fail de [[Evidently]] et de [[Deepchecks]] transforment des seuils métier en conditions rejouables ; la documentation de Deepchecks fournit un pipeline GitHub Actions complet qui sort en erreur si la suite échoue.
- **Garder un humain là où la gouvernance l'exige.** CD4ML recommande des étapes manuelles pour le biais, l'équité et l'explicabilité ; Google donne l'exemple d'un déploiement automatique en test, semi-automatique en préproduction et manuel en production.

### Déployer progressivement
- Blue-green, canary, shadow et A/B sont posés dans [[Déploiement de modèles]] ; ce qui s'ajoute ici est leur place dans le pipeline. Breck et al. notent que le canary arrive souvent tard par rapport à la décision d'ingénierie fautive : mieux vaut détecter plus tôt, en test unitaire ou d'intégration.
- Deux réalisations documentées : [[KServe]] répartit le trafic entre la dernière révision saine et la nouvelle par `canaryTrafficPercent` (mode Knative/Serverless seulement dans la doc), et `0` épingle le trafic sur la révision précédente ; [[Seldon Core]] 2 a des *experiments* avec un modèle `mirror` qui reçoit une copie du trafic sans répondre à l'appelant, donc un shadow.

### Réentraîner : déclenché ou planifié
- Le guide de Google liste cinq déclencheurs : manuel, planifié, nouvelles données, dégradation de performance, dérive de distribution. Les deux derniers viennent de [[Monitoring de modèle en production]] et de [[Data drift]].
- **Une politique réactive n'est pas d'office la meilleure.** Une étude de 2026 (Dasari, préprint d'un seul auteur, non relu) mesure 3 933 exécutions sur flux avec dérive : sans apprentissage incrémental, le choix de politique pèse de 15 à 55 points de précision après la dérive, et le réentraînement périodique simple bat les deux politiques réactives testées en dérive abrupte ou graduelle. Avec apprentissage incrémental par échantillon, le choix ne change plus rien. Elle relève aussi qu'une interaction latence–budget divise silencieusement par deux le budget de réentraînement effectif.
- **Le coût compte.** Poenaru-Olaru et al. (2025) mesurent jusqu'à 25 % d'énergie en moins en réentraînant sur les seules données récentes, et jusqu'à 40 % avec un réentraînement déclenché par détection de changement — à condition que la détection soit fiable.
- **Les boucles de rétroaction.** Un modèle qui influence les données de son propre réentraînement crée des boucles difficiles à voir (Sculley et al.). Un CT entièrement automatique les aggrave ; les étiquettes qui arrivent en différé sont l'autre limite, et Breck et al. la reconnaissent sans la résoudre.

### Promouvoir par le registre, revenir en arrière
- **Promouvoir = déplacer un pointeur, pas recopier un fichier.** Dans [[MLflow]], un alias (`champion`) est une référence nommée et mutable vers une version ; les *stages* sont dépréciés depuis la 2.9.0. Pour les configurations mûres, la doc préfère un pipeline qui entraîne et enregistre le modèle dans chaque environnement plutôt qu'une copie de version. Détails dans [[Model registry & versioning]].
- **Le retour arrière** se déduit de ce mécanisme — réaffecter l'alias à la version précédente ; la doc MLflow ne le décrit pas explicitement. Azure ML découple le registre des espaces de travail et nomme les déploiements par version de modèle, ce qui permet un retour à un nom connu.

### Reproductibilité
- **Versionner les trois artefacts ensemble** : le code dans Git, les données et les modèles par [[DVC]] (qui stocke les fichiers ailleurs et garde leurs versions dans des commits Git), l'environnement d'exécution.
- **Elle n'est jamais totale.** PyTorch ne garantit pas de résultats identiques entre versions, commits ou plateformes, ni entre CPU et GPU ; fixer les graines et activer les algorithmes déterministes est plus lent. Breck et al. notent que même avec une graine fixée, l'ordre d'initialisation et des threads reste une source de non-déterminisme. Un retour arrière fiable passe donc par l'artefact stocké, pas par « réentraîner à l'identique ».

## Les maths, simplement

- **Le ML Test Score** : un test vaut 0,5 point s'il est exécuté à la main et documenté, 1 point s'il est automatisé ; on somme par catégorie, et le score final est le **minimum** des quatre catégories, pas leur moyenne. Un système est aussi prêt que sa catégorie la plus faible : sept tests d'infrastructure automatisés (7 points) ne rachètent pas une catégorie monitoring à zéro, le score reste 0.

## En pratique

- **Commencer par le niveau 1.** Un entraînement qui se rejoue d'une commande, des données versionnées et une suite de tests qui échoue avant tout déploiement valent plus qu'un CT déclenché par la dérive sur un pipeline non testé.
- **On-prem, sans cloud.** L'orchestration peut être [[Airflow]], [[Flyte]], [[ZenML]] ou [[Metaflow]] ; [[Kubeflow]] Pipelines n'a de sens que si un cluster est déjà opéré — cf. [[Du Compose à Kubernetes — quand changer d'échelle]] pour le seuil. La CI elle-même tourne sur des exécuteurs auto-hébergés ([[GitHub Actions]]).
- **Relier chaque modèle servi à son entraînement** : le registre porte la version, et le monitoring de production la relit pour déclencher ou geler un réentraînement.
- **Garder un retour arrière testé** : tant qu'il n'a pas été exécuté une fois, le ML Test Score le compte comme absent.

## Approches voisines & alternatives

- [[Déploiement de modèles]] — les stratégies de bascule (canary, shadow, blue-green) qui terminent le pipeline.
- [[Model registry & versioning]] — le pointeur de promotion et la traçabilité du modèle au run qui l'a produit.
- [[Monitoring de modèle en production]] — la source des déclencheurs de réentraînement et des critères de retour arrière.
- [[Evidently]] et [[Deepchecks]] — les suites de tests de données et de modèle que la CI exécute.
- [[Kubeflow]], [[Flyte]], [[ZenML]], [[Metaflow]] — les orchestrateurs du pipeline d'entraînement.
- [[DVC]] — la version des données et des modèles, avec Git.
- [[KServe]] et [[Seldon Core]] — les serveurs qui réalisent le canary et le shadow.

## Pour aller plus loin

- Google Cloud, « MLOps: Continuous delivery and automation pipelines in machine learning » — niveaux 0 à 2, CI, CD et CT : https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning
- Sato, Wider, Windheuser, « Continuous Delivery for Machine Learning » (2019) : https://martinfowler.com/articles/cd4ml.html
- Breck et al., « The ML Test Score » (IEEE Big Data 2017) : https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/
- Sculley et al., « Hidden Technical Debt in Machine Learning Systems » (NeurIPS 2015) : https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html
- Kreuzberger, Kühl, Hirschl, « Machine Learning Operations (MLOps): Overview, Definition, and Architecture » (2022), neuf principes et neuf composants issus de 27 articles, 11 outils et 8 entretiens : https://arxiv.org/abs/2205.02302
- Ribeiro et al., « Beyond Accuracy: Behavioral Testing of NLP Models with CheckList » (ACL 2020) : https://aclanthology.org/2020.acl-main.442/
- Dasari, « When to Retrain » (préprint, août 2026) : https://arxiv.org/abs/2608.19488 ; Poenaru-Olaru et al., « Sustainable Machine Learning Retraining » (2025) : https://arxiv.org/abs/2506.13838
- Documentation MLflow, registre de modèles : https://mlflow.org/docs/latest/ml/model-registry/
