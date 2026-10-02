---
role: notion
nom: Score et seuil d'alerte
alias: [Seuil d'alerte, Seuillage des scores d'anomalie, Fatigue d'alerte, Taux de fausses alertes]
categorie: ml/anomalie
domaines: [data-sci, ml-eng, mlops]
tags: [anomaly-detection, thresholding]
---

# Score et seuil d'alerte

## Aperçu

- Un détecteur d'anomalies rend d'abord un **score** continu, pas une décision. Le **seuil** qui le transforme en alerte est un second modèle, qui se règle séparément et qui décide de ce que le détecteur vaut en exploitation.
- Un bon score avec un mauvais seuil donne un système inutilisable : trop d'alertes et plus personne ne les lit, trop peu et la panne passe. Le choix du seuil est un choix de **coût**, pas de statistique pure.

## Concepts clés

### Du score à la décision

- Une technique rend soit un **score** (une liste classée, le seuil étant choisi par l'analyste), soit une **étiquette** (Chandola et al., 2009). Le score garde l'information ; l'étiquette l'a déjà tranchée à la place de l'utilisateur.
- Dans scikit-learn, plus le score est bas, plus l'observation est anormale. `decision_function` vaut `score_samples` moins `offset_` et devient négatif pour un outlier ; `predict` rend $\pm 1$. Le seuil se règle avec `contamination`.
- Pour `LocalOutlierFactor`, avec `contamination` fixé, `offset_` est le percentile correspondant des scores d'entraînement. **Le seuil est donc un quantile de ce qu'on a déjà vu**, ce qui revient à décider d'avance quelle fraction sera signalée. C'est une règle de décision, pas une garantie sur le taux de fausses alertes d'un flux futur (lecture de la documentation, qui ne l'énonce pas ainsi).

### Quantile empirique

- Le plus simple : retenir le quantile $1-q$ des scores d'un jeu de référence. Valable à condition que ce jeu soit propre et représentatif ([[Types d'anomalies et régimes de supervision]]), et que $q\cdot n$ reste assez grand pour que le quantile soit estimable.
- Limite : au-delà du maximum observé, un quantile empirique ne dit plus rien. Descendre à $q=10^{-5}$ avec $10^3$ points de référence est une extrapolation déguisée.

### Valeurs extrêmes (POT)

- Pour atteindre des niveaux de risque très bas, Siffer, Fouque, Termier et Largouët (KDD 2017) appliquent la théorie des valeurs extrêmes aux scores. Le théorème de Pickands-Balkema-de Haan dit que les **excès** au-dessus d'un seuil initial élevé $t$ suivent approximativement une loi de Pareto généralisée (GPD). On ajuste la GPD sur ces excès seuls, puis on en déduit le seuil $z_q$ tel que $P(X>z_q)<q$.
- **SPOT** est la version pour un flux stationnaire. **DSPOT** travaille sur l'écart à une moyenne mobile des $d$ dernières observations « normales », pour absorber une dérive lente.
- Le paramètre principal est le **risque** $q$, censé contrôler les faux positifs. Le seuil initial $t$ est lui-même un quantile élevé. La théorie est détaillée dans [[Théorie des valeurs extrêmes]].
- Côté code : l'implémentation citée par l'article (`github.com/Amossys-team/SPOT`) ne répond plus (404 le 2026-10-02) et la licence d'origine n'a pas pu être vérifiée. Deux repreneurs existent et portent des licences copyleft : `libspot` (C++, par le premier auteur) est en LGPL-3.0 d'après l'API GitHub, `python3-libspot` en GPL-3.0, et `ads-evt` (tiers) en GPLv3. À regarder avant de les embarquer dans une livraison.

### Conformal : un seuil avec garantie

