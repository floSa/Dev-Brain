---
galaxie: wiki
type: concept
nom: Model registry & versioning
alias: [model registry, registre de modèles, model versioning, versioning de modèles, lignage de modèle, model lineage, champion-challenger]
categorie: concept/ml
domaines: [mlops]
tags: [model-registry, experiment-tracking]
---

# Model registry & versioning

## Aperçu

- Un **point de vérité unique** pour les modèles entraînés : chaque modèle y est versionné, daté, traçable jusqu'à son run d'entraînement, et promu par stades avant d'atteindre la production.
- Répond à trois questions : *quelle version tourne en prod ?*, *d'où vient-elle (données, code, params) ?*, *comment revenir en arrière ?*

## Concepts clés

### Versions & stades
- Chaque réentraînement crée une **version** immuable. Les versions transitent par des **stades** : `None` → `Staging` → `Production` → `Archived` (modèle MLflow historique), ou des **alias** mobiles modernes (`champion`, `challenger`) déplacés d'une version à l'autre.
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

- Le registre est alimenté par le **suivi d'expériences** : on enregistre le meilleur run, on le promeut. [[Dev/Services/MLflow|MLflow]] couple les deux (Tracking + Model Registry).
- Promouvoir = changer le stade / l'alias, **pas** recopier des fichiers : les consommateurs (serving) chargent « la version `Production` » par référence stable.
- Versionner aussi les **données** et le code, sinon le lignage est troué (un modèle n'est reproductible que si ses entrées le sont).
- Brancher le déploiement sur le registre : le [[Déploiement de modèles|rollout]] consomme la version promue, le [[Monitoring de modèle en production|monitoring]] reporte sur cette version.

## Approches voisines & alternatives

- [[Déploiement de modèles]] — consomme la version promue par le registre.
- [[Monitoring de modèle en production]] — rattache les métriques de prod à une version précise du registre.
- [[Data drift]] — un drift mesuré déclenche un nouveau run → une nouvelle version enregistrée.
- [[Dev/Services/MLflow|MLflow]] — implémentation de référence (tracking + registre couplés).

## Pour aller plus loin

- Versionnage de données complémentaire (DVC, lakeFS, Delta) pour boucler le lignage.
- Documentation MLflow Model Registry — stades, alias et webhooks de promotion.
