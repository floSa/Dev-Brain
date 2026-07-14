---
galaxie: wiki
type: concept
nom: Monitoring de modèle en production
alias: [model monitoring, monitoring ML, surveillance de modèle, observabilité ML, ML monitoring]
categorie: concept/ml
domaines: [mlops]
tags: [model-monitoring, data-drift, concept-drift]
---

# Monitoring de modèle en production

## Aperçu

- Un modèle déployé se dégrade **silencieusement** : il continue de répondre alors que le monde change. Le monitoring détecte cette dégradation avant qu'elle ne coûte cher.
- Distinct de l'observabilité d'infra (latence, CPU, erreurs 500) : ici on surveille la **qualité prédictive** et la **distribution des données**, pas seulement la santé du service.

## Concepts clés

### Les quatre couches à surveiller
- **Infra / service** : latence, débit, taux d'erreur, disponibilité (observabilité classique).
- **Données en entrée** : schéma, valeurs manquantes, plages, cardinalités — un pipeline cassé en amont est la panne la plus fréquente.
- **Dérive** : [[Data drift]] (entrées) et concept drift (relation entrée→cible) — la distribution s'écarte de l'entraînement.
- **Performance** : métriques métier et ML réelles, dès que les **labels** arrivent.

### Le problème des labels retardés
- La vérité terrain arrive souvent **en différé** (jours, semaines), voire jamais. Sans labels, la performance n'est pas mesurable directement.
- Parade : surveiller des **proxies** — drift des features, drift des **scores** de sortie, taux d'abstention — comme alertes précoces.

### Alerter sans crier au loup
- Distinguer un vrai incident d'une variation saisonnière connue. Seuils, fenêtres glissantes, et investigation avant action.
- Boucle de réaction : alerte → diagnostic → ré-entraînement ciblé ou [[Déploiement de modèles|rollback]].

## Les maths, simplement

- Quantifier la dérive : PSI, tests KS / khi-deux, divergences entre distributions ([[Data drift]] détaille). Sur gros volumes, ces tests sur-déclenchent → préférer une taille d'effet à une p-value.
- Performance dégradée : suivre la métrique de prod (AUC, F1, MAE…) sur fenêtre glissante et la comparer à la baseline d'entraînement — cf. [[Classification metrics]].

## En pratique

- Logger entrées, scores et version de modèle (du [[Model registry & versioning|registre]]) pour relier une dégradation à une version précise.
- Surveiller features **et** sorties : le drift des scores est mesurable immédiatement, sans attendre les labels.
- Tracer drift et performance dans le suivi d'expériences ([[Dev/Services/MLflow|MLflow]]).
- Outillage spécialisé : [[Dev/Services/Evidently|Evidently]] (en fiche), NannyML, WhyLabs, Arize.

## Approches voisines & alternatives

- [[Data drift]] — le signal central du monitoring ; ce concept en détaille la mesure.
- [[Déploiement de modèles]] — le monitoring fournit les métriques qui valident un canary / shadow.
- [[Model registry & versioning]] — rattache chaque métrique de prod à une version traçable.
- [[Calibration]] — la fiabilité des probabilités prédites se dégrade typiquement avec la dérive.
- [[Dev/Services/Evidently|Evidently]] — framework qui outille les quatre couches (données, drift, performance) avec rapports, tests et dashboards.
- [[Dev/Services/MLflow|MLflow]] — où journaliser drift et performance par version.

## Pour aller plus loin

- Documentation Evidently / NannyML — détection de drift et estimation de performance sans labels.
- Couche service (Prometheus, Grafana) pour l'`observability` d'infra, complémentaire du monitoring ML.
