---
galaxie: dev
type: service
nom: lifelines
alias: []
pitch: "Analyse de survie en Python pur — estimateurs non paramétriques (Kaplan-Meier, Nelson-Aalen) et modèles de régression (Cox à risques proportionnels, AFT) pour modéliser le temps jusqu'à un événement avec données censurées."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [survival-analysis, regression]
url_docs: https://lifelines.readthedocs.io/
url_repo: https://github.com/CamDavidsonPilon/lifelines
---

# lifelines

## Pourquoi

Bibliothèque d'**analyse de survie** (time-to-event) en Python pur, au-dessus de pandas/numpy. Modélise le temps jusqu'à un événement (décès, churn, panne, conversion) en gérant la **censure** — les sujets dont l'événement n'est pas observé sur la période. Couvre les estimateurs non paramétriques (Kaplan-Meier, Nelson-Aalen), le modèle semi-paramétrique de Cox à risques proportionnels et les modèles paramétriques AFT (Weibull, log-normal…). API homogène proche de statsmodels (`fit`, `predict_*`, `print_summary`), avec tests (log-rank) et diagnostics (vérification de l'hypothèse des risques proportionnels).

## Quand l'utiliser

- Estimer une **courbe de survie** et comparer des groupes (Kaplan-Meier + test du log-rank).
- Modéliser l'effet de covariables sur le risque instantané → régression de **Cox** (risques proportionnels).
- Prévoir une durée de vie ou un temps de panne avec des modèles **paramétriques** (AFT).
- Analyser le **churn** ou la durée de rétention avec données censurées.

## Quand NE PAS l'utiliser

- Survie « machine learning » (Random Survival Forests, gradient boosting de survie) → scikit-survival (hors brain).
- Modélisation statistique générale (GLM, séries temporelles, tests) sans volet survie → [[Dev/Services/statsmodels|statsmodels]].
- Survie bayésienne sur mesure → programmation probabiliste ([[Dev/Services/PyMC|PyMC]], [[Dev/Services/Stan|Stan]]).

## Déploiement & coût

- Bibliothèque Python (`uv add lifelines`), pur Python au-dessus de pandas/numpy/scipy. Rien à héberger.
- Single-node, en mémoire ; taillée pour des jeux de données analytiques courants.
- MIT, gratuit.

## Pièges

- La **censure** doit être encodée correctement (colonne événement 0/1) : l'ignorer biaise tout.
- L'hypothèse des **risques proportionnels** de Cox se vérifie (`check_assumptions`, résidus de Schoenfeld) ; sinon, modèle stratifié ou AFT.
- Le format des données change selon le modèle (durée + événement, ou format long pour covariables variant dans le temps).
- Pas conçu pour le très gros volume ni le GPU : rester sur des tailles raisonnables.

## Alternatives

- Aucune alternative directe répertoriée dans le brain — lib spécialisée en analyse de survie (l'équivalent ML, scikit-survival, n'y figure pas encore).

## Liens

- [[Wiki/Concepts/Analyse de survie|Analyse de survie]] — le concept (Wiki)
- Statistiques connexes : [[Dev/Services/statsmodels|statsmodels]], [[Dev/Services/scipy.stats|scipy.stats]].
- Doc : https://lifelines.readthedocs.io/
