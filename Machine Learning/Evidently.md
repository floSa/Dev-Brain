---
role: brique
nom: Evidently
alias: [evidently, evidently ai, evidentlyai]
pitch: "Framework open-source d'évaluation et de monitoring ML/LLM en Python — 100+ métriques pour détecter la dérive de données, mesurer qualité et performance et générer rapports et tableaux de bord, de l'expérimentation à la production."
categorie: ml/monitoring
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: ["[[MLflow]]"]
tags: [model-monitoring, data-drift, concept-drift, model-evaluation]
url_docs: https://docs.evidentlyai.com/
url_repo: https://github.com/evidentlyai/evidently
---

# Evidently

<!-- AUTO:BANDEAU:START -->
> Framework open-source d'évaluation et de monitoring ML/LLM en Python — 100+ métriques pour détecter la dérive de données, mesurer qualité et performance et générer rapports et tableaux de bord, de l'expérimentation à la production.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-03-10 |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework Python pour **évaluer et surveiller** les systèmes ML et LLM. On lui donne un jeu de
**référence** et un jeu **courant** ; il calcule plus de 100 métriques — dérive de données et
de prédictions, qualité des données, performance du modèle, métriques de classification et de
régression, évaluation LLM — et produit des rapports interactifs, des suites de **tests**
pass/fail intégrables en CI, et des tableaux de bord de suivi dans le temps. Tout repose donc
sur la fenêtre de référence choisie, et sur le contexte métier qui l'entoure : une dérive
saisonnière connue n'est pas un incident, mais rien dans l'outil ne le sait à votre place.
C'est l'outillage qui opérationnalise [[Data drift]] et
[[Monitoring de modèle en production]].

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Détecter la dérive — data drift, concept drift — entre entraînement et production : 20+ méthodes de test de distribution, PSI, KS, khi-deux | Le choix de la **fenêtre de référence** conditionne tout : une référence non représentative déclenche de fausses alertes, ou en masque de vraies |
| Monitorer un modèle en production : performance, qualité des données, dérive, suivi dans le temps avec alertes | Sur **gros volumes**, les tests statistiques (KS, khi-deux) sur-déclenchent — préférer PSI ou des seuils d'effet, ou sous-échantillonner |
| Tests de données et de modèle en **CI** : transformer des seuils métier en suites pass/fail rejouables | Observabilité d'**infrastructure** — latence, CPU, logs applicatifs : Evidently surveille le modèle, pas le système |
| Évaluer des applications **LLM** — qualité de réponses, RAG, tracing — dans le même cadre | Adaptation **en continu** à la dérive plutôt que détection batch → [[River]], et ses détecteurs ADWIN / Page-Hinkley |
| | Journaliser paramètres et métriques d'entraînement, versionner les modèles → [[MLflow]], complémentaire et non substituable |
| | API en évolution rapide, refondue autour de `Report` / `Dataset` : épingler la version et lire les notes de migration |

## Mise en œuvre

- Installation — `uv add evidently`
- Point d'entrée — API Python dans le pipeline (batch, Airflow) : jeu de référence contre jeu courant, puis `Report` ou suite de tests
- Prérequis — une fenêtre de référence représentative, et le contexte métier qui distingue dérive attendue et incident
- Exécution — la bibliothèque s'exécute dans le pipeline ; le service de monitoring (UI, stockage, dashboards) se déploie à côté, en conteneur
- Coût — gratuit en bibliothèque pure (Apache-2.0) ; Evidently Cloud, managé, est payant, tout comme le stockage des traces

## Écosystème

### Alternatives

- NannyML — estimation de performance sans labels et détection de drift (pas encore en fiche).
- WhyLabs / whylogs — profiling et monitoring de données à grande échelle (pas encore en fiche).

### Compléments

- [[MLflow]] — Plateforme open-source de cycle de vie ML (Linux Foundation) — tracking d'expériences, registre de modèles, packaging et déploiement, agnostique au framework et au cloud — où journaliser dérive et performance : la fiche l'énonce comme complémentaire, pas comme substitut.

## Ressources

- Documentation — https://docs.evidentlyai.com/
- Dépôt — https://github.com/evidentlyai/evidently

## Voir aussi

- [[Data drift]] — la dérive de données et de concept qu'Evidently détecte et quantifie
- [[Monitoring de modèle en production]] — le cadre opérationnel qu'il outille
- [[River]] — l'approche en ligne : adaptation continue plutôt que détection batch
