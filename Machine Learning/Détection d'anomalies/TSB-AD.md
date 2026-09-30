---
role: brique
nom: TSB-AD
alias: [TSB_AD, TheDatumOrg TSB-AD, The Elephant in the Room]
pitch: "Banc d'essai et bibliothèque Python de détection d'anomalies en séries temporelles (NeurIPS 2024) — 1 070 séries univariées et multivariées tirées de 40 jeux, une quarantaine d'algorithmes statistiques, neuronaux et modèles de fondation sous une même fonction, et VUS-PR comme métrique de référence ; sert à comparer et à évaluer, pas à déployer."
categorie: ml/anomalie
famille: paquet
licence_type: open-source
maturite: beta
langage: Python
alternatives: []
complements: []
tags: [timeseries, benchmark, model-evaluation]
url_docs: https://thedatumorg.github.io/TSB-AD/
url_repo: https://github.com/TheDatumOrg/TSB-AD
---

# TSB-AD

<!-- AUTO:BANDEAU:START -->
> Banc d'essai et bibliothèque Python de détection d'anomalies en séries temporelles (NeurIPS 2024) — 1 070 séries univariées et multivariées tirées de 40 jeux, une quarantaine d'algorithmes statistiques, neuronaux et modèles de fondation sous une même fonction, et VUS-PR comme métrique de référence ; sert à comparer et à évaluer, pas à déployer.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

*The Elephant in the Room: Towards A Reliable Time-Series Anomaly Detection Benchmark*
(Liu et Paparrizos, NeurIPS 2024, Datasets and Benchmarks) vise trois défauts du domaine :
jeux de données défectueux, métriques biaisées, protocoles de comparaison incohérents. Le
dépôt `TheDatumOrg/TSB-AD` en est le code, sous trois angles :

- **Données** : TSB-AD-U (univarié) et TSB-AD-M (multivarié), 1 070 séries de 40 jeux, à
  télécharger à part (archives hébergées sur `thedatum.org`, pas dans le dépôt).
- **Algorithmes** : le README annonce 40 détecteurs, rangés en méthodes statistiques ((Sub-)MCD,
  OCSVM, LOF, KNN, IForest, HBOS, PCA, COPOD, MatrixProfile, SAND, Series2Graph, SR…),
  réseaux de neurones (AutoEncoder, LSTMAD, Donut, OmniAnomaly, USAD, Anomaly Transformer,
  TranAD, TimesNet, FITS…) et modèles de fondation (OFA, Lag-Llama, [[Chronos]], TimesFM,
  MOMENT). Le code en liste davantage (`TSB_AD/model_wrapper.py` : 33 + 29 noms, variantes comprises) ; le tableau du README n'a pas été recompté.
