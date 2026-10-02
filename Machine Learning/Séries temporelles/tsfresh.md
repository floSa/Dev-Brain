---
role: brique
nom: tsfresh
alias: [Time Series FeatuRe Extraction, blue-yonder tsfresh, FRESH]
pitch: "Extraction automatique de centaines de caractéristiques d'une série temporelle (statistiques, spectre, dynamique non linéaire), suivie d'un filtrage par tests d'hypothèse à contrôle du taux de fausses découvertes — la table de features qui nourrit un modèle de classification ou de régression."
categorie: ml/series-temporelles
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: ["[[sktime]]"]
tags: [timeseries, feature-engineering, supervised]
url_docs: https://tsfresh.readthedocs.io/
url_repo: https://github.com/blue-yonder/tsfresh
---

# tsfresh

<!-- AUTO:BANDEAU:START -->
> Extraction automatique de centaines de caractéristiques d'une série temporelle (statistiques, spectre, dynamique non linéaire), suivie d'un filtrage par tests d'hypothèse à contrôle du taux de fausses découvertes — la table de features qui nourrit un modèle de classification ou de régression.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Paquet Python dont le nom abrège *Time Series FeatuRe Extraction based on scalable
hypothesis tests*. Il transforme chaque série (ou chaque fenêtre) en une ligne de
caractéristiques : nombre de pics, moyenne, maximum, mais aussi des descripteurs plus
fins comme la statistique de symétrie par renversement du temps. Le README parle de
« centaines » de caractéristiques, tirées de la statistique, de l'analyse de séries, du
traitement du signal et de la dynamique non linéaire. Deuxième moitié du paquet : un
filtrage de pertinence (algorithme FRESH) qui teste chaque caractéristique, une par une,
contre la cible, puis corrige les p-valeurs par la procédure de Benjamini-Yekutieli pour
contrôler la proportion de caractéristiques retenues à tort. La sortie est une table
ordinaire, que n'importe quel modèle de [[Scikit-Learn]] consomme ; la documentation
fournit des transformeurs compatibles avec ses pipelines.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Transformer des fenêtres de capteurs en table pour un classifieur de défaut ou une régression de RUL, sans écrire les descripteurs à la main | Peu de temps ou de mémoire de calcul : la documentation décrit comme problèmes des grandes séries le temps d'extraction et la mémoire, et consacre une page aux grands volumes (Dask, Spark) |
| Faire le tri : le filtre de pertinence écarte le bruit et les redondances **avant** le modèle | Des séries autocorrélées : les tests sont univariés, et la page consultée de la documentation ne traite ni l'autocorrélation ni la fuite temporelle — découper en train / test **par unité**, et refaire le filtre sur le seul train |
| Données volumineuses : le paquet accepte un DataFrame Dask, et expose une fonction pour s'insérer dans un graphe PySpark | Un modèle qui apprend les représentations de lui-même (réseau sur la fenêtre brute) : [[RUL par apprentissage profond]] n'en a pas besoin |
| Prévoir en fenêtre glissante : la documentation a une page dédiée aux séries « roulées » (rolling) | Prévoir une série : les outils de prévision ([[darts]], [[statsforecast]]) font ce travail sans table de features |

## Mise en œuvre

- Installation — `uv add tsfresh`
- Point d'entrée — API Python : `extract_features(df, column_id="id", column_sort="time")`, puis `select_features(features, y)` ; `extract_relevant_features` enchaîne les deux
- Prérequis — Python 3.9 ou plus récent d'après PyPI ; pandas et NumPy ; Dask ou PySpark seulement pour le calcul réparti
- Exécution — CPU ; parallélisme local activé par défaut, réparti sur Dask ou Spark au besoin
- Coût — gratuit, MIT ; aucune infrastructure

Version 0.21.2 publiée le 2026-05-31 ; dernier push du dépôt le 2026-07-06.

## Écosystème

### Alternatives

- voisin : [[aeon]] — la boîte à outils de séries temporelles compatible scikit-learn ; tsfresh figure parmi les extras optionnels de son installation complète.

### Compléments

- [[sktime]] — Interface unifiée, façon scikit-learn, pour toutes les tâches d'apprentissage sur séries temporelles — prévision, classification, régression, clustering, détection — avec pipelines, réglage et réduction, et des adaptateurs vers statsmodels, tsfresh, PyOD ou Prophet ; plus de 500 estimateurs.

## Ressources

- Documentation — https://tsfresh.readthedocs.io/
- Dépôt — https://github.com/blue-yonder/tsfresh
- Papier — Christ, Braun, Neuffer, Kempa-Liehr, *Time Series FeatuRe Extraction on basis of Scalable Hypothesis tests (tsfresh – A Python package)*, Neurocomputing 307, 2018 : https://doi.org/10.1016/j.neucom.2018.03.067
- Papier — Christ, Kempa-Liehr, Feindt, *Distributed and parallel time series feature extraction for industrial big data applications*, 2017 : https://arxiv.org/abs/1610.07717

## Voir aussi

- [[Time series feature engineering]] — la notion du dossier : quelles caractéristiques fabriquer, et pourquoi
- [[Séries temporelles]] — le hub du dossier
- [[Indicateurs de santé]] — ce que devient une caractéristique quand elle sert à suivre l'état d'une machine
- [[Maintenance prédictive et RUL]] — le cadre de pronostic où une table de features alimente la régression
- [[scikit-survival]] — consomme une table de features : la survie sur des fenêtres de capteurs agrégées
- [[Data leakage]] — le piège du filtre de pertinence ajusté hors du pli d'entraînement
