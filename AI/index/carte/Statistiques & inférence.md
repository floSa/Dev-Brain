# Statistiques & inférence — carte

> Généré par `AI/scripts/build_carte.py`. Ne pas éditer à la main.
> 56 pages, chacune avec son chemin et une ligne.
> Couvre : Analyse factorielle, Bayésien, Méthodes causales, Probabilités, Tests & estimation.

## Au niveau du dossier
- [[A-B testing|A/B testing]] · notion · `Statistiques & inférence/A-B testing.md` — Expérience contrôlée : on répartit aléatoirement les unités (utilisateurs, sessions) entre une variante A (contrôle) et une variante B (traitement), puis on…
- [[CUPED]] · notion · `Statistiques & inférence/CUPED.md` — Technique de réduction de variance pour les tests A/B : on corrige la métrique de chaque unité avec une covariable mesurée avant l'expérience.
- [[Multi-armed bandits]] · notion · `Statistiques & inférence/Multi-armed bandits.md` — Cadre d'allocation dynamique : à chaque étape on choisit un bras (variante), on observe une récompense, et on réajuste les choix futurs pour maximiser le gain…
- [[Sequential testing]] · notion · `Statistiques & inférence/Sequential testing.md` — Évaluer un test en continu, en regardant les données à mesure qu'elles arrivent, et décider de s'arrêter dès que la preuve est suffisante — sans gonfler…

## Analyse factorielle
- [[Fanalysis]] · brique · `Statistiques & inférence/Analyse factorielle/Fanalysis.md` — Analyses factorielles descriptives (PCA, CA, MCA) avec aides à l'interprétation façon FactoMineR ; dépôt sans commit depuis juin 2018, resté en v0.0.1 —…
- [[Prince]] · brique · `Statistiques & inférence/Analyse factorielle/Prince.md` — Analyse factorielle (PCA, CA, MCA, FAMD, MFA, GPA) en API scikit-learn — fit/transform sur DataFrames pandas.
- [[CA]] · notion · `Statistiques & inférence/Analyse factorielle/CA.md` — Analyse factorielle d'une table de contingence : visualise les associations entre les modalités de deux variables qualitatives.
- [[FAMD]] · notion · `Statistiques & inférence/Analyse factorielle/FAMD.md` — Analyse factorielle pour données mixtes : variables continues et catégorielles dans la même analyse.
- [[GPA]] · notion · `Statistiques & inférence/Analyse factorielle/GPA.md` — Generalized Procrustes Analysis : superpose plusieurs configurations de points décrivant les mêmes individus, pour en extraire une configuration consensus.
- [[HCPC]] · notion · `Statistiques & inférence/Analyse factorielle/HCPC.md` — Hierarchical Clustering on Principal Components : enchaîne une méthode factorielle puis une classification des individus sur les composantes retenues.
- [[MCA]] · notion · `Statistiques & inférence/Analyse factorielle/MCA.md` — Analyse des correspondances appliquée à plusieurs variables qualitatives (questionnaires, enquêtes).
- [[MFA]] · notion · `Statistiques & inférence/Analyse factorielle/MFA.md` — Analyse factorielle de variables structurées en groupes (blocs), chaque groupe pouvant être quantitatif ou qualitatif.
- [[PCA]] · notion · `Statistiques & inférence/Analyse factorielle/PCA.md` — Réduction de dimension linéaire pour variables quantitatives : trouve des axes orthogonaux (composantes principales) qui captent le maximum de variance.
- [[PGA]] · notion · `Statistiques & inférence/Analyse factorielle/PGA.md` — Principal Geodesic Analysis : généralisation de la PCA aux données vivant sur une variété riemannienne (formes, tenseurs de diffusion, matrices SPD, rotations).
- [[Réduction de dimension]] · notion · `Statistiques & inférence/Analyse factorielle/Réduction de dimension.md` — Famille de méthodes qui résument un tableau à beaucoup de variables par quelques axes synthétiques, en perdant le moins d'information possible.

