---
galaxie: wiki
type: concept
nom: FAMD
alias: [AFDM, Analyse factorielle de données mixtes, Factor Analysis of Mixed Data]
categorie: concept/stats
domaines: [data-sci]
tags: [dimensionality-reduction, factor-analysis]
---

# FAMD

## Aperçu

- Analyse factorielle pour données **mixtes** : variables continues **et** catégorielles dans la même analyse.
- Combine [[PCA]] (quantitatives) et [[MCA]] (qualitatives) en équilibrant leur influence.

## Concepts clés

### Équilibrage des deux types
- Les quantitatives sont centrées-réduites (comme en PCA).
- Les qualitatives sont codées en indicatrices, pondérées par l'inverse de la fréquence de la modalité (comme en MCA).
- Résultat : aucun type ne domine a priori.

### Une projection commune
- Individus, variables quantitatives (cercle des corrélations) et modalités (barycentres) se lisent dans le même espace.

## Les maths, simplement

- Tableau prétraité : bloc quantitatif centré-réduit + bloc qualitatif en indicatrices pondérées par $1/p_m$ ($p_m$ = proportion de la modalité $m$).
- Chaque variable (quanti ou quali) est normalisée pour contribuer à hauteur de 1 à l'inertie.
- SVD du tableau ainsi pondéré → axes factoriels.

## En pratique

- Le bon choix quand séparer continu et catégoriel ferait perdre de l'information.
- Tout-continu → préférer [[PCA]] ; tout-catégoriel → [[MCA]].
- Variables organisées en groupes thématiques → [[MFA]].
- Outils : `prince.FAMD`, `FactoMineR::FAMD`.

## Approches voisines & alternatives

- [[Réduction de dimension]] — la famille.
- [[PCA]] — la composante quantitative de FAMD.
- [[MCA]] — la composante qualitative de FAMD.
- [[MFA]] — généralise en gérant des groupes de variables.
- [[HCPC]] — clustering sur les composantes de la FAMD.

## Pour aller plus loin

- Pagès (2004), *Analyse factorielle de données mixtes* ; Husson & Pagès (FactoMineR).
