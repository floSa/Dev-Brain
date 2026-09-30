---
role: comparatif
nom: Comparatif - Monitoring de modèles
categorie: ml/monitoring
tags: [model-monitoring, data-drift, model-evaluation]
---

# Comparatif - Monitoring de modèles

> On tranche sur : **la vérité terrain dont on dispose** (étiquettes immédiates, différées ou absentes), **le moment du contrôle** (avant déploiement ou en production) et **la maintenance sur laquelle on peut compter** — deux outils sur trois sont à l’arrêt.

![[Comparatif - Monitoring de modèles.base]]

## Ce qui départage

- [[Evidently]] — le seul des trois **réellement maintenu** (v0.7.23, septembre 2026) et le plus large : dérive, qualité des données, performance, suites de tests pass/fail en CI, évaluation de LLM, rapports et dashboard de monitoring dans l'édition libre. Les alertes, tâches planifiées, authentification et RBAC sont réservés à l'édition commerciale, et l'API a été refondue à la 0.7.
- [[NannyML]] — le seul dont l'objet est d'**estimer la performance sans étiquettes** (CBPE, DLE) et de relier la dérive à son effet sur elle. Tabulaire seulement, Apache-2.0, mais figé depuis juillet 2025 ; concept drift, dashboards, alertes et planification sont dans NannyML Cloud.
- [[Deepchecks]] — le seul qui traite la validation comme des **tests avant déploiement**, en tabulaire, NLP et vision. AGPL-3.0 pour le cœur, bibliothèque dormante depuis décembre 2024, équipe rachetée par Check Point, LLM et fonctions premium commerciaux.

## Par critère

| Critère | [[Evidently]] | [[NannyML]] | [[Deepchecks]] |
|---|---|---|---|
| Dérive de données | 20+ méthodes de test, PSI, Wasserstein, Jensen-Shannon | six méthodes univariées, reconstruction par ACP, classifieur de domaine | checks de dérive entre jeu de référence et jeu courant |
| Dérive de concept | via performance et prédictions | détecteur réservé à NannyML Cloud | non documenté dans les pages lues |
| Performance sans vérité terrain | proxies : dérive des features et des scores | **estimation CBPE et DLE**, cœur de l'outil | non documenté dans les pages lues |
| Tests avant déploiement | suites pass/fail rejouables en CI | non | **cœur de l'outil**, tabulaire, NLP et vision |
| LLM | oui (évaluation, tracing) | non | plateforme commerciale, hors du paquet libre |
| Rapports et tableaux de bord | rapports, dashboard de monitoring libre | graphiques Plotly ; dashboard dans Cloud | rapports HTML et JSON ; dashboard du monitoring limité à un modèle |
| Exploitation | bibliothèque + service UI en conteneur | bibliothèque, CLI YAML, APScheduler, image Docker | bibliothèque + service Docker Compose |
| Licence | Apache-2.0, fonctions d'exploitation payantes | Apache-2.0, fonctions avancées dans Cloud | AGPL-3.0-or-later, `ee/` et LLM commerciaux |
| Maintenance (2026-09-30) | active | aucun commit depuis 2025-07-12 | aucun commit depuis 2025-11-24, dernière release 2024-12 |

## Écartés, sans fiche

Quatre outils de dérive ont été évalués à la source et n'ont pas de fiche, faute de maintenance ou de licence exploitable on-prem.

- **Alibi Detect** (Seldon) — détecteurs de dérive et d'anomalies très complets, mais sous **BSL 1.1** depuis janvier 2024 : la production n'est permise gratuitement qu'aux établissements d'enseignement à but non lucratif, toute autre entreprise doit acheter une licence. Dernière release 0.13.0 le 2025-12-11, aucun commit depuis. Il se déploie derrière [[Seldon Core]] et [[KServe]], dont l'exemple officiel en dépend. Seldon a été racheté par TrueFoundry en juin 2026.
- **whylogs** — profils statistiques de jeux de données, Apache-2.0, mais dernière release le 2024-12-03 et dernier commit en janvier 2025 ; l'éditeur WhyLabs a fermé.
- **Frouros** — bibliothèque dédiée à la seule dérive (données et concept, flux), BSD-3-Clause, publiée dans SoftwareX en 2024 ; 261 étoiles, dernière release en octobre 2024. Maintenue à petite échelle, trop confidentielle pour une fiche.
- **Arize Phoenix** — licence Elastic 2.0, et surtout observabilité de LLM : l'analyse de dérive d'embeddings a été retirée en février 2026 (version 13.3.0). La dérive de ML classique reste dans l'offre commerciale d'Arize.

## Voir aussi

- [[Monitoring de modèles]] — le dossier de ces outils
- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
