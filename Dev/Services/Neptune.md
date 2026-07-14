---
galaxie: dev
type: service
nom: Neptune
alias: [neptune.ai, neptune-client, Neptune Scale]
pitch: "Tracker d'expériences SaaS spécialisé entraînements longue durée et foundation models — racheté par OpenAI, service hébergé arrêté en mars 2026."
categorie: ml/tracking
licence_type: proprietary
hosted: both
maturite: deprecated
langage: Python
scaling: distributed
alternatives: ["[[Dev/Services/MLflow|MLflow]]", "[[Dev/Services/Weights & Biases|Weights & Biases]]", "[[Dev/Services/Comet|Comet]]", "[[Dev/Services/ClearML|ClearML]]", "[[Dev/Services/Aim|Aim]]"]
remplace_par: []
status: abandonne
tags: [experiment-tracking, model-registry]
url_docs: https://docs.neptune.ai/
url_repo: https://github.com/neptune-ai/neptune-client
---

# Neptune

## Pourquoi

Plateforme SaaS de suivi d'expériences réputée pour rester **fluide sur les entraînements longue durée** (millions de points loggés), avec comparaison de runs, *forking* depuis un checkpoint et lineage complet — d'où son positionnement sur les **foundation models**. En décembre 2025, **OpenAI a annoncé le rachat de Neptune** (~400 M$ en actions) ; le service hébergé a été **arrêté le 5 mars 2026** après une période de transition (export des données obligatoire). À considérer comme **déprécié** : ne pas démarrer de nouveau projet dessus.

## Quand l'utiliser

- En pratique : **plus de nouvel usage**. Le service hébergé est fermé depuis mars 2026.
- Cas résiduel : migration / export de données depuis une instance existante.

## Quand NE PAS l'utiliser

- Tout nouveau projet → [[Dev/Services/MLflow|MLflow]] (open-source) ou [[Dev/Services/Weights & Biases|Weights & Biases]] (SaaS) à la place.
- Besoin de pérennité : produit en fin de vie, absorbé par OpenAI.

## Déploiement & coût

- Historiquement : SaaS managé + déploiements on-prem / cloud privé (architecture HA, horizontalement scalable).
- Le SaaS public a été arrêté le **5 mars 2026** ; pas de transfert de données client vers OpenAI.
- Client `neptune` (open-source) encore sur PyPI/GitHub, mais sans backend hébergé.

## Pièges

- **Produit arrêté** : toute nouvelle dépendance est une dette immédiate.
- Données à exporter avant la fin de la transition sous peine de perte.
- Ne pas confondre `neptune` (v3 / Neptune Scale) et l'ancien `neptune-client` (API legacy).

## Alternatives

- [[Dev/Services/MLflow|MLflow]] — Plateforme open-source de cycle de vie ML (Linux Foundation) — tracking d'expériences, registre de modèles, packaging et déploiement, agnostique au framework et au cloud.
- [[Dev/Services/Weights & Biases|Weights & Biases]] — Plateforme SaaS de suivi d'expériences et de visualisation — dashboards riches, sweeps d'hyperparamètres, artefacts et registre de modèles ; référence en R&D deep learning.
- [[Dev/Services/Comet|Comet]] — Plateforme SaaS de suivi d'expériences ML couplée à l'observabilité LLM (Opik, open-source) — du tracking classique au monitoring d'applications génératives.
- [[Dev/Services/ClearML|ClearML]] — Plateforme MLOps open-source tout-en-un — tracking automatique sans code, plus gestion de données, pipelines, orchestration d'agents et serving.
- [[Dev/Services/Aim|Aim]] — Tracker d'expériences open-source léger et auto-hébergé — UI de comparaison rapide sur des centaines de milliers de runs, sans dépendance à un SaaS.

## Liens

- Annonce du rachat : https://openai.com/index/openai-to-acquire-neptune/
- Doc : https://docs.neptune.ai/
