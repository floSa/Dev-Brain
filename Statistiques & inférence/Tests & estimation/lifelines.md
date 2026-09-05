---
role: brique
nom: lifelines
alias: []
pitch: "Analyse de survie en Python pur — estimateurs non paramétriques (Kaplan-Meier, Nelson-Aalen) et modèles de régression (Cox à risques proportionnels, AFT) pour modéliser le temps jusqu'à un événement avec données censurées."
categorie: stats/inference
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: []
tags: [survival-analysis, regression]
url_docs: https://lifelines.readthedocs.io/
url_repo: https://github.com/CamDavidsonPilon/lifelines
---

# lifelines

<!-- AUTO:BANDEAU:START -->
> Analyse de survie en Python pur — estimateurs non paramétriques (Kaplan-Meier, Nelson-Aalen) et modèles de régression (Cox à risques proportionnels, AFT) pour modéliser le temps jusqu'à un événement avec données censurées.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque d'analyse de survie — le temps jusqu'à un événement : décès, churn, panne,
conversion. Ce qui la distingue d'une régression ordinaire est la **censure**, traitée en
première classe : les sujets dont l'événement n'est pas observé sur la période comptent
quand même, et les ignorer biaise tout. Couvre les estimateurs non paramétriques
(Kaplan-Meier, Nelson-Aalen), le modèle semi-paramétrique de **Cox** à risques
proportionnels et les modèles paramétriques AFT (Weibull, log-normal), avec le test du
log-rank et les diagnostics d'hypothèse. API homogène proche de statsmodels — `fit`,
`predict_*`, `print_summary`.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Estimer une courbe de survie et comparer des groupes — Kaplan-Meier plus test du log-rank | La censure doit être encodée correctement (colonne événement 0/1) : mal posée, elle biaise l'ensemble |
| Mesurer l'effet de covariables sur le risque instantané — régression de Cox | L'hypothèse des risques proportionnels se vérifie (`check_assumptions`, résidus de Schoenfeld) ; sinon, modèle stratifié ou AFT |
| Prévoir une durée de vie ou un temps de panne par un modèle paramétrique AFT | Le format des données change selon le modèle : durée plus événement, ou format long pour covariables variant dans le temps |
| Analyser le churn ou la durée de rétention avec données censurées | Ni gros volume ni GPU — et la survie « machine learning » (Random Survival Forests, boosting de survie) est hors périmètre, côté scikit-survival, absent du brain |

## Mise en œuvre

- Installation — `uv add lifelines`
- Point d'entrée — import Python, `from lifelines import KaplanMeierFitter, CoxPHFitter`
- Prérequis — pandas, NumPy et SciPy ; pur Python, aucune toolchain
- Exécution — dans le process appelant, CPU, mono-nœud, tout en mémoire
- Coût — gratuit, MIT, aucune limite d'usage

## Écosystème

### Alternatives

- Aucune dans le brain : lifelines est la seule bibliothèque d'analyse de survie répertoriée, et son pendant ML, scikit-survival, n'y figure pas encore.

## Ressources

- Documentation — https://lifelines.readthedocs.io/
- Dépôt — https://github.com/CamDavidsonPilon/lifelines

## Voir aussi

- [[Analyse de survie]] — la notion du dossier
- [[Comparatif - Outils stats]] — ce qui départage les outils du dossier
