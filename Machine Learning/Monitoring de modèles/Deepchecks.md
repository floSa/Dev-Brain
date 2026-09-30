---
role: brique
nom: Deepchecks
alias: [deepchecks, deepchecks testing]
pitch: "Bibliothèque Python de validation continue pour le ML — suites de checks sur données et modèles tabulaires, NLP et vision, avec conditions pass/fail rejouables en CI ; cœur AGPL-3.0, monitoring auto-hébergé limité à un modèle, évaluation de LLM et fonctions premium commerciales."
categorie: ml/monitoring
famille: paquet
domaines: [mlops, data-sci]
licence_type: open-core
maturite: production
langage: Python
alternatives: ["[[Evidently]]", "[[NannyML]]"]
complements: []
tags: [model-monitoring, data-drift, model-evaluation, data-validation]
url_docs: https://docs.deepchecks.com/stable/
url_repo: https://github.com/deepchecks/deepchecks
---

# Deepchecks

<!-- AUTO:BANDEAU:START -->
> Bibliothèque Python de validation continue pour le ML — suites de checks sur données et modèles tabulaires, NLP et vision, avec conditions pass/fail rejouables en CI ; cœur AGPL-3.0, monitoring auto-hébergé limité à un modèle, évaluation de LLM et fonctions premium commerciales.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-core | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque Python qui traite la validation d'un modèle comme des **tests logiciels**. Des
*checks* (intégrité des données, dérive, fuite de données, performance, segments faibles,
cohérence entre jeux d'entraînement et de test) sont regroupés en *suites* ; chaque check porte des
**conditions** dont le résultat est pass, fail ou warning, et la suite échoue comme un test
échoue. Trois modules : tabulaire (installé par défaut), NLP et vision (extras `deepchecks[nlp]`
et `deepchecks[vision]`). Le **module LLM n'est pas dans le paquet libre** : l'évaluation de LLM est
une plateforme commerciale distincte. Un service de monitoring (dépôt `deepchecks/monitoring`)
complète la bibliothèque pour le suivi en production. La bibliothèque sert de garde-fou avant
déploiement ; elle outille [[Monitoring de modèle en production]] en amont, là où
[[Evidently]] couvre surtout l'aval.

**État au 2026-09-30.** Dernière version 0.19.1 (PyPI, 2024-12-15) ; dernier commit sur `main` le
2025-11-24 ; 4 061 étoiles ; 255 issues ouvertes. Check Point a annoncé le 2026-05-22 l'acquisition
de l'équipe et de la propriété intellectuelle de Deepchecks ; le site de l'éditeur ne parle plus que
d'évaluation de LLM, payante, et aucune source lue ne dit ce que devient le code open source.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Des **tests de validation avant déploiement** à faire échouer un build : le même jeu de checks couvre tabulaire, NLP et vision, avec des conditions rejouables | **Licence** : le cœur est sous AGPL-3.0-or-later (plus une permission additionnelle pour le dossier `ee/` du dépôt de monitoring, sous licence commerciale). Un usage interne est simple ; une offre réseau ou une redistribution demande une revue juridique |
| Un pipeline CI documenté : exemple GitHub Actions complet (`sys.exit(1)` si la suite échoue) et page d'intégration Airflow avec export HTML vers S3 | La bibliothèque est **dormante** : aucune release depuis décembre 2024, le correctif NumPy 2 (`np.Inf`) n'est sorti dans aucune version et exige une installation depuis `main`, un bug scikit-learn ≥ 1.7 (`needs_proba`) est ouvert |
| Un rapport HTML ou JSON par exécution, lisible hors Jupyter | Le **monitoring auto-hébergé** est une installation de démonstration : un modèle par déploiement, capacité « limitée » au-delà d'environ 100 000 échantillons par mois, Docker, 4 Go de RAM, 2 vCPU, 20 Go de disque ; le code de `ee/` exige une licence Deepchecks |
| | Évaluer un **LLM** : hors du paquet libre. Le module vision tire des dépendances vieillissantes (`albumentations<1.4`, `imgaug`) |
| | Pas d'intégration documentée avec Prometheus, Grafana, MLflow ou Kubernetes dans les pages lues |

## Mise en œuvre

- Installation — `uv add deepchecks` (extras `deepchecks[nlp]` ou `deepchecks[vision]` selon le module) ; le monitoring s'installe avec `deepchecks-installer install-monitoring`, en Docker Compose
- Point d'entrée — API Python : un jeu de données enveloppé dans un `Dataset`, une suite de checks, puis `suite.run()` ; le résultat s'exporte en HTML, en JSON ou en valeurs Python
- Prérequis — Python 3 (aucune borne déclarée, des installations en 3.11 et 3.12 sont rapportées), les extras NLP et vision tirent PyTorch de façon transitive ; un vérificateur de version tourne au premier import, `DISABLE_LATEST_VERSION_CHECK` le coupe
- Exécution — en bibliothèque dans un job ou une CI ; le monitoring est un service à héberger à côté
- Coût — bibliothèque gratuite (AGPL-3.0) ; LLM, tests managés en CI et fonctions premium sont commerciaux, avec des déploiements SaaS, VPC et on-prem proposés par l'éditeur pour cette offre

## Écosystème

### Alternatives

- [[Evidently]] — Framework open-source d'évaluation et de monitoring ML/LLM en Python — 100+ métriques pour détecter la dérive de données, mesurer qualité et performance et générer rapports et tableaux de bord, de l'expérimentation à la production.
- [[NannyML]] — Bibliothèque Python open source d'estimation de performance sans vérité terrain (CBPE, DLE) et de détection de dérive univariée et multivariée sur données tabulaires — édition libre figée depuis juillet 2025, fonctions avancées réservées à NannyML Cloud.

## Ressources

- Documentation — https://docs.deepchecks.com/stable/
- Dépôt — https://github.com/deepchecks/deepchecks
- Documentation — monitoring auto-hébergé : https://docs.deepchecks.com/monitoring/stable/getting-started/deploy_self_host_open_source.html
- Article — rachat par Check Point : https://securityboulevard.com/2026/05/check-point-acquires-deepchecks-as-it-builds-out-agentic-security-platform/

## Voir aussi

- [[Monitoring de modèle en production]] — le cadre opérationnel que les suites de checks outillent avant déploiement
- [[Data drift]] — les checks de dérive entre jeu de référence et jeu courant
- [[Comparatif - Monitoring de modèles]] — ce qui départage les trois outils du dossier
- [[GitHub Actions]] — l'exemple officiel de pipeline CI qui fait échouer le build si une suite de checks échoue
- [[Airflow]] — la page d'intégration officielle : checks en tâches de court-circuit, rapport HTML exporté vers S3
