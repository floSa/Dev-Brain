---
role: hub
nom: Monitoring de modèles
alias: []
pitch: Savoir qu'un modèle déployé se dégrade avant que ses utilisateurs ne le disent — dérive, performance sans étiquettes, tests avant mise en production.
domaines: [mlops, data-sci]
tags: [model-monitoring, data-drift, concept-drift, model-evaluation]
---

# Monitoring de modèles

> Savoir qu'un modèle déployé se dégrade avant que ses utilisateurs ne le disent — dérive, performance sans étiquettes, tests avant mise en production.

## Ce qu'il faut comprendre

- **Un modèle déployé ne tombe pas en panne, il se dégrade.** L'endpoint répond, les codes HTTP sont verts, et les prédictions dérivent depuis trois semaines. [[Monitoring de modèle en production]] pose les quatre couches à surveiller ; [[Data drift]] détaille la mesure. Ce dossier en tient l'outillage.
- **Le premier arbitrage est la vérité terrain.** Si les étiquettes arrivent vite, la performance se mesure ; si elles arrivent en différé ou jamais, il faut soit l'estimer ([[NannyML]]), soit surveiller des proxies — dérive des features et des scores ([[Evidently]]).
- **Le second est le moment du contrôle.** Avant le déploiement, des tests pass/fail qui font échouer un build ([[Deepchecks]], et les suites de tests d'[[Evidently]]) ; après, des rapports et des tableaux de bord sur des fenêtres glissantes. Les tests et les déclencheurs de réentraînement s'insèrent dans le pipeline décrit par [[CI-CD pour le ML]].
- **Ce dossier n'est pas l'observabilité d'infrastructure.** Latence, CPU, erreurs 500 : [[Prometheus]] et [[Grafana]], au niveau du domaine Observabilité. Le monitoring de modèle surveille la qualité prédictive, pas la santé du service.
- **La maintenance est le vrai critère d'exclusion.** Au 2026-09-30, [[Evidently]] est le seul outil fiché encore maintenu. [[NannyML]] (Apache-2.0) et [[Deepchecks]] (AGPL-3.0) sont dormants depuis 2025 et leurs éditeurs ont été rachetés. Les autres candidats ont été écartés : Alibi Detect (BSL 1.1, production payante), whylogs (abandonné), Arize Phoenix (licence Elastic, dérive retirée). Le détail est dans [[Comparatif - Monitoring de modèles]].

## Choisir

- Un outil maintenu qui couvre dérive, qualité, performance, tests et LLM → [[Evidently]].
- Estimer la performance quand les étiquettes n'arrivent pas, sur du tabulaire → [[NannyML]], en sachant que l'édition libre est figée depuis juillet 2025.
- Des tests de validation rejouables en CI, en tabulaire, NLP ou vision → [[Deepchecks]], à condition d'accepter l'AGPL et une bibliothèque dormante.
- Comparer les trois sur des critères → [[Comparatif - Monitoring de modèles]].

<!-- AUTO:START -->
### Notions
- [[Data drift]] — domaines : mlops, data-sci
- [[Monitoring de modèle en production]] — domaines : mlops

### Briques
- [[Deepchecks]] — Bibliothèque Python de validation continue pour le ML — suites de checks sur données et modèles tabulaires, NLP et vision, avec conditions pass/fail rejouables en CI ; cœur AGPL-3.0, monitoring auto-hébergé limité à un modèle, évaluation de LLM et fonctions premium commerciales.
- [[Evidently]] — Framework open-source d'évaluation et de monitoring ML/LLM en Python — 100+ métriques pour détecter la dérive de données, mesurer qualité et performance et générer rapports et tableaux de bord, de l'expérimentation à la production.
- [[NannyML]] — Bibliothèque Python open source d'estimation de performance sans vérité terrain (CBPE, DLE) et de détection de dérive univariée et multivariée sur données tabulaires — édition libre figée depuis juillet 2025, fonctions avancées réservées à NannyML Cloud.

### Comparatifs
- [[Comparatif - Monitoring de modèles]]
<!-- AUTO:END -->

## Notes
