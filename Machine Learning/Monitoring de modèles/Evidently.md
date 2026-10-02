---
role: brique
nom: Evidently
alias: [evidently, evidently ai, evidentlyai]
pitch: "Framework open-source d'évaluation et de monitoring ML/LLM en Python — 100+ métriques pour détecter la dérive de données, mesurer qualité et performance et générer rapports et tableaux de bord, de l'expérimentation à la production."
categorie: ml/monitoring
famille: paquet
licence_type: open-core
maturite: production
langage: Python
alternatives: ["[[NannyML]]", "[[Deepchecks]]"]
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
| Librairie Python | open-core | en bibliothèque, rien à héberger | production | amont non sondé |
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

**État au 2026-09-30.** Version 0.7.23 (GitHub 2026-09-10, PyPI 2026-09-11), 7 950 étoiles,
Apache-2.0, toujours 0.x. C'est le seul des trois outils du dossier encore maintenu
([[Comparatif - Monitoring de modèles]]), mais le rythme est irrégulier : aucune release entre
mars et septembre 2026.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Détecter la dérive — data drift, concept drift — entre entraînement et production : 20+ méthodes de test de distribution, PSI, KS, khi-deux | Le choix de la **fenêtre de référence** conditionne tout : une référence non représentative déclenche de fausses alertes, ou en masque de vraies |
| Monitorer un modèle en production : performance, qualité des données, dérive, suivi dans le temps sur le dashboard libre (les **alertes** sont réservées à l'édition commerciale) | Sur **gros volumes**, les tests statistiques (KS, khi-deux) sur-déclenchent — préférer PSI ou des seuils d'effet, ou sous-échantillonner ; les défauts actuels passent déjà à Wasserstein et Jensen-Shannon au-delà de 1000 observations de référence |
| Tests de données et de modèle en **CI** : transformer des seuils métier en suites pass/fail rejouables | Observabilité d'**infrastructure** — latence, CPU, logs applicatifs : Evidently surveille le modèle, pas le système |
| Évaluer des applications **LLM** — qualité de réponses, RAG, tracing — dans le même cadre | Adaptation **en continu** à la dérive plutôt que détection batch → [[River]], et ses détecteurs ADWIN / Page-Hinkley |
| | Journaliser paramètres et métriques d'entraînement, versionner les modèles → [[MLflow]], complémentaire et non substituable |
| | API **refondue** : la nouvelle (`Report`, `Dataset`, descriptors) est apparue en 0.6 (janvier 2025) et est devenue celle par défaut en 0.7.0 (avril 2025) avec rupture ; garder l'ancienne impose `<= 0.6.7`. Épingler la version et lire la page de migration |
| | Tâches planifiées, authentification, RBAC, alertes et no-code : **édition commerciale** (Enterprise auto-hébergé). Le support de l'édition libre passe par Discord |

## Mise en œuvre

- Installation — `uv add evidently`
- Point d'entrée — API Python dans le pipeline (batch, Airflow) : jeu de référence contre jeu courant, puis `Report` ou suite de tests
- Prérequis — une fenêtre de référence représentative, et le contexte métier qui distingue dérive attendue et incident
- Exécution — la bibliothèque s'exécute dans le pipeline ; le service de monitoring (UI, stockage, dashboards) se déploie à côté, en conteneur
- Coût — gratuit en bibliothèque et en service libre (Apache-2.0), tracing compris ; les fonctions d'exploitation ci-dessus sont payantes. La doc dit que Evidently Cloud n'est plus disponible en SaaS alors que le README du dépôt le promeut encore : les deux sources se contredisent, à revérifier avant tout engagement

## Écosystème

### Alternatives

- [[NannyML]] — Bibliothèque Python open source d'estimation de performance sans vérité terrain (CBPE, DLE) et de détection de dérive univariée et multivariée sur données tabulaires — édition libre figée depuis juillet 2025, fonctions avancées réservées à NannyML Cloud.
- [[Deepchecks]] — Bibliothèque Python de validation continue pour le ML — suites de checks sur données et modèles tabulaires, NLP et vision, avec conditions pass/fail rejouables en CI ; cœur AGPL-3.0, monitoring auto-hébergé limité à un modèle, évaluation de LLM et fonctions premium commerciales.
- voisin : whylogs — profiling de données par sketches, sans fiche : Apache-2.0 mais sans release depuis décembre 2024 et éditeur WhyLabs fermé (cf. [[Comparatif - Monitoring de modèles]]).

### Compléments

- [[MLflow]] — Plateforme open-source de cycle de vie ML (Linux Foundation) — tracking d'expériences, registre de modèles, packaging et déploiement, agnostique au framework et au cloud — où journaliser dérive et performance : la fiche l'énonce comme complémentaire, pas comme substitut. L'intégration n'est décrite que dans l'ancienne documentation (API `<= 0.6.7`), plus dans la documentation actuelle.

## Ressources

- Documentation — https://docs.evidentlyai.com/
- Dépôt — https://github.com/evidentlyai/evidently

## Voir aussi

- [[Data drift]] — la dérive de données et de concept qu'Evidently détecte et quantifie
- [[Monitoring de modèle en production]] — le cadre opérationnel qu'il outille
- [[River]] — l'approche en ligne : adaptation continue plutôt que détection batch
- [[Monitoring de modèles]] — le dossier de ce sous-domaine
- [[Comparatif - Monitoring de modèles]] — ce qui le départage de NannyML et de Deepchecks
- [[Grafana]] — des exemples du dépôt montent Evidently, PostgreSQL et Grafana en docker-compose ; Prometheus n'est documenté nulle part
- [[Airflow]] — cité par la documentation comme orchestrateur possible d'un job de monitoring batch
- [[Détection hors distribution (OOD)]] — la même question posée à l'entrée isolée plutôt qu'au flux : frontière avec la dérive de données
