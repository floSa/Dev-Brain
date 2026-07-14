---
galaxie: wiki
type: concept
nom: Encodage des variables catégorielles
alias: [Encodage catégoriel, Categorical encoding, One-Hot encoding, Target encoding, Weight of Evidence, WoE]
categorie: concept/ml
domaines: [data-sci]
tags: [feature-engineering]
---

# Encodage des variables catégorielles

## Aperçu

- Convertir des variables qualitatives (texte, modalités) en numérique, seul format que la plupart des modèles acceptent.
- Le choix dépend de la cardinalité, de l'ordre éventuel des modalités et du modèle aval.

## Concepts clés

### Nominal vs ordinal
- **Ordinal** (`OrdinalEncoder`) : un entier par modalité, n'a de sens que si un ordre existe (petit < moyen < grand). Sur du nominal, induit un faux ordre — toléré seulement par les arbres.
- **Nominal** : pas d'ordre → One-Hot ou encodage par la cible.

### One-Hot
- Une colonne binaire par modalité (`OneHotEncoder`). Sans hypothèse d'ordre, lisible. Explose en dimension si forte cardinalité (sparsité, coût). Gérer les modalités inconnues au test (`handle_unknown`).

### Target / mean encoding
- Remplace chaque modalité par une statistique de la cible (moyenne) sur cette modalité. Compact, efficace en haute cardinalité.
- **Risque de fuite majeur** : lisser (*smoothing*) vers la moyenne globale et ajuster en validation croisée interne. `TargetEncoder` (scikit-learn ≥ 1.3) fait ce repli automatiquement.

### Weight of Evidence (WoE)
- Cas particulier pour cible binaire, hérité du scoring crédit : $\mathrm{WoE} = \ln\dfrac{P(x \mid y=1)}{P(x \mid y=0)}$. Monotone, interprétable, se marie bien avec la [[Régression logistique]].

## Les maths, simplement

- Target encoding lissé : $\hat{e}_c = \dfrac{n_c\,\bar{y}_c + m\,\bar{y}}{n_c + m}$ — $\bar{y}_c$ moyenne cible de la modalité $c$, $\bar{y}$ moyenne globale, $n_c$ effectif, $m$ force du lissage.
- WoE : $\ln\dfrac{\text{part des positifs}}{\text{part des négatifs}}$ par modalité ; base du calcul de l'*Information Value*.

## En pratique

- Faible cardinalité → One-Hot. Forte cardinalité → target encoding (avec lissage + CV) ou hashing.
- Arbres : tolèrent l'ordinal brut, pas besoin de One-Hot systématique.
- Toujours `fit` l'encodeur sur le train (modalités, moyennes cibles), `transform` le test ; prévoir les modalités inconnues.
- Encoder dans le `ColumnTransformer`, aux côtés des transformations numériques (cf. [[Ingénierie des caractéristiques]]).
- Outils : [[Dev/Services/Scikit-Learn|sklearn.preprocessing]] (`OneHotEncoder`, `OrdinalEncoder`, `TargetEncoder`), [[Dev/Services/category_encoders|category_encoders]] (WoE, James-Stein, hashing…).

## Approches voisines & alternatives

- [[Ingénierie des caractéristiques]] — l'étape englobante.
- [[Régression logistique]] — partenaire naturel du WoE (scoring).
- [[Mise à l'échelle]] — appliquée ensuite aux colonnes numériques.
- [[Imputation des valeurs manquantes]] — traiter les modalités manquantes en amont.

## Pour aller plus loin

- Micci-Barreca (2001) — target encoding par lissage hiérarchique.
- Documentation scikit-learn — *Encoding categorical features*, *TargetEncoder*.
