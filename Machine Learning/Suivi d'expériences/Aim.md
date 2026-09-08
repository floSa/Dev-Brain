---
role: brique
nom: Aim
alias: [aim, aimstack, AimHub]
pitch: "Tracker d'expériences open-source léger et auto-hébergé — UI de comparaison rapide sur des centaines de milliers de runs, sans dépendance à un SaaS."
categorie: ml/tracking
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[MLflow]]", "[[Weights & Biases]]", "[[Neptune]]", "[[Comet]]", "[[ClearML]]"]
complements: []
tags: [experiment-tracking]
url_docs: https://aimstack.readthedocs.io/
url_repo: https://github.com/aimhubio/aim
---

# Aim

<!-- AUTO:BANDEAU:START -->
> Tracker d'expériences open-source léger et auto-hébergé — UI de comparaison rapide sur des centaines de milliers de runs, sans dépendance à un SaaS.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Python | open-source | self-hébergé · mono-nœud | production | à jour · 2025-05-08 |
<!-- AUTO:BANDEAU:END -->

## Définition

Tracker d'expériences au positionnement léger et auto-hébergé : `aim.Run` journalise, une UI
web tient la comparaison de centaines de milliers d'exécutions — courbes, distributions,
médias — et un SDK de requêtes explore les métadonnées par programme. Rien ne part vers un
service tiers : les données restent sur l'infrastructure de l'équipe. Le projet se pense comme
socle de suivi au sens large, métriques ML mais aussi prompts et traces LLM. Il n'y a ni
registre de modèles ni RBAC — c'est le prix de la légèreté.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Tracker simple à lancer en local, sans compte ni service tiers | |
| Comparaison interactive de très nombreuses exécutions, avec une UI qui reste fluide | Ni registre de modèles ni RBAC : les fonctions d'entreprise manquent |
| Souveraineté des données : tout reste auto-hébergé | Packaging et déploiement de modèles ne sont pas dans le périmètre |
| Alternative légère quand le registre de modèles n'est pas requis | |

## Mise en œuvre

- Installation — `uv add aim` ; UI via `aim up`
- Point d'entrée — API Python `aim.Run`, UI web, et un SDK de requêtes sur les métadonnées
- Prérequis — un disque pour le dépôt de runs, où les exécutions vivent : sauvegarde et rétention sont à prévoir ; aucun service externe
- Exécution — serveur mono-nœud auto-hébergé : bare metal, AWS, GCP ou Kubernetes
- Coût — gratuit, Apache-2.0 ; aucun service central imposé

## Écosystème

### Alternatives

- [[MLflow]] — Plateforme open-source de cycle de vie ML (Linux Foundation) — tracking d'expériences, registre de modèles, packaging et déploiement, agnostique au framework et au cloud.
- [[Weights & Biases]] — Plateforme SaaS de suivi d'expériences et de visualisation — dashboards riches, sweeps d'hyperparamètres, artefacts et registre de modèles ; référence en R&D deep learning.
- [[Neptune]] — Tracker d'expériences SaaS spécialisé entraînements longue durée et foundation models — racheté par OpenAI, service hébergé arrêté en mars 2026.
- [[Comet]] — Plateforme SaaS de suivi d'expériences ML couplée à l'observabilité LLM (Opik, open-source) — du tracking classique au monitoring d'applications génératives.
- [[ClearML]] — Plateforme MLOps open-source tout-en-un — tracking automatique sans code, plus gestion de données, pipelines, orchestration d'agents et serving.

## Ressources

- Documentation — https://aimstack.readthedocs.io/
- Dépôt — https://github.com/aimhubio/aim

## Voir aussi

- [[Suivi d'expériences]] — le hub du dossier
- [[PyTorch]] · [[HuggingFace]] — les frameworks qu'il instrumente
- [[Comparatif - Suivi d'expériences ML]] — ce qui départage les briques du dossier
