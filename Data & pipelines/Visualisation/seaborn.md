---
role: brique
nom: seaborn
alias: [sns]
pitch: "Surcouche statistique de matplotlib : graphiques soignés en une ligne (distributions, relations, catégories) directement depuis un DataFrame pandas."
categorie: data/viz
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[matplotlib]]"]
complements: []
tags: [dataviz, statistical-viz, static-viz]
url_docs: https://seaborn.pydata.org/
url_repo: https://github.com/mwaskom/seaborn
---

# seaborn

<!-- AUTO:BANDEAU:START -->
> Surcouche statistique de matplotlib : graphiques soignés en une ligne (distributions, relations, catégories) directement depuis un DataFrame pandas.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont ancien · 2024-01-25 |
<!-- AUTO:BANDEAU:END -->

## Définition

Surcouche haut niveau de [[matplotlib]] orientée **statistiques**. Elle prend un `DataFrame`
[[pandas]] et produit une figure soignée en un appel : distributions (`histplot`,
`kdeplot`), relations (`scatterplot`, `lmplot`), catégories (`boxplot`, `violinplot`),
matrices (`heatmap`). L'agrégation, les intervalles de confiance, le mapping couleur et les
facettes sont gérés pour soi. Le résultat reste une figure matplotlib : la touche finale se
fait en récupérant l'`Axes` et en redescendant dans l'API du socle. Depuis la 0.12, une
seconde interface coexiste avec la première, `seaborn.objects`, qui expose une grammaire des
graphiques par couches — il faut en choisir une et s'y tenir.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Visualisation exploratoire **statistique** rapide, directement depuis un DataFrame | Aucune interactivité : la sortie est une image, héritée du socle statique |
| Graphes courants jolis par défaut, sans régler matplotlib à la main | C'est un wrapper : la personnalisation fine oblige à retomber sur l'API matplotlib |
| Facettes (`FacetGrid`, `relplot`) pour décliner un graphe par sous-groupes | `set_theme` modifie l'état matplotlib **partagé** du processus, donc les figures des autres bibliothèques |
| Intervalles de confiance et régressions tracés automatiquement (`lmplot`, `regplot`) | Deux API coexistent — fonctions historiques et `seaborn.objects` — et les mélanger désoriente |
| | Très gros volumes tracés point par point : il faut échantillonner ou agréger en amont |

## Mise en œuvre

- Installation — `uv add seaborn` ; tire matplotlib, pandas et numpy
- Point d'entrée — import Python, `import seaborn as sns` ; entrée naturelle, un DataFrame
- Prérequis — Python ; scipy et statsmodels en option pour certaines statistiques
- Exécution — dans le process appelant, mono-nœud ; rendu statique hérité de matplotlib
- Coût — gratuit, licence BSD-3-Clause ; projet quasi mono-mainteneur, cadence de publication lente

## Écosystème

### Alternatives

- [[matplotlib]] — Socle de la visualisation Python : API impérative bas niveau pour des graphiques statiques entièrement contrôlables (PNG/SVG/PDF), base de presque tout l'écosystème viz.

## Ressources

- Documentation — https://seaborn.pydata.org/
- Dépôt — https://github.com/mwaskom/seaborn

## Voir aussi

- [[Visualisation]] — le hub du dossier
- [[pandas]] — la source de données attendue en entrée
- [[Comparatif - Visualisation]] — ce qui départage les bibliothèques du dossier