## Bayésien
- [[ArviZ]] · brique · `Statistiques & inférence/Bayésien/ArviZ.md` — Analyse exploratoire et diagnostics des modèles bayésiens, indépendant du moteur — trace plots, R̂, ESS, comparaison LOO/WAIC.
- [[PyMC]] · brique · `Statistiques & inférence/Bayésien/PyMC.md` — Programmation probabiliste en Python — modélisation bayésienne et échantillonnage MCMC (NUTS) sur un backend autodiff (PyTensor).
- [[Stan]] · brique · `Statistiques & inférence/Bayésien/Stan.md` — Inférence bayésienne haute performance : langage de modélisation dédié compilé en C++, échantillonneur NUTS de référence, piloté depuis Python via CmdStanPy.
- [[A priori conjugués]] · notion · `Statistiques & inférence/Bayésien/A priori conjugués.md` — A priori choisi pour que l'a posteriori reste dans la même famille de lois que lui.
- [[Estimation MAP]] · notion · `Statistiques & inférence/Bayésien/Estimation MAP.md` — Estimation ponctuelle bayésienne : prend le mode de la distribution a posteriori — la valeur la plus probable du paramètre une fois les données vues.
- [[Inférence bayésienne]] · notion · `Statistiques & inférence/Bayésien/Inférence bayésienne.md` — Met à jour la probabilité d'une hypothèse (ou d'un paramètre) à mesure que les données s'ajoutent, en combinant une croyance a priori avec la vraisemblance des…
- [[MCMC]] · notion · `Statistiques & inférence/Bayésien/MCMC.md` — Famille d'algorithmes qui échantillonnent une distribution connue seulement à une constante de normalisation près, en construisant une chaîne de Markov dont la…
- [[Modèles graphiques probabilistes]] · notion · `Statistiques & inférence/Bayésien/Modèles graphiques probabilistes.md` — Représenter une loi de probabilité jointe sur plusieurs variables par un graphe : les nœuds sont les variables, l'absence d'arête dit une indépendance…
- [[Monte Carlo et inférence variationnelle]] · notion · `Statistiques & inférence/Bayésien/Monte Carlo et inférence variationnelle.md` — Deux familles pour la même tâche : calculer une espérance ou une loi a posteriori quand l'intégrale n'a pas de forme fermée.

