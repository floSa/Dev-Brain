---
role: notion
nom: Expliquer une anomalie (contribution des capteurs)
alias: [Attribution d'anomalie, Localisation d'anomalie, Contribution plots, Anomaly attribution, Explication d'anomalie, Bavure des contributions]
categorie: ml/anomalie
domaines: [data-sci, ml-eng, mlops]
tags: [anomaly-detection, explainability, timeseries]
---

# Expliquer une anomalie (contribution des capteurs)

## Aperçu

- Un détecteur multivarié rend un **score** pour un instant ou une fenêtre. L'opérateur de ligne pose la question suivante : **quel capteur ?** Expliquer une anomalie, c'est répartir l'écart entre les $m$ variables et rendre une liste classée.
- Les méthodes se rangent en deux familles : celles que le détecteur porte en lui (erreur de reconstruction par canal, contributions de l'ACP, décomposition de Mahalanobis) et celles qui s'appliquent à n'importe quel détecteur (SHAP, gradients, occlusion, contre-factuels).
- La liste répond à « où le détecteur voit-il l'écart ? », pas à « pourquoi la machine s'est-elle écartée ? ». Le capteur qui dévie le plus peut être un simple symptôme. Le passage à la cause est l'objet de [[Cause racine d'une anomalie]].

## Concepts clés

### Du score au vecteur de contributions

