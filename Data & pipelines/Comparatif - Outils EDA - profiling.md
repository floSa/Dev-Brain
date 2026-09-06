---
role: comparatif
nom: Comparatif - Outils EDA - profiling
categorie: data/eda
tags: [eda, data-quality, missing-data]
---

# Comparatif - Outils EDA - profiling

> On tranche sur : l'étendue du rapport — tout le jeu, la relation à une cible, ou la seule nullité.

![[Comparatif - Outils EDA - profiling.base]]

## Ce qui départage

- [[ydata-profiling]] — le rapport **exhaustif** en une ligne : par variable (type, distribution, quantiles, manquants, cardinalité), entre variables (Pearson/Spearman/Cramér's V, interactions, doublons), plus une section d'**alertes** automatiques. C'est aussi le seul du lot à profiler un DataFrame **Spark**, depuis la v4. Le prix est en $O(p^2)$ : corrélations et interactions rendent le rapport interminable sur un large jeu — `minimal=True` ou échantillonner.
- [[sweetviz]] — construit autour d'une **variable cible** et de la **comparaison de deux jeux** : `compare` pour train vs test, `compare_intra` pour deux sous-populations séparées par une condition booléenne. C'est le seul à répondre « la distribution a-t-elle bougé ? ». Pensé pour du tabulaire de taille raisonnable — passer `pairwise_analysis="off"` au-delà de quelques dizaines de colonnes.
- [[missingno]] — un seul problème, la **nullité**, mais quatre vues dessus : `matrix` (motifs ligne à ligne), `bar` (complétude par colonne), `heatmap` (corrélation de nullité) et `dendrogram` (colonnes qui manquent ensemble). C'est ce qui distingue un manque aléatoire d'un manque **structuré**. La `matrix` **échantillonne** au-delà d'un certain nombre de lignes : ne pas lire un motif partiel comme exhaustif.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
