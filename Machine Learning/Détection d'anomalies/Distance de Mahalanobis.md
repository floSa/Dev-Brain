---
role: notion
nom: Distance de Mahalanobis
alias: [distance de Mahalanobis, Mahalanobis distance, distance généralisée, distance de Mahalanobis au carré, D² de Mahalanobis]
categorie: ml/anomalie
domaines: [data-sci, ml-eng]
tags: [anomaly-detection, multivariate, unsupervised]
---

# Distance de Mahalanobis

## Aperçu

- La distance de Mahalanobis dit **à quel point un point est bizarre**, en tenant compte de deux choses que la distance ordinaire ignore : l'**échelle** de chaque capteur et les **corrélations** entre capteurs. Un point peut être normal sur chaque capteur pris seul et anormal **ensemble**, parce qu'il casse une relation habituelle.
- Exemple de chaudière : la température et la pression montent et descendent presque ensemble (corrélation 0,9). Voir les deux monter de deux écarts-types est banal. Voir l'une monter de deux écarts-types **pendant que l'autre descend** de deux est un signal fort, alors que chaque valeur isolée reste dans la plage. La distance euclidienne ne voit aucune différence entre les deux cas ; Mahalanobis, oui.
- La page est le point d'entrée du sujet. Les détecteurs qui l'emploient (l'enveloppe elliptique) sont dans [[Détection d'outliers multivariée]], et sa décomposition capteur par capteur dans [[Expliquer une anomalie (contribution des capteurs)]].

## Concepts clés

### Une distance qui suit la forme du nuage

- Les points normaux forment un nuage en **ellipse** (allongée le long des corrélations). Mahalanobis mesure la distance **en unités de cette ellipse** : un point est à 3 si, dans la direction où il s'écarte, il est à 3 écarts-types de dispersion normale.
- Deux points à égale distance euclidienne du centre peuvent avoir des distances de Mahalanobis très différentes : celui qui s'écarte dans la direction large du nuage est normal, celui qui s'écarte dans la direction étroite est suspect.

### Le seuil se lit dans une table de $\chi^2$

- Si les données normales sont à peu près **gaussiennes**, le carré de la distance suit une loi du $\chi^2$ à $p$ degrés de liberté, avec $p$ le nombre de capteurs. Un seuil se fixe donc par un quantile, par exemple le 99,9 %, sans avoir à régler un paramètre à l'aveugle.

### Le piège du masquage et la version robuste

- Le centre $\mu$ et la covariance $\Sigma$ doivent être estimés sur les données. Si ces données contiennent déjà des anomalies, elles **tirent** $\mu$ et **gonflent** $\Sigma$ : les anomalies se cachent derrière leur propre influence (masquage).
- Remède : une estimation **robuste**, le déterminant de covariance minimal (MCD, algorithme rapide de Rousseeuw et Van Driessen, 1999). C'est ce qu'emploie l'`EllipticEnvelope` de scikit-learn : une estimation robuste de la position et de la covariance, puis les distances de Mahalanobis comme mesure d'étrangeté.

## Les maths, simplement

- $d_M^2(x)=(x-\mu)^\top\Sigma^{-1}(x-\mu)$ : l'écart au centre, pondéré par l'inverse de la covariance. Si $\Sigma$ est l'identité, on retrouve la distance euclidienne au carré.
- **Exemple chiffré** (calcul de cette page). Deux capteurs centrés réduits, de corrélation $\rho=0{,}9$ : $d_M^2=\dfrac{x_1^2-2\rho x_1x_2+x_2^2}{1-\rho^2}$.
  - Point $(2;\,2)$ : $\dfrac{4-7{,}2+4}{0{,}19}\approx4{,}2$. Sous les 13,8 du quantile 99,9 % d'un $\chi^2$ à 2 degrés de liberté : normal.
  - Point $(2;\,-2)$ : $\dfrac{4+7{,}2+4}{0{,}19}=80$. Très au-dessus du seuil : anomalie.
  - Distance euclidienne au carré : 8 dans les deux cas.
- **Lien avec l'ACP.** La distance au carré se réécrit comme la somme des carrés des scores de l'ACP, chacun divisé par sa variance. Avec toutes les composantes, c'est $d_M^2$ ; avec seulement les $R$ premières, c'est la statistique $T^2$ de [[T² et SPE]].

## En pratique

- **Avoir assez de lignes.** L'estimation de $\Sigma$ demande beaucoup plus de lignes que de capteurs. Avec des capteurs redondants (corrélation proche de 1), $\Sigma$ devient presque non inversible et la distance explose : réduire la dimension ([[PCA]]) ou régulariser avant.
- **Données d'apprentissage normales et d'un seul régime.** Une machine qui a deux régimes de marche (charge faible, charge forte) forme **deux nuages** ; une seule ellipse les couvre tous les deux et laisse passer l'entre-deux. Ajuster une ellipse par régime.
- **Standardiser n'est pas nécessaire pour Mahalanobis**, qui absorbe l'échelle. Les unités (°C, bar) n'ont pas d'influence sur le résultat.
- **Hypothèse gaussienne.** Si la forme du nuage est courbe ou à plusieurs bosses, l'ellipse est un mauvais modèle ; voir [[Isolation Forest]], [[Local Outlier Factor]] ou [[Anomalies multivariées par apprentissage profond]].
- **Dans le temps.** La distance traite chaque ligne seule ; une dérive lente ou une corrélation temporelle demande un suivi par cartes de contrôle ([[Contrôle statistique de procédé (SPC)]]).
- **Quel capteur est en cause ?** La distance ne le dit pas. Décomposer le score par capteur : [[Expliquer une anomalie (contribution des capteurs)]].

## Approches voisines & alternatives

- [[Détection d'outliers multivariée]] — la notion qui range l'enveloppe elliptique avec LOF, Isolation Forest et ECOD.
- [[Détection d'outliers univariée]] — un seuil par capteur : plus simple, mais aveugle aux corrélations.
- [[T² et SPE]] — Mahalanobis dans le sous-espace de l'ACP, plus la distance au sous-espace.
- [[PCA]] — réduire la dimension avant d'inverser la covariance.
- [[PyOD]] — les détecteurs multivariés derrière une même API.
- [[Détection d'anomalies]] — le cadre : types d'anomalies, supervision, seuil.

## Pour aller plus loin

- Mahalanobis (1936), *On the generalised distance in statistics*, Proceedings of the National Institute of Sciences of India 2(1), 49-55 (référence confirmée par recherche, texte non relu) : https://dspace.isical.ac.in/items/dabb573e-3ce2-4bef-add0-04efa29d0317/full
- Rousseeuw, Van Driessen (1999), *A fast algorithm for the minimum covariance determinant estimator*, Technometrics 41(3), 212 (référence reprise de la documentation scikit-learn, texte non relu).
- Documentation scikit-learn, *Novelty and Outlier Detection* (`EllipticEnvelope`, `MinCovDet`) : https://scikit-learn.org/stable/modules/outlier_detection.html (lue)