- Un détecteur donne $s(x)\in\mathbb{R}$. Une explication est un vecteur $a(x)\in\mathbb{R}^m$ dont chaque composante dit combien le capteur $j$ pèse dans $s(x)$. Le but opérationnel est un **top-$k$** de capteurs à regarder en premier.
- Deux fidélités à ne pas confondre : être fidèle **au détecteur** (ce qui a fait monter le score) et être fidèle **au procédé** (ce qui s'est réellement passé). Toutes les méthodes ci-dessous visent la première ; la seconde exige un cadre causal.

### Attributions que le détecteur porte en lui

- **Erreur de reconstruction ou de prévision par canal.** Hundman et al. (KDD 2018) entraînent un modèle LSTM **par canal de télémétrie** ; ils notent que cela donne une traçabilité jusqu'au canal, les anomalies de bas niveau pouvant ensuite être agrégées par groupes et par sous-systèmes. Le score reste unique par canal : aucune attribution inter-canaux n'est calculée.
- **Vraisemblance factorisée.** OmniAnomaly (Su et al., KDD 2019) décompose le score en somme de termes par dimension, parce que la loi de reconstruction est gaussienne à covariance diagonale. Les dimensions sont classées par contribution croissante de $\log p$ ; l'article précise que cette factorisation ne tient que sous cette hypothèse. Détecteurs [[Autoencodeurs]] et apparentés : voir [[Anomalies multivariées par apprentissage profond]].
- **Cartes de contrôle multivariées (SPC/ACP).** Le modèle [[PCA]] d'un fonctionnement normal donne deux statistiques : $T^2$ de Hotelling (écart **dans** le sous-espace du modèle) et SPE ou $Q$ (écart **hors** du sous-espace). Westerhuis, Gurden et Smilde (2000) généralisent les **contribution plots** : une barre par variable, avec des limites de contrôle propres à chaque contribution, calculées sur le fonctionnement normal. Contexte général des cartes dans [[Contrôle statistique de procédé (SPC)]].
- **Mahalanobis décomposée.** La distance de [[Détection d'outliers multivariée]] se scinde en termes par variable (décomposition de Mason, Tracy et Young, 1995, citée ici d'après des descriptions secondaires). Un terme non conditionnel grand dit « la variable est hors plage seule » ; un terme conditionnel grand dit « elle a rompu sa corrélation avec les autres ».
- **Contribution par reconstruction** (Alcala et Qin, 2009) : retirer l'écart le long de la direction d'une variable et voir de combien l'indice baisse. Article non ouvert ; son principe et sa limite viennent d'un résumé.

### Attributions agnostiques du détecteur

- **SHAP sur le score.** La cible expliquée est la fonction $s$, pas une étiquette. Pour une [[Isolation Forest]], [[SHAP]] propose TreeSHAP, polynomial sur les arbres (Lundberg et al., 2020). La note de version 0.32.0 de SHAP annonce la prise en charge de l'Isolation Forest de scikit-learn ; la page de documentation de `TreeExplainer` ne la cite pas dans sa liste, donc à tester avant de s'y fier.
- **DIFFI** (Carletti, Terzi, Susto) : importance par variable propre à l'Isolation Forest, locale et globale, fondée sur les profondeurs d'isolement. Les auteurs l'évaluent sur jeux synthétiques et réels, face à d'autres techniques (résumé lu seulement).
- **SHAP sur des modèles de reconstruction.** Antwarg et al. appliquent SHAP à un autoencodeur et visualisent les variables qui contribuent à l'anomalie et celles qui la compensent (évaluation préliminaire, d'après le résumé). Takeishi (2019) calcule les valeurs de Shapley des erreurs de reconstruction d'une ACP en s'appuyant sur sa formulation probabiliste, pour que les variables corrélées soient traitées correctement.
- **Gradients.** Integrated Gradients appliqué au score ou à l'erreur de reconstruction : voir [[Attribution par gradient]] et [[Captum]]. La baseline doit être un état normal, pas zéro.
- **Occlusion / perturbation.** Remplacer ou masquer un capteur, mesurer la baisse du score. Simple, valable pour tout détecteur, mais la perturbation peut créer une entrée hors distribution.
- **Contre-factuels.** Chercher le plus petit changement qui ramène l'entrée dans le normal, idée de Wachter, Mittelstadt et Russell (2017) pour des décisions automatisées. Pour un capteur, la réponse est « quelle correction minimale ramène le score sous le seuil ».

### Limites

- **Bavure (*smearing*).** Dans l'exemple de Westerhuis et al., deux capteurs corrélés (une température et une pression) sautent, un troisième reste sur sa consigne ; les résidus du troisième deviennent pourtant grands. Le modèle compresse tout en peu de scores, donc l'information se répand sur les variables voisines. Des résumés d'articles ultérieurs (non ouverts) disent que les contributions des variables saines en sortent exagérées au point de franchir leur limite, et que la méthode par reconstruction garantit un diagnostic correct pour un défaut de capteur unique de forte amplitude, sans supprimer la bavure en général.
- **Les capteurs corrélés se partagent la faute.** Une valeur de Shapley répartit entre variables redondantes : par symétrie, deux capteurs jumeaux reçoivent chacun la moitié de l'importance. Le choix de la fonction de valeur change la réponse : Janzing et al. soutiennent l'espérance non conditionnelle (interventionnelle), Takeishi retient la loi conditionnelle de l'ACP probabiliste. Les deux choix diffèrent, et rien ne les tranche d'avance. Kumar et al. (ICML 2020) recensent plus largement des problèmes mathématiques et d'adéquation aux besoins humains des explications fondées sur Shapley (résumé lu seulement).
- **Perturbations hors distribution.** Mishra et al. (2026) reprochent à SHAP et Integrated Gradients de supposer l'indépendance des variables, donc de fabriquer des états qu'aucun procédé ne produit. Ils proposent des références **conditionnelles** : des états normaux proches du contexte de l'anomalie.
- **Expliquer la détection n'est pas expliquer la cause.** Garg et al. (2021) le constatent sur leur propre mesure : sur certains événements, d'autres canaux que les causes d'origine sont affectés et se retrouvent diagnostiqués comme causes. Un symptôme en aval bat souvent la cause à l'amplitude. Voir [[Cause racine d'une anomalie]].
- **Si le défaut est univarié, tout classement marche.** Pinet et al. (2026) trouvent, sur huit jeux publics, qu'aucune rupture inter-canaux ne survient sans écart univarié, et que sur six jeux au moins la moitié des anomalies étiquetées dévient en univarié sur 89 à 100 % de leurs instants. Lecture de cette page (non vérifiée dans l'article) : ces jeux discriminent mal les méthodes d'attribution, car une simple erreur par canal suffit.

## Les maths, simplement

- **ACP.** Avec $x$ centré, $P$ la matrice des $R$ axes retenus, $\Lambda=\mathrm{diag}(\lambda_1,\dots,\lambda_R)$ les variances des scores $t=P^\top x$ : $T^2=t^\top\Lambda^{-1}t$ et $\mathrm{SPE}=\lVert x-PP^\top x\rVert^2$. Contribution de la variable $j$ au SPE : $c^{Q}_j=e_j^2$ avec $e=(I-PP^\top)x$ (Westerhuis et al., éq. 6). Contribution à $T^2$ : $c^{T}_j=x_j\,[P\Lambda^{-1}P^\top x]_j$, de somme $T^2$ ; elle peut être négative (Westerhuis et al. discutent ce cas).
- **Origine de la bavure** (calcul de cette page). Un défaut $\delta$ sur la seule variable $k$ donne $e_j=e^{0}_j-\delta\,(PP^\top)_{jk}$ pour $j\ne k$. Le terme est non nul dès que $j$ et $k$ ont des chargements communs, c'est-à-dire dès qu'ils sont corrélés dans le modèle.
- **Mahalanobis en chaîne.** Pour une loi gaussienne centrée : $d^2(x)=\sum_{j=1}^{m}\dfrac{\big(x_j-\mathbb{E}[x_j\mid x_{<j}]\big)^2}{\mathrm{Var}(x_j\mid x_{<j})}$. Chaque terme est un résidu standardisé de $x_j$ prédit par les variables précédentes. La décomposition dépend de l'ordre des variables.
- **Valeur de Shapley d'un capteur.** $\phi_j(x)=\sum_{S\subseteq M\setminus\{j\}}\dfrac{|S|!\,(m-|S|-1)!}{m!}\,[\,v_x(S\cup\{j\})-v_x(S)\,]$, avec $M$ l'ensemble des capteurs et $v_x(S)=\mathbb{E}[s(x_S,X_{\bar S})]$. L'espérance est marginale (les capteurs hors de $S$ tirés indépendamment) ou conditionnelle ($X_{\bar S}\mid X_S=x_S$). Les $\phi_j$ somment à $s(x)-\mathbb{E}[s(X)]$. Le calcul exact coûte $2^m$ évaluations ; TreeSHAP l'évite pour les arbres.
- **Contre-factuel.** $\min_{\delta}\ \lVert\delta\rVert_0\ \text{(ou }\lVert\delta\rVert_1)$ sous $s(x+\delta)\le\tau$. Les capteurs où $\delta_j\ne0$ forment l'explication.
- **HitRate@P%.** Avec $GT_t$ les dimensions étiquetées fautives et $AS_t$ la liste classée : $\mathrm{HitRate@}P\% = \dfrac{|GT_t\cap \mathrm{top}_{\lfloor P\%\cdot|GT_t|\rfloor}(AS_t)|}{|GT_t|}$, $P\in\{100,150\}$ (Su et al.). Si 2 dimensions sont fautives, le 150 % regarde le top 3.

## En pratique

- **Normaliser l'erreur par canal** avant de classer (par l'écart-type de l'erreur sur du normal vérifié) : sans cela, un capteur de forte amplitude gagne toujours. Pratique usuelle, non sourcée ici.
- **Attribuer sur l'événement, pas sur l'instant** : agréger la contribution sur l'intervalle de l'alerte, après regroupement des alertes consécutives ([[Score et seuil d'alerte]]).
- **Regrouper les capteurs redondants** ou voisins (même sous-système) avant d'attribuer. ShaTS (Franco de la Peña et al., 2025) applique le même principe aux séries : il groupe les variables à l'avance pour que les valeurs de Shapley respectent les dépendances temporelles, et vise les capteurs, actionneurs et processus touchés sur SWaT (résumé lu seulement).
- **Montrer la trajectoire du capteur désigné avec sa trajectoire normale.** Westerhuis et al. recommandent cette confirmation visuelle, qui rassure ingénieurs et opérateurs et indique aussi le type d'écart (dérive lente, saut).
- **Choisir la méthode la plus simple qui tient.** Garg et al. trouvent qu'un autoencodeur univarié entièrement connecté avec un score gaussien dynamique est efficace en détection **et** en diagnostic, face à des modèles plus complexes.
- **Contrôler la méthode sur des défauts injectés** : rejouer sur du normal un saut ou une dérive posés à la main sur un capteur connu, et mesurer le HitRate. Recommandation de cette page, non sourcée.
- **Mesurer la stabilité des explications** : deux anomalies de même type doivent donner des listes proches. Exathlon l'évalue sous le nom de concordance, plus difficile à atteindre que la stabilité pour les trois méthodes testées.

### Évaluer une explication

- **Étiquettes par dimension.** Dans SMD (Su et al.), les anomalies et leurs dimensions fautives sont étiquetées par des experts du domaine d'après des rapports d'incident ; le dépôt fournit `interpretation_label`. SMAP et MSL n'ont **aucune** vérité terrain d'interprétation (Su et al.). Sur SMD, OmniAnomaly rapporte HitRate@100 % = 0,80 et @150 % = 0,89 ; LSTM-VAE 0,50 et 0,62.
- **TranAD** (Tuli et al., VLDB 2022) reprend HitRate et NDCG sur SMD et MSDS seulement ; il annonce détecter 46,3 à 75,3 % des causes selon le jeu.
- **Garg et al.** mesurent HitRate@150 et RC-top-3 (au moins une vraie cause dans le top 3) sur DMDS, SMD, SWaT et WADI : environ 0,95 sur DMDS et SMD, **moins de 0,63** sur SWaT et WADI, avec la réserve ci-dessus sur les canaux affectés sans être causes.
- **Exathlon** (Jacob et al., VLDB 2021) fournit pour chaque anomalie un intervalle de **cause racine** et un intervalle d'**effet étendu**. Il mesure concision, cohérence (stabilité, concordance), exactitude et efficience ; MacroBase, EXstream et LIME y sont comparés. Les explications de MacroBase et d'EXstream ne se généralisent pas à d'autres contextes (autre débit d'entrée).
- **Mishra et al. (2026)** définissent Top-K Recall, un score pondéré par la confiance et un score temporel, et rapportent 53,7 % de rappel top-3 sur SWaT contre 39,3 % pour la meilleure base (ShaTS). Chiffres des auteurs, sans reproduction indépendante ; la source de la vérité terrain n'est pas détaillée dans les sections lues, et certaines attaques donnent un rappel nul.
- **Ne pas comparer les chiffres d'un article à l'autre** : jeux, étiquetages, horizons et nombres de capteurs diffèrent. Voir aussi [[Évaluer une détection d'anomalies]] et [[Jeux de données d'anomalies]].

## Approches voisines & alternatives

- [[Cause racine d'une anomalie]] — l'étape d'après : de la liste de capteurs à la cause ; cadre causal, graphes de procédé, RCA logicielle.
- [[Explicabilité des modèles]] — le cadre général (SHAP, LIME, importance par permutation) ; ici, la cible est un score non supervisé.
- [[SHAP]] et [[Captum]] — les bibliothèques d'attribution les plus citées ; aucune n'est spécifique aux anomalies.
- [[Time series anomaly detection]] et [[TSB-AD]] — la détection ; TSB-AD mesure la qualité du score, pas celle de l'explication.
- [[Score et seuil d'alerte]] — l'alerte que l'explication accompagne.
- [[Types d'anomalies et régimes de supervision]] — une anomalie collective ou contextuelle n'a pas de capteur unique fautif.
- [[Surveillance conditionnelle et modes de défaillance]] — relier les capteurs désignés à un mode de défaillance connu.
- [[Indicateurs de santé]] — résumer des capteurs en une grandeur qui suit une dégradation, au lieu de classer des écarts.

## Pour aller plus loin

- Hundman, Constantinou, Laporte, Colwell, Soderstrom (2018), *Detecting Spacecraft Anomalies Using LSTMs and Nonparametric Dynamic Thresholding*, KDD 2018. arXiv : https://arxiv.org/abs/1802.04431
- Su, Zhao, Niu, Liu, Sun, Pei (2019), *Robust Anomaly Detection for Multivariate Time Series through Stochastic Recurrent Neural Network*, KDD 2019 (§4.5 et §5.2.3 pour l'interprétation) : https://netman.aiops.org/wp-content/uploads/2019/08/OmniAnomaly_camera-ready.pdf ; dépôt et jeu SMD : https://github.com/NetManAIOps/OmniAnomaly (licence MIT).
- Tuli, Casale, Jennings (2022), *TranAD*, VLDB 2022. arXiv : https://arxiv.org/abs/2201.07284
- Garg, Zhang, Samaran, Ramasamy, Foo (2021), *An Evaluation of Anomaly Detection and Diagnosis in Multivariate Time Series*, IEEE TNNLS. arXiv : https://arxiv.org/abs/2109.11428
- Jacob, Song, Stiegler, Rad, Diao, Tatbul (2021), *Exathlon: A Benchmark for Explainable Anomaly Detection over Time Series*, VLDB 2021. arXiv : https://arxiv.org/abs/2010.05073
- Mishra, Patil, Schockaert, Stricker, Rambach (2026), *Conditional Attribution for Root Cause Analysis in Time-Series Anomaly Detection*, accepté à ECML PKDD 2026. arXiv : https://arxiv.org/abs/2604.17616
- Pinet, Cumin, Berlemont, Vaufreydaz (2026), *Anomalies in Multivariate Time Series Benchmarks Are Mostly Univariate*. arXiv : https://arxiv.org/abs/2606.02670 (résumé lu seulement).
- Franco de la Peña, Perales Gómez, Fernández Maimó (2025), *ShaTS*, soumis à Information Fusion. arXiv : https://arxiv.org/abs/2506.01450 (résumé lu seulement).
- Westerhuis, Gurden, Smilde (2000), *Generalized contribution plots in multivariate statistical process monitoring*, Chemometrics and Intelligent Laboratory Systems 51:95-114. DOI : https://doi.org/10.1016/S0169-7439(00)00062-9
- Mason, Tracy, Young (1995), *Decomposition of T² for multivariate control chart interpretation*, Journal of Quality Technology 27:99-108 (non ouvert).
- Alcala, Qin (2009), *Reconstruction-based contribution for process monitoring*, Automatica 45(7):1593-1600 (non ouvert ; résumé via recherche) : https://www.sciencedirect.com/science/article/abs/pii/S0005109809001277
- Lundberg et al. (2020), *From local explanations to global understanding with explainable AI for trees*, Nature Machine Intelligence 2(1):56-67. DOI : https://doi.org/10.1038/s42256-019-0138-9 ; arXiv : https://arxiv.org/abs/1905.04610
- Carletti, Terzi, Susto, *Interpretable Anomaly Detection with DIFFI*. arXiv : https://arxiv.org/abs/2007.11117 (résumé lu ; venue non vérifiée).
- Antwarg, Mindlin Miller, Shapira, Rokach, *Explaining Anomalies Detected by Autoencoders Using SHAP*. arXiv : https://arxiv.org/abs/1903.02407 (résumé lu ; venue non vérifiée).
- Takeishi (2019), *Shapley Values of Reconstruction Errors of PCA for Explaining Anomaly Detection*, LMID 2019. arXiv : https://arxiv.org/abs/1909.03495
- Kumar, Venkatasubramanian, Scheidegger, Friedler (2020), *Problems with Shapley-value-based explanations as feature importance measures*, ICML 2020. arXiv : https://arxiv.org/abs/2002.11097
- Janzing, Minorics, Blöbaum (2019), *Feature relevance quantification in explainable AI: A causal problem*. arXiv : https://arxiv.org/abs/1910.13413
- Sundararajan, Taly, Yan (2017), *Axiomatic Attribution for Deep Networks*. arXiv : https://arxiv.org/abs/1703.01365
- Wachter, Mittelstadt, Russell (2018), *Counterfactual Explanations without Opening the Black Box*, Harvard Journal of Law & Technology. arXiv : https://arxiv.org/abs/1711.00399
