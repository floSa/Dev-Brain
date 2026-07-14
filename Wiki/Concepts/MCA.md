---
galaxie: wiki
type: concept
nom: MCA
alias: [ACM, Analyse des correspondances multiples, Multiple Correspondence Analysis]
categorie: concept/stats
domaines: [data-sci]
tags: [dimensionality-reduction, factor-analysis]
---

# MCA

## Aperçu

- Analyse des correspondances appliquée à **plusieurs variables qualitatives** (questionnaires, enquêtes).
- Généralise la [[CA]] : place individus et modalités sur des axes synthétiques.

## Concepts clés

### Tableau disjonctif complet
- Chaque variable qualitative est codée en indicatrices (0/1), une par modalité.
- MCA = CA appliquée à ce tableau disjonctif (ou au tableau de Burt).

### Modalités et individus
- Une modalité se place au barycentre des individus qui la portent.
- Les modalités rares tirent les axes → les surveiller (inertie gonflée).

### Inertie et corrections
- L'inertie brute sous-estime la qualité des axes ; corrections de Benzécri / Greenacre pour des pourcentages d'inertie plus réalistes.

## Les maths, simplement

- $K$ variables, codage disjonctif $Z$ ($n \times J$, $J$ = nombre total de modalités).
- MCA = CA sur $Z$ : SVD des résidus standardisés du tableau disjonctif.
- Inertie totale $= J/K - 1$ — mécaniquement élevée, d'où les corrections d'inertie.

## En pratique

- Entrée = individus × variables qualitatives (données brutes, pas une contingence).
- Variables quantitatives à intégrer → les discrétiser, ou passer à [[FAMD]].
- Prolonger par un clustering des individus → [[HCPC]].
- Outils : `prince.MCA`, `FactoMineR::MCA`.

## Approches voisines & alternatives

- [[Réduction de dimension]] — la famille.
- [[CA]] — le cas à deux variables, que MCA généralise.
- [[PCA]] — l'équivalent pour des quantitatives.
- [[FAMD]] — quand s'ajoutent des variables continues.
- [[HCPC]] — classer les individus sur les axes de la MCA.

## Pour aller plus loin

- Greenacre & Blasius — *Multiple Correspondence Analysis and Related Methods*.
