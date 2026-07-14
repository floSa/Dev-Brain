---
galaxie: dev
type: service
nom: Aim
alias: [aim, aimstack, AimHub]
pitch: "Tracker d'expériences open-source léger et auto-hébergé — UI de comparaison rapide sur des centaines de milliers de runs, sans dépendance à un SaaS."
categorie: ml/tracking
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/MLflow|MLflow]]", "[[Dev/Services/Weights & Biases|Weights & Biases]]", "[[Dev/Services/Neptune|Neptune]]", "[[Dev/Services/Comet|Comet]]", "[[Dev/Services/ClearML|ClearML]]"]
remplace_par: []
status: actif
tags: [experiment-tracking]
url_docs: https://aimstack.readthedocs.io/
url_repo: https://github.com/aimhubio/aim
---

# Aim

## Pourquoi

Tracker d'expériences open-source (Apache-2.0) au positionnement **léger et auto-hébergé** : `aim.Run` pour logger, une **UI web rapide** pour comparer des centaines de milliers de runs (courbes, distributions, médias) et un **SDK de requêtes** pour explorer les métadonnées par programme. Pas de SaaS imposé, données sur sa propre infra. Pensé comme socle d'un écosystème de suivi (métriques ML mais aussi prompts / traces LLM).

## Quand l'utiliser

- Besoin d'un tracker **open-source, gratuit, simple à lancer en local**.
- Comparaison interactive de **très nombreux runs** avec une UI fluide.
- Souveraineté des données : tout reste auto-hébergé.
- Alternative légère à MLflow quand le registre de modèles n'est pas requis.

## Quand NE PAS l'utiliser

- Registre de modèles, packaging, déploiement → [[Dev/Services/MLflow|MLflow]].
- Suite MLOps complète (data, pipelines, orchestration) → [[Dev/Services/ClearML|ClearML]].
- Collaboration SaaS et dashboards très riches → [[Dev/Services/Weights & Biases|Weights & Biases]], [[Dev/Services/Comet|Comet]].

## Déploiement & coût

- Open-source (Apache-2.0), `uv add aim` ; UI via `aim up`. Single-node, stockage local.
- Auto-hébergeable partout (bare metal, AWS / GCP, Kubernetes).
- Gratuit ; l'usage de référence est self-host (pas de SaaS central imposé).

## Pièges

- Stockage des runs **local au serveur Aim** : prévoir sauvegarde et rétention.
- Moins de fonctions « entreprise » (RBAC, registre de modèles) que les plateformes SaaS.

## Alternatives

- [[Dev/Services/MLflow|MLflow]] — Plateforme open-source de cycle de vie ML (Linux Foundation) — tracking d'expériences, registre de modèles, packaging et déploiement, agnostique au framework et au cloud.
- [[Dev/Services/Weights & Biases|Weights & Biases]] — Plateforme SaaS de suivi d'expériences et de visualisation — dashboards riches, sweeps d'hyperparamètres, artefacts et registre de modèles ; référence en R&D deep learning.
- [[Dev/Services/Neptune|Neptune]] — Tracker d'expériences SaaS spécialisé entraînements longue durée et foundation models — racheté par OpenAI, service hébergé arrêté en mars 2026.
- [[Dev/Services/Comet|Comet]] — Plateforme SaaS de suivi d'expériences ML couplée à l'observabilité LLM (Opik, open-source) — du tracking classique au monitoring d'applications génératives.
- [[Dev/Services/ClearML|ClearML]] — Plateforme MLOps open-source tout-en-un — tracking automatique sans code, plus gestion de données, pipelines, orchestration d'agents et serving.

## Liens

- S'intègre avec : [[Dev/Services/PyTorch|PyTorch]], [[Dev/Services/HuggingFace|HuggingFace]].
- Doc : https://aimstack.readthedocs.io/
