---
role: brique
nom: sktime
alias: [sktime-ai, scikit-time, sktime forecasting]
pitch: "Interface unifiée, façon scikit-learn, pour toutes les tâches d'apprentissage sur séries temporelles — prévision, classification, régression, clustering, détection — avec pipelines, réglage et réduction, et des adaptateurs vers statsmodels, tsfresh, PyOD ou Prophet ; plus de 500 estimateurs."
categorie: ml/series-temporelles
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[darts]]", "[[aeon]]"]
complements: ["[[tsfresh]]"]
tags: [timeseries, forecasting, classification, clustering]
url_docs: https://www.sktime.net/
url_repo: https://github.com/sktime/sktime
---

# sktime

<!-- AUTO:BANDEAU:START -->
> Interface unifiée, façon scikit-learn, pour toutes les tâches d'apprentissage sur séries temporelles — prévision, classification, régression, clustering, détection — avec pipelines, réglage et réduction, et des adaptateurs vers statsmodels, tsfresh, PyOD ou Prophet ; plus de 500 estimateurs.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque Python qui donne une même interface à des tâches voisines mais distinctes sur
séries temporelles. Le README en liste les modules avec un statut : prévision, classification,
régression et transformations sont « stables » ; détection, clustering, distances et
séparateurs temporels sont « en maturation » ; l'alignement est expérimental. Deux idées la
portent. La première est l'**uniformité** : un estimateur de prévision, de classification
ou de régression se manipule comme dans scikit-learn (`fit`, `predict`), et la documentation
annonce plus de 500 estimateurs, certains écrits pour la bibliothèque, d'autres venus
d'ailleurs par adaptateur (scikit-learn, statsmodels, tsfresh, PyOD, Prophet…). La seconde est
la **composition** : pipelines, ensembles, réglage, et « réduction » — appliquer un algorithme
conçu pour une tâche à une autre, par exemple un régresseur tabulaire à une prévision.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Une seule API pour classer des fenêtres de capteurs, régresser un RUL et prévoir une grandeur, avec la même validation temporelle | Seule la prévision compte, avec backtesting et covariables prêts à l'emploi → [[darts]], [[statsforecast]] ; le catalogue large de sktime est aussi une surface à apprendre |
| Brancher des bibliothèques existantes (tsfresh, PyOD, statsmodels) derrière le même `fit` / `predict` et les mêmes pipelines | Détection d'anomalies sérieuse : le module « détection » est annoncé en maturation, l'outillage dédié est ailleurs → [[PyOD]], [[Comparatif - Détection d'anomalies en séries temporelles]] |
| Comparer des algorithmes de classification de séries sur le même protocole | Dépendances : les extras optionnels sont nombreux, et la version de Python est bornée (3.10 à 3.14 d'après PyPI et la documentation) ; isoler l'environnement |
| Prototyper avant de choisir un outil spécialisé, sans réécrire les données | [[aeon]] est un fork de sktime v0.16.0 (2022, d'après son README) : même idée, projet distinct — comparer avant de s'engager sur l'un |

## Mise en œuvre

- Installation — `uv add sktime` ; des extras optionnels ajoutent les dépendances des familles d'estimateurs
- Point d'entrée — API Python : `from sktime.forecasting.theta import ThetaForecaster`, `from sktime.split import temporal_train_test_split`, `ForecastingHorizon` pour l'horizon
- Prérequis — Python 3.10 à 3.14 ; pandas et NumPy ; les bibliothèques adaptées (statsmodels, tsfresh, PyOD…) restent des dépendances optionnelles
- Exécution — dans le process appelant, CPU, mono-nœud
- Coût — gratuit, BSD-3-Clause ; aucune infrastructure

Version 1.2.0 publiée le 2026-09-22 ; dépôt actif (dernier push le 2026-09-29).

## Écosystème

### Alternatives

- [[darts]] — Bibliothèque de prévision unifiée — une même API fit/predict de l'ARIMA aux réseaux de neurones (PyTorch Lightning), avec backtesting, covariables et détection d'anomalies.
- [[aeon]] — Boîte à outils Python compatible scikit-learn pour l'apprentissage sur séries temporelles — classification, régression, clustering, prévision, segmentation et anomalies ; son module d'anomalies est modeste (une quinzaine de détecteurs fenêtrés ou à distance, aucun réseau profond) : l'intérêt est de rester dans la même API que le reste.

### Compléments

- [[tsfresh]] — Extraction automatique de centaines de caractéristiques d'une série temporelle (statistiques, spectre, dynamique non linéaire), suivie d'un filtrage par tests d'hypothèse à contrôle du taux de fausses découvertes — la table de features qui nourrit un modèle de classification ou de régression.

## Ressources

- Documentation — https://www.sktime.net/
- Dépôt — https://github.com/sktime/sktime
- Tutoriel — https://www.sktime.net/en/stable/examples.html

## Voir aussi

- [[Séries temporelles]] — le hub du dossier
- [[Forecasting framing]] — cadrer l'horizon et la validation que ses séparateurs temporels matérialisent
- [[Comparatif - Forecasting]] — ce qui départage les briques de prévision du dossier
- [[Maintenance prédictive et RUL]] — la régression et la classification de fenêtres y servent le pronostic
- [[Time series feature engineering]] — la notion que ses transformations outillent
- [[Walk-forward CV]] — la validation en origine glissante, à garder pour évaluer un modèle de maintenance
