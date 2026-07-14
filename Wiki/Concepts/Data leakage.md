---
galaxie: wiki
type: concept
nom: Data leakage
alias: [fuite de données, fuite d'information, target leakage]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [model-evaluation, supervised, data-leakage]
---

# Data leakage

## Aperçu

- De l'information indisponible au moment de la prédiction se glisse dans l'entraînement → score de validation optimiste qui s'effondre en production.
- Symptôme typique : des performances « trop belles pour être vraies » en validation, suivies d'une déception en production.

## Concepts clés

### Fuite de la cible (*target leakage*)
- Une variable encode (partiellement) la cible ou n'existe qu'**après** elle. Ex. « date de remboursement » pour prédire le défaut de paiement : elle n'est connue qu'une fois le défaut survenu.

### Contamination train → test
- Un prétraitement ajusté sur **tout** le jeu avant le découpage : standardisation, imputation, encodage, sélection de variables, SMOTE. Le test « voit » alors des statistiques du train.
- Règle : `fit` sur le **train seul**, `transform` sur le test. Voir [[Mise à l'échelle]] et [[Ingénierie des caractéristiques]].

### Fuite temporelle
- Utiliser des données du futur pour prédire le passé. Sur séries temporelles, le découpage aléatoire est interdit → validation glissante (*walk-forward*).

### Fuite de groupe
- Des lignes corrélées (même patient, même client, même session) réparties des deux côtés du découpage : le modèle reconnaît le groupe plutôt que d'apprendre. Utiliser un découpage **par groupe**.

## Les maths, simplement

- Pas de formule, une règle : l'estimateur d'erreur n'est non biaisé que si le jeu de test est **strictement indépendant** de tout choix fait sur le train.
- Tout `fit` — paramètres, stats d'échelle, choix de variables, seuils, hyperparamètres — appartient à l'entraînement. Le sortir du pli, ou régler les hyperparamètres sans [[Validation croisée]] **imbriquée**, biaise le score vers le haut.

## En pratique

- Enfermer **tout** le prétraitement dans un `Pipeline` scikit-learn passé à la validation croisée → le `fit` se rejoue à chaque pli.
- Réglage d'hyperparamètres : CV **imbriquée** (*nested*), sinon le score retenu est optimiste.
- Séries temporelles : découpage chronologique (`TimeSeriesSplit`). Groupes : `GroupKFold`.
- Détecter : une variable au pouvoir prédictif quasi parfait est suspecte — auditer sa disponibilité réelle au moment de la prédiction.

## Approches voisines & alternatives

- [[Validation croisée]] — le cadre où la fuite se produit, ou s'évite (pipeline + nested CV).
- [[Ingénierie des caractéristiques]], [[Mise à l'échelle]], [[Encodage des variables catégorielles]] — étapes à n'ajuster que sur le train.
- [[Imbalanced classification]] — rééchantillonner hors du pli d'entraînement est une fuite fréquente.

## Pour aller plus loin

- Kaufman et al. (2012) — *Leakage in Data Mining: Formulation, Detection, and Avoidance*.
- Documentation scikit-learn — *Common pitfalls and recommended practices* (data leakage).
