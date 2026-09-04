---
role: brique
nom: Comet
alias: [Comet ML, comet_ml, comet.com]
pitch: "Plateforme SaaS de suivi d'expériences ML couplée à l'observabilité LLM (Opik, open-source) — du tracking classique au monitoring d'applications génératives."
categorie: ml/tracking
famille: plateforme
licence_type: proprietary
hosted: [self, managed]
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[MLflow]]", "[[Weights & Biases]]", "[[Neptune]]", "[[ClearML]]", "[[Aim]]"]
complements: []
tags: [experiment-tracking, model-registry]
url_docs: https://www.comet.com/docs/
url_repo: 
---

# Comet

<!-- AUTO:BANDEAU:START -->
> Plateforme SaaS de suivi d'expériences ML couplée à l'observabilité LLM (Opik, open-source) — du tracking classique au monitoring d'applications génératives.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme Python | propriétaire | self-hébergé ou managé · distribué | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme commerciale couvrant le cycle ML : suivi d'expériences — paramètres, métriques,
artefacts, comparaison d'exécutions —, registre de modèles, gestion de jeux de données et
panneaux de visualisation personnalisables. Son extension vers l'observabilité des
applications génératives passe par **Opik**, brique de tracing et d'évaluation de RAG et
d'agents, déployable en Docker ou Kubernetes. Le périmètre est à lire avec soin : le cœur
Comet est fermé, Opik seul est ouvert.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Suivi ML et observabilité d'applications LLM dans un même écosystème | Deux périmètres et deux licences : le cœur Comet est propriétaire, seul Opik est ouvert |
| Panneaux personnalisables et comparaisons d'exécutions partagées | En mode hébergé, les données partent au cloud par défaut |
| Self-host côté LLM : Opik se déploie en Docker ou en Kubernetes | Tarification à l'usage ou par siège dès qu'on quitte le palier gratuit |

## Mise en œuvre

- Installation — `uv add comet_ml` ; Opik séparément, en Docker local ou en Kubernetes
- Point d'entrée — SDK Python et UI web ; Opik pour le tracing des applications LLM
- Prérequis — un compte côté éditeur pour le service hébergé ; un cluster pour Opik à l'échelle
- Exécution — service managé, ou déploiement on-prem
- Coût — gratuit en usage personnel et recherche, payant en équipe, à l'usage ou par siège

## Écosystème

### Alternatives

- [[MLflow]] — Plateforme open-source de cycle de vie ML (Linux Foundation) — tracking d'expériences, registre de modèles, packaging et déploiement, agnostique au framework et au cloud.
- [[Weights & Biases]] — Plateforme SaaS de suivi d'expériences et de visualisation — dashboards riches, sweeps d'hyperparamètres, artefacts et registre de modèles ; référence en R&D deep learning.
- [[Neptune]] — Tracker d'expériences SaaS spécialisé entraînements longue durée et foundation models — racheté par OpenAI, service hébergé arrêté en mars 2026.
- [[ClearML]] — Plateforme MLOps open-source tout-en-un — tracking automatique sans code, plus gestion de données, pipelines, orchestration d'agents et serving.
- [[Aim]] — Tracker d'expériences open-source léger et auto-hébergé — UI de comparaison rapide sur des centaines de milliers de runs, sans dépendance à un SaaS.

## Ressources

- Documentation — https://www.comet.com/docs/
- Dépôt — https://github.com/comet-ml/opik

## Voir aussi

- [[Suivi d'expériences]] — le hub du dossier
- [[Comparatif - Suivi d'expériences ML]] — ce qui départage les briques du dossier