- **Évaluation** : `get_metrics(output, label)` rend AUC-ROC, AUC-PR, VUS-ROC et VUS-PR
  (indépendantes d'un seuil), plus F1 ponctuel, F1 avec point-adjust, F1 par événement, F1 par
  plage et F affiliée (dépendantes d'un seuil, fixé par défaut sur un seuil oracle). Le README
  désigne **VUS-PR** comme la mesure la plus fiable. Les métriques sont décrites dans
  [[Évaluer une détection d'anomalies]].

Résultat annoncé dans le résumé de l'article : les architectures simples et les méthodes
statistiques battent souvent les réseaux profonds, tandis que les réseaux se défendent mieux en
multivarié et les modèles de fondation sur les anomalies ponctuelles. Un classement public accepte des soumissions depuis le 2026-04-01 (README).

TSB-AD **n'est pas** un détecteur à mettre en production : c'est la grille d'essai qui sert à
décider quel détecteur (voir [[Comparatif - Détection d'anomalies en séries temporelles]])
mérite d'être gardé.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Choisir un détecteur de séries sur des données comparables aux vôtres, avec un protocole de réglage publié (jeux de réglage et d'évaluation séparés) | Livrer un détecteur à un client : c'est un banc d'essai, le code est de recherche (une fonction `run_<modèle>` par algorithme) |
| Évaluer son propre détecteur avec VUS-PR, plus fiable que point-adjust, et le soumettre au classement | Un seul jeu de données à vous : les 1 070 séries ne dispensent pas d'un test sur vos données |
| Récupérer des implémentations de référence (Sub-PCA, KShapeAD, SAND, Series2Graph…) | Réutiliser les **données** commercialement sans lire chaque licence : le jeu agrège 40 sources de licences différentes |
| Étudier les limites des jeux classiques et du point-adjust | Environnement NumPy 2 : la version PyPI 1.5 épingle `numpy<2.0`, à installer dans un environnement à part |
| | Un modèle de fondation : installations manuelles (autogluon pour Chronos, `momentfm` limité à Python 3.11, `timesfm`, etc.) |

## Mise en œuvre

- Installation — `uv add TSB-AD` (le nom PyPI est `TSB-AD`, version 1.5 du 2025-02-18, bien plus ancienne que le dépôt, dernier push le 2026-09-07 ; pour le code courant, cloner le dépôt puis `pip install -e .`)
- Point d'entrée — API Python : `from TSB_AD.model_wrapper import run_Unsupervise_AD`, puis `from TSB_AD.evaluation.metrics import get_metrics` ; ou `python -m TSB_AD.main --AD_Name IForest`
- Prérequis — Python `>=3.8` selon PyPI, 3.8 à 3.12 selon le README ; PyTorch, scikit-learn, stumpy, tslearn, transformers, arch, einops ; les jeux TSB-AD-U/M sont à télécharger séparément ; les modèles de fondation demandent des installations additionnelles (voir `TSB_AD/models/README.md`)
- Exécution — CPU ou GPU mono-machine, en bibliothèque ; le dossier `TSB_AD/models` contient un binaire compilé (`TimeRCD_MAFT`, Linux x86-64, CPython 3.11) à côté des sources
- Coût — gratuit ; code et curation sous Apache-2.0 (fichier LICENSE du dépôt) ; les **données** gardent la licence de chaque jeu source (voir ci-dessous)

### Licence du code et licence des données

Le README précise que les jeux sont fournis pour la reproductibilité, que les étapes de
prétraitement et de curation sont sous Apache-2.0, et que l'usage d'un jeu impose de se référer
à sa source. La page du projet liste des licences hétérogènes : « None » pour certains, GPL,
CC0-1.0, Apache-2.0, CC BY 4.0, CC BY-NC-SA 4.0, MIT, Caltech, Open Data Commons Attribution
v1.0. Un seul `licence_type: open-source` ne dit donc **que le code**. Le détail par jeu est
dans [[Jeux de données d'anomalies]].

## Écosystème

### Alternatives

<!-- Aucune : un banc d'essai n'a pas d'équivalent fiché dans le brain. -->

## Ressources

- Documentation — https://thedatumorg.github.io/TSB-AD/ (jeux, classement, licences par jeu)
- Dépôt — https://github.com/TheDatumOrg/TSB-AD
- Article — Liu et Paparrizos, *The Elephant in the Room: Towards A Reliable Time-Series Anomaly Detection Benchmark*, NeurIPS 2024 : https://openreview.net/pdf?id=R6kJtWsTGy
- Dépôt — s apparentés (README : TSB-UAD (suite univariée, VLDB 2022), VUS (mesure d'exactitude), TSB-AutoAD

## Voir aussi

- [[Évaluer une détection d'anomalies]] — VUS-PR, point-adjust et leurs défauts, que ce dépôt implémente
- [[Anomalies multivariées par apprentissage profond]] — ce que le banc d'essai dit des réseaux profonds sur séries multivariées
- [[Détection d'anomalies]] — le hub du dossier
- [[Comparatif - Détection d'anomalies en séries temporelles]] — la grille de choix, que ce banc d'essai chiffre
- [[Jeux de données d'anomalies]] — l'entrée TSB-AD et les licences des jeux sources
- [[Time series anomaly detection]] — la notion générale
- [[Foundation models pour séries temporelles]] — les modèles de fondation testés (Chronos, TimesFM, MOMENT…)
- [[STUMPY]] — le matrix profile, une des références statistiques du banc
