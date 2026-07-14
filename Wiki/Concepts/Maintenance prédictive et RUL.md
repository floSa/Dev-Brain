---
galaxie: wiki
type: concept
nom: Maintenance prédictive et RUL
alias: [Maintenance prédictive / RUL, Maintenance prédictive, RUL, Remaining useful life, Durée de vie résiduelle, Pronostic, Predictive maintenance, PdM]
categorie: concept/ts
domaines: [data-sci, mlops]
tags: [timeseries, survival-analysis, regression]
---

# Maintenance prédictive et RUL

## Aperçu

- **Maintenance prédictive** (PdM) : anticiper la défaillance d'un équipement à partir de données de capteurs / de condition, pour intervenir **juste avant** la panne — entre le correctif (réparer après) et le préventif systématique (entretenir au calendrier, souvent trop tôt).
- **RUL** (*Remaining Useful Life*, durée de vie résiduelle) : temps — ou nombre de cycles — restant avant qu'un composant ne puisse plus assurer sa fonction. C'est la grandeur **pronostique** centrale ; sa prédiction par modèle est le cœur quantitatif de la PdM.

## Concepts clés

### Stratégies de maintenance
- **Correctif** (run-to-failure), **préventif** (calendaire / systématique, indépendant de l'état réel), **prédictif / conditionnel** (CBM — basé sur l'état mesuré). La PdM est la branche prédictive : on remplace « tous les X mois » par « quand l'état le justifie ».

### Diagnostic vs pronostic
- **Diagnostic** : détecter et identifier un défaut *présent* (condition monitoring). **Pronostic** : prédire le RUL *futur*. La détection de l'amorce de dégradation relève de la [[Time series anomaly detection]] ; elle déclenche en amont le calcul de RUL.

### Familles d'approche RUL
- **Modèles physiques / de dégradation** : lois d'usure, propagation de fissure (Paris) — précis mais exigent un modèle du mécanisme.
- **Similarité** : comparer la trajectoire de dégradation courante à des historiques *run-to-failure* connus, en déduire le RUL par analogie.
- **Survie / statistique** : modéliser le temps-jusqu'à-panne avec censure (Weibull, hasard, Cox) — cadre directement emprunté à l'analyse de survie.
- **ML / DL** : régression sur fenêtres de capteurs (gradient boosting, Random Forest) ou réseaux séquentiels (LSTM, CNN 1D, Transformers) prédisant le RUL.

### Indice de santé & cible RUL
- Construire un **health index** par fusion de capteurs (PCA, agrégats) pour résumer l'état. La cible RUL est souvent étiquetée en **plateau-puis-linéaire** (*piecewise-linear*) : RUL constant tant que l'unité est saine, décroissance linéaire une fois la dégradation amorcée — convention classique sur C-MAPSS.

### Censure
- La plupart des unités ne sont pas observées jusqu'à la panne (encore en service, retirées). Ces trajectoires **censurées** sont la raison du recours aux méthodes de survie plutôt qu'à une régression naïve.

## Les maths, simplement

- Définition : $\mathrm{RUL}(t) = T_{\text{panne}} - t$ — temps restant à l'instant $t$ avant l'échéance de défaillance.
- **Score asymétrique** (PHM08 / C-MAPSS) : pour une erreur $h = \widehat{\mathrm{RUL}} - \mathrm{RUL}$, le score sur $n$ unités vaut $\sum_i \big(e^{-h_i/13}-1\big)$ si $h_i<0$ (prédiction **précoce**) et $\sum_i \big(e^{h_i/10}-1\big)$ si $h_i\ge 0$ (prédiction **tardive**). La pente plus raide côté tardif pénalise davantage le retard : sous-estimer le risque (prédire trop tard) coûte plus cher qu'un excès de prudence.
- Contraste avec la RMSE, qui pénalise symétriquement : en pronostic, une alerte tardive peut signifier une casse, une alerte précoce seulement une maintenance anticipée.

## En pratique

- **Jeux de référence** : NASA **C-MAPSS** (turboréacteurs simulés, défi PHM08), roulements **FEMTO/PRONOSTIA**, batteries lithium (PCoE). Le RUL y est dérivé de runs jusqu'à la panne.
- **Métriques** : RMSE *et* score asymétrique ; toujours regarder la distribution des erreurs tardives.
- **Pièges** : fuite temporelle (cf. [[Forecasting framing]]) ; choix de l'étiquette RUL (plateau-linéaire vs linéaire pur) qui change tout ; normalisation par **régime de fonctionnement** (un capteur n'a pas le même niveau à pleine charge) ; gestion des trajectoires censurées ; capteurs manquants ou bruités (cf. [[Imputation des valeurs manquantes]]).
- **Outils** : [[Dev/Services/lifelines|lifelines]] pour le cadre survie/censure (Kaplan-Meier, Cox) ; [[Dev/Services/STUMPY|STUMPY]] pour repérer des signatures de dégradation (matrix profile) ; [[Dev/Services/darts|darts]] pour les modèles séquentiels et le backtesting ; gradient boosting / sklearn pour la régression sur features.
- **Validation** : en temporel strict, par [[Walk-forward CV]] — jamais entraîner sur des cycles postérieurs au test.

## Approches voisines & alternatives

- [[Time series anomaly detection]] — détection de l'amorce du défaut ; déclencheur amont du pronostic.
- [[Time series feature engineering]] — lags, fenêtres glissantes, RMS, énergie spectrale : les features capteurs en entrée des modèles RUL.
- [[Forecasting framing]] — cadrage horizon / fuite temporelle, commun à toute prédiction temporelle.
- [[Regression metrics]] — le RUL se pose souvent en régression ; ici une métrique asymétrique dédiée s'y ajoute.
- [[Détection d'outliers multivariée]] — fusion de capteurs et health index, repérage d'états anormaux.
- [[Walk-forward CV]] — protocole d'évaluation honnête en série temporelle.

## Pour aller plus loin

- Saxena, Goebel, Simon & Eklund (2008) — *Damage propagation modeling for aircraft engine run-to-failure simulation* (dataset C-MAPSS, défi PHM08).
- Si, Wang, Hu & Zhou (2011) — *Remaining useful life estimation – A review on the statistical data driven approaches* (EJOR).
- Lei et al. (2018) — *Machinery health prognostics: A systematic review* (Mechanical Systems and Signal Processing).
- NASA Prognostics Center of Excellence (PCoE) — jeux de données prognostics (turbofan, batteries, roulements). Standards ISO 13381 / OSA-CBM.
