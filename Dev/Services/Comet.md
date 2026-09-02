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

## Pourquoi

Plateforme commerciale couvrant tout le cycle ML : **suivi d'expériences** (paramètres, métriques, artefacts, comparaison de runs), **registre de modèles**, gestion de datasets et panneaux de visualisation personnalisables. Comet a étendu son offre vers l'**observabilité LLM** avec **Opik**, brique open-source de tracing et d'évaluation d'applications génératives (RAG, agents). Cœur de plateforme propriétaire, Opik ouvert et auto-hébergeable.

## Quand l'utiliser

- Suivi d'expériences ML **et** observabilité d'apps LLM dans un même écosystème.
- Besoin de dashboards personnalisables et de comparaisons de runs partagées.
- Self-host souhaité côté LLM : Opik se déploie en Docker / Kubernetes.

## Quand NE PAS l'utiliser

- Stack 100 % open-source pour le tracking ML classique → [[MLflow]], [[ClearML]].
- Visualisations deep learning de référence → [[Weights & Biases]].
- Besoin minimal et local → [[Aim]].

## Déploiement & coût

- SaaS managé (gratuit en perso/recherche, payant en équipe) ; déploiement on-prem possible.
- **Opik** (observabilité LLM) open-source, auto-hébergeable (Docker local, K8s à l'échelle).
- Plateforme cœur propriétaire ; tarification à l'usage / par sièges.

## Pièges

- Distinguer le **cœur Comet** (propriétaire) d'**Opik** (open-source) — périmètres et licences différents.
- Données envoyées au cloud par défaut en mode SaaS.

## Alternatives

- [[MLflow]] — Plateforme open-source de cycle de vie ML (Linux Foundation) — tracking d'expériences, registre de modèles, packaging et déploiement, agnostique au framework et au cloud.
- [[Weights & Biases]] — Plateforme SaaS de suivi d'expériences et de visualisation — dashboards riches, sweeps d'hyperparamètres, artefacts et registre de modèles ; référence en R&D deep learning.
- [[Neptune]] — Tracker d'expériences SaaS spécialisé entraînements longue durée et foundation models — racheté par OpenAI, service hébergé arrêté en mars 2026.
- [[ClearML]] — Plateforme MLOps open-source tout-en-un — tracking automatique sans code, plus gestion de données, pipelines, orchestration d'agents et serving.
- [[Aim]] — Tracker d'expériences open-source léger et auto-hébergé — UI de comparaison rapide sur des centaines de milliers de runs, sans dépendance à un SaaS.

## Liens

- Opik (observabilité LLM, open-source) : https://github.com/comet-ml/opik
- Doc : https://www.comet.com/docs/
