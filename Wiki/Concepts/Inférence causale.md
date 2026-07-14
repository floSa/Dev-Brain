---
galaxie: wiki
type: concept
nom: Inférence causale
alias: [causal inference, inférence causale, causalité, DAG, confounding, confondeur, backdoor, propensity score, score de propension]
categorie: concept/stats
domaines: [data-sci]
tags: [causal-inference, statistical-inference]
---

# Inférence causale

## Aperçu

- Estimer l'**effet d'une cause** sur un résultat — pas une corrélation, mais ce qui se passerait si l'on **intervenait** sur la variable de traitement.
- Difficulté irréductible : le **contrefactuel** est inobservable (on ne voit jamais la même unité traitée *et* non traitée). On le reconstruit sous hypothèses explicites.
- Deux langages pour la même question d'identification : les *potential outcomes* (Rubin) et les graphes causaux / DAG (Pearl).

## Concepts clés

### DAG et confounding

- Un **DAG** (graphe orienté acyclique) encode les relations causales supposées entre variables ; il rend les hypothèses lisibles avant tout calcul.
- Un **confondeur** est une cause commune du traitement et du résultat : ignoré, il fabrique une association non causale (corrélation ≠ causalité).
- Exemple : l'âge influe à la fois sur le traitement reçu et sur l'issue → comparer brut traités vs non traités est biaisé.

### Critère du backdoor

- Identifier l'effet de $T$ sur $Y$ suppose de **bloquer tous les chemins « par la porte de derrière »** (backdoor) : les chemins $T \leftarrow \dots \rightarrow Y$ passant par un ancêtre commun.
- Conditionner sur un ensemble de variables satisfaisant le critère backdoor rend l'effet identifiable depuis les données observées.
- Piège : conditionner sur un **collider** (descendant commun) ou un médiateur *ouvre* un chemin au lieu de le fermer — « ajuster toutes les variables » est faux.

### Propensity score

- **Score de propension** : probabilité de recevoir le traitement sachant les covariables, $e(x) = P(T=1 \mid X=x)$.
- Théorème de Rosenbaum-Rubin : conditionner sur le seul score de propension équilibre toutes les covariables → ramène un ajustement multidimensionnel à une seule dimension.
- Usages : matching, pondération inverse (IPW), stratification sur le score.

## Les maths, simplement

- Effet causal moyen (ATE) : $\tau = \mathbb{E}[Y(1) - Y(0)]$ — différence des résultats potentiels avec et sans traitement, sur la population.
- Identification backdoor : si $X$ bloque les chemins backdoor, $\mathbb{E}[Y(1)] = \mathbb{E}_X\big[\mathbb{E}[Y \mid T=1, X]\big]$ — la moyenne ajustée des résultats observés estime le contrefactuel.
- IPW : $\hat\tau = \frac{1}{n}\sum_i \big(\frac{T_i Y_i}{e(X_i)} - \frac{(1-T_i) Y_i}{1 - e(X_i)}\big)$ — repondérer par l'inverse de la propension recrée une pseudo-population randomisée.

## En pratique

- Commencer par **dessiner le DAG** : il décide quoi ajuster (et surtout quoi ne pas ajuster). Les hypothèses d'abord, les estimateurs ensuite.
- Vérifier l'**overlap / positivité** : chaque unité doit avoir une probabilité non nulle des deux traitements, sinon le score de propension explose.
- Les confondeurs **non observés** sont l'angle mort : aucune méthode observationnelle ne les corrige → tester la sensibilité (E-value).
- L'essai **randomisé** ([[A-B testing]]) reste l'étalon : la randomisation casse tous les chemins backdoor par construction. L'observationnel prend le relais quand randomiser est impossible.

## Approches voisines & alternatives

- [[A-B testing]] — randomisation : identification causale sans hypothèse d'absence de confondeur non observé.
- [[Diff-in-Diff]] — quasi-expérience exploitant la variation avant/après croisée aux groupes.
- [[Dev/Services/CausalImpact|CausalImpact]] — contrefactuel prédit par séries temporelles structurelles bayésiennes.
- [[CUPED]] — réduction de variance dans les essais randomisés (efficacité de l'estimation, pas identification).
- Variables instrumentales, régression sur discontinuité, contrôle synthétique — autres stratégies d'identification, selon la source de variation exogène disponible.

## Pour aller plus loin

- Pearl — *Causality* (2009) ; Pearl & Mackenzie — *The Book of Why*.
- Hernán & Robins — *Causal Inference: What If* (référence appliquée, libre en ligne).
- Outils Python : `DoWhy` (DAG → identification → estimation), `EconML` (effets hétérogènes), [[Dev/Services/statsmodels|statsmodels]] pour les régressions sous-jacentes.
- Connexions brain : [[Diff-in-Diff]], [[CUPED]], [[Dev/Services/CausalImpact|CausalImpact]], [[A-B testing]].