## Méthodes causales
- [[CausalImpact]] · brique · `Statistiques & inférence/Méthodes causales/CausalImpact.md` — Effet causal d'une intervention par séries temporelles structurelles bayésiennes — contrefactuel prédit depuis des séries de contrôle.
- [[Diff-in-Diff]] · notion · `Statistiques & inférence/Méthodes causales/Diff-in-Diff.md` — Méthode quasi-expérimentale : estimer l'effet d'un traitement en comparant l'évolution d'un groupe traité à celle d'un groupe témoin, avant et après…
- [[Découverte causale]] · notion · `Statistiques & inférence/Méthodes causales/Découverte causale.md` — Retrouver un graphe causal (qui cause quoi) à partir de données, au lieu de le dessiner à la main avant d'estimer un effet comme le fait l'Inférence causale.
- [[Inférence causale]] · notion · `Statistiques & inférence/Méthodes causales/Inférence causale.md` — Estimer l'effet d'une cause sur un résultat — pas une corrélation, mais ce qui se passerait si l'on intervenait sur la variable de traitement.
- [[Modélisation d'uplift]] · notion · `Statistiques & inférence/Méthodes causales/Modélisation d'uplift.md` — Estimer, pour chaque individu, l'effet incrémental d'une action (une offre, un message, un traitement) : ce qui change à cause de l'action, pas ce qui arrive…

## Probabilités
- [[Chaînes de Markov]] · notion · `Statistiques & inférence/Probabilités/Chaînes de Markov.md` — Processus aléatoire dont l'état futur ne dépend que de l'état présent, pas du chemin parcouru pour y arriver — la propriété de Markov (« sans mémoire »).
- [[Inégalités de concentration]] · notion · `Statistiques & inférence/Probabilités/Inégalités de concentration.md` — Bornent la probabilité qu'une variable aléatoire — souvent une moyenne — s'écarte de son espérance, sans attendre que $n \to \infty$.
- [[Loi des grands nombres]] · notion · `Statistiques & inférence/Probabilités/Loi des grands nombres.md` — La moyenne empirique d'observations indépendantes et de même loi converge vers l'espérance théorique quand le nombre d'observations grandit.
- [[Modèles de Markov cachés et filtre de Kalman]] · notion · `Statistiques & inférence/Probabilités/Modèles de Markov cachés et filtre de Kalman.md` — Deux modèles pour la même situation : un état qu'on ne voit pas évolue dans le temps, et on n'en observe que des mesures bruitées.
- [[Mouvement brownien]] · notion · `Statistiques & inférence/Probabilités/Mouvement brownien.md` — Processus stochastique à temps continu et trajectoires continues, dont les incréments sont indépendants, stationnaires et gaussiens.
- [[Processus de Poisson]] · notion · `Statistiques & inférence/Probabilités/Processus de Poisson.md` — Modèle de comptage d'événements qui surviennent indépendamment, à taux constant $\lambda$, sans coordination entre eux.
- [[Théorie des valeurs extrêmes]] · notion · `Statistiques & inférence/Probabilités/Théorie des valeurs extrêmes.md` — Branche des probabilités et de la statistique qui modélise le comportement des valeurs les plus grandes (ou les plus petites) d'un échantillon : le maximum…
- [[Théorème central limite]] · notion · `Statistiques & inférence/Probabilités/Théorème central limite.md` — La somme (ou la moyenne) de variables aléatoires indépendantes et de même loi, recentrée et normalisée, tend vers une loi normale — quelle que soit la loi de…

## Tests & estimation
- [[lifelines]] · brique · `Statistiques & inférence/Tests & estimation/lifelines.md` — Analyse de survie en Python pur — estimateurs non paramétriques (Kaplan-Meier, Nelson-Aalen) et modèles de régression (Cox à risques proportionnels, AFT) pour…
- [[pingouin]] · brique · `Statistiques & inférence/Tests & estimation/pingouin.md` — Tests statistiques simples et lisibles, tailles d'effet incluses — la clarté plutôt que l'exhaustivité, sur pandas.
- [[scipy.stats]] · brique · `Statistiques & inférence/Tests & estimation/scipy.stats.md` — Socle bas niveau des tests statistiques et lois de probabilité en Python — p-values, distributions, corrélations, au sein de SciPy.
- [[statsmodels]] · brique · `Statistiques & inférence/Tests & estimation/statsmodels.md` — Modélisation statistique façon R en Python — GLM, séries temporelles, tests de spécification avec tables de résultats détaillées.
- [[Analyse de puissance]] · notion · `Statistiques & inférence/Tests & estimation/Analyse de puissance.md` — Relie quatre quantités d'un test : taille d'effet, taille d'échantillon, seuil α et puissance.
- [[Analyse de survie]] · notion · `Statistiques & inférence/Tests & estimation/Analyse de survie.md` — Modéliser le temps jusqu'à un événement (décès, panne, churn, conversion), pas seulement son occurrence.
- [[Bootstrap]] · notion · `Statistiques & inférence/Tests & estimation/Bootstrap.md` — Estime la distribution d'échantillonnage d'une statistique en rééchantillonnant l'échantillon lui-même, avec remise.
- [[Correction des tests multiples]] · notion · `Statistiques & inférence/Tests & estimation/Correction des tests multiples.md` — Lancer beaucoup de tests gonfle mécaniquement les faux positifs : il faut ajuster les p-values (ou le seuil) pour le contrôler.
- [[Facteurs de Bayes et tailles d'effet]] · notion · `Statistiques & inférence/Tests & estimation/Facteurs de Bayes et tailles d'effet.md` — Deux réponses à une même limite de la p-valeur : elle dit si les données sont peu compatibles avec l'hypothèse nulle, ni de combien l'effet s'écarte de zéro…
- [[Intervalles de confiance]] · notion · `Statistiques & inférence/Tests & estimation/Intervalles de confiance.md` — Intervalle calculé sur l'échantillon, censé contenir le vrai paramètre (moyenne, proportion…) avec un niveau de confiance donné.
- [[MANOVA et tests multivariés]] · notion · `Statistiques & inférence/Tests & estimation/MANOVA et tests multivariés.md` — Généralisent le test t / l'ANOVA à plusieurs variables réponses simultanées : on teste si des groupes diffèrent sur un vecteur de moyennes.
- [[Maximum de vraisemblance]] · notion · `Statistiques & inférence/Tests & estimation/Maximum de vraisemblance.md` — Estime les paramètres d'un modèle en cherchant la valeur qui rend les données observées les plus probables.
- [[Modèles à effets mixtes]] · notion · `Statistiques & inférence/Tests & estimation/Modèles à effets mixtes.md` — Régression pour des observations groupées ou répétées (élèves dans des écoles, mesures répétées sur un patient, capteurs sur des machines) : les lignes d'un…
- [[Prédiction conforme]] · notion · `Statistiques & inférence/Tests & estimation/Prédiction conforme.md` — Transformer n'importe quel modèle (une régression, un réseau, un LLM) en un générateur d'ensembles de prédiction : un intervalle pour une cible continue, un…
- [[Test du khi-deux]] · notion · `Statistiques & inférence/Tests & estimation/Test du khi-deux.md` — Famille de tests sur données catégorielles : compare des effectifs observés à des effectifs attendus.
- [[Test t et ANOVA]] · notion · `Statistiques & inférence/Tests & estimation/Test t et ANOVA.md` — Tests paramétriques de comparaison de moyennes : test t pour 2 groupes, ANOVA pour 3 groupes ou plus.
- [[Tests d'hypothèse]] · notion · `Statistiques & inférence/Tests & estimation/Tests d'hypothèse.md` — Démarche pour décider si un effet observé sur un échantillon est réel ou attribuable au seul hasard d'échantillonnage.
- [[Tests non paramétriques]] · notion · `Statistiques & inférence/Tests & estimation/Tests non paramétriques.md` — Tests qui ne supposent pas de forme de distribution (notamment pas de normalité).
- [[Comparatif - Outils stats]] · comparatif · `Statistiques & inférence/Tests & estimation/Comparatif - Outils stats.md` — l'étage — une fonction de test, un objet modèle avec ses diagnostics, ou un modèle bayésien qu'on écrit soi-même — puis sur la question posée : tester…
