---
role: brique
nom: ClearML
alias: [clearml, Trains, Allegro Trains]
pitch: "Plateforme MLOps open-source tout-en-un — tracking automatique sans code, plus gestion de données, pipelines, orchestration d'agents et serving."
categorie: ml/tracking
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[MLflow]]", "[[Weights & Biases]]", "[[Neptune]]", "[[Comet]]", "[[Aim]]"]
complements: []
tags: [experiment-tracking, model-registry, orchestration]
url_docs: https://clear.ml/docs/
url_repo: https://github.com/clearml/clearml
---

# ClearML

<!-- AUTO:BANDEAU:START -->
> Plateforme MLOps open-source tout-en-un — tracking automatique sans code, plus gestion de données, pipelines, orchestration d'agents et serving.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Python | open-source | self-hébergé ou managé · distribué | production | à jour · 2026-08-19 |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme MLOps qui dépasse le suivi d'expériences : la capture des métriques, des
hyperparamètres et des modèles se fait **sans modifier le code**, par simple import, et s'y
ajoutent la gestion de données versionnées, les pipelines, l'orchestration par agents et files
d'attente sur un parc de GPU, et le serving. Serveur et SDK sont entièrement
auto-hébergeables, avec une offre managée en face. Le prix de cette étendue est un serveur à
plusieurs services — Elasticsearch, MongoDB, Redis. Ancien nom : *Trains*, chez Allegro AI.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Suite MLOps unifiée : tracking, données, pipelines, orchestration | Le serveur auto-hébergé embarque Elasticsearch, MongoDB et Redis : non trivial à opérer et à sauvegarder |
| Tracking sans effort : instrumentation automatique, sans réécrire le code | L'autocapture logge plus que prévu : cadrer ce qui part vers le serveur |
| Orchestrer des entraînements sur un parc de GPU, par agents et files d'attente | Besoin du seul tracking : la plateforme entière est alors une charge d'exploitation pour rien |
| Self-host complet, sans limite d'utilisateurs ni d'expériences | |

## Mise en œuvre

- Installation — `uv add clearml` ; serveur en Docker, AMI AWS ou Kubernetes
- Point d'entrée — SDK Python (capture par simple import), UI web, et agents `clearml-agent` sur les files d'attente
- Prérequis — pour le self-host, Elasticsearch, MongoDB et Redis en backend
- Exécution — auto-hébergé en architecture distribuée, ou managé
- Coût — gratuit et sans limite en self-host, Apache-2.0 ; offre managée avec palier gratuit et plans payants (RBAC avancé, support, sécurité)

## Écosystème

### Alternatives

- [[MLflow]] — Plateforme open-source de cycle de vie ML (Linux Foundation) — tracking d'expériences, registre de modèles, packaging et déploiement, agnostique au framework et au cloud.
- [[Weights & Biases]] — Plateforme SaaS de suivi d'expériences et de visualisation — dashboards riches, sweeps d'hyperparamètres, artefacts et registre de modèles ; référence en R&D deep learning.
- [[Neptune]] — Tracker d'expériences SaaS spécialisé entraînements longue durée et foundation models — racheté par OpenAI, service hébergé arrêté en mars 2026.
- [[Comet]] — Plateforme SaaS de suivi d'expériences ML couplée à l'observabilité LLM (Opik, open-source) — du tracking classique au monitoring d'applications génératives.
- [[Aim]] — Tracker d'expériences open-source léger et auto-hébergé — UI de comparaison rapide sur des centaines de milliers de runs, sans dépendance à un SaaS.

## Ressources

- Documentation — https://clear.ml/docs/
- Dépôt — https://github.com/clearml/clearml

## Voir aussi

- [[Suivi d'expériences]] — le hub du dossier
- [[PyTorch]] · [[Scikit-Learn]] · [[Optuna]] — les frameworks que sa capture automatique reconnaît
- [[Comparatif - Suivi d'expériences ML]] — ce qui départage les briques du dossier
