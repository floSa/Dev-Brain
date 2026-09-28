---
role: notion
nom: Model registry & versioning
alias: [model registry, registre de modèles, model versioning, versioning de modèles, lignage de modèle, model lineage, champion-challenger]
categorie: ml/tracking
domaines: [mlops]
tags: [model-registry, experiment-tracking]
---

# Model registry & versioning

## Aperçu

- Un **point de vérité unique** pour les modèles entraînés : chaque modèle y est versionné, daté, traçable jusqu'à son run d'entraînement, et promu par déplacement d'**alias** avant d'atteindre la production.
- Répond à trois questions : *quelle version tourne en prod ?*, *d'où vient-elle (données, code, params) ?*, *comment revenir en arrière ?*

## Concepts clés

### Versions & alias
- Chaque réentraînement crée une **version** immuable. Les versions se désignent par des **alias** mobiles (`champion`, `challenger`) déplacés d'une version à l'autre ; les **stades** `None` → `Staging` → `Production` → `Archived` de MLflow sont dépréciés depuis la 2.9.0 (la documentation annonce leur retrait dans une version majeure future) ; des **alias** et des **tags de version** (`validation_status: passed`, par exemple) les remplacent.
- La promotion est une **décision gouvernée** (validation, revue), pas un simple `git push`.

### Lignage (lineage)
- Relier la version de modèle à tout ce qui l'a produite : run d'entraînement, hyperparamètres, métriques, **version des données**, commit de code, image d'environnement.
- Sans lignage, un modèle en prod est une boîte noire non reproductible.

### Signature & model card
- **Signature** : schéma d'entrée/sortie attendu (types, formes) — contrat qui prévient le train/serve skew au chargement.
- **Model card** : métadonnées de gouvernance (usage prévu, limites, métriques par segment).

### Reproductibilité
- Pouvoir **recréer** une version à l'identique : mêmes données + même code + mêmes params → même modèle. C'est ce que le couple registre + suivi d'expériences garantit.

## En pratique

- Le registre est alimenté par le **suivi d'expériences** : on enregistre le meilleur run, on le promeut. [[MLflow]] couple les deux (Tracking + Model Registry).
- Promouvoir = déplacer l'alias (ou, dans l'ancien schéma, changer le stade), **pas** recopier des fichiers : les consommateurs (serving) chargent « la version `champion` » par référence stable.
- Versionner aussi les **données** et le code, sinon le lignage est troué (un modèle n'est reproductible que si ses entrées le sont).
- Brancher le déploiement sur le registre : le [[Déploiement de modèles|rollout]] consomme la version promue, le [[Monitoring de modèle en production|monitoring]] reporte sur cette version.

## Approches voisines & alternatives

- [[Déploiement de modèles]] — consomme la version promue par le registre.
- [[Monitoring de modèle en production]] — rattache les métriques de prod à une version précise du registre.
- [[Data drift]] — un drift mesuré déclenche un nouveau run → une nouvelle version enregistrée.
- [[MLflow]] — implémentation de référence (tracking + registre couplés).
- Voir aussi : [[DVC]], [[lakeFS]], [[Delta Lake]], [[CI-CD pour le ML]].

## Pour aller plus loin

- Versionnage de données complémentaire ([[DVC]], [[lakeFS]], [[Delta Lake]]) pour boucler le lignage.
- Documentation MLflow Model Registry — alias et tags de version, qui remplacent les stades dépréciés depuis la 2.9.0 : https://mlflow.org/docs/latest/ml/model-registry/workflow/
