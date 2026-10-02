---
role: notion
nom: Types d'anomalies et régimes de supervision
alias: [Typologie des anomalies, Anomalie ponctuelle contextuelle collective, Outlier novelty OOD, Contamination]
categorie: ml/anomalie
domaines: [data-sci, ml-eng]
tags: [anomaly-detection, unsupervised]
---

# Types d'anomalies et régimes de supervision

## Aperçu

- Avant de choisir un détecteur, deux questions décident de tout : **quelle sorte d'écart** cherche-t-on (un point, un point dans son contexte, un motif entier) et **que sait-on du normal** (des étiquettes, un échantillon propre, rien).
- Le vocabulaire est flottant : *anomalie*, *outlier*, *novelty* et *hors distribution* se recouvrent selon les auteurs. Cette page pose les trois types d'écart, les trois régimes de supervision, puis le désaccord de mots.

## Concepts clés

### Trois types d'anomalies

La taxonomie vient de l'enquête de Chandola, Banerjee et Kumar (2009).

- **Ponctuelle** : une instance est anormale par rapport au reste des données. Le cas le plus simple, et celui qui concentre l'essentiel de la recherche.
- **Contextuelle** : une instance est anormale *dans un contexte précis*, et banale ailleurs. Chaque instance porte des attributs de **contexte** (le temps, la position) et des attributs de **comportement** ; le contexte découle de la structure des données et se fixe dans la formulation du problème.
- **Collective** : un *groupe* d'instances liées est anormal par rapport à l'ensemble, alors que chacune, prise seule, peut sembler ordinaire. Exemples de l'enquête : un électrocardiogramme dont une valeur basse dure trop longtemps, une séquence d'appels système.

Le type dicte la méthode. Un seuil sur une valeur suffit au ponctuel ; le contextuel exige de modéliser le contexte (la saison, le régime de marche d'une machine) ; le collectif exige de regarder des fenêtres ou des sous-séquences (cf. [[Time series anomaly detection]]).

### Trois régimes de supervision

Selon les étiquettes disponibles (Chandola et al.).

- **Supervisé** : le jeu d'entraînement est étiqueté pour le normal *et* pour l'anomalie. Deux difficultés : le déséquilibre des classes ([[Imbalanced classification]]) et le coût d'obtention des étiquettes d'anomalie.
- **Semi-supervisé** : seules des instances **normales** sont étiquetées. On apprend le normal, tout ce qui s'en écarte est suspect. C'est le régime de la plupart des lignes de production, où le défaut est rare et jamais exhaustif.
- **Non supervisé** : aucune étiquette. L'hypothèse implicite est que le normal est « bien plus fréquent » que l'anomalie dans les données de test ; sans elle, le taux de fausses alertes grimpe.

Ruff et al. (2021) présentent ces trois régimes comme un **spectre** plutôt que trois cases : on passe de l'un à l'autre en faisant varier la part de données étiquetées.

### Outlier, novelty, hors distribution : le désaccord

Trois sources, trois découpages. Les deux premiers se rejoignent peu.

- **scikit-learn** distingue par l'état de l'entraînement. *Outlier detection* : les données d'entraînement **contiennent** des outliers, que l'estimateur doit ignorer en ajustant les zones denses. *Novelty detection* : les données d'entraînement sont **propres**, et la question porte sur une observation nouvelle. Conséquence documentée : en outlier detection, les anomalies ne doivent pas former un amas dense ; en novelty detection elles le peuvent, tant que leur zone est de faible densité *dans l'entraînement*.
- **Ruff et al.** distinguent par la distribution : une *anomalie* vient d'une distribution autre que celle du normal ; un *outlier* est une instance rare du normal ; une *novelty* vient d'une région ou d'un mode nouveau d'un normal non stationnaire. Puis ils écrivent que les méthodes de détection sont essentiellement les mêmes et qu'ils ne maintiennent pas la distinction.
- **Yang et al.** (enquête sur la détection hors distribution) rangent anomalie, novelty, *open-set recognition*, hors distribution et outlier comme cas particuliers d'un même cadre. La novelty y rejoint l'anomalie *sémantique* ; l'outlier detection y est qualifiée de transductive plutôt qu'inductive, la distribution de référence étant « la majorité des observations ».

La conséquence pratique est de ne pas se fier au mot : lire, pour chaque outil, **sur quelles données il s'entraîne** et **sur quoi il prédit**. Le cas des entrées d'un réseau de neurones qui n'ont rien à voir avec ce qu'il a vu est traité dans [[Détection hors distribution (OOD)]].

### L'hypothèse « normal propre » et la contamination

- **Normal propre** : le jeu d'apprentissage ne contient que du normal. Hypothèse de tout le régime semi-supervisé, et de la *novelty detection* de scikit-learn.
- **Contamination** : une part $\eta$ des données d'apprentissage est en réalité anormale. Ruff et al. la notent ainsi : la distribution observée est un mélange du normal et de l'anomalie, et « une contamination plus forte déforme la frontière de décision du normal ».
- Dans scikit-learn, `contamination` désigne la proportion d'outliers attendue et sert **à fixer le seuil sur les scores**. Par défaut, dans `IsolationForest`, elle vaut `'auto'` (seuil « comme dans l'article original ») ; un nombre doit tomber dans $(0, 0{,}5]$.

