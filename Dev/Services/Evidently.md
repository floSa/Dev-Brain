---
galaxie: dev
type: service
nom: Evidently
alias: [evidently, evidently ai, evidentlyai]
pitch: "Framework open-source d'évaluation et de monitoring ML/LLM en Python — 100+ métriques pour détecter la dérive de données, mesurer qualité et performance et générer rapports et tableaux de bord, de l'expérimentation à la production."
categorie: ml/monitoring
licence_type: open-source
hosted: both
maturite: production
langage: Python
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [model-monitoring, data-drift, concept-drift, model-evaluation]
url_docs: https://docs.evidentlyai.com/
url_repo: https://github.com/evidentlyai/evidently
---

# Evidently

## Pourquoi

Framework Python open-source pour **évaluer et surveiller** les systèmes ML et LLM. On lui donne un jeu de **référence** et un jeu **courant** ; il calcule plus de 100 métriques (dérive de données et de prédictions, qualité des données, performance du modèle, métriques de classification/régression, et désormais évaluation LLM) et produit des **rapports** interactifs, des suites de **tests** (assertions pass/fail intégrables en CI) et des **tableaux de bord** de suivi dans le temps. La même bibliothèque va du diagnostic ponctuel en notebook au monitoring continu via un service self-hostable ou Evidently Cloud. C'est l'outillage qui opérationnalise les concepts de [[Data drift]] et de [[Monitoring de modèle en production]].

## Quand l'utiliser

- **Détecter la dérive** (data drift, concept drift) entre entraînement et production : 20+ méthodes de test de distribution, PSI, KS, khi-deux.
- **Monitorer un modèle en production** : performance, qualité des données, dérive, suivis dans le temps avec alertes.
- **Tests de données/modèle en CI** : transformer des seuils métier en suites pass/fail rejouables.
- Évaluer des **applications LLM** (qualité de réponses, RAG, tracing) avec le même cadre.

## Quand NE PAS l'utiliser

- Besoin d'**observabilité d'infrastructure** (latence, CPU, logs applicatifs) → stack Prometheus/Grafana ; Evidently surveille le modèle, pas le système.
- Adaptation **en continu** à la dérive plutôt que détection batch → [[Dev/Services/River|River]] (apprentissage en ligne, détecteurs ADWIN/Page-Hinkley).
- Journaliser paramètres/métriques d'entraînement et versionner les modèles → [[Dev/Services/MLflow|MLflow]] (tracking/registry), complémentaire d'Evidently.

## Déploiement & coût

- Bibliothèque open-source (Apache-2.0), gratuite ; `uv add evidently`. Modèle **hybride** : cœur d'évaluation open-source + service self-hostable + **Evidently Cloud** (managé, payant).
- Self-host : la lib s'exécute dans le pipeline (batch, Airflow…) ; le service de monitoring (UI, stockage, dashboards) se déploie en conteneur.
- Coût = gratuit en lib pure ; offre cloud facturée si l'on veut le suivi managé et le stockage des traces.

## Pièges

- Le choix de la **fenêtre de référence** conditionne tout : une référence non représentative déclenche de fausses alertes (ou en masque de vraies).
- Sur **gros volumes**, les tests statistiques (KS, khi-deux) sur-déclenchent — préférer PSI/seuils d'effet ou sous-échantillonner.
- Dérive **saisonnière connue** ≠ incident : sans contexte métier, l'alerte induit en erreur.
- API en évolution rapide (refonte autour de `Report`/`Dataset` récente) : épingler la version et lire les notes de migration.

## Alternatives

- NannyML — estimation de performance sans labels et détection de drift (pas encore en fiche).
- WhyLabs / whylogs — profiling et monitoring de données à grande échelle (pas encore en fiche).

## Liens

- [[Data drift]] — dérive de données/concept qu'Evidently détecte et quantifie.
- [[Monitoring de modèle en production]] — cadre opérationnel qu'il outille.
- [[Dev/Services/MLflow|MLflow]] — tracking/registry où journaliser drift et performance ; complémentaire.
- [[Dev/Services/River|River]] — approche en ligne, adaptation continue plutôt que détection batch.
- Doc : https://docs.evidentlyai.com/
