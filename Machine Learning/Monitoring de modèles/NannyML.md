---
role: brique
nom: NannyML
alias: [nannyml, nanny ml]
pitch: "Bibliothèque Python open source d'estimation de performance sans vérité terrain (CBPE, DLE) et de détection de dérive univariée et multivariée sur données tabulaires — édition libre figée depuis juillet 2025, fonctions avancées réservées à NannyML Cloud."
categorie: ml/monitoring
famille: paquet
domaines: [mlops, data-sci]
licence_type: open-core
maturite: production
langage: Python
alternatives: ["[[Evidently]]", "[[Deepchecks]]"]
complements: []
tags: [model-monitoring, data-drift, concept-drift, model-evaluation]
url_docs: https://nannyml.readthedocs.io/en/stable/
url_repo: https://github.com/NannyML/nannyml
---

# NannyML

<!-- AUTO:BANDEAU:START -->
> Bibliothèque Python open source d'estimation de performance sans vérité terrain (CBPE, DLE) et de détection de dérive univariée et multivariée sur données tabulaires — édition libre figée depuis juillet 2025, fonctions avancées réservées à NannyML Cloud.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-core | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque Python qui répond à une question précise : **comment se comporte un modèle déployé
dont les étiquettes n'arrivent pas encore ?** Elle **estime la performance** sans vérité terrain
— CBPE (*confidence-based performance estimation*) pour la classification, DLE (*direct loss
estimation*) pour la régression — puis relie les alertes de dérive à leur effet probable sur cette
performance, pour ne réagir que lorsque la dérive compte. La dérive se détecte par feature (six
méthodes univariées) et sur l'ensemble des variables (reconstruction par ACP, classifieur de
domaine). Le périmètre est le **tabulaire**, en classification et en régression : ni vision, ni
texte, ni LLM. Elle outille la couche « performance » de [[Monitoring de modèle en production]]
et mesure ce que [[Data drift]] décrit.

**État au 2026-09-30.** Dernière version 0.13.1, publiée sur PyPI le 2025-07-12 ; 2 156 étoiles ;
aucun commit sur la branche principale depuis cette date. Soda a racheté NannyML le 2025-06-09 et a
écrit que le projet open source resterait « maintained and fully supported », sans l'arrêter. Dans
les faits, le dépôt n'est pas archivé mais dort : une issue intitulée « Stale repository since soda
acquisition » (2026-07) a été fermée par un robot d'obsolescence, et des bugs de septembre 2026
restent sans réponse.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Les étiquettes arrivent en **différé** (jours, semaines, jamais) et la performance doit quand même être estimée : c'est la fonction centrale de CBPE et DLE | Le dépôt est **figé** : dernière release en juillet 2025, `plotly<6`, `kaleido<0.3`, `lightgbm<4.6` épinglés, Python limité à 3.9–3.12 ; l'écart avec pandas, numpy et plotly récents ne fera que grandir |
| Une édition **Apache-2.0** à forker et à épingler : le code complet de l'édition libre est auditable, et un gel se gère en copiant le dépôt | Le concept drift, M-CBPE, les dashboards, les webhooks et notifications, le stockage de métriques, la planification et le multi-modèles sont **réservés à NannyML Cloud**, propriétaire |
| Données tabulaires, classification ou régression | Vision, texte, LLM ou séries d'embeddings : aucun support, et l'issue sur les LLM est fermée sans réponse |
| Un job batch planifiable sans service à héberger : CLI `nml run` pilotée par un fichier YAML, planificateur APScheduler intégré, image Docker | Un service avec interface et alertes dans l'édition libre : il n'y en a pas, la *Web App* n'est qu'une liste d'attente |
| | La **télémétrie** est active par défaut (`segment-analytics-python`, dépendance obligatoire) : exporter `NML_DISABLE_USAGE_LOGGING=1` dans tout déploiement on-prem ou isolé |

## Mise en œuvre

- Installation — `uv add nannyml`
- Point d'entrée — API Python (chunks, période de **référence** et période d'**analyse**) ou CLI `nml run` avec un fichier YAML ; sorties en graphiques Plotly, DataFrames, fichiers ou base relationnelle (extra `db`)
- Prérequis — une période de référence représentative avec ses étiquettes (les estimateurs s'y calibrent) ; Python 3.9 à 3.12
- Exécution — bibliothèque ou job planifié, sans rien à héberger ; l'image `nannyml/nannyml` tourne en conteneur ; lecture locale ou via fsspec (S3, GCS, Azure)
- Coût — édition libre Apache-2.0, gratuite ; NannyML Cloud est payant (deux grilles de prix contradictoires sur le site au 2026-09-30, aucune retenue ici)

## Écosystème

### Alternatives

- [[Evidently]] — Framework open-source d'évaluation et de monitoring ML/LLM en Python — 100+ métriques pour détecter la dérive de données, mesurer qualité et performance et générer rapports et tableaux de bord, de l'expérimentation à la production.
- [[Deepchecks]] — Bibliothèque Python de validation continue pour le ML — suites de checks sur données et modèles tabulaires, NLP et vision, avec conditions pass/fail rejouables en CI ; cœur AGPL-3.0, monitoring auto-hébergé limité à un modèle, évaluation de LLM et fonctions premium commerciales.

## Ressources

- Documentation — https://nannyml.readthedocs.io/en/stable/
- Dépôt — https://github.com/NannyML/nannyml
- Article — rachat par Soda : https://soda.io/blog/soda-acquires-nannyml
- Article — édition libre contre Cloud : https://www.nannyml.com/oss-vs-cloud

## Voir aussi

- [[Monitoring de modèle en production]] — la couche « performance » que CBPE et DLE estiment sans étiquettes
- [[Data drift]] — la dérive de données qu'il détecte, par feature et en multivarié
- [[Comparatif - Monitoring de modèles]] — ce qui départage les trois outils du dossier
- [[Détection hors distribution (OOD)]] — la même question posée à l'entrée isolée plutôt qu'au flux : frontière avec la dérive de données