- Bates, Candès, Lei, Romano et Sesia (*Annals of Statistics*, 2023) transforment un score quelconque en **p-valeur conformelle** : pour un point $x$ et $n$ points de calibration, tous des inliers, $\hat u(x)=\dfrac{1+\left|\{i:\hat s(X_i)\le \hat s(x)\}\right|}{n+1}$ (ici $\hat s$ est un score où les petites valeurs signalent l'anormal).
- La garantie est que, pour un inlier, $P(\hat u\le t)\le t$ : la p-valeur est valide en moyenne sur le jeu de calibration. Elle exige que inliers de calibration et de test soient **échangeables** et indépendants ; les outliers de test peuvent, eux, être dépendants entre eux.
- Les p-valeurs de points de test différents sont **dépendantes** (corrélation $1/(n+2)$). La procédure de Benjamini-Hochberg garde malgré cela le contrôle du **FDR** moyen — la proportion attendue d'inliers parmi les points signalés — là où le test global de Fisher devient invalide.
- Le coût : il faut un jeu de calibration d'inliers **séparé** de celui qui entraîne le détecteur. Cadre général dans [[Prédiction conforme]] ; sur une série temporelle, l'échangeabilité est précisément ce qui casse.

### Taux de fausses alertes : l'erreur du taux de base

- Axelsson (2000) montre pourquoi le taux de fausses alarmes domine tout. Hypothèses de son article : $10^6$ enregistrements d'audit par jour, 2 intrusions par jour de 10 enregistrements chacune, soit $P(I)=2\cdot 10^{-5}$.
- Même avec un taux de détection de 1,0 (irréaliste), il faut un taux de fausses alarmes de l'ordre de $10^{-5}$ pour que la probabilité qu'une alarme soit une vraie intrusion, $P(I\mid A)$, atteigne 66 %. À $10^{-3}$ de fausses alarmes — 100 par jour — $P(I\mid A)$ tombe autour de 2 %. Le taux de détection pèse peu, c'est le taux de fausses alarmes qui commande.
- Le raisonnement vaut pour toute anomalie rare : plus l'événement est rare, plus un faible taux de faux positifs suffit à noyer les vrais.

### Fatigue d'alerte

- Source : Poly et al. (*JMIR Medical Informatics*, 2020), revue systématique de 23 études sur les alertes de prescription informatisée. Les taux d'alertes **passées outre** (*override*) vont de 46,2 % à 96,2 %. La part d'overrides jugés appropriés varie fortement selon le type d'alerte (0 à 95 % pour les interactions médicament-médicament, par exemple).
- **Limites de lecture** : le taux d'override est un indicateur indirect de la fatigue, pas sa mesure ; l'étude porte sur la prescription, pas sur la détection d'anomalies industrielle ; les auteurs signalent l'hétérogénéité des études. Le chiffre sert à fixer un ordre de grandeur du phénomène, pas à prédire le taux d'ignorance d'un tableau de bord de maintenance.

## Les maths, simplement

- **Bayes sur l'alerte.** $P(I\mid A)=\dfrac{P(I)\,P(A\mid I)}{P(I)\,P(A\mid I)+\big(1-P(I)\big)\,P(A\mid \lnot I)}$ : la probabilité qu'une alerte soit réelle dépend du taux de base $P(I)$ au moins autant que de la qualité du détecteur. Avec $P(I)=2\cdot10^{-5}$, $P(A\mid I)=1$ et $P(A\mid\lnot I)=10^{-3}$, on obtient environ 2 %.
- **Seuil POT.** $z_q\simeq t+\dfrac{\hat\sigma}{\hat\gamma}\left(\Big(\dfrac{q\,n}{N_t}\Big)^{-\hat\gamma}-1\right)$ : $n$ observations, $N_t$ excès au-dessus de $t$, $(\hat\gamma,\hat\sigma)$ les paramètres de forme et d'échelle de la GPD ajustée.
- **Seuil à coût.** Avec $c_{FA}$ le coût d'une fausse alerte et $c_M$ celui d'une panne manquée, on choisit $\tau$ qui minimise $c_{FA}\cdot \mathrm{FP}(\tau)+c_M\cdot \mathrm{FN}(\tau)$ sur des données d'évaluation. Rarement symétrique.

## En pratique

- **Fixer le budget d'alertes avant le seuil** : combien d'alertes par jour l'équipe d'exploitation peut-elle traiter ? Ce budget, rapporté à la fréquence d'événements attendue, donne un taux de fausses alertes maximal acceptable.
- **Calibrer le seuil sur du normal vérifié**, jamais sur le jeu qui sert à mesurer le détecteur : sinon le chiffre d'évaluation est optimiste ([[Évaluer une détection d'anomalies]], [[Data leakage]]).
- **Un seuil se réexamine** : si la machine, le procédé ou le capteur changent, la distribution des scores bouge ([[Data drift]]). DSPOT et les seuils adaptatifs traitent la dérive lente ; un changement de régime exige un nouvel étalonnage.
- **Regrouper les alertes consécutives en un événement** avant de les compter ou de les envoyer : une anomalie qui dure cinq minutes n'est pas trois cents alertes.
- Un score est parfois mieux **calibré en probabilité** avant d'être seuillé ([[Calibration]]), surtout si plusieurs détecteurs alimentent la même décision.

## Approches voisines & alternatives

- [[Tests d'hypothèse]] — un seuil de détection est un seuil de test ; la p-valeur conformelle en est la version sans hypothèse de loi.
- [[Théorie des valeurs extrêmes]] — le socle mathématique du seuil POT.
- [[Prédiction conforme]] — le cadre général des garanties sans hypothèse de loi, valables à taille finie.
- [[Calibration]] — transformer un score en probabilité.
- [[ROC-AUC & courbe PR]] — résumer un score **sur tous les seuils** ; ne choisit pas le seuil.
- [[Classification metrics]] — précision, rappel, F-mesure : ce qu'un seuil donné produit.
- [[Imbalanced classification]] — le cadre de la classe rare, où le taux de base pèse.
- [[Isolation Forest]], [[Local Outlier Factor]], [[One-Class SVM]] — trois détecteurs dont la sortie est un score, seuillé par `contamination`.
- [[Types d'anomalies et régimes de supervision]] — la contamination et le « normal propre », dont dépend la fiabilité du quantile.

## Pour aller plus loin

- Siffer, Fouque, Termier, Largouët (2017), *Anomaly Detection in Streams with Extreme Value Theory*, KDD '17. DOI : https://doi.org/10.1145/3097983.3098144
- Bates, Candès, Lei, Romano, Sesia (2023), *Testing for outliers with conformal p-values*, Annals of Statistics 51(1). arXiv : https://arxiv.org/abs/2104.08279
- Axelsson (2000), *The Base-Rate Fallacy and the Difficulty of Intrusion Detection*, ACM TISSEC 3(3).
- Poly, Islam, Yang, Li (2020), *Appropriateness of overridden alerts in computerized physician order entry: systematic review*, JMIR Medical Informatics 8(7), e15653. DOI : https://doi.org/10.2196/15653
- Chandola, Banerjee, Kumar (2009), *Anomaly Detection: A Survey*, ACM Computing Surveys 41(3). DOI : https://doi.org/10.1145/1541880.1541882
