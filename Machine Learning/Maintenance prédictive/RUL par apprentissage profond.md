---
role: notion
nom: RUL par apprentissage profond
alias: [RUL deep learning, Deep RUL, Pronostic par apprentissage profond]
categorie: ml/maintenance
domaines: [data-sci, ml-eng]
tags: [rul, predictive-maintenance, deep-learning, timeseries, cnn, transformers]
---

# RUL par apprentissage profond

## Aperçu

- Estimer la durée de vie résiduelle avec un réseau qui lit une **fenêtre glissante** de capteurs et rend un nombre : CNN 1D, LSTM, puis Transformers. Le cadre, la définition du RUL et le score asymétrique sont dans [[Maintenance prédictive et RUL]] ; cette page traite ce qui est propre au réseau.
- Presque toute la littérature s'appuie sur **un seul jeu simulé**, C-MAPSS, avec un protocole que chaque article règle à sa façon. Les classements mélangent donc des chiffres qui ne se comparent pas : c'est la limite principale.

## Concepts clés

### Le cadrage : une fenêtre, un RUL

- Une fenêtre de $T_w$ cycles sur $k$ capteurs est l'entrée ; le RUL du **dernier** cycle est la cible, avec un pas de 1. À l'évaluation, seule la dernière fenêtre de chaque moteur de test compte : ces moteurs sont tronqués avant la panne et leur RUL vrai est fourni (Babu et al. ; Zhang et al.).
- **CNN 1D** : Babu, Zhao et Li (DASFAA 2016) se disent les premiers à l'appliquer au RUL : convolution et pooling le long du temps, deux étages puis un perceptron, perte quadratique. Fenêtre de 15 cycles, imposée par le moteur de test le plus court (15 cycles). Li, Ding et Sun (RESS, 2018) vont plus profond ; Javanmardi et Hüllermeier, qui réutilisent leur réseau, le décrivent : quatre couches de convolution identiques, une cinquième à un filtre, une couche dense de 100 neurones, dropout 0,5, Adam. Fenêtres de 30, 20, 30 et 15 sur FD001 à FD004.
- **LSTM** : Zheng, Ristovski, Farahat et Gupta (ICPHM 2017) reprochent aux approches à fenêtre aplatie d'ignorer l'ordre de la séquence. Avant eux, Heimes (PHM 2008) avait résolu le défi PHM08 par un réseau récurrent (deuxième du concours).
- **Transformers** : DAST (Zhang, Song, Li, IEEE TIM 2022), encodeur-décodeur fondé sur la seule auto-attention ([[Self-attention]], [[Transformer architectures]]), avec **deux encodeurs parallèles**, l'un sur les capteurs, l'autre sur les pas de temps. Fenêtre de 40 cycles (FD001, FD003) ou 60 (FD002, FD004), 14 capteurs sur 21, moyenne de 10 exécutions.
- Le réseau lui-même : [[CNN]], [[Perceptron et MLP]]. Le LSTM : [[LSTM et réseaux récurrents]].

### L'étiquette plateau-puis-linéaire

- **Idée** : $y_t=\min(R_{\max},\,T_{\text{panne}}-t)$. La cible reste à $R_{\max}$ tant que le moteur est sain, puis décroît d'un cycle par cycle. Le réseau n'invente plus de pente là où rien ne se dégrade.
- **Qui l'a introduite** : Babu et al. l'attribuent à Heimes (2008), Javanmardi et Hüllermeier aussi. Le texte de Heimes n'a pas pu être consulté : la valeur qu'il retient est **non vérifiée**. Babu écrit que la valeur maximale est choisie d'après les observations et diffère selon le jeu.
- **La valeur 125** : DAST la fixe « en suivant Zheng et al. » ; Javanmardi et Hüllermeier « comme » Li et al. Deux filiations, une valeur d'origine à confirmer dans des articles non lus ici.
- **Un choix lourd** : Babu note que le plateau évite de surestimer le RUL et suit l'idée qu'une dégradation ne démarre qu'après un certain usage, alors que l'étiquette linéaire suit la définition stricte du RUL mais suppose une santé qui baisse linéairement. Dans l'audit de Gupta (préimpression, 2026-09), le plafond est, sur les sous-jeux multirégimes, le deuxième ou le premier facteur de variance du RMSE : 54,9 % sur FD002, 41,7 % sur FD004 (descriptif, graines appariées).

### Score et RMSE

- Le score asymétrique est défini dans [[Maintenance prédictive et RUL]]. Babu en liste trois défauts : un seul retard fort domine la somme ; l'horizon de pronostic est ignoré ; il **favorise les modèles qui sous-estiment** le RUL. D'où le RMSE rapporté en parallèle.
- La somme croît avec le nombre d'unités de test (100 moteurs sur FD001, 248 sur FD004) : Wang et al. (2025) rapportent un score **moyen**.

### Incertitude

