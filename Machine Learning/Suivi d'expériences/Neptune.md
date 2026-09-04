---
role: brique
nom: Neptune
alias: [neptune.ai, neptune-client, Neptune Scale]
pitch: "Tracker d'expériences SaaS spécialisé entraînements longue durée et foundation models — racheté par OpenAI, service hébergé arrêté en mars 2026."
categorie: ml/tracking
famille: plateforme
licence_type: proprietary
hosted: [self, managed]
maturite: deprecated
langage: Python
scaling: distributed
alternatives: ["[[MLflow]]", "[[Weights & Biases]]", "[[Comet]]", "[[ClearML]]", "[[Aim]]"]
complements: []
tags: [experiment-tracking, model-registry]
url_docs: https://docs.neptune.ai/
url_repo: https://github.com/neptune-ai/neptune-client
---

# Neptune

<!-- AUTO:BANDEAU:START -->
> Tracker d'expériences SaaS spécialisé entraînements longue durée et foundation models — racheté par OpenAI, service hébergé arrêté en mars 2026.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme Python | propriétaire | self-hébergé ou managé · distribué | deprecated |
<!-- AUTO:BANDEAU:END -->

## Définition

Tracker réputé pour rester fluide sur les entraînements de longue durée — millions de points
journalisés, comparaison d'exécutions, *forking* depuis un checkpoint, lignage complet —, d'où
son positionnement sur les foundation models. OpenAI en a annoncé le rachat en décembre 2025,
pour environ 400 M$ en actions, et le service hébergé a fermé le **5 mars 2026** au terme
d'une transition qui imposait l'export des données. Le client `neptune` reste publié sur PyPI,
mais il n'a plus de backend en face.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Cas résiduel : exporter ou migrer les données d'une instance existante | Service hébergé arrêté le 5 mars 2026 : toute nouvelle dépendance est une dette immédiate |
| | Produit en fin de vie, absorbé par OpenAI : plus aucune perspective d'évolution |
| | Données à exporter avant la fin de la transition, sous peine de perte |
| | Ne pas confondre `neptune` (v3, Neptune Scale) et l'ancien `neptune-client`, dont l'API diffère |

## Mise en œuvre

- Installation — `uv add neptune` ; le client reste publié, sans backend hébergé en face
- Point d'entrée — API Python ; l'UI hébergée n'existe plus
- Prérequis — historiquement, une instance managée ou un déploiement on-prem en haute disponibilité
- Exécution — service public arrêté le 5 mars 2026 ; aucun transfert des données client vers OpenAI
- Coût — sans objet : le service n'est plus commercialisé

## Écosystème

### Alternatives

- [[MLflow]] — Plateforme open-source de cycle de vie ML (Linux Foundation) — tracking d'expériences, registre de modèles, packaging et déploiement, agnostique au framework et au cloud.
- [[Weights & Biases]] — Plateforme SaaS de suivi d'expériences et de visualisation — dashboards riches, sweeps d'hyperparamètres, artefacts et registre de modèles ; référence en R&D deep learning.
- [[Comet]] — Plateforme SaaS de suivi d'expériences ML couplée à l'observabilité LLM (Opik, open-source) — du tracking classique au monitoring d'applications génératives.
- [[ClearML]] — Plateforme MLOps open-source tout-en-un — tracking automatique sans code, plus gestion de données, pipelines, orchestration d'agents et serving.
- [[Aim]] — Tracker d'expériences open-source léger et auto-hébergé — UI de comparaison rapide sur des centaines de milliers de runs, sans dépendance à un SaaS.

## Ressources

- Documentation — https://docs.neptune.ai/
- Dépôt — https://github.com/neptune-ai/neptune-client
- Article — https://openai.com/index/openai-to-acquire-neptune/

## Voir aussi

- [[Suivi d'expériences]] — le hub du dossier
- [[Comparatif - Suivi d'expériences ML]] — ce qui départage les briques du dossier
