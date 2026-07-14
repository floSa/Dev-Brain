---
galaxie: dev
type: service
nom: ClearML
alias: [clearml, Trains, Allegro Trains]
pitch: "Plateforme MLOps open-source tout-en-un — tracking automatique sans code, plus gestion de données, pipelines, orchestration d'agents et serving."
categorie: ml/tracking
licence_type: open-source
hosted: both
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Dev/Services/MLflow|MLflow]]", "[[Dev/Services/Weights & Biases|Weights & Biases]]", "[[Dev/Services/Neptune|Neptune]]", "[[Dev/Services/Comet|Comet]]", "[[Dev/Services/Aim|Aim]]"]
remplace_par: []
status: actif
tags: [experiment-tracking, model-registry, orchestration]
url_docs: https://clear.ml/docs/
url_repo: https://github.com/clearml/clearml
---

# ClearML

## Pourquoi

Plateforme MLOps open-source qui va bien au-delà du tracking : **suivi d'expériences automatique** (capture métriques, hyperparamètres et modèles **sans modifier le code**, par simple import), **gestion de données** versionnées, **pipelines**, **orchestration** via agents (files d'attente, scheduling) et **serving**. Serveur et SDK sous Apache-2.0, entièrement auto-hébergeables ; offre managée disponible. Ancien nom : *Trains* (Allegro AI).

## Quand l'utiliser

- Besoin d'une **suite MLOps unifiée** open-source (tracking + data + pipelines + orchestration).
- Tracking « zéro effort » : instrumentation automatique sans réécrire le code.
- Orchestration d'entraînements sur un parc de GPU via agents / queues.
- Self-host complet sans limite d'utilisateurs ni d'expériences.

## Quand NE PAS l'utiliser

- Besoin uniquement de tracking, sans la lourdeur d'une plateforme → [[Dev/Services/MLflow|MLflow]], [[Dev/Services/Aim|Aim]].
- Visualisations DL haut de gamme + collaboration SaaS → [[Dev/Services/Weights & Biases|Weights & Biases]].

## Déploiement & coût

- Open-source (Apache-2.0) : ClearML Server auto-hébergé (Docker, AWS AMI, Kubernetes), gratuit sans limite.
- Offre managée (free tier + plans payants : RBAC avancé, support, sécurité entreprise).
- Architecture distribuée (Elasticsearch / MongoDB / Redis en backend) — prévoir les ressources.

## Pièges

- Le serveur self-host embarque plusieurs services (ES, Mongo, Redis) : non trivial à opérer et à sauvegarder.
- L'autocapture peut logger plus que prévu : cadrer ce qui part vers le serveur.

## Alternatives

- [[Dev/Services/MLflow|MLflow]] — Plateforme open-source de cycle de vie ML (Linux Foundation) — tracking d'expériences, registre de modèles, packaging et déploiement, agnostique au framework et au cloud.
- [[Dev/Services/Weights & Biases|Weights & Biases]] — Plateforme SaaS de suivi d'expériences et de visualisation — dashboards riches, sweeps d'hyperparamètres, artefacts et registre de modèles ; référence en R&D deep learning.
- [[Dev/Services/Neptune|Neptune]] — Tracker d'expériences SaaS spécialisé entraînements longue durée et foundation models — racheté par OpenAI, service hébergé arrêté en mars 2026.
- [[Dev/Services/Comet|Comet]] — Plateforme SaaS de suivi d'expériences ML couplée à l'observabilité LLM (Opik, open-source) — du tracking classique au monitoring d'applications génératives.
- [[Dev/Services/Aim|Aim]] — Tracker d'expériences open-source léger et auto-hébergé — UI de comparaison rapide sur des centaines de milliers de runs, sans dépendance à un SaaS.

## Liens

- S'intègre avec : [[Dev/Services/PyTorch|PyTorch]], [[Dev/Services/Scikit-Learn|Scikit-Learn]], [[Dev/Services/Optuna|Optuna]].
- Doc : https://clear.ml/docs/