- **Ensembles et MC dropout** : le benchmark de Basora, Viens, Arias Chao et Olive (RESS 253, 2025) compare réseau hétéroscédastique, réseaux bayésiens variationnels, MC dropout (dropout actif à l'inférence) et ensembles profonds sur 5 sous-jeux de N-CMAPSS (54 unités : 33 en développement, 21 en test). Aucune méthode ne domine ; ensembles et MC dropout donnent une incertitude plus **prudente** que les réseaux bayésiens ; le réseau hétéroscédastique, plus simple, tient bien ; **aucune n'est robuste hors distribution** (réseaux bayésiens et hétéroscédastiques : faible précision avec excès de confiance) ; aucune métrique unique ne classe les méthodes.
- **Conformal** : Javanmardi et Hüllermeier (IJPHM 14(2), 2023) enveloppent un CNN et un gradient boosting dans des variantes de prédiction conforme (fractionnée, par régression quantile, pondérée pour données non échangeables). La calibration prend 10 % des **unités** d'entraînement, pas des fenêtres ; 15 tirages ; couvertures nominales de 75 à 90 %. Les non échangeables couvrent mieux en moyenne, la régression quantile donne les intervalles les plus étroits, et les intervalles se resserrent près de la panne. Les auteurs rappellent que l'échangeabilité se viole facilement sur des données ordonnées. Cadre : [[Prédiction conforme]].
- **Censure** : Noot, Martin et Birmele (IJPHM 16(2), 2025) adaptent DAST et un LSTM aux données censurées, avec intervalles conformes (C-MAPSS, N-CMAPSS). Passerelle vers [[RUL par analyse de survie]].

## Les maths, simplement

- **Mélange d'ensemble** (Basora et al.) : $M$ réseaux rendent $(\mu_m,\sigma_m^2)$ ; $\hat\mu=\frac1M\sum_m\mu_m$ et $\hat\sigma^2=\frac1M\sum_m(\sigma_m^2+\mu_m^2)-\hat\mu^2$ : variance aléatoire moyenne plus désaccord entre membres.
- **Perte symétrique** : l'erreur quadratique (Babu) ou le RMSE (DAST) n'apprend pas l'asymétrie du score, qui ne s'ajoute qu'à l'évaluation, sauf perte dédiée.

## En pratique

- **Découper par unité, jamais par fenêtre.** Deux fenêtres voisines d'un moteur sont presque identiques : les répartir des deux côtés donne de la fuite ([[Data leakage]]). Shamim et al. (préimpression, 2026-07), sur un modèle multitâche diagnostic et RUL (C-MAPSS, IMS, UCI Hydraulic), voient un découpage naïf faire passer l'exactitude de classification d'un niveau réel de 20 à 60 % à 99,9 %. Le chiffre concerne la classification, pas le RMSE ; le mécanisme est le même.
- **Normaliser sur l'entraînement seul**, régime par régime sur FD002 et FD004. Gupta : la normalisation par condition abaisse le RMSE dans toutes les cellules appariées de FD002 et FD004 (écart moyen -4,39 et -7,40), et réajuster modèle et normaliseur sur entraînement plus validation le déplace de -1,119 à -0,206. Dans son banc d'essai (MLP, CNN, LSTM compacts), cet effet dépasse l'écart entre DAST et le meilleur modèle comparé sur FD001 (11,43 contre 11,78).
- **Écrire le protocole avec le résultat** : plafond, fenêtre, capteurs, normalisation, graines, jeu de réglage. DAST ne mentionne aucun jeu de validation et teste des fenêtres de 30 à 70 en indiquant seulement que 40 (FD001, FD003) et 60 (FD002, FD004) sont les meilleures ; sur quel jeu, le texte ne le dit pas.
- **RMSE et score ensemble**, avec la distribution des erreurs tardives ([[Regression metrics]]). Hors benchmark, le cadre temporel est celui de [[Walk-forward CV]].

## Résultats publiés, et ce qu'ils valent

- Babu et al. (2016), RMSE du CNN sur FD001 à FD004 : 18,45 / 30,29 / 19,82 / 29,16, contre 20,96 / 42,00 / 21,05 / 45,35 pour la régression à vecteurs de support. Score sur le test PHM08 : 2056 contre 15886 pour cette dernière.
- Zhang et al. (2022), DAST : RMSE 11,43 / 15,25 / 11,32 / 18,36 (moyenne 14,09), score 203,15 / 924,96 / 154,92 / 1490,72. Leur table reprend le CNN de Li et al. à 12,61 / 22,36 / 12,64 / 23,31.
- **Ces deux jeux de chiffres ne se comparent pas** : fenêtre, capteurs, plafond et normalisation diffèrent. Gupta (grille de 1080 exécutions) trouve que le sous-jeu explique à lui seul 60,8 % de la variance du RMSE, et que plafond et normalisation pèsent plus que l'architecture sur les sous-jeux multirégimes : l'évidence est plus solide pour la sensibilité au protocole que pour le classement fin des modèles.
- Des RMSE plus bas circulent, par exemple 9,989 sur FD001 pour un empilement de quatre réseaux et d'un méta-modèle XGBoost (Hossain et al., arXiv, 2026-08) : protocole **non audité ici**.

## Limites : simulé n'est pas réel

- **C-MAPSS est une simulation.** Saxena et al. (2008) imposent un taux de perte de débit et d'efficacité exponentiel, un indice de santé égal au minimum de marges, et la panne quand il atteint zéro. Basora et al. ajoutent qu'elle ne simule que le vol de croisière, avec un début de dégradation indépendant du profil d'usage. N-CMAPSS (Arias Chao et al., *Data* 6(1), 2021) simule des vols complets à 1 Hz, au prix de 14 Go.
- Gupta écrit que C-MAPSS « peut ne pas capturer » bruit, interventions de maintenance, dérive de capteurs et hétérogénéité de flotte, et qu'une bonne performance de benchmark ne prouve pas qu'un modèle soit déployable.
- Vollert et Theissler (ETFA 2021) retiennent comme défis l'interprétabilité, l'incertitude et l'adaptation de domaine. En exploitation, peu de moteurs vont jusqu'à la panne (Wang et al.) : voir [[Maintenance prédictive avec peu de pannes]]. Jeux plus proches du terrain : [[Jeux de données PHM]].

## Approches voisines & alternatives

- [[RUL par analyse de survie]] — une loi de durée de vie avec censure, au lieu d'une valeur ; seul cadre qui exploite les unités non menées jusqu'à la panne.
- [[Indicateurs de santé]] — résumer l'état avant de prédire.
- [[Maintenance prédictive avec peu de pannes]] — transfert et simulation quand les trajectoires manquent.
- [[Politique de maintenance et coût]] — transformer un RUL et son incertitude en décision.
- [[Time series feature engineering]] — la voie sans réseau.
- [[Régression quantile]], [[Calibration]], [[Prédiction conforme]] — les briques d'un intervalle fiable.
- [[LSTM et réseaux récurrents]] — le réseau de séquence derrière les modèles récurrents de cette page : cellule, portes, gradient.
- [[Adaptation de domaine]] — passer d'une flotte ou d'un régime à l'autre sans étiquettes de panne côté cible.
- [[Maintenance prédictive]] — le dossier.

## Pour aller plus loin

- Babu, Zhao, Li (2016), DASFAA. DOI : https://doi.org/10.1007/978-3-319-32025-0_14
- Li, Ding, Sun (2018), *Remaining useful life estimation in prognostics using deep convolution neural networks*, RESS 172. DOI : https://doi.org/10.1016/j.ress.2017.11.021
- Zheng, Ristovski, Farahat, Gupta (2017), *Long Short-Term Memory Network for Remaining Useful Life estimation*, ICPHM. DOI : https://doi.org/10.1109/icphm.2017.7998311
- Zhang, Song, Li (2022), *Dual Aspect Self-Attention based on Transformer for Remaining Useful Life Prediction*, IEEE TIM 71. DOI : https://doi.org/10.1109/TIM.2022.3160561 — arXiv : https://arxiv.org/abs/2106.15842
- Heimes (2008), *Recurrent neural networks for remaining useful life estimation*, PHM. DOI : https://doi.org/10.1109/PHM.2008.4711422
- Saxena, Goebel, Simon, Eklund (2008), *Damage propagation modeling for aircraft engine run-to-failure simulation*, PHM. DOI : https://doi.org/10.1109/PHM.2008.4711414
- Arias Chao, Kulkarni, Goebel, Fink (2021), *Aircraft Engine Run-to-Failure Dataset under Real Flight Conditions*, Data 6(1), 5.
- Javanmardi, Hüllermeier (2023), IJPHM 14(2). DOI : https://doi.org/10.36001/ijphm.2023.v14i2.3417 — arXiv : https://arxiv.org/abs/2212.14612
- Basora et al. (2025), RESS 253, 110513. DOI : https://doi.org/10.1016/j.ress.2024.110513
- Noot, Martin, Birmele (2025), IJPHM 16(2). DOI : https://doi.org/10.36001/ijphm.2025.v16i2.4260
- Gupta (2026), *Auditing Operating-Condition Normalization in C-MAPSS Remaining Useful Life Evaluation*, engrXiv. DOI : https://doi.org/10.31224/8145
- Shamim et al. (2026), arXiv : https://arxiv.org/abs/2607.16493
- Vollert, Theissler (2021), ETFA. DOI : https://doi.org/10.1109/ETFA45728.2021.9613682
- Wang et al. (2025), arXiv : https://arxiv.org/abs/2510.03604 ; Hossain et al. (2026), arXiv : https://arxiv.org/abs/2608.27940
