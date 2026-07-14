---
galaxie: dev
type: service
nom: Comet
alias: [Comet ML, comet_ml, comet.com]
pitch: "Plateforme SaaS de suivi d'expériences ML couplée à l'observabilité LLM (Opik, open-source) — du tracking classique au monitoring d'applications génératives."
categorie: ml/tracking
licence_type: proprietary
hosted: both
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Dev/Services/MLflow|MLflow]]", "[[Dev/Services/Weights & Biases|Weights & Biases]]", "[[Dev/Services/Neptune|Neptune]]", "[[Dev/Services/ClearML|ClearML]]", "[[Dev/Services/Aim|Aim]]"]
remplace_par: []
status: actif
tags: [experiment-tracking, model-registry]
url_docs: https://www.comet.com/docs/
url_repo: 
---

# Comet

## Pourquoi

Plateforme commerciale couvrant tout le cycle ML : **suivi d'expériences** (paramètres, métriques, artefacts, comparaison de runs), **registre de modèles**, gestion de datasets et panneaux de visualisation personnalisables. Comet a étendu son offre vers l'**observabilité LLM** avec **Opik**, brique open-source de tracing et d'évaluation d'applications génératives (RAG, agents). Cœur de plateforme propriétaire, Opik ouvert et auto-hébergeable.

## Quand l'utiliser

- Suivi d'expériences ML **et** observabilité d'apps LLM dans un même écosystème.
- Besoin de dashboards personnalisables et de comparaisons de runs partagées.
- Self-host souhaité côté LLM : Opik se déploie en Docker / Kubernetes.

## Quand NE PAS l'utiliser

- Stack 100 % open-source pour le tracking ML classique → [[Dev/Services/MLflow|MLflow]], [[Dev/Services/ClearML|ClearML]].
- Visualisations deep learning de référence → [[Dev/Services/Weights & Biases|Weights & Biases]].
- Besoin minimal et local → [[Dev/Services/Aim|Aim]].

## Déploiement & coût

- SaaS managé (gratuit en perso/recherche, payant en équipe) ; déploiement on-prem possible.
- **Opik** (observabilité LLM) open-source, auto-hébergeable (Docker local, K8s à l'échelle).
- Plateforme cœur propriétaire ; tarification à l'usage / par sièges.

## Pièges

- Distinguer le **cœur Comet** (propriétaire) d'**Opik** (open-source) — périmètres et licences différents.
- Données envoyées au cloud par défaut en mode SaaS.

## Alternatives

- [[Dev/Services/MLflow|MLflow]] — Plateforme open-source de cycle de vie ML (Linux Foundation) — tracking d'expériences, registre de modèles, packaging et déploiement, agnostique au framework et au cloud.
- [[Dev/Services/Weights & Biases|Weights & Biases]] — Plateforme SaaS de suivi d'expériences et de visualisation — dashboards riches, sweeps d'hyperparamètres, artefacts et registre de modèles ; référence en R&D deep learning.
- [[Dev/Services/Neptune|Neptune]] — Tracker d'expériences SaaS spécialisé entraînements longue durée et foundation models — racheté par OpenAI, service hébergé arrêté en mars 2026.
- [[Dev/Services/ClearML|ClearML]] — Plateforme MLOps open-source tout-en-un — tracking automatique sans code, plus gestion de données, pipelines, orchestration d'agents et serving.
- [[Dev/Services/Aim|Aim]] — Tracker d'expériences open-source léger et auto-hébergé — UI de comparaison rapide sur des centaines de milliers de runs, sans dépendance à un SaaS.

## Liens

- Opik (observabilité LLM, open-source) : https://github.com/comet-ml/opik
- Doc : https://www.comet.com/docs/
