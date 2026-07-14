---
galaxie: wiki
type: concept
nom: Mécanismes de données manquantes
alias: [MCAR, MAR, MNAR, missingness, mécanisme du manque, données manquantes, missing data mechanism, Rubin]
categorie: concept/ml
domaines: [data-sci]
tags: [missing-data, feature-engineering]
---

# Mécanismes de données manquantes

## Aperçu

- Classification de Rubin du **pourquoi** une valeur manque : MCAR, MAR, MNAR.
- Le mécanisme décide quelles méthodes d'imputation ou d'analyse restent **non biaisées** : c'est l'hypothèse à poser *avant* de choisir une stratégie de [[Imputation des valeurs manquantes]].

## Concepts clés

### MCAR — Missing Completely At Random
- La probabilité de manquer ne dépend **ni** des valeurs observées **ni** de la valeur manquante. Manque purement aléatoire.
- Cas idéal : supprimer les lignes incomplètes (listwise deletion) ne biaise pas — on ne perd que de la puissance.

### MAR — Missing At Random
- La probabilité de manquer dépend des **valeurs observées**, mais pas de la valeur manquante elle-même (ex. les hommes répondent moins à une question de santé, à âge donné).
- Conditionné sur les autres variables, le manque redevient aléatoire → l'imputation **conditionnelle** (KNN, MICE) est valide.

### MNAR — Missing Not At Random
- La probabilité de manquer dépend de la **valeur manquante** elle-même (les hauts revenus ne se déclarent pas).
- Toute imputation biaise : il faut **modéliser le mécanisme** (modèle de sélection, pattern-mixture) ou apporter de l'information externe.

### Peut-on tester le mécanisme ?
- MCAR est **testable** (test de Little).
- MAR vs MNAR sont **indistinguables** à partir des seules données observées : c'est une **hypothèse de domaine**, pas un test.

## Les maths, simplement

- Soit $R$ l'indicateur de manque ($R=1$ si manquant), $X_{\text{obs}}$ / $X_{\text{mis}}$ les parties observée / manquante.
- **MCAR** : $P(R \mid X) = P(R)$. **MAR** : $P(R \mid X) = P(R \mid X_{\text{obs}})$. **MNAR** : $P(R \mid X)$ dépend encore de $X_{\text{mis}}$.

## En pratique

- Poser le mécanisme **avant** la stratégie : il conditionne la validité de [[Imputation des valeurs manquantes]].
- Ne jamais supprimer aveuglément les lignes incomplètes sans justifier MCAR (sinon biais de sélection).
- Ajouter un **indicateur de manquant** (`add_indicator`) capte une partie de l'information sous MNAR : le manque lui-même est souvent prédictif.
- Imputer **dans le pipeline**, statistiques apprises sur le train seul — sinon [[Data leakage]].

## Approches voisines & alternatives

- [[Dev/Services/missingno|missingno]] — l'outil Python pour visualiser la structure des manquants (matrice, heatmap, dendrogramme de nullité) et poser le mécanisme.
- [[Imputation des valeurs manquantes]] — les méthodes concrètes (médiane, KNN, MICE) dont la validité dépend du mécanisme.
- [[Ingénierie des caractéristiques]] — l'étape englobante du prétraitement.
- [[Data leakage]] — imputer sur tout le jeu plutôt que sur le train seul est une fuite classique.

## Pour aller plus loin

- Rubin (1976) — *Inference and Missing Data* (la classification d'origine).
- Little & Rubin — *Statistical Analysis with Missing Data*.
