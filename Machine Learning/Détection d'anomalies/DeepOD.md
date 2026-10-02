---
role: brique
nom: DeepOD
alias: [deepod, Deep Outlier Detection, xuhongzuo DeepOD]
pitch: "Bibliothèque Python de détecteurs d'anomalies profonds, tabulaires et séries temporelles (Deep SVDD, REPEN, RDP, GOAD, USAD, TimesNet, Anomaly Transformer, DCdetector…), sous une API fit / decision_function à la PyOD, avec un banc d'essai de recherche ; PyTorch, dépendances épinglées anciennes et dernière release en 2023."
categorie: ml/anomalie
famille: paquet
licence_type: open-source
maturite: beta
langage: Python
alternatives: ["[[aeon]]", "[[Orion]]"]
complements: []
tags: [timeseries, deep-learning, unsupervised]
url_docs: https://deepod.readthedocs.io/
url_repo: https://github.com/xuhongzuo/DeepOD
---

# DeepOD

<!-- AUTO:BANDEAU:START -->
> Bibliothèque Python de détecteurs d'anomalies profonds, tabulaires et séries temporelles (Deep SVDD, REPEN, RDP, GOAD, USAD, TimesNet, Anomaly Transformer, DCdetector…), sous une API fit / decision_function à la PyOD, avec un banc d'essai de recherche ; PyTorch, dépendances épinglées anciennes et dernière release en 2023.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Rassemble des détecteurs d'anomalies à base de réseaux de neurones derrière une interface
unique, celle de scikit-learn et de [[PyOD]] : `clf.fit(X_train)`, puis
`clf.decision_function(X_test)` qui rend les scores d'anomalie.
Deux familles : **tabulaire** (`deepod.models.tabular`) et **séries temporelles**
(`deepod.models.time_series`). Le README annonce 27 algorithmes ; le décompte vient de deux
tableaux de 14 et 13 lignes dont cinq modèles figurent des deux côtés (DIF, Deep SVDD, DevNet,
PReNet, Deep SAD), soit 22 modèles distincts.

Relevé dans le README, avec la conférence de chaque article :

- **Tabulaires, non supervisés** : Deep SVDD (ICML 2018), REPEN (KDD 2018), RDP (IJCAI 2020), RCA
  (IJCAI 2021), GOAD (ICLR 2020), NeuTraL (ICML 2021), ICL (ICLR 2022), DIF (TKDE 2023), SLAD
  (ICML 2023).
- **Tabulaires, faiblement supervisés** (quelques anomalies connues, marquées `1`) : DevNet (KDD
  2019), PReNet (KDD 2023), Deep SAD (ICLR 2020), FeaWAD (TNNLS 2021), RoSAS (IP&M 2023).
- **Séries, non supervisés** : DCdetector (KDD 2023), TimesNet (ICLR 2023), Anomaly Transformer
  (ICLR 2022), NCAD (IJCAI 2022), TranAD (VLDB 2022), COUTA (TKDE 2024), USAD (KDD 2020), DIF,
  TcnED (TNNLS 2021), Deep SVDD.
- **Séries, faiblement supervisés** : DevNet, PReNet, Deep SAD, avec un paramètre `network` qui
  accepte TCN, GRU, LSTM, Transformer, ConvSeq ou DilatedConv.

Les auteurs du dépôt sont aussi ceux de plusieurs de ces méthodes (DIF, SLAD, RoSAS, COUTA) ;
la bibliothèque est donc un outil de recherche avant d'être un produit. Le dossier `testbed/`
fournit des scripts qui chargent un jeu, entraînent le modèle et évaluent, avec plusieurs
exécutions pour rapporter une moyenne et un écart-type. `deepod.metrics` propose
`ts_metrics` et `point_adjustment` ; ce dernier gonfle les scores, voir
[[Évaluer une détection d'anomalies]].

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Comparer plusieurs détecteurs profonds (tabulaires et séries) avec une API unique, comme avec [[PyOD]] | Ligne de base à battre d'abord : [[TSB-AD]] rapporte que méthodes simples et statistiques battent souvent les réseaux profonds |
| Reproduire ou citer des articles récents de détection profonde (DCdetector, TimesNet, COUTA, DIF…) | Production durable : dernière release 0.4.1 en 2023-09 ; les dépendances sont épinglées anciennes |
| Peu d'anomalies étiquetées disponibles : DevNet, PReNet, Deep SAD, FeaWAD, RoSAS | Un environnement récent (PyTorch actuel, Python 3.11+) : `torch>=1.10,<1.13.1` ; classifieurs PyPI jusqu'à Python 3.10 |
| Séries multivariées avec du `time_series.TimesNet`, `TranAD` ou `USAD` | Aucun GPU ni temps d'entraînement : chaque modèle s'entraîne, contrairement à [[STUMPY]] ou [[Isolation Forest]] |
| | Évaluer en croyant le point-adjust : il est fourni mais optimiste → [[Évaluer une détection d'anomalies]] |

## Mise en œuvre

- Installation — `uv add deepod` ; le README recommande plutôt l'installation depuis les sources (`git clone`, puis `pip install .`) comme version de développement
- Point d'entrée — API Python : `from deepod.models.tabular import DeepSVDD` ou `from deepod.models.time_series import TimesNet`, puis `fit` et `decision_function`
- Prérequis — PyTorch (`>=1.10,<1.13.1`), NumPy, SciPy, scikit-learn, pandas, tqdm ; le `requirements.txt` ajoute `ray==2.6.1`, `einops`, `statsmodels`, `arch` ; GPU recommandé pour les modèles de séries
- Exécution — en bibliothèque, entraînement local (CPU ou CUDA) ; aucune infrastructure à héberger
- Coût — gratuit, BSD-2-Clause (fichier LICENSE du dépôt) ; coût réel : temps d'entraînement et conflit possible de versions avec une pile PyTorch récente

## Écosystème

### Alternatives

- [[aeon]] — Boîte à outils Python compatible scikit-learn pour l'apprentissage sur séries temporelles — classification, régression, clustering, prévision, segmentation et anomalies ; son module d'anomalies est modeste (une quinzaine de détecteurs fenêtrés ou à distance, aucun réseau profond) : l'intérêt est de rester dans la même API que le reste.
- [[Orion]] — Bibliothèque Python du Data to AI Lab (MIT) de détection d'anomalies non supervisée sur séries temporelles — pipelines « vérifiés » prêts à l'emploi (AER, TadGAN, LSTM à seuil dynamique, autoencodeurs, matrix profile…), benchmark intégré, statut officiel pre-alpha.

## Ressources

- Documentation — https://deepod.readthedocs.io/
- Dépôt — https://github.com/xuhongzuo/DeepOD
- Papier — Article cité par le README : Xu, Pang, Wang, Wang, *Deep isolation forest for anomaly detection*, IEEE TKDE 35(12), 2023 : https://doi.org/10.1109/TKDE.2023.3270293

## Voir aussi

- [[Anomalies multivariées par apprentissage profond]] — la notion qu'il outille : reconstruction, prédiction, représentation et leurs limites
- [[Détection d'anomalies]] — le hub du dossier
- [[Comparatif - Détection d'anomalies en séries temporelles]] — ce qui le départage des détecteurs de séries
- [[Autoencodeurs]] — le mécanisme de reconstruction derrière USAD, RCA et d'autres
- [[PyTorch]] — le moteur d'entraînement
- [[Évaluer une détection d'anomalies]] — point-adjust, VUS-PR et pièges d'évaluation
- [[Jeux de données d'anomalies]] — ADBench pour le tabulaire, jeux de séries pour le reste
