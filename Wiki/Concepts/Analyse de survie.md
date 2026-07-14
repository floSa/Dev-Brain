---
galaxie: wiki
type: concept
nom: Analyse de survie
alias: [survival analysis, time-to-event, analyse de survie, Kaplan-Meier, Cox, risques proportionnels, hazard, censure]
categorie: concept/stats
domaines: [data-sci]
tags: [survival-analysis, regression, non-parametric]
---

# Analyse de survie

## Aperçu

- Modéliser le **temps jusqu'à un événement** (décès, panne, churn, conversion), pas seulement son occurrence.
- Spécificité irréductible : la **censure** — pour certains sujets, l'événement n'est pas observé sur la fenêtre d'étude (encore en vie, encore client). Les jeter ou les traiter comme « sans événement » biaise tout.
- Répond à des questions que la régression classique gère mal : « quelle proportion survit au-delà de $t$ ? », « quel facteur accélère l'événement ? ».

## Concepts clés

### Censure

- **Censure à droite** (la plus courante) : on sait seulement que l'événement n'a pas eu lieu avant la fin du suivi.
- L'information partielle d'un sujet censuré est exploitée jusqu'à sa date de censure — pas jetée. C'est ce qui distingue la discipline.
- Variantes : censure à gauche, par intervalle ; troncature.

### Fonction de survie et de risque

- **Fonction de survie** $S(t) = P(T > t)$ : probabilité de « tenir » au-delà de $t$, décroissante de 1 à 0.
- **Fonction de risque** (hazard) $h(t)$ : taux instantané d'événement en $t$ sachant qu'on y est parvenu. C'est l'objet que modélisent Cox et les modèles paramétriques.

### Kaplan-Meier

- Estimateur **non paramétrique** de $S(t)$ : produit, à chaque date d'événement, des facteurs $(1 - d_i/n_i)$.
- Donne une courbe de survie en escalier sans hypothèse de forme. Comparaison de groupes par **test du log-rank**.

### Modèle de Cox

- Régression **semi-paramétrique** à risques proportionnels : $h(t \mid x) = h_0(t)\,\exp(\beta^\top x)$.
- Le risque de base $h_0(t)$ reste libre ; seul l'effet des covariables est paramétré. Les $e^{\beta}$ se lisent en **hazard ratios**.
- Hypothèse clé : les risques restent **proportionnels** dans le temps (à vérifier).

## Les maths, simplement

- Lien survie / risque : $S(t) = \exp\big(-\int_0^t h(u)\,du\big)$ — accumuler le risque instantané donne la probabilité de survie.
- Kaplan-Meier : $\hat{S}(t) = \prod_{t_i \le t} \big(1 - \tfrac{d_i}{n_i}\big)$, où $d_i$ = événements en $t_i$ et $n_i$ = sujets encore à risque.
- Cox : $h(t\mid x) = h_0(t)\,e^{\beta^\top x}$, estimé par **vraisemblance partielle** ([[Maximum de vraisemblance|MV]]) qui élimine $h_0(t)$. Un $e^{\beta_j} = 1{,}5$ ⇒ risque +50 % par unité de $x_j$.

## En pratique

- Encoder correctement le couple **(durée, indicateur d'événement 0/1)** : l'oubli de la censure est l'erreur n°1.
- Vérifier l'hypothèse des **risques proportionnels** de Cox (résidus de Schoenfeld) ; si elle casse → modèle stratifié ou AFT paramétrique.
- Kaplan-Meier pour décrire et comparer (log-rank) ; Cox dès qu'il faut ajuster sur des covariables.
- Survie « ML » (Random Survival Forests, gradient boosting de survie) → scikit-survival, au-delà du périmètre de lifelines.

## Approches voisines & alternatives

- [[Dev/Services/lifelines|lifelines]] — l'implémentation Python de référence (Kaplan-Meier, Cox, AFT) avec gestion de la censure.
- [[GLM]] / [[Régression logistique]] — modélisent l'occurrence d'un événement mais ignorent le *temps* et la censure.
- [[Régression linéaire]] — inadaptée telle quelle : ne gère ni la censure ni des durées strictement positives et asymétriques.
- Modèles paramétriques AFT (Weibull, log-normal) — alternative à Cox quand on veut une forme explicite du risque de base.

## Pour aller plus loin

- Klein & Moeschberger — *Survival Analysis* ; Kleinbaum & Klein — *Survival Analysis: A Self-Learning Text*.
- Outils : [[Dev/Services/lifelines|lifelines]] (Python pur), scikit-survival (survie ML), package `survival` (R, référence historique).
- Domaines d'usage : médecine (durée de vie), industrie (fiabilité), product analytics (rétention, churn).