## Les maths, simplement

- Données observées : $\mathbb{P}=(1-\eta)\,\mathbb{P}^{+}+\eta\,\mathbb{P}^{-}$, où $\mathbb{P}^{+}$ est le normal, $\mathbb{P}^{-}$ l'anomalie et $\eta$ la contamination. Régime « normal propre » : $\eta=0$.
- Un détecteur produit un **score** $s(x)$, plus grand quand $x$ est plus suspect, puis une décision $s(x)>\tau$. Le seuil $\tau$ est l'objet de [[Score et seuil d'alerte]] ; fixer `contamination` revient à choisir $\tau$ comme un quantile des scores d'entraînement.

## En pratique

- **Commencer par l'inventaire des étiquettes**, pas par l'algorithme : aucune étiquette → non supervisé, avec l'hypothèse que le normal domine ; un échantillon vérifié de normal → semi-supervisé, le régime le plus sûr en production ; des défauts étiquetés mais rares → supervisé possible, mais avec les pièges de l'évaluation en classe rare ([[Évaluer une détection d'anomalies]]).
- **Une contamination non maîtrisée est un biais silencieux** : un détecteur entraîné sur des données qui contiennent déjà des défauts apprend à les trouver normaux. Cas fréquent en industrie, où le « normal » vient de l'historique brut d'un procédé.
- Avec `LocalOutlierFactor`, le mode `novelty=True` change l'usage : `predict`, `decision_function` et `score_samples` ne s'appliquent qu'à des données **nouvelles**, jamais à l'entraînement.
- Le contexte d'une anomalie contextuelle est un choix de modélisation, pas une donnée : le fixer à tort (une saison, un régime de charge) fabrique des fausses alertes ou en masque.

## Approches voisines & alternatives

- [[Détection d'outliers univariée]] — le cas ponctuel sur un axe : Z-score, IQR, MAD.
- [[Détection d'outliers multivariée]] — le cas ponctuel dans l'espace des variables jointes.
- [[Isolation Forest]], [[Local Outlier Factor]], [[One-Class SVM]] — les trois hypothèses classiques sur le mot « anormal » : isolement, densité locale, enveloppe du normal.
- [[Time series anomaly detection]] — les types contextuel et collectif sur une série.
- [[Apprentissage non supervisé]], [[Apprentissage semi-supervisé]], [[Apprentissage supervisé]] — les régimes d'apprentissage en général, dont les trois ci-dessus sont la déclinaison pour l'anomalie.
- [[Autoencodeurs]] — apprendre le normal par reconstruction : un détecteur semi-supervisé typique.
- [[Data drift]] — le normal lui-même bouge ; ce n'est plus une anomalie mais un changement de distribution.
- [[Détection hors distribution (OOD)]] — la même question, posée à un modèle entraîné.

## Pour aller plus loin

- Chandola, Banerjee, Kumar (2009), *Anomaly Detection: A Survey*, ACM Computing Surveys 41(3), article 15. DOI : https://doi.org/10.1145/1541880.1541882
- Ruff et al. (2021), *A Unifying Review of Deep and Shallow Anomaly Detection*, Proceedings of the IEEE 109(5). arXiv : https://arxiv.org/abs/2009.11732
- Yang, Zhou, Li, Liu, *Generalized Out-of-Distribution Detection: A Survey*. arXiv : https://arxiv.org/abs/2110.11334 (venue de publication non vérifiée).
- scikit-learn, *Novelty and Outlier Detection* : https://scikit-learn.org/stable/modules/outlier_detection.html
