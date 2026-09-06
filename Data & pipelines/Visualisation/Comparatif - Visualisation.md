---
role: comparatif
nom: Comparatif - Visualisation
categorie: data/viz
tags: [dataviz, static-viz, interactive-viz, declarative-viz]
---

# Comparatif - Visualisation

> On tranche sur : où le graphe est rendu — une image ou un navigateur — et comment on le décrit, primitive par primitive ou par encodages.

![[Comparatif - Visualisation.base]]

## Ce qui départage

- [[matplotlib]] — le **socle** : rendu statique PNG/SVG/PDF et contrôle **au pixel** de chaque composant, ce sur quoi [[seaborn]], le `.plot` de pandas et le rendu statique de bien d'autres libs s'appuient. Deux API mélangées — `pyplot` *stateful* contre l'API objet — un état global qui surprend en boucle, et une verbosité réelle sur des graphes pourtant simples.
- [[seaborn]] — la surcouche **statistique** : un `DataFrame` en entrée, et l'agrégation, les intervalles de confiance et les facettes sont gérés pour soi, la sortie restant une figure matplotlib donc retouchable à la main. Aucune interactivité, et `set_theme` modifie l'état matplotlib **partagé** du processus.
- [[plotly]] — l'interactif **immédiat** : plotly.js dans le navigateur, zoom, survol et sélection sans écrire de JavaScript, et c'est le moteur de rendu de [[Dash]]. Pages HTML lourdes dès qu'il y a beaucoup de figures, export image conditionné à **Kaleido**, et le rendu rame sur beaucoup de points — agréger ou passer en `scattergl`.
- [[bokeh]] — l'interactif **côté serveur** : un serveur Bokeh relie les widgets Python à des callbacks, ce qui donne des dashboards réactifs sans JS, et le rendu est pensé pour rester fluide sur de gros volumes ou du **streaming**. Le modèle de sessions et de callbacks a une courbe plus raide, et il n'y a pas d'export image natif simple.
- [[altair]] — le seul **déclaratif** : on décrit des encodages plutôt qu'un tracé, et la sortie est une spécification **Vega-Lite** réutilisable hors Python. Limite par défaut à **5000 lignes** (`MaxRowsError`), et la personnalisation très fine reste bornée par ce que Vega-Lite expose.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
